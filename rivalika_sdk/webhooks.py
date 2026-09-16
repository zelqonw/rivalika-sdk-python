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


def verify_webhook_envelope(secret: str, payload: bytes, headers: Mapping[str, str], *,
                            organization_id: str, event_types: set[str], now: int | None = None) -> dict[str, Any]:
    """Verify signature and the versioned, organization-bound event identity."""
    from uuid import UUID
    event = parse_and_verify_webhook(secret, payload, headers, now=now)
    if not isinstance(event, dict) or event.get("api_version") != "v1":
        raise WebhookVerificationError("Unsupported webhook envelope version")
    try:
        identity = str(UUID(str(event.get("id", ""))))
        organization = str(UUID(str(event.get("organization_id", ""))))
    except ValueError as exc:
        raise WebhookVerificationError("Invalid webhook envelope identity") from exc
    if identity != headers.get("webhook-id") or organization != str(UUID(organization_id)):
        raise WebhookVerificationError("Webhook organization or event identity mismatch")
    if event.get("type") not in event_types or not isinstance(event.get("data"), dict):
        raise WebhookVerificationError("Unsupported webhook event")
    return event
