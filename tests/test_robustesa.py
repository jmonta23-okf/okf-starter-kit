"""
Proves negatives de robustesa del validador (F2.2).

Cada test injecta dades malformades en un node i verifica que el validador
**no llança cap excepció no controlada** (`Traceback`) i que retorna un codi
de sortida coherent (0, 1 o 2), no un crash (ex: -11/139). És la bateria que
blinda el validador contra regressions de robustesa.
"""

import subprocess
import sys
from pathlib import Path

import validar_yaml as v  # noqa: F401  (garanteix que el mòdul sigui importable)

from conftest import CONVENCIO, crear_vault


VALIDAR = str(Path(__file__).resolve().parent.parent / "03-eines" / "validar_yaml.py")

# Convenció que declara CatalegCurricular (idèntica a la de test_validar_yaml.py).
CONV_AMB_CATALEG = CONVENCIO.replace(
    "| `Guia` | Guia d'ús o tutorial. |",
    "| `Guia` | Guia d'ús o tutorial. |\n"
    "| `CatalegCurricular` | Catàleg de RAs i CAs d'un mòdul. |",
)


# ---------------------------------------------------------------------------
# Helpers de construcció de nodes malformats
# ---------------------------------------------------------------------------

def _node_cataleg_malformada(nid, cos_criteris, cos_ancres=""):
    """Node CatalegCurricular amb un bloc `criteris:` (o sense, si None)."""
    bloc = ""
    if cos_criteris is not None:
        bloc = f"criteris:\n{cos_criteris}"
    return (
        "---\n"
        f"id: {nid}\n"
        "type: CatalegCurricular\n"
        'title: "Catàleg robustesa"\n'
        'version: "V1.0-Esborrany"\n'
        'data_ultima_actualitzacio: "2026-11-02"\n'
        'authors:\n  - "Test"\n'
        'llicencia: "CC BY-SA 4.0"\n'
        'tags:\n  - okf/test\n'
        "estat: vigent\n"
        f"{bloc}"
        "---\n"
        "# Catàleg robustesa\n"
        "## 5 · Desglossament de CAs per RA\n"
        f"{cos_ancres}\n"
    )


def _node_fitxa_malformada(nid, instruments_block):
    """Node FitxaAEA amb un bloc `instruments_avaluacio:` (o sense, si None)."""
    bloc = ""
    if instruments_block is not None:
        bloc = f"instruments_avaluacio:\n{instruments_block}"
    return (
        "---\n"
        f"id: {nid}\n"
        "type: FitxaAEA\n"
        'title: "Fitxa robustesa"\n'
        'version: "V1.0-Esborrany"\n'
        'data_ultima_actualitzacio: "2026-11-02"\n'
        'authors:\n  - "Test"\n'
        'llicencia: "CC BY-SA 4.0"\n'
        'tags:\n  - okf/test\n'
        "estat: vigent\n"
        'credit: "1"\n'
        f"{bloc}"
        "---\n"
        "# Fitxa robustesa\n"
    )


def _exec_validador(ruta_vault, tmp_path):
    """Executa el validador complet via CLI i en retorna l'objecte Popen."""
    return subprocess.run(
        [sys.executable, VALIDAR, "--ruta", ruta_vault, "--output", str(tmp_path / "inf.md")],
        capture_output=True, text=True, timeout=120,
    )


def _assert_no_crash(proc, codi=None):
    """Codi coherent (no Traceback) i codi Y esperat a la sortida (si s'indica)."""
    assert proc.returncode in (0, 1, 2), (
        f"returncode inesperat {proc.returncode}\n--- stdout ---\n{proc.stdout}\n--- stderr ---\n{proc.stderr}"
    )
    assert "Traceback" not in proc.stderr, proc.stderr
    if codi is not None:
        assert codi in proc.stdout, f"codi esperat {codi} absent.\n{proc.stdout}"


# ============================================================
# Robustesa: proves negatives amb dades malformades
# ============================================================

def test_robustesa_criteris_dict_en_lloc_de_llista(tmp_path):
    """criteris: amb un dict en lloc d'una llista -> Y048, sense petar."""
    node = _node_cataleg_malformada("EX-CAT-R1", '  RA1: "5.1"\n')
    ruta = crear_vault(tmp_path, {"03_Cat.md": node, "01_Convencio.md": CONV_AMB_CATALEG})
    _assert_no_crash(_exec_validador(ruta, tmp_path), codi="Y048")


