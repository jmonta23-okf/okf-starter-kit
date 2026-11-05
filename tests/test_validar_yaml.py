"""
Proves automàtiques del validador del OKF Starter Kit (v1.1.0).

Cada test crea un vault temporal mínim (MOC + Convenció + Handoff + el node
en qüestió) i comprova els codis d'error esperats. Els codis es defineixen a
`CODIS_ERROR` del mateix validador.
"""

import subprocess
import sys
from pathlib import Path

import validar_yaml as v

from conftest import (
    NODE_BASE,
    CONVENCIO,
    MOC,
    HANDOFF,
    crear_vault,
    validar_vault,
)


VALIDAR = str(Path(__file__).resolve().parent.parent / "03-eines" / "validar_yaml.py")


# ---------------------------------------------------------------------------
# Casos bàsics
# ---------------------------------------------------------------------------

def test_node_valid_passa(vault_valid, codis_error):
    """Un node universal (Guia) amb l'estructura del vault compleix tot."""
    errors = validar_vault(vault_valid)
    assert errors == []


def test_type_no_hashable_dona_error(tmp_path, codis_error):
    """type com a llista (no hashable) ha de donar error Y025, no un crash."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="[a, b]", titol="Guia amb type llista")
    node = node.replace('type: "[a, b]"', "type:\n  - a\n  - b")
    errors = validar_vault(crear_vault(tmp_path, {"03_Guia.md": node}))
    assert "Y025" in codis_error(errors)


def test_id_mal_escrit_dona_error(tmp_path, codis_error):
    """ID amb espais no segueix el patró {CODI}-{ÀMBIT}-{NN}."""
    node = NODE_BASE.format(nid="id mal escrit", tipus="Guia", titol="Guia amb ID dolent")
    errors = validar_vault(crear_vault(tmp_path, {"03_Guia.md": node}))
    assert "Y005" in codis_error(errors)


def test_node_amb_name_i_sense_id_no_desapareix(tmp_path, codis_error):
    """
    Antiga heurística Hermes (name: sense id:) suprimida: el node ara es
    valida i dona error Y002 (id absent), en lloc de desaparèixer.
    """
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Guia sense id")
    node = node.replace("id: EX-GUIA-01\n", "name: Una guia\n")
    errors = validar_vault(crear_vault(tmp_path, {"03_Guia.md": node}))
    assert "Y002" in codis_error(errors)


def test_title_buit_dona_error(tmp_path, codis_error):
    """title: \"\" compta com a camp universal buit."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="")
    errors = validar_vault(crear_vault(tmp_path, {"03_Guia.md": node}))
    assert "Y002" in codis_error(errors)


def test_tags_buits_donen_error(tmp_path, codis_error):
    """tags: [] compta com a camp universal buit."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Guia sense tags")
    node = node.replace("tags:\n  - okf/test", "tags: []")
    errors = validar_vault(crear_vault(tmp_path, {"03_Guia.md": node}))
    assert "Y002" in codis_error(errors)


def test_authors_cadena_dona_error(tmp_path, codis_error):
    """authors ha de ser una llista, mai una cadena."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Guia amb authors cadena")
    node = node.replace("authors:\n  - \"Test\"", 'authors: "Josep"')
    errors = validar_vault(crear_vault(tmp_path, {"03_Guia.md": node}))
    assert "Y026" in codis_error(errors)


def test_bom_dona_error_clar(tmp_path, codis_error):
    """Un fitxer amb BOM UTF-8 ha de donar un error clar (Y023)."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Guia amb BOM")
    ruta = crear_vault(tmp_path, {"03_Guia.md": "\ufeff" + node})
    errors = validar_vault(ruta)
    codis = codis_error(errors)
    assert "Y023" in codis
    desc = next(d for _, c, d, _ in errors if c == "Y023")
    assert "BOM" in desc


def test_claus_duplicades_dona_error(tmp_path, codis_error):
    """Dues claus title: al frontmatter han de donar error (abans guanyava l'última)."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Primer títol")
    node = node.replace('title: "Primer títol"', 'title: "Primer títol"\ntitle: "Segon títol"')
    errors = validar_vault(crear_vault(tmp_path, {"03_Guia.md": node}))
    assert "Y024" in codis_error(errors)


# ---------------------------------------------------------------------------
# Comprovacions de graf
# ---------------------------------------------------------------------------

def test_enllac_trencat_dona_error(tmp_path, codis_error):
    """Un enllaç marcat com a falla ([[...]]) prohibada."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Guia amb enllaç trencat")
    node += "\n- [Fitxer inexistent](./no_existeix.md)\n"
    errors = validar_vault(crear_vault(tmp_path, {"03_Guia.md": node}))
    assert "Y018" in codis_error(errors)


def test_wikilink_dona_error(tmp_path, codis_error):
    """Un wikilink [[...]] és prohibit al cos del node."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Guia amb wikilink")
    node += "\nVegeu [[02_Handoff]] per al context.\n"
    errors = validar_vault(crear_vault(tmp_path, {"03_Guia.md": node}))
    assert "Y019" in codis_error(errors)


