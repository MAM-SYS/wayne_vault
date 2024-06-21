import os
from pathlib import Path
from pathlib import PosixPath
from typing import Iterator, Optional

_default_ignore_finder_dirs = ("venv", "env", ".git", ".idea", "migrations", ".vscode", "__pycache__")


def finder(base_path: Path, suffix: str, file_name: str = None, ignores: Optional[Iterator[str]] = _default_ignore_finder_dirs) -> Iterator[PosixPath]:
    lookup_name: str = (file_name + suffix) if file_name else suffix

    for root, dirs, files in os.walk(base_path, topdown=True):
        if ignores:
            dirs[:] = [d for d in dirs if d not in ignores]
            ignores = []
        for file in files:
            if file.endswith(lookup_name):
                yield PosixPath(root, file)
