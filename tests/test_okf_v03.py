"""
Proves del suport additiu OKF v0.3 (Bloc 1/3) al validador i al JSON Schema.

Cobreix els camps opcionals v0.3 (okf_version, sources, generated, verified,
status, stale_after, superseded_by), les claus d'extensió `x-*`, els timestamps
RFC 3339 (Y054) i la resolució relativa de `superseded_by` (Y055), sense trencar
la retrocompatibilitat (index.md reservat, data YYYY-MM-DD).
"""

import json
import subprocess
import sys
from pathlib import Path

import validar_yaml as v

from conftest import (
    NODE_BASE,
    crear_vault,
    validar_vault,
)

VALIDAR = str(Path(__file__).resolve().parent.parent / "03-eines" / "validar_yaml.py")
SCHEMA_PATH = (
    Path(__file__).resolve().parent.parent / "01-cores" / "okf-core.schema.json"
)


# ---------------------------------------------------------------------------
# (a) index.md reservat: s'ignora a qualsevol nivell, sense exigir-li camps
# ---------------------------------------------------------------------------

def test_index_md_arrel_ignorat_sense_error(tmp_path, codis_error):
    """
    Un index.md a l'arrel no és un node OKF: no ha de donar errors ni exigir
    id:/authors: (sigui sense frontmatter o amb frontmatter incomplet).
    """
    index_sense_fm = "# Índex del vault\n\n- [MOC](./00_MOC.md)\n"
    ruta = crear_vault(tmp_path, {"index.md": index_sense_fm})

    # No apareix entre els fitxers escanejats.
    noms = [Path(r).name for r in v.trobar_fitxers_md(ruta)]
    assert "index.md" not in noms

    # El vault complet valida sense errors (cap Y001 pel fitxer reservat).
    errors = validar_vault(ruta)
    assert codis_error(errors) == []

    # Frontmatter incomplet (sense id ni authors): tampoc no s'exigeix res.
    index_fm_incomplet = (
        "---\n"
        "title: \"Índex del vault\"\n"
        "---\n"
        "# Índex del vault\n"
    )
    (tmp_path / "b").mkdir()
    ruta2 = crear_vault(tmp_path / "b", {"index.md": index_fm_incomplet})
    assert codis_error(validar_vault(ruta2)) == []


# ---------------------------------------------------------------------------
# (b) Camps opcionals v0.3, claus x-* i timestamps RFC 3339 (Y054)
# ---------------------------------------------------------------------------

def _node_v03(nid="EX-GUIA-01", extra=""):
    """Node base amb els camps opcionals v0.3 i una clau d'extensió x-*."""
    node = NODE_BASE.format(nid=nid, tipus="Guia", titol="Guia v0.3")
    node = node.replace(
        "estat: vigent",
        "okf_version: \"0.3\"\n"
        "sources:\n"
        "  - resource: \"https://exemple.cat/curriculum\"\n"
        "generated:\n"
        "  by: \"Agent de generació\"\n"
        "  at: \"2026-11-18T10:30:00Z\"\n"
        "verified:\n"
        "  - by: \"Equip de revisió\"\n"
        "    at: \"2026-11-18T12:45:00+01:00\"\n"
        "status: stable\n"
        "stale_after: \"2027-11-18\"\n"
        "x-miae-1: \"extensió MI-AE\"\n"
        "x-miae-nivell: 3\n"
        "estat: vigent\n"
        + extra,
    )
    return node


def test_camps_v03_i_claus_x_acceptats(tmp_path, codis_error):
    """Camps v0.3 + x-* + timestamps RFC 3339: el node valida sense errors
    i la data YYYY-MM-DD de data_ultima_actualitzacio es manté intacta."""
    node = _node_v03()
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    errors = validar_vault(ruta)
    assert codis_error(errors) == []

    # El frontmatter original conserva la data en format YYYY-MM-DD.
    data, _errs = v.extreure_yaml(Path(ruta) / "03_Guia.md")
    assert data["data_ultima_actualitzacio"] == "2026-10-31"
    assert v.validar_timestamp_rfc3339(data["generated"]["at"])
    assert v.validar_timestamp_rfc3339(data["verified"][0]["at"])

    # També passa la validació en viu del JSON Schema (draft-07).
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    try:
        import jsonschema
    except ImportError:
        return  # jsonschema és opcional als entorns lleugers
    jsonschema.validate(instance=data, schema=schema)


