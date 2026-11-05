"""Tests per a l'auditoria curricular del validador (RFC-OKF-02, Fase 3).

Cada test crea un vault temporal petit (catàleg + fitxes), crida el validador
amb --audit i comprova el codi de sortida i l'informe de cobertura.
"""

import subprocess
import sys
from pathlib import Path

import pytest

import validar_yaml as v

VALIDAR = str(Path(__file__).resolve().parent.parent / "03-eines" / "validar_yaml.py")

CONVENCIO = """---
id: TEST-CONV-00
type: ConvencioNomenclatura
title: "Convenció de test"
version: "V1.0-Esborrany"
data_ultima_actualitzacio: "2026-11-02"
authors:
  - "Test"
llicencia: "CC BY-SA 4.0"
tags:
  - okf/test
estat: vigent
---

# Convenció de test

## 2 · Tipus de node vàlids

| Tipus | Descripció breu |
|:---|:---|
| `CatalegCurricular` | Catàleg de RAs i CAs. |
| `FitxaAEA` | Fitxa d'activitat. |
"""


def run_audit(dir_vault, *extra):
    return subprocess.run(
        [sys.executable, VALIDAR, "--ruta", str(dir_vault), "--audit", *extra],
        capture_output=True,
        text=True,
        timeout=120,
    )


def node_cataleg(nid="EX-CAT-00", version="V2.1", criteris=None, ancres_cos=None):
    criteris = criteris or {"RA1": ["1.1", "1.2"]}
    llista = ", ".join(f'"{c}"' for c in criteris["RA1"])
    files = "".join(
        f'| <a id="ca-{c}"></a>{c.replace("-", ".")} | 1a | Desc | A | AEA1 |\n'
        for c in (ancres_cos or ["1-1", "1-2"])
    )
    return (
        "---\n"
        f"id: {nid}\n"
        "type: CatalegCurricular\n"
        'title: "Catàleg de test"\n'
        f'version: "{version}"\n'
        'data_ultima_actualitzacio: "2026-11-02"\n'
        'authors:\n  - "Test"\n'
        'llicencia: "CC BY-SA 4.0"\n'
        'tags:\n  - okf/test\n'
        "estat: vigent\n"
        "criteris:\n"
        f"  RA1: [{llista}]\n"
        "---\n"
        f"# Catàleg de test\n\n## 5 · CAs\n\n{files}\n"
    )


def node_fitxa(nid, codis, cataleg="01_Cataleg.md", versio="V2.1", naturalesa="analitica"):
    llista = "".join(f'  - "{c}"\n' for c in codis)
    return (
        "---\n"
        f"id: {nid}\n"
        "type: FitxaAEA\n"
        'title: "Fitxa de test"\n'
        'version: "V1.0-Esborrany"\n'
        'data_ultima_actualitzacio: "2026-11-02"\n'
        'authors:\n  - "Test"\n'
        'llicencia: "CC BY-SA 4.0"\n'
        'tags:\n  - okf/test\n'
        "estat: vigent\n"
        f'cataleg_referencia: "./{cataleg}"\n'
        f'cataleg_versio: "{versio}"\n'
        f"naturalesa: {naturalesa}\n"
        "criteris_avaluacio:\n"
        f"{llista}"
        "---\n"
        "# Fitxa de test\n"
    )


def test_audit_cobertura_completa(tmp_path):
    """Una AEA que declara tots els CAs del catàleg dona cobertura 100% (exit 0)."""
    (tmp_path / "00_Convencio.md").write_text(CONVENCIO)
    (tmp_path / "01_Cataleg.md").write_text(node_cataleg())
    (tmp_path / "02_AEA.md").write_text(node_fitxa("EX-AEA-01", ["1.1", "1.2"]))
    r = run_audit(tmp_path)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "Verdicte: COBERT" in r.stdout
    assert "CAs orfes: 0" in r.stdout
    assert "CAs inexistents: 0" in r.stdout


