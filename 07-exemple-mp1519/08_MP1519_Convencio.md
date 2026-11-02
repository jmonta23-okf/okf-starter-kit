---
id: 07-MP1519-CONV-00
type: ConvencioNomenclatura
title: "Convenció de Nomenclatura del vault MP 1519 (dues capes)"
subtitle: "Tipus vàlids, àlies i regles de nomenclatura"
cycle: "CFGS Documentació i Administració Sanitàries (SAD)"
center: "Centre educatiu de referència"
academic_year: "2026-2027"
version: "V1.0-Esborrany"
data_ultima_actualitzacio: "2026-11-02"
llicencia: "CC BY-SA 4.0"
authors:
  - "Josep Montañà Piqué"
legal_framework: "Ordre EDU/10/2020 i RD 768/2014 (LOE)"
tags:
  - okf/exemple
  - okf/convencio
  - mp1519/dues-capes
estat: vigent
---

# Convenció de Nomenclatura del vault MP 1519 (dues capes)

> **Propòsit.** Aquest document és la **font de veritat única** de les regles del vault d'exemple: quins tipus de node són vàlids, quins àlies s'accepten i com es nomenen els nodes. Cap node no pot existir al vault si no compleix aquestes regles.

---

## 1 · Propòsit

Il·lustrar l'arquitectura curricular de dues capes del RFC-OKF-02 amb un mòdul complet: catàleg normatiu (Capa 1) + fitxes d'activitat referenciades (Capa 2).

---

## 2 · Tipus de node vàlids

### Tipus universals

| Tipus | Descripció breu |
|:---|:---|
| `MOC` | Mapa de continguts del vault. |
| `Guia` | Guia d'ús o tutorial. |
| `Glossari` | Recull de termes i definicions. |
| `Protocol` | Protocol o procediment. |
| `PaquetLLM` | Instruccions per a un agent LLM. |
| `ConvencioNomenclatura` | Regles de nomenclatura del vault. |
| `Llicencia` | Llicència del contingut. |
| `Plantilla` | Plantilla per a un tipus de node. |
| `DocumentHandoff` | Traspàs entre cursos o docents. |

### Tipus de família LOE (declarats en aquest vault)

| Tipus | Descripció breu |
|:---|:---|
| `CatalegCurricular` | Catàleg de RAs i CAs d'un mòdul. |
| `FitxaAEA` | Fitxa d'activitat d'ensenyament-aprenentatge. |
| `EinaTecnica` | Eina o script del vault. |

**Nota sobre `credit`:** aquest vault és LOE; cap tipus no requereix `credit`. Si la descripció d'un tipus digués «requereix credit», el validador activaria Y003 per a aquells nodes sense el camp (la semàntica és per a vaults LOGSE).

**Regla.** Cap node no pot declarar un `type:` que no sigui universal o no consti en aquesta taula. Els àlies de la secció següent encara no són processats pel validador (Fase 3): un node amb `type: Activitat` seria rebutjat (Y004) fins llavors.

---

## 3 · Àlies de tipus

Els àlies permeten acceptar tipus heretats d'altres convencions. El validador els normalitza al tipus canònic.

| Àlies | Tipus canònic |
|:---|:---|
| `Activitat` | `FitxaAEA` |
| `Cataleg` | `CatalegCurricular` |

> **Estat d'implementació:** documental. El validador v1.1.0 no llegeix aquesta secció (la Fase 3 del RFC-OKF-02 implementarà la normalització d'àlies).

---

## 4 · Format del camp id

```
{CODI}-{ÀMBIT}-{NN}
```

Exemples d'aquest vault: `07-MP1519-MOC-00`, `MP1519-CAT-02`, `07-MP1519-AEA-01`.

---

## 5 · Enllaços interns

Enllaços amb **ruta relativa** des del fitxer origen i extensió `.md`:

```markdown
[Catàleg Curricular](./01_MP1519_Cataleg_Curricular.md)
```

Sintaxi wiki (dobles claudàtors, estil Obsidian) prohibida, com fixa el Core.

---

## Versionatge

| Versió | Data | Descripció |
|:------:|:----:|:-----------|
| V1.0-Esborrany | 2026-11-02 | Creació de la Convenció del vault de dues capes (MP 1519). |

---

## Relacions (Graf)

- Complementa: [MOC del vault](./00_MP1519_MOC.md)
- Complementa: [OKF-CORE-FP-00](../01-cores/OKF-CORE-FP-00.md) — core del marc FP (LOE).