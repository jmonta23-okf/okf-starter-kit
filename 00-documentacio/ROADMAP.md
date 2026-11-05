# Full de ruta — OKF Starter Kit

> Document viu. S'actualitza quan arriba un informe nou (intern o extern).
> Els informes originals no es guarden: les seves aportacions s'integren aquí o es descarten.
> **Última revisió:** 2026-11-05 · **Versió del document:** 1.5 (F0 i F1 completades)

---

## 1 · Principis

1. **Consolidar abans d'ampliar.** No afegir codis Y ni camps fins que els existents siguin semànticament consistents.
2. **Reduir fricció.** Cada decisió es valora per si acosta el kit a un docent sense coneixements de terminal.
3. **No sobreenginyeria.** Un sol document de planificació, no un arxiu d'informes. Una eina, no quatre.
4. **Verificar abans de corregir.** Els problemes detectats en informes s'han de convertir en proves reproduïbles abans de tocar codi.

---

## 2 · Estat actual (2026-11-05, post-F0/F1)

| Component | Estat |
|:---|:---|
| Validador | v1.3.0, 38 codis, **73 passed + 1 skipped** |
| Criteris (`criteris:`) | Format nou (dicts) + compatibilitat amb strings |
| Instruments (`instruments_avaluacio`) | Format nou (dicts) + compatibilitat amb strings |
| `--audit` | Mètriques noves + Y045/Y046/Y052, **per catàleg** |
| CAs afegits | Camp `id` estable, referenciables des de `criteris_avaluacio` |
| Documentació | 7 documents actualitzats (14h-a, 14h-b) + ROADMAP + CHANGELOG |
| Release | Tag `V1.3`, DOI `10.5281/zenodo.23964880` |
| CI | Verd |

**Prova d'usabilitat en curs:** docent extern (Alícia, mòdul **0056** — *Atenció sanitària especial en situacions d'emergència*, CFGM en Emergències Sanitàries – TES).  
- **Vault:** `~/.hermes/okf-curs-0056/` — 6 fitxers (`00_MOC.md`, `01_Cataleg_Curricular.md`, `02_Protocol_Avaluacio.md`, `03_Convencio.md`, `04_Handoff.md`, `05_Paquet_LLM-00.md`).  
- **Catàleg:** 43 CAs, 6 RAs, 43 àncores.  
- **Estat:** validat amb 0 errors; auditoria: 43 CAs al decret, 43 orfes (esperat, perquè encara no hi ha fitxes).  
- **Aproximació híbrida:** l'Alícia genera l'AEA amb el seu model d'IA (Paquet LLM-00), nosaltres la validem amb el validador i li tornem el resultat. No se li exigeix instal·lar Python.  
- **Resultats pendents d'integrar.** És la informació més valuosa que tindrem: on es perd un docent real.

**Problemes resolts a F0:**
- ~~El badge del README encara diu V1.2.~~ → **Resolt** (F0-a, `f75dedc`).
- ~~No hi ha `requirements.txt` ni `pyproject.toml`.~~ → **`requirements.txt` creat** (F0-a); `pyproject.toml` queda per a F4.
- ~~`cataleg_versio` deprecated però encara present als exemples.~~ → **Eliminat** (F0-b, `924223c`).

---

## 3 · Prioritats P0 (consolidació semàntica) ✅ **Fet a F1**

### 3.1 · Identitat dels criteris afegits (P0) ✅ **Fet a F1.1**

**Implementat al commit `0ff7d39`.** Nou camp `id` als CAs amb `afegit: true`. Format: `{catalog_id}-RA{N}-ADD-{NN}` (o `{filename_stem}-RA{N}-ADD-{NN}` si el catàleg no té `id`). Els CAs afegits amb `id` poden ser referenciats des de `criteris_avaluacio`, i Y045 no es dispara per a ells. CAs afegits sense `id` → fallback a `guia` (compatibilitat).

**Criteri de tancament:** un CA afegit referenciat per `id` no dona Y045 ni "inexistent". ✅ Complert.

### 3.2 · Y052 i el format antic (P0 — decisió de disseny, no bug) ✅ **Fet a F1.2**

