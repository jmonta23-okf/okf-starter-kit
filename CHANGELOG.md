# Changelog

Tots els canvis notables d'aquest projecte es documenten en aquest fitxer.

El format es basa en [Keep a Changelog](https://keepachangelog.com/ca/1.1.0/)
i aquest projecte segueix [Versionat Semàntic](https://semver.org/lang/ca/).

---

## [No publicat] — propera versió

### F0 · Neteja i coherència inicial

- **Badge del README** actualitzat a V1.3.
- **`requirements.txt`** creat amb `pyyaml>=6.0`.
- **Docstring dels Cores** corregida (`V1.1.0 / V1.1.2`).
- **`ROADMAP.md`** mogut a `00-documentacio/` (exclòs del validador) i afegit a l'índex.
- **CHANGELOG**: eliminades les entrades `[No publicat]` redundants (la [V1.3] ja les resumeix).
- **`cataleg_versio`** eliminat de les 10 fitxes AEA i de la prosa del MOC/Handoff.
- **BibTeX del README** actualitzat a `version = {V1.3}`.
- **`07-com-compartir.md`**: netejada la cua anòmala (fence orfe + fragment conversacional) i afegit enllaç a `02-com-compartir.md`.

### F1 · Consolidació semàntica (RFC-OKF-03)

- **F1.1** · **Identitat dels CAs afegits**: nou camp `id` als CAs amb `afegit: true`, perquè puguin ser referenciats des de `criteris_avaluacio`. `Y045` deixa de disparar-se si el CA afegit és referenciat per `id`. Fallback a `guia` per a CAs sense `id` (compatibilitat). Commit `0ff7d39`.
- **F1.2** · **`Y052` no s'aplica a fitxes amb instruments en format antic o mixt** (alguns elements no són `dict`). Elimina falsos positius durant la migració. Test de regressió inclòs. Commit `0c13e0a`.
- **F1.3** · **Auditoria per catàleg**: `Y045` i `Y046` es calculen per catàleg, no globalment. El veredicte global és `INCOMPLET` si **algun** catàleg té orfes o inexistents. Els missatges inclouen l'`id` del catàleg (`(catalog: MP1519-CAT-00)`). Commit `eacc716`.

### F2.5 · Correccions de l'auditoria externa

- **F2.5.a** · Correccions de baix cost i alt impacte detectades per l'auditoria externa:
  - DOIs actualitzats a V1.3 (`23964880`) a `CONTRIBUTING.md`, `00-documentacio/00-index.md` i `06-comunitat/03-article-edigital.md`.
  - Recompte de plantilles corregit: «6» → «7» (a `README.md` i `04-plantilles/README.md`).
  - Recompte de nodes del mini-vault corregit: «3» → «5» (a `00-documentacio/04-inici-rapid.md`).
  - **Text de privacitat honest**: el README diu que el validador comprova la coherència dels flags de privacitat (`dades_personals`, `anonimitzat`, `visibilitat`), no que «detecta dades personals». La detecció de dades personals en prosa és responsabilitat del docent (revisió manual).
  - **Tests de snapshot resilients sense `.git`**: `test_snapshot_format` i `test_snapshot_deterministic` fan `skip` si no hi ha `.git` (per exemple, quan es baixa el ZIP de GitHub).
  - Commit `3184e0d`.
- **F2.5.b1** · Documentació i portabilitat:
  - Documentada la relació entre `02-exemple-complet/` i `07-exemple-mp1519/`: són dues variants del mateix mòdul (MP 1519), totes dues amb el format nou de la V1.3. La diferència principal és el MOC (`07` és més detallat). `07-exemple-mp1519/` es va crear al **Bloc 12d** com a exemple focalitzat de l'arquitectura de dues capes.
  - **Mini-vault portable**: eliminat l'enllaç a `../../01-cores/` de `05-exemples-minims/vault-de-3-nodes/03_C1_Convencio.md`. El mini-vault ja no depèn de carpetes del kit.
  - Commit `dfd72c2`.
- **F2.5.b2** · **MOC absent → `Y014`**: ara un vault sense cap node `MOC` emet `Y014` (`No MOC node found in vault`) a més dels `Y018` que corresponguin. La comprovació és global (després de validar tots els nodes) i només s'aplica a directoris. Commit `d87437b`.

### F3 · Reducció de fricció (parcial)

- **Taula de decisió inductiu/deductiu** a `00-documentacio/04-inici-rapid.md`: ajuda el docent a triar quin Paquet LLM fer servir segons el seu punt de partida. Commit `c610ad0`.
- **Secció «El docent no és un programador»** a `00-documentacio/02-filosofia.md` (§9): respon a la crítica que el docent mitjà es perdrà en els YAML. El kit no pretén que els docents es converteixin en programadors, sinó que entenguin l'estructura del coneixement curricular i sàpiguen guiar una IA. Commit `f879dc4`.
- **`PLANTILLA-PaquetLLM-00.md`** (Paquet deductiu): parteix del currículum oficial i baixa cap a la pràctica. Útil per a mòduls nous o per a docents que volen repensar la programació des de zero. Commit `f879dc4`.
- **`PLANTILLA-PaquetLLM-01.md`** (Paquet inductiu): parteix de la programació existent del docent i puja cap al currículum. Útil per a docents que ja tenen una programació feta i no volen reescriure-la. Commit `f879dc4`.
- **`PLANTILLA-PaquetLLM-02.md`** (Paquet de sortida): genera el document oficial de Programació Didàctica en HTML/CSS a partir dels nodes del vault (MOC, Catàleg, Protocol, Fitxes AEA). Inclou l'exemple complet `exemples/Programacio_Didactica_MP1519.html`. Commit `[pendent]`.

### Descartat

- **D3 (detecció de DNI/NIE en prosa)**: descartat. Un kit de Sanitat genera casos clínics ficticis amb DNIs inventats; un regex de DNI generaria falsos positius constants per a zero valor. El risc real es cobreix amb els flags de privacitat i la revisió manual (que el README ja documenta).

### Estat

- Validador v1.3.0, **38 codis**, 0 errors.
- `--audit` per catàleg: 2 catàlegs coberts, 52/52/0/0.
- **75 tests passed, 1 skipped.**
- CI verd.
- **Política de retirada:** els formats antics de `criteris:` i `instruments_avaluacio` s'eliminaran a la v1.4. Fins llavors, s'accepten amb warning. El warning de format mixt (alguns elements dict + alguns strings) s'afegirà a la v1.4/v1.5.

---

## [V1.3] — 2026-11-04

### Completitud normativa del graf de dues capes (RFC-OKF-03)

Implementació del RFC-OKF-03 v0.1: suport normatiu complet al graf
curricular de dues capes (criteris contextualitzats, CAs afegits,
instruments d'avaluació estructurats).

#### Canvis principals

- **Format nou de `criteris:` als catàlegs** (llista de diccionaris). Es manté
  la compatibilitat amb el format antic.
- **Format nou d'`instruments_avaluacio` a les fitxes AEA** (llista de
  diccionaris). Es manté la compatibilitat amb el format antic.
- **10 codis d'error nous**: `Y040`, `Y042`, `Y043`, `Y044`, `Y045`, `Y046`,
  `Y048`, `Y050`, `Y051`, `Y052`. Total: **28 → 38 codis**.
- **`--audit` actualitzat**: `CAs coberts`, `CAs contextualitzats (*)`, `CAs
  afegits pel docent`. Es mantenen `CAs avaluats (analítics)` i `Mismatch de
  versió` per compatibilitat amb `status_snapshot.py`.
- **Deprecacions toves**: `cataleg_versio` (silenciós), `--strict-versio`
  (no-op amb warning), `Y035` (🔴 → 🟠), `Y036` (🟠 → 🟡).

#### Blocs

14a (deprecacions), 14b (format `criteris:`), 14c (Y044/Y048), 14d
(`instruments_avaluacio`), 14e (migració de catàlegs), 14f (instruments a les
10 fitxes), 14g (`--audit` + Y045/Y046), 14g-bis (Y052).

#### Codis d'error (38)

`Y001-Y009`, `Y012-Y026`, `Y030`, `Y031`, `Y035`, `Y036`, `Y040`, `Y042`,
`Y043`, `Y044`, `Y045`, `Y046`, `Y048`, `Y050`, `Y051`, `Y052`.
(`Y010`/`Y011` no existeixen; `Y047`/`Y049` lliures.)

#### Compatibilitat

- Catàlegs i fitxes en format antic continuen funcionant.
- `status_snapshot.py` no s'ha modificat.
- Tots els tests passen (63 passed, 1 skipped).
- **Política de retirada:** els formats antics de `criteris:` i
  `instruments_avaluacio` s'eliminaran a la v1.4. Fins llavors, s'accepten amb
  warning.

#### Referències

- RFC-OKF-03 v0.1 (document intern).
- HANDOFF-09 (pre-V1.3) i HANDOFF-10 (post-V1.3).
- Reial Decret 768/2014 (MP 1519).

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
- El validador és una adaptació del TCAI-OKF, pensat per a un kit genèric.

---

## Notes sobre el versionat

- **Concept DOI:** [10.5281/zenodo.23823818](https://doi.org/10.5281/zenodo.23823818) — sempre apunta a l'última versió del projecte. **Recomanat per a citacions generals**, per a headers de documents i per al badge del README.
- **DOI de versió:** cada release a GitHub genera un DOI de versió nou (V1.1 = `10.5281/zenodo.23823819`; V1.2 = `10.5281/zenodo.23888081`; V1.3 = `10.5281/zenodo.23964880`). **Recomanat per a citacions que hagin de ser reproduïbles en una versió concreta.**
- **Política del kit:** els headers i peus dels documents fan servir el **concept DOI** (descriuen el projecte, no una versió). Les **citacions APA/BibTeX de versió** (README, CONTRIBUTING, 00-index, article d'eDigital) fan servir el **DOI de versió** corresponent.
- **Format del badge Zenodo:** `https://zenodo.org/badge/DOI/10.5281/zenodo.<id>.svg`. El format `https://zenodo.org/badge/<id>.svg` **no és vàlid** (retorna 404).