---
id: "OKF-DOC-09"
type: Guia
title: "El graf curricular de dues capes"
version: "V1.0"
data_ultima_actualitzacio: "2026-11-04"
llicencia: "CC BY-SA 4.0"
authors:
  - "Josep Montañà Piqué"
tags: ["okf", "curricular", "audit", "okf/doc"]
estat: vigent
---

# El graf curricular de dues capes

Aquest document explica com l'OKF Starter Kit resol la **fractura curricular** entre el decret (el món prescriptiu) i l'aula (el món operatiu). És la guia de referència del **RFC-OKF-02**, implementat a la V1.2, ampliat a la **V1.3** amb els formats de criteris contextualitzats, CAs afegits i instruments d'avaluació estructurats (RFC-OKF-03).

## 1 · El problema: la fractura entre el decret i l'aula

A la Formació Professional, el currículum viu en dos mons que sovint no es parlen:

- **El decret** (DOGC/BOE): un document estàtic, amb Resultats d'Aprenentatge (RA) i Criteris d'Avaluació (CA) que el docent ha de cobrir. Té una vigència de 5 a 10 anys.
- **L'aula**: les activitats reals, els tallers, les proves, els projectes. Canvien cada curs.

Sense una infraestructura d'enllaç explícita, passen tres coses:

1. **No hi ha garantia que el conjunt d'activitats avali el 100% dels CAs obligatoris.** El docent pot acabar el curs sense haver tocat algun criteri, i no ho sap.
2. **Quan inspecció o una auditoria demana evidències d'un criteri concret**, el docent ha de buscar per carpetes disperses.
3. **Els agents d'IA al·lucinen criteris** perquè no tenen un graf tancat de la norma. Inventen codis, confonen terminologia, barregen mòduls.

## 2 · La solució: dues capes connectades

L'OKF Starter Kit proposa separar el mòdul professional en **dues capes** amb cicles de vida diferents, connectades per enllaços relatius i metadades formals:

### Capa 1 — El catàleg curricular (el decret)

Un únic fitxer per mòdul, `type: CatalegCurricular`, que digitalitza el decret. Conté:

- Els RA i els CAs al **frontmatter** (format `criteris:`), perquè les màquines els puguin llegir. Des de la V1.3 cada CA és un **diccionari** (vegeu §3).
- Les taules de CAs al **cos**, amb descripció, prioritat i AEA assignada, perquè els humans els puguin llegir.
- Les àncores `<a id="ca-5-1"></a>` al cos, perquè els enllaços dels altres nodes hi puguin apuntar.

És l'única font de veritat normativa del mòdul. La seva versió es declara al camp `version` (per exemple `V2.1`).

### Capa 2 — Les fitxes AEA (l'aula)

Cada activitat d'ensenyament-aprenentatge és una fitxa `type: FitxaAEA`. Conté:

- `cataleg_referencia`: ruta relativa al catàleg (per exemple `./01_MP1519_Cataleg_Curricular.md`).
- `cataleg_versio`: la versió del catàleg a la qual respon (per exemple `V2.1`).
- `criteris_avaluacio`: la llista de codis oficials que aquesta activitat avalua (per exemple `["5.1", "5.2", "6.1"]`).
- `instruments_avaluacio`: els instruments amb què s'avaluen els criteris (format diccionari des de la V1.3).
- `naturalesa`: `analitica` (per defecte) o `sintesi` (per a projectes integradors).

Les fitxes es mouen, es milloren, es refan cada curs. No han de tocar el catàleg.

### La connexió

El catàleg i les fitxes es connecten per **enllaços relatius estàndard** (CommonMark, POSIX) i per les **metadades formals** de cada node. El validador pot auditar la coherència en temps real.

## 3 · Els camps del RFC-OKF-02

Els camps que fan possible l'arquitectura de dues capes són:

| Camp | On viu | Què fa |
|:---|:---|:---|
| `criteris` | CatalegCurricular (frontmatter) | Declara els codis oficials de cada RA. És la font de veritat per a l'auditoria. |
| `cataleg_referencia` | FitxaAEA | Ruta relativa al catàleg. |
| `cataleg_versio` | FitxaAEA | Versió del catàleg a la qual respon la fitxa. |
| `criteris_avaluacio` | FitxaAEA | Codis oficials que la fitxa avalua. |
| `instruments_avaluacio` | FitxaAEA | Instruments amb què s'avaluen els criteris (V1.3). |
| `naturalesa` | FitxaAEA | `analitica` o `sintesi`. Les de síntesi no compten per a la cobertura de primer ordre. |

