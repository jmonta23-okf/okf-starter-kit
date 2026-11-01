"""
Arrencada compartida dels tests del validador del OKF Starter Kit.

Converteix `03-eines/` en un mòdul importable i exposa helpers per crear
vaults temporals amb l'estructura mínima (MOC arrel + Convenció + Handoff)
de manera que els tests es centren en la comprovació que volen provar.
"""

import sys
import pathlib

import pytest

ARREL_KIT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ARREL_KIT / "03-eines"))

import validar_yaml as v  # noqa: E402


NODE_BASE = """---
id: {nid}
type: {tipus}
title: "{titol}"
version: "V1.0-Esborrany"
data_ultima_actualitzacio: "2026-10-31"
authors:
  - "Test"
llicencia: "CC BY-SA 4.0"
tags:
  - okf/test
estat: vigent
---

# {titol}

## Relacions (Graf)

- Complementa: [MOC del vault](./00_MOC.md)
"""

CONVENCIO = """---
id: EX-CONV-00
type: ConvencioNomenclatura
title: "Convenció del vault d'exemple"
version: "V1.0-Esborrany"
data_ultima_actualitzacio: "2026-10-31"
authors:
  - "Test"
llicencia: "CC BY-SA 4.0"
tags:
  - okf/test
estat: vigent
---

# Convenció del vault d'exemple

## 2 · Tipus de node vàlids

| Tipus | Descripció breu |
|:---|:---|
| `Guia` | Guia d'ús o tutorial. |
| `UnitatDidactica` | Unitat didàctica amb continguts, activitats i avaluació. |
| `FitxaAEA` | Fitxa d'una activitat d'ensenyament-aprenentatge. Requereix credit. |
"""

HANDOFF = NODE_BASE.format(
    nid="EX-HANDOFF-00", tipus="DocumentHandoff",
    titol="Handoff del vault d'exemple",
).replace("id: EX-HANDOFF-00", "id: EX-HANDOFF-00", 1)

MOC = NODE_BASE.format(nid="EX-MOC-00", tipus="MOC", titol="MOC del vault d'exemple")


def crear_vault(tmp_path, fitxers, amb_estructura=True):
    """
    Crea un vault temporal amb els fitxers indicats.

    fitxers: diccionari {ruta_relativa: contingut}.
    amb_estructura: si True, afegeix MOC arrel, Convenció i Handoff.
    Retorna la ruta absoluta del vault.
    """
    dades = dict(fitxers)
    if amb_estructura:
        dades.setdefault("00_MOC.md", MOC)
        dades.setdefault("01_Convencio.md", CONVENCIO)
        dades.setdefault("02_Handoff.md", HANDOFF)

    ruta_vault = tmp_path / "vault"
    ruta_vault.mkdir()
    for rel, contingut in dades.items():
        p = ruta_vault / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(contingut, encoding="utf-8")
    return str(ruta_vault)


def validar_vault(ruta_vault):
    """
    Executa el flux complet del validador (sense `main()` ni exit) sobre un
    vault temporal. Retorna la llista d'errors (ruta, codi, descripció, acció).
    """
    fitxers = v.trobar_fitxers_md(ruta_vault)
    yaml_per_ruta = {}
    errors = []

    for r in fitxers:
        data, errs = v.extreure_yaml(r)
        yaml_per_ruta[r] = {"data": data, "errors": errs}
        for e in errs:
            errors.append((r, e[0], e[1], e[2]))

    declarats, _convencions = v.llegir_tipus_de_les_convencions(fitxers, yaml_per_ruta)
    tipus_valid, _fam, tipus_credit = v.construir_tipus_valid(declarats)

    ids_vists = {}
    for r in fitxers:
        data = yaml_per_ruta[r]["data"]
        if data is None:
            continue
        enllacos = v.analitzar_enllacos(r)
        for e in v.validar_node(r, data, ids_vists, tipus_valid, tipus_credit, enllacos):
            errors.append((r, e[0], e[1], e[2]))

    for e in v.comprovacions_estructurals(ruta_vault, fitxers, yaml_per_ruta):
        errors.append((ruta_vault, e[0], e[1], e[2]))

    return errors


@pytest.fixture
def vault_valid(tmp_path):
    """Un vault completament vàlid (MOC + Convenció + Handoff + una Guia)."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Una guia vàlida")
    return crear_vault(tmp_path, {"03_Guia.md": node})


@pytest.fixture
def codis_error():
    """Converteix una llista d'errors en la llista de codis (ex: ['Y001','Y020'])."""
    def _codis(errors):
        return sorted(e[1] for e in errors)
    return _codis
