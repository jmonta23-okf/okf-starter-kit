# Changelog

Tots els canvis notables d'aquest projecte es documenten en aquest fitxer.

El format es basa en [Keep a Changelog](https://keepachangelog.com/ca/1.1.0/)
i aquest projecte segueix [Versionat Semàntic](https://semver.org/lang/ca/).

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
  - `01-casos-us.md` — els tres casos reals (Benet M. a Química, César G. a Sanitat, Anna C. a Pedagogia Terapèutica).
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
- **Privacitat:** ús d'inicials (**Benet M.**, **César G.**, **Anna C.**, **Montse G.**) i supressió de noms de centres educatius.
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

- **V1.0-Esborrany** (25-28/10/2026): 4 fites de desenvolupament amb commits al repo local. Al final del període, el kit era funcional però encara tenia el to "tècnic" original.
- **V1.1** (29/10/2026): humanització, MIAE+VCER, exemple de 11 nodes, privacitat. **Aquesta és la versió que s'ha publicat.**
- **V1.1-publicació** (31/10/2026): publicació oficial a GitHub i Zenodo amb DOI permanent. El DOI `10.5281/zenodo.23823819` correspon a la V1.1.

**Sobre el DOI:** el concept DOI (`10.5281/zenodo.23823818`) sempre apunta a la darrera versió. El DOI de la versió (`10.5281/zenodo.23823819`) correspon a la V1.1 específicament. Quan es faci una V1.2, es generarà un DOI nou automàticament.