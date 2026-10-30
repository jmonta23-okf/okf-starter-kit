# Glossari d'OKF Starter Kit

> **Terminologia canònica del sistema, ordenada alfabèticament.**  
> Aquest document fixa el significat precís de cada concepte per garantir la coherència pedagògica i tècnica del graf.

---

## A

**AEA (Activitat d'Ensenyament-Aprenentatge)** — Seqüència formativa concreta d'aula o taller dins d'una unitat didàctica. Detalla els objectius, la temporització minutada, els recursos necessaris, els Criteris d'Avaluació mobilitzats i els instruments de qualificació. Vegeu `FitxaAEA`.

**Agnòstic de model** — Propietat d'un sistema que no depèn de cap proveïdor ni model d'Intel·ligència Artificial concret. OKF és agnòstic: funciona amb Claude, ChatGPT, Gemini, models d'execució local (com Ollama o LM Studio), o sense cap mena d'IA (únicament amb text pla i criteri docent).

**Auditabilitat** — Propietat que permet que qualsevol persona pugui llegir, entendre, verificar i modificar el funcionament intern d'un sistema sense trobar caixes negres. A OKF tot és auditable: les dades són text pla transparent i el validador és un script obert en Python de 400 línies.

---

## C

**Camp obligatori** — Camp del frontmatter YAML que ha d'estar present a la capçalera de tots els nodes perquè el validador el doni per bo (per exemple: `id`, `type`, `title`, `version`, `academic_year`, `legal_framework`, `tags`). Si el node és de tipus curricular, també requereix obligatòriament el camp `credit`.

**Convenció de Nomenclatura** — Document formal que fixa les regles internes d'un vault: quins tipus de nodes s'admeten, quins camps són requerits, quin patró segueixen els identificadors i on s'ubica cada fitxer. És la "constitució" de governança del vault. Vegeu `04-plantilles/PLANTILLA-ConvencioNomenclatura.md`.

**Convenció YAML Mixta** — Decisió d'arquitectura d'OKF que combina l'anglès per a les metadades de framework i identitat (`id`, `type`, `title`, `version`, `authors`, `tags`...) per garantir la interoperabilitat tecnològica internacional, i el català per als camps de domini pedagògic (`data_ultima_actualitzacio`, `credit`, `durada`, `resultats_aprenentatge`, `criteris_avaluacio`, `estat`...) per reflectir la realitat curricular de la nostra comunitat docent. Vegeu [Arquitectura §4](./03-arquitectura.md#4--la-convenció-yaml-mixta-en--ca).

**Core (o Nucli normatiu)** — Document que estableix el marc curricular oficial prescriptiu (LOE o LOMLOE) per a una etapa o família professional. Conté els Resultats d'Aprenentatge, Criteris d'Avaluació i competències oficials. A OKF és el *Kernel* que garanteix la interoperabilitat entre vaults diferents.

**Currículum oficial (prescrit)** — El marc legal aprovat pel Departament d'Educació i publicat al DOGC/BOE (primer nivell de concreció). És immutable per al docent i serveix de base de referència comuna. Es diferencia clarament de la *Programació Didàctica viva*.

---

## E

**EINES/** — Carpeta de treball local on el validador desa els informes d'auditoria automàtics (`informe_validacio_YYYY-MM-DD.md`). Està inclosa al fitxer `.gitignore` perquè conté artefactes temporals d'execució, no contingut curricular del curs.

**Enllaç relatiu** — Enllaç de Markdown que connecta dos fitxers a partir de la seva posició relativa a l'arbre de carpetes (per exemple: `[Activitat 1](./02_Fitxa_AEA_1.md)`). És l'únic format admès a OKF perquè assegura que el vault funcioni en qualsevol sistema operatiu, es pugui moure de carpeta o es cloni per git sense trencar cap vincle.

---

## F

**Fenotip curricular** — Metàfora biològica que descriu qualsevol expressió o document extern derivat del graf (com la programació de 80 pàgines per a Inspecció, una presentació interactiva per a classe o una fitxa d'exercicis en PDF). És una vista temporal i contextualitzada, no la font de veritat del curs. Vegeu `Genotip curricular` i `Vista derivada`.

**FitxaAEA** — Tipus de node canònic que descriu una Activitat d'Ensenyament-Aprenentatge concreta. És un node de crèdit i requereix el camp `credit`.

**Frontmatter YAML** — Bloc de metadades estructurades situat a l'inici d'un fitxer Markdown, delimitat per dues línies de tres guions (`---`). Actua com el carnet d'identitat del node per al validador i per als agents d'IA.

---

## G

**Genotip curricular** — Metàfora biològica que descriu el graf de fitxers Markdown i YAML que compon el teu curs. És la font de veritat bàsica, pura i interconnectada d'on neixen tots els materials.

**Graf** — Xarxa de nodes interconnectats mitjançant enllaços semàntics. A diferència d'un sistema de carpetes aïllades, en un graf cada activitat està vinculada simultàniament al seu criteri d'avaluació, al seu protocol de seguretat i a la seva rúbrica.

---

## H

**Handoff (DocumentHandoff)** — Tipus de node que documenta l'estat d'un projecte en un moment exacte del temps: què s'ha fet, quines decisions s'han pres, quins deutes tècnics queden pendents i com continuar. Funciona com una memòria històrica immutable i facilita el relleu immediat entre docents.

---

## I

**ID** — Clau primària única que identifica un node al graf sense ambigüitat. Segueix el patró canònic `{CODI}-{ÀMBIT}-{NN}` (per exemple: `MP1519-MOC-00`, `QU20-MP1257-UD-01`).

**Interoperabilitat** — Capacitat de dos vaults docents diferents de compartir activitats, rúbriques o mòduls sencers sense fricció, gràcies a compartir el mateix Core normatiu i la mateixa Convenció de Nomenclatura.

---

## L

**Llicència oberta** — Marc legal que permet l'ús, la modificació i la redistribució lliure del coneixement. OKF Starter Kit utilitza una doble llicència: **MIT** per al codi de les eines i scripts de Python, i **Creative Commons Reconeixement-CompartirIgual 4.0 (CC BY-SA 4.0)** per a les plantilles, guies i continguts curriculars.

---

## M

**Markdown** — Format de text pla estàndard (`.md`) fàcilment llegible tant per persones com per màquines. Utilitza caràcters senzills per definir títols (`#`), llistes (`-`) o enllaços (`[]()`). És la base indestructible sobre la qual s'escriuen tots els nodes d'OKF.

**MIAE (Marc per a la Integració de la IA en Educació)** — Marc metodològic (De Haro, 2026) que regula el grau d'intervenció humana en els processos assistits per IA (Nivells 0 al 5). A OKF, els Paquets LLM s'adscriuen al **Nivell 3** (*esborrany IA + reconstrucció humana obligatòria*), garantint que cap decisió d'avaluació o de seguretat es prengui sense supervisió docent.

**MOC (Map of Content)** — Tipus de node arrel que actua com a mapa i taula d'indexació d'un mòdul, cicle o secció. És el punt d'entrada per navegar pel graf.

---

## N

**Node** — La unitat atòmica de coneixement a OKF. És un fitxer Markdown amb una capçalera YAML que descriu un sol element pedagògic: una unitat didàctica, una sessió d'aula, un protocol de seguretat, una rúbrica o un glossari.

---

## O

**OKF** — Acrònim amb doble lectura complementària:
1. **Open Knowledge Format:** L'especificació tècnica oberta (impulsada per la indústria el 2026) per estructurar dades en text pla i evitar al·lucinacions en agents d'IA.
2. **Organized Knowledge Framework:** El marc de treball docent d'aquest kit per organitzar el currículum com un graf i operar-lo artesanalment a l'aula.

**Ontologia curricular** — Sistema d'organització del coneixement basat en conceptes interconnectats i relacions semàntiques (inspirat en ontologies mèdiques com SNOMED-CT o la CIM-10). Supera la visió clàssica de la programació com a document pla i la transforma en una xarxa viva i coherent.

---

## P

**PaquetLLM** — Tipus de node operatiu que defineix un **contracte de generació per a la IA**. Conté el context tancat del vault, les instruccions de format i les restriccions pedagògiques perquè un model generi materials d'aula (presentacions, fitxes, exàmens) d'alta qualitat, sota els marcs **MIAE** i **VCER**. Més enllà d'un prompt, és el **taller** del docent.

**Programació Didàctica (viva)** — El conjunt estructurat d'unitats, activitats, criteris contextualitzats i instruments d'avaluació que el professorat desplega i manté al llarg del curs (segon i tercer nivell de concreció). A OKF, la programació viva és el graf mateix, que s'adapta al grup-classe i evoluciona curs rere curs.

**Python** — Llenguatge de programació amb què està construït el validador automàtic (`validar_yaml.py`). No requereix coneixements de codi per part del docent, només la seva instal·lació bàsica per executar l'script d'auditoria.

---

## R

**Reutilització** — Principi ètic i professional d'OKF segons el qual el coneixement estructurat és del docent i camina amb ell. Si canvies de destí o d'institut, obres el teu portàtil i tens el teu taller operatiu immediatament, evitant començar des del fang cada setembre.

---

## S

**Sistema operatiu del coneixement (Proposta de)** — Metàfora arquitectònica que descriu OKF com una capa d'abstracció entre el decret legal cru i la pràctica d'aula, proporcionant estàndards (Cores), interfícies d'integritat (YAML i validador), adaptadors (plantilles) i aplicacions (Paquets LLM). Sempre s'acompanya de l'aclariment: *«No és un programa que s'instal·la; és una manera d'organitzar i validar el coneixement en text pla»*. Vegeu [Filosofia §4](./02-filosofia.md#4--una-proposta-de-sistema-operatiu-lordre-que-fa-lliure-la-ment).

---

## T

**Tag** — Etiqueta de classificació al frontmatter YAML (per exemple: `okf/ud`, `mp1519/mostres`). El validador exigeix que com a mínim un tag comenci amb el prefix de control `okf/`.

**Taller docent** — El model mental que oposa la creació activa a la simple acumulació d'arxius en carpetes. En el taller, el graf és la fusta seleccionada, els Paquets LLM són les eines d'alta precisió i el docent és l'artesà que dissenya els recursos amb criteri propi. El taller no té sostre: creix a mesura que avança l'experiència docent i la tecnologia.

**Tipus de node** — Valor canònic del camp `type` al frontmatter YAML. El Starter Kit admet exactament 15 tipus:
* *Curriculars (requereixen `credit`):* `UnitatDidactica`, `FitxaAEA`, `PaquetLLM`.
* *Transversals:* `MOC`, `ConvencioNomenclatura`, `Guia`, `Protocol`, `Glossari`, `DocumentHandoff`, `CatalegCurricular`, `CoordinacioCurricular`, `PlaEstrategic`, `EinaTecnica`, `NotaDecisions`, `Estàndard`.

---

## V

**Validador** — Script en Python (`03-eines/validar_yaml.py`) que audita estàticament el vault per comprovar que tots els nodes compleixin la Convenció: revisa camps obligatoris, coherència de dates, sintaxi d'identificadors i integritat d'enllaços.

**Vault** — El directori arrel que conté tot el conjunt de nodes, carpetes, eines i plantilles que conformen el graf d'un curs, d'un cicle o d'un departament.

**VCER (Vibe Coding Educatiu Responsable)** — Marc ètic i rúbrica de qualitat ([vibe-coding-educativo.github.io](https://vibe-coding-educativo.github.io/vibe-responsable/ca/)) que audita l'**artefacte generat amb IA**. Exigeix que el material sigui segur per a l'alumnat (zero dades personals), resilient (100% offline i autocontingut en un sol fitxer), universalment accessible per teclat i alliberat amb llicència lliure.

**Vista derivada** — Document o recurs obtingut a partir de la informació continguda al graf (per exemple: el document de Word per a Inspecció, un quadern d'estada a l'empresa en PDF o una presentació HTML interactiva). Si el graf s'actualitza, la vista derivada es regenera mantenint sempre la traçabilitat absoluta.

---

## Y

**YAML** — Format de serialització de dades net i llegible per persones que s'utilitza a la capçalera de tots els nodes OKF (entre els dos `---`) per registrar les metadades de control curricular i de framework.

---

## Com fer servir aquest glossari

* **Si trobes un concepte ambigu o desconegut** mentre desplegues el teu curs, cerca'l en aquesta llista per verificar-ne el propòsit exacte.
* **Si proposes un nou tipus de node o camp al teu centre**, comprova que no entri en conflicte amb aquestes definicions canòniques per preservar la interoperabilitat amb altres vaults.