def test_wikilink_dins_fence_no_error(tmp_path, codis_error):
    """Els [[...]] dins d'un bloc de codi (fence) són documentació, no wikilinks."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Guia amb fence")
    node += "\n```markdown\n- Vegeu [[02_Handoff]] (exemple de sintaxi)\n```\n"
    errors = validar_vault(crear_vault(tmp_path, {"03_Guia.md": node}))
    assert codis_error(errors) == []


# ---------------------------------------------------------------------------
# Enums i privacitat
# ---------------------------------------------------------------------------

def test_visibilitat_invalida_dona_error(tmp_path, codis_error):
    """visibilitat: totpublic no és de l'enum del Core (§4.1)."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Guia amb visibilitat rara")
    node = node.replace("estat: vigent", "estat: vigent\nvisibilitat: totpublic")
    errors = validar_vault(crear_vault(tmp_path, {"03_Guia.md": node}))
    assert "Y020" in codis_error(errors)


def test_estat_invalid_dona_error(tmp_path, codis_error):
    """estat: obsolescit (en lloc d'obsolet) no és de l'enum del Core."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Guia amb estat rar")
    node = node.replace("estat: vigent", "estat: obsolescit")
    errors = validar_vault(crear_vault(tmp_path, {"03_Guia.md": node}))
    assert "Y021" in codis_error(errors)


def test_dades_personals_publica_dona_error(tmp_path, codis_error):
    """Privacitat: dades_personals: true amb visibilitat publica és un error."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Guia amb dades")
    node = node.replace(
        "estat: vigent",
        "estat: vigent\nvisibilitat: publica\ndades_personals: true",
    )
    errors = validar_vault(crear_vault(tmp_path, {"03_Guia.md": node}))
    assert "Y022" in codis_error(errors)


def test_dades_personals_restringida_passa(tmp_path, codis_error):
    """Privacitat: restringida + dades_personals: true és correcte."""
    node = NODE_BASE.format(nid="EX-GUIA-01", tipus="Guia", titol="Guia restringida")
    node = node.replace(
        "estat: vigent",
        "estat: vigent\nvisibilitat: restringida\ndades_personals: true",
    )
    errors = validar_vault(crear_vault(tmp_path, {"03_Guia.md": node}))
    assert codis_error(errors) == []


# ---------------------------------------------------------------------------
# Tipus i credit
# ---------------------------------------------------------------------------

def test_credit_en_tipus_universal_dona_error(tmp_path, codis_error):
    """Un tipus universal (PaquetLLM) no pot dur el camp credit."""
    node = NODE_BASE.format(nid="EX-LLM-01", tipus="PaquetLLM", titol="Paquet sense crèdit")
    node = node.replace("estat: vigent", "estat: vigent\ncredit: MP1519")
    errors = validar_vault(crear_vault(tmp_path, {"03_PaquetLLM.md": node}))
    assert "Y017" in codis_error(errors)


def test_familia_sense_convencio_dona_error(tmp_path, codis_error):
    """Un tipus de família no declarat a la Convenció no s'accepta."""
    node = NODE_BASE.format(nid="EX-UD1-00", tipus="TipusInventat", titol="UD inventada")
    errors = validar_vault(crear_vault(tmp_path, {"03_UD.md": node}))
    assert "Y004" in codis_error(errors)


def test_familia_declarada_a_convencio_passa(tmp_path, codis_error):
    """Un tipus de família declarat a la Convenció del vault s'accepta."""
    node = NODE_BASE.format(nid="EX-UD1-00", tipus="UnitatDidactica", titol="Unitat didàctica")
    errors = validar_vault(crear_vault(tmp_path, {"03_UD.md": node}))
    assert codis_error(errors) == []


def test_credit_obligatori_segons_convencio(tmp_path, codis_error):
    """Si la Convenció declara que un tipus requereix credit, cal dur-lo."""
    node = NODE_BASE.format(nid="EX-AEA-01", tipus="FitxaAEA", titol="AEA sense credit")
    errors = validar_vault(crear_vault(tmp_path, {"03_AEA.md": node}))
    assert "Y003" in codis_error(errors)


# ---------------------------------------------------------------------------
# Estructura del vault (MOC arrel, Handoff, Convenció)
# ---------------------------------------------------------------------------

def build_node(nid, tipus, titol, extra=""):
    """Node base amb camps extra opcionals al frontmatter."""
    node = NODE_BASE.format(nid=nid, tipus=tipus, titol=titol)
    if extra:
        node = node.replace("estat: vigent", "estat: vigent\n" + extra)
    return node


