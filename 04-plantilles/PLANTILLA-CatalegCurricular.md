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
  # Format nou (v1.3): cada CA és un diccionari.
  # Per contextualitzar un CA, canvia 'contextualitzat' a true i modifica la
  # seva 'descripcio' al context del centre. Per afegir un CA nou (no oficial),
  # usa 'codi: null' amb 'afegit: true' i indica l''origen' (ex: "recurs propi").
  RA1:
    - codi: "1.1"
      guia: "1a"
      descripcio: "Descripció literal del CA 1.1."
      contextualitzat: false
      afegit: false
      origen: null
    - codi: "1.2"
      guia: "1b"
      descripcio: "Descripció literal del CA 1.2."
      contextualitzat: false
      afegit: false
      origen: null
    - codi: "1.3"
      guia: "1c"
      descripcio: "Descripció literal del CA 1.3."
      contextualitzat: true
      afegit: false
      origen: null
    # CAs d'anglès professional (descomentar i moure al RA que correspongui):
    # - codi: null
    #   guia: "1y"
    #   descripcio: "Interpreta documentació professional en llengua anglesa."
    #   afegit: true
    #   origen: "anglès professional"
    # - codi: null
    #   guia: "1z"
    #   descripcio: "Es comunica, per escrit i/o oralment, en llengua anglesa en situacions professionals habituals."
    #   afegit: true
    #   origen: "anglès professional"
  RA2:
    - codi: "2.1"
      guia: "2a"
      descripcio: "Descripció literal del CA 2.1."
      contextualitzat: false
      afegit: false
      origen: null
    - codi: "2.2"
      guia: "2b"
      descripcio: "Descripció literal del CA 2.2."
      contextualitzat: false
      afegit: false
      origen: null
    - codi: null
      guia: "2z"
      descripcio: "CA afegit pel docent (exemple)."
      contextualitzat: false
      afegit: true
      origen: "recurs propi"
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
| <a id="ca-1-1"></a>1.1 | 1a | ... | A | AEA1 |
| <a id="ca-1-2"></a>1.2 | 1b | ... | B | AEA1 |
| <a id="ca-1-3"></a>1.3 | 1c | ... | A | AEA1 |

### RA2

| Oficial | Guia | Descripció | Prioritat | AEA |
|:---|:---|:---|:---:|:---:|
| <a id="ca-2-1"></a>2.1 | 2a | ... | A | AEA2 |
| <a id="ca-2-2"></a>2.2 | 2b | ... | B | AEA2 |

---

## Notes

- La columna `Oficial` és la que ha d'aparèixer al camp `criteris:` del frontmatter.
- La columna `Guia` és un àlies local. El linter l'accepta, però la notació canònica és l'Oficial.
- Cada fila d'aquesta taula ha de tenir la seva àncora `<a id="ca-<ra>-<ca>">` (per exemple `<a id="ca-1-1"></a>`) al principi de la descripció, quan la Fase 3 del RFC implementi la coherència YAML↔àncores.

---
Generat per OKF Starter Kit · Plantilla CatalegCurricular