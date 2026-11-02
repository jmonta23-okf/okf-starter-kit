#!/usr/bin/env python3
"""status_snapshot.py — Genera un snapshot estandarditzat de l'estat del repo OKF.

Read-only per disseny: només llegeix, executa el validador i pytest, i escriu per stdout.

Ús:
    python3 03-eines/status_snapshot.py --quick
    python3 03-eines/status_snapshot.py --full
    python3 03-eines/status_snapshot.py --audit
    python3 03-eines/status_snapshot.py --since abc1234

Modes:
    --quick    Només git (branca, HEAD, working tree, últims 5 commits).
    --full     (per defecte) git + validador + tests + recompte de nodes.
    --audit    --full + auditoria curricular (requereix PyYAML).
    --since R  Afegeix els commits des de R.

Sortida: text pla, delimitat per "=== OKF SNAPSHOT v1 ===" i "=== END SNAPSHOT ===".
Exit: 0 si s'ha generat el snapshot; 2 si la ruta no és un repo git.
"""

import argparse
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

SNAPSHOT_VERSION = "v1"
TIMEOUT = 180
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", ".pytest_cache"}


def run(cmd, cwd=None, timeout=TIMEOUT):
    """Executa una comanda i retorna (exit_code, stdout, stderr)."""
    try:
        r = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "timeout"
    except FileNotFoundError as e:
        return -2, "", str(e)


