"""Small httpx clients for consumers who prefer a generic sync or async surface."""

from __future__ import annotations

from types import TracebackType
from typing import Any, Type

import httpx


class RivalikaClient:
    """Synchronous httpx client with Rivalika API-key authentication."""

    def __init__(self, api_key: str, base_url: str = "https://api.rivalika.md", *, transport: httpx.BaseTransport | None = None) -> None:
        self._client = httpx.Client(
            transport=transport,
            base_url=base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30.0,
        )

    def request(self, method: str, path: str, **kwargs: Any) -> httpx.Response:
        response = self._client.request(method, path, **kwargs)
        response.raise_for_status()
        return response

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "RivalikaClient":
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()


class AsyncRivalikaClient:
    """Asynchronous httpx client with Rivalika API-key authentication."""

    def __init__(self, api_key: str, base_url: str = "https://api.rivalika.md") -> None:
        self._client = httpx.AsyncClient(
            base_url=base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30.0,
        )

    async def request(self, method: str, path: str, **kwargs: Any) -> httpx.Response:
        response = await self._client.request(method, path, **kwargs)
        response.raise_for_status()
        return response

    async def close(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> "AsyncRivalikaClient":
        return self

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.close()