def test_sense_moc_arrel_dona_error(tmp_path, codis_error):
    """Un vault amb el MOC en una subcarpeta (no a l'arrel) dona Y014."""
    guia = build_node("EX-GUIA-01", "Guia", "Una guia").replace(
        "## Relacions (Graf)\n\n- Complementa: [MOC del vault](./00_MOC.md)",
        "## Relacions (Graf)\n\n- Complementa: [MOC del vault](./sub/00_MOC.md)",
    )
    handoff = build_node("EX-HANDOFF-00", "DocumentHandoff", "Handoff").replace(
        "## Relacions (Graf)\n\n- Complementa: [MOC del vault](./00_MOC.md)",
        "## Relacions (Graf)\n\n- Complementa: [MOC del vault](./sub/00_MOC.md)",
    )
    errors = validar_vault(crear_vault(
        tmp_path,
        {
            "sub/00_MOC.md": MOC,
            "01_Convencio.md": CONVENCIO,
            "02_Handoff.md": handoff,
            "03_Guia.md": guia,
        },
        amb_estructura=False,
    ))
    assert "Y014" in codis_error(errors)


def test_sense_handoff_dona_error(tmp_path, codis_error):
    """Un vault sense cap DocumentHandoff dona Y015."""
    guia = build_node("EX-GUIA-01", "Guia", "Una guia")
    errors = validar_vault(crear_vault(
        tmp_path,
        {"00_MOC.md": MOC, "01_Convencio.md": CONVENCIO, "03_Guia.md": guia},
        amb_estructura=False,
    ))
    assert "Y015" in codis_error(errors)


def test_sense_convencio_dona_error(tmp_path, codis_error):
    """Un vault sense cap ConvencioNomenclatura dona Y016."""
    guia = build_node("EX-GUIA-01", "Guia", "Una guia")
    errors = validar_vault(crear_vault(
        tmp_path,
        {"00_MOC.md": MOC, "02_Handoff.md": HANDOFF, "03_Guia.md": guia},
        amb_estructura=False,
    ))
    assert "Y016" in codis_error(errors)


def test_enums_absents_passen(tmp_path, codis_error):
    """Els camps absents visibilitat/estat assumeixen els valors del Core i passen."""
    node = build_node("EX-GUIA-01", "Guia", "Una guia").replace("estat: vigent\n", "")
    errors = validar_vault(crear_vault(tmp_path, {"03_Guia.md": node}))
    assert codis_error(errors) == []


# ---------------------------------------------------------------------------
# Àlies i naturalesa (RFC-OKF-02, Fase 3)
# ---------------------------------------------------------------------------

# Convenció amb una secció d'àlies i FitxaAEA sense «requereix credit»
# (per aïllar la normalització del Y003).
ALIAS_CONVENCIO = CONVENCIO.replace(
    "Fitxa d'una activitat d'ensenyament-aprenentatge. Requereix credit.",
    "Fitxa d'una activitat d'ensenyament-aprenentatge.",
) + """

## 3 · Àlies de tipus

| Àlies | Tipus canònic |
|:---|:---|
| `Activitat` | `FitxaAEA` |
"""


def _validar_amb_aliases(ruta_vault):
    """Flux complet de validació, incloent la normalització d'àlies."""
    import validar_yaml as v
    fitxers = v.trobar_fitxers_md(ruta_vault)
    yaml_per_ruta = {}
    errors = []
    for r in fitxers:
        data, errs = v.extreure_yaml(r)
        yaml_per_ruta[r] = {"data": data, "errors": errs}
        for e in errs:
            errors.append((r, e[0], e[1], e[2]))
    declarats, _ = v.llegir_tipus_de_les_convencions(fitxers, yaml_per_ruta)
    aliases, _conf = v.llegir_aliases_de_les_convencions(fitxers, yaml_per_ruta)
    tipus_valid, _fam, tipus_credit = v.construir_tipus_valid(declarats)
    ids_vists = {}
    for r in fitxers:
        data = yaml_per_ruta[r]["data"]
        if data is None:
            continue
        enllacos = v.analitzar_enllacos(r)
        for e in v.validar_node(r, data, ids_vists, tipus_valid, tipus_credit, enllacos, aliases):
            errors.append((r, e[0], e[1], e[2]))
    return errors


def test_alias_normalization(tmp_path, codis_error):
    """type: Activitat es normalitza a FitxaAEA si la Convenció declara l'àlies."""
    node = NODE_BASE.format(nid="EX-AEA-01", tipus="Activitat", titol="Activitat amb àlies")
    ruta = crear_vault(tmp_path, {
        "03_Activitat.md": node,
        "01_Convencio.md": ALIAS_CONVENCIO,
    })
    assert "Y004" not in codis_error(_validar_amb_aliases(ruta))

    # Sense la Convenció que declara l'àlies, Activitat no és vàlid (Y004).
    (tmp_path / "b").mkdir()
    ruta2 = crear_vault(tmp_path / "b", {"03_Activitat.md": node})
    assert "Y004" in codis_error(_validar_amb_aliases(ruta2))