**Implementat al commit `0c13e0a`.** Y052 no s'aplica si algun element de `instruments_avaluacio` no és un `dict` (format antic o mixt). Test de regressió inclòs (`test_y052_es_dispara_en_format_nou`).

**Criteri de tancament:** una fitxa amb instruments en format antic no genera Y052. ✅ Complert.

**Pendent per a v1.4/v1.5:** afegir un warning textual quan es detecti format mixt (alguns dicts + alguns strings), perquè l'usuari sàpiga que té un estat estrany.

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
| **F2** | Robustesa del validador (tipus i proves) | 1-2 setmanes | 🔴 P0 | ⏳ Pendent |
| **F3** | Reducció de fricció (schema, ZIP, guia, especificació, Paquet LLM-00) | 2-3 setmanes | 🟠 P1 | ⏳ Pendent |
| **F4** | Producte (okf-tools o plugin, un a la vegada) | 2-3 mesos | 🟠 P1 | ⏳ Pendent |
| **F5** | Comunitat (Registry, MkDocs) | 6-12 mesos | 🟡 P2 | ⏳ Pendent |
| **F6** | Integració de la prova d'usabilitat (Alícia) | quan hi hagi resultats | 🟠 P1 | ⏳ Pendent |

### F0 · Correccions immediates ✅ **Fet**

- [x] Actualitzar el badge del README a V1.3 (`f75dedc`)
- [x] Afegir `requirements.txt` amb `pyyaml` (`f75dedc`)
- [x] Corregir la docstring interna dels Cores a `validar_yaml.py` (`V1.1.1/V1.0.1` → `V1.1.0/V1.1.2`) (`f75dedc`)
- [x] Verificar `com-compartir.md` (no és duplicació, són complementaris) (`f75dedc`)
- [x] Fusionar o eliminar les entrades `[No publicat]` del CHANGELOG (`924223c`)
- [x] Eliminar `cataleg_versio` dels exemples (`924223c`)
- [x] Netejar la prosa de `cataleg_versio` al MOC/Handoff (`68ff50c`)
- [x] Netejar la cua anòmala de `07-com-compartir.md` (`68ff50c`)
- [x] Actualitzar el BibTeX del README a V1.3 (`924223c`)

### F1 · Consolidació semàntica ✅ **Fet**

- [x] Resoldre §3.1 (identitat dels CAs afegits) — **F1.1 (`0ff7d39`)**
- [x] Resoldre §3.2 (Y052 i format antic, com a decisió de disseny) — **F1.2 (`0c13e0a`)**
- [x] Resoldre §4.1 (auditoria per catàleg) — **F1.3 (`eacc716`)**
- [x] Afegir fixtures que reprodueixin cada problema abans de corregir-lo

### F2 · Robustesa del validador ⏳ **Pendent**

- [ ] Matriu de tipus per a cada camp de `criteris:` i `instruments_avaluacio`
- [ ] Validar que `codi` d'instrument sigui hashable
- [ ] Validar que `criteris` d'instrument sigui una llista
- [ ] Proves negatives (cap excepció no controlada)

### F3 · Reducció de fricció ⏳ **Pendent**

