from pathlib import Path
import re


WORKFLOWS = Path(__file__).parents[1] / ".github" / "workflows"
FORK_GUARD = (
    "github.event_name != 'pull_request' || "
    "github.event.pull_request.head.repo.full_name == github.repository"
)


def test_only_registry_publication_uses_a_hosted_signing_runner() -> None:
    for workflow in WORKFLOWS.glob("*.yml"):
        source = workflow.read_text(encoding="utf-8")
        job = ""
        for line in source.splitlines():
            match = re.fullmatch(r"  ([a-z-]+):", line)
            if match:
                job = match.group(1)
            if line.lstrip().startswith("runs-on:"):
                if workflow.name == "publish.yml" and job == "publish":
                    assert line.strip() == "runs-on: ubuntu-latest"
                else:
                    assert "self-hosted" in line, f"{workflow.name}: {line.strip()}"
    publish = (WORKFLOWS / "publish.yml").read_text(encoding="utf-8")
    assert "environment: release" in publish
    assert "id-token: write" in publish
    assert "ref: refs/tags/" in publish
    assert "startsWith(github.ref, 'refs/tags/v')" in publish
    assert 'TAG="${RELEASE_TAG#v}"' in publish
    assert 'if [ "$TAG" != "$META" ]' in publish


def test_pull_request_jobs_do_not_run_fork_code() -> None:
    verify = (WORKFLOWS / "verify.yml").read_text(encoding="utf-8")
    contract = (WORKFLOWS / "discord-contract.yml").read_text(encoding="utf-8")
    assert verify.count(FORK_GUARD) == 3
    assert FORK_GUARD in contract
