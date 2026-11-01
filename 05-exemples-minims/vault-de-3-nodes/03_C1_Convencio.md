---
id: C1-CONV-00
type: ConvencioNomenclatura
title: "Convenció de Nomenclatura del vault C1"
subtitle: "Tipus vàlids, camps i regles de nomenclatura del vault d'exemple"
cycle: "CFGM Cures Auxiliars d'Infermeria (TCAI)"
center: "El teu centre educatiu"
academic_year: "2026-2027"
version: "V1.0-Esborrany"
data_ultima_actualitzacio: "2026-10-31"
authors:
  - "El teu nom"
llicencia: "CC BY-SA 4.0"
legal_framework: "Decret 203/1997 (DOGC núm. 2464)"
tags:
  - okf/exemple
  - okf/convencio
estat: vigent
---

# Convenció de Nomenclatura del vault C1

> **Propòsit.** Aquest document és la **font de veritat única** de les regles del vault d'exemple: quins tipus de node són vàlids, quins camps han de dur i com es nomenen. Cap node no pot existir al vault si no compleix aquestes regles.

---

## 1 · Propòsit

Il·lustrar amb un vault mínim de 3 nodes (ara 5 amb la Convenció i l'handoff) com s'aplica el OKF Starter Kit, amb els 8 camps universals i la sintaxi d'enllaç del Core.

---

## 2 · Tipus de node vàlids

La llista és **tancada**: els tipus universals del Core (MOC, Guia, Glossari, Protocol, PaquetLLM, ConvencioNomenclatura, Llicencia, Plantilla, DocumentHandoff) més els tipus de família declarats aquí:

| Tipus | Descripció breu |
|:---|:---|
| `MOC` | Map of Content. Índex navegable del vault. |
| `UnitatDidactica` | Unitat didàctica amb continguts, activitats i avaluació. |
| `FitxaAEA` | Fitxa d'una activitat d'ensenyament-aprenentatge concreta. |

**Regla.** Cap node no pot declarar un `type:` que no sigui universal o no consti en aquesta taula. Si cal un tipus nou, s'amplia aquesta Convenció i es puja la versió.

---

## 3 · Camps obligatoris del frontmatter

Tots els nodes han de dur els **8 camps universals** del Core (id, type, title, version, data_ultima_actualitzacio, authors, llicencia, tags), més `estat` i opcionalment `visibilitat`.

---

## 4 · Format del camp id

```
{CODI}-{ÀMBIT}-{NN}
```

Exemples d'aquest vault: `C1-MOC-00`, `C1-UD1-00`, `C1-AEA-01`.

---

## 5 · Enllaços interns

Enllaços amb **ruta relativa** des del fitxer origen i extensió `.md`:

```markdown
[Convenció del vault](./03_C1_Convencio.md)
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
| V1.0-Esborrany | 2026-10-31 | Creació inicial de la Convenció del vault d'exemple. |

---

## Relacions (Graf)

- Complementa: [MOC del vault](./00_C1_MOC.md)
- Complementa: [OKF-CORE-FP-00](../../01-cores/OKF-CORE-FP-00.md) — core del marc FP (origen LOGSE inclòs).
