---
id: MP1519-EINA-VALIDATOR-01
type: EinaTecnica
title: "Eina Tècnica: Validador Determinista CIE-10-ES (Python + SQLite)"
subtitle: "Arquitectura, instal·lació i operació del validador local de codis clínics (cie10es_validator.py)"
cycle: "CFGS Documentació i Administració Sanitàries (SAD)"
center: "Centre educatiu de referència"
academic_year: "2026-2027"
version: "V2.0-Complet"
data_ultima_actualitzacio: "2026-10-29"
authors:
  - "Josep Montañà Piqué"
legal_framework: "Ordre EDU/10/2020 i RD 768/2014 (LOE)"
credit: "MP1519"
tags:
  - okf/eina-tecnica
  - okf/sanitat
  - mp1519/validador
  - okf/cie10es
  - okf/anti-al-lucinacio
estat: vigent
---

# Eina Tècnica: Validador Determinista CIE-10-ES (Python + SQLite)

> **Propòsit.** Aquest document descriu l'arquitectura, el desplegament i el funcionament de `cie10es_validator.py`, una eina local de línia de comandes en Python que audita de manera **determinista i instantània** qualsevol codi clínic contra la base de dades oficial de la 6a edició de la CIE-10-ES (2026) del Ministeri de Sanitat d'Espanya.

---

## 1 · Propòsit i Fonament: El «Validador de Domini»

A l'arquitectura d'OKF conviuen dos nivells de validació complementaris:
1. **El Validador d'Estructura (`validar_yaml.py`):** Audita la sintaxi del graf, la integritat de les metadades YAML, els enllaços relatius i les versions.
2. **El Validador de Domini (`cie10es_validator.py`):** Audita la **veracitat factual del contingut docent**, comprovant que cap codi clínic generat per una IA o proposat per un alumne sigui inventat o pertanyi a una normativa estrangera.

```
┌────────────────────────────────────────────────────────────────────────┐
│  PRINCIPI DE DISSENY FONAMENTAL                                        │
├────────────────────────────────────────────────────────────────────────┤
│  El model de llenguatge (LLM) NO és la font de veritat; és només       │
│  un motor probabilístic de redacció.                                   │
│  La taula oficial del Ministeri de Sanitat és l'única font de veritat. │
│  Aquest validador converteix aquest principi en una rutina operativa.  │
└────────────────────────────────────────────────────────────────────────┘
```

### Per què era imprescindible crear aquesta eina?
Tot i que el Paquet LLM ([08_MP1519_Paquet_LLM.md](./08_MP1519_Paquet_LLM.md)) incorpora 7 capes de blindatge i la Taula dels 10 Falsos Amics, els models de llenguatge són sistemes no deterministes que poden patir petites fallades d'al·lucinació (especialment truncant codis a 3 caràcters o important subtipus de l'ICD-10-CM americà). 

Aquest validador elimina el risc d'al·lucinació per disseny: **el codi és vàlid si i només si existeix com a registre a la base de dades oficial**.

---

## 2 · Arquitectura Tècnica i Components

L'eina està construïda seguint els principis de màxima simplicitat, resiliència i zero dependències de servidors externs:

```
┌───────────────────────────────────────────────┐
│ Fitxer Oficial del Ministeri de Sanitat      │
│ (CIE10ES_2026_Diagnosticos.xlsx / .csv)       │
└───────────────────────┬───────────────────────┘
                        │ Comanda: load
                        ▼
┌───────────────────────────────────────────────┐
│ Base de Dades SQLite Local (cie10es.db)       │
│ • Taula 'codes': ~15.200 codis terminals      │
│ • Índex FTS5: cerca ràpida per text insensible│
│   a accents i majúscules (remove_diacritics 2)│
└───────────────────────┬───────────────────────┘
                        │
         ┌──────────────┴──────────────┐
         ▼                             ▼
┌─────────────────┐           ┌─────────────────┐
│ Comanda: check  │           │ Comanda: search │
│ Comprovació O(1)│           │ Cerca semàntica │
│ de codi exacte  │           │ per paraules    │
└─────────────────┘           └─────────────────┘
```