def test_robustesa_criteri_int_en_lloc_de_dict(tmp_path):
    """Un element de criteris[RA] que és un int (ni string ni dict) -> sense petar."""
    node = _node_cataleg_malformada("EX-CAT-R2", "  RA1:\n    - 42\n")
    ruta = crear_vault(tmp_path, {"03_Cat.md": node, "01_Convencio.md": CONV_AMB_CATALEG})
    _assert_no_crash(_exec_validador(ruta, tmp_path))


def test_robustesa_criteri_tots_camps_malformats(tmp_path):
    """CA amb tots els camps amb tipus incorrecte -> Y053 per camp, sense petar."""
    node = _node_cataleg_malformada(
        "EX-CAT-R3",
        '  RA1:\n    - codi: 123\n      id: 9\n      guia: 5\n'
        '      descripcio: [x]\n      contextualitzat: "sí"\n      afegit: "potser"\n',
    )
    ruta = crear_vault(tmp_path, {"03_Cat.md": node, "01_Convencio.md": CONV_AMB_CATALEG})
    _assert_no_crash(_exec_validador(ruta, tmp_path), codi="Y053")


def test_robustesa_instruments_dict_en_lloc_de_llista(tmp_path):
    """instruments_avaluacio: amb un dict en lloc d'una llista -> sense petar."""
    node = _node_fitxa_malformada("EX-AEA-R4", '{codi: "I1"}\n')
    ruta = crear_vault(tmp_path, {"03_Fitxa.md": node})
    _assert_no_crash(_exec_validador(ruta, tmp_path))


def test_robustesa_instrument_criteris_string(tmp_path):
    """Un instrument amb criteris: com a string -> Y053, sense petar."""
    node = _node_fitxa_malformada(
        "EX-AEA-R5", '  - codi: "I1"\n    descripcio: "D"\n    criteris: "5.1"\n'
    )
    ruta = crear_vault(tmp_path, {"03_Fitxa.md": node})
    _assert_no_crash(_exec_validador(ruta, tmp_path), codi="Y053")


def test_robustesa_cataleg_sense_criteris(tmp_path):
    """Un catàleg sense el camp criteris: -> sense petar."""
    node = _node_cataleg_malformada("EX-CAT-R6", None)
    ruta = crear_vault(tmp_path, {"03_Cat.md": node, "01_Convencio.md": CONV_AMB_CATALEG})
    _assert_no_crash(_exec_validador(ruta, tmp_path))


def test_robustesa_fitxa_sense_instruments(tmp_path):
    """Una fitxa sense instruments_avaluacio: -> sense petar."""
    node = _node_fitxa_malformada("EX-AEA-R7", None)
    ruta = crear_vault(tmp_path, {"03_Fitxa.md": node})
    _assert_no_crash(_exec_validador(ruta, tmp_path))


def test_robustesa_instrument_none(tmp_path):
    """instruments_avaluacio: amb un None a la llista -> sense petar."""
    node = _node_fitxa_malformada(
        "EX-AEA-R8", '  - null\n  - codi: "I2"\n    descripcio: "D"\n    criteris: ["1.1"]\n'
    )
    ruta = crear_vault(tmp_path, {"03_Fitxa.md": node})
    _assert_no_crash(_exec_validador(ruta, tmp_path))


def test_robustesa_criteris_int(tmp_path):
    """criteris: que és un int (42) -> sense petar."""
    node = _node_cataleg_malformada("EX-CAT-R9", "  42\n")
    ruta = crear_vault(tmp_path, {"03_Cat.md": node, "01_Convencio.md": CONV_AMB_CATALEG})
    _assert_no_crash(_exec_validador(ruta, tmp_path))


def test_robustesa_criteri_id_int(tmp_path):
    """Un CA amb id: com a int -> Y053, sense petar."""
    node = _node_cataleg_malformada(
        "EX-CAT-R10",
        '  RA1:\n    - codi: "5.1"\n      id: 9\n      contextualitzat: false\n      afegit: false\n',
        cos_ancres='| 5.1 | Xa | <a id="ca-5-1"></a>Desc | A | AEA |',
    )
    ruta = crear_vault(tmp_path, {"03_Cat.md": node, "01_Convencio.md": CONV_AMB_CATALEG})
    _assert_no_crash(_exec_validador(ruta, tmp_path), codi="Y053")