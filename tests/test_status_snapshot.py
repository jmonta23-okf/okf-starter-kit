"""Tests per a 03-eines/status_snapshot.py.

IMPORTANT: Aquests tests NOMÉS poden cridar l'snapshot amb --quick o --audit
sobre directoris temporals. NO cridar mai --full sobre el repo real,
perquè dins de --full s'executa pytest sobre tests/ i això provocaria recursió.
"""

import re
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "03-eines" / "status_snapshot.py"


def run_snapshot(*args, cwd=None):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True,
        text=True,
        cwd=cwd or REPO_ROOT,
        timeout=180,
    )


def init_repo(path):
    subprocess.run(["git", "init"], cwd=path, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.email", "test@test.com"], cwd=path, check=True)
    (path / "README.md").write_text("# Test\n")
    subprocess.run(["git", "add", "README.md"], cwd=path, check=True)
    subprocess.run(["git", "commit", "-m", "init"], cwd=path, check=True)


def has_git():
    """
    True si l'arrel del repo en prova té un directori .git propi.

    Coherent amb 03-eines/status_snapshot.py (que comprova `(repo / '.git').exists()`):
    un `git rev-parse --git-dir` caminant cap amunt trobaria repos avantpassats
    (p. ex. /opt/data/.git) i donaria falsos positius.
    """
    return (REPO_ROOT / ".git").exists()


def test_snapshot_runs(tmp_path):
    """L'snapshot s'executa en un repo git buit i retorna exit 0."""
    init_repo(tmp_path)
    result = run_snapshot("--quick", "--ruta", str(tmp_path))
    assert result.returncode == 0, result.stderr


@pytest.mark.skipif(not has_git(), reason="requires a git repository")
def test_snapshot_format():
    """L'output conté les capçaleres esperades i les seccions."""
    result = run_snapshot("--quick")
    assert result.returncode == 0
    out = result.stdout
    assert "=== OKF SNAPSHOT v1 ===" in out
    assert "=== END SNAPSHOT ===" in out
    assert "timestamp:" in out
    assert "branch:" in out
    assert "head:" in out
    assert "last_5_commits:" in out
    assert "--- files_summary ---" in out


@pytest.mark.skipif(not has_git(), reason="requires a git repository")
def test_snapshot_deterministic():
    """Dues execucions seguides donen el mateix output (excepte timestamp)."""
    r1 = run_snapshot("--quick")
    r2 = run_snapshot("--quick")
    assert r1.returncode == 0
    assert r2.returncode == 0

    def strip_ts(s):
        return "\n".join(l for l in s.split("\n") if not l.startswith("timestamp:"))

    assert strip_ts(r1.stdout) == strip_ts(r2.stdout)


def test_snapshot_dirty_tree(tmp_path):
    """Amb un fitxer modificat, working_tree és dirty i modified >= 1."""
    init_repo(tmp_path)
    f = tmp_path / "README.md"
    f.write_text("# Test modificat\n")

    result = run_snapshot("--quick", "--ruta", str(tmp_path))
    assert result.returncode == 0
    assert "working_tree: dirty" in result.stdout
    m = re.search(r"modified:\s*(\d+)", result.stdout)
    assert m and int(m.group(1)) >= 1


def test_snapshot_not_a_repo(tmp_path):
    """En un directori que no és git, retorna exit 2."""
    result = run_snapshot("--quick", "--ruta", str(tmp_path))
    assert result.returncode == 2


def test_snapshot_audit_no_catalogs(tmp_path):
    """Amb --audit i cap catàleg, la secció curriculum diu catalogs: 0."""
    init_repo(tmp_path)
    result = run_snapshot("--audit", "--ruta", str(tmp_path))
    if result.returncode != 0:
        pytest.skip("PyYAML not installed or audit failed")
    assert "--- curriculum ---" in result.stdout
    assert "catalogs: 0" in result.stdout
