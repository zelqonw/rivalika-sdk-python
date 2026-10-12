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
                detail = f"{len(data)} item(s)" if isinstance(data, list) else f"{len(data)} field(s)"
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
