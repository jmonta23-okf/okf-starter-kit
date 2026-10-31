# `CONTRIBUTING.md` — fitxer complet amb el DOI afegit

**Instruccions:** substitueix **tot** el contingut actual de `CONTRIBUTING.md` per aquest. Els canvis principals:
- **DOI a la capçalera** (just després de la introducció).
- **Secció nova "Com citar el projecte"** (abans de "Llicència de les contribucions").
- **Correcció menor:** `06-comunitat/casos-d-us.md` → `06-comunitat/01-casos-us.md` (el nom real del fitxer).

```markdown
# Com contribuir

Gràcies per l'interès a contribuir al OKF Starter Kit. Aquest document explica com fer-ho.

**DOI:** [10.5281/zenodo.23823819](https://doi.org/10.5281/zenodo.23823819) · **Repositori:** [github.com/jmonta23-okf/okf-starter-kit](https://github.com/jmonta23-okf/okf-starter-kit)

---

## Tipus de contribucions benvingudes

- **Errors i bugs**: obre un *issue* explicant què passa i com reproduir-ho.
- **Millores a la documentació**: obre un *issue* o envia un *pull request*.
- **Plantilles noves**: obre un *issue* explicant quina plantilla proposes i per què.
- **Exemples d'ús**: si has fet servir el kit, explica-ho a `06-comunitat/01-casos-us.md` o obre un *issue*.
- **Traduccions**: al castellà, a l'anglès, o a qualsevol altra llengua.
- **Millores al validador**: si trobes un bug o vols afegir una validació, obre un *issue* primer.

## Com enviar un *pull request*

1. Fes un *fork* del repositori.
2. Crea una branca descriptiva: `git checkout -b millora/nom-descriptiu`.
3. Fes els canvis.
4. Assegura't que el validador passa:
   ```bash
   python3 03-eines/validar_yaml.py --ruta 05-exemples-minims/vault-de-3-nodes
   ```
   Ha de retornar 0 errors.
5. Fes *commit* amb un missatge clar. **Sense accents** (per evitar problemes d'encoding al shell):
   ```bash
   git commit -m "Afegeix plantilla per a Protocol"
   ```
6. Envia el *pull request* explicant què has canviat i per què.

## Convencions

### Nomenclatura de fitxers

- Carpetes: minúscules, amb guions (`00-documentacio`, no `00_Documentacio`).
- Fitxers de documentació: `NN-nom-descriptiu.md` (on `NN` és un número de dues xifres).
- Plantilles: `PLANTILLA-NomDelTipus.md`.
- Scripts: `nom_descriptiu.py` (snake_case).

### Codi Python

- Python 3.9+.
- Segueix [PEP 8](https://peps.python.org/pep-0008/).
- Documenta les funcions amb *docstrings*.
- Si afegeixes una validació nova, documenta-la al `docstring` del mòdul i al `README.md` de `03-eines/`.

### Missatges de commit

- En català.
- Sense accents (per evitar problemes d'encoding).
- En imperatiu: "Afegeix...", "Corregeix...", "Millora...".
- Primera línia curta (< 72 caràcters), després línia en blanc, després detalls si cal.

## Com citar el projecte

Si la teva contribució es publica en un treball acadèmic o una comunicació, pots citar el projecte així:

> Montañà Piqué, J. (2026). *OKF Starter Kit: una proposta de sistema operatiu per al coneixement curricular* (V1.1) [Programari]. Zenodo. https://doi.org/10.5281/zenodo.23823819

Per als detalls complets (APA, BibTeX, text pla), consulta la secció **[Com citar aquest projecte](README.md#com-citar-aquest-projecte)** del README principal.

## Llicència de les contribucions

En enviar un *pull request*, acceptes que la teva contribució es distribueixi sota la mateixa doble llicència del projecte:

- **Codi**: MIT.
- **Contingut**: CC BY-SA 4.0.

## Codi de conducta

Aquest projecte segueix el [Contributor Covenant](https://www.contributor-covenant.org/). Esperem un tracte respectuós i constructiu entre tots els participants.

## Preguntes?

Obre un *issue* o contacta amb l'autor original.
```
