from __future__ import annotations

from pathlib import Path
import subprocess
import sys


def test_all_package_modules_compile_and_import(tmp_path: Path) -> None:
    smoke_test = Path(__file__).with_name("package_smoke.py")
    result = subprocess.run(
        [sys.executable, str(smoke_test)],
        cwd=tmp_path,
        capture_output=True,
        check=False,
        text=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr
