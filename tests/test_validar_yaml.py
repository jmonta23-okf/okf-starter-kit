"""
Proves automàtiques del validador del OKF Starter Kit (v1.1.0).

Cada test crea un vault temporal mínim (MOC + Convenció + Handoff + el node
en qüestió) i comprova els codis d'error esperats. Els codis es defineixen a
`CODIS_ERROR` del mateix validador.
"""

from conftest import (
    NODE_BASE,
    CONVENCIO,
    MOC,
    HANDOFF,
    crear_vault,
    validar_vault,
)


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
