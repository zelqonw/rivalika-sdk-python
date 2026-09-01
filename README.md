# Rivalika Python SDK

Official Python client for Rivalika's `/api/v1` public API, generated from the
committed OpenAPI 3.1 contract with OpenAPI Generator 7.22.0. The package also
includes maintained sync/async HTTP helpers and signed-webhook verification.

The beta package name is `rivalika-sdk` and its first approved release will be
`1.0.0b1`. Registry publication is a separate release approval; until that tag
is published, clone this repository and install it with `python -m pip install -e .`.

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
