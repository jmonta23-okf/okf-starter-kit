---
id: MP1519-CONV-00
type: ConvencioNomenclatura
title: "Convenció de Nomenclatura del MP 1519"
subtitle: "Tipus vàlids, camps i regles de nomenclatura de l'exemple complet"
cycle: "CFGS Documentació i Administració Sanitàries (SAD)"
center: "Centre educatiu de referència"
academic_year: "2026-2027"
version: "V1.0-Esborrany"
data_ultima_actualitzacio: "2026-10-31"
authors:
  - "Josep Montañà Piqué"
llicencia: "CC BY-SA 4.0"
legal_framework: "Ordre EDU/10/2020 i RD 768/2014 (LOE)"
tags:
  - okf/mp1519
  - okf/convencio
estat: vigent
---

# Convenció de Nomenclatura del MP 1519

> **Propòsit.** Aquest document és la **font de veritat única** de les regles de l'exemple complet: quins tipus de node són vàlids i com es nomenen. És la Convenció que el validador del kit llegeix per acceptar els tipus de família d'aquest mòdul.

---

## 1 · Propòsit

L'exemple complet (`02-exemple-complet/`) desplega el mòdul professional MP 1519 (*Sistemes d'informació i classificació sanitaris*) amb l'arquitectura del OKF Starter Kit: nodes curriculars, fitxes d'activitat, protocol d'avaluació, paquet LLM, guia d'arquitectura i eines tècniques, tots interconnectats.

---

## 2 · Tipus de node vàlids

La llista és **tancada**: els 9 tipus universals del Core FP (MOC, Guia, Glossari, Protocol, PaquetLLM, ConvencioNomenclatura, Llicencia, Plantilla, DocumentHandoff) més els tipus de família declarats aquí:

| Tipus | Descripció breu |
|:---|:---|
| `CatalegCurricular` | Catàleg de resultats d'aprenentatge i criteris d'avaluació del mòdul. |
| `EinaTecnica` | Eina, script o utilitat tècnica del vault (validador CIE-10-ES, ecosistema d'automatització). |
| `FitxaAEA` | Fitxa d'una activitat d'ensenyament-aprenentatge concreta (5 al mòdul). |

**Regla.** Cap node no pot declarar un `type:` que no sigui universal o no consti en aquesta taula. Si cal un tipus nou, s'amplia aquesta Convenció i es puja la versió.

---

## 3 · Camps obligatoris del frontmatter

Tots els nodes han de dur els **8 camps universals** del Core (id, type, title, version, data_ultima_actualitzacio, authors, llicencia, tags), més `estat` i opcionalment `visibilitat`.

---

## 4 · Format del camp id

```
{CODI}-{ÀMBIT}-{NN}
```

Exemples d'aquest mòdul: `MP1519-MOC-00`, `MP1519-CAT-00`, `MP1519-AEA-01`, `MP1519-EINA-VALIDATOR-01`.

---

## 5 · Enllaços interns

Enllaços amb **ruta relativa** des del fitxer origen i extensió `.md`:

```markdown
[Convenció del mòdul](./12_MP1519_Convencio.md)
```

Sintaxi wiki (dobles claudàtors, estil Obsidian) prohibida, com fixa el Core.

---

## 6 · Com ampliar aquesta Convenció

1. Detecta la necessitat: un node no encaixa en cap tipus.
2. Documenta el cas.
3. Proposa l'ampliació: puja la versió i afegeix el tipus a §2.
4. Registra el canvi a la taula de versionatge.
5. Verifica dependències.
6. Segella la nova versió.

---

## Versionatge

| Versió | Data | Descripció |
|:------:|:----:|:-----------|
| V1.0-Esborrany | 2026-10-31 | Creació inicial de la Convenció de l'exemple complet (MP 1519). |

---

## Relacions (Graf)

- Complementa: [MOC del mòdul](./00_MP1519_MOC.md)
- Complementa: [OKF-CORE-FP-00](../01-cores/OKF-CORE-FP-00.md) — core del marc FP (LOE).
