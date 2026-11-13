"""Test per connectar el JSON Schema al CI.

Valida que tots els nodes OKF del repo compleixin l'esquema
definit a 01-cores/okf-core.schema.json.
"""
import json
from pathlib import Path

import jsonschema
import pytest

# Carpetes que el validador exclou (no són nodes OKF)
EXCLUDED_DIRS = {
    "00-documentacio",
    "06-comunitat",
    "tests",
    "03-eines",
    ".git",
    "EINES",
    "node_modules",
}

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "01-cores" / "okf-core.schema.json"


def load_schema():
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        return json.load(f)


def extract_frontmatter(text: str) -> str | None:
    """Extreu el frontmatter YAML d'un fitxer Markdown."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    end = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = i
            break
    if end is None:
        return None
    return "\n".join(lines[1:end])


def find_okf_nodes():
    """Retorna tots els fitxers .md que són nodes OKF (tenen frontmatter)."""
    nodes = []
    for p in REPO_ROOT.rglob("*.md"):
        # Excloure carpetes
        if any(part in EXCLUDED_DIRS for part in p.relative_to(REPO_ROOT).parts):
            continue
        text = p.read_text(encoding="utf-8")
        fm = extract_frontmatter(text)
        if fm:
            nodes.append((p, fm))
    return nodes


def test_schema_valid_per_a_tots_els_nodes():
    """Tots els nodes OKF del repo compleixen el JSON Schema."""
    schema = load_schema()
    nodes = find_okf_nodes()
    assert len(nodes) > 0, "No s'ha trobat cap node OKF"
    errors = []
    for path, fm in nodes:
        try:
            import yaml
            data = yaml.safe_load(fm)
        except yaml.YAMLError as e:
            errors.append(f"{path}: YAML invàlid: {e}")
            continue
        try:
            jsonschema.validate(instance=data, schema=schema)
        except jsonschema.ValidationError as e:
            errors.append(f"{path}: {e.message}")
    assert not errors, "Nodes que no compleixen l'esquema:\n" + "\n".join(errors)