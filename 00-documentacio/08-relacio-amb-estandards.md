# Relació amb estàndards existents

> *«No cal inventar un format nou si n'hi ha un que ja funciona. Però cal dir exactament com t'hi relaciones.»*

Aquest document situa l'OKF Starter Kit respecte als estàndards educatius i d'intercanvi de dades que ja existeixen. No pretén ser exhaustiu, però sí honest: si el kit no implementa un estàndard, ho diu; si s'hi inspira, ho explica; i si podria ser-hi compatible en el futur, ho assenyala.

**DOI:** [10.5281/zenodo.23823818](https://doi.org/10.5281/zenodo.23823818) · **Repositori:** [github.com/jmonta23-okf/okf-starter-kit](https://github.com/jmonta23-okf/okf-starter-kit)

---

## 1 · L'especificació base: Open Knowledge Format (Google Cloud)

El juny de 2026, Google Cloud va publicar l'**Open Knowledge Format (OKF)**: un format obert per estructurar coneixement en fitxers Markdown amb frontmatter YAML, pensat perquè els agents d'IA el puguin llegir i compartir. L'especificació és minimalista: exigeix un camp `type` i deixa la resta oberta.

**L'OKF Starter Kit és un perfil d'aquesta especificació**, adaptat a l'educació catalana. Això vol dir:

| Aspecte | OKF de Google | OKF Starter Kit (perfil) |
|:---|:---|:---|
| **Camp obligatori** | `type` | `type` (i 8 camps universals més) |
| **Tipus permesos** | Oberts | 9 universals + 12 de família (15 en total) |
| **Enllaços** | Markdown estàndard | Markdown relatiu amb `.md` |
| **Validació** | No n'inclou | Inclou un validador (`validar_yaml.py`) |
| **Propòsit** | Coneixement empresarial per a agents d'IA | Governança del coneixement curricular docent |

**Compatibilitat:** un fitxer del kit és llegible per una eina genèrica d'OKF (que només comprova el `type`). Els camps addicionals són ignorats per l'eina genèrica i validats pel validador del kit. Això és el que fa que el kit sigui un **perfil**, no un format nou.

---

## 2 · Estàndards educatius: CASE, LRMI, Schema.org

Aquests tres estàndards són els referents internacionals en la descripció i intercanvi de dades educatives. El kit **no els implementa**, però dialoga amb ells conceptualment.

### 2.1 · CASE (Competencies and Academic Standards Exchange)

**Què és:** l'estàndard d'1EdTech per intercanviar informació sobre estàndards d'aprenentatge i competències d'una manera llegible per màquina, generalment mitjançant APIs REST.

**Relació amb el kit:** CASE és un estàndard d'**intercanvi** entre sistemes. El kit és un estàndard de **governança local** del coneixement. Són complementaris: el kit podria exportar el seu catàleg curricular a CASE, però no ho fa (encara).

**Què caldria per ser-hi compatible:** un exportador del Catàleg Curricular (nodes `CatalegCurricular`) a un fitxer CASE (JSON-LD amb el vocabulari d'1EdTech).

### 2.2 · LRMI (Learning Resource Metadata Initiative)

**Què és:** una iniciativa per descriure recursos educatius mitjançant vocabulari de `schema.org`, facilitant-ne la trobada per part de professors i alumnes.

**Relació amb el kit:** LRMI descriu **recursos** (llibres, vídeos, activitats). El kit descriu **estructures curriculars** (unitats, criteris d'avaluació, activitats d'ensenyament-aprenentatge). Són capes diferents: un node `FitxaAEA` del kit podria tenir una descripció LRMI (per fer-lo trobable a la web), però el node en si mateix no és un recurs LRMI.

**Què caldria per ser-hi compatible:** afegir camps LRMI (opcionals) als nodes que descriuen materials, i un exportador a `schema.org`.

### 2.3 · Schema.org

**Què és:** el vocabulari col·laboratiu (Google, Microsoft, Yahoo, Yandex) per estructurar dades a la web, permetent que els cercadors entenguin el contingut.

**Relació amb el kit:** Schema.org és **infraestructura web** (JSON-LD incrustat en pàgines HTML). El kit és **text pla local** (Markdown + YAML). No hi ha incompatibilitat, però tampoc no hi ha cap integració. Si algun dia el kit es publica en una web, podria generar `schema.org` a partir dels nodes.

---

## 3 · Estàndards d'intercanvi de dades educatives: OOAPI

**Què és:** l'estàndard europeu per a l'intercanvi de dades educatives (matrícules, notes, expedients) entre institucions. El fan servir universitats i institucions a països com els Països Baixos.

**Relació amb el kit:** OOAPI és el candidat més clar per connectar el kit amb els sistemes administratius (com Esfer@). La idea seria:

1. El docent té les notes i els comentaris al seu vault (nodes d'avaluació).
2. El kit genera un fitxer en format OOAPI (o un perfil seu).
3. El sistema administratiu (si admet OOAPI) importa el fitxer directament.

**Avui això no és possible perquè Esfer@ no exposa cap API pública ni accepta OOAPI.** Però la via existeix, i el kit pot preparar-s'hi.

---

## 4 · Sistemes administratius: Esfer@ i SAGA

**Què són:** les aplicacions corporatives del Departament d'Educació de la Generalitat per a la gestió acadèmica i administrativa dels centres públics. SAGA va ser substituït per Esfer@.

**Relació amb el kit:** el kit **no pretén substituir-los**. Són eines d'administració (matrícules, expedients, notes oficials); el kit és una eina de governança del coneixement curricular. La relació és de **complementarietat**, no de competència.

**El punt de fricció real:** la introducció de notes i comentaris a Esfer@ és manual, alumne per alumne, matèria per matèria. Això és un cost de temps important per al docent.

**La via pràctica que el kit ofereix:** un **Paquet LLM** específic que llegeixi els nodes d'avaluació del vault (notes, comentaris) i generi un **fitxer d'importació massiva** en el format que Esfer@ accepti (probablement CSV o Excel). Això no és una connexió via API (perquè Esfer@ no en té), però **digitalitza el procés** i elimina la feina manual repetitiva.

**Què caldria per fer-ho realitat:**
1. Documentar el format d'importació que accepta Esfer@ (cal consultar el Departament).
2. Crear un node `Protocol` que descrigui el procediment d'exportació.
3. Crear un `PaquetLLM` que generi el fitxer a partir dels nodes d'avaluació.
4. Provar-ho en un centre real.

---

## 5 · Taula resum

| Estàndard | Propòsit | El kit l'implementa? | Relació |
|:---|:---|:---:|:---|
| **OKF (Google)** | Format obert per a agents d'IA | ✅ **Sí** (com a perfil) | El kit és un perfil de l'OKF de Google |
| **CASE** | Intercanvi de competències | ❌ No | Complementari (exportador pendent) |
| **LRMI** | Descripció de recursos educatius | ❌ No | Complementari (capa diferent) |
| **Schema.org** | Dades estructurades a la web | ❌ No | Complementari (infraestructura web) |
| **OOAPI** | Intercanvi de dades educatives | ❌ No | Via futura per connectar amb Esfer@ |
| **Esfer@/SAGA** | Gestió administrativa | ❌ No | Complementari (no substitutiu) |

---

## 6 · La via pràctica: Paquets LLM com a pont

Mentre no hi hagi una API o un estàndard adoptat, la manera més pràctica de connectar el kit amb les eines oficials és **generar fitxers d'importació** a partir dels nodes del vault, mitjançant Paquets LLM.

**Exemple de flux (per a notes d'avaluació a Esfer@):**

```
Nodes del vault (notes + comentaris)
    ↓
Paquet LLM específic ("Generador de notes per a Esfer@")
    ↓
Fitxer d'importació (CSV o Excel amb el format que Esfer@ accepta)
    ↓
Pujada manual a Esfer@ (una sola operació, no alumne per alumne)
```

**Avantatges:**
- **Estalvi de temps:** una operació massiva en lloc de N operacions individuals.
- **Traçabilitat:** el vault és la font de veritat; el fitxer generat n'és una vista derivada.
- **Revisió:** el docent pot revisar el fitxer abans de pujar-lo.
- **Ètica:** cap dada d'alumnat s'envia a un model d'IA (el Paquet LLM treballa amb les notes ja calculades, no amb el procés d'avaluació).

**Què falta per fer-ho realitat:**
- Documentar el format exacte que accepta Esfer@ (cal consultar el Departament).
- Crear el Paquet LLM i el Protocol.
- Provar-ho en un centre.

---

## 7 · Què falta (i com col·laborar-hi)

Aquest document és una **declaració de posicionament**, no una implementació completa. El que falta és:

1. **Exportador a CASE** (per al Catàleg Curricular).
2. **Exportador a LRMI** (per als materials).
3. **Exportador a OOAPI** (per a les notes, si algun dia Esfer@ l'adopta).
4. **Paquet LLM per a Esfer@** (la via pràctica immediata).
5. **Documentació del format d'importació d'Esfer@** (cal col·laboració amb el Departament).

Si treballes en un centre i vols col·laborar en algun d'aquests punts, obre un *issue* al [repositori](https://github.com/jmonta23-okf/okf-starter-kit/issues) o escriu-me. **La interoperabilitat no es fa sol: es fa entre tots.**

---

## 8 · Referències

### 8.1 · Referències formals (APA)

- 1EdTech Consortium. (2025). *Competencies and Academic Standards Exchange (CASE) Service REST/JSON Binding Version 1.1*. 1EdTech Consortium.
- Barker, P., & Campbell, L. M. (2015). LRMI, Learning Resource Metadata on the Web. In *Proceedings of the 24th International Conference on World Wide Web Companion* (p. 687). Association for Computing Machinery. https://doi.org/10.1145/2740908.2741745
- Guha, R., Brickley, D., & Macbeth, S. (2016). Schema.org: Evolution of structured data on the web. *Communications of the ACM, 59*(2), 44–51. https://doi.org/10.1145/2844544
- Google Cloud. (2026, juny). *Open Knowledge Format (OKF) Specification*.

### 8.2 · Referències formals (BibTeX)

```bibtex
@techreport{1edtech2025case,
  author      = {{1EdTech Consortium}},
  title       = {Competencies and Academic Standards Exchange (CASE) Service REST/JSON Binding Version 1.1},
  year        = {2025},
  month       = {January},
  institution = {1EdTech Consortium},
  url         = {http://www.imsglobal.org/activity/case/}
}

@inproceedings{barker2015lrmi,
  author    = {Barker, Phil and Campbell, Lorna M.},
  title     = {LRMI, Learning Resource Metadata on the Web},
  booktitle = {Proceedings of the 24th International Conference on World Wide Web Companion},
  year      = {2015},
  pages     = {687},
  publisher = {Association for Computing Machinery},
  doi       = {10.1145/2740908.2741745}
}

@article{guha2016schema,
  author  = {Guha, Ramanathan and Brickley, Dan and Macbeth, Steve},
  title   = {Schema.org: Evolution of structured data on the web},
  journal = {Communications of the ACM},
  year    = {2016},
  volume  = {59},
  number  = {2},
  pages   = {44--51},
  doi     = {10.1145/2844544}
}

@techreport{google2026okf,
  author      = {{Google Cloud}},
  title       = {Open Knowledge Format (OKF) Specification},
  year        = {2026},
  month       = {June},
  institution = {Google Cloud}
}
```

### 8.3 · Referències internes

- [Què és OKF?](./01-que-es-okf.md) — la doble lectura de les sigles.
- [Filosofia](./02-filosofia.md) — l'origen (Google OKF, juny 2026) i la declaració d'ús d'IA.
- [Arquitectura](./03-arquitectura.md) — el model de capes i la convenció YAML.
- [Compartir](./07-com-compartir.md) — com publicar el vault.

---

## 9 · Relacions (Graf)

- Complementa: [Què és OKF?](./01-que-es-okf.md) — la doble lectura (Open + Organized).
- Complementa: [Filosofia](./02-filosofia.md) — l'origen de Google i el perfil.
- Complementa: [Arquitectura](./03-arquitectura.md) — la implementació tècnica del perfil.
- Referenciat per: [README](../README.md) — la secció "D'on surt aquesta idea?".

---

## 10 · Versionatge

| Versió | Data | Canvis |
|:------:|:----:|:-------|
| V1.0-Esborrany | 2026-11-01 | Creació inicial. Posicionament respecte a OKF (Google), CASE, LRMI, Schema.org, OOAPI, Esfer@/SAGA. Referències formals (APA + BibTeX). |

---

*Document de posicionament de l'OKF Starter Kit respecte als estàndards existents. Honestedat sobre què s'implementa i què no. Invitació a col·laborar en la interoperabilitat.*
```
