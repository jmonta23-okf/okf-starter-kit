# Full de ruta — OKF Starter Kit

> Document viu. S'actualitza quan arriba un informe nou (intern o extern).
> Els informes originals no es guarden: les seves aportacions s'integren aquí o es descarten.
> **Última revisió:** 2026-11-10 · **Versió del document:** 1.10 (F3.1, F3.2, F3.4 i F3.5 completades)

---

## 1 · Principis

1. **Consolidar abans d'ampliar.** No afegir codis Y ni camps fins que els existents siguin semànticament consistents.
2. **Reduir fricció.** Cada decisió es valora per si acosta el kit a un docent sense coneixements de terminal.
3. **No sobreenginyeria.** Un sol document de planificació, no un arxiu d'informes. Una eina, no quatre.
4. **Verificar abans de corregir.** Els problemes detectats en informes s'han de convertir en proves reproduïbles abans de tocar codi.

---

## 2 · Estat actual (2026-11-05, post-F0/F1/F2.5 + Paquets)

| Component | Estat |
|:---|:---|
| Validador | v1.3.0, 38 codis, **75 passed + 1 skipped** |
| Criteris (`criteris:`) | Format nou (dicts) + compatibilitat amb strings |
| Instruments (`instruments_avaluacio`) | Format nou (dicts) + compatibilitat amb strings |
| `--audit` | Mètriques noves + Y045/Y046/Y052, **per catàleg** |
| CAs afegits | Camp `id` estable, referenciables des de `criteris_avaluacio` |
| MOC absent | Detectat amb `Y014` (comprovació global, només per a directoris) |
| Paquets LLM | **00 (deductiu)** i **01 (inductiu)** documentats i desats a `04-plantilles/` |
| Documentació | 7 documents actualitzats (14h-a, 14h-b) + ROADMAP + CHANGELOG + filosofia + inici ràpid |
| Release | Tag `V1.3`, DOI `10.5281/zenodo.23964880` |
| CI | Verd |
| Paquets LLM | **00 (deductiu)**, **01 (inductiu)** i **02 (sortida)** documentats i desats a `04-plantilles/` |

**Prova d'usabilitat en curs:** docent extern (Alícia, mòdul **0056** — *Atenció sanitària especial en situacions d'emergència*, CFGM en Emergències Sanitàries – TES).  
- **Vault:** `~/.hermes/okf-curs-0056/` — 6 fitxers (`00_MOC.md`, `01_Cataleg_Curricular.md`, `02_Protocol_Avaluacio.md`, `03_Convencio.md`, `04_Handoff.md`, `05_Paquet_LLM-00.md`).  
- **Catàleg:** 43 CAs, 6 RAs, 43 àncores.  
- **Estat:** validat amb 0 errors; auditoria: 43 CAs al decret, 43 orfes (esperat, perquè encara no hi ha fitxes).  
- **Aproximació híbrida:** l'Alícia genera l'AEA amb el seu model d'IA (Paquet LLM-00), nosaltres la validem amb el validador i li tornem el resultat. No se li exigeix instal·lar Python.  
- **Resultats pendents d'integrar.** És la informació més valuosa que tindrem: on es perd un docent real.

**Problemes resolts a F0/F1/F2.5:**
- ~~El badge del README encara diu V1.2.~~ → **Resolt** (F0-a).
- ~~No hi ha `requirements.txt`.~~ → **Creat** (F0-a).
- ~~`cataleg_versio` deprecated als exemples.~~ → **Eliminat** (F0-b).
- ~~DOIs desactualitzats a CONTRIBUTING, 00-index i article eDigital.~~ → **Actualitzats a V1.3** (F2.5.a).
- ~~Recompte de plantilles i nodes incorrecte.~~ → **Corregit** (F2.5.a).
- ~~Text de privacitat sobrepromès.~~ → **Ajustat** (F2.5.a).
- ~~Tests de snapshot fallen sense `.git`.~~ → **Fan `skip`** (F2.5.a).
- ~~Exemple mínim no portable.~~ → **Portable** (F2.5.b1).
- ~~MOC absent mal diagnosticat.~~ → **`Y014` global** (F2.5.b2).