def test_audit_criteri_inexistent(tmp_path):
    """Una AEA que declara un CA que no és al catàleg dona error (exit 1)."""
    (tmp_path / "00_Convencio.md").write_text(CONVENCIO)
    (tmp_path / "01_Cataleg.md").write_text(node_cataleg())
    (tmp_path / "02_AEA.md").write_text(node_fitxa("EX-AEA-01", ["1.1", "9.9"]))
    r = run_audit(tmp_path)
    assert r.returncode == 1, r.stdout + r.stderr
    assert "CAs inexistents: 1" in r.stdout
    assert "Verdicte: INCOMPLET" in r.stdout


def test_audit_criteri_orfes(tmp_path):
    """Un CA del catàleg sense cap AEA que l'avaluï dona error (exit 1)."""
    (tmp_path / "00_Convencio.md").write_text(CONVENCIO)
    (tmp_path / "01_Cataleg.md").write_text(node_cataleg())
    (tmp_path / "02_AEA.md").write_text(node_fitxa("EX-AEA-01", ["1.1"]))
    r = run_audit(tmp_path)
    assert r.returncode == 1, r.stdout + r.stderr
    assert "CAs orfes: 1" in r.stdout
    assert "Verdicte: INCOMPLET" in r.stdout


def test_audit_sintesi_no_compta(tmp_path):
    """Una AEA amb naturalesa: sintesi no compta com a cobertura analítica: s'emet
    Y046, la síntesi compta com a 'CAs coberts' i el verdicte és COBERT (Bloc 14g)."""
    (tmp_path / "00_Convencio.md").write_text(CONVENCIO)
    (tmp_path / "01_Cataleg.md").write_text(node_cataleg())
    (tmp_path / "02_AEA.md").write_text(node_fitxa("EX-AEA-01", ["1.1", "1.2"], naturalesa="sintesi"))
    r = run_audit(tmp_path)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "CAs avaluats (analítics): 0" in r.stdout
    assert "CAs coberts: 2" in r.stdout
    assert "CAs orfes: 0" in r.stdout
    assert "Verdicte: COBERT" in r.stdout
    assert "[Y046] CA '1.1' covered only by synthesis AEAs" in r.stdout
    assert "[Y046] CA '1.2' covered only by synthesis AEAs" in r.stdout


def test_audit_mismatch_versio(tmp_path):
    """El mismatch de versió és una mètrica informativa (deprecated): no afecta el veredicte ni l'exit."""
    (tmp_path / "00_Convencio.md").write_text(CONVENCIO)
    (tmp_path / "01_Cataleg.md").write_text(node_cataleg())
    (tmp_path / "02_AEA.md").write_text(node_fitxa("EX-AEA-01", ["1.1", "1.2"], versio="V1.0"))
    r = run_audit(tmp_path)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "Mismatch de versió: 1" in r.stdout
    assert "Verdicte: COBERT" in r.stdout
    r2 = run_audit(tmp_path, "--strict-versio")
    assert r2.returncode == 0, r2.stdout + r2.stderr


def test_strict_versio_noop(tmp_path):
    """
    --strict-versio és un no-op: mateix codi de sortida que sense el flag,
    emet el warning literal en anglès i no converteix el mismatch en error.
    """
    (tmp_path / "00_Convencio.md").write_text(CONVENCIO)
    (tmp_path / "01_Cataleg.md").write_text(node_cataleg())
    (tmp_path / "02_AEA.md").write_text(node_fitxa("EX-AEA-01", ["1.1", "1.2"], versio="V1.0"))
    r = run_audit(tmp_path)
    r2 = run_audit(tmp_path, "--strict-versio")
    assert r.returncode == 0, r.stdout + r.stderr
    assert r2.returncode == r.returncode, r2.stdout + r2.stderr
    assert "--strict-versio is deprecated; version mismatch is always a warning" in r2.stdout
    assert "Verdicte: COBERT" in r2.stdout
    assert "Mismatch de versió: 1" in r2.stdout


