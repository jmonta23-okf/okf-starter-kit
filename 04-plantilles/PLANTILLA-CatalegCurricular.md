---
id: "MP0000-CAT-00"
type: CatalegCurricular
title: "Catàleg Curricular: MP 0000 — Títol del mòdul"
version: "V1.0-Esborrany"
data_ultima_actualitzacio: "2026-11-02"
llicencia: "CC BY-SA 4.0"
authors:
  - "Nom del docent"
tags: ["fp", "cataleg", "okf/cataleg"]
estat: vigent
criteris:
  RA1: ["1.1", "1.2", "1.3"]
  RA2: ["2.1", "2.2"]
  # ... un RA per clau, i cada RA amb la llista de codis Oficials dels CAs
---

# Catàleg Curricular: MP 0000 — Títol del mòdul

## 1 · Identificació

- **Cicle:** CFGS/CFGM ...
- **Mòdul:** MP 0000
- **Hores:** N
- **Marc legal:** Ordre ... / Reial Decret ...

## 2 · Resultats d'Aprenentatge (RAs)

| RA | Descripció | Pes | Hores |
|:---|:---|:---:|:---:|
| RA1 | ... | ... | ... |
| RA2 | ... | ... | ... |

## 3 · Criteris d'Avaluació (CAs)

### RA1

| Oficial | Guia | Descripció | Prioritat | AEA |
|:---|:---|:---|:---:|:---:|
| 1.1 | 1a | ... | A | AEA1 |
| 1.2 | 1b | ... | B | AEA1 |

### RA2

| Oficial | Guia | Descripció | Prioritat | AEA |
|:---|:---|:---|:---:|:---:|
| 2.1 | 2a | ... | A | AEA2 |
| 2.2 | 2b | ... | B | AEA2 |

---

## Notes

- La columna `Oficial` és la que ha d'aparèixer al camp `criteris:` del frontmatter.
- La columna `Guia` és un àlies local. El linter l'accepta, però la notació canònica és l'Oficial.
- Cada fila d'aquesta taula ha de tenir la seva àncora `<a id="ca-<ra>-<ca>">` (per exemple `<a id="ca-1-1"></a>`) al principi de la descripció, quan la Fase 3 del RFC implementi la coherència YAML↔àncores.

---
Generat per OKF Starter Kit · Plantilla CatalegCurricular