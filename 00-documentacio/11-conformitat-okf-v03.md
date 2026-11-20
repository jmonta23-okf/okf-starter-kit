---
id: "OKF-DOC-11"
type: Guia
title: "El teu vault parla OKF: conformitat v0.3 i governança del coneixement docent"
version: "V1.0"
data_ultima_actualitzacio: "2026-11-20"
authors:
  - "Josep Montañà Piqué"
llicencia: "CC BY-SA 4.0"
tags:
  - okf/doc
  - okf/conformitat
  - okf/governanca
estat: esborrany
visibilitat: publica
dades_personals: false
anonimitzat: true
okf_version: "0.3"
generated:
  by: "anthropic/claude-opus-4.5"
  at: "2026-11-20T09:15:00Z"
# verified:
#   - by: "human:Josep Montañà"
#     at: "2026-11-19T16:15:00Z"
# Nota de frescor (verified[].at >= generated.at): en actualitzar generated.at a
# 2026-11-20, el segell humà del 2026-11-19 caduca. En Josep ha de re-segellar:
# afegir una entrada verified amb `by: human:` i `at >= 2026-11-20` i tornar
# `estat` a `vigent`.
sources:
  - resource: "/README.md"
    title: "README del kit: què és i per on començar"
  - resource: "09-graf-curricular.md"
    title: "Graf curricular: especificació tècnica del kit"
  - resource: "08-relacio-amb-estandards.md"
    title: "Relació amb estàndards (posicionament honest)"
  - resource: "ROADMAP.md"
    title: "Full de ruta del projecte"
  - resource: "/CHANGELOG.md"
    title: "Historial de canvis del kit"
  - resource: "/03-eines/validar_yaml.py"
    title: "Validador: font de veritat dels codis Y"
---

# El teu vault parla OKF

> **Què vol dir ser conforme a l'estàndard (i per què t'importa).**
> Guia divulgativa · 10 minuts de lectura · No cal terminal ni saber programar.

**DOI:** 10.5281/zenodo.23823818 · **Repositori:** github.com/jmonta23-okf/okf-starter-kit

Aquesta guia és el pont entre el README (què és el kit) i el document `09-graf-curricular.md`
(l'especificació tècnica). És per a docents que no volen ser programadors, per a coordinacions
digitals i per a direccions que han de decidir si aquesta manera de treballar és seriosa.
Explica, en llenguatge planer, la capa de governança que el kit ha incorporat seguint
l'especificació OKF v0.3 de Google Cloud: el segell de revisió humana, el cicle de vida dels
nodes, la privacitat verificable i què canviarà a la v1.4.

---

## 1 · Ser conforme no és inventar un format

**OKF (Open Knowledge Format)** és una especificació oberta publicada per Google Cloud el
juny de 2026 per estructurar coneixement en fitxers de text pla: Markdown amb una capçalera
de metadades **YAML** (un bloc de camps clau-valor entre dues línies `---`). La seva regla
mínima és un camp `type`; la resta queda oberta perquè cada comunitat hi afegeixi el que
necessita.

L'OKF Starter Kit **no és un format nou: és un perfil** d'aquesta especificació. Hi ha tres
capes, i convé no confondre-les:

1. **Especificació base (Google OKF v0.3):** Markdown + YAML, camp `type`, fitxers `index.md`
   i camps opcionals de governança.
2. **Perfil Starter Kit:** hi afegeix els **8 camps universals** (`id`, `type`, `title`,
   `version`, `data_ultima_actualitzacio`, `authors`, `llicencia`, `tags`), els **9 tipus
   universals** de node i els enums de `visibilitat` i `estat`.
3. **Perfils curriculars** (TCAI, DAS, ESO…): hi afegeixen els tipus de família (`FitxaAEA`,
   `CatalegCurricular`…) i les regles de coherència pròpies de cada marc legal.

La promesa pràctica: **una eina genèrica d'OKF pot llegir el teu vault.** Els camps que el
kit afegeix són ignorats per l'eina genèrica i validats pel teu validador. Això és el que
vol dir «perfil»: el teu coneixement no queda captiu de cap eina.

> **Honestedat:** el kit *dialoga* amb CASE, LRMI i Schema.org, però **no els implementa**
> (els exportadors són feina pendent; vegeu `08-relacio-amb-estandards.md`). I el nom
> «OKF Starter Kit» també el fan servir projectes corporatius aliens: aquest és el
> **perfil educatiu català**, governat per docents.

## 2 · Les quatre versions (i un malentès freqüent)

| Element | Què versiona | Font de veritat |
|:---|:---|:---|
| **Kit** (Starter Kit) | El conjunt publicat a Zenodo (documents, eines, plantilles, exemples). | [README](/README.md) |
| **Model de dades** (perfil) | Camps i tipus universals. Canvia poc. | `01-cores/` |
| **Validador** (`validar_yaml.py`) | L'eina. Evoluciona independentment del kit. | [CHANGELOG](/CHANGELOG.md) |
| **Cores** | Les regles de cada família (LOE/LOGSE, llengua). | `01-cores/` |
| **Especificació Google OKF** | El format base extern. No el governa el kit. | v0.3 (especificació externa) |

Els números de versió vigents no es reprodueixen aquí: el [README](/README.md), els fitxers
`01-cores/` i el [CHANGELOG](/CHANGELOG.md) en són la font única de veritat viva.

**El malentès:** l'**RFC-OKF-03** és un document *intern* del kit (el graf curricular de dues
capes, implementat a la V1.3). **No té cap relació amb l'OKF v0.3 de Google.** Coincideixen
en el número, no en el significat: és com confondre el número de la teva carpeta de curs amb
el número de la llei.

