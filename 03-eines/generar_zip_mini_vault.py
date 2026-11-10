#!/usr/bin/env python3
"""Genera el ZIP del mini-vault (05-exemples-minims/vault-de-3-nodes/)."""
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "05-exemples-minims" / "vault-de-3-nodes"
DST = REPO / "05-exemples-minims" / "vault-de-3-nodes.zip"

def main():
    if not SRC.is_dir():
        print(f"Error: no existeix {SRC}")
        return 1
    with zipfile.ZipFile(DST, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(SRC.iterdir()):
            if f.is_file() and not f.name.startswith("."):
                zf.write(f, f.name)
    print(f"ZIP creat: {DST} ({DST.stat().st_size} bytes)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())