def test_audit_coherencia_yaml_ancora(tmp_path):
    """Un CA al frontmatter sense àncora al cos dona error (Y030, exit 1)."""
    (tmp_path / "00_Convencio.md").write_text(CONVENCIO)
    (tmp_path / "01_Cataleg.md").write_text(node_cataleg(ancres_cos=["1-1"]))
    (tmp_path / "02_AEA.md").write_text(node_fitxa("EX-AEA-01", ["1.1", "1.2"]))
    r = run_audit(tmp_path)
    assert r.returncode == 1, r.stdout + r.stderr
    assert "Y030" in r.stdout or "ERROR (Y030/Y031" in r.stdout


@pytest.mark.skip(reason="instruments_per_criteri: fase posterior")
def test_audit_instrument_per_criteri():
    """Un CA sense instrument associat dona warning."""
    pass


# ---------------------------------------------------------------------------
# Bloc 14g: format nou de --audit, Y045 i Y046
# ---------------------------------------------------------------------------

def node_cataleg_amb_afegit():
    """Catàleg amb un CA oficial (1.1) i un CA afegit (codi null, guia X)."""
    return (
        "---\n"
        "id: EX-CAT-00\n"
        "type: CatalegCurricular\n"
        'title: "Catàleg de test"\n'
        'version: "V2.1"\n'
        'data_ultima_actualitzacio: "2026-11-02"\n'
        'authors:\n  - "Test"\n'
        'llicencia: "CC BY-SA 4.0"\n'
        'tags:\n  - okf/test\n'
        "estat: vigent\n"
        "criteris:\n"
        "  RA1:\n"
        '    - codi: "1.1"\n'
        "    - codi: null\n"
        '      guia: "X"\n'
        "      afegit: true\n"
        "---\n"
        "# Catàleg de test\n"
        "## 5 · CAs\n"
        '| 1.1 | 1a | <a id="ca-1-1"></a>Desc | A | AEA |\n'
    )


def test_audit_format_nou(tmp_path):
    """El nou format de --audit inclou les línies noves i elimina 'CAs només a síntesi'."""
    (tmp_path / "00_Convencio.md").write_text(CONVENCIO)
    (tmp_path / "01_Cataleg.md").write_text(node_cataleg())
    (tmp_path / "02_AEA.md").write_text(node_fitxa("EX-AEA-01", ["1.1", "1.2"]))
    r = run_audit(tmp_path)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "CAs coberts:" in r.stdout
    assert "CAs contextualitzats (*):" in r.stdout
    assert "CAs afegits pel docent:" in r.stdout
    assert "CAs només a síntesi:" not in r.stdout


def test_y045_ca_afegit_no_referenciat(tmp_path):
    """Un CA afegit (afegit: true) sense cap FitxaAEA que el referenciï -> Y045 (🟡 Mitjana)."""
    (tmp_path / "00_Convencio.md").write_text(CONVENCIO)
    (tmp_path / "01_Cataleg.md").write_text(node_cataleg_amb_afegit())
    (tmp_path / "02_AEA.md").write_text(node_fitxa("EX-AEA-01", ["1.1"]))
    _linies, _exit_code, errors = v.audit_curricular(str(tmp_path))
    codis = [e[0] for e in errors]
    assert "Y045" in codis
    assert v.CODIS_ERROR["Y045"][1] == "🟡 Mitjana"


def test_y046_ca_nomes_sintesi(tmp_path):
    """Un CA cobert només per fitxes de síntesi -> Y046 (🟡 Mitjana) sense afectar el veredicte."""
    (tmp_path / "00_Convencio.md").write_text(CONVENCIO)
    (tmp_path / "01_Cataleg.md").write_text(node_cataleg())
    (tmp_path / "02_AEA.md").write_text(node_fitxa("EX-AEA-01", ["1.1", "1.2"], naturalesa="sintesi"))
    linies, _exit_code, errors = v.audit_curricular(str(tmp_path))
    codis = [e[0] for e in errors]
    assert "Y046" in codis
    assert v.CODIS_ERROR["Y046"][1] == "🟡 Mitjana"
    assert "Verdicte: COBERT" in "\n".join(linies)


