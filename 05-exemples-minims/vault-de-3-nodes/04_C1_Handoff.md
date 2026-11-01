---
id: C1-HANDOFF-00
type: DocumentHandoff
title: "Handoff del vault C1"
subtitle: "Transferència de context del vault entre sessions o agents"
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
  - okf/handoff
estat: vigent
---

# Handoff del vault C1

> **Propòsit.** Aquest node transfereix el context mínim del vault entre sessions o agents, tal com exigeix la interoperabilitat del Core (§7.3).

---

## 1 · Què és aquest vault

Un vault d'exemple de la família C1 amb els nodes:

- [00_C1_MOC.md](./00_C1_MOC.md) — MOC arrel del vault.
- [01_C1_Unitat_Didactica.md](./01_C1_Unitat_Didactica.md) — unitat didàctica 1.
- [02_C1_Fitxa_Activitat.md](./02_C1_Fitxa_Activitat.md) — fitxa d'activitat d'ensenyament-aprenentatge.
- [03_C1_Convencio.md](./03_C1_Convencio.md) — Convenció de Nomenclatura (tipus vàlids i regles).
- Aquest node — handoff de context.

## 2 · Estat del vault

**Estat:** operatiu, 0 errors de validació. S'usa com a laboratori mínim per provar el kit.

## 3 · Regles que cal respectar

- Els 8 camps universals són obligatoris a tots els nodes.
- Els tipus vàlids són els de la [Convenció](./03_C1_Convencio.md): universals + `UnitatDidactica` + `FitxaAEA`.
- Els enllaços interns són relatius, amb `.md` i text visible (mai dobles claudàtors).
- `credit` només en tipus de família (ex: la unitat didàctica), mai en tipus universals.

## 4 · Següents passes

- Ampliar el vault amb més unitats i activitats seguint la Convenció.
- Mantenir aquest handoff actualitzat quan el vault canviï de mans.

---

## Relacions (Graf)

- Complementa: [00_C1_MOC.md](./00_C1_MOC.md)
- Complementa: [03_C1_Convencio.md](./03_C1_Convencio.md)