def test_naturalesa_validation(tmp_path, codis_error):
    """
    naturalesa: sintesi és vàlid; naturalesa: inventada dona warning Y036
    (severitat 🟡 Mitjana, no error crític/alta).
    """
    import validar_yaml as v

    ok = NODE_BASE.format(nid="EX-AEA-02", tipus="FitxaAEA", titol="Fitxa amb naturalesa")
    ok = ok.replace("tags:", "naturalesa: sintesi\ntags:")
    ruta_ok = crear_vault(tmp_path, {"03_AEA.md": ok, "01_Convencio.md": ALIAS_CONVENCIO})
    assert codis_error(validar_vault(ruta_ok)) == []

    bad = NODE_BASE.format(nid="EX-AEA-03", tipus="FitxaAEA", titol="Fitxa amb naturalesa dolenta")
    bad = bad.replace("tags:", "naturalesa: inventada\ntags:")
    (tmp_path / "b").mkdir()
    ruta_bad = crear_vault(tmp_path / "b", {"03_AEA.md": bad, "01_Convencio.md": ALIAS_CONVENCIO})
    errors = validar_vault(ruta_bad)
    assert "Y036" in codis_error(errors)
    assert v.CODIS_ERROR["Y036"][1] == "🟡 Mitjana"


# ---------------------------------------------------------------------------
# Coherència catàleg: frontmatter ↔ àncores (RFC-OKF-02, Fase 3)
# ---------------------------------------------------------------------------

CONV_AMB_CATALEG = CONVENCIO.replace(
    "| `Guia` | Guia d'ús o tutorial. |",
    "| `Guia` | Guia d'ús o tutorial. |\n| `CatalegCurricular` | Catàleg de RAs i CAs d'un mòdul. |",
)


def _cataleg_test_node(nid, codis_fm, ancres_cos):
    """Node CatalegCurricular mínim amb criteris al frontmatter i àncores al cos."""
    llista = ", ".join(f'"{c}"' for c in codis_fm)
    files = "\n".join(
        f'| {c.replace("-", ".")} | Xa | <a id="ca-{c}"></a>Descripció | A | AEA |'
        for c in ancres_cos
    )
    return (
        "---\n"
        f"id: {nid}\n"
        "type: CatalegCurricular\n"
        'title: "Catàleg de test"\n'
        'version: "V1.0-Esborrany"\n'
        'data_ultima_actualitzacio: "2026-11-02"\n'
        'authors:\n  - "Test"\n'
        'llicencia: "CC BY-SA 4.0"\n'
        'tags:\n  - okf/test\n'
        "estat: vigent\n"
        "criteris:\n"
        f"  RA5: [{llista}]\n"
        "---\n"
        "# Catàleg de test\n"
        "## 5 · Desglossament de CAs per RA\n"
        f"{files}\n"
    )


def test_y030_criteri_sense_ancora(tmp_path, codis_error):
    """Un CA del frontmatter sense àncora al cos dona Y030."""
    node = _cataleg_test_node("EX-CAT-01", ["5.1", "5.2"], ["5-1"])
    errors = validar_vault(crear_vault(
        tmp_path, {"03_Cataleg.md": node, "01_Convencio.md": CONV_AMB_CATALEG}
    ))
    assert "Y030" in codis_error(errors)


def test_y031_ancora_sense_criteri(tmp_path, codis_error):
    """Una àncora al cos sense criteri al frontmatter dona Y031."""
    node = _cataleg_test_node("EX-CAT-02", ["5.1", "5.2"], ["5-1", "5-2", "5-3"])
    errors = validar_vault(crear_vault(
        tmp_path, {"03_Cataleg.md": node, "01_Convencio.md": CONV_AMB_CATALEG}
    ))
    assert "Y031" in codis_error(errors)
    assert "Y030" not in codis_error(errors)


# ---------------------------------------------------------------------------
# Format de `criteris:` (Bloc 14b): normalització i invariants del format nou
# ---------------------------------------------------------------------------

def _cataleg_test_node_nou(nid, criteris_body, ancres_cos):
    """Node CatalegCurricular amb `criteris:` en format nou (dicts)."""
    files = "\n".join(
        f'| {c.replace("-", ".")} | Xa | <a id="ca-{c}"></a>Descripció | A | AEA |'
        for c in ancres_cos
    )
    return (
        "---\n"
        f"id: {nid}\n"
        "type: CatalegCurricular\n"
        'title: "Catàleg de test"\n'
        'version: "V1.0-Esborrany"\n'
        'data_ultima_actualitzacio: "2026-11-02"\n'
        'authors:\n  - "Test"\n'
        'llicencia: "CC BY-SA 4.0"\n'
        'tags:\n  - okf/test\n'
        "estat: vigent\n"
        "criteris:\n"
        f"{criteris_body}"
        "---\n"
        "# Catàleg de test\n"
        "## 5 · Desglossament de CAs per RA\n"
        f"{files}\n"
    )


