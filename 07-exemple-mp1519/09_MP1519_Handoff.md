---
id: 07-MP1519-HANDOFF-00
type: DocumentHandoff
title: "Handoff del MP 1519 — curs 2026-2027 (vault de dues capes)"
subtitle: "Estat del curs, incidències i properes passes"
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
  - okf/handoff
  - mp1519/dues-capes
estat: vigent
---

# Handoff del MP 1519 — curs 2026-2027 (vault de dues capes)

> **Propòsit.** Document de traspàs: què hi ha, com s'ha construït, què hi ha pendent i com continuar. Aquest vault és un exemple viu de l'arquitectura de dues capes del RFC-OKF-02.

## 1 · Estat del curs

- **Capa 1 (catàleg):** els **52 CAs oficials** (RA1-RA8) estan declarats al frontmatter (`criteris:`) i al cos del [catàleg](./01_MP1519_Cataleg_Curricular.md), amb una àncora per criteri (`<a id="ca-X-Y"></a>`, 52 en total).
- **Capa 2 (fitxes):** les 5 fitxes referencien el catàleg amb `cataleg_referencia` + `cataleg_versio: "V1.0"` i declaren els CAs que avaluen a `criteris_avaluacio` (notació oficial). Cobertura de l'exemple: 52/52, cap orfe, cap inexistent.
- **Avaluació:** protocol de tres portes + rúbrica C1-C6 (node `02_MP1519_Protocol_Avaluacio.md`).

## 2 · Incidències

- Els **àlies de tipus** (`Activitat` → `FitxaAEA`, `Cataleg` → `CatalegCurricular`) estan declarats a la [Convenció](./08_MP1519_Convencio.md) com a **documentals**: el validador v1.1.0 no els processa encara (Y004 rebutjaria un `type: Activitat`). No fer-los servir en nodes reals fins a la Fase 3.
- La **coherència YAML↔àncores** (cada CA del frontmatter amb la seva àncora al cos) és la verificació que implementarà la Fase 3; les 52 àncores ja són al lloc perquè es pugui validar.
- Aquest vault **no inclou** PaquetLLM ni eines tècniques (a diferència de `02-exemple-complet/`): és l'esquelet mínim de dues capes.

## 3 · Properes passes

1. **Fase 3 del RFC-OKF-02:** implementar la lectura d'àlies, la coherència YAML↔àncores i l'auditoria de cobertura al validador (i activar els 7 tests de `tests/test_curriculum_audit.py`).
2. Decidir si l'`--audit` de l'snapshot ha de comptar els catàlegs per carpeta (agregació per unió, no per suma).
3. Revisar si aquest exemple ha de promocionar-se a `02-exemple-complet/` quan la Fase 3 consolidi el format.

---

*Fi del document de traspàs.*