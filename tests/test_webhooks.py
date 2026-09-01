import base64
import hashlib
import hmac

import pytest

from rivalika_sdk.webhooks import parse_and_verify_webhook, verify_webhook_signature

KEY = b"01234567890123456789012345678901"
SECRET = "whsec_" + base64.urlsafe_b64encode(KEY).decode().rstrip("=")
PAYLOAD = b'{"id":"evt_1","type":"endpoint.test.v1"}'
TIMESTAMP = 1_788_192_000
SIGNATURE = base64.b64encode(
    hmac.new(KEY, b"evt_1." + str(TIMESTAMP).encode() + b"." + PAYLOAD, hashlib.sha256).digest()
).decode()
HEADERS = {
    "webhook-id": "evt_1",
    "webhook-timestamp": str(TIMESTAMP),
    "webhook-signature": "v1," + SIGNATURE,
}


def test_verifies_and_parses_an_authentic_event() -> None:
    assert parse_and_verify_webhook(SECRET, PAYLOAD, HEADERS, now=TIMESTAMP)["id"] == "evt_1"


def test_rejects_payload_tampering() -> None:
    with pytest.raises(ValueError, match="Invalid webhook signature"):
        verify_webhook_signature(SECRET, PAYLOAD + b" ", HEADERS, now=TIMESTAMP)


def test_rejects_replayed_event() -> None:
    with pytest.raises(ValueError, match="outside the replay tolerance"):
        verify_webhook_signature(SECRET, PAYLOAD, HEADERS, now=TIMESTAMP + 301)
