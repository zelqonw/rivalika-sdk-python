# Contributing

The API client is generated from `openapi/rivalika-public-api.json` with OpenAPI Generator
7.22.0. Do not hand-edit generated API or model files. Contributions to authentication,
webhook verification, tests, and documentation are welcome through a pull request.

Run `python -m pip install -e . pytest mypy`, `pytest tests`, and the focused mypy command
from `.github/workflows/verify.yml` before submitting a change. Use Conventional Commits.

## Spec sync

The Rivalika monorepo owns the OpenAPI contract. After a qualified `main` build
whose public spec differs from the one committed here (and from any pending
`bot/openapi-sync` branch), its `Sync SDKs` workflow sends an `openapi-updated`
dispatch and waits for `.github/workflows/sync-openapi.yml` to finish; a failed
sync fails that run and reaches the Rivalika ops channel.

`sync-openapi.yml` fetches the spec at the dispatched commit, regenerates with
the pinned generator and opens or updates the single `bot/openapi-sync` pull
request, then starts Verify on it (pull requests opened with `GITHUB_TOKEN` do
not trigger workflows on their own). Maintained `client.py`, `integration.py`, `webhooks.py`, root exports and tests are not
regenerated: when the contract changes their shape, add that change to the bot
pull request before merging.

Self-hosted runners keep their workspaces between jobs, so containers that
write into the checkout run as the runner user (`--user "$(id -u):$(id -g)"`);
with rootless Podman also pass `--userns=keep-id`.

## Live check

`python -m pip install -e . && python scripts/smoke.py` calls read-only endpoints through the generated
client against a running API (`RIVALIKA_BASE_URL`, default production, and
`RIVALIKA_API_KEY`). Run it against a local Rivalika stack before merging a
sync that changes shapes.

## Releases (written for beta.3)

The source OpenAPI version is `1.0.0-beta.3`; Python normalizes its package version
to `1.0.0b3`. Generate using the pinned configuration and templates, then verify a
second generation leaves all tracked and newly generated files unchanged. Maintained
`client.py`, `integration.py`, `webhooks.py`, tests and root exports are deliberately
excluded from generation. New generated model types must also be exported at the root.

Before publishing: run maintained tests/types, build wheel and sdist, run `twine check`,
install the wheel in a clean virtual environment and consume REST responses through
both a generated client and `IntegrationClient`. Record the OpenAPI SHA-256 and exact
artifact hashes alongside Rivalika's validated API release. Never publish a consumer
contract before the producer deployment is available for acceptance testing.

Publication uses the `v1.0.0b3` tag and `.github/workflows/publish.yml` in the GitHub
`release` environment. Configure PyPI trusted publishing for repository
`zelqonw/rivalika-sdk-python`, workflow `publish.yml`, environment `release`; a first
publication may require an owner to register a pending publisher for `rivalika-sdk`.
Keep secrets out of source and release evidence. A built wheel is not a published
release; verify the registry version and a clean registry install afterwards.
