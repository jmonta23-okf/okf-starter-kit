---
id: PLANTILLA-MOC-00
type: MOC
title: "[Nom del teu curs o àrea] — Map of Content"
subtitle: "[Descripció breu de què agrupa aquest MOC]"
cycle: "[El teu cicle o àmbit]"
center: "El teu centre educatiu"
academic_year: "2026-2027"
version: "V1.0-Esborrany"
data_ultima_actualitzacio: "2026-10-25"  # Canvia per la data d'avui
authors:
  - "El teu nom"
legal_framework: "[El marc legal del teu cicle]"
tags:
  - okf/plantilla
  - okf/moc
estat: esborrany
visibilitat: publica
---

# [Nom del teu curs o àrea] — Map of Content

> **Propòsit.** Aquest node és l'índex navegable del teu vault (o d'una secció). Actua com a porta d'entrada: des d'aquí s'ha de poder arribar a qualsevol node rellevant en un màxim de dos clics.

> **Quan fer servir aquesta plantilla.** Per crear el node arrel del vault, el MOC d'un crèdit o el MOC d'una àrea temàtica. Si el MOC és específic d'un crèdit, afegeix el camp `credit` al frontmatter. Un MOC no requereix `credit`.

---

## 1 · Nodes del vault

Organitza els enllaços per categories. Cada entrada segueix el format:

```markdown
- [Nom del node](ruta/al/fitxer.md) — descripció breu d'una línia
```

### Aprenentatge

- [Unitat 1: Introducció](01_C1_Unitat_Didactica.md) — primera unitat del curs
- [Unitat 2: [Títol]](01_C2_Unitat_Didactica.md) — [descripció breu]

### Avaluació

- [Prova pràctica 1](02_C1_Prova_Practica.md) — prova sumativa del bloc 1
- [Rúbrica del cas clínic](02_C1_Rubrica_Cas.md) — instrument d'avaluació

### Govern del vault

- [Convenció de Nomenclatura](../04-plantilles/PLANTILLA-ConvencioNomenclatura.md) — regles del vault
- [Core de l'àmbit](../01-cores/OKF-CORE-CATALA-00.md) — nucli normatiu de referència

---

## 2 · Criteris d'un bon MOC

1. **És el punt d'entrada.** Qualsevol persona que obri el vault ha de començar aquí.
2. **Navegació en dos clics.** No s'ha d'enterrar un node a cinc nivells de profunditat.
3. **Es manté actualitzat.** Quan s'afegeix o es reanomena un node, el MOC s'actualitza.
4. **Agrupa, no duplica.** Un node només pot aparèixer en una categoria (o enllaçat des del MOC amb una referència creuada, mai copiat).

---

## 3 · Notes d'ús

- El MOC és l'únic node que **no enllaça cap amunt**: no té node pare.
- Tots els nodes del vault haurien d'enllaçar el seu MOC a la secció `Relacions (Graf)` del cos.
- Si el vault creix molt, es poden crear MOC de segon nivell (un per àrea) i enllaçar-los des del MOC arrel.

---

## 4 · Historial de versions

| Versió | Data | Descripció |
|:------:|:----:|:-----------|
| V1.0-Esborrany | 2026-10-25 | Creació de la plantilla. |

---

**Fi de la plantilla.**

*Versió V1.0-Esborrany*