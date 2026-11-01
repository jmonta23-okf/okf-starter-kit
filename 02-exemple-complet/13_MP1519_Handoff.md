---
id: MP1519-HANDOFF-00
type: DocumentHandoff
title: "Handoff del MP 1519"
subtitle: "Transferència de context de l'exemple complet entre sessions o agents"
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
  - okf/handoff
estat: vigent
---

# Handoff del MP 1519

> **Propòsit.** Aquest node transfereix el context mínim de l'exemple complet entre sessions o agents, tal com exigeix la interoperabilitat del Core (§7.3).

---

## 1 · Què és aquest mòdul d'exemple

`02-exemple-complet/` desplega el mòdul **MP 1519 — Sistemes d'informació i classificació sanitaris** (CFGS Documentació i Administració Sanitàries) amb l'arquitectura del kit:

- [00_MP1519_MOC.md](./00_MP1519_MOC.md) — MOC arrel del mòdul.
- [01_MP1519_Cataleg_Curricular.md](./01_MP1519_Cataleg_Curricular.md) — catàleg amb 54 criteris d'avaluació.
- [02_MP1519_Protocol_Avaluacio.md](./02_MP1519_Protocol_Avaluacio.md) — protocol de tres portes amb matriu OC.
- [03-07_MP1519_Fitxa_AEA_1-5.md](./03_MP1519_Fitxa_AEA_1.md) — 5 fitxes d'activitat d'ensenyament-aprenentatge.
- [08_MP1519_Paquet_LLM.md](./08_MP1519_Paquet_LLM.md) — paquet LLM amb 7 capes anti-al·lucinació.
- [09_MP1519_Arquitectura_DualUser.md](./09_MP1519_Arquitectura_DualUser.md) — guia d'arquitectura Dual-User.
- [10_MP1519_Validador_CIE10ES.md](./10_MP1519_Validador_CIE10ES.md) — validador determinista CIE-10-ES.
- [11_MP1519_Ecosistema_Automatitzacio.md](./11_MP1519_Ecosistema_Automatitzacio.md) — eina d'automatització amb Google Workspace.
- [12_MP1519_Convencio.md](./12_MP1519_Convencio.md) — Convenció de Nomenclatura (tipus vàlids i regles).
- Aquest node — handoff de context.

## 2 · Estat del mòdul d'exemple

**Estat:** operatiu, 0 errors de validació (validador v1.1.0 del kit). Serveix de mirall de referència real: qualsevol docent que vulgui desplegar un mòdul propi pot copiar-ne l'estructura.

## 3 · Regles que cal respectar

- Els 8 camps universals són obligatoris a tots els nodes.
- Els tipus vàlids són els de la [Convenció](./12_MP1519_Convencio.md): universals + `CatalegCurricular` + `EinaTecnica` + `FitxaAEA`.
- Els enllaços interns són relatius, amb `.md` i text visible (mai dobles claudàtors).
- `credit` només en tipus de família, mai en tipus universals.

## 4 · Següents passes

- Adaptar l'exemple a un altre mòdul (canviar `MP1519` per l'identificador propi i els continguts).
- Mantenir aquest handoff actualitzat quan el mòdul canviï de mans.

---

## Relacions (Graf)

- Complementa: [00_MP1519_MOC.md](./00_MP1519_MOC.md)
- Complementa: [12_MP1519_Convencio.md](./12_MP1519_Convencio.md)
