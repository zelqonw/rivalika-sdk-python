# Rivalika Python SDK

Official Python client for Rivalika's `/api/v1` public API, generated from the
committed OpenAPI 3.1 contract with OpenAPI Generator 7.22.0. The package also
includes maintained sync/async HTTP helpers and signed-webhook verification.

This source builds `rivalika-sdk==1.0.0b5` (beta). It includes structured import failure and row-error diagnostics from the current beta.3 API contract. Package versions are independent of the API contract version. Registry publication is performed by the tagged release workflow.

Python 3.9 or newer is supported.

## API client

API keys are server credentials. Keep them outside client-side applications and
source control. The generated API classes provide typed async endpoint access;
the maintained clients provide compact sync and async access when desired.

```python
import os
from rivalika_sdk import RivalikaClient

with RivalikaClient(os.environ["RIVALIKA_API_KEY"]) as client:
    context = client.request("GET", "/api/v1/context").json()
```

Every mutation requires an `Idempotency-Key`. Generated endpoint references
live in [`docs/`](docs/) and the exact generation input is
[`openapi/rivalika-public-api.json`](openapi/rivalika-public-api.json).

## Verify webhooks

Verify the exact raw request body before parsing it. The helper uses a
constant-time signature comparison and rejects timestamps older than five
minutes by default.

```python
from rivalika_sdk import parse_and_verify_webhook

event = parse_and_verify_webhook(
    webhook_secret,
    request_body,
    {
        "webhook-id": webhook_id,
        "webhook-timestamp": webhook_timestamp,
        "webhook-signature": webhook_signature,
    },
)
```

Consumers must also deduplicate `webhook-id` values for their business replay
window.

## Development

```bash
python -m pip install -e . pytest mypy build twine
pytest tests
mypy --follow-imports=skip rivalika_sdk/client.py rivalika_sdk/webhooks.py
python -m build
twine check dist/*
docker run --rm -w /local -v "$PWD:/local" \
  openapitools/openapi-generator-cli:v7.22.0 \
  generate -c openapi-generator-config.json
git diff --exit-code
```

Generated API and model files are not hand-edited. See [CONTRIBUTING](CONTRIBUTING.md)
and [SECURITY](SECURITY.md) for contribution and vulnerability-reporting rules.

## Maintained integration helpers (beta 3)

`rivalika_sdk.integration.IntegrationClient` provides organization attestation,
bounded pagination and retries, resumable CSV imports, polling, authenticated
artifact downloads, and lossless `integration_v1` bulk exports. The default origin
is `https://api.rivalika.md`. Retry state belongs in durable application storage;
never log presigned upload URLs or credentials.

```python
from rivalika_sdk.integration import IntegrationClient

with IntegrationClient(api_key, organization_id=organization_id) as sdk:
    sdk.attest(forbidden_scopes=("repricing:apply",))
    products = tuple(sdk.pages("/api/v1/commercial/products"))
    result = sdk.import_csv("products", csv_bytes, expected_rows=100,
        dry_run=True, idempotency_key="catalog-snapshot-products-chunk-1",
        state=previous_progress, progress=save_progress)
```

Imports accept at most 5,000 rows and 25 MiB per chunk. `validation_import_ids`
may reference successful product/partner dry runs in the same organization;
this validates dependencies for a fresh catalog without commercial writes.
Dry-run and apply must use different idempotency keys. Reuse persisted progress
for interrupted requests; rejected or missing rows raise `IntegrationError` and
remain available in the progress record. Expired upload URLs are renewed.

`export(request, idempotency_key=...)` verifies organization, export identity,
dataset, row count and archive bounds. Decimal strings remain strings. Capture all
required datasets before atomically publishing an application snapshot.
`download(endpoint)` follows only authenticated download descriptors on the API
origin and never forwards an API credential to object storage. Report runs expire
at the source after 14 days; archive completed reports in your application's storage
if longer retention is needed. `verify_webhook_envelope` additionally checks the
organization, API version and signed event identity; persist deduplication separately.
