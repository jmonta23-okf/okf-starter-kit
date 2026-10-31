# Plantilles

Aquesta carpeta conté les plantilles de nodes del OKF Starter Kit. Una **plantilla** és un fitxer Markdown amb un frontmatter YAML vàlid i un cos amb seccions a omplir. Serveix per crear nodes consistents sense començar de zero.

**DOI:** [10.5281/zenodo.23823819](https://doi.org/10.5281/zenodo.23823819) · **Repositori:** [github.com/jmonta23-okf/okf-starter-kit](https://github.com/jmonta23-okf/okf-starter-kit)

## Com es fan servir?

1. **Copia** la plantilla al teu vault.
2. **Omple** el frontmatter (els textos entre claudàtors `[...]`).
3. **Omple** el cos seguint les seccions.
4. **Valida** amb el validador del kit (`03-eines/validar_yaml.py`).
5. **Esborra** la taula d'historial de versions de la plantilla quan el node passi a ser real (o mantén-la, com prefereixis).

Totes les plantilles passen el validador tal com són, amb els valors d'exemple.

## Les 6 plantilles

| Plantilla | Tipus | Categoria | Descripció |
|:---|:---|:---|:---|
| **`PLANTILLA-ConvencioNomenclatura.md`** | `ConvencioNomenclatura` | transversal | Regles formals del vault: tipus vàlids, camps obligatoris, format d'ID, ubicació i enllaços |
| **`PLANTILLA-MOC.md`** | `MOC` | transversal | Node arrel: índex navegable del vault o d'una àrea |
| **`PLANTILLA-UnitatDidactica.md`** | `UnitatDidactica` | crèdit | Unitat didàctica completa: continguts, activitats i avaluació |
| **`PLANTILLA-PaquetLLM.md`** | `PaquetLLM` | crèdit | Instruccions autocontingudes perquè un LLM generi materials d'un crèdit |
| **`PLANTILLA-Protocol.md`** | `Protocol` | transversal | Procediment d'aplicació general amb passos, responsables i indicadors |
| **`PLANTILLA-FitxaAEA.md`** | `FitxaAEA` | crèdit | Fitxa d'una activitat d'ensenyament-aprenentatge concreta |

## Notes

- **Els tipus de crèdit** (`UnitatDidactica`, `PaquetLLM`, `FitxaAEA`) requereixen el camp `credit` al frontmatter; els transversals no.
- **Camps opcionals:** cada plantilla afegeix camps específics del seu tipus (per exemple, `durada`, `ambit`, `model_objectiu`). El validador els tolera; no són obligatoris.
- **Els noms dels camps** segueixen l'esquema del validador (`type`, `version`, `data_ultima_actualitzacio`, `authors`), no la terminologia divulgativa.
- Si el teu marc legal usa una terminologia diferent (per exemple, `competencies_especifiques` en lloc de `resultats_aprenentatge`), adapta els camps opcionals: el validador no els imposa.

## Llicència

Les plantilles es distribueixen sota **CC BY-SA 4.0**, com la resta de contingut del kit. El projecte complet té DOI permanent: [10.5281/zenodo.23823819](https://doi.org/10.5281/zenodo.23823819).