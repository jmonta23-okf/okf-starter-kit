---
id: PLANTILLA-UD-00
type: UnitatDidactica
title: "Unitat [N]: [Títol de la unitat]"
subtitle: "[Descripció breu de la unitat]"
cycle: "[El teu cicle o àmbit]"
center: "El teu centre educatiu"
academic_year: "2026-2027"
version: "V1.0-Esborrany"
data_ultima_actualitzacio: "2026-10-25"  # Canvia per la data d'avui
authors:
  - "El teu nom"
legal_framework: "[El marc legal del teu cicle]"
credit: "C[n]"
modul: "[Codi del mòdul o crèdit]"
durada: "[X hores]"
resultats_aprenentatge:
  - "RA1: [Redacta el resultat d'aprenentatge que treballa la unitat]"
  - "RA2: [Redacta el resultat d'aprenentatge que treballa la unitat]"
criteris_avaluacio:
  - "1.1: [Redacta el criteri d'avaluació vinculat a RA1]"
  - "1.2: [Redacta el criteri d'avaluació vinculat a RA1]"
tags:
  - okf/plantilla
  - okf/unitat
estat: esborrany
visibilitat: publica
---

# Unitat [N]: [Títol de la unitat]

> **Propòsit.** Aquest node descriu una unitat didàctica completa: què s'aprèn, com s'aprèn i com s'avalua. És el node de planificació per excel·lència: agrupa les activitats (FitxaAEA) i els recursos.

> **Quan fer servir aquesta plantilla.** Cada unitat didàctica del crèdit ha de tenir un node com aquest. Crea un node per unitat, no un de sol per a tot el crèdit.

---

## 1 · Presentació

[Descriu la unitat en 3-5 línies: quin lloc ocupa en el crèdit, què aporta, quines idees prèvies requereix.]

## 2 · Objectius

- [Objectiu 1: què ha de saber fer l'alumne en acabar la unitat]
- [Objectiu 2]
- [Objectiu 3]

## 3 · Continguts

- [Concepte 1]
- [Procediment 2]
- [Actitud 3]

## 4 · Activitats

Cada activitat viu en un node `FitxaAEA` separat. Aquesta secció només les enllaça, en ordre:

- [Activitat 1: Introducció al concepte](02_C1_AEA_01.md) — 1 hora
- [Activitat 2: Pràctica guiada](02_C1_AEA_02.md) — 2 hores
- [Activitat 3: Cas pràctic](02_C1_AEA_03.md) — 2 hores

## 5 · Avaluació

| Instrument | Pes | Què avalua |
|:---|:---:|:---|
| [Prova pràctica] | [60%] | [RA1, RA2] |
| [Activitats d'aula] | [40%] | [RA1] |

## 6 · Recursos

- [Material 1: presentació, dossier, enllaç]
- [Material 2]

## 7 · Bibliografia

- [Referència 1]
- [Referència 2]

---

## Exemple de resultats d'aprenentatge i criteris d'avaluació

```yaml
resultats_aprenentatge:
  - "RA1: Identificar els tipus de document administratiu sanitari i la seva finalitat"
  - "RA2: Elaborar documents administratius amb les aplicacions ofimàtiques del centre"
criteris_avaluacio:
  - "1.1: Ha classificat els documents segons el circuit administratiu"
  - "1.2: Ha emplenat els documents amb les dades correctes i sense errades"
  - "2.1: Ha fet servir la plantilla corporativa del centre"
```

**Nota de terminologia.** Els noms dels camps d'aquest frontmatter (`resultats_aprenentatge`, `criteris_avaluacio`) corresponen al marc LOE/FP (Core FP). En àmbits LOMLOE (Core Català) es poden substituir per `competencies_especifiques` i `sabers`, o per `objectius_terminals` i `indicadors_assoliment` en marcs LOGSE. El validador no imposa cap d'aquests camps: són opcionals i lliures.

---

## Historial de versions

| Versió | Data | Descripció |
|:------:|:----:|:-----------|
| V1.0-Esborrany | 2026-10-25 | Creació de la plantilla. |

---

**Fi de la plantilla.**

*Versió V1.0-Esborrany*