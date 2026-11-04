# Changelog

Tots els canvis notables d'aquest projecte es documenten en aquest fitxer.

El format es basa en [Keep a Changelog](https://keepachangelog.com/ca/1.1.0/)
i aquest projecte segueix [Versionat Semàntic](https://semver.org/lang/ca/).

---

## [No publicat] — Bloc 14d: instruments_avaluacio estructurat

### Afegit

- **`03-eines/validar_yaml.py`** — format nou d'`instruments_avaluacio` (llista de dicts) a les `FitxaAEA`, compatible amb el format antic (llista de strings), amb 2 codis nous:
  - `Y050` — 'codi' d'instrument duplicat (no nul) dins la fitxa. 🟠 Alta.
  - `Y051` — instrument en format nou (dict) sense cap criteri. 🟡 Mitjana. **No s'aplica als instruments en format antic (strings).**
  - `normalitzar_instruments_avaluacio()`: normalitza strings→dicts; `Y051` s'avalua sobre la llista original i només sobre dicts.
  - Warnings textuals a `--- Warnings ---`: format antic (una per fitxa) i camp desconegut (una per (fitxa, camp)).
  - Total de codis: 33 → **35**.
- **`04-plantilles/PLANTILLA-FitxaAEA.md`** — afegit el camp `instruments_avaluacio` al frontmatter (format nou) amb la nota d'format antic obsolet.
- **`tests/test_validar_yaml.py`** — 7 tests nous.

### No s'ha tocat

- `Y052` (ajornat al Bloc 14f), `Y049` lliure. Les fitxes d'exemple (format antic) es mantenen fins al 14e.

---

## [No publicat] — Bloc 14c: Y044 i Y048

### Afegit

- **`03-eines/validar_yaml.py`** — tanca la validació del format de `criteris:` amb 2 codis nous:
  - `Y044` — `afegit: true` i `contextualitzat: true` alhora (redundant). 🟡 Mitjana.
  - `Y048` — `criteris[RA]` no és una llista. 🟠 Alta.
  - Total de codis d'error: 31 → **33**.
- **`tests/test_validar_yaml.py`** — 2 tests nous (`Y044` i `Y048`).

### No s'ha tocat

- `Y041` (retirat de la v1.3), `Y045`/`Y046` (ajornades al Bloc 14f). `instruments_avaluacio`, els catàlegs d'exemple (format antic) i la plantilla es mantenen.

---

## [No publicat] — Bloc 14b: format nou de `criteris:` (v3)

### Afegit

- **`03-eines/validar_yaml.py`** — format nou de `criteris:` (llista de dicts), compatible amb el format antic (llista de strings), amb 3 codis nous d'invariants del format:
  - `Y040` (`contextualitzat` no boolean) — 🟠 Alta.
  - `Y042` (`codi` nul sense `afegit: true`) — 🔴 Crític.
  - `Y043` (`afegit: true` sense camp `guia`) — 🔴 Crític.
  - `normalitzar_criteris()`: normalitza el format antic al canònic intern; conserva els `null` explícits perquè les invariants els puguin detectar.
  - Els camps desconeguts dins d'un dict emeten una advertència textual a la secció `--- Warnings ---` (una línia per camp únic al catàleg), sense codi Y i sense afectar el codi de sortida.
  - `Y030`/`Y031` i `audit_curricular` llegeixen de l'estructura normalitzada; un CA amb `codi: null` (afegit) no espera àncora i no dispara `Y030`.

### Modificat

- **`04-plantilles/PLANTILLA-CatalegCurricular.md`** — exemple del format nou de `criteris:` amb els 6 camps, comentaris per contextualitzar i afegir CAs, i CAs d'anglès professional comentats.
- **`tests/test_validar_yaml.py`** — 7 tests nous (normalització dels dos formats, `Y040`/`Y042`/`Y043`, i warning de camp desconegut amb dedup).

### No s'ha tocat

- `Y041`, `Y044`, `Y045`, `Y046` no s'implementen en aquest bloc. `instruments_avaluacio` i els catàlegs d'exemple (format antic) mantenen l'estat actual fins als Blocs 14c/14d/14e.

---

## [No publicat] — Bloc 14a: deprecacions toves

### Modificat

- **`03-eines/validar_yaml.py`** — deprecacions toves (RFC-OKF-03, V1.3), sense canvi de format de dades:
  - `Y035` (àlies duplicat) rebaixat de 🔴 Crític a 🟠 Alta.
  - `Y036` (`naturalesa` invàlida) rebaixat de 🟠 Alta a 🟡 Mitjana (warning).
  - `cataleg_versio` s'ignora silenciosament (ni error ni warning).
  - `--strict-versio` esdevé no-op: emet el warning literal `--strict-versio is deprecated; version mismatch is always a warning` i no canvia el codi de sortida.
  - El mismatch de versió de `--audit` es marca com a informatiu/deprecated i no afecta el veredicte ni el codi de sortida.
- **`01-cores/OKF-CORE-FP-00.md`** (§8.2) — `cataleg_versio` marcat com a deprecated (llegat).

---

## [V1.2] - 2026-11-02

**Publicació oficial de la V1.2.** Consolida el validador v1.1.0 (sincronitzat amb els Cores), afegeix l'eina d'snapshot de l'estat del repositori, i alinea tota la documentació pública amb el Core v1.1.0 (8 camps universals, 9 tipus universals, tipus de família des de la Convenció, matriu d'errors Y001-Y026).

### Afegit

- **`03-eines/status_snapshot.py`** — Eina de només lectura que genera un snapshot estandarditzat de l'estat del repositori (branca, HEAD, working tree, últims 5 commits, validador, tests, recompte de nodes). Modes: `--quick`, `--full` (per defecte), `--audit`, `--since <ref>`. Pensada per enganxar en briefs i converses amb assistents.
- **6 tests nous** per a `status_snapshot.py` (`tests/test_status_snapshot.py`). Total: **30 tests**.
- **Pas nou al CI** (`.github/workflows/test.yml`): `Snapshot (quick)` a cada push/PR.
- **Secció «Snapshot de l'estat del repositori»** a `CONTRIBUTING.md`.
- **Paràgraf «L'eina d'snapshot»** i menció a la taula d'eines del `README.md`.
- **Nota `--output`** al `CONTRIBUTING.md` per evitar que el validador embruti `EINES/` en execucions manuals.

### Modificat

- **Documentació pública alineada amb el Core v1.1.0** (Bloc 9.5):
  - `03-arquitectura.md`: taula de camps universals (8 reals), «15 tipus» → «9 universals + família», `PaquetLLM` fora de la secció `credit`, matriu d'errors Y001-Y026, «400 línies» → «901 línies».
  - `05-glossari.md`: «Camp universal obligatori» amb els 8 camps reals, «15 tipus» → «9 universals + família», llistes de tipus corregides.
  - `04-plantilles/README.md`: `PaquetLLM` fora de la columna `credit`, nota de política de `credit` reescrita.
  - `00-index.md`: descripció de `03-arquitectura.md` actualitzada.
- **README**:
  - Bloc de sortida del validador amb el format real del v1.1.0 (taula resum + «## ✅ Resultat»).
  - Badge Status → `V1.2` (URL slug i alt text).
  - Badge DOI → **concept DOI (23823818)** amb el format correcte de Zenodo (`DOI/10.5281/zenodo.23823818.svg`).
  - Versions dels Cores a la línia 200: `V1.1.2, V1.0.2` (abans `V1.1.1, V1.0.1`).
- **Headers i peus de 11 fitxers**: DOI de versió (23823819) → **concept DOI (23823818)**, per política nova (els headers descriuen el projecte, no una versió concreta).
- **`02-filosofia.md:111`**: «d'unes 400 línies» → «d'unes 900 línies» (mida real del validador).

### Corregit

- **Badge DOI trencat (HTTP 404)** des de la V1.1: el format `zenodo.org/badge/23823819.svg` no és vàlid; el correcte és `zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg`.
- **Fence orfe** al final de `01-que-es-okf.md`.
- **Fence orfe** al final de `03-arquitectura.md`.
- **Fence orfe** al final de `CONTRIBUTING.md`.
- **Newline final absent** al `CHANGELOG.md`.

### Estat

- **Repositori:** evolució contínua des de la publicació de la V1.1 (31/10/2026).
- **27 nodes OKF** al kit (0 errors).
- **30 tests** (24 existents + 6 de `status_snapshot.py`).
- **5 fitxers Python** (4 eines + 1 test runner).
- **CI verd** (pytest + validador + snapshot a cada push/PR).
- **Validador**: v1.1.0 (8 camps universals, 9 tipus universals, tipus de família des de la Convenció, comprovacions de graf, Y001-Y026).
- **Cores**: Català v1.1.2, FP v1.0.2.

### DOI

- **DOI de versió V1.2**: [10.5281/zenodo.23888081](https://doi.org/10.5281/zenodo.23888081)
- **Concept DOI** (sempre apunta a l'última versió): [10.5281/zenodo.23823818](https://doi.org/10.5281/zenodo.23823818)
- **DOI de versió V1.1** (anterior): [10.5281/zenodo.23823819](https://doi.org/10.5281/zenodo.23823819)

---

## [Validador v1.2.0] - 2026-11-03

**Versió del validador** (no del kit). Acompanya el kit V1.2 amb la funcionalitat d'auditoria curricular.

### Afegit

- **`--audit`**: auditoria de cobertura curricular per catàleg. Llegeix els catàlegs, les fitxes AEA, i calcula orfes/inexistents/mismatch de versió.
- **`--strict-versio`**: tracta el mismatch de versió com a error (per defecte és warning).
- **Codis Y030 i Y031**: coherència YAML↔àncores (criteri al frontmatter sense àncora al cos, i viceversa).
- **Codis Y035 i Y036**: àlies de tipus duplicats i `naturalesa` invàlida.

### Modificat

- **Àlies de tipus**: el validador llegeix la secció `## X · Àlies de tipus` de les Convencions i normalitza `Activitat` → `FitxaAEA`, `Cataleg` → `CatalegCurricular`.
- **`naturalesa`**: el camp s'accepta a qualsevol node amb `type` de família, amb valors `analitica` o `sintesi` (per defecte `analitica`).

### Codis de sortida

- **`--audit`**: 0 (tots els catàlegs coberts), 1 (algun catàleg amb orfes o inexistents), 2 (només warnings o sense catàlegs).

### Tests

- **40 passed, 1 skipped** (24 originals + 2 d'àlies/naturalesa + 2 de coherència + 6 d'auditoria + 1 skip per `instruments_per_criteri`).

---

## [V1.1-publicació] - 2026-10-31 · DOI: [10.5281/zenodo.23823819](https://doi.org/10.5281/zenodo.23823819)

### Afegit
- **Publicació oficial a GitHub i Zenodo:** primera versió pública del kit amb DOI permanent.
- **Secció "Com citar aquest projecte"** al README: APA, BibTeX i text pla.
- **Badge del DOI** a la capçalera del README.
- **7 handoffs (00-06)** documentant tot el desenvolupament. Es conserven fora del repo, a `~/Documents/OKF-CATALA/okf-handoffs/`.

### Modificat
- **Neteja del repo:** eliminació dels handoffs interns (no són contingut del kit públic) i del fitxer `05-exemples-minims/vault-de-3-nodes/EINES/Scripts/informe_validacio_2026-10-25.md` (artefacte del validador).
- **README:** afegida la secció "Com citar", el badge del DOI, i la referència als tres projectes germans (TCAI-OKF, SAD-GRAF, PTE-OKF).
- **00-index.md:** afegit el DOI, els tres projectes germans, els 7 handoffs i la referència a `06-comunitat/`.
- **Repo recreat:** historial net amb 3 commits (`a226ac0`, `52b8d76`, `2f63176`).

### Estat
- **23 nodes OKF** validats amb **0 errors**.
- **Mòdul MP1519** completament desplegat a `02-exemple-complet/`.
- **3 nodes** a `05-exemples-minims/` (LOGSE/C1).
- **6 plantilles** a `04-plantilles/`.
- **2 Cores** a `01-cores/`.

---

## [V1.1] - 2026-10-29

### Afegit
- **Bloc 8 — Comunitat (`06-comunitat/`):** 4 documents humans:
  - `README.md` — presentació de la carpeta.
  - `01-casos-us.md` — els tres casos reals (Benet M. a Química, César G. a Sanitat, Ariadna C. a Pedagogia Terapèutica).
  - `02-com-compartir.md` — guia pràctica per compartir el kit o el vault amb privacitat.
  - `03-article-edigital.md` — article de difusió per a `comunitat.edigital.cat`.
- **Validador v1.0.2:** exclou `06-comunitat/` de la validació (com `00-documentacio/`).
- **Exemple complet de 11 nodes canònics** a `02-exemple-complet/` (MP1519, LOE Sanitat):
  - 5 Fitxes AEA (DIKW → auditoria clínica d'expedients).
  - Protocol d'avaluació de tres portes i matriu OC (C1-C6).
  - Paquet LLM amb 7 capes anti-al·lucinació, Taula dels 10 Falsos Amics i regla dels 3 artefactes separats.
  - Guia d'arquitectura Dual-User (SYS_PROMPT oficial, NotebookLM, RGPD).
  - Validador determinista local en Python/SQLite (`cie10es_validator.py`).
  - Eina d'automatització amb Google Workspace (Hub-Spoke de 5 fulls).
- **MIAE (Nivell 3)** i **VCER** (*Vibe Coding Educatiu Responsable*) integrats a la documentació central i a `PLANTILLA-PaquetLLM.md`.

### Modificat
- **Documentació central humanitzada** (`00-documentacio/`): to "de docent a docent", mirada ontològica i biològica, distinció entre *currículum oficial* i *programació didàctica viva*, i superació de la "tirania de les carpetes".
- **Privacitat:** ús d'inicials (**Benet M.**, **César G.**, **Ariadna C.**, **Montse G.**) i supressió de noms de centres educatius.
- **README:** reescrit amb la metàfora del sistema operatiu, el taller, la genealogia dels tres projectes germans i la secció "Amb qui he après".
- **02-filosofia.md:** reescrit com a manifest (7 principis, transparència honesta, factor Montse, sobreenginyeria).
- **PLANTILLA-PaquetLLM.md:** afegit el contracte VCER i el checklist d'aula.

---

## [V1.0-Esborrany] - 2026-10-28

### Afegit
- **Metàfora del sistema operatiu** a la filosofia i al README.
- **Genealogia dels dos projectes germans** (TCAI-OKF + SAD-GRAF) al README i a `02-filosofia.md`.
- **Doble lectura d'OKF** (*Open Knowledge Format* + *Organized Knowledge Framework*) a `01-que-es-okf.md` i al glossari.
- **Secció "El taller"** a la filosofia: els Paquets LLM com a espai de creació docent.

### Modificat
- **README:** ampliat amb 7 situacions del problema (traçabilitat, nomenclatura, versions, demostrabilitat, traspàs, reaprofitament, programacions que encaixen amb tot).

---

## [V1.0-Esborrany] - 2026-10-27

### Afegit
- **Marc MIAE (Nivell 3)** a `PLANTILLA-PaquetLLM.md`.
- **Curs OKF-CURS-MP1523** (projecte paral·lel, fora del repo): 9 mòduls, 59 nodes OKF, 0 errors.
- **Primer push a GitHub** (repositori privat).

---

## [V1.0-Esborrany] - 2026-10-26

### Afegit
- **Bloc 5 — 5 plantilles canòniques:** MOC, UnitatDidactica, PaquetLLM, Protocol, FitxaAEA.
- **Bloc 7 — Exemple complet MP1519** (7 nodes inicials: MOC, Catàleg, 2 Fitxes AEA, PaquetLLM, Protocol, README).
- **Convenció YAML mixta** (framework en anglès, domini en català) documentada a `03-arquitectura.md` i al glossari.

### Modificat
- `02-exemple-credit/` renombrat a `02-exemple-complet/`.
- Micro-rúbrica de 2 punts corregida a l'exemple complet.

---

## [V1.0-Esborrany] - 2026-10-25

### Afegit
- **Estructura bàsica del projecte** (6 carpetes: `00-documentacio/`, `01-cores/`, `02-exemple-complet/`, `03-eines/`, `04-plantilles/`, `05-exemples-minims/`, `06-comunitat/`).
- **`LICENSE.md`** amb doble llicència (MIT + CC BY-SA 4.0).
- **`README.md`** (portada del repositori).
- **`04-inici-rapid.md`** (tutorial de 30 minuts).
- **`05-exemples-minims/vault-de-3-nodes/`** amb 3 nodes validats (MOC + UD + FitxaAEA).
- **`03-eines/validar_yaml.py` v1.0.0** (validador genèric del kit, 15 tipus de node).
- **`04-plantilles/PLANTILLA-ConvencioNomenclatura.md`** (plantilla de Convenció).
- **2 Cores** (`01-cores/`): OKF-CORE-CATALA-00 (LOMLOE) i OKF-CORE-FP-00 (LOE/FP).
- **Blocs 1, 2, 3, 4a, 4b, 6** completats (estructura, governança, validador, documentació conceptual i pràctica, Cores).

### Notes
- Aquesta és la primera versió del kit. És un esborrany i pot canviar.
- El validador és una adaptació del TCAI-OKF, pensada per a un kit genèric.

---

## Notes sobre el versionat

- **Concept DOI:** [10.5281/zenodo.23823818](https://doi.org/10.5281/zenodo.23823818) — sempre apunta a l'última versió del projecte. **Recomanat per a citacions generals**, per a headers de documents i per al badge del README.
- **DOI de versió:** cada release a GitHub genera un DOI de versió nou (V1.1 = `10.5281/zenodo.23823819`; V1.2 = `10.5281/zenodo.23888081`). **Recomanat per a citacions que hagin de ser reproduïbles en una versió concreta.**
- **Política del kit:** els headers i peus dels documents fan servir el **concept DOI** (descriuen el projecte, no una versió). Les **citacions APA/BibTeX de versió** (README, CONTRIBUTING, 00-index, article d'eDigital) fan servir el **DOI de versió** corresponent.
- **Format del badge Zenodo:** `https://zenodo.org/badge/DOI/10.5281/zenodo.<id>.svg`. El format `https://zenodo.org/badge/<id>.svg` **no és vàlid** (retorna 404).
