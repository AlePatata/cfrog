import os
import subprocess
from pathlib import Path


def needs_rebuild(source: Path, output: Path) -> bool:
    if not os.path.exists(output):
        return True
    out_mtime = os.path.getmtime(output)
    return os.path.getmtime(source) > out_mtime


def build(source: Path, output: Path, compile_command: list[str]):
    if not needs_rebuild(source, output):
        return
    cmd = compile_command + [str(source)]
    print(" ".join(cmd))
    subprocess.run(cmd, check=True)
