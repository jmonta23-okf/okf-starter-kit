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

### Famílies de validació

Els codis d'error del validador s'organitzen en famílies segons l'aspecte que validen:

| Família | Què valida | Codis (rang) |
|:---|:---|:---|
| **YAML** | Estructura del frontmatter, sintaxi, enums | `Y001`-`Y009`, `Y023`, `Y024` (BOM, claus duplicades) |
| **Node** | Camps universals, tipus, coherència del node | `Y012`-`Y026` (subconjunt), `Y030`, `Y031` |
| **Graf** | Enllaços, coherència YAML↔àncores, àlies | `Y018`, `Y019` (enllaços i wikilinks), `Y030`, `Y031`, `Y035` |
| **Currículum** | Format de `criteris:`, CAs afegits, contextualitzats, `naturalesa` | `Y036`, `Y040`, `Y042`, `Y043`, `Y044`, `Y045`, `Y046`, `Y048` |
| **Avaluació** | `instruments_avaluacio` i cobertura creuada | `Y050`, `Y051`, `Y052` |
| **Governança** | MOC arrel, Handoff, Convenció | `Y014` (MOC arrel), `Y015` (Handoff), `Y016` (Convenció) |
| **Privacitat** | Inicials, pseudònims, dades de menors | `Y022` |

### Deprecacions (V1.3)

- `cataleg_versio` s'ignora silenciosament (ni error ni warning).
- `--strict-versio` és un *no-op*: s'accepta el flag, s'emet un warning literal i no canvia el codi de sortida.
- `Y035` (àlies duplicat) ha baixat de 🔴 Crític a 🟠 Alta.
- `Y036` (`naturalesa` invàlida) ha baixat de 🟠 Alta a 🟡 Mitjana.

### Validació en viu amb el JSON Schema

El fitxer [`01-cores/okf-core.schema.json`](../01-cores/okf-core.schema.json) defineix l'esquema JSON dels nodes OKF (8 camps universals, 13 tipus i enums bàsics). Permet que editors com VS Code i Obsidian donin **validació en viu** mentre escrius els nodes, sense haver d'executar el validador.

