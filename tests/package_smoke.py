from __future__ import annotations

import importlib
import importlib.util
from pathlib import Path
import py_compile
import sys


def _package_modules(package_root: Path) -> list[tuple[str, Path]]:
    modules: list[tuple[str, Path]] = []
    for source_path in sorted(package_root.rglob("*.py")):
        relative_path = source_path.relative_to(package_root)
        if source_path.name == "__init__.py":
            module_parts = ("rivalika_sdk", *relative_path.parent.parts)
        else:
            module_parts = ("rivalika_sdk", *relative_path.with_suffix("").parts)
        modules.append((".".join(module_parts), source_path))
    return modules


def main() -> int:
    package_spec = importlib.util.find_spec("rivalika_sdk")
    if package_spec is None or package_spec.submodule_search_locations is None:
        print("rivalika_sdk is not installed", file=sys.stderr)
        return 1

    package_root = Path(next(iter(package_spec.submodule_search_locations))).resolve()
    modules = _package_modules(package_root)
    failures: list[str] = []

    for module_name, source_path in modules:
        try:
            py_compile.compile(str(source_path), doraise=True)
        except py_compile.PyCompileError as error:
            failures.append(f"compile {module_name}: {error.msg}")

    for module_name, _ in modules:
        try:
            importlib.import_module(module_name)
        except Exception as error:  # noqa: BLE001 - the smoke test reports every import failure
            failures.append(f"import {module_name}: {type(error).__name__}: {error}")

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1

    print(f"compiled and imported {len(modules)} modules from {package_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