| Component | Tecnologia | Funció al sistema |
|:---|:---|:---|
| **Motor de dades** | SQLite 3 (`cie10es.db`) | Emmagatzematge ràpid en un sol fitxer local d'uns 15 MB. |
| **Índex de text complet** | SQLite FTS5 | Motor de cerca per termes clínics insensible a accents (`fèmur` = `fémur`). |
| **Codi d'execució** | Python 3 (CLI) | Script autònom sense interfície gràfica, apte per a terminals i scripts batch. |
| **Integració d'IA (opcional)** | Anthropic Claude API | A la comanda `code`, l'LLM tria entre els candidats trobats (mai genera codis nous). |

---

## 3 · Instal·lació i Preparació

### 3.1 · Requisits previs
* Python 3.8 o superior (`python3 --version`).
* Gestor de paquets `pip` (`pip3 --version`).
* Sistema operatiu: macOS, Linux o Windows.

### 3.2 · Instal·lació de dependències
Al terminal del teu equip:

```bash
pip3 install openpyxl anthropic
```

* `openpyxl`: Necessari per llegir el fitxer oficial Excel del Ministeri a la càrrega inicial.
* `anthropic` *(opcional)*: Només cal si es vol utilitzar la comanda avançada `code`. Per a les comandes `check` i `search`, no cal cap clau d'API ni paquet extern.