- [ ] `01-cores/okf-core.schema.json` (validació en viu a VS Code / Obsidian)
- [ ] ZIP preconfigurat del `vault-de-3-nodes`
- [ ] Guia ràpida per a docents sense Git (`00-documentacio/09-arrencada-rapida.md`)
- [ ] Publicar l'RFC-OKF-03 com a document consultable
- [ ] Ampliar `09-graf-curricular.md` amb una secció d'especificació del model de dades (camps, tipus, invariants, compatibilitat). **No crear un document nou** tret que el model creixi fins al punt que ho justifiqui.
- [ ] Convertir el Paquet LLM-00 (actualment `05_Paquet_LLM-00.md` al vault de l'Alícia) en plantilla oficial (`04-plantilles/PLANTILLA-PaquetLLM-00.md`) i documentar-lo com a via recomanada per crear fitxes AEA.
- [ ] Documentar l'aproximació híbrida (docent genera amb IA, nosaltres validem) com a via d'entrada per a docents sense Python.

### F4 · Producte (triar-ne un) ⏳ **Pendent**

- [ ] `okf-tools` a PyPI (`pip install okf-tools`) — **recomanat**
- [ ] Plugin d'Obsidian per editar YAML visualment
- [ ] Servidor MCP per a clients d'IA
- [ ] Generador de vistes derivades institucionals (CSV per a Esfer@/SAGA)

**Nota:** no fer-ne quatre alhora. Triar-ne un, fer-lo bé, i valorar el següent segons l'adopció.

### F5 · Comunitat ⏳ **Pendent**

- [ ] OKF Registry (catàleg de mòduls compartits)
- [ ] Documentació web amb MkDocs
- [ ] Comitè RFC formalitzat
- [ ] Traducció a castellà/anglès

**Nota:** no començar fins que hi hagi almenys 3 docents externs usant el kit.

### F6 · Integració de la prova d'usabilitat (Alícia) ⏳ **Pendent**

**Quan arribin els resultats:**

- [ ] Validar l'AEA de l'Alícia:
  - Desar-la al vault: `~/.hermes/okf-curs-0056/06_Fitxa_AEA_1.md`.
  - Executar `validar_yaml.py --ruta .` i `--audit` sobre el vault.
  - Reportar: errors, codis Y disparats, si l'auditoria ha passat de 43 orfes a menys orfes.
- [ ] Documentar la prova a `~/.hermes/okf-curs-0056/PROVA-USABILITAT.md`:
  - Temps per fase (descàrrega, comprensió, generació, revisió, validació).
  - Errors comesos (del model o de l'Alícia).
  - Punts de fricció (on ha necessitat ajuda).
  - Feedback qualitatiu (què li ha agradat, què canviaria, què li ha sobrat, què li ha faltat).
- [ ] Integrar els resultats al ROADMAP (v1.6):
  - Afegir les troballes a §3 (si són problemes del model) o a §5 F3 (si són problemes de fricció).
  - Actualitzar §9 (registre de revisions).
- [ ] Crear `HANDOFF-11` amb els resultats de la prova i les seves conclusions.

**Nota:** no modificar el kit (`~/.hermes/okf-starter-kit/`) fins que tinguem els resultats. Les correccions al kit es faran a la v1.4.

---

## 6 · Criteris d'èxit per a la V1.4 (consolidació)

La V1.4 no es publica fins que es compleixin:

| Indicador | Objectiu | Estat |
|:---|:---|:---:|
| CAs afegits | Referenciables de manera inequívoca | ✅ F1.1 |
| Y052 | Decisió de disseny documentada; sense falsos positius en formats antics | ✅ F1.2 |
| Auditoria multi-catàleg | Cap interferència entre codis repetits | ✅ F1.3 |
| Validació de tipus | Completa per als camps nous | ⏳ F2 |
| Excepcions no controlades | 0 en les proves negatives | ⏳ F2 |
| Tests | Tots actius; cap `skip` sense justificació | ⏳ F2 |
| Documentació | README, CHANGELOG, CONTRIBUTING i RFC sincronitzats | ✅ F0 |
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
| 2026-11-05 | 1.4 | Congelada. Aplicades les dues esmenes finals: `cataleg_versio` mogut de F1 a F0 (és neteja, no consolidació); HANDOFF-11 convertit en tasca explícita a F6. |
| 2026-11-05 | 1.5 | **F0 i F1 completades.** Commits: F0-a `f75dedc`, F0-b `924223c`, F0-c `68ff50c`, F1.1 `0ff7d39`, F1.2 `0c13e0a`, F1.3 `eacc716`. Actualitzats §2 (problemes resolts, 73 tests), §3.1/§3.2/§4.1 (marcats com a fets), §5 (F0/F1 ✅), §6 (taula d'estat). La propera actualització serà v1.6, quan arribin els resultats de la prova d'usabilitat o comenci F2. |

---

**Fi del ROADMAP v1.5. F0 i F1 completades. La propera versió (v1.6) es farà quan arribin els resultats de l'Alícia o quan comenci F2.**