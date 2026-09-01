"""Verification helpers for Standard Webhooks-compatible Rivalika deliveries."""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import time
from typing import Any, Mapping, cast


class WebhookVerificationError(ValueError):
    """Raised when a webhook signature or replay check fails."""


def _signing_key(secret: str) -> bytes:
    if not secret.startswith("whsec_"):
        raise WebhookVerificationError("Invalid Rivalika webhook signing secret")
    encoded = secret.removeprefix("whsec_")
    return base64.urlsafe_b64decode(encoded + "=" * (-len(encoded) % 4))


def verify_webhook_signature(
    secret: str,
    payload: bytes | str,
    headers: Mapping[str, str],
    *,
    tolerance_seconds: int = 300,
    now: int | None = None,
) -> None:
    raw = payload.encode("utf-8") if isinstance(payload, str) else payload
    message_id = headers.get("webhook-id", "")
    timestamp_raw = headers.get("webhook-timestamp", "")
    signature_header = headers.get("webhook-signature", "")
    try:
        timestamp = int(timestamp_raw)
    except ValueError as error:
        raise WebhookVerificationError("Invalid webhook timestamp") from error
    current = int(time.time()) if now is None else now
    if abs(current - timestamp) > tolerance_seconds:
        raise WebhookVerificationError("Webhook timestamp is outside the replay tolerance")
    signed = message_id.encode() + b"." + str(timestamp).encode() + b"." + raw
    expected = base64.b64encode(hmac.new(_signing_key(secret), signed, hashlib.sha256).digest()).decode()
    candidates = (candidate.partition(",") for candidate in signature_header.split(" "))
    if not any(
        version == "v1" and hmac.compare_digest(encoded, expected)
        for version, separator, encoded in candidates
        if separator
    ):
        raise WebhookVerificationError("Invalid webhook signature")


def parse_and_verify_webhook(
    secret: str,
    payload: bytes | str,
    headers: Mapping[str, str],
    *,
    tolerance_seconds: int = 300,
    now: int | None = None,
) -> dict[str, Any]:
    verify_webhook_signature(
        secret,
        payload,
        headers,
        tolerance_seconds=tolerance_seconds,
        now=now,
    )
    return cast(dict[str, Any], json.loads(payload))
