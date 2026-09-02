from __future__ import annotations

import importlib
import importlib.util
import json
from typing import Any
from uuid import UUID

from rivalika_sdk.api_client import ApiClient
from rivalika_sdk.api.commercial_catalog_api import CommercialCatalogApi
from rivalika_sdk.api.commercial_imports_api import CommercialImportsApi
from rivalika_sdk.configuration import Configuration

API_KEY = "rk_live_test"
IDEMPOTENCY_KEY = "sync-snapshot-42"
PRODUCT_ID = UUID("11111111-1111-4111-8111-111111111111")
IMPORT_ID = UUID("22222222-2222-4222-8222-222222222222")


def generated_model(module_name: str, class_name: str) -> type[Any]:
    qualified_name = f"rivalika_sdk.models.{module_name}"
    assert importlib.util.find_spec(qualified_name) is not None, (
        f"missing generated model {class_name}"
    )
    model_type = getattr(importlib.import_module(qualified_name), class_name)
    package = importlib.import_module("rivalika_sdk")
    assert getattr(package, class_name, None) is model_type, f"missing package export {class_name}"
    return model_type


def api_client() -> ApiClient:
    return ApiClient(Configuration(access_token=API_KEY))


def test_serializes_prepare_upload_with_authentication_and_idempotency() -> None:
    request_type = generated_model(
        "prepare_commercial_import_upload_request", "PrepareCommercialImportUploadRequest"
    )
    api = CommercialImportsApi(api_client())
    serializer = getattr(api, "_prepare_commercial_import_upload_serialize", None)
    assert serializer is not None, "missing prepare_commercial_import_upload"

    method, url, headers, body, post_params = serializer(
        idempotency_key=IDEMPOTENCY_KEY,
        prepare_commercial_import_upload_request=request_type(
            file_name="products.csv",
            content_sha256="a" * 64,
            size_bytes=128,
        ),
        _request_auth=None,
        _content_type=None,
        _headers=None,
        _host_index=0,
    )

    assert method == "POST"
    assert url == "https://api.rivalika.com/api/v1/commercial/imports/prepare-upload"
    assert headers == {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Idempotency-Key": IDEMPOTENCY_KEY,
        "Authorization": f"Bearer {API_KEY}",
        "User-Agent": "OpenAPI-Generator/1.0.0b2/python",
    }
    assert body == {
        "fileName": "products.csv",
        "contentSha256": "a" * 64,
        "sizeBytes": 128,
    }
    assert post_params == []


def test_serializes_authenticated_import_detail_request() -> None:
    api = CommercialImportsApi(api_client())
    serializer = getattr(api, "_get_commercial_import_serialize", None)
    assert serializer is not None, "missing get_commercial_import"

    method, url, headers, body, post_params = serializer(
        import_id=IMPORT_ID,
        _request_auth=None,
        _content_type=None,
        _headers=None,
        _host_index=0,
    )

    assert method == "GET"
    assert url == f"https://api.rivalika.com/api/v1/commercial/imports/{IMPORT_ID}"
    assert headers == {
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}",
        "User-Agent": "OpenAPI-Generator/1.0.0b2/python",
    }
    assert body is None
    assert post_params == []


def test_round_trips_prepare_upload_response() -> None:
    envelope_type = generated_model(
        "commercial_import_prepared_upload_envelope", "CommercialImportPreparedUploadEnvelope"
    )
    wire = {
        "data": {
            "storage_key": "organizations/org_1/imports/upload.csv",
            "upload_url": "https://uploads.example.test/object",
            "upload_headers": {
                "Content-Type": "text/csv",
                "x-amz-checksum-sha256": "checksum",
            },
            "expires_in_seconds": 300,
        }
    }

    model = envelope_type.from_dict(wire)

    assert model is not None
    assert json.loads(model.to_json()) == wire


def test_round_trips_bounded_import_detail_response() -> None:
    envelope_type = generated_model(
        "commercial_import_detail_envelope", "CommercialImportDetailEnvelope"
    )
    wire = {
        "data": {
            "id": str(IMPORT_ID),
            "kind": "products",
            "status": "failed",
            "file_name": "products.csv",
            "dry_run": True,
            "sheet_name": None,
            "total_rows": 2,
            "imported_rows": 1,
            "rejected_rows": 1,
            "last_processed_row": 2,
            "has_error_report": True,
            "failure_summary": "One row needs attention",
            "row_errors": [{"row_number": 2, "message": "Missing SKU"}],
            "row_errors_truncated": False,
            "started_at": "2026-09-02T12:00:00Z",
            "completed_at": "2026-09-02T12:01:00Z",
            "created_at": "2026-09-02T11:59:00Z",
            "updated_at": "2026-09-02T12:01:00Z",
        }
    }

    model = envelope_type.from_dict(wire)

    assert model is not None
    assert json.loads(model.to_json()) == wire


def test_serializes_archive_and_restore_with_authentication_and_idempotency() -> None:
    api = CommercialCatalogApi(api_client())
    for action in ("archive", "restore"):
        serializer = getattr(api, f"_{action}_commercial_product_serialize", None)
        assert serializer is not None, f"missing {action}_commercial_product"

        method, url, headers, body, post_params = serializer(
            idempotency_key=IDEMPOTENCY_KEY,
            product_id=PRODUCT_ID,
            _request_auth=None,
            _content_type=None,
            _headers=None,
            _host_index=0,
        )

        assert method == "POST"
        assert url == f"https://api.rivalika.com/api/v1/commercial/products/{PRODUCT_ID}/{action}"
        assert headers == {
            "Accept": "application/json",
            "Idempotency-Key": IDEMPOTENCY_KEY,
            "Authorization": f"Bearer {API_KEY}",
            "User-Agent": "OpenAPI-Generator/1.0.0b2/python",
        }
        assert body is None
        assert post_params == []


def test_round_trips_product_lifecycle_response() -> None:
    envelope_type = generated_model(
        "commercial_product_lifecycle_envelope", "CommercialProductLifecycleEnvelope"
    )
    wire = {"data": {"product_id": str(PRODUCT_ID), "status": "archived"}}

    model = envelope_type.from_dict(wire)

    assert model is not None
    assert json.loads(model.to_json()) == wire
