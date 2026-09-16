import csv
import io
import json
import zipfile

import httpx
import pytest
from rivalika_sdk.integration import IntegrationClient, IntegrationError, read_integration_export

ORG = '11111111-1111-4111-8111-111111111111'


def client(handler):
    return IntegrationClient('secret', organization_id=ORG, transport=httpx.MockTransport(handler), sleep=lambda _: None)


def test_pagination_stops_and_preserves_search():
    requests = []
    def handler(request):
        requests.append(request)
        page = int(request.url.params['page'])
        return httpx.Response(200, json={'data': [{'id': str(page)}], 'page': {'total': 2, 'has_more': page == 1}})
    with client(handler) as sdk:
        assert list(sdk.pages('/api/v1/commercial/products', params={'search': '001,2'})) == [{'id': '1'}, {'id': '2'}]
    assert len(requests) == 2
    assert requests[0].url.params['search'] == '001,2'


def test_repeated_or_incomplete_pages_fail():
    for rows, total in [([], 1), ([{'id': 'same'}], 3)]:
        with client(lambda request: httpx.Response(200, json={'data': rows, 'page': {'total': total, 'has_more': True}})) as sdk:
            with pytest.raises(IntegrationError):
                list(sdk.pages('/api/v1/commercial/products'))


def test_only_safe_or_idempotent_requests_retry():
    calls = []
    def handler(request):
        calls.append(request)
        return httpx.Response(503 if len(calls) == 1 else 200, json={'data': {}})
    with client(handler) as sdk:
        sdk.request('POST', '/api/v1/reports', headers={'Idempotency-Key': 'stable'})
        assert len(calls) == 2
        calls.clear()
        with pytest.raises(httpx.HTTPStatusError):
            sdk.request('POST', '/api/v1/reports')
        assert len(calls) == 1


def test_org_attestation_and_download_reject_cross_origin():
    with client(lambda request: httpx.Response(200, json={'data': {'organization_id': 'different', 'download_url': 'https://other.example/file'}})) as sdk:
        with pytest.raises(IntegrationError):
            sdk.attest()
        with pytest.raises(IntegrationError):
            sdk.download('/api/v1/report-runs/id/download')
        with pytest.raises(IntegrationError):
            sdk.request('GET', 'https://other.example/')


def test_machine_export_preserves_exact_amount_and_count():
    row = {'price': '9999999999.1234', 'internal_sku': '001', 'observed_at': '2026-09-01T10:00:00.000Z'}
    csv_content = io.StringIO()
    writer = csv.writer(csv_content)
    writer.writerow(['record_json'])
    writer.writerow([json.dumps(row)])
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w') as archive:
        archive.writestr('integration.csv', csv_content.getvalue())
        archive.writestr('metadata.json', json.dumps({'profile': 'integration_v1', 'organization_id': ORG, 'row_count': 1}))
    assert read_integration_export(output.getvalue(), organization_id=ORG)[1] == (row,)
    with pytest.raises(IntegrationError):
        read_integration_export(output.getvalue(), organization_id='other')


def test_import_resume_does_not_repeat_upload_or_create():
    requests = []
    import_id = '22222222-2222-4222-8222-222222222222'
    detail = {'id': import_id, 'status': 'completed', 'total_rows': 1, 'imported_rows': 1, 'rejected_rows': 0}
    def handler(request):
        requests.append(request)
        return httpx.Response(200, json={'data': detail})
    import hashlib
    content = b'name\na\n'
    with client(handler) as sdk:
        assert sdk.import_csv('products', content, expected_rows=1, dry_run=False, idempotency_key='one', state={
            'sha256': hashlib.sha256(content).hexdigest(), 'dry_run': False, 'import_id': import_id,
        }) == detail
    assert [(req.method, req.url.path) for req in requests] == [('GET', f'/api/v1/commercial/imports/{import_id}')]


def test_import_renews_expired_upload_without_leaking_api_credentials(monkeypatch):
    import_id = '22222222-2222-4222-8222-222222222222'
    dependency = '33333333-3333-4333-8333-333333333333'
    uploads, mutations, saved = [], [], []
    prepared = 0
    def handler(request):
        nonlocal prepared
        if request.url.path.endswith('prepare-upload'):
            prepared += 1
            return httpx.Response(200, json={'data': {'upload_url': f'https://storage.example/upload-{prepared}', 'storage_key': f'prepared-{prepared}', 'upload_headers': {'Content-Type': 'text/csv'}}})
        if request.method == 'POST':
            mutations.append(json.loads(request.content))
            return httpx.Response(202, json={'data': {'id': import_id}})
        return httpx.Response(200, json={'data': {'id': import_id, 'status': 'completed', 'total_rows': 1, 'imported_rows': 1, 'rejected_rows': 0}})
    sdk = client(handler)
    class Uploader:
        def __init__(self, **kwargs):
            assert kwargs['follow_redirects'] is False
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass
        def put(self, url, **kwargs):
            uploads.append(kwargs)
            return httpx.Response(403 if len(uploads) == 1 else 200, request=httpx.Request('PUT', url))
    monkeypatch.setattr(httpx, 'Client', Uploader)
    try:
        sdk.import_csv('supplier_offers', b'name\na\n', expected_rows=1, dry_run=True,
            idempotency_key='stable', progress=saved.append, validation_import_ids=(dependency,))
    finally:
        sdk.close()
    assert prepared == 2 and len(mutations) == 1
    assert mutations[0]['validationImportIds'] == [dependency]
    assert mutations[0]['storageKey'] == 'prepared-2'
    assert all('Authorization' not in upload['headers'] for upload in uploads)
    assert saved[0]['request']['storageKey'] == 'prepared-2'
    assert saved[-1]['result']['rejected_rows'] == 0


def test_authenticated_download_carries_organization_and_bounds_bytes():
    def handler(request):
        assert request.headers['x-organization-id'] == ORG
        if request.url.path.endswith('/download'):
            return httpx.Response(200, json={'data': {'download_url': '/api/v1/artifact'}})
        return httpx.Response(200, content=b'original workbook bytes')
    with client(handler) as sdk:
        assert sdk.download('/api/v1/report-runs/id/download') == b'original workbook bytes'
        with pytest.raises(IntegrationError, match='byte limit'):
            sdk.download('/api/v1/report-runs/id/download', max_bytes=3)