**Per citar:** el *concept DOI* (`10.5281/zenodo.23823818`) apunta sempre a l'última versió
i és el recomanat per a cites generals. El DOI de versió (`…23964880` per a la V1.3) és per
a cites que han de ser reproduïbles en una versió concreta.

## 3 · `index.md`: la fitxa de presentació del teu vault

Cada vault (i l'arrel del repositori) té un `index.md` autodescriptiu: una portada que una
IA llegeix **abans que res** per saber si aquí hi ha el que busca.

```yaml
---
okf_version: "0.3"
title: "Vault curricular · MP 1519"
description: "Catàleg, activitats i protocol d'avaluació del mòdul de Sistemes d'informació i classificació sanitaris (CFGS SAD)."
license: "CC BY-SA 4.0"
---
```

La `description` d'una frase clara no és cosmètica: és el que permet el *routing* d'agents
(que un assistent decideixi quin vault consultar). Els `index.md` **no són nodes**: no els
cal `id` ni `authors`, i el validador els ignora.

Dues convencions més, sense misteri:

- **`.okfignore`** és una convenció comunitària del kit perquè les eines externes saltin
  carpetes internes (`03-eines/`, `04-plantilles/`, `tests/`…). **No és una regla normativa
  de l'especificació.**
- L'especificació exclou per defecte els fitxers ocults (`.*`) i els `.md` **sense `type:`**
  (README, CHANGELOG, manuals). No són nodes i no han de complir cap frontmatter.

## 4 · El segell de revisió humana

Qui ve del laboratori sap que el que no està registrat, validat i traçat, no existeix.
El kit aplica aquest rigor al coneixement docent amb dos camps:

- **`generated`** — qui ha produït l'esborrany i quan: `{by, at}`.
- **`verified`** — qui l'ha revisat i quan: una llista d'entrades `{by, at}`.

Els actors porten prefix: `human:<id>`, `process:<id>`, `team:<id>` o
`<producer>/<version>`. **Només un actor amb prefix `human:` atorga l'estat `human-reviewed`.**
La resta són revisions automàtiques o de procés (un `team:` no equival a una revisió
humana individual). És la traducció formal del marc **MIAE** (Model d'Integració d'IA
en Educació, de Juan José de Haro): la IA proposa, el docent disposa.

Dues regles que el validador exigeix de debò:

1. **Cada entrada de `verified` ha de dur `by` i `at`.** Una entrada incompleta es rebutja
   amb **Y056** (🟠 Alta).
2. **Frescor:** `verified[].at` ha de ser posterior o igual a `generated.at`. Si un agent
   edita el node *després* de la verificació, **el segell humà caduca** fins a una nova
   confirmació. Un segell sobre un text que ja no existeix no és un segell.

```yaml
generated:
  by: "anthropic/claude-opus-4.5"
  at: "2026-11-19T10:00:00Z"
verified:
  - by: "human:Josep Montañà"
    at: "2026-11-19T12:00:00Z"   # posterior a generated.at → segell vàlid
```

> **Aquesta guia practica el que predica.** Neix com a esborrany generat per un model
> (`generated.by` sense prefix `human:`) i **no porta cap segell de revisió humana** fins
> que l'autor la revisi. Quan la revisi, s'hi afegirà l'entrada `verified` i l'`estat`
> passarà a `vigent`. Si llegeixes això amb `estat: esborrany`, el protocol està funcionant.

## 5 · El cicle de vida d'un node, en llenguatge planer

El kit manté els seus camps propis per compatibilitat, i els mapeja amb l'estàndard:

| Camp del kit | Equivalent OKF v0.3 | Notes |
|:---|:---|:---|
| `estat: vigent` | `status: stable` | Node en ús. |
| `estat: esborrany` | `status: draft` | Pendent de revisió. |
| `estat: obsolet` / `arxivat` | `status: deprecated` | Substituït o retirat. |
| `authors` (llista) | `generated.by` (actor) | El kit admet múltiples autors. |
| `data_ultima_actualitzacio` | `generated.at` | El kit manté `YYYY-MM-DD`; v0.3 exigeix timestamp RFC 3339. |

I tres mecanismes de temps i relleu:

- **`stale_after`** — data límit *recomanada* per revisar la vigència del contingut.
- **Finestra d'ús pedagògic** — a nivell de concepte es declara amb l'extensió
  **`x-okfedu-usage-window: {from, to}`** (per exemple, un trimestre). És una finestra
  d'ús recomanat, no una caducitat forçada. El camp `usage_window` a nivell d'arrel de
  node és un camp **diferit** de v0.3 i es preserva sense validar; només
  `sources[].usage_window` es manté per compatibilitat v0.2.
- **`superseded_by`** — la **cadena de relleu**: camí relatiu al node successor. Si comença
  per `/`, es resol des de l'arrel del vault. Declarar-lo exigeix marcar el node com a
  `status: deprecated` o `estat: obsolet`. (El format llista, per a múltiples successors,
  és una extensió del perfil educatiu.)

Què t'avisa el validador, en planer:

| Codi | Què ha passat | Què has de fer |
|:---:|:---|:---|
| **Y054** 🟡 | Una data de v0.3 no és un timestamp RFC 3339 complet ni una data vàlida `YYYY-MM-DD` (`generated.at`, `verified[].at`, `stale_after`, `sources[].last_modified`, i `sources[].usage_window.from/to` per compatibilitat v0.2). | Escriu-la com `2026-11-19T12:00:00Z`, `2026-11-19T12:00:00+01:00` o la data sola `2026-11-19`. No valen el `date-time` sense zona horària (`2026-11-19T12:00:00`) ni una data irreal (`2026-02-30`). La data del kit (`data_ultima_actualitzacio`) segueix sent `YYYY-MM-DD`. |
| **Y055** 🟠 | Un `superseded_by` apunta a un fitxer que no existeix. | Corregir el camí relatiu. |
| **Y056** 🟠 | Una entrada de `verified` no té `by` o `at`. | Completar actor i timestamp. |
| **Y057** 🟡 | Hi ha `superseded_by` però el node no es declara obsolet/deprecated. | Declarar el relleu explícitament. |

Finalment, l'espai **`x-*`**: qualsevol clau d'extensió en kebab-case (`x-el-meu-camp`) és
teva. Les claus desconegudes que no comencin per `x-` es **preserven**: el validador mai
les elimina ni les rebutja. El teu coneixement no es perd per no ser «estàndard».

## 6 · Privacitat honesta: què comprova el kit i què no

El kit declara la sensibilitat de cada node amb tres flags:

- `dades_personals: true/false`
- `anonimitzat: true/false`
- `visibilitat: publica | interna | restringida | personal | externa`

El validador comprova la **coherència** d'aquests flags: un node amb dades personals (o no
anonimitzat) i `visibilitat: publica` dispara **Y022**. Això és verificable per màquina.