Aquests camps es declaren al **Core FP §8.2** com a camps de família.

### Els formats de la V1.3 (RFC-OKF-03)

Des de la V1.3, **cada CA del catàleg és un diccionari** amb els camps `codi`,
`guia`, `descripcio`, `contextualitzat`, `afegit` i `origen`. El format antic
(una llista de strings per a cada RA) continua sent acceptat pel validador,
però és obsolet i es retirarà a la v1.4:

```yaml
criteris:
  RA5:
    - codi: "5.1"
      guia: "5a"
      descripcio: "Utilitza les funcions, prestacions i procediments dels processadors de textos."
      contextualitzat: false
      afegit: false
      origen: null
    - codi: null
      guia: "5h"
      descripcio: "Interpreta documentació professional en llengua anglesa."
      afegit: true
      origen: "anglès professional"
```

També des de la V1.3, **cada instrument d'avaluació de la fitxa és un
diccionari** amb `codi`, `descripcio` i `criteris`. El format antic (una
llista de rutes) continua sent acceptat, però és obsolet:

```yaml
instruments_avaluacio:
  - codi: "I1"
    descripcio: "Pràctica de taller 1"
    criteris: ["5.1", "5.2"]
```

El validador comprova la coherència interna d'aquests formats: `codi` nul sense
`afegit`, `afegit` sense `guia`, instruments sense criteris o criteris sense
instrument, codis duplicats, etc. (els codis d'error corresponents es detallen
a la secció d'auditoria, §4).

## 4 · Com auditar la cobertura

El validador v1.3 té el flag `--audit`, que calcula la cobertura curricular per catàleg:

```bash
python3 03-eines/validar_yaml.py --ruta . --audit
```

La sortida és un informe per catàleg:

```
=== Cobertura curricular: 07-exemple-mp1519/01_MP1519_Cataleg_Curricular.md ===
Versió del catàleg: V1.0
Total CAs al decret: 52
CAs avaluats (analítics): 52
CAs coberts: 52
CAs orfes: 0
CAs inexistents: 0
Mismatch de versió: 0 (deprecated, informatiu)
Verdicte: COBERT

=== Resum ===
Catàlegs analitzats: 2
Catàlegs coberts: 2
Catàlegs incomplets: 0
CAs únics al decret: 52
CAs únics coberts: 52
CAs contextualitzats (*): 0
CAs afegits pel docent: 0
```

### Interpretació de les mètriques

- **CAs orfes:** criteris del decret que cap fitxa avalua (ni analítica ni de síntesi). Si n'hi ha, la cobertura no és completa.
- **CAs inexistents:** criteris que una fitxa declara avaluar però que no són al catàleg. Sol ser un error de transcripció (per exemple `6.9` quan el decret s'atura a `6.8`).
- **CAs coberts:** criteris coberts per alguna fitxa (analítica o de síntesi).
- **CAs contextualitzats (*):** criteris marcats com a `contextualitzat: true` (adaptats al centre).
- **CAs afegits pel docent:** criteris marcats com a `afegit: true` (que no són al decret).
- **Mismatch de versió:** fitxes que apunten a una versió del catàleg diferent de la vigent. És una mètrica informativa (deprecated): no afecta el veredicte.
- Les línies `CAs avaluats (analítics)` i `Mismatch de versió` es mantenen per compatibilitat enrere amb les eines que llegeixen la sortida de `--audit`.

### Codis de sortida

| Codi | Significat |
|:---:|:---|
| 0 | Tots els catàlegs coberts. |
| 1 | Algun catàleg amb orfes, inexistents o errors estructurals. |
| 2 | Cap catàleg per auditar. |

### Els codis d'error de la V1.3

Des de la V1.3 el validador ha afegit 10 codis d'error per a la coherència dels nous formats:

| Codi | Descripció | Severitat |
|:---|:---|:---:|
| `Y040` | `contextualitzat` no és boolean | 🟠 Alta |
| `Y042` | `codi: null` sense `afegit: true` | 🔴 Crític |
| `Y043` | `afegit: true` sense `guia` | 🔴 Crític |
| `Y044` | `afegit` + `contextualitzat` redundants | 🟡 Mitjana |
| `Y045` | CA afegit no referenciat per cap FitxaAEA | 🟡 Mitjana |
| `Y046` | CA només cobert per fitxes de síntesi | 🟡 Mitjana |
| `Y048` | `criteris[RA]` no és una llista | 🟠 Alta |
| `Y050` | Codi d'instrument duplicat | 🟠 Alta |
| `Y051` | Instrument sense cap criteri | 🟡 Mitjana |
| `Y052` | Criteri sense cap instrument | 🟡 Mitjana |

Cap d'aquests codis no afecta el veredicte (COBERT/INCOMPLET) ni el codi de sortida d'`--audit`; són observacions de coherència i traçabilitat que cal corregir, però no bloquegen la cobertura.

### Deprecacions (V1.3)

- `cataleg_versio` s'ignora silenciosament (ni error ni warning).
- `--strict-versio` és un *no-op*: s'accepta el flag, s'emet un warning literal i no canvia el codi de sortida.
- `Y035` (àlies duplicat) ha baixat de 🔴 Crític a 🟠 Alta.
- `Y036` (`naturalesa` invàlida) ha baixat de 🟠 Alta a 🟡 Mitjana.

## 5 · Un exemple pràctic

El kit inclou `07-exemple-mp1519/`, un exemple complet de l'arquitectura de dues capes amb el mòdul MP 1519 (*Sistemes d'informació i classificació sanitaris*, CFGS Documentació i Administració Sanitàries):

- `00_MP1519_MOC.md` — porta d'entrada.
- `01_MP1519_Cataleg_Curricular.md` — 52 CAs al frontmatter, 52 àncores al cos.
- `02_MP1519_Protocol_Avaluacio.md` — marc d'avaluació.
- `03` a `07` — 5 fitxes AEA (12 + 12 + 15 + 13 + 19 CAs; l'última és de síntesi).
- `08_MP1519_Convencio.md` — Convenció amb àlies.
- `09_MP1519_Handoff.md` — traspàs de curs.

L'`--audit` sobre aquest exemple dona `52/52/0/0/0` i `Verdicte: COBERT`.

## 6 · Límits i decisions pendents

- **`instruments_per_criteri`:** el camp és opcional al RFC i no s'implementa encara al validador. La coherència instruments↔criteris es valida a nivell de fitxa amb `Y051` (instrument sense criteri) i `Y052` (criteri sense instrument).
- **`criteris_treballats`:** opcional al RFC. Permet distingir criteris formatius (treballats a l'aula) de sumatius (avaluats). No s'implementa encara al validador.
- **La notació Guia:** el catàleg pot tenir una columna `Guia` (per exemple `5a` com a àlies de `5.1`). El validador accepta `ca-5-1` i `ca-5-1-<guia>`, però la notació canònica és l'Oficial.
- **Els CAs al frontmatter i al cos:** el validador comprova que coincideixen (Y030/Y031). Si no coincideixen, error.
- **L'auditoria per catàleg:** cada catàleg té la seva pròpia cobertura. Dos catàlegs que declaren els mateixos codis (per exemple el 02-exemple i el 07-exemple) no se sumen a l'`--audit`; es mostra la unió (52) i el total per catàleg (104) a l'snapshot.

## 7 · Per a agents d'IA

L'arquitectura de dues capes és **nativament computable per agents**:

- **Injecció de límit normatiu:** un agent que redacta una activitat només necessita dos documents al context: el MOC i el catàleg. No ha de fer cerques semàntiques per 50 fitxers.
- **Generació determinista:** si l'agent vol treballar el criteri `6.4`, localitza `#ca-6-4` al catàleg, i enllaça la fitxa amb `./01_MP1519_Cataleg_Curricular.md#ca-6-4`. No inventa codis.
- **Flux supervisat (MIAE Nivell 3):** l'agent genera l'activitat amb `estat: proposta`. El docent la valida i canvia a `estat: vigent`. El control humà és total.

## 8 · Relació amb la resta del kit

- **Core FP §8.2:** declara els camps de família que fan possible l'arquitectura.
- **`01-cores/OKF-CORE-FP-00.md` §8.3:** declara els tipus de família LOE (`CatalegCurricular`, `EinaTecnica`, `FitxaAEA`).
- **`03-eines/validar_yaml.py` v1.3:** té `--audit` i els codis Y030-Y036, Y040-Y046, Y048-Y052.
- **`04-plantilles/PLANTILLA-CatalegCurricular.md`:** plantilla per crear un catàleg nou.
- **`07-exemple-mp1519/`:** exemple complet de l'arquitectura.

---

*Document creat el 3 de novembre de 2026. Forma part del RFC-OKF-02 (arquitectura del graf curricular de dues capes).*