def test_normalitzar_criteris_format_antic():
    """Llista de strings -> dicts normalitzats amb defaults (format antic)."""
    resultat = v.normalitzar_criteris({"RA5": ["5.1", "5.2"]})
    assert resultat == {
        "RA5": [
            {"codi": "5.1", "id": None, "guia": None, "descripcio": None,
             "contextualitzat": False, "afegit": False, "origen": None},
            {"codi": "5.2", "id": None, "guia": None, "descripcio": None,
             "contextualitzat": False, "afegit": False, "origen": None},
        ]
    }


def test_normalitzar_criteris_format_nou():
    """Dicts complets -> idèntics (idempotent); defaults per als camps absents."""
    entrada = {
        "RA5": [
            {"codi": "5.1", "id": None, "guia": "5a", "descripcio": "Desc",
             "contextualitzat": False, "afegit": False, "origen": None},
            {"codi": None, "id": None, "guia": "5h", "descripcio": "Anglès",
             "contextualitzat": True, "afegit": True, "origen": "anglès professional"},
        ]
    }
    assert v.normalitzar_criteris(entrada) == entrada  # idempotent

    parcial = {"RA5": [{"codi": "5.3"}]}
    d = v.normalitzar_criteris(parcial)["RA5"][0]
    assert d == {"codi": "5.3", "id": None, "guia": None, "descripcio": None,
                 "contextualitzat": False, "afegit": False, "origen": None}
    assert "guia" not in parcial["RA5"][0]  # no muta l'entrada

    # 'origen' accepta qualsevol valor (aquí un enter) sense petar.
    amb_origen = {"RA5": [{"codi": None, "afegit": True, "guia": "5i", "origen": 42}]}
    assert v.normalitzar_criteris(amb_origen)["RA5"][0]["origen"] == 42


def test_y040_contextualitzat_no_boolean(tmp_path, codis_error):
    """`contextualitzat: "sí"` -> Y040 (🟠 Alta)."""
    node = _cataleg_test_node_nou(
        "EX-CAT-30",
        '  RA5:\n    - codi: "5.1"\n      contextualitzat: "sí"\n      afegit: false\n',
        ["5-1"],
    )
    errors = validar_vault(crear_vault(
        tmp_path, {"03_Cataleg.md": node, "01_Convencio.md": CONV_AMB_CATALEG}
    ))
    assert "Y040" in codis_error(errors)


def test_y042_codi_null_sense_afegit(tmp_path, codis_error):
    """`codi: null` sense `afegit: true` -> Y042 (🔴 Crític)."""
    node = _cataleg_test_node_nou(
        "EX-CAT-31",
        "  RA5:\n    - codi: null\n      guia: \"5a\"\n      afegit: false\n",
        ["5-1"],
    )
    errors = validar_vault(crear_vault(
        tmp_path, {"03_Cataleg.md": node, "01_Convencio.md": CONV_AMB_CATALEG}
    ))
    assert "Y042" in codis_error(errors)


def test_y043_afegit_sense_guia(tmp_path, codis_error):
    """`afegit: true` sense `guia` -> Y043 (🔴 Crític)."""
    node = _cataleg_test_node_nou(
        "EX-CAT-32",
        "  RA5:\n    - codi: null\n      afegit: true\n",
        [],
    )
    errors = validar_vault(crear_vault(
        tmp_path, {"03_Cataleg.md": node, "01_Convencio.md": CONV_AMB_CATALEG}
    ))
    assert "Y043" in codis_error(errors)


