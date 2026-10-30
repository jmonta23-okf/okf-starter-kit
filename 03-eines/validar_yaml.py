#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validador_yaml.py — Validador YAML de vaults OKF (OKF Starter Kit)

Versió genèrica i reutilitzable del validador del projecte TCAI-OKF,
adaptada per a qualsevol vault creat amb la plantilla de Convenció
d'aquest kit (`04-plantilles/PLANTILLA-ConvencioNomenclatura.md`).

Diferències respecte al validador TCAI (v1.4.2):
  - Tipus vàlids: només els recomanats a la plantilla (15 tipus, §2).
  - `PaquetLLM` afegit a V1.0.1 (és un tipus de crèdit: requereix `credit`).
  - `MOC` és transversal: no exigeix el camp `credit` (el `credit` només
    és obligatori per a `UnitatDidactica` i `FitxaAEA`).
  - Patró d'ID genèric `{CODI}-{ÀMBIT}-{NN}` (ampliable per tipus).
  - Prefix de tags configurable (`PREFIX_TAG`, per defecte `okf/`).
  - `legal_framework`: llista configurable; buida = no es valida.
  - Terminologia LOMLOE: llista configurable; buida = no es valida
    (aquest kit no imposa cap marc legal; cada vault defineix el seu).
  - Sense regles específiques de nodes `Skill` d'Hermes.
  - V1.0.1: `00-documentacio/` exclosa (és documentació del repositori, no vault).
  - V1.0.2: `06-comunitat/` exclosa (conté documents humans — casos d'ús, guies —, no nodes OKF).

Ús:
    python3 validar_yaml.py [--ruta RUTA] [--output FITXER]

Per defecte l'informe es desa a `RUTA/EINES/Scripts/informe_validacio_*.md`.
"""

import os
import sys
import re
import datetime
import argparse
from pathlib import Path
from collections import defaultdict

try:
    import yaml
except ImportError:
    print("ERROR: Cal instal·lar pyyaml. Executa: pip3 install pyyaml")
    sys.exit(2)


# =============================================================================
# CONSTANTS
# =============================================================================

VERSIO_SCRIPT = "1.0.2"

# Prefix que ha de tenir com a mínim un dels tags de cada node.
PREFIX_TAG = "okf/"


def detectar_ruta_vault():
    """Retorna la ruta per defecte: l'exemple mínim del kit si existeix;
    en cas contrari, el directori de treball actual."""
    candidats = [
        Path(__file__).resolve().parent.parent / "05-exemples-minims" / "vault-de-3-nodes",
        Path.cwd(),
    ]
    for c in candidats:
        if c.is_dir():
            return str(c)
    return str(Path.cwd())


RUTA_DEFAULT = detectar_ruta_vault()

CARPETES_EXCLUIRE = {".git", ".obsidian", ".trash", "EINES", "__pycache__", "_font", "_materials", "_staging", "00-documentacio", "06-comunitat"}

# Fitxers que NO són nodes OKF i s'exclouen de la validació.
# README.md, LICENSE.md, etc.: documents del repositori, no nodes OKF.
FITXERS_EXCLUIRE = {"README.md", "LICENSE.md", "CHANGELOG.md", "CONTRIBUTING.md"}

# Skills funcionals d'Hermes que viuen al vault però NO són nodes OKF.
# El kit no n'inclou cap; es manté la lògica per si algú l'amplia.
SKILLS_FUNCIONALS_EXCLOSES = set()

CAMPS_OBLIGATORIS_GLOBALS = [
    "id", "type", "title", "subtitle", "cycle", "center",
    "academic_year", "version", "data_ultima_actualitzacio",
    "authors", "legal_framework", "tags",
]

# Tipus que pertanyen a un crèdit: exigeixen el camp 'credit'.
# Amplia aquesta llista si la teva Convenció afegeix tipus curriculars.
TIPUS_CREDIT = [
    "UnitatDidactica", "FitxaAEA", "PaquetLLM",
]

# Tipus transversals (agnòstics al domini): no exigeixen 'credit'.
TIPUS_TRANSVERSAL = [
    "MOC", "ConvencioNomenclatura", "Guia", "Protocol", "Glossari",
    "DocumentHandoff", "CatalegCurricular", "CoordinacioCurricular",
    "PlaEstrategic", "EinaTecnica", "NotaDecisions", "Estàndard",
]

TIPUS_VALID = TIPUS_CREDIT + TIPUS_TRANSVERSAL
TOTAL_TIPUS = len(TIPUS_VALID)

# Patró genèric d'ID segons la plantilla: {CODI}-{ÀMBIT}-{NN}.
# Exemples: EX-MOC-00, C1-UD1-00, C1-AEA-01, PLANTILLA-CONVENCIO-00.
# Es pot endurir per tipus substituint l'entrada corresponent.
PATRO_ID = r"^[A-Z0-9]+(-[A-Z0-9]+)+-\d{2}$"
PATRONS_ID = {t: PATRO_ID for t in TIPUS_VALID}

# Terminologia LOMLOE (configurable). Si la llista és buida, no es valida.
# Qui treballi amb marcs anteriors (p. ex. LOGSE) pot omplir-la, per exemple:
# TERMES_LOMLOE = ["Criteris d'Avaluació", "Sabers Bàsics", "Competències Específiques",
#                  "Situacions d'Aprenentatge", "Resultats d'Aprenentatge"]
TERMES_LOMLOE = []

# Marcs legals vàlids (configurable). Si la llista és buida, no es valida.
# Per tancar la llista: MARCS_LEGAL_VALID = ["Decret 203/1997 (DOGC núm. 2464)"]
MARCS_LEGAL_VALID = []

PATRO_VERSION = r"^V\d+\.\d+(\.\d+)?(-[A-Za-zÀ-ÿ]+)?$"

CODIS_ERROR = {
    "Y001": ("YAML absent o mal format", "🔴 Crític"),
    "Y002": ("Camp obligatori absent", "🔴 Crític"),
    "Y003": ("Camp 'credit' absent en node de crèdit", "🔴 Crític"),
    "Y004": ("Tipus no vàlid", "🔴 Crític"),
    "Y005": ("ID no segueix el patró del seu tipus", "🟠 Alta"),
    "Y006": ("ID duplicat", "🔴 Crític"),
    "Y007": (f"Tags sense prefix '{PREFIX_TAG}'", "🟡 Mitjana"),
    "Y008": ("Data amb format incorrecte", "🟡 Mitjana"),
    "Y009": ("Versió amb format incorrecte", "🟡 Mitjana"),
    # Y010/Y011: reservats per a nodes Skill d'Hermes (no aplicables al kit)
    "Y012": ("Terminologia LOMLOE detectada", "🔴 Crític"),
    "Y013": ("Marc legal incorrecte", "🔴 Crític"),
}


# =============================================================================
# FUNCIONS DE DETECCIÓ
# =============================================================================

def es_format_hermes(ruta_fitxer):
    """
    Detecta si un fitxer té format Hermes (name: en lloc de id:).
    """
    try:
        with open(ruta_fitxer, "r", encoding="utf-8") as f:
            contingut = f.read()
    except Exception:
        return False

    linies = contingut.split("\n")
    if not linies or linies[0].strip() != "---":
        return False

    final = -1
    for i in range(1, len(linies)):
        if linies[i].strip() == "---":
            final = i
            break

    if final == -1:
        return False

    bloc_yaml = "\n".join(linies[1:final])
    try:
        data = yaml.safe_load(bloc_yaml)
        if isinstance(data, dict):
            return "name" in data and "id" not in data
    except yaml.YAMLError:
        return False

    return False


def es_node_okf(ruta_fitxer):
    """
    Determina si un fitxer és un node OKF que s'ha de validar.
    """
    nom_fitxer = os.path.basename(ruta_fitxer)

    if nom_fitxer in FITXERS_EXCLUIRE:
        return False

    if nom_fitxer in SKILLS_FUNCIONALS_EXCLOSES:
        return False

    if es_format_hermes(ruta_fitxer):
        return False

    return True


def trobar_fitxers_md(ruta_vault):
    """Recorre el vault i retorna només els fitxers que són nodes OKF."""
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
# FUNCIONS DE VALIDACIÓ
# =============================================================================

def extreure_yaml(ruta_fitxer):
    try:
        with open(ruta_fitxer, "r", encoding="utf-8") as f:
            contingut = f.read()
    except Exception as e:
        return None, f"No es pot llegir el fitxer: {e}"

    linies = contingut.split("\n")
    if not linies or linies[0].strip() != "---":
        return None, "El fitxer no comença amb '---'"

    final = -1
    for i in range(1, len(linies)):
        if linies[i].strip() == "---":
            final = i
            break

    if final == -1:
        return None, "No es troba el '---' de tancament del YAML"

    bloc_yaml = "\n".join(linies[1:final])
    try:
        data = yaml.safe_load(bloc_yaml)
        if not isinstance(data, dict):
            return None, "El YAML no és un diccionari"
        return data, None
    except yaml.YAMLError as e:
        return None, f"YAML mal format: {e}"


def validar_data(data_str):
    if not isinstance(data_str, str):
        return False
    try:
        datetime.datetime.strptime(data_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validar_node(ruta_fitxer, yaml_data, ids_vists):
    errors = []
    if yaml_data is None:
        return errors

    for camp in CAMPS_OBLIGATORIS_GLOBALS:
        if camp not in yaml_data or yaml_data[camp] is None:
            errors.append(("Y002", f"Camp obligatori '{camp}' absent", f"Afegir el camp '{camp}' al YAML"))

    tipus = yaml_data.get("type", "")
    node_id = yaml_data.get("id", "")

    if tipus in TIPUS_CREDIT:
        if "credit" not in yaml_data or yaml_data["credit"] is None:
            errors.append(("Y003", "Camp 'credit' absent en node de crèdit", "Afegir el camp 'credit'"))

    if tipus and tipus not in TIPUS_VALID:
        errors.append((
            "Y004",
            f"Tipus '{tipus}' no és un dels {TOTAL_TIPUS} tipus vàlids",
            "Canviar a un tipus de la llista tancada de la teva Convenció"
        ))

    if node_id and tipus in PATRONS_ID:
        patro = PATRONS_ID[tipus]
        if not re.match(patro, str(node_id)):
            errors.append((
                "Y005",
                f"ID '{node_id}' no segueix el patró '{patro}' del tipus '{tipus}'",
                "Corregir l'ID segons el patró {CODI}-{ÀMBIT}-{NN} de la teva Convenció"
            ))

    if node_id:
        if node_id in ids_vists:
            errors.append(("Y006", f"ID '{node_id}' duplicat (també a {ids_vists[node_id]})", "Renombrar un dels dos IDs"))
        else:
            ids_vists[node_id] = ruta_fitxer

    tags = yaml_data.get("tags", [])
    if tags:
        if isinstance(tags, list):
            te_prefix = any(str(t).startswith(PREFIX_TAG) for t in tags)
            if not te_prefix:
                errors.append(("Y007", f"Cap tag comença amb '{PREFIX_TAG}'", f"Afegir com a mínim un tag amb prefix '{PREFIX_TAG}<categoria>'"))
        else:
            errors.append(("Y007", "El camp 'tags' no és una llista", "Convertir 'tags' a una llista YAML"))

    data_act = yaml_data.get("data_ultima_actualitzacio", "")
    if data_act and not validar_data(str(data_act)):
        errors.append(("Y008", f"Data '{data_act}' no té format ISO 8601", "Corregir la data al format 'YYYY-MM-DD'"))

    versio = yaml_data.get("version", "")
    if versio and not re.match(PATRO_VERSION, str(versio)):
        errors.append((
            "Y009",
            f"Versió '{versio}' no segueix el patró 'V<maj>.<min>[.<patch>][-<estat>]'",
            "Corregir la versió (ex: 'V1.0-Esborrany' o 'V1.0')"
        ))

    if TERMES_LOMLOE:
        valors_a_cercar = []
        for camp in ["title", "subtitle", "tags"]:
            val = yaml_data.get(camp, "")
            if isinstance(val, str):
                valors_a_cercar.append(val)
            elif isinstance(val, list):
                valors_a_cercar.extend([str(v) for v in val])

        text_concatenat = " ".join(valors_a_cercar)
        for terme in TERMES_LOMLOE:
            if terme.lower() in text_concatenat.lower():
                errors.append(("Y012", f"Terminologia LOMLOE detectada: '{terme}'", "Substituir per la terminologia del teu marc legal"))

    marc_legal = yaml_data.get("legal_framework", "")
    if MARCS_LEGAL_VALID and marc_legal and str(marc_legal) not in MARCS_LEGAL_VALID:
        errors.append(("Y013", f"Marc legal '{marc_legal}' incorrecte", f"Corregir a un dels valors vàlids: {MARCS_LEGAL_VALID}"))

    return errors


def generar_informe(resultats, ruta_vault, ruta_sortida):
    total_fitxers = resultats["total_fitxers"]
    fitxers_valids = resultats["fitxers_valids"]
    fitxers_amb_errors = resultats["fitxers_amb_errors"]
    errors_totals = resultats["errors_totals"]
    ids_duplicats = resultats["ids_duplicats"]
    termes_lomloe = resultats["termes_lomloe"]
    fitxers_excloso = resultats["fitxers_excloso"]

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

def main():
    parser = argparse.ArgumentParser(description=f"Validador YAML de vaults OKF (v{VERSIO_SCRIPT})")
    parser.add_argument("--ruta", default=RUTA_DEFAULT)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

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

    ids_vists = {}
    errors_totals = []
    fitxers_valids = 0
    fitxers_amb_errors = 0
    ids_duplicats = defaultdict(list)
    termes_lomloe_count = 0

    for ruta in fitxers:
        yaml_data, error_yaml = extreure_yaml(ruta)
        if yaml_data is None:
            errors_totals.append((ruta, "Y001", error_yaml or "YAML no llegit", "Corregir o afegir el bloc YAML"))
            fitxers_amb_errors += 1
            continue

        errors_node = validar_node(ruta, yaml_data, ids_vists)
        if errors_node:
            fitxers_amb_errors += 1
            for codi, desc, accio in errors_node:
                errors_totals.append((ruta, codi, desc, accio))
                if codi == "Y006":
                    node_id = yaml_data.get("id", "")
                    if node_id not in ids_duplicats:
                        ids_duplicats[node_id].append(ids_vists.get(node_id, ruta))
                    ids_duplicats[node_id].append(ruta)
                if codi == "Y012":
                    termes_lomloe_count += 1
        else:
            fitxers_valids += 1

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
    }

    contingut_informe = generar_informe(resultats, ruta_vault, ruta_sortida)
    print(contingut_informe)
    print(f"\n📄 Informe desat a: {ruta_sortida}")

    sys.exit(1 if errors_totals else 0)


if __name__ == "__main__":
    main()