def parse_frontmatter(text):
    """Retorna el contingut del frontmatter YAML o None."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    return text[3:end]


def iter_md(repo):
    """Itera sobre fitxers .md del repo, saltant directoris ignorats."""
    for md in repo.rglob("*.md"):
        if any(p in md.parts for p in SKIP_DIRS):
            continue
        yield md


def node_types(repo):
    """Retorna Counter de tipus de node detectats als frontmatters."""
    types = Counter()
    for md in iter_md(repo):
        try:
            text = md.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        fm = parse_frontmatter(text)
        if fm is None:
            continue
        for line in fm.split("\n"):
            if line.startswith("type:"):
                t = line.split(":", 1)[1].strip().strip('"').strip("'")
                if t:
                    types[t] += 1
                break
    return types


def git_block(repo, since=None):
    lines = []

    rc, out, _ = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repo)
    lines.append(f"branch: {out.strip() if rc == 0 else 'unknown'}")

    rc, out, _ = run(["git", "log", "-1", "--pretty=format:%h | %an | %s"], cwd=repo)
    lines.append(f"head: {out.strip() if rc == 0 and out.strip() else 'none'}")

    rc, out, _ = run(["git", "status", "--porcelain"], cwd=repo)
    if rc == 0:
        entries = [l for l in out.split("\n") if l.strip()]
        lines.append(f"working_tree: {'dirty' if entries else 'clean'}")
        untracked = sum(1 for l in entries if l.startswith("??"))
        staged = sum(1 for l in entries if len(l) >= 1 and l[0] in "MADRCU")
        modified = sum(1 for l in entries if len(l) >= 2 and l[0] == " " and l[1] == "M")
        lines.append(f"staged: {staged}")
        lines.append(f"modified: {modified}")
        lines.append(f"untracked: {untracked}")

    rc, out, _ = run(
        ["git", "rev-list", "--left-right", "--count", "HEAD...@{u}"], cwd=repo
    )
    if rc == 0:
        parts = out.strip().split()
        lines.append(f"ahead_behind: {parts[0]}/{parts[1]}" if len(parts) == 2 else "ahead_behind: 0/0")
    else:
        lines.append("ahead_behind: n/a")

    lines.append("last_5_commits:")
    rc, out, _ = run(
        ["git", "log", "-5", "--pretty=format:%h | %ad | %s", "--date=short"], cwd=repo
    )
    if rc == 0 and out.strip():
        for line in out.split("\n"):
            if line.strip():
                lines.append(f"  {line}")
    else:
        lines.append("  (no commits)")

    if since:
        lines.append(f"since ({since}):")
        rc, out, _ = run(
            ["git", "log", f"{since}..HEAD", "--pretty=format:%h | %ad | %s", "--date=short"],
            cwd=repo,
        )
        if rc == 0 and out.strip():
            for line in out.split("\n"):
                if line.strip():
                    lines.append(f"  {line}")
        else:
            lines.append("  (no changes or invalid ref)")

    return "\n".join(lines)


def validator_block(repo):
    script = repo / "03-eines" / "validar_yaml.py"
    nt = node_types(repo)
    total_nodes = sum(nt.values())

    if not script.exists():
        return (
            f"exit: 2\nversion: n/a (script not found)\n"
            f"nodes: {total_nodes}\nerrors: n/a\nwarnings: n/a"
        )

    fd, tmp_report = tempfile.mkstemp(prefix="okf_snap_", suffix=".md")
    os.close(fd)
    try:
        rc, out, err = run(
            [sys.executable, str(script), "--ruta", ".", "--output", tmp_report],
            cwd=repo,
        )
    finally:
        try:
            os.unlink(tmp_report)
        except OSError:
            pass
    combined = out + "\n" + err

    version = "unknown"
    m = re.search(r"v\d+\.\d+\.\d+", combined)
    if m:
        version = m.group(0)

    nodes = str(total_nodes)
    m = re.search(r"(\d+)\s+nodes?", combined, re.IGNORECASE)
    if m:
        nodes = m.group(1)

    errors = "n/a"
    for pat in (
        r"Fitxers amb errors\s*\|\s*(\d+)",
        r"Errors\s*\|\s*(\d+)",
        r"(\d+)\s+errors?",
    ):
        m = re.search(pat, combined, re.IGNORECASE)
        if m:
            errors = m.group(1)
            break

    warnings = "n/a"
    for pat in (
        r"Advertències\s*\([^)]*\)\s*\|\s*(\d+)",
        r"Fitxers amb avisos\s*\|\s*(\d+)",
        r"Avisos\s*\|\s*(\d+)",
        r"(\d+)\s+warnings?",
        r"(\d+)\s+avisos?",
    ):
        m = re.search(pat, combined, re.IGNORECASE)
        if m:
            warnings = m.group(1)
            break

    return f"exit: {rc}\nversion: {version}\nnodes: {nodes}\nerrors: {errors}\nwarnings: {warnings}"


def tests_block(repo):
    if not (repo / "tests").exists():
        return "exit: 2\n(skipped: no tests directory)"

    rc, out, err = run(
        [sys.executable, "-m", "pytest", "tests/", "-q", "--tb=no", "--no-header"],
        cwd=repo,
    )
    combined = out + "\n" + err

    passed = failed = skipped = "0"
    duration = "n/a"
    m = re.search(r"(\d+)\s+passed", combined)
    if m:
        passed = m.group(1)
    m = re.search(r"(\d+)\s+failed", combined)
    if m:
        failed = m.group(1)
    m = re.search(r"(\d+)\s+skipped", combined)
    if m:
        skipped = m.group(1)
    m = re.search(r"in\s+([\d.]+)s", combined)
    if m:
        duration = m.group(1) + "s"

    return f"exit: {rc}\npassed: {passed}\nfailed: {failed}\nskipped: {skipped}\nduration: {duration}"


def files_summary(repo):
    total_md = total_py = total_yml = total_files = 0
    for p in repo.rglob("*"):
        if not p.is_file():
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        total_files += 1
        if p.suffix == ".md":
            total_md += 1
        elif p.suffix == ".py":
            total_py += 1
        elif p.suffix in (".yml", ".yaml"):
            total_yml += 1
    return f"total_files: {total_files}\ntotal_md: {total_md}\ntotal_py: {total_py}\ntotal_yml: {total_yml}"


def curriculum_block(repo):
    """Delega l'auditoria al validador (--audit) i n'agrega les mètriques.

    Manté el format de sortida històric (catalogs, total_cas_decret,
    cas_avaluats, cas_orfes, cas_inexistents, version_mismatch) sumant els
    valors per catàleg que emet el validador.
    """
    script = repo / "03-eines" / "validar_yaml.py"
    if not script.exists():
        return (
            "catalogs: 0\n"
            "total_cas_decret: 0\n"
            "cas_avaluats: 0\n"
            "cas_orfes: 0\n"
            "cas_inexistents: 0\n"
            "version_mismatch: 0"
        )

    fd, tmp_report = tempfile.mkstemp(prefix="okf_snap_", suffix=".md")
    os.close(fd)
    try:
        rc, out, err = run(
            [sys.executable, str(script), "--ruta", str(repo), "--audit", "--output", tmp_report],
            cwd=repo,
        )
    finally:
        try:
            os.unlink(tmp_report)
        except OSError:
            pass
    combined = out + "\n" + err

    def suma(pat):
        return sum(int(x) for x in re.findall(pat, combined))

    pat_catalogs = r'Catàlegs analitzats:\s*(\d+)'
    pat_unic_decret = r'CAs únics al decret:\s*(\d+)'
    pat_unic_coberts = r'CAs únics coberts:\s*(\d+)'
    pat_per_cataleg = r'Total CAs al decret:\s*(\d+)'
    pat_orfes = r'CAs orfes:\s*(\d+)'
    pat_inexistents = r'CAs inexistents:\s*(\d+)'
    pat_mismatch = r'Mismatch de versió:\s*(\d+)'

    return (
        f"catalogs: {suma(pat_catalogs)}\n"
        f"total_cas_decret: {suma(pat_unic_decret)}\n"
        f"cas_avaluats: {suma(pat_unic_coberts)}\n"
        f"cas_orfes: {suma(pat_orfes)}\n"
        f"cas_inexistents: {suma(pat_inexistents)}\n"
        f"version_mismatch: {suma(pat_mismatch)}\n"
        f"total_per_cataleg: {suma(pat_per_cataleg)}"
    )


def main():
    parser = argparse.ArgumentParser(
        description="Genera un snapshot estandarditzat de l'estat del repo OKF (read-only)."
    )
    parser.add_argument("--quick", action="store_true", help="Només git, sense validador ni tests")
    parser.add_argument("--full", action="store_true", help="(per defecte) git + validador + tests + node_types")
    parser.add_argument("--audit", action="store_true", help="Afegeix auditoria curricular (requereix PyYAML)")
    parser.add_argument("--since", type=str, default=None, help="Mostra commits des de <ref>")
    parser.add_argument("--ruta", type=str, default=".", help="Ruta del repo (per defecte: .)")
    args = parser.parse_args()

    repo = Path(args.ruta).resolve()
    if not (repo / ".git").exists():
        print(f"ERROR: {repo} no és un repositori git", file=sys.stderr)
        return 2

    print(f"=== OKF SNAPSHOT {SNAPSHOT_VERSION} ===")
    ts = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    print(f"timestamp: {ts}")
    print(f"repo: {repo.name}")
    print(git_block(repo, args.since))

    if not args.quick:
        print("--- validator ---")
        print(validator_block(repo))
        print("node_types:")
        nt = node_types(repo)
        if nt:
            for t, c in sorted(nt.items()):
                print(f"  {t}: {c}")
        else:
            print("  (none)")

        print("--- tests ---")
        print(tests_block(repo))

    if args.audit:
        print("--- curriculum ---")
        print(curriculum_block(repo))

    print("--- files_summary ---")
    print(files_summary(repo))
    print("=== END SNAPSHOT ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
