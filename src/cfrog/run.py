import os
import subprocess
from pathlib import Path


def needs_rebuild(input: Path, output: Path) -> bool:
    if not os.path.exists(output):
        return True
    out_mtime = os.path.getmtime(output)
    return os.path.getmtime(input) > out_mtime


def compile(input: Path, output: Path, flags: list[str] = []):
    if not needs_rebuild(input, output):
        return
    cmd = ["g++", str(input)]
    print(" ".join(cmd))
    subprocess.run(cmd, check=True)
