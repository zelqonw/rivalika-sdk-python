"""Maintained helpers for bounded integrations using the official v1 contract.

These helpers complement generated operation clients. Progress callbacks may persist
state before a remote mutation, allowing imports to resume after a process restart.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import time
import uuid
import zipfile
from collections.abc import Callable, Iterator, Mapping
from typing import Any
from urllib.parse import urljoin, urlsplit

import httpx
from rivalika_sdk.client import RivalikaClient


class IntegrationError(RuntimeError):
    """A response cannot be safely used as a complete integration capture."""


class IntegrationClient(RivalikaClient):
    def __init__(self, api_key: str, base_url: str = "https://api.rivalika.md", *,
                 organization_id: str, transport: httpx.BaseTransport | None = None,
                 sleep: Callable[[float], None] = time.sleep, attempts: int = 4) -> None:
        super().__init__(api_key, base_url, transport=transport)
        self.organization_id = str(uuid.UUID(organization_id))
        self._sleep = sleep
        if attempts < 1 or attempts > 10:
            raise ValueError("attempts must be between 1 and 10")
        self._attempts = attempts
        self._base_url = base_url.rstrip("/")

    def __enter__(self) -> IntegrationClient:
        return self

    def request(self, method: str, path: str, **kwargs: Any) -> httpx.Response:
        target = urlsplit(urljoin(self._base_url + "/", path))
        if (target.scheme, target.netloc) != (urlsplit(self._base_url).scheme, urlsplit(self._base_url).netloc):
            raise IntegrationError("Authenticated requests must remain on the configured API origin")
        headers = {"X-Organization-Id": self.organization_id, **kwargs.pop("headers", {})}
        retryable = method.upper() in {"GET", "HEAD"} or any(k.lower() == "idempotency-key" for k in headers)
        for attempt in range(self._attempts):
            try:
                response = self._client.request(method, path, headers=headers, follow_redirects=False, **kwargs)
                if response.is_redirect:
                    raise IntegrationError("Unexpected API redirect")
                response.raise_for_status()
                return response
            except httpx.HTTPStatusError as exc:
                if not retryable or exc.response.status_code not in {429, 502, 503, 504} or attempt + 1 == self._attempts:
                    raise
                retry_after = exc.response.headers.get("Retry-After", "")
                delay = min(60.0, float(retry_after)) if retry_after.isdigit() else min(2 ** attempt, 30)
            except httpx.TransportError:
                if not retryable or attempt + 1 == self._attempts:
                    raise
                delay = min(2 ** attempt, 30)
            self._sleep(delay)
        raise IntegrationError("Request attempts exhausted")

    def attest(self, *, forbidden_scopes: tuple[str, ...] = ()) -> dict[str, Any]:
        context = self.data("GET", "/api/v1/context")
        if context.get("organization_id") != self.organization_id:
            raise IntegrationError("API credential organization does not match configuration")
        if set(context.get("scopes", ())).intersection(forbidden_scopes):
            raise IntegrationError("API credential has forbidden scopes")
        return context

    def data(self, method: str, path: str, **kwargs: Any) -> dict[str, Any]:
        value = self.request(method, path, **kwargs).json().get("data")
        if not isinstance(value, dict):
            raise IntegrationError("Expected an object response envelope")
        return value

    def pages(self, path: str, *, params: Mapping[str, Any] | None = None,
              max_pages: int = 10000, cursor: bool = False) -> Iterator[dict[str, Any]]:
        query = dict(params or {})
        query.setdefault("limit" if cursor else "size", 100)
        seen: set[str] = set()
        expected: int | None = None
        received = 0
        for number in range(1, max_pages + 1):
            if not cursor:
                query["page"] = number
            value = self.request("GET", path, params=query).json()
            rows, page = value.get("data"), value.get("page")
            if not isinstance(rows, list) or not isinstance(page, dict) or not isinstance(page.get("has_more"), bool):
                raise IntegrationError("Invalid pagination envelope")
            total = page.get("total")
            if not isinstance(total, int) or isinstance(total, bool) or total < 0:
                raise IntegrationError("Missing expected pagination count")
            if expected is None:
                expected = total
            if total != expected:
                raise IntegrationError("Collection changed during pagination; retry a complete capture")
            for row in rows:
                if not isinstance(row, dict):
                    raise IntegrationError("Invalid collection row")
                identity = str(row.get("id") or hashlib.sha256(json.dumps(row, sort_keys=True).encode()).hexdigest())
                if identity in seen:
                    raise IntegrationError("Repeated pagination row")
                seen.add(identity)
                received += 1
                yield row
            if not page["has_more"]:
                if received != expected:
                    raise IntegrationError("Collection count mismatch")
                return
            if not rows:
                raise IntegrationError("Empty page claims more results")
            if cursor:
                next_cursor = page.get("next_cursor")
                if not next_cursor or next_cursor == query.get("cursor"):
                    raise IntegrationError("Missing or repeated cursor")
                query["cursor"] = next_cursor
        raise IntegrationError("Pagination exceeded the bounded page limit")

    def poll(self, path: str, *, timeout: float = 1800, interval: float = 2) -> dict[str, Any]:
        deadline = time.monotonic() + timeout
        while True:
            detail = self.data("GET", path)
            if detail.get("status") in {"completed", "succeeded", "ready", "failed", "cancelled", "expired"}:
                return detail
            if time.monotonic() >= deadline:
                raise TimeoutError("Remote operation is still running; resume using its persisted ID")
            self._sleep(interval)

    def import_csv(self, kind: str, content: bytes, *, expected_rows: int, dry_run: bool,
                   idempotency_key: str, state: dict[str, Any] | None = None,
                   progress: Callable[[dict[str, Any]], None] | None = None,
                   validation_import_ids: tuple[str, ...] = ()) -> dict[str, Any]:
        if not 1 <= expected_rows <= 5000 or not 0 < len(content) <= 25 * 1024 * 1024:
            raise ValueError("Import chunk exceeds its row or byte limit")
        if validation_import_ids and not dry_run:
            raise ValueError("Validation dependencies require dry_run")
        dependencies = [str(uuid.UUID(value)) for value in validation_import_ids]
        current = dict(state or {})
        identity = hashlib.sha256(content).hexdigest()
        if current and (current.get("sha256") != identity or current.get("dry_run") is not dry_run or current.get("validation_import_ids", []) != dependencies):
            raise IntegrationError("Import resume state belongs to different content or mode")
        def save() -> None:
            if progress is not None:
                progress(dict(current))
        current.update(sha256=identity, dry_run=dry_run, expected_rows=expected_rows, validation_import_ids=dependencies)
        if not current.get("import_id"):
            if not current.get("request"):
                file_name = f"{kind}-{identity}.csv"
                # An expired prepared URL is renewed with a fresh prepare key before create.
                for upload_attempt in range(2):
                    upload = self.data("POST", "/api/v1/commercial/imports/prepare-upload",
                        headers={"Idempotency-Key": f"{idempotency_key}-upload-{uuid.uuid4()}"},
                        json={"fileName": file_name, "contentSha256": identity, "sizeBytes": len(content)})
                    url = urlsplit(upload["upload_url"])
                    if url.scheme != "https" or url.username or url.password:
                        raise IntegrationError("Invalid upload URL")
                    # A separate client ensures the API credential is never sent to storage.
                    with httpx.Client(timeout=120, follow_redirects=False) as uploader:
                        response = uploader.put(upload["upload_url"], content=content, headers=upload["upload_headers"])
                    if response.status_code in {401, 403} and upload_attempt == 0:
                        continue
                    response.raise_for_status()
                    if response.is_redirect:
                        raise IntegrationError("Unexpected upload redirect")
                    break
                current["request"] = {"kind": kind, "fileName": file_name, "storageKey": upload["storage_key"],
                    "contentSha256": identity, "sizeBytes": len(content), "dryRun": dry_run, "autoMatchEnabled": False, "validationImportIds": dependencies}
                save()
            accepted = self.data("POST", "/api/v1/commercial/imports", json=current["request"],
                                 headers={"Idempotency-Key": idempotency_key})
            current["import_id"] = accepted["id"]
            save()
        detail = self.poll(f"/api/v1/commercial/imports/{uuid.UUID(current['import_id'])}")
        current["result"] = detail
        save()
        if detail.get("status") != "completed" or detail.get("rejected_rows") != 0 or detail.get("total_rows") != expected_rows or detail.get("imported_rows") != expected_rows:
            raise IntegrationError("Import did not accept every expected row; inspect persisted import results")
        return detail

    def download(self, endpoint: str, *, max_bytes: int = 100 * 1024 * 1024) -> bytes:
        descriptor = self.data("GET", endpoint)
        url = descriptor.get("download_url")
        if not isinstance(url, str):
            raise IntegrationError("Missing authenticated download URL")
        target = urlsplit(urljoin(self._base_url + "/", url))
        origin = urlsplit(self._base_url)
        if (target.scheme, target.netloc) != (origin.scheme, origin.netloc):
            raise IntegrationError("Download must use the authenticated API origin")
        with self._client.stream("GET", url, headers={"X-Organization-Id": self.organization_id}, follow_redirects=False) as response:
            response.raise_for_status()
            if response.is_redirect:
                raise IntegrationError("Unexpected download redirect")
            data = bytearray()
            for chunk in response.iter_bytes():
                data.extend(chunk)
                if len(data) > max_bytes:
                    raise IntegrationError("Download exceeds the configured byte limit")
            return bytes(data)

    def export(self, request: Mapping[str, Any], *, idempotency_key: str) -> tuple[dict[str, Any], tuple[dict[str, Any], ...]]:
        accepted = self.data("POST", "/api/v1/exports", json={**request, "profile": "integration_v1", "format": "csvZip"}, headers={"Idempotency-Key": idempotency_key})
        export_id = str(uuid.UUID(accepted["id"]))
        detail = self.poll(f"/api/v1/exports/{export_id}")
        if detail.get("status") != "ready":
            raise IntegrationError("Export did not complete")
        content = self.download(f"/api/v1/exports/{export_id}/download")
        metadata, rows = read_integration_export(content, organization_id=self.organization_id)
        if metadata.get("export_id") != export_id or metadata.get("dataset") != request.get("dataset"):
            raise IntegrationError("Export identity mismatch")
        return metadata, rows


def read_integration_export(content: bytes, *, organization_id: str, max_uncompressed_bytes: int = 512 * 1024 * 1024) -> tuple[dict[str, Any], tuple[dict[str, Any], ...]]:
    with zipfile.ZipFile(io.BytesIO(content)) as archive:
        if set(archive.namelist()) != {"integration.csv", "metadata.json"} or len(archive.infolist()) != 2:
            raise IntegrationError("Unexpected integration archive entries")
        if sum(item.file_size for item in archive.infolist()) > max_uncompressed_bytes:
            raise IntegrationError("Export exceeds the uncompressed byte limit")
        metadata = json.loads(archive.read("metadata.json"))
        if metadata.get("profile") != "integration_v1" or metadata.get("organization_id") != organization_id:
            raise IntegrationError("Export profile or organization mismatch")
        with archive.open("integration.csv") as source:
            reader = csv.DictReader(io.TextIOWrapper(source, encoding="utf-8"))
            if reader.fieldnames != ["record_json"]:
                raise IntegrationError("Unexpected export columns")
            rows = tuple(json.loads(row["record_json"]) for row in reader)
        if any(not isinstance(row, dict) for row in rows) or len(rows) != metadata.get("row_count"):
            raise IntegrationError("Export count or row mismatch")
        return metadata, rows