**A VS Code:**
1. Instal·la l'extensió **YAML** (de Red Hat).
2. Obre la configuració (`Cmd+,` o `Ctrl+,`) i afegeix:
   ```json
   "yaml.schemas": {
     "./01-cores/okf-core.schema.json": "*.md"
   }
   ```
   (La ruta és relativa a l'arrel del projecte obert a VS Code.)
3. Els fitxers `.md` amb frontmatter YAML mostraran errors en vermell si no compleixen l'esquema.

**A Obsidian:**
1. Instal·la el plugin **Linter** o **YAML Validation**.
2. Configura'l perquè apunti a `01-cores/okf-core.schema.json`.
3. Els nodes mostraran avisos si no compleixen l'esquema.

**Nota:** el JSON Schema és una **ajuda per a l'editor**, no substitueix el validador (`validar_yaml.py`). El validador fa comprovacions addicionals que el schema no pot fer (enllaços relatius, coherència YAML↔àncores, etc.).

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

## 9 · Distinció de versions

L'ecosistema OKF-CATALA té quatre versions diferents que no s'han de confondre:

| Element | Versió actual | Què versiona |
|:---|:---|:---|
| **Kit** (OKF Starter Kit) | V1.3 | El conjunt del kit (documents, eines, plantilles, exemples). És la versió que es publica a Zenodo. |
| **Model de dades** (perfil OKF) | v1.1.0 | L'especificació del model de dades (camps universals, tipus, famílies). Canvia poc. |
| **Validador** (`validar_yaml.py`) | v1.3.0 | L'eina de validació. Pot evolucionar independentment del kit. |
| **Core** (FP, Català) | FP v1.1.0 · Català v1.1.2 | Les regles específiques de cada família (LOE/LOGSE, llengua). |

> Nota: el validador v1.3.0 és el que acompanya el kit V1.3. A la v1.4 es preveu un salt de versió amb l'eliminació de les deprecacions.

---

## 10 · Especificació del model de dades

Aquesta secció formalitza el **model de dades** dels nodes OKF: quins camps té cada tipus, quines invariants s'apliquen i com és la compatibilitat entre el format antic i el nou. Els valors provenen del codi (`03-eines/validar_yaml.py`), dels Cores (`01-cores/OKF-CORE-*.md`) i de les plantilles (`04-plantilles/`).

### 10.1 · Camps universals (8)

Tots els nodes OKF han de tenir aquests 8 camps al frontmatter YAML (`CAMPS_UNIVERSALS` al validador):

| Camp | Tipus | Obligatori | Descripció |
|:---|:---|:---:|:---|
| `id` | string | ✅ | Identificador únic del node. Patró `^[A-Z0-9]+(-[A-Z0-9]+)+-\d{2}$` (`PATRO_ID`). |
| `type` | string | ✅ | Tipus de node (un dels 9 universals de §10.2 o 4 de família de §10.3). |
| `title` | string | ✅ | Títol llegible. |
| `version` | string | ✅ | Versió del node. Patró `^V\d+\.\d+(\.\d+)?(-[A-Za-zÀ-ÿ]+)?$` (`PATRO_VERSION`). |
| `data_ultima_actualitzacio` | string | ✅ | Data de la darrera modificació en format `YYYY-MM-DD`. |
| `authors` | llista de strings | ✅ | Autors del node. Mínim 1 (`CAMPS_ARRAY`). |
| `llicencia` | string | ✅ | Llicència del node. |
| `tags` | llista de strings | ✅ | Etiquetes. Almenys una amb prefix `okf/` (Y007). |

### 10.2 · Tipus universals (9)

Aquests tipus són transversals a tots els marcs legals («tancats i compartits»): `MOC`, `Guia`, `Glossari`, `Protocol`, `PaquetLLM`, `ConvencioNomenclatura`, `Llicencia`, `Plantilla`, `DocumentHandoff`. (`TIPUS_UNIVERSALS` al validador; Cores §2.)

### 10.3 · Tipus de família (4)

Aquests tipus són específics d'un marc legal. No estan fixats al codi: es llegeixen de la Convenció de Nomenclatura del vault (el validador accepta els 9 universals + els declarats). Els declarats pels Cores del kit són:

| Tipus | Marc legal | Estat |
|:---|:---|:---:|
| `CatalegCurricular` | LOE | Vigent |
| `EinaTecnica` | LOE | Vigent |
| `FitxaAEA` | LOE | Vigent |
| `UnitatDidactica` | LOGSE | Deprecated |

(*Nota:* el validador emet `Y004` per a qualsevol `type` que no sigui universal ni declarat a la Convenció, i `Y025` si `type` no és un string.)

### 10.4 · Camps específics per tipus de família

A més dels 8 camp universals, cada família declara camps propis (fonts: Core FP §8.2, §8.3 i les plantilles). El validador **no obliga** la majoria d'aquests camps (són opcionals); el model els documenta per a intercanvi entre eines.

#### CatalegCurricular

- `criteris:` — llista de diccionaris per RA amb els camps `codi`, `id`, `guia`, `descripcio`, `contextualitzat`, `afegit`, `origen` (`CAMPS_CRITERI` + `id`). Font de veritat dels CAs per a l'auditoria.
- `estat:` — opcional; del enum `vigent|esborrany|obsolet|arxivat` (defecte `vigent`).
- `visibilitat:` — opcional; del enum `publica|interna|restringida|personal|externa` (defecte `interna`).

#### FitxaAEA

- `modul:` — codi del mòdul professional (ex: `MP1519`).
- `cataleg_referencia:` — ruta relativa al catàleg que respon la fitxa.
- `cataleg_versio:` — versió del catàleg. **Deprecated** (vegeu §10.6); el validador la ignora silenciosament.
- `durada:` — durada de l'activitat (ex: `4 h`).
- `resultats_aprenentatge:` — llista de RA que treballa.
- `criteris_avaluacio:` — llista de codis oficials que avalua (ex: `["5.1", "5.2"]`).
- `instruments_avaluacio:` — llista de diccionaris amb `codi`, `descripcio`, `criteris` (`CAMPS_INSTRUMENT`).
- `naturalesa:` — `analitica` (defecte) o `sintesi` (Y036 si és invàlida).

#### UnitatDidactica (LOGSE, deprecated)

- `credit:` — codi del crèdit LOGSE. El validador només l'exigeix (Y003) si la Convenció ho declara; **mai** s'accepta en un tipus universal (Y017).
- `durada:` — durada de la unitat (ex: `8 h`).
- Camps residuals compartits amb la família LOE: `modul`, `resultats_aprenentatge`, `criteris_avaluacio` (vegeu la nota de terminologia de `PLANTILLA-UnitatDidactica.md`).

### 10.5 · Invariants del format de criteris i instruments (Y040-Y052)

Aquestes invariants s'apliquen al bloc `criteris:` dels catàlegs i a `instruments_avaluacio:` de les fitxes (`validar_invariants_format_criteris` i la validació de fitxa al validador). Severitats del `CODIS_ERROR`:

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

### 10.6 · Compatibilitat de formats

El validador accepta **dos formats** per a `criteris:` i `instruments_avaluacio:` (el validador normalitza el format antic al nou abans de validar-lo):

| Camp | Format antic | Format nou | Estat |
|:---|:---|:---|:---:|
| `criteris:` | Llista de strings per RA (`["5.1", "5.2"]`) | Llista de diccionaris (amb `codi`, `guia`, `descripcio`, `contextualitzat`, `afegit`, `origen`) | Ambdós acceptats |
| `instruments_avaluacio:` | Llista de strings/rutes (`["./prova.md#seccio"]`) | Llista de diccionaris (amb `codi`, `descripcio`, `criteris`) | Ambdós acceptats |

**Política de retirada:** els formats antics s'eliminaran a la v1.4. Fins llavors, s'accepten amb warning (el warning de format mixt — alguns dicts + alguns strings — s'afegirà a la v1.4/v1.5).

### 10.7 · Relació amb el JSON Schema

El fitxer [`01-cores/okf-core.schema.json`](../01-cores/okf-core.schema.json) (F3.1) implementa els **8 camps universals** i els **enums bàsics** (`visibilitat`, `estat`) d'aquest model. Els camps de família (`criteris:`, `instruments_avaluacio:`, `modul:`, etc.) **no estan restringits** al JSON Schema (es deixen com a `additionalProperties: true`), però sí que estan documentats en aquesta secció. Per obtenir les restriccions completes de coherència (enllaços, auditories), la font de veritat continua sent el validador (`validar_yaml.py`) i els Cores.

## 11 · Publicació i distribució dels recursos OKF

Un cop el vault OKF està construït i validat, el següent pas natural és **publicar-lo** perquè arribi a l'alumnat o a la comunitat docent. Igual que passa amb les eines d'autoria com eXeLearning, la publicació no ha d'estar lligada a una única plataforma privativa. La filosofia de sobirania del kit també s'aplica aquí: **el docent ha de poder decidir on i com publica el seu coneixement**.

Aquesta secció descriu les opcions de publicació que ofereix l'ecosistema OKF, des de la compartició del codi font fins a la generació de recursos per a plataformes LMS.

### 11.1 · Nivells de publicació

La publicació d'un vault OKF es pot fer en quatre nivells, segons l'objectiu i el públic destinatari:

| Nivell | Format | Públic | Eina / Mètode |
|:---|:---|:---|:---|
| **1. Codi font** | Fitxers `.md` + YAML | Altres docents (compartir) | ZIP del vault, repositori Git, Obsidian Publish |
| **2. Web estàtica** | HTML5 + CSS | Alumnat, comunitat | Hugo, MkDocs, GitHub Pages (com el blog d'aquest projecte) |
| **3. LMS** | Paquet SCORM o IMS | Alumnat (Moodle, Classroom) | Exportació des del Paquet LLM (futur) |
| **4. Document formal** | HTML/CSS o PDF | Inspecció, direcció | Paquet LLM 02 (Programació Didàctica) |

### 11.2 · Opcions de publicació (inspirades en les 10 vies d'eXeLearning)

L'article *Cómo publicar los recursos de eXeLearning* de Juan José de Haro descriu deu maneres de publicar un recurs. Adaptem-les al context de l'OKF:

1. **Compartir el vault en ZIP:** És l'opció més bàsica i sobirana. El docent pot descarregar el ZIP del seu vault (o del mini-vault, com a `05-exemples-minims/vault-de-3-nodes.zip`) i compartir-lo per correu o per un drive. Qualsevol persona amb un editor de text el pot obrir.
2. **Publicar en un repositori Git (GitHub, GitLab):** El vault es converteix en un repositori, versionat i col·laboratiu. És ideal per a equips docents que volen treballar junts. Es pot clonar o descarregar com a ZIP.
3. **Web estàtica amb Hugo o MkDocs:** A partir dels fitxers Markdown, es pot generar un lloc web (HTML5) que es pot penjar a **GitHub Pages**, a un servidor del centre o a qualsevol allotjament estàtic. Aquesta és l'opció que hem fet servir per al blog d'aquest projecte (vegeu `okf-blog` a l'ecosistema).
4. **Obsidian Publish:** Si el docent treballa amb Obsidian, pot publicar el vault directament amb aquest servei (de pagament), mantenint la privacitat i la sincronització.
5. **Google Sites / Google Drive:** Es pot exportar el contingut com a HTML i pujar-lo a Google Sites o Google Drive per compartir-lo amb l'alumnat. És una opció còmoda per a centres que ja fan servir Google Workspace.
6. **Exportació a HTML autocontingut:** El Paquet LLM 02 pot generar un fitxer `.html` únic (amb CSS incrustat) que es pot obrir sense internet i desar com a document.
7. **Paquet SCORM per a Moodle:** (Futur) El Paquet LLM 03 podria generar un paquet SCORM a partir dels nodes AEA, perquè es pugui pujar directament a Moodle o a qualsevol LMS compatible.
8. **Document PDF / Word:** El Paquet LLM 02 ja genera un document HTML/CSS que es pot importar a Word i desar com a PDF. És l'opció per a Inspecció o per a la direcció del centre.
9. **Impressió en paper:** A partir del document HTML/PDF, es pot imprimir el material per a l'alumnat que no té accés a dispositius digitals.
10. **Publicació al fòrum o a la comunitat:** Compartir l'experiència i els aprenentatges en un fòrum (com eDigital) o en un blog personal. És l'opció per difondre el projecte i crear comunitat.

### 11.3 · Com els Paquets LLM hi poden ajudar

Els Paquets LLM (especialment el **Paquet 02**) ja estan dissenyats per generar un document de Programació Didàctica en HTML/CSS. Però poden anar més enllà:

- **Generació de web estàtica:** Un sub-prompt pot convertir els nodes del vault en un lloc web (Hugo/MkDocs) llest per publicar a GitHub Pages.
- **Generació de paquets SCORM:** (Futur) Un prompt pot empaquetar els nodes AEA en un fitxer SCORM per a Moodle.
- **Generació de recursos per a Google Sites:** Un prompt pot exportar els continguts en format HTML compatible amb Google Sites.

**La idea és que la IA no només generi el contingut, sinó que també ajudi a publicar-lo**, respectant la sobirania del docent (que tria on publicar).

### 11.4 · Publicació al blog personal (cas pràctic)

El blog personal d'aquest projecte (a `https://jmonta23-okf.github.io/`) és un exemple de com publicar un article de reflexió (com el de *Del laboratori a la sala de mestres*). El flux és:

1. Escriure l'article en Markdown (dins del vault o al blog).
2. Generar el lloc estàtic amb Hugo.
3. Pujar-lo a GitHub Pages (o al servidor del centre).
4. Compartir l'enllaç a LinkedIn, fòrums o xarxes socials.

Aquest flux és totalment sobirà i es pot replicar per a qualsevol docent que vulgui publicar els seus materials.

### 11.5 · Recomanacions

- **Per a compartir amb altres docents:** ZIP o repositori Git.
- **Per a l'alumnat:** Web estàtica (Hugo/MkDocs) o SCORM (si el centre té Moodle).
- **Per a Inspecció:** Document HTML/PDF (Paquet 02).
- **Per a difusió:** Blog personal i xarxes socials (LinkedIn).

**Recorda:** la publicació ha de servir per compartir el coneixement, no per quedar atrapat en una plataforma. El text pla és el format més durador i el que millor resisteix els canvis de programari.
---

*Document creat el 3 de novembre de 2026. Forma part del RFC-OKF-02 (arquitectura del graf curricular de dues capes).*