### 3.3 · Càrrega de la taula oficial del Ministeri (`load`)
1. Descarrega la taula oficial completa de codis de la CIE-10-ES 6a edició (2026) des del portal oficial del Ministeri: [eciemaps.sanidad.gob.es/documentation](https://eciemaps.sanidad.gob.es/documentation).
2. Executa la comanda de càrrega per generar la base de dades local:

```bash
python3 cie10es_validator.py load CIE10ES_2026_Diagnosticos.xlsx
```

**Sortida esperada al terminal:**
```text
15234 codis carregats amb èxit a cie10es.db. Mostra de registres:
  A00.0  Còlera degut a Vibrio cholerae 01, biotip cholerae
  A00.1  Còlera degut a Vibrio cholerae 01, biotip El Tor
  K35.30 Apendicitis aguda amb peritonitis localitzada
  ...
```

---

## 4 · Guia d'Ús de les Comandes CLI

### 4.1 · Comanda `check`: Validació determinista de codis
Comprova a l'instant si un o diversos codis existeixen oficialment a la 6a edició:

```bash
python3 cie10es_validator.py check K35.30 S72.0 E11.9 CODI_FALS
```

**Retorn en format JSON estructurat:**
```json
{"input": "K35.30", "status": "valid", "code": "K35.30", "descr": "Apendicitis aguda con peritonitis localizada"}
{"input": "S72.0", "status": "incomplet", "hint": ["S72.001A", "S72.002A", "S72.011A"]}
{"input": "E11.9", "status": "valid", "code": "E11.9", "descr": "Diabetes mellitus tipo 2 sin complicaciones"}
{"input": "CODI_FALS", "status": "no_existeix"}
```

#### Els 4 estats de validació:

| Estat | Significat clínic | Acció immediata de l'auditor |
|:---:|:---|:---|
| **`valid`** | Codi exacte, terminal i facturable al CMBD. | ✅ Es pot publicar directament al solucionari o rúbrica. |
| **`incomplet`** | El codi existeix com a categoria, però requereix caràcters addicionals (5è, 6è o 7è dígit). | ⚠️ Cal baixar al nivell d'especificitat proposat a la llista `hint`. |
| **`no_existeix`** | El codi no consta a la 6a edició espanyola (al·lucinació o codi americà). | ❌ Descartar immediatament i revisar l'informe clínic. |
| **`format_invalid`**| La cadena no respecta la sintaxi (3-7 caràcters alfanumèrics). | ❌ Error tipogràfic de transcripció. |

---

### 4.2 · Comanda `search`: Cerca ràpida per text clínic
Permet explorar el catàleg oficial mitjançant llenguatge natural sense connexió a internet:

```bash
python3 cie10es_validator.py search "fractura coll femur"
```

**Sortida al terminal:**
```text
S72.001A  Fractura no desplazada del cuello del fémur derecho, contacto inicial
S72.002A  Fractura no desplazada del cuello del fémur izquierdo, contacto inicial
S72.011A  Fractura desplazada de la cabeza del fémur derecho, contacto inicial
... (fins a 25 resultats ordenats per rellevància FTS5)
```

---

### 4.3 · Comanda `code`: Selecció assistida per IA amb filtre determinista
Combina la intel·ligència d'un LLM amb la certesa d'una base de dades local. **El model mai inventa codis; només tria entre els candidats reals que l'script ha trobat a la base de dades**:

```bash
python3 cie10es_validator.py code "pacient de 68 anys amb pneumònia per legionel·la"
```

**Retorn auditat:**
```json
{
  "text": "pacient de 68 anys amb pneumònia per legionel·la",
  "result": [
    {
      "input": "A48.1",
      "status": "valid",
      "code": "A48.1",
      "descr": "Enfermedad de los legionarios (neumonía por Legionella pneumophila)"
    }
  ]
}
```

---

## 5 · Flux Operatiu al Mòdul: Verificació abans de Publicar

Aquest validador s'integra com a filtre de seguretat obligatori en la generació de materials docents:

```
[Docent demana un solucionari al Paquet LLM (08)]
                       │
                       ▼
[La IA genera la proposta amb codis CIE-10-ES]
                       │
                       ▼
[El docent copia els codis i executa 'check' en local]
python3 cie10es_validator.py check K35.30 Z90.11 T39.1X1A
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
(Tots 'valid' ✅)            (Algun 'no_existeix' o 'incomplet' ⚠️)
         │                           │
         ▼                           ▼
[Publicació immediata]       [Esmena a eCIEMaps o amb 'hint']
```

**Temps invertit:** Menys de 10 segons per cada activitat o prova d'avaluació.

---

## 6 · Integració amb els Marcs MIAE i VCER

L'eina fa plenament operatius els principis ètics del projecte:

* **Compliment MIAE (Nivell 3):** Dona una eina empírica al docent per exercir la **supervisió humana obligatòria**. El docent no necessita saber-se de memòria els 15.000 codis de la classificació: l'script li certifica la validesa normativa a l'instant.
* **Compliment VCER:** 
  * **100 % Offline i Local-First:** Les comandes `load`, `check` i `search` s'executen íntegrament a la màquina del docent, sense dependre de xarxa ni de servidors de tercers.
  * **Zero recollida de dades:** No processa dades d'alumnes ni transmet cap informació.
  * **Zero cost:** Funcionament sobre programari lliure i de codi obert (SQLite + Python).

---

## 7 · Manteniment i Límits Coneguts

| Aspecte | Comportament | Procediment de manteniment |
|:---|:---|:---|
| **Actualització del manual** | El Ministeri publica edicions bianuals. | En publicar-se una nova edició (ex: 7a edició 2028), només cal descarregar el nou `.xlsx` i tornar a executar `load`. |
| **Abast de la validació** | Valida l'existència i terminalitat del codi individual. | **No valida la seqüenciació ni el POA**: determinar si un codi és DP o DS, o si li correspon POA S o N, continua sent un judici del docent d'acord amb el [Protocol d'Avaluació](./02_MP1519_Protocol_Avaluacio.md). |
| **Mida del fitxer** | Base de dades d'uns 15 a 18 MB. | No cal pujar `cie10es.db` a GitHub (està al `.gitignore`). Cada docent el compila en 30 segons amb `load`. |

---

## 8 · Relacions del Graf (Enllaços interns)

- **[00_MP1519_MOC.md](./00_MP1519_MOC.md)** — Node arrel i mapa general del mòdul.
- **[01_MP1519_Cataleg_Curricular.md](./01_MP1519_Cataleg_Curricular.md)** — Criteris d'Avaluació de selecció de codis (RA4, RA6, RA8).
- **[08_MP1519_Paquet_LLM.md](./08_MP1519_Paquet_LLM.md)** — Contracte d'IA que utilitza aquest validador a la Capa 6 de blindatge.
- **[09_MP1519_Arquitectura_DualUser.md](./09_MP1519_Arquitectura_DualUser.md)** — Manual de la IA Co-Docent i protocol de fonts tancades.
- **[11_MP1519_Ecosistema_Automatitzacio.md](./11_MP1519_Ecosistema_Automatitzacio.md)** — Ecosistema d'eines que interactua amb les avaluacions del centre.
```
