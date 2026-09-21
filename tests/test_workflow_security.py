from pathlib import Path


WORKFLOWS = Path(__file__).parents[1] / ".github" / "workflows"
FORK_GUARD = (
    "github.event_name != 'pull_request' || "
    "github.event.pull_request.head.repo.full_name == github.repository"
)


def test_every_workflow_job_uses_the_self_hosted_pool() -> None:
    for workflow in WORKFLOWS.glob("*.yml"):
        source = workflow.read_text(encoding="utf-8")
        assert "runs-on: ubuntu-" not in source, workflow.name
        for line in source.splitlines():
            if line.lstrip().startswith("runs-on:"):
                assert "self-hosted" in line, f"{workflow.name}: {line.strip()}"


def test_pull_request_jobs_do_not_run_fork_code() -> None:
    verify = (WORKFLOWS / "verify.yml").read_text(encoding="utf-8")
    contract = (WORKFLOWS / "discord-contract.yml").read_text(encoding="utf-8")
    assert verify.count(FORK_GUARD) == 3
    assert FORK_GUARD in contract