**Problemes resolts a la documentació dels Paquets:**
- ~~Els docents no saben per on començar (corba d'entrada).~~ → **Paquets 00 i 01** (taula de decisió a `04-inici-rapid.md`, secció 9 a `02-filosofia.md`).
- ~~Crítica: «el docent es perdrà en els YAML».~~ → **Resposta a `02-filosofia.md` §9** («El docent no és un programador»).

---

## 3 · Prioritats P0 (consolidació semàntica) ✅ **Fet a F1**

### 3.1 · Identitat dels criteris afegits (P0) ✅ **Fet a F1.1**

**Implementat al commit `0ff7d39`.** Nou camp `id` als CAs amb `afegit: true`. Format: `{catalog_id}-RA{N}-ADD-{NN}` (o `{filename_stem}-RA{N}-ADD-{NN}` si el catàleg no té `id`). Els CAs afegits amb `id` poden ser referenciats des de `criteris_avaluacio`, i Y045 no es dispara per a ells. CAs afegits sense `id` → fallback a `guia` (compatibilitat).

**Criteri de tancament:** un CA afegit referenciat per `id` no dona Y045 ni "inexistent". ✅ Complert.

### 3.2 · Y052 i el format antic (P0 — decisió de disseny, no bug) ✅ **Fet a F1.2**

**Implementat al commit `0c13e0a`.** Y052 no s'aplica si algun element de `instruments_avaluacio` no és un `dict` (format antic o mixt). Test de regressió inclòs.

**Criteri de tancament:** una fitxa amb instruments en format antic no genera Y052. ✅ Complert.

**Pendent per a v1.4/v1.5:** afegir un warning textual quan es detecti format mixt (alguns dicts + alguns strings).

---

## 4 · Prioritats P1 (correccions del kit, no del model) ✅ **Fet a F1.3**

### 4.1 · Auditoria per catàleg (Y045/Y046) ✅ **Fet a F1.3**

**Implementat al commit `eacc716`.** Y045 i Y046 es calculen per catàleg, no globalment. El veredicte global és INCOMPLET si algun catàleg té orfes o inexistents. El desglossament per catàleg mostra l'ID, el veredicte i les mètriques de cada catàleg.

**Criteri de tancament:** un vault amb dos catàlegs i codis repetits no barreja les auditories. ✅ Complert.

---

## 5 · Pla per fases

| Fase | Objectiu | Durada | Prioritat | Estat |
|:---:|:---|:---:|:---:|:---:|
| **F0** | Correccions immediates (badge, requirements, docstring, neteja) | 1-2 dies | 🔴 P0 | ✅ **Fet** |
| **F1** | Consolidació semàntica (§3) | 2-3 setmanes | 🔴 P0 | ✅ **Fet** |
| **F2** | Robustesa del validador (tipus i proves) | 1-2 setmanes | 🔴 P0 | 🔜 **Proper fita** |
| **F2.5** | Correccions de l'auditoria externa | 1 setmana | 🔴 P0 | ✅ **Fet** |
| **F3** | Adopció del Starter Kit i reducció de fricció (schema, ZIP, guia, RFC, Paquets 00/01) | 2-3 setmanes | 🟠 P1 | 🟡 **Parcial** |
| **F4** | Eines del Starter Kit (okf-tools, plugin o MCP; un a la vegada) | 2-3 mesos | 🟠 P1 | ⏳ Pendent |
| **F5** | Comunitat (Registry, MkDocs) | 6-12 mesos | 🟡 P2 | ⏳ Pendent |
| **F6** | Integració de la prova d'usabilitat (Alícia) | quan hi hagi resultats | 🟠 P1 | ⏳ Pendent |

**Reclassificació v1.8:** F3 cobreix l'adopció i la reducció de fricció del **Starter Kit**; F4 cobreix les eines que s'hi construeixin (una a la vegada). L'**OKF Operational Kit** és el Programa B, un producte MIAE-3 separat, i no forma part de F4: [repositori OKF Operational Kit](https://github.com/jmonta23-okf/okf-operational-kit). La propera fita del Starter Kit és **F2 · Robustesa del validador**; F3/F4 no són prerequisits per començar O1 de l'Operational Kit.

### F0 · Correccions immediates ✅ **Fet**

- [x] Badge del README a V1.3 (`f75dedc`)
- [x] `requirements.txt` amb `pyyaml` (`f75dedc`)
- [x] Docstring dels Cores (`f75dedc`)
- [x] `ROADMAP.md` a `00-documentacio/` (`f75dedc`)
- [x] `[No publicat]` del CHANGELOG eliminades (`924223c`)
- [x] `cataleg_versio` dels exemples eliminat (`924223c`)
- [x] Prosa de `cataleg_versio` al MOC/Handoff (`68ff50c`)
- [x] Cua anòmala de `07-com-compartir.md` (`68ff50c`)
- [x] BibTeX `version = {V1.3}` (`924223c`)

### F1 · Consolidació semàntica ✅ **Fet**

- [x] §3.1 · Identitat dels CAs afegits — **F1.1 (`0ff7d39`)**
- [x] §3.2 · Y052 i format antic/mixt — **F1.2 (`0c13e0a`)**
- [x] §4.1 · Auditoria per catàleg — **F1.3 (`eacc716`)**

### F2 · Robustesa del validador 🔜 **Propera fita**

- [ ] Matriu de tipus per a cada camp de `criteris:` i `instruments_avaluacio`
- [ ] Validar que `codi` d'instrument sigui hashable
- [ ] Validar que `criteris` d'instrument sigui una llista
- [ ] Proves negatives (cap excepció no controlada)

### F2.5 · Correccions de l'auditoria externa ✅ **Fet**

- [x] DOIs actualitzats a V1.3 (`CONTRIBUTING`, `00-index`, article eDigital) (`3184e0d`)
- [x] Recompte de plantilles (6 → 7) (`3184e0d`)
- [x] Recompte de nodes del mini-vault (3 → 5) (`3184e0d`)
- [x] Text de privacitat honest (flags, no prosa) (`3184e0d`)
- [x] Tests de snapshot amb `skip` sense `.git` (`3184e0d`)
- [x] Documentar relació 02/07 i fer portable el mini-vault (`dfd72c2`)
- [x] MOC absent → `Y014` global (`d87437b`)

### F3 · Reducció de fricció 🟡 **Parcial**

- [x] `01-cores/okf-core.schema.json` (validació en viu a VS Code / Obsidian) (`c0fabe6`)
- [x] ZIP preconfigurat del `vault-de-3-nodes` (`867c761`)
- [ ] Guia ràpida per a docents sense Git (`00-documentacio/09-arrencada-rapida.md`)
- [x] Publicar l'RFC-OKF-03 com a document consultable (`00-documentacio/10-rfc-okf-03.md`)
- [x] Ampliar `09-graf-curricular.md` amb una secció d'especificació del model de dades
- [x] **Convertir el Paquet LLM-00 en plantilla oficial** — **Fet** (`04-plantilles/PLANTILLA-PaquetLLM-00.md`, `f879dc4`)
- [x] **Documentar l'aproximació inductiva (Paquet 01)** — **Fet** (`04-plantilles/PLANTILLA-PaquetLLM-01.md`, `f879dc4`)
- [x] **Taula de decisió inductiu/deductiu a `04-inici-rapid.md`** — **Fet** (`c610ad0`)
- [x] **Secció «El docent no és un programador» a `02-filosofia.md`** — **Fet** (`f879dc4`)

### F4 · Producte (triar-ne un) ⏳ **Pendent**

- [ ] `okf-tools` a PyPI (`pip install okf-tools`) — **recomanat**
- [ ] Plugin d'Obsidian per editar YAML visualment
- [ ] Servidor MCP per a clients d'IA
- [ ] Generador de vistes derivades institucionals (CSV per a Esfer@/SAGA)
- [x] Generador de vistes derivades institucionals (Programació Didàctica en HTML/CSS per a Word) — **Fet** (`04-plantilles/PLANTILLA-PaquetLLM-02.md`)

**Nota:** no fer-ne quatre alhora. Triar-ne un, fer-lo bé, i valorar el següent segons l'adopció.

### F5 · Comunitat ⏳ **Pendent**

- [ ] OKF Registry (catàleg de mòduls compartits)
- [ ] Documentació web amb MkDocs
- [ ] Comitè RFC formalitzat
- [ ] Traducció a castellà/anglès

**Nota:** no començar fins que hi hagi almenys 3 docents externs usant el kit.

### F6 · Integració de la prova d'usabilitat (Alícia) ⏳ **Pendent**

**Quan arribin els resultats:**

- [ ] Validar l'AEA de l'Alícia
- [ ] Documentar la prova a `~/.hermes/okf-curs-0056/PROVA-USABILITAT.md`
- [ ] Integrar els resultats al ROADMAP en la propera revisió
- [ ] Crear `HANDOFF-11` amb els resultats

---

## 6 · Criteris d'èxit per a la V1.4 (consolidació)

La V1.4 no es publica fins que es compleixin:

| Indicador | Objectiu | Estat |
|:---|:---|:---:|
| CAs afegits | Referenciables de manera inequívoca | ✅ F1.1 |
| Y052 | Decisió de disseny documentada; sense falsos positius en formats antics | ✅ F1.2 |
| Auditoria multi-catàleg | Cap interferència entre codis repetits | ✅ F1.3 |
| MOC absent | Detectat amb `Y014` | ✅ F2.5.b2 |
| Text de privacitat honest | Reflecteix el que el codi fa realment | ✅ F2.5.a |
| Paquets d'onboarding | 00 (deductiu) i 01 (inductiu) documentats | ✅ F3 |
| Validació de tipus | Completa per als camps nous | ⏳ F2 |
| Excepcions no controlades | 0 en les proves negatives | ⏳ F2 |
| Tests | Tots actius; cap `skip` sense justificació | ⏳ F2 |
| Documentació | README, CHANGELOG, CONTRIBUTING i RFC sincronitzats | ✅ F0/F2.5/F3 |
| Prova d'usabilitat | Resultats integrats (o justificació de per què no) | ⏳ F6 |

---

## 7 · Descartat (i per què)

| Proposta | Motiu del descart |
|:---|:---|
| Afegir més codis Y abans de consolidar | Acumularia deute tècnic |
| Fer totes les propostes de producte alhora | Massa abast per a un sol autor |
| Aplicació web pròpia | No hi ha prou evidència de necessitat |
| Basar-se en els errors factuals dels informes | Portaria a implementar camps i tipus que no existeixen |
| Guardar els informes originals | El full de ruta n'integra les aportacions; els informes es descarten |
| Canviar els 8 camps universals o els 9 tipus universals | Són la base de la interoperabilitat; no es toquen |
| Crear un document separat d'especificació del model | Massa sobreenginyeria; per defecte s'amplia `09-graf-curricular.md`. **Excepció:** si el model creix fins al punt que ho justifiqui, es pot crear un document nou. |
| **D3 · Detecció de DNI/NIE en prosa** | **Falsos positius garantits** en un kit de Sanitat (casos clínics ficticis amb DNI inventat). El risc real es cobreix amb els flags de privacitat i la revisió manual, no amb un regex. |

---

## 8 · Com actualitzar aquest document

1. Quan arribi un informe nou (intern o extern), **llegir-lo amb esperit crític**.
2. **Verificar** les afirmacions contra el codi abans d'incorporar-les.
3. **Integrar** les aportacions vàlides a les seccions corresponents (§3, §4 o §5).
4. **Descartar** les que no siguin verificables o que contradiguin el codi, anotant-ho a §7.
5. **Actualitzar** la data i la versió del document a la capçalera.
6. **No guardar** l'informe original.

---

## 9 · Registre de revisions

| Data | Versió | Canvi |
|:---|:---:|:---|
| 2026-11-05 | 1.0 | Integració dels tres informes post-V1.3 (auditoria tècnica, visió de producte, radiografia estructural) |
| 2026-11-05 | 1.1 | Revisió: §3.3 reformulat com a decisió de disseny; §3.2 baixa a P1; afegida la prova de l'Alícia (F6); afegides l'especificació del model i el Paquet LLM-00 a F3 |
| 2026-11-05 | 1.2 | Enriquit amb detalls del brief de la prova d'usabilitat: vault `okf-curs-0056`, 43 CAs, aproximació híbrida, Paquet LLM-00 com a `05_Paquet_LLM-00.md`, passos concrets per integrar els resultats (F6), i referència a HANDOFF-11 |
| 2026-11-05 | 1.3 | Aplicades les tres esmenes de la valoració: excepció a §7 (especificació del model), cross-referències a §2 (→ F0/F1), i docstring dels Cores a F0 |
| 2026-11-05 | 1.4 | Congelada. Aplicades les dues esmenes finals: `cataleg_versio` mogut de F1 a F0; HANDOFF-11 convertit en tasca explícita a F6. |
| 2026-11-05 | 1.5 | **F0 i F1 completades.** Commits: F0-a `f75dedc`, F0-b `924223c`, F0-c `68ff50c`, F1.1 `0ff7d39`, F1.2 `0c13e0a`, F1.3 `eacc716`. |
| 2026-11-05 | 1.6 | **F2.5 completada.** Commits: F2.5.a `3184e0d`, F2.5.b1 `dfd72c2`, F2.5.b2 `d87437b`. 75 tests. D3 descartat (falsos positius en Sanitat). MOC absent → `Y014`. Text de privacitat honest. |
| 2026-11-05 | 1.7 | **Paquets 00/01 i filosofia.** Commits: `c610ad0` (taula de decisió a `04-inici-rapid.md`), `f879dc4` (secció 9 a `02-filosofia.md` + dos PLANTILLA). Resposta a la crítica «el docent es perdrà en els YAML». F3 parcial (4 tasques fetes). |
| 2026-11-09 | 1.8 | **F2 és la propera fita.** Reclassificades F3 (adopció/fricció del Starter Kit) i F4 (eines del Starter Kit); l'OKF Operational Kit s'identifica com a Programa B independent, fora de F4. Afegit enllaç al repositori. F3/F4 no bloquegen O1 de l'Operational Kit. |
| 2026-11-10 | 1.9 | F3.1 (JSON Schema), F3.2 (ZIP mini-vault) i F3.4 (RFC-OKF-03 publicat) completades. |
| 2026-11-10 | 1.10 | F3.5 (especificació del model de dades a `09-graf-curricular.md`) completada. |

---

**Fi del ROADMAP v1.8.** F0, F1 i F2.5 completades; Paquets 00/01 documentats. **F2 és la propera fita del Starter Kit.** F3/F4 queden delimitades al Starter Kit; l'OKF Operational Kit és un Programa B independent. La propera versió (v1.9) s'actualitzarà quan tanqui F2 o arribin els resultats de l'Alícia.