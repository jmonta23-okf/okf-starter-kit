"""
Proves del suport additiu OKF v0.3 (Bloc 1/3 + Mini-Brief P0) al validador
i al JSON Schema.

Cobreix els camps opcionals v0.3 (okf_version, sources, generated, verified,
status, stale_after, superseded_by), les claus d'extensió `x-*` (inclosa
l'extensió `x-okfedu-usage-window` per a la finestra d'ús de concepte, camp
diferit de v0.3), els timestamps RFC 3339 complets O dates soles YYYY-MM-DD
(Y054), verified complet (Y056), la resolució relativa i absoluta de
`superseded_by` (Y055) i la seva coherència amb deprecated (Y057), sense trencar
la retrocompatibilitat (index.md reservat, data YYYY-MM-DD, sources[].usage_window
per compatibilitat v0.2).
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

CAMPS_V03_NODE = (
    "okf_version: \"0.3\"\n"
    "sources:\n"
    "  - resource: \"https://exemple.cat/curriculum\"\n"
    "    last_modified: \"2026-06-01T09:00:00Z\"\n"
    "    usage_window:\n"
    "      from: \"2026-09-01T00:00:00Z\"\n"
    "      to: \"2027-06-30T23:59:59Z\"\n"
    "generated:\n"
    "  by: \"Agent de generació\"\n"
    "  at: \"2026-11-18T10:30:00Z\"\n"
    "verified:\n"
    "  - by: \"Equip de revisió\"\n"
    "    at: \"2026-11-18T12:45:00+01:00\"\n"
    "status: stable\n"
    "stale_after: \"2027-11-18T23:59:59Z\"\n"
    "x-okfedu-usage-window:\n"
    "  from: \"2026-09-01T00:00:00Z\"\n"
    "  to: \"2027-06-30T23:59:59Z\"\n"
    "x-miae-1: \"extensió MI-AE\"\n"
    "x-miae-nivell: 3\n"
)


def _node_v03(nid="EX-GUIA-01", extra=""):
    """Node base amb els camps opcionals v0.3 complerts i una clau x-*."""
    node = NODE_BASE.format(nid=nid, tipus="Guia", titol="Guia v0.3")
    node = node.replace("estat: vigent", CAMPS_V03_NODE + "estat: vigent\n" + extra)
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
    assert v.validar_timestamp_rfc3339(data["stale_after"])
    assert v.validar_timestamp_rfc3339(data["sources"][0]["last_modified"])
    assert v.validar_timestamp_rfc3339(data["sources"][0]["usage_window"]["from"])
    assert v.validar_timestamp_rfc3339(data["sources"][0]["usage_window"]["to"])

    # La finestra d'ús a nivell de node es declara amb l'extensió
    # x-okfedu-usage-window (camps diferits de v0.3), no amb usage_window.
    assert data["x-okfedu-usage-window"]["from"] == "2026-09-01T00:00:00Z"
    assert "usage_window" not in data  # ja no és un camp normatiu d'arrel

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
    # La versió final d'OKF v0.3 torna a admetre la data sola YYYY-MM-DD
    # (equivalent a 00:00:00Z UTC).
    assert v.validar_timestamp_rfc3339("2026-11-18")
    # Segueixen sent invàlids: date-time sense zona horària i dates irreals.
    assert not v.validar_timestamp_rfc3339("2026-11-18T10:30:00")
    assert not v.validar_timestamp_rfc3339("2026-11-18 10:30:00Z")
    assert not v.validar_timestamp_rfc3339("2026-02-30T10:30:00Z")
    assert not v.validar_timestamp_rfc3339("2026-02-30")


# ---------------------------------------------------------------------------
# Mini-Brief P0: Y054 estès a stale_after / sources[].last_modified /
# usage_window.from / usage_window.to (mantenint YYYY-MM-DD)
# ---------------------------------------------------------------------------

def test_stale_after_data_sola_valida(tmp_path, codis_error):
    """stale_after amb data sola YYYY-MM-DD (ex: 2027-09-01) és vàlid: a la
    versió final d'OKF v0.3 la data sola equival a 00:00:00Z i NO dispara
    Y054. `data_ultima_actualitzacio` continua acceptant YYYY-MM-DD (Y008)."""
    node = _node_v03()
    node = node.replace('stale_after: "2027-11-18T23:59:59Z"', 'stale_after: "2027-09-01"')
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    errors = validar_vault(ruta)
    assert "Y054" not in codis_error(errors)
    assert "Y008" not in codis_error(errors)


def test_stale_after_datetime_sense_offset_dona_y054(tmp_path, codis_error):
    """stale_after amb date-time sense zona horària (2027-11-18T10:00:00) -> Y054."""
    node = _node_v03()
    node = node.replace('stale_after: "2027-11-18T23:59:59Z"', 'stale_after: "2027-11-18T10:00:00"')
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    errors = validar_vault(ruta)
    assert "Y054" in codis_error(errors)


def test_stale_after_data_irreal_dona_y054(tmp_path, codis_error):
    """stale_after amb una data de calendari inexistent (2026-02-30) -> Y054."""
    node = _node_v03()
    node = node.replace('stale_after: "2027-11-18T23:59:59Z"', 'stale_after: "2026-02-30"')
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    errors = validar_vault(ruta)
    assert "Y054" in codis_error(errors)


def test_last_modified_sense_offset_dona_y054(tmp_path, codis_error):
    """sources[].last_modified sense offset RFC 3339 -> Y054."""
    node = _node_v03()
    node = node.replace('last_modified: "2026-06-01T09:00:00Z"', 'last_modified: "2026-06-01 09:00"')
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    errors = validar_vault(ruta)
    assert "Y054" in codis_error(errors)


def test_usage_window_arrel_diferit_no_dona_y054(tmp_path, codis_error):
    """usage_window a nivell d'arrel de node és un camp DIFERIT de v0.3:
    la finestra d'ús es declara amb l'extensió x-okfedu-usage-window i el
    camp llegat `usage_window` es preserva sense validar (cap Y054)."""
    node = _node_v03()
    node = node.replace(
        "status: stable\n",
        "status: stable\n"
        "usage_window:\n"
        '  from: "01/09/2026"\n'
        '  to: "30/06/2027"\n',
    )
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    errors = validar_vault(ruta)
    codis = codis_error(errors)
    assert "Y054" not in codis
    assert "Y008" not in codis


def test_sources_usage_window_sense_rfc3339_dona_y054(tmp_path, codis_error):
    """sources[].usage_window.from / .to sense RFC 3339/date-only -> Y054
    (compatibilitat v0.2; un per extrem de la finestra de la font)."""
    node = _node_v03()
    node = node.replace(
        '      from: "2026-09-01T00:00:00Z"\n'
        '      to: "2027-06-30T23:59:59Z"\n',
        '      from: "01/09/2026"\n'
        '      to: "30/06/2027"\n',
    )
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    errors = validar_vault(ruta)
    codis = codis_error(errors)
    assert codis.count("Y054") == 2  # un per cada extrem de la finestra de la font


# ---------------------------------------------------------------------------
# Mini-Brief P0: verified complet (Y056)
# ---------------------------------------------------------------------------

def test_verified_sense_at_dona_y056(tmp_path, codis_error):
    """verified[] sense 'at' -> Y056 (🟠 Alta): calen by i at a cada entrada."""
    node = _node_v03()
    node = node.replace('    at: "2026-11-18T12:45:00+01:00"\n', "")
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    errors = validar_vault(ruta)
    assert "Y056" in codis_error(errors)
    assert v.CODIS_ERROR["Y056"][1] == "🟠 Alta"


def test_verified_sense_by_dona_y056(tmp_path, codis_error):
    """verified[] sense 'by' -> Y056."""
    node = _node_v03()
    node = node.replace('  - by: "Equip de revisió"\n', "")
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    errors = validar_vault(ruta)
    assert "Y056" in codis_error(errors)


def test_verified_incompleta_no_dona_y054(tmp_path, codis_error):
    """Una entrada sense at no ha de generar Y054 a més de Y056."""
    node = _node_v03()
    node = node.replace('    at: "2026-11-18T12:45:00+01:00"\n', "")
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    assert "Y054" not in codis_error(validar_vault(ruta))


# ---------------------------------------------------------------------------
# (c) superseded_by: resolució relativa (Y055), absoluta i coherència (Y057)
# ---------------------------------------------------------------------------

def _node_superseded(nid="EX-GUIA-01", titol="Guia substituïda", body=""):
    """Node amb superseded_by i estat: obsolet (coherència Y057 satisfeta)."""
    node = NODE_BASE.format(nid=nid, tipus="Guia", titol=titol)
    node = node.replace(
        "estat: vigent",
        "estat: obsolet\n" + body,
    )
    return node


def test_superseded_by_trencat_dona_error(tmp_path, codis_error):
    """superseded_by amb camí que no resol -> Y055 (🟠 Alta)."""
    node = _node_superseded(body='superseded_by: "./no_existeix.md"\n')
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    errors = validar_vault(ruta)
    assert "Y055" in codis_error(errors)
    assert v.CODIS_ERROR["Y055"][1] == "🟠 Alta"


def test_superseded_by_valid_passa(tmp_path, codis_error):
    """superseded_by apuntant a un node existent del mateix directori: OK.

    També accepta la forma llista (múltiples successors)."""
    node = _node_superseded(titol="Guia actual", body='superseded_by: "./01_Convencio.md"\n')
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    assert codis_error(validar_vault(ruta)) == []


def test_superseded_by_llista_detecta_trencat(tmp_path, codis_error):
    """Llista amb un camí trencat: només el trencat dispara Y055."""
    node = _node_superseded(body=(
        "superseded_by:\n"
        "  - \"./01_Convencio.md\"\n"
        "  - \"./fantasma.md\"\n"
    ))
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    errors = validar_vault(ruta)
    codis = codis_error(errors)
    assert "Y055" in codis
    assert codis.count("Y055") == 1


def test_superseded_by_extern_no_error(tmp_path, codis_error):
    """Destins externs (URL, mailto:) no es resolen com a camí relatiu."""
    node = _node_superseded(titol="Guia actual", body='superseded_by: "https://exemple.cat/futur.md"\n')
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    assert codis_error(validar_vault(ruta)) == []


# ---------------------------------------------------------------------------
# Mini-Brief P0: camins absoluts / des de l'arrel del bundle (Y055)
# ---------------------------------------------------------------------------

def test_superseded_by_absolut_resol_des_de_l_arrel(tmp_path, codis_error):
    """Un camí que comença per '/' es resol des de l'arrel del bundle: si el
    fitxer hi existeix, no hi ha Y055."""
    node = _node_superseded(titol="Guia actual", body='superseded_by: "/01_Convencio.md"\n')
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    assert "Y055" not in codis_error(validar_vault(ruta))


def test_superseded_by_absolut_trencat_dona_error(tmp_path, codis_error):
    """Un camí '/' que no existeix a l'arrel del bundle -> Y055."""
    node = _node_superseded(body='superseded_by: "/no-existeix-a-l-arrel.md"\n')
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    assert "Y055" in codis_error(validar_vault(ruta))