def test_rfc3339_invalid_dona_y054(tmp_path, codis_error):
    """generated.at / verified[].at amb format no RFC 3339 -> Y054 (🟡 Mitjana)."""
    node_ok = _node_v03(nid="EX-GUIA-01")
    node_bad = node_ok.replace('at: "2026-11-18T10:30:00Z"', 'at: "2026-11-18 10:30"')
    ruta = crear_vault(tmp_path, {"03_Guia.md": node_bad})
    errors = validar_vault(ruta)
    assert "Y054" in codis_error(errors)
    assert v.CODIS_ERROR["Y054"][1] == "🟡 Mitjana"

    # verified[].at també es valida (forma de llista).
    (tmp_path / "b").mkdir()
    node_ver = node_ok.replace('at: "2026-11-18T12:45:00+01:00"', 'at: "18/11/2026"')
    ruta2 = crear_vault(tmp_path / "b", {"03_Guia.md": node_ver})
    assert "Y054" in codis_error(validar_vault(ruta2))

    # L'error es limita al timestamp: cap Y008 sobre data_ultima_actualitzacio.
    assert "Y008" not in codis_error(validar_vault(ruta))


def test_rfc3339_accepta_z_i_offset():
    """Tant Z com l'offset horari +HH:MM són RFC 3339 vàlids."""
    assert v.validar_timestamp_rfc3339("2026-11-18T10:30:00Z")
    assert v.validar_timestamp_rfc3339("2026-11-18T10:30:00+01:00")
    assert v.validar_timestamp_rfc3339("2026-11-18T10:30:00.123Z")
    assert not v.validar_timestamp_rfc3339("2026-11-18T10:30:00")
    assert not v.validar_timestamp_rfc3339("2026-11-18")
    assert not v.validar_timestamp_rfc3339("2026-11-18 10:30:00Z")
    assert not v.validar_timestamp_rfc3339("2026-02-30T10:30:00Z")


# ---------------------------------------------------------------------------
# (c) superseded_by: resolució relativa des del directori del node (Y055)
# ---------------------------------------------------------------------------

def test_superseded_by_trencat_dona_error(tmp_path, codis_error):
    """superseded_by amb camí que no resol -> Y055 (🟠 Alta)."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Guia substituïda")
    node = node.replace(
        "estat: vigent",
        "superseded_by: \"./no_existeix.md\"\nestat: vigent",
    )
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    errors = validar_vault(ruta)
    assert "Y055" in codis_error(errors)
    assert v.CODIS_ERROR["Y055"][1] == "🟠 Alta"


def test_superseded_by_valid_passa(tmp_path, codis_error):
    """superseded_by apuntant a un node existent del mateix directori: OK.

    També accepta la forma llista (múltiples successors)."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Guia actual")
    node = node.replace(
        "estat: vigent",
        "superseded_by: \"./01_Convencio.md\"\nestat: vigent",
    )
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    assert codis_error(validar_vault(ruta)) == []


def test_superseded_by_llista_detecta_trencat(tmp_path, codis_error):
    """Llista amb un camí trencat: només el trencat dispara Y055."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Guia substituïda")
    node = node.replace(
        "estat: vigent",
        "superseded_by:\n"
        "  - \"./01_Convencio.md\"\n"
        "  - \"./fantasma.md\"\n"
        "estat: vigent",
    )
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    errors = validar_vault(ruta)
    codis = codis_error(errors)
    assert "Y055" in codis
    assert codis.count("Y055") == 1


def test_superseded_by_extern_no_error(tmp_path, codis_error):
    """Destins externs (URL, mailto:) no es resolen com a camí relatiu."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Guia actual")
    node = node.replace(
        "estat: vigent",
        "superseded_by: \"https://exemple.cat/futur.md\"\nestat: vigent",
    )
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    assert codis_error(validar_vault(ruta)) == []


# ---------------------------------------------------------------------------
# End-to-end: un node v0.3 complet també passa el CLI (exit 0)
# ---------------------------------------------------------------------------

def test_cli_accepta_node_v03_complet(tmp_path):
    """El validador per CLI retorna exit 0 per un node amb tots els camps v0.3."""
    ruta = crear_vault(tmp_path, {"03_Guia.md": _node_v03()})
    proc = subprocess.run(
        [sys.executable, VALIDAR, "--ruta", ruta,
         "--output", str(tmp_path / "inf.md")],
        capture_output=True, text=True, timeout=120,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "Y054" not in proc.stdout
    assert "Y055" not in proc.stdout
