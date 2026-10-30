# Changelog

Tots els canvis notables d'aquest projecte es documenten en aquest fitxer.

El format es basa en [Keep a Changelog](https://keepachangelog.com/ca/1.1.0/)
i aquest projecte segueix [Versionat Semàntic](https://semver.org/lang/ca/).

## [Unreleased]



### Pendent
- Documentació completa (`00-documentacio/`)
- Totes les plantilles (`04-plantilles/`)
- Nuclis (`01-cores/`)
- Exemple de crèdit sencer (`02-exemple-complet/`)
- Materials de comunitat (`06-comunitat/`)

## [V1.2] - 2026-10-30

### Modificat
- **Documentació central (`00-documentacio/`):** Humanització del to ("de docent a docent"), integració de la mirada ontològica i biològica, distinció formal entre *currículum oficial* i *programació didàctica viva*, i superació de la tirania de les carpetes.
- **Ètica i qualitat de la IA:** Integració formal dels marcs **MIAE (Nivell 3)** i **VCER** (*Vibe Coding Educatiu Responsable*: 100% offline, privacitat de l'alumnat, accessibilitat per teclat i llicència lliure).
- **Privacitat:** Blindatge de dades personals amb inicials (**Benet M.** i **César G.**) i supressió de noms de centres educatius.
- **Plantilles (`04-plantilles/`):** Actualització de `PLANTILLA-PaquetLLM.md` amb el contracte d'enginyeria VCER i checklist d'aula.

### Afegit / Reestructurat
- **Exemple complet (`02-exemple-complet/`):** Desplegament integral del mòdul MP 1519 en 11 nodes canònics:
  - 5 de 5 AEAs completes (des de la piràmide DIKW fins a l'auditoria clínica d'expedients).
  - Protocol d'avaluació de tres portes i matriu OC (C1-C6).
  - Paquet LLM canònic amb les 7 capes anti-al·lucinació, Taula dels 10 Falsos Amics i regla dels 3 artefactes separats.
  - Guia d'arquitectura Dual-User (SYS_PROMPT oficial, NotebookLM i RGPD).
  - Eina tècnica del validador determinista local en Python/SQLite (`cie10es_validator.py`).
  - Eina tècnica d'automatització amb Google Workspace (Hub-Spoke de 5 fulls i solució a `@ProjectPermissionDenied`).
  - `README.md` de presentació del mòdul.

## [1.0-Esborrany] — 2026-10-25

### Afegit
- Estructura bàsica de carpetes (6 carpetes).
- `LICENSE.md` amb doble llicència (MIT + CC BY-SA 4.0).
- `README.md` (portada del repositori).
- `04-inici-rapid.md` (tutorial de 30 minuts).
- `05-exemples-minims/vault-de-3-nodes/` amb 3 nodes validats (MOC + UD + FitxaAEA).
- `03-eines/validar_yaml.py` v1.0.0 (validador genèric del kit).
- `04-plantilles/PLANTILLA-ConvencioNomenclatura.md` (plantilla de Convenció).
- **Bloc 8 — Comunitat (`06-comunitat/`):** 4 documents humans (README, casos d'ús de Benet M. / César G. / Anna C., guia per compartir, esborrany de l'article per a eDigital).
- **Validador v1.0.2:** exclou `06-comunitat/` de la validació (com `00-documentacio/`).


### Notes
- Aquesta és la primera versió pública del kit. És un esborrany i pot canviar.
- El validador és una versió adaptada del TCAI-OKF, pensada per a un kit genèric.