# ---------------------------------------------------------------------------
# Mini-Brief P0: coherència superseded_by <-> deprecated (Y057)
# ---------------------------------------------------------------------------

def test_superseded_by_sense_deprecated_dona_y057(tmp_path, codis_error):
    """superseded_by sense 'status: deprecated' ni 'estat: obsolet' -> Y057
    (🟡 Mitjana), encara que el camí resolgui."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Guia actual")
    node = node.replace(
        "estat: vigent",
        'superseded_by: "./01_Convencio.md"\nestat: vigent',
    )
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    errors = validar_vault(ruta)
    assert "Y057" in codis_error(errors)
    assert v.CODIS_ERROR["Y057"][1] == "🟡 Mitjana"
    assert "Y055" not in codis_error(errors)  # el camí resol: només manca coherència


def test_superseded_by_amb_status_deprecated_passa(tmp_path, codis_error):
    """status: deprecated (OKF) també satisfà la coherència, sense estat: obsolet."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Guia actual")
    node = node.replace(
        "estat: vigent",
        'superseded_by: "./01_Convencio.md"\nstatus: deprecated\nestat: vigent',
    )
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    assert "Y057" not in codis_error(validar_vault(ruta))


def test_superseded_by_amb_estat_obsolet_passa(tmp_path, codis_error):
    """estat: obsolet (perfil) satisfà la coherència."""
    node = _node_superseded(titol="Guia actual", body='superseded_by: "./01_Convencio.md"\n')
    ruta = crear_vault(tmp_path, {"03_Guia.md": node})
    assert "Y057" not in codis_error(validar_vault(ruta))


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
    assert "Y056" not in proc.stdout
    assert "Y057" not in proc.stdout
