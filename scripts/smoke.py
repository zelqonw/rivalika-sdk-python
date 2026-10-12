"""Live check that this SDK still talks to a running Rivalika API.

    python -m pip install -e .
    RIVALIKA_BASE_URL=http://localhost:3000 RIVALIKA_API_KEY=... python scripts/smoke.py

Read-only: it lists and reads, it never creates anything. Not part of CI,
because it needs a real API key.
"""

from __future__ import annotations

import asyncio
import os
import sys
from typing import Any, Awaitable, Callable

import rivalika_sdk as sdk


async def import_detail(client: sdk.ApiClient) -> Any:
    """A typed detail model, not a list of plain records: catches a changed
    required field or format that list envelopes would let through."""
    imports = sdk.CommercialImportsApi(client)
    listed = (await imports.list_commercial_imports(size=1)).data
    if not listed:
        return sdk.DataEnvelope(data={})
    return await imports.get_commercial_import(listed[0]["id"])


async def main() -> int:
    base_url = os.environ.get("RIVALIKA_BASE_URL", "https://api.rivalika.md").rstrip("/")
    api_key = os.environ.get("RIVALIKA_API_KEY")
    if not api_key:
        raise SystemExit("RIVALIKA_API_KEY is required")

    async with sdk.ApiClient(sdk.Configuration(host=base_url, access_token=api_key)) as client:
        exports = sdk.ExportsApi(client)
        checks: list[tuple[str, Callable[[], Awaitable[Any]]]] = [
            ("context", lambda: sdk.ContextApi(client).get_context()),
            ("stores", lambda: sdk.StoresApi(client).list_stores(size=5)),
            ("products", lambda: sdk.CatalogApi(client).list_products(size=5)),
            ("exports", lambda: exports.list_exports(limit=5)),
            ("alert rules", lambda: sdk.AlertsApi(client).list_alert_rules(size=5)),
            ("reports", lambda: sdk.ReportsApi(client).list_reports(size=5)),
            ("webhook endpoints", lambda: sdk.WebhooksApi(client).list_webhook_endpoints()),
            ("commercial import detail", lambda: import_detail(client)),
        ]
        # Operations newer than some generated trees: checked when present.
        if hasattr(exports, "list_export_schedules"):
            checks.append(("export schedules", lambda: exports.list_export_schedules()))

        failed = 0
        for name, call in checks:
            try:
                data = (await call()).data
                if data is None:
                    raise ValueError("response has no data envelope")
                if isinstance(data, list):
                    detail = f"{len(data)} item(s)"
                else:
                    fields = data.model_dump(exclude_unset=True) if hasattr(data, "model_dump") else data
                    detail = f"{len(fields)} field(s)"
                print(f"ok    {name}: {detail}")
            except Exception as error:  # noqa: BLE001 - report every check, then fail once
                failed += 1
                status = getattr(error, "status", None)
                print(f"FAIL  {name}: {f'HTTP {status}' if status else error}")

    total = len(checks)
    print(f"{failed} of {total} checks failed against {base_url}" if failed else f"all {total} checks passed against {base_url}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