def test_camp_desconegut_warning(tmp_path):
    """Camp extra en un dict -> warning textual, sense codi Y, exit 0, `--- Warnings ---`."""
    node = _cataleg_test_node_nou(
        "EX-CAT-33",
        '  RA5:\n'
        '    - codi: "5.1"\n'
        '      guia: "5a"\n'
        '      descripcions: "camp no permès"\n'
        '    - codi: "5.2"\n'
        '      guia: "5b"\n',
        ["5-1", "5-2"],
    )
    ruta = crear_vault(tmp_path, {
        "03_Cataleg.md": node, "01_Convencio.md": CONV_AMB_CATALEG
    })
    proc = subprocess.run(
        [sys.executable, VALIDAR, "--ruta", ruta, "--output", str(tmp_path / "inf.md")],
        capture_output=True, text=True, timeout=120,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "--- Warnings ---" in proc.stdout
    assert "Warning: camp desconegut 'descripcions' a criteris['RA5'][0]" in proc.stdout
    assert "Y040" not in proc.stdout  # cap codi Y pel camp desconegut


def test_camp_desconegut_warning_dedup(tmp_path):
    """Un mateix camp desconegut en 3 CAs -> UNA sola línia de warning."""
    node = _cataleg_test_node_nou(
        "EX-CAT-34",
        '  RA5:\n'
        '    - codi: "5.1"\n'
        '      descripcions: "a"\n'
        '    - codi: "5.2"\n'
        '      descripcions: "b"\n'
        '    - codi: "5.3"\n'
        '      descripcions: "c"\n',
        ["5-1", "5-2", "5-3"],
    )
    ruta = crear_vault(tmp_path, {
        "03_Cataleg.md": node, "01_Convencio.md": CONV_AMB_CATALEG
    })
    proc = subprocess.run(
        [sys.executable, VALIDAR, "--ruta", ruta, "--output", str(tmp_path / "inf.md")],
        capture_output=True, text=True, timeout=120,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert proc.stdout.count("Warning: camp desconegut 'descripcions'") == 1


def test_y044_afegit_i_contextualitzat(tmp_path, codis_error):
    """`afegit: true` i `contextualitzat: true` -> Y044 (🟡 Mitjana)."""
    node = _cataleg_test_node_nou(
        "EX-CAT-40",
        '  RA5:\n'
        '    - codi: null\n'
        '      guia: "5a"\n'
        '      afegit: true\n'
        '      contextualitzat: true\n',
        [],
    )
    errors = validar_vault(crear_vault(
        tmp_path, {"03_Cataleg.md": node, "01_Convencio.md": CONV_AMB_CATALEG}
    ))
    assert "Y044" in codis_error(errors)
    assert v.CODIS_ERROR["Y044"][1] == "🟡 Mitjana"


def test_y048_criteris_ra_no_llista(tmp_path, codis_error):
    """`criteris: {RA5: "5.1"}` (string) -> Y048 (🟠 Alta); la resta es valida i --audit no peta."""
    node = _cataleg_test_node_nou(
        "EX-CAT-41",
        '  RA5: "5.1"\n'
        '  RA6:\n'
        '    - codi: "6.1"\n'
        '      guia: "6a"\n',
        ["6-1"],
    )
    ruta = crear_vault(tmp_path, {
        "03_Cataleg.md": node, "01_Convencio.md": CONV_AMB_CATALEG
    })
    errors = validar_vault(ruta)
    assert "Y048" in codis_error(errors)
    assert v.CODIS_ERROR["Y048"][1] == "🟠 Alta"
    # el RA vàlid (RA6) es processa normalment: la seva àncora ca-6-1 no dispara Y030/Y031
    assert "Y030" not in codis_error(errors)
    assert "Y031" not in codis_error(errors)
    # --audit no peta davant d'un RA no-llista (contribueix 0 CAs, però no falla)
    proc = subprocess.run(
        [sys.executable, VALIDAR, "--ruta", ruta, "--audit",
         "--output", str(tmp_path / "inf.md")],
        capture_output=True, text=True, timeout=120,
    )
    assert proc.returncode is not None  # arriba al final sense penjar-se
    assert "Traceback" not in proc.stderr


# ---------------------------------------------------------------------------
# instruments_avaluacio de les FitxaAEA (Bloc 14d)
# ---------------------------------------------------------------------------

def _fitxa_test_node(nid, instruments_body):
    """Node FitxaAEA mínim i vàlid amb `instruments_avaluacio:`."""
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
        'credit: "1"\n'
        "estat: vigent\n"
        f"instruments_avaluacio:\n{instruments_body}"
        "---\n"
        "# Fitxa de test\n"
    )


def test_instruments_format_antic(tmp_path, codis_error):
    """FitxaAEA amb `instruments_avaluacio` de strings: s'accepta, warning de
    format antic a --- Warnings ---, normalitza correctament i NO genera Y051."""
    node = _fitxa_test_node(
        "EX-AEA-01",
        '  - "./01_Protocol.md#proves-escrites"\n'
        '  - "./01_Protocol.md#observacio-competencial"\n',
    )
    ruta = crear_vault(tmp_path, {"03_Fitxa.md": node})

    # normalització correcta (funció pura)
    norm = v.normalitzar_instruments_avaluacio(
        ["./01_Protocol.md#proves-escrites", "./01_Protocol.md#observacio-competencial"]
    )
    assert norm == [
        {"codi": None, "descripcio": "./01_Protocol.md#proves-escrites", "criteris": []},
        {"codi": None, "descripcio": "./01_Protocol.md#observacio-competencial", "criteris": []},
    ]

    # no genera Y051 i el node és vàlid (exit 0)
    errors = validar_vault(ruta)
    assert "Y051" not in codis_error(errors)

    proc = subprocess.run(
        [sys.executable, VALIDAR, "--ruta", ruta, "--output", str(tmp_path / "inf.md")],
        capture_output=True, text=True, timeout=120,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "--- Warnings ---" in proc.stdout
    assert "Warning: instruments_avaluacio uses legacy format in EX-AEA-01" in proc.stdout


def test_instruments_format_nou(tmp_path, codis_error):
    """FitxaAEA amb `instruments_avaluacio` de dicts vàlids: s'accepta, sense warning."""
    node = _fitxa_test_node(
        "EX-AEA-02",
        '  - codi: "Pt1"\n'
        '    descripcio: "Pràctica de taller 1"\n'
        '    criteris: ["1.1", "1.2"]\n'
        '  - codi: "Pe1"\n'
        '    descripcio: "Prova escrita 1"\n'
        '    criteris: ["2.1"]\n',
    )
    ruta = crear_vault(tmp_path, {"03_Fitxa.md": node})
    errors = validar_vault(ruta)
    assert "Y050" not in codis_error(errors)
    assert "Y051" not in codis_error(errors)
    proc = subprocess.run(
        [sys.executable, VALIDAR, "--ruta", ruta, "--output", str(tmp_path / "inf.md")],
        capture_output=True, text=True, timeout=120,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "--- Warnings ---" not in proc.stdout


def test_instruments_camp_desconegut(tmp_path):
    """Un instrument amb un camp extra -> warning textual, sense codi Y, exit 0."""
    node = _fitxa_test_node(
        "EX-AEA-03",
        '  - codi: "Pt1"\n'
        '    descripcio: "Pràctica"\n'
        '    criteris: ["1.1"]\n'
        '    notes: "extra"\n',
    )
    ruta = crear_vault(tmp_path, {"03_Fitxa.md": node})
    proc = subprocess.run(
        [sys.executable, VALIDAR, "--ruta", ruta, "--output", str(tmp_path / "inf.md")],
        capture_output=True, text=True, timeout=120,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "--- Warnings ---" in proc.stdout
    assert "Warning: unknown field 'notes' in instruments_avaluacio[0] of EX-AEA-03" in proc.stdout
    assert "Y051" not in proc.stdout


def test_y050_codi_instrument_duplicat(tmp_path, codis_error):
    """Dos instruments amb `codi: "Pt1"` -> Y050 (🟠 Alta)."""
    node = _fitxa_test_node(
        "EX-AEA-04",
        '  - codi: "Pt1"\n'
        '    descripcio: "A"\n'
        '    criteris: ["1.1"]\n'
        '  - codi: "Pt1"\n'
        '    descripcio: "B"\n'
        '    criteris: ["1.2"]\n',
    )
    errors = validar_vault(crear_vault(tmp_path, {"03_Fitxa.md": node}))
    assert "Y050" in codis_error(errors)
    assert v.CODIS_ERROR["Y050"][1] == "🟠 Alta"


def test_y051_instrument_sense_criteris(tmp_path, codis_error):
    """Un instrument en format nou (dict) amb `criteris: []` -> Y051 (🟡 Mitjana)."""
    node = _fitxa_test_node(
        "EX-AEA-05",
        '  - codi: "Pt1"\n'
        '    descripcio: "A"\n'
        "    criteris: []\n",
    )
    errors = validar_vault(crear_vault(tmp_path, {"03_Fitxa.md": node}))
    assert "Y051" in codis_error(errors)
    assert v.CODIS_ERROR["Y051"][1] == "🟡 Mitjana"


def test_y050_codi_null_no_es_duplicat(tmp_path, codis_error):
    """Tres instruments amb `codi: null` -> cap Y050 (no són duplicats entre si)."""
    node = _fitxa_test_node(
        "EX-AEA-06",
        '  - codi: null\n    descripcio: "A"\n    criteris: ["1.1"]\n'
        '  - codi: null\n    descripcio: "B"\n    criteris: ["1.2"]\n'
        '  - codi: null\n    descripcio: "C"\n    criteris: ["1.3"]\n',
    )
    errors = validar_vault(crear_vault(tmp_path, {"03_Fitxa.md": node}))
    assert "Y050" not in codis_error(errors)
    assert "Y051" not in codis_error(errors)


def test_y051_no_es_dispara_en_format_antic(tmp_path, codis_error):
    """FitxaAEA amb instruments en format antic (strings) -> NO genera Y051, només el warning."""
    node = _fitxa_test_node(
        "EX-AEA-07",
        '  - "./01_Protocol.md#proves-escrites"\n'
        '  - "./01_Protocol.md#observacio-competencial"\n',
    )
    ruta = crear_vault(tmp_path, {"03_Fitxa.md": node})
    errors = validar_vault(ruta)
    assert "Y051" not in codis_error(errors)
    proc = subprocess.run(
        [sys.executable, VALIDAR, "--ruta", ruta, "--output", str(tmp_path / "inf.md")],
        capture_output=True, text=True, timeout=120,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "--- Warnings ---" in proc.stdout
    assert "Warning: instruments_avaluacio uses legacy format" in proc.stdout
    assert "Y051" not in proc.stdout


# ---------------------------------------------------------------------------
# Bloc 14g-bis: Y052 (criteri de criteris_avaluacio sense instrument)
# ---------------------------------------------------------------------------

def _fitxa_test_node_ca(nid, criteris_yaml, instruments_yaml=None):
    """Node FitxaAEA vàlid amb `criteris_avaluacio` (i `instruments_avaluacio` opcional)."""
    txt = (
        "---\n"
        f"id: {nid}\n"
        "type: FitxaAEA\n"
        'title: "Fitxa de test"\n'
        'version: "V1.0-Esborrany"\n'
        'data_ultima_actualitzacio: "2026-11-02"\n'
        'authors:\n  - "Test"\n'
        'llicencia: "CC BY-SA 4.0"\n'
        'tags:\n  - okf/test\n'
        'credit: "1"\n'
        "estat: vigent\n"
        f"criteris_avaluacio:\n{criteris_yaml}"
    )
    if instruments_yaml is not None:
        txt += f"instruments_avaluacio:\n{instruments_yaml}"
    txt += "---\n# Fitxa de test\n"
    return txt


def test_y052_criteri_sense_instrument(tmp_path, codis_error):
    """Un criteri de criteris_avaluacio que cap instrument avalua -> Y052 (🟡 Mitjana)."""
    node = _fitxa_test_node_ca(
        "EX-AEA-80",
        '  - "5.1"\n  - "5.2"\n  - "6.1"\n',
        '  - codi: "I1"\n    descripcio: "D"\n    criteris:\n      - "5.1"\n      - "5.2"\n',
    )
    errors = validar_vault(crear_vault(tmp_path, {"03_Fitxa.md": node}))
    assert "Y052" in codis_error(errors)
    assert v.CODIS_ERROR["Y052"][1] == "🟡 Mitjana"
    assert codis_error(errors).count("Y052") == 1  # només per a 6.1


def test_y052_no_es_dispara_si_no_hi_ha_instruments(tmp_path, codis_error):
    """Sense instruments_avaluacio (o [] ) NO s'emet Y052."""
    node_abs = _fitxa_test_node_ca("EX-AEA-81", '  - "5.1"\n  - "5.2"\n', None)
    node_buit = _fitxa_test_node_ca("EX-AEA-82", '  - "5.1"\n', "  []\n")
    errors = validar_vault(crear_vault(
        tmp_path, {"03_Fitxa_a.md": node_abs, "03_Fitxa_b.md": node_buit}
    ))
    assert "Y052" not in codis_error(errors)


def test_y052_dos_criteris_no_coberts(tmp_path, codis_error):
    """Dos criteris no coberts -> dos Y052 (un per criteri)."""
    node = _fitxa_test_node_ca(
        "EX-AEA-83",
        '  - "5.1"\n  - "6.1"\n  - "7.1"\n',
        '  - codi: "I1"\n    descripcio: "D"\n    criteris:\n      - "5.1"\n',
    )
    errors = validar_vault(crear_vault(tmp_path, {"03_Fitxa.md": node}))
    assert codis_error(errors).count("Y052") == 2


def test_y052_no_es_dispara_en_format_antic(tmp_path, codis_error):
    """Instruments en format antic (strings) -> Y052 NO s'aplica (no es pot verificar)."""
    node = _fitxa_test_node_ca(
        "EX-AEA-90",
        '  - "5.1"\n  - "5.2"\n',
        '  - "./protocol.md#prova-escrita"\n  - "./protocol.md#observacio"\n',
    )
    errors = validar_vault(crear_vault(tmp_path, {"03_Fitxa.md": node}))
    assert "Y052" not in codis_error(errors)


def test_y052_no_es_dispara_en_format_mixt(tmp_path, codis_error):
    """Barreja de dict + string (format mixt) -> Y052 NO s'aplica."""
    node = _fitxa_test_node_ca(
        "EX-AEA-91",
        '  - "5.1"\n  - "5.2"\n',
        '  - codi: "I1"\n    descripcio: "D"\n    criteris:\n      - "5.1"\n'
        '  - "./protocol.md#treball"\n',
    )
    errors = validar_vault(crear_vault(tmp_path, {"03_Fitxa.md": node}))
    assert "Y052" not in codis_error(errors)


def test_y052_es_dispara_en_format_nou(tmp_path, codis_error):
    """Tots els instruments en format nou (dicts) -> Y052 s'aplica com abans."""
    node = _fitxa_test_node_ca(
        "EX-AEA-92",
        '  - "5.1"\n  - "6.1"\n',
        '  - codi: "I1"\n    descripcio: "D"\n    criteris:\n      - "5.1"\n',
    )
    errors = validar_vault(crear_vault(tmp_path, {"03_Fitxa.md": node}))
    assert "Y052" in codis_error(errors)
    assert codis_error(errors).count("Y052") == 1  # només per a 6.1