def test_audit_per_cataleg_no_barreja(tmp_path):
    """Dos catàlegs amb el mateix codi: la cobertura d'un NO emmascara l'altre (F1.3)."""
    (tmp_path / "00_Convencio.md").write_text(CONVENCIO)
    # Catàleg A (MP1519): CA 1.1, cobert analíticament per la seva fitxa.
    (tmp_path / "01_Cataleg_A.md").write_text(node_cataleg(
        nid="MP1519-CAT-00", criteris={"RA1": ["1.1"]}, ancres_cos=["1-1"]))
    # Catàleg B (MP1520): CA 1.1 — cap fitxa seva el cobreix.
    (tmp_path / "02_Cataleg_B.md").write_text(node_cataleg(
        nid="MP1520-CAT-00", criteris={"RA1": ["1.1"]}, ancres_cos=["1-1"]))
    (tmp_path / "03_Fitxa_A.md").write_text(node_fitxa("MP1519-AEA-01", ["1.1"], cataleg="01_Cataleg_A.md"))
    (tmp_path / "04_Fitxa_B.md").write_text(node_fitxa("MP1520-AEA-01", [], cataleg="02_Cataleg_B.md"))
    linies, exit_code, errors = v.audit_curricular(str(tmp_path))
    text = "\n".join(linies)
    # A cobert, B incomplet (orfe 1.1), verdicte global incomplet.
    assert "CAs orfes: 1" in text
    assert text.count("Verdicte: COBERT") == 1       # A
    assert "Verdicte: INCOMPLET" in text              # B
    assert exit_code == 1
    codis = [e[0] for e in errors]
    assert "Y045" not in codis
    assert "Y046" not in codis


def test_audit_per_cataleg_y046(tmp_path):
    """Mateix codi en dos catàlegs: només el cobert per síntesi genera Y046 (F1.3)."""
    (tmp_path / "00_Convencio.md").write_text(CONVENCIO)
    (tmp_path / "01_Cataleg_A.md").write_text(node_cataleg(
        nid="MP1519-CAT-00", criteris={"RA1": ["1.1"]}, ancres_cos=["1-1"]))
    (tmp_path / "02_Cataleg_B.md").write_text(node_cataleg(
        nid="MP1520-CAT-00", criteris={"RA1": ["1.1"]}, ancres_cos=["1-1"]))
    (tmp_path / "03_Fitxa_A.md").write_text(node_fitxa("MP1519-AEA-01", ["1.1"], cataleg="01_Cataleg_A.md", naturalesa="sintesi"))
    (tmp_path / "04_Fitxa_B.md").write_text(node_fitxa("MP1520-AEA-01", ["1.1"], cataleg="02_Cataleg_B.md"))
    linies, exit_code, errors = v.audit_curricular(str(tmp_path))
    assert "Verdicte: COBERT" in "\n".join(linies)
    assert exit_code == 0
    y046 = [e for e in errors if e[0] == "Y046"]
    assert len(y046) == 1                                  # només el catàleg A (síntesi)
    assert "MP1519-CAT-00" in y046[0][1]
    assert "MP1520-CAT-00" not in y046[0][1]
    codis = [e[0] for e in errors]
    assert "Y045" not in codis


# ---------------------------------------------------------------------------
# Bloc F1.1: identitat dels CAs afegits (camp `id`)
# ---------------------------------------------------------------------------