**Què NO fa:** el validador **no llegeix la prosa per caçar noms o DNI**. La detecció per
expressions regulars es va descartar deliberadament: un kit de Sanitat genera casos clínics
ficticis amb DNI inventats, i un regex produiria falsos positius constants per zero valor.
La detecció real de dades personals en el text és **revisió manual del docent**, i és
indelegable.

La regla sagrada no canvia: **cap dada personal d'alumnat, ni al graf ni als prompts.**
Les adaptacions (DUA — Disseny Universal per a l'Aprenentatge — i Plans Individuals)
s'articulen com a bancs d'estratègies abstractes i patrons tipificats. El cas de l'Ariadna C.
(Pedagogia Terapèutica) ho demostra: 63 fitxers alineats amb el core català i `visibilitat:
restringida` per a les dades sensibles, sense noms ni historials.

## 7 · Auditoria de cobertura sense mites

El graf de dues capes connecta el **catàleg** (el decret: RAs — Resultats d'Aprenentatge —
i CAs — Criteris d'Avaluació) amb les **fitxes AEA** (l'aula: Activitats d'Ensenyament i
Aprenentatge). L'ordre `--audit` creua cada catàleg amb les seves fitxes:

```bash
python3 03-eines/validar_yaml.py --ruta 07-exemple-mp1519 --audit
```

Distingeix dues coses que sovint es barregen:

- **Mètriques de cobertura (bloquegen):** *CAs orfes* (oficials que cap activitat avalua) i
  *CAs inexistents* (declarats a una fitxa però absents del catàleg) → veredicte
  `INCOMPLET`, codi de sortida 1.
- **Observacions de coherència (no bloquegen):** **Y045** (un CA *afegit pel docent* que cap
  fitxa referencia), **Y046** (un CA oficial cobert *només* per activitats de síntesi),
  **Y052** (un criteri de la fitxa que cap instrument d'avaluació mesura). Són 🟡 Mitjana:
  cal corregir-les, però no afecten el veredicte.

L'exemple real del kit (`07-exemple-mp1519`, 52 CAs del decret) dona:

```text
Total CAs al decret: 52 · CAs coberts: 52 · CAs orfes: 0 · CAs inexistents: 0
Verdicte: COBERT
```

Codis de sortida: **0** tot cobert · **1** algun catàleg incomplet · **2** cap catàleg per
auditar. I la Regla d'Or de sempre: *«0 errors» confirma forma i enllaç; el rigor pedagògic
del contingut continua sent responsabilitat del docent.*

## 8 · Prepara't per a la v1.4

La v1.4 **eliminarà els formats antics** de `criteris:` i `instruments_avaluacio`. Avui
encara s'accepten amb warning. Migració en cinc punts:

1. **`criteris:`** al catàleg: diccionari per RA (`RA1`, `RA2`…) amb una llista de
   diccionaris (`codi`, `guia`, `descripcio`, `contextualitzat`, `afegit`, `origen`).
2. **CAs afegits:** `codi: null` + `afegit: true` + **`guia` obligatòria** (la seva absència
   és Y043, 🔴 Crític) + `id` estable amb patró `{catalog_id}-RA{N}-ADD-{NN}` (perquè les
   fitxes el puguin referenciar) + `origen`.
3. **`instruments_avaluacio:`** a les fitxes: llista de diccionaris (`codi`, `descripcio`,
   `criteris`).
4. **Fora `cataleg_versio`:** s'ignora silenciosament; la versió del catàleg viu al camp
   universal `version`. `--strict-versio` és un no-op.
5. **Xarxa de seguretat en viu:** el JSON Schema `01-cores/okf-core.schema.json` permet
   validació mentre escrius a VS Code (extensió YAML de Red Hat, `yaml.schemas`) i Obsidian.
   És una ajuda d'editor: no substitueix el validador.

```yaml
# ABANS (antic, s'eliminarà a la v1.4)     # DESPRÉS (format V1.3)
criteris:                                  criteris:
  RA1: ["1.1", "1.2"]                        RA1:
                                               - codi: "1.1"
                                                 guia: "1a"
                                                 descripcio: "Text literal del decret."
                                                 contextualitzat: false
                                                 afegit: false
```

## 9 · Starter Kit i Operational Kit: qui fa què

Des del novembre de 2026, l'ecosistema separa responsabilitats: **OKF Starter Kit =
infraestructura** (l'estàndard, el validador, els cores i els exemples) i **OKF Operational
Kit = producte** (el projecte germà que construeix la capa d'abstracció per al docent: l'agent
que tradueix el YAML a llenguatge planer).

La separació neix d'una prova d'usabilitat real: una docent va generar una Fitxa AEA completa i
vàlida amb el Paquet LLM en unes dues hores. Èxit, sí — i una lliçó clara: **el YAML és dur de
llegir per a humans no tècnics**. El kit no pretén convertir els docents en programadors;
pretén que entenguin l'estructura del seu coneixement i sàpiguen guiar una IA. Els detalls de
l'estat actual (paquets LLM, mini-vault en ZIP, barreres d'entrada) viuen al
[README](/README.md) i al [ROADMAP](ROADMAP.md), que són la font única viva.

## 10 · Límits honests i com contribuir

Els límits són sincers: el **factor autobús és 1** (un estàndard només existeix si una
comunitat externa l'adopta i en governa els canvis), les fites de comunitat **no arrenquen
fins que hi hagi almenys 3 docents externs** usant el kit, un graf gran exigeix constància de
manteniment, i l'eina verifica **forma i enllaços, no idoneïtat pedagògica** — la resta és
criteri professional del docent. El [README](/README.md) desenvolupa aquests límits sense
embuts i n'és la font viva.

**Com contribuir:** llegeix [CONTRIBUTING.md](/CONTRIBUTING.md), obre un *issue*, explica el
teu cas a `06-comunitat/` (amb inicials i sense noms de centres) o proposa un core per a la
teva etapa. **Llicències:** codi i eines MIT; continguts, plantilles i exemples CC BY-SA 4.0.
Per citar el projecte (APA, BibTeX, text pla), vegeu el [README](/README.md#com-citar-aquest-projecte).

---

## Relacions (Graf)

- Complementa: `01-que-es-okf.md` (què és OKF) i `02-filosofia.md` (per què).
- Pont divulgatiu de: `09-graf-curricular.md` §10.8 (mapatge tècnic v0.3).
- Complementa: `08-relacio-amb-estandards.md` (posicionament honest).
- Prepara: la migració v1.4 (CHANGELOG, política de retirada).
- Derivats *(no creats en aquesta versió)*: `11-conformitat-okf-v03.html` (claustres/formació)
  i `annex-onepager-direccio.html` (direcció/inspecció).

## Versionatge

| Versió | Data | Canvis |
|:------:|:----:|:-------|
| V1.0 | 2026-11-19 | Creació: guia divulgativa de la conformitat OKF v0.3 i la governança del cicle de vida. Pendent de revisió humana (`verified`). |

---

*OKF Starter Kit · concept DOI 10.5281/zenodo.23823818 · Fet amb estima per l'artesania docent.*
