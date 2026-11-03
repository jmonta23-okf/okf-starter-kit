#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validar_yaml.py — Validador YAML de vaults OKF (OKF Starter Kit) v1.2.0

Validador genèric i reutilitzable per a qualsevol vault creat amb el
OKF Starter Kit. Sincronitzat amb els Cores del kit (V1.1.1 / V1.0.1):

  - 8 camps universals obligatoris (id, type, title, version,
    data_ultima_actualitzacio, authors, llicencia, tags), segons els
    Cores §3. Ni més ni menys: els antics camps obligatoris
    (subtitle, cycle, center, academic_year, legal_framework) ara són
    opcionals (camps de família o d'informació).
  - 9 tipus universals (MOC, Guia, Glossari, Protocol, PaquetLLM,
    ConvencioNomenclatura, Llicencia, Plantilla, DocumentHandoff),
    segons els Cores §2. `Llicencia` i `Plantilla` són universals.
  - Els tipus de família NO estan fixos al codi: es llegeixen de la
    Convenció de Nomenclatura del vault (nodes tipus
    `ConvencioNomenclatura`), de les taules de tipus vàlids (§2) i de
    les taules de tipus de família per perfil (§8). El validador
    accepta els 9 universals + els tipus declarats a la Convenció.
  - `credit` només es pot exigir a tipus de família la Convenció dels
    quals ho declari (descripció amb "requereix credit"). Un tipus
    universal NO pot dur `credit` (error Y017).

Comprovacions de graf (el README del kit les promet des del principi):
  - Enllaços relatius: tots han d'apuntar a un fitxer existent.
  - Wikilinks `[[...]]` prohibits (sintaxi del Core §6: markdown relatiu).
  - Enums `visibilitat` i `estat` tancats (valors del Core §4).
  - MOC arrel, DocumentHandoff i ConvencioNomenclatura presents quan
    l'arrel validada és un vault (té nodes directes). Els repos amb
    subvaults (com el kit sencer) no es consideren un vault únic.

Robustesa:
  - `type` no hashable (llista/diccionari) -> error Y025, sense crash.
  - Ja no hi ha l'heuristica Hermes (`name:` sense `id:`): un node amb
    l'`id` mal escrit dona error, no desapareix.
  - Valors buits (`title: ""`, `tags: []`) -> error Y002.
  - `authors` / `tags` han de ser llistes -> error Y026.
  - BOM UTF-8 -> error Y023 amb avís d'eliminació.
  - Claus YAML duplicades -> error Y024 (abans guanyava l'última).

Ús:
    python3 validar_yaml.py [--ruta RUTA] [--output FITXER]

Codi de sortida: 0 = tot valid; 1 = hi ha errors; 2 = error d'ús.
Determinista: el mateix vault produeix sempre els mateixos errors.
"""

import os
import sys
import re
import datetime
import argparse
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: Cal instal·lar pyyaml. Executa: pip3 install pyyaml")
    sys.exit(2)


# =============================================================================
# CONSTANTS
# =============================================================================

VERSIO_SCRIPT = "1.2.0"

# Prefix que ha de tenir com a mínim un dels tags de cada node.
PREFIX_TAG = "okf/"

# ---------------------------------------------------------------- Cores (§3) -
# Els 8 camps universals obligatoris. Són els únics camps exigits per a tots
# els nodes; qualsevol altre camp (subtitle, cycle, center, academic_year,
# legal_framework, estat, visibilitat, credit, ...) és opcional.
CAMPS_UNIVERSALS = [
    "id", "type", "title", "version",
    "data_ultima_actualitzacio", "authors", "llicencia", "tags",
]

# Camps universals que han de ser llistes de cadenes.
CAMPS_ARRAY = {"authors", "tags"}

# ---------------------------------------------------------------- Cores (§2) -
# Els 9 tipus universals. Tancats i compartits per tots els vaults OKF.
TIPUS_UNIVERSALS = [
    "MOC", "Guia", "Glossari", "Protocol", "PaquetLLM",
    "ConvencioNomenclatura", "Llicencia", "Plantilla", "DocumentHandoff",
]

# Tipus considerats "Convenció de Nomenclatura" (font dels tipus de família).
TIPUS_CONVENCIO = {"ConvencioNomenclatura"}

# ---------------------------------------------------------------- Cores (§4) -
# Enums comuns. Opcionals: si no es declaren, s'assumeix el valor per defecte.
ENUM_VISIBILITAT = {"publica", "interna", "restringida", "personal", "externa"}
VISIBILITAT_DEFECTE = "interna"
ENUM_ESTAT = {"vigent", "esborrany", "obsolet", "arxivat"}
ESTAT_DEFECTE = "vigent"

# ---------------------------------------------------------------- Config ----
CARPETES_EXCLUIRE = {
    ".git", ".obsidian", ".trash", "EINES", "__pycache__", "_font",
    "_materials", "_staging", "00-documentacio", "06-comunitat",
    ".github", "tests",
}

# Fitxers que NO són nodes OKF i s'exclouen de la validació.
FITXERS_EXCLUIRE = {"README.md", "LICENSE.md", "CHANGELOG.md", "CONTRIBUTING.md"}

# Patró genèric d'ID segons la Convenció: {CODI}-{ÀMBIT}-{NN}.
PATRO_ID = r"^[A-Z0-9]+(-[A-Z0-9]+)+-\d{2}$"

# Terminologia LOMLOE (configurable). Llista buida = comprovació inactiva.
TERMES_LOMLOE = []

# Marcs legals vàlids (configurable). Llista buida = comprovació inactiva.
MARCS_LEGAL_VALID = []

PATRO_VERSION = r"^V\d+\.\d+(\.\d+)?(-[A-Za-zÀ-ÿ]+)?$"

CODIS_ERROR = {
    "Y001": ("YAML absent o mal format", "🔴 Crític"),
    "Y002": ("Camp universal absent o buit", "🔴 Crític"),
    "Y003": ("Camp 'credit' absent en tipus de família que el requereix", "🔴 Crític"),
    "Y004": ("Tipus no vàlid (no universal ni declarat a la Convenció)", "🔴 Crític"),
    "Y005": ("ID no segueix el patró de la Convenció", "🟠 Alta"),
    "Y006": ("ID duplicat", "🔴 Crític"),
    "Y007": (f"Tags sense prefix '{PREFIX_TAG}' o mal formats", "🟡 Mitjana"),
    "Y008": ("Data amb format incorrecte", "🟡 Mitjana"),
    "Y009": ("Versió amb format incorrecte", "🟡 Mitjana"),
    # Y010 / Y011: reservats per a nodes Skill d'Hermes (no aplicables al kit).
    "Y012": ("Terminologia LOMLOE detectada", "🔴 Crític"),
    "Y013": ("Marc legal incorrecte", "🔴 Crític"),
    "Y014": ("Vault sense MOC a l'arrel", "🔴 Crític"),
    "Y015": ("Vault sense DocumentHandoff", "🔴 Crític"),
    "Y016": ("Vault sense ConvencioNomenclatura", "🔴 Crític"),
    "Y017": ("Camp 'credit' en un tipus universal", "🔴 Crític"),
    "Y018": ("Enllaç intern relatiu trencat", "🟠 Alta"),
    "Y019": ("Wikilink [[...]] prohibit", "🟠 Alta"),
    "Y020": ("Valor de 'visibilitat' fora de l'enum del Core", "🟠 Alta"),
    "Y021": ("Valor de 'estat' fora de l'enum del Core", "🟠 Alta"),
    "Y022": ("Privacitat: dades personals amb visibilitat 'publica'", "🔴 Crític"),
    "Y023": ("Fitxer amb BOM UTF-8", "🟡 Mitjana"),
    "Y024": ("Claus YAML duplicades", "🔴 Crític"),
    "Y025": ("El camp 'type' no és una cadena", "🔴 Crític"),
    "Y026": ("Camp array (authors/tags) amb tipus incorrecte", "🔴 Crític"),
    "Y030": ("Criteri al frontmatter sense àncora al cos", "🟠 Alta"),
    "Y031": ("Àncora al cos sense criteri al frontmatter", "🟠 Alta"),
    "Y035": ("Àlies declarats amb canònics conflictius entre Convencions", "🟠 Alta"),
    "Y036": ("Valor no vàlid per a 'naturalesa'", "🟡 Mitjana"),
}


# =============================================================================
# CÀRREGA YAML AMB DETECCIÓ DE CLAUS DUPLICADES
# =============================================================================

class ClausDuplicades(Exception):
    """Es llança quan el YAML té una clau repetida."""


class CarregadorYaml(yaml.SafeLoader):
    """SafeLoader que detecta claus duplicades al frontmatter."""


def _constructor_mapping(loader, node, deep=False):
    """Constructor de mapes que fa fallar el YAML si una clau es repeteix."""
    mapping = {}
    for key_node, value_node in node.value:
        clau = loader.construct_object(key_node, deep=deep)
        if clau in mapping:
            raise ClausDuplicades(f"Clau duplicada: '{clau}'")
        mapping[clau] = loader.construct_object(value_node, deep=deep)
    return mapping


CarregadorYaml.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _constructor_mapping
)


# =============================================================================
# FUNCIONS DE DETECCIÓ I EXTRACCIÓ
# =============================================================================

def detectar_ruta_vault():
    """Ruta per defecte: l'exemple mínim del kit si existeix; si no, el cwd."""
    candidats = [
        Path(__file__).resolve().parent.parent / "05-exemples-minims" / "vault-de-3-nodes",
        Path.cwd(),
    ]
    for c in candidats:
        if c.is_dir():
            return str(c)
    return str(Path.cwd())


RUTA_DEFAULT = detectar_ruta_vault()


def extreure_yaml(ruta_fitxer):
    """
    Extreu el frontmatter YAML d'un fitxer .md.

    Retorna (data, errors): data és el diccionari YAML o None; errors és una
    llista de tuples (codi, descripció, acció) acumulades (BOM, YAML mal
    format, claus duplicades, ...).
    """
    errors = []

    try:
        with open(ruta_fitxer, "rb") as f:
            bytes_cont = f.read()
    except Exception as e:
        return None, [("Y001", f"No es pot llegir el fitxer: {e}", "Comprovar permisos i ruta")]

    if bytes_cont.startswith(b"\xef\xbb\xbf"):
        errors.append((
            "Y023",
            "El fitxer comença amb un BOM UTF-8 (\\ufeff)",
            "Eliminar el BOM (p. ex. reobrir en UTF-8 sense BOM) abans de validar",
        ))
        contingut = bytes_cont.decode("utf-8-sig", errors="replace")
    else:
        contingut = bytes_cont.decode("utf-8", errors="replace")

    linies = contingut.split("\n")
    if not linies or linies[0].strip() != "---":
        return None, errors + [
            ("Y001", "El fitxer no comença amb '---' (o té un BOM sense eliminar)", "Afegir el bloc YAML amb delimitadors '---'")
        ]

    final = -1
    for i in range(1, len(linies)):
        if linies[i].strip() == "---":
            final = i
            break

    if final == -1:
        return None, errors + [
            ("Y001", "No es troba el '---' de tancament del YAML", "Tancar el bloc YAML amb '---'")
        ]

    bloc_yaml = "\n".join(linies[1:final])
    try:
        data = yaml.load(bloc_yaml, Loader=CarregadorYaml)
        if not isinstance(data, dict):
            return None, errors + [
                ("Y001", "El YAML no és un diccionari (és un escalar o una llista)", "El frontmatter ha de ser un mapa de claus: valor")
            ]
        return data, errors
    except ClausDuplicades as e:
        return None, errors + [
            ("Y024", f"Claus YAML duplicades al frontmatter ({e})", "Deixar una sola aparició de cada clau")
        ]
    except yaml.YAMLError as e:
        return None, errors + [
            ("Y001", f"YAML mal format: {e}", "Corregir la sintaxi YAML del frontmatter")
        ]


def es_node_okf(ruta_fitxer):
    """Un fitxer és node OKF si no és cap dels fitxers exclosos per nom."""
    nom_fitxer = os.path.basename(ruta_fitxer)
    return nom_fitxer not in FITXERS_EXCLUIRE


def trobar_fitxers_md(ruta_vault):
    """Recorre el vault i retorna els fitxers .md que són nodes OKF."""
    fitxers = []
    for root, dirs, files in os.walk(ruta_vault):
        dirs[:] = [d for d in dirs if d not in CARPETES_EXCLUIRE]
        for f in files:
            if f.endswith(".md"):
                ruta = os.path.join(root, f)
                if es_node_okf(ruta):
                    fitxers.append(ruta)
    return sorted(fitxers)


# =============================================================================
# CONVENCIÓ DE NOMENCLATURA: TIPUS DE FAMÍLIA
# =============================================================================

def extreure_cos_md(ruta_fitxer):
    """Retorna el cos del .md (tot el que no és frontmatter)."""
    try:
        with open(ruta_fitxer, "rb") as f:
            contingut = f.read().decode("utf-8-sig", errors="replace")
    except Exception:
        return ""
    linies = contingut.split("\n")
    if not linies or linies[0].strip() != "---":
        return contingut
    final = -1
    for i in range(1, len(linies)):
        if linies[i].strip() == "---":
            final = i
            break
    if final == -1:
        return ""
    return "\n".join(linies[final + 1:])


def extreure_tipus_convencio(contingut):
    """
    Extreu els tipus declarats per una Convenció de Nomenclatura.

    Només es miren les taules sota seccions el títol de les quals conté
    "tipus" (per exemple "## 2 · 9 tipus universals", "## 2 · Tipus de node
    vàlids" o "### 8.3 · Tipus de família del perfil ..."). Cada fila

        | `Tipus` | Descripció breu ... |

    declara un tipus. La descripció es guarda per detectar exigències de
    `credit` (fila amb "requereix" i "credit").
    """
    tipus = {}
    seccio_actual = ""
    dins_taula_validada = False

    for line in contingut.splitlines():
        m_cap = re.match(r"^(#{1,6})\s+(.*)", line)
        if m_cap:
            seccio_actual = m_cap.group(2).lower()
            dins_taula_validada = (
                "tipus" in seccio_actual
                and "àlies" not in seccio_actual
                and "alias" not in seccio_actual
            )
            continue

        if not dins_taula_validada:
            continue

        if line.strip().startswith("|"):
            m = re.match(r"^\|\s*`([^`]+)`\s*\|(.*)$", line)
            if m:
                tipus[m.group(1).strip()] = m.group(2).lower()

    return tipus


def llegir_tipus_de_les_convencions(fitxers, yaml_per_ruta):
    """
    Recull els tipus declarats per totes les Convencions del vault.

    Retorna ({tipus: descripcio}, convencions_trobades).
    Els tipus universals hi són declarats pels Cores; els tipus de família
    ho poden estar per qualsevol Convenció del vault (plantilla, perfil...).
    """
    declarats = {}
    convencions = []
    for ruta in fitxers:
        data = yaml_per_ruta.get(ruta, {}).get("data")
        if not isinstance(data, dict):
            continue
        tipus_node = data.get("type")
        if isinstance(tipus_node, str) and tipus_node in TIPUS_CONVENCIO:
            convencions.append(ruta)
            cos = extreure_cos_md(ruta)
            for t, desc in extreure_tipus_convencio(cos).items():
                declarats[t] = desc
    return declarats, convencions


def extreure_aliases_convencio(contingut):
    """
    Extreu els àlies de tipus declarats per una Convenció de Nomenclatura.

    Llegeix les taules sota seccions amb "àlies" (o "alias") al títol
    (per exemple "## 3 · Àlies de tipus"). Cada fila

        | `Activitat` | `FitxaAEA` |

    declara un àlies -> tipus canònic.
    """
    aliases = {}
    seccio_actual = ""
    dins_taula_aliases = False

    for line in contingut.splitlines():
        m_cap = re.match(r"^(#{1,6})\s+(.*)", line)
        if m_cap:
            seccio_actual = m_cap.group(2).lower()
            dins_taula_aliases = (
                "àlies" in seccio_actual or "alias" in seccio_actual
            )
            continue

        if not dins_taula_aliases:
            continue

        if line.strip().startswith("|"):
            m = re.match(r"^\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|", line)
            if m:
                aliases[m.group(1).strip()] = m.group(2).strip()

    return aliases


def llegir_aliases_de_les_convencions(fitxers, yaml_per_ruta):
    """
    Recull els àlies declarats per totes les Convencions del vault.

    Retorna (aliases, errors_conflictes):
    - aliases: {àlies: tipus_canonic} (el primer declarat guanya si coincideix).
    - errors_conflictes: llista de (ruta, "Y035", descripció, acció) quan el
      mateix àlies es declara amb canònics diferents en convencions diferents
      (error de configuració, no de node).
    """
    aliases = {}
    conflictes = []
    for ruta in fitxers:
        data = yaml_per_ruta.get(ruta, {}).get("data")
        if not isinstance(data, dict):
            continue
        tipus_node = data.get("type")
        if isinstance(tipus_node, str) and tipus_node in TIPUS_CONVENCIO:
            cos = extreure_cos_md(ruta)
            for alias, canonic in extreure_aliases_convencio(cos).items():
                if alias in aliases and aliases[alias] != canonic:
                    conflictes.append((
                        ruta, "Y035",
                        f"Àlies '{alias}' declarat amb canònics diferents: "
                        f"'{aliases[alias]}' vs '{canonic}'",
                        "Unificar el canònic de l'àlies a totes les Convencions",
                    ))
                elif alias not in aliases:
                    aliases[alias] = canonic
    return aliases, conflictes


def construir_tipus_valid(declarats_convencio):
    """
    Tipus vàlids = 9 universals + tipus de família declarats a la Convenció.

    Retorna (tipus_valid, tipus_familia, tipus_credit).
    - tipus_familia: els declarats que no són universals.
    - tipus_credit: els de família la Convenció dels quals declara que
      requereixen `credit` (descripció amb "requereix" i "credit").
      Els universals MAI exigeixen `credit`.
    """
    tipus_familia = {
        t: desc for t, desc in declarats_convencio.items()
        if t not in TIPUS_UNIVERSALS
    }
    tipus_credit = {
        t for t, desc in tipus_familia.items()
        if "requereix" in desc and "credit" in desc
    }
    tipus_valid = set(TIPUS_UNIVERSALS) | set(tipus_familia)
    return sorted(tipus_valid), tipus_familia, tipus_credit


# =============================================================================
# ANÀLISI DEL COS: ENLLAÇOS I WIKILINKS
# =============================================================================

def analitzar_enllacos(ruta_fitxer):
    """
    Comprova els enllaços del cos (fora de blocs de codi ```).

    Retorna (enllacos_trencats, wikilinks): llistes de (destí, línia) que
    no compleixen la sintaxi del Core §6.
    """
    cos = extreure_cos_md(ruta_fitxer)
    directori = os.path.dirname(ruta_fitxer)
    trencats = []
    wikilinks = []
    in_fence = False

    for num, line in enumerate(cos.split("\n"), 1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        # Wikilinks [[...]]: prohibits a tot el cos (fora de blocs de codi).
        for m in re.finditer(r"\[\[([^\]]+)\]\]", line):
            wikilinks.append((m.group(0), num))

        # Enllaços markdown [text](destí)
        for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)\)", line):
            desti = m.group(1)
            if desti.startswith(("http://", "https://", "mailto:", "#")):
                continue
            # Un fragment '#...' no forma part de la ruta del fitxer.
            ruta_desti = desti.split("#", 1)[0]
            if not ruta_desti:
                continue
            p_resolt = os.path.normpath(os.path.join(directori, ruta_desti))
            if not os.path.exists(p_resolt):
                trencats.append((desti, num))

    return trencats, wikilinks


# =============================================================================
# VALIDACIÓ DE NODE
# =============================================================================

def validar_data(data_str):
    if not isinstance(data_str, str):
        return False
    try:
        datetime.datetime.strptime(data_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def es_buit(v):
    """Un valor compta com a buit si és None, cadena en blanc o llista buida."""
    if v is None:
        return True
    if isinstance(v, str):
        return not v.strip()
    if isinstance(v, list):
        return len(v) == 0
    return False


def comprovar_coherencia_cataleg(node_yaml, cos, ruta_node):
    """
    Comprova la coherència entre el frontmatter i el cos d'un CatalegCurricular
    (RFC-OKF-02, Fase 3):

    - Cada codi X.Y del camp `criteris:` ha de tenir la seva àncora
      <a id="ca-X-Y"></a> al cos (si falta -> Y030).
    - Cada àncora del cos ha de correspondre a un criteri del frontmatter
      (si sobra -> Y031).

    Retorna la llista de (codi, descripció, acció).
    """
    errors = []

    crits = node_yaml.get("criteris") or {}
    codis_fm = set()
    if isinstance(crits, dict):
        for llista in crits.values():
            if isinstance(llista, list):
                codis_fm |= {str(c) for c in llista}

    ancres = set(re.findall(r"<a id=\"ca-([0-9]+-[0-9]+)\"></a>", cos or ""))

    for codi in sorted(codis_fm):
        clau = str(codi).replace(".", "-")
        if clau not in ancres:
            errors.append((
                "Y030",
                f"Criteri '{codi}' al frontmatter sense àncora "
                f"<a id=\"ca-{clau}\"></a> al cos",
                f"Afegir l'àncora <a id=\"ca-{clau}\"></a> a la fila del criteri al cos",
            ))

    for clau in sorted(ancres):
        codi_txt = clau.replace("-", ".", 1)
        if codi_txt not in codis_fm:
            errors.append((
                "Y031",
                f"Àncora <a id=\"ca-{clau}\"></a> al cos sense criteri "
                f"'{codi_txt}' al frontmatter",
                f"Afegir '{codi_txt}' al camp `criteris:` del frontmatter o treure l'àncora",
            ))

    return errors


def validar_node(ruta_fitxer, yaml_data, ids_vists, tipus_valid, tipus_credit, errors_enllacos, aliases=None):
    """
    Valida un node. Retorna la llista d'errors (codi, descripció, acció).
    """
    errors = []
    if yaml_data is None:
        return errors

    # ---- 8 camps universals (Cores §3) -------------------------------
    for camp in CAMPS_UNIVERSALS:
        valor = yaml_data.get(camp)
        if es_buit(valor):
            errors.append((
                "Y002",
                f"Camp universal '{camp}' absent o buit",
                f"Afegir el camp '{camp}' amb un valor no buit al YAML",
            ))

    # ---- Tipus d'array (Cores §3: authors i tags són arrays) ---------
    for camp in CAMPS_ARRAY:
        valor = yaml_data.get(camp)
        if valor is not None and not es_buit(valor) and not isinstance(valor, list):
            errors.append((
                "Y026",
                f"El camp '{camp}' ha de ser una llista de cadenes (ara és {type(valor).__name__})",
                f"Convertir '{camp}' a llista YAML, ex: - \"valor\"",
            ))

    # ---- Camp type: ha de ser cadena (mai llista/diccionari) ---------
    tipus = yaml_data.get("type")
    if not isinstance(tipus, str):
        if not es_buit(tipus):
            errors.append((
                "Y025",
                f"El camp 'type' ha de ser una cadena (ara és {type(tipus).__name__})",
                "Corregir 'type' a una cadena, ex: 'Guia'",
            ))
        tipus = ""

    node_id = yaml_data.get("id")

    # ---- Àlies: normalització transparent (RFC-OKF-02, Fase 3) --------
    if tipus and tipus not in tipus_valid and aliases and tipus in aliases:
        tipus = aliases[tipus]

    # ---- Tipus vàlid: universal o declarat a la Convenció ------------
    if tipus and tipus not in tipus_valid:
        errors.append((
            "Y004",
            f"Tipus '{tipus}' no és un dels {len(tipus_valid)} tipus vàlids "
            f"(9 universals del Core + tipus de família de la Convenció)",
            "Usar un tipus universal o declarar-lo a la Convenció de Nomenclatura",
        ))

    # ---- credit: mai a universals; obligatori només si la Convenció ho declara
    if tipus:
        if "credit" in yaml_data and tipus in TIPUS_UNIVERSALS:
            errors.append((
                "Y017",
                f"El camp 'credit' no es pot usar en el tipus universal '{tipus}' "
                "(el Core el reserva per a tipus de família de marcs amb crèdits)",
                "Treure el camp 'credit' del node o canviar-ne el tipus",
            ))
        elif tipus in tipus_credit and es_buit(yaml_data.get("credit")):
            errors.append((
                "Y003",
                f"Camp 'credit' absent en el tipus de família '{tipus}', que la "
                "Convenció declara com a tipus de crèdit",
                "Afegir el camp 'credit'",
            ))

    # ---- naturalesa (camp LOE del RFC-OKF-02; opcional, per defecte 'analitica')
    naturalesa = yaml_data.get("naturalesa")
    if not es_buit(naturalesa):
        if not isinstance(naturalesa, str) or naturalesa not in ("analitica", "sintesi"):
            errors.append((
                "Y036",
                f"Valor no vàlid per a 'naturalesa': '{naturalesa}' "
                "(permesos: 'analitica', 'sintesi')",
                "Usar 'analitica' o 'sintesi' (o treure el camp)",
            ))

    # ---- Coherència catàleg: frontmatter ↔ àncores (RFC-OKF-02) ------
    if tipus == "CatalegCurricular":
        errors.extend(comprovar_coherencia_cataleg(
            yaml_data, extreure_cos_md(ruta_fitxer), ruta_fitxer
        ))

    # ---- ID: patró i duplicats ----------------------------------------
    if node_id is not None:
        if not isinstance(node_id, str):
            node_id = str(node_id)
        if not re.match(PATRO_ID, node_id):
            errors.append((
                "Y005",
                f"ID '{node_id}' no segueix el patró '{{CODI}}-{{ÀMBIT}}-{{NN}}' de la Convenció",
                "Corregir l'ID (ex: 'EX-MOC-00')",
            ))
        if node_id in ids_vists:
            errors.append((
                "Y006",
                f"ID '{node_id}' duplicat (també a {ids_vists[node_id]})",
                "Renombrar un dels dos IDs",
            ))
        else:
            ids_vists[node_id] = ruta_fitxer

    # ---- Tags: amb prefix okf/ i llista ---------------------------------
    tags = yaml_data.get("tags")
    if isinstance(tags, list) and tags:
        te_prefix = any(isinstance(t, str) and t.startswith(PREFIX_TAG) for t in tags)
        if not te_prefix:
            errors.append((
                "Y007",
                f"Cap tag comença amb '{PREFIX_TAG}'",
                f"Afegir com a mínim un tag amb prefix '{PREFIX_TAG}<categoria>'",
            ))

    # ---- Data i versió ---------------------------------------------------
    data_act = yaml_data.get("data_ultima_actualitzacio")
    if isinstance(data_act, str) and data_act and not validar_data(data_act):
        errors.append(("Y008", f"Data '{data_act}' no té format ISO 8601", "Corregir la data al format 'YYYY-MM-DD'"))

    versio = yaml_data.get("version")
    if isinstance(versio, str) and versio and not re.match(PATRO_VERSION, versio):
        errors.append((
            "Y009",
            f"Versió '{versio}' no segueix el patró 'V<maj>.<min>[.<patch>][-<estat>]'",
            "Corregir la versió (ex: 'V1.0-Esborrany' o 'V1.0')",
        ))

    # ---- Enums del Core §4 (opcionals; si es declaren, tancats) ----------
    visibilitat = yaml_data.get("visibilitat")
    if visibilitat is not None and visibilitat not in ENUM_VISIBILITAT:
        errors.append((
            "Y020",
            f"Valor de 'visibilitat' '{visibilitat}' no és dels permesos "
            f"({', '.join(sorted(ENUM_VISIBILITAT))})",
            f"Usar un valor de l'enum del Core (per defecte: '{VISIBILITAT_DEFECTE}')",
        ))

    estat = yaml_data.get("estat")
    if estat is not None and estat not in ENUM_ESTAT:
        errors.append((
            "Y021",
            f"Valor de 'estat' '{estat}' no és dels permesos "
            f"({', '.join(sorted(ENUM_ESTAT))})",
            f"Usar un valor de l'enum del Core (per defecte: '{ESTAT_DEFECTE}')",
        ))

    # ---- Privacitat (Cores §4.1) -----------------------------------------
    dades_personals = yaml_data.get("dades_personals")
    anonimitzat = yaml_data.get("anonimitzat")
    te_dades_sensibles = (
        dades_personals is True
        or (anonimitzat is not None and anonimitzat is False)
    )
    if te_dades_sensibles and visibilitat == "publica":
        errors.append((
            "Y022",
            "Node amb dades personals/de menors (dades_personals: true o "
            "anonimitzat: false) amb visibilitat 'publica'",
            "Canviar 'visibilitat' a 'interna' o 'restringida' (o anonimitzar les dades)",
        ))

    # ---- Terminologia LOMLOE / marc legal (configurables) ----------------
    if TERMES_LOMLOE:
        valors_a_cercar = []
        for camp in ("title", "subtitle", "tags"):
            val = yaml_data.get(camp, "")
            if isinstance(val, str):
                valors_a_cercar.append(val)
            elif isinstance(val, list):
                valors_a_cercar.extend(str(v) for v in val)
        text_concatenat = " ".join(valors_a_cercar)
        for terme in TERMES_LOMLOE:
            if terme.lower() in text_concatenat.lower():
                errors.append((
                    "Y012", f"Terminologia LOMLOE detectada: '{terme}'",
                    "Substituir per la terminologia del teu marc legal",
                ))

    marc_legal = yaml_data.get("legal_framework")
    if MARCS_LEGAL_VALID and isinstance(marc_legal, str) and marc_legal not in MARCS_LEGAL_VALID:
        errors.append((
            "Y013", f"Marc legal '{marc_legal}' incorrecte",
            f"Corregir a un dels valors vàlids: {MARCS_LEGAL_VALID}",
        ))

    # ---- Graf: enllaços i wikilinks --------------------------------------
    trencats, wikilinks = errors_enllacos if errors_enllacos else ([], [])
    for desti, num in trencats:
        errors.append((
            "Y018",
            f"Enllaç intern relatiu trencat: '{desti}' (línia {num})",
            "Corregir la ruta relativa o eliminar l'enllaç",
        ))
    for wl, num in wikilinks:
        errors.append((
            "Y019",
            f"Wikilink prohibit: {wl} (línia {num})",
            "Substituir per un enllaç markdown relatiu: [text](./ruta.md)",
        ))

    return errors


# =============================================================================
# COMPROVACIONS ESTRUCTURALS (MOC ARREL, HANDOFF, CONVENCIÓ)
# =============================================================================

def comprovacions_estructurals(ruta_vault, fitxers, yaml_per_ruta):
    """
    Comprova l'estructura mínima d'un vault (Cores §7.1-7.3).

    Només s'apliquen quan l'arrel validada ÉS un vault: conté com a mínim
    un node directament a la seva arrel. Si l'arrel no té cap node directe
    (és una carpeta repositori amb subvaults, com el kit sencer), les
    comprovacions no s'emeten: cada subvault es validarà individualment.
    """
    ruta_vault_abs = os.path.abspath(ruta_vault)
    directes = [
        r for r in fitxers
        if os.path.abspath(os.path.dirname(r)) == ruta_vault_abs
    ]
    if not directes:
        return []

    tipus_a_l_arbre = set()
    tipus_a_l_arrel = set()
    for r in fitxers:
        data = yaml_per_ruta.get(r, {}).get("data")
        if isinstance(data, dict) and isinstance(data.get("type"), str):
            tipus_a_l_arbre.add(data["type"])
            if os.path.abspath(os.path.dirname(r)) == ruta_vault_abs:
                tipus_a_l_arrel.add(data["type"])

    # Sense cap MOC a tot l'arbre no és un vault: és una carpeta de fragments
    # (ex: 01-cores/ amb només les convencions). Les comprovacions estructurals
    # només apliquen a arrels que s'assemblin a un vault.
    if "MOC" not in tipus_a_l_arbre:
        return []

    errors = []
    if "MOC" not in tipus_a_l_arrel:
        errors.append((
            "Y014",
            "El vault no té cap node de tipus 'MOC' a l'arrel",
            "Crear un MOC arrel que indexi el vault (ex: 'EX-MOC-00')",
        ))
    if "DocumentHandoff" not in tipus_a_l_arbre:
        errors.append((
            "Y015",
            "El vault no té cap node de tipus 'DocumentHandoff'",
            "Afegir un node de transferència de context (Cores §7.3)",
        ))
    if not (tipus_a_l_arbre & TIPUS_CONVENCIO):
        errors.append((
            "Y016",
            "El vault no té cap node de tipus 'ConvencioNomenclatura'",
            "Afegir la Convenció de Nomenclatura del vault (Cores §7.2)",
        ))

    return errors


# =============================================================================
# INFORME
# =============================================================================

def generar_informe(resultats, ruta_vault, ruta_sortida):
    total_fitxers = resultats["total_fitxers"]
    fitxers_valids = resultats["fitxers_valids"]
    fitxers_amb_errors = resultats["fitxers_amb_errors"]
    errors_totals = resultats["errors_totals"]
    ids_duplicats = resultats["ids_duplicats"]
    termes_lomloe = resultats["termes_lomloe"]
    fitxers_excloso = resultats["fitxers_excloso"]
    convencions = resultats["convencions"]
    tipus_familia = resultats["tipus_familia"]

    criticos = sum(1 for e in errors_totals if CODIS_ERROR.get(e[1], ("", "🔴 Crític"))[1] == "🔴 Crític")
    alts = sum(1 for e in errors_totals if CODIS_ERROR.get(e[1], ("", "🟠 Alta"))[1] == "🟠 Alta")
    mitjans = sum(1 for e in errors_totals if CODIS_ERROR.get(e[1], ("", "🟡 Mitjana"))[1] == "🟡 Mitjana")

    informe = []
    informe.append("# Informe de Validació YAML — OKF Starter Kit")
    informe.append("")
    informe.append(f"**Data:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    informe.append(f"**Ruta del vault:** `{ruta_vault}`")
    informe.append(f"**Script:** `validar_yaml.py` v{VERSIO_SCRIPT}")
    informe.append("")
    informe.append("## Resum Executiu")
    informe.append("")
    informe.append("| Mètrica | Valor |")
    informe.append("|:--------|:-----:|")
    informe.append(f"| Fitxers .md escanejats (nodes OKF) | {total_fitxers} |")
    informe.append(f"| Fitxers exclosos (no OKF) | {fitxers_excloso} |")
    informe.append(f"| Fitxers amb YAML vàlid | {fitxers_valids} |")
    informe.append(f"| Fitxers amb errors | {fitxers_amb_errors} |")
    informe.append(f"| Errors crítics (🔴) | {criticos} |")
    informe.append(f"| Errors alts (🟠) | {alts} |")
    informe.append(f"| Advertències (🟡) | {mitjans} |")
    informe.append(f"| IDs duplicats detectats | {len(ids_duplicats)} |")
    informe.append(f"| Terminologia LOMLOE | {termes_lomloe} |")
    informe.append(f"| Convencions llegides | {len(convencions)} |")
    informe.append(f"| Tipus de família declarats | {len(tipus_familia)} |")
    informe.append("")

    if tipus_familia:
        informe.append("## Tipus de família declarats a la Convenció")
        informe.append("")
        informe.append("| Tipus | Font |")
        informe.append("|:------|:-----|")
        for t in sorted(tipus_familia):
            informe.append(f"| `{t}` | Convenció del vault |")
        informe.append("")

    if errors_totals:
        informe.append("## Errors Detectats")
        informe.append("")
        informe.append("| # | Fitxer | Codi | Gravetat | Descripció | Acció |")
        informe.append("|:-:|:-------|:----:|:--------:|:-----------|:------|")
        for i, (ruta, codi, desc, accio) in enumerate(errors_totals, 1):
            gravetat = CODIS_ERROR.get(codi, ("", "🔴 Crític"))[1]
            nom_fitxer = os.path.basename(ruta)
            informe.append(f"| {i} | `{nom_fitxer}` | {codi} | {gravetat} | {desc} | {accio} |")
        informe.append("")

    if ids_duplicats:
        informe.append("## IDs Duplicats")
        informe.append("")
        informe.append("| ID | Fitxer 1 | Fitxer 2 |")
        informe.append("|:---|:---------|:---------|")
        for id_dup, rutes in ids_duplicats.items():
            if len(rutes) >= 2:
                informe.append(f"| `{id_dup}` | `{rutes[0]}` | `{rutes[1]}` |")
        informe.append("")

    if not errors_totals:
        informe.append("## ✅ Resultat")
        informe.append("")
        informe.append("Tots els nodes OKF del vault han passat la validació sense errors.")
        informe.append("")

    informe.append("## Recomanacions")
    informe.append("")
    if criticos > 0:
        informe.append("- ⚠️ Hi ha errors crítics que s'han de resoldre abans de continuar.")
    if termes_lomloe > 0:
        informe.append("- 🚨 S'ha detectat terminologia LOMLOE. Substituir-la per la terminologia del teu marc legal.")
    if len(ids_duplicats) > 0:
        informe.append("- 🔴 Hi ha IDs duplicats. Cal renombrar un dels nodes.")
    if not errors_totals:
        informe.append("- El graf està net.")
    informe.append("")
    informe.append("---")
    informe.append(f"Generat per `validar_yaml.py` v{VERSIO_SCRIPT} · OKF Starter Kit")
    informe.append("")

    contingut_informe = "\n".join(informe)
    with open(ruta_sortida, "w", encoding="utf-8") as f:
        f.write(contingut_informe)
    return contingut_informe


# =============================================================================
# MAIN
# =============================================================================

def audit_curricular(vault_path, strict_versio=False):
    """
    Auditoria de cobertura curricular per catàleg (RFC-OKF-02, Fase 3).

    Per a cada CatalegCurricular del vault (excloses les plantilles de
    04-plantilles/), calcula: total CAs del decret, CAs avaluats per fitxes
    analítiques, CAs només a síntesi, orfes, inexistents, mismatch de versió
    (mètrica informativa; deprecated a RFC-OKF-03) i la coherència
    YAML↔àncores (Y030/Y031).

    `strict_versio` és deprecated i no-op (Bloc 14a): el mismatch de versió
    és sempre una mètrica informativa que no afecta el veredicte ni el codi
    de sortida.

    Retorna (linies, exit_code) amb exit_code 0 (tot cobert), 1 (incomplert o
    error) o 2 (només warnings).
    """
    fitxers = trobar_fitxers_md(vault_path)

    yaml_per_ruta = {}
    for r in fitxers:
        data, _errs = extreure_yaml(r)
        yaml_per_ruta[r] = data

    # Àlies declarats per les convencions (per normalitzar el type).
    aliases, _conflictes = llegir_aliases_de_les_convencions(
        fitxers, {r: {"data": d} for r, d in yaml_per_ruta.items()}
    )

    def tipus_normalitzat(d):
        if not isinstance(d, dict):
            return None
        t = d.get("type")
        if isinstance(t, str) and t in aliases:
            return aliases[t]
        return t

    def no_es_plantilla(ruta):
        return "04-plantilles" not in Path(ruta).parts

    # Catàlegs per ruta absoluta.
    catalegs = {}
    for r, d in yaml_per_ruta.items():
        if not no_es_plantilla(r):
            continue
        if isinstance(d, dict) and tipus_normalitzat(d) == "CatalegCurricular":
            criteris = d.get("criteris")
            catalegs[str(Path(r).resolve())] = {
                "version": str(d.get("version", "")),
                "criteris": criteris if isinstance(criteris, dict) else {},
                "fitxes": [],
            }

    # Fitxes per catàleg referenciat (resolució de ruta relativa).
    for r, d in yaml_per_ruta.items():
        if not no_es_plantilla(r):
            continue
        if not (isinstance(d, dict) and tipus_normalitzat(d) == "FitxaAEA"):
            continue
        ref = d.get("cataleg_referencia")
        if not isinstance(ref, str):
            continue
        ref_path = str((Path(r).parent / ref).resolve())
        if ref_path in catalegs:
            catalegs[ref_path]["fitxes"].append((r, d))

    linies = []
    sortida = 0
    coberts = 0
    incomplets = 0
    tots_cas_decret = set()
    tots_cas_coberts = set()

    for ruta_cat, info in sorted(catalegs.items()):
        codis_decret = set()
        for llista in info["criteris"].values():
            if isinstance(llista, list):
                codis_decret |= {str(c) for c in llista}
        total_decret = len(codis_decret)
        tots_cas_decret |= codis_decret

        analitics = set()
        sintesi = set()
        mismatch = 0
        for _r, d in info["fitxes"]:
            codis = {str(c) for c in (d.get("criteris_avaluacio") or [])}
            if d.get("naturalesa") == "sintesi":
                sintesi |= codis
            else:
                analitics |= codis
            v_fitxa = str(d.get("cataleg_versio")) if d.get("cataleg_versio") else ""
            if v_fitxa and info["version"] and v_fitxa != info["version"]:
                mismatch += 1

        tots_cas_coberts |= analitics
        nomes_sintesi = (sintesi & codis_decret) - analitics
        orfes = codis_decret - analitics
        inexistents = analitics - codis_decret

        errors_coherencia = comprovar_coherencia_cataleg(
            {"criteris": info["criteris"]}, extreure_cos_md(ruta_cat), ruta_cat
        )

        verdicte = "COBERT"
        if errors_coherencia:
            verdicte = f"ERROR (Y030/Y031 × {len(errors_coherencia)})"
        elif orfes or inexistents:
            verdicte = "INCOMPLET"
        elif nomes_sintesi:
            verdicte = "WARNING (CAs només a síntesi)"

        if verdicte == "COBERT":
            coberts += 1
        else:
            incomplets += 1

        if verdicte.startswith("ERROR") or verdicte.startswith("INCOMPLET"):
            sortida = max(sortida, 1)
        elif verdicte.startswith("WARNING"):
            sortida = max(sortida, 2)

        linies.append(f"=== Cobertura curricular: {ruta_cat} ===")
        linies.append(f"Versió del catàleg: {info['version']}")
        linies.append(f"Total CAs al decret: {total_decret}")
        linies.append(f"CAs avaluats (analítics): {len(analitics)}")
        linies.append(f"CAs només a síntesi: {len(nomes_sintesi)}")
        linies.append(f"CAs orfes: {len(orfes)}")
        linies.append(f"CAs inexistents: {len(inexistents)}")
        linies.append(f"Mismatch de versió: {mismatch} (deprecated, informatiu)")
        linies.append(f"Verdicte: {verdicte}")
        linies.append("")

    if not catalegs:
        sortida = 2

    linies.append("=== Resum ===")
    linies.append(f"Catàlegs analitzats: {len(catalegs)}")
    linies.append(f"Catàlegs coberts: {coberts}")
    linies.append(f"Catàlegs incomplets: {incomplets}")
    linies.append(f"CAs únics al decret: {len(tots_cas_decret)}")
    linies.append(f"CAs únics coberts: {len(tots_cas_coberts)}")

    return linies, sortida


def main():
    parser = argparse.ArgumentParser(description=f"Validador YAML de vaults OKF (v{VERSIO_SCRIPT})")
    parser.add_argument("--ruta", default=RUTA_DEFAULT)
    parser.add_argument("--output", default=None)
    parser.add_argument("--audit", action="store_true", help="Auditoria de cobertura curricular per catàleg")
    parser.add_argument(
        "--strict-versio", action="store_true",
        help="Deprecated (no-op): el mismatch de versió sempre és un warning",
    )
    args = parser.parse_args()

    if args.strict_versio:
        print("--strict-versio is deprecated; version mismatch is always a warning")

    ruta_vault = args.ruta
    if not os.path.isdir(ruta_vault):
        print(f"ERROR: La ruta '{ruta_vault}' no és un directori vàlid.")
        sys.exit(2)

    fitxers = trobar_fitxers_md(ruta_vault)

    total_md = 0
    for root, dirs, files in os.walk(ruta_vault):
        dirs[:] = [d for d in dirs if d not in CARPETES_EXCLUIRE]
        total_md += sum(1 for f in files if f.endswith(".md"))
    fitxers_excloso = total_md - len(fitxers)

    if not fitxers:
        print(f"ERROR: No s'han trobat nodes OKF a '{ruta_vault}'.")
        sys.exit(2)

    # ---- 1a passada: llegir YAML de tots els fitxers ------------------
    yaml_per_ruta = {}
    errors_totals = []
    fitxers_amb_errors = 0

    for ruta in fitxers:
        data, errors_yaml = extreure_yaml(ruta)
        yaml_per_ruta[ruta] = {"data": data, "errors": errors_yaml}
        if errors_yaml:
            fitxers_amb_errors += 1
            for codi, desc, accio in errors_yaml:
                errors_totals.append((ruta, codi, desc, accio))

    # ---- 2a passada: llegir les Convencions per descobrir tipus de família
    declarats_convencio, convencions = llegir_tipus_de_les_convencions(fitxers, yaml_per_ruta)
    aliases, errors_aliases = llegir_aliases_de_les_convencions(fitxers, yaml_per_ruta)
    tipus_valid, tipus_familia, tipus_credit = construir_tipus_valid(declarats_convencio)

    for ruta_cfg, codi, desc, accio in errors_aliases:
        fitxers_amb_errors += 1
        errors_totals.append((ruta_cfg, codi, desc, accio))

    # ---- 3a passada: anàlisi d'enllaços i validació per node ----------
    ids_vists = {}
    fitxers_valids = 0
    ids_duplicats = dict()
    termes_lomloe_count = 0

    for ruta in fitxers:
        data = yaml_per_ruta[ruta]["data"]
        if data is None:
            continue  # ja s'ha reportat a la 1a passada

        errors_enllacos = analitzar_enllacos(ruta)
        errors_node = validar_node(
            ruta, data, ids_vists, tipus_valid, tipus_credit, errors_enllacos, aliases
        )
        fitxers_amb_errors += 1 if errors_node else 0
        fitxers_valids += 1 if not errors_node else 0
        for codi, desc, accio in errors_node:
            errors_totals.append((ruta, codi, desc, accio))
            if codi == "Y006":
                node_id = str(data.get("id", ""))
                if node_id not in ids_duplicats:
                    ids_duplicats[node_id] = [ids_vists.get(node_id, ruta)]
                ids_duplicats[node_id].append(ruta)
            if codi == "Y012":
                termes_lomloe_count += 1

    # ---- 4a passada: comprovacions estructurals -----------------------
    for codi, desc, accio in comprovacions_estructurals(ruta_vault, fitxers, yaml_per_ruta):
        errors_totals.append((ruta_vault, codi, desc, accio))

    data_avui = datetime.datetime.now().strftime("%Y-%m-%d")
    if args.output:
        ruta_sortida = args.output
    else:
        ruta_sortida = os.path.join(ruta_vault, "EINES", "Scripts", f"informe_validacio_{data_avui}.md")

    if os.path.dirname(ruta_sortida):
        os.makedirs(os.path.dirname(ruta_sortida), exist_ok=True)

    resultats = {
        "total_fitxers": len(fitxers),
        "fitxers_valids": fitxers_valids,
        "fitxers_amb_errors": fitxers_amb_errors,
        "errors_totals": errors_totals,
        "ids_duplicats": ids_duplicats,
        "termes_lomloe": termes_lomloe_count,
        "fitxers_excloso": fitxers_excloso,
        "convencions": convencions,
        "tipus_familia": tipus_familia,
    }

    contingut_informe = generar_informe(resultats, ruta_vault, ruta_sortida)
    print(contingut_informe)
    print(f"\n📄 Informe desat a: {ruta_sortida}")

    exit_final = 1 if errors_totals else 0
    if args.audit:
        linies_audit, exit_audit = audit_curricular(
            ruta_vault, strict_versio=args.strict_versio
        )
        print("\n" + "\n".join(linies_audit))
        exit_final = max(exit_final, exit_audit)

    sys.exit(exit_final)


if __name__ == "__main__":
    main()