def node_cataleg_afegit(oficials=("1.1",), id_afegit=None, guia_afegit="1z", nid="EX-CAT-00"):
    """Catàleg en format nou: CAs oficials + un CA afegit (id opcional), amb àncores pels oficials."""
    parts = [
        "---", f"id: {nid}", "type: CatalegCurricular", 'title: "Catàleg de test"',
        'version: "V2.1"', 'data_ultima_actualitzacio: "2026-11-02"',
        "authors:", '  - "Test"', 'llicencia: "CC BY-SA 4.0"', "tags:", "  - okf/test",
        "estat: vigent", "criteris:", "  RA1:",
    ]
    for c in oficials:
        parts.append(f'    - codi: "{c}"')
    parts.append("    - codi: null")
    if id_afegit is not None:
        parts.append(f'      id: "{id_afegit}"')
    parts.append(f'      guia: "{guia_afegit}"')
    parts.append("      afegit: true")
    parts.append("---")
    parts.append("# Catàleg de test")
    parts.append("## 5 · CAs")
    for c in oficials:
        parts.append(f'| <a id="ca-{c.replace(".", "-")}"></a>{c} | 1a | Desc | A | AEA1 |')
    return "\n".join(parts) + "\n"


def test_y045_ca_afegit_amb_id_referenciat(tmp_path):
    """Un CA afegit amb id referenciat per una fitxa NO genera Y045 (F1.1)."""
    (tmp_path / "00_Convencio.md").write_text(CONVENCIO)
    (tmp_path / "01_Cataleg.md").write_text(node_cataleg_afegit(
        oficials=[], id_afegit="MP1519-CAT-00-RA1-ADD-01"))
    (tmp_path / "02_AEA.md").write_text(node_fitxa("EX-AEA-01", ["MP1519-CAT-00-RA1-ADD-01"]))
    _l, _exit_code, errors = v.audit_curricular(str(tmp_path))
    codis = [e[0] for e in errors]
    assert "Y045" not in codis


def test_y045_ca_afegit_amb_id_no_referenciat(tmp_path):
    """Un CA afegit amb id sense cap fitxa que el referenciï -> Y045 amb l'id."""
    (tmp_path / "00_Convencio.md").write_text(CONVENCIO)
    (tmp_path / "01_Cataleg.md").write_text(node_cataleg_afegit(
        oficials=[], id_afegit="MP1519-CAT-00-RA1-ADD-01"))
    _l, _exit_code, errors = v.audit_curricular(str(tmp_path))
    y045 = [e for e in errors if e[0] == "Y045"]
    assert y045 and "MP1519-CAT-00-RA1-ADD-01" in y045[0][1]


def test_y045_ca_afegit_sense_id(tmp_path):
    """Un CA afegit sense id -> Y045 amb la guia com a identificador (fallback)."""
    (tmp_path / "00_Convencio.md").write_text(CONVENCIO)
    (tmp_path / "01_Cataleg.md").write_text(node_cataleg_afegit(oficials=[], id_afegit=None, guia_afegit="1z"))
    _l, _exit_code, errors = v.audit_curricular(str(tmp_path))
    y045 = [e for e in errors if e[0] == "Y045"]
    assert y045 and "CA '1z'" in y045[0][1]


def test_audit_afegits_no_compten_com_orfs(tmp_path):
    """Els afegits no compten a 'Total CAs al decret' ni a 'CAs orfes' (F1.1)."""
    (tmp_path / "00_Convencio.md").write_text(CONVENCIO)
    (tmp_path / "01_Cataleg.md").write_text(node_cataleg_afegit(
        oficials=["1.1", "1.2"], id_afegit="MP1519-CAT-00-RA1-ADD-01"))
    linies, _exit_code, _errors = v.audit_curricular(str(tmp_path))
    text = "\n".join(linies)
    assert "Total CAs al decret: 2" in text
    assert "CAs orfes: 2" in text
    assert "CAs orfes: 3" not in text


def test_audit_id_inexistent(tmp_path):
    """Una referència a un id que no existeix al catàleg -> CAs inexistents: 1."""
    (tmp_path / "00_Convencio.md").write_text(CONVENCIO)
    (tmp_path / "01_Cataleg.md").write_text(node_cataleg_afegit(oficials=["1.1"], id_afegit=None))
    (tmp_path / "02_AEA.md").write_text(node_fitxa("EX-AEA-01", ["1.1", "MP1519-CAT-00-RA1-ADD-99"]))
    linies, _exit_code, _errors = v.audit_curricular(str(tmp_path))
    text = "\n".join(linies)
    assert "CAs inexistents: 1" in text