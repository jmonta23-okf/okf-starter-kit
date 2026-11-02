# OKF Starter Kit

> **Una proposta de sistema operatiu per al coneixement curricular docent.**  
> El currículum com un graf de text pla: llegible, versionable i teu.  
> I una invitació oberta a construir, entre tots, un estàndard per al currículum.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE.md)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-blue.svg)](LICENSE.md)
[![Status: V1.1-Esborrany](https://img.shields.io/badge/Status-V1.1--Esborrany-yellow.svg)](CHANGELOG.md)
[![DOI](https://zenodo.org/badge/23823819.svg)](https://doi.org/10.5281/zenodo.23823819)
[![Language: Català](https://img.shields.io/badge/Language-Catal%C3%A0-red.svg)](#)

---

## Què és això, de docent a docent?

OKF no és cap programari que hagis d'instal·lar ni cap plataforma amb subscripció. És una metodologia oberta per estructurar programacions, activitats, criteris d'avaluació i materials en **fitxers de text pla (Markdown)** connectats com un graf.

Un sistema operatiu posa ordre als recursos d'un ordinador; OKF intenta posar-ne a la complexitat curricular perquè hi puguis treballar amb coherència. És una metàfora: un sistema operatiu fa complir les regles, i OKF les proposa i, com a molt, les comprova.

Quan el teu coneixement és endreçat i validat, hi pots connectar la IA mitjançant els **Paquets LLM**: receptes obertes, en text pla, que pots llegir i modificar. La idea és que el coneixement docent deixi de ser un cementiri de fitxers Word oblidats i passi a ser un taller.

---

## D'on surt aquesta idea?

Soc del 74, biòleg de formació i professor de FP a l'escola pública catalana des del 2008. Abans treballava en control microbiològic a la indústria farmacèutica, on el que no estava validat, registrat i traçat, senzillament no existia.

El 2015, sent interí, em va tocar el mòdul de Codificació Sanitària, el «marró» que ningú volia per la seva complexitat. Me'l vaig agafar com un repte, i treballant amb ontologies i classificacions mèdiques (SNOMED-CT, CIM-10) em va caure la fitxa: **el currículum funciona com una xarxa viva**. Té resultats d'aprenentatge, criteris d'avaluació, continguts, activitats i protocols que depenen els uns dels altres. I tanmateix el gestionem amb documents de Word lineals de 80 pàgines que es trenquen i es desfasen cada trimestre.

**El juny de 2026, Google Cloud va publicar l'especificació Open Knowledge Format (OKF):** un format obert per estructurar coneixement en fitxers Markdown amb frontmatter YAML, pensat perquè els agents d'IA el puguin llegir i compartir. L'especificació era minimalista (només exigia un camp `type`), i estava pensada per al coneixement empresarial.

Quan la vaig llegir, em va caure la fitxa: **allò que Google proposava per al coneixement corporatiu es podia aplicar al currículum.** Un graf de nodes interconnectats, amb metadades validables, era exactament el que necessitava el sistema educatiu. No calia inventar un format nou: n'hi havia prou d'adaptar-ne un d'existent i afegir-hi la capa curricular (Cores, plantilles, Paquets LLM).

Aquest kit és, per tant, un **perfil de l'especificació OKF de Google**, adaptat a l'educació catalana. Respecta el nucli (el camp `type`) i afegeix 9 tipus i 8 camps universals per a la governança del currículum. Si vols el detall tècnic, és a [`02-filosofia.md`](00-documentacio/02-filosofia.md).

**Relació amb altres estàndards educatius.** El kit no implementa CASE (intercanvi de competències), LRMI (descripció de recursos) ni Schema.org (dades estructurades a la web), però hi dialoga conceptualment. Tampoc no pretén substituir els sistemes administratius com Esfer@ o SAGA: la via pràctica per connectar-s'hi és generar fitxers d'importació massiva a partir dels nodes del vault (mitjançant un Paquet LLM), eliminant la introducció manual de notes alumne per alumne. Els detalls complets són a [`08-relacio-amb-estandards.md`](00-documentacio/08-relacio-amb-estandards.md).

---

## El setembre que coneixem tots

Arribes a un institut nou, et canvien el mòdul o obres el Drive per preparar el curs:

- Tens 50 fitxers escampats: `Programacio_v2_definitiva_OK.docx`, exàmens sense pauta de correcció i fitxes de pràctiques que no saps a quin criteri responen.
- Si adaptes un criteri d'avaluació al gener, has de revisar dotze documents a mà, i sempre te'n descuides algun.
- Si cobreixes una substitució, sovint reps carpetes amb retalls o el buit absolut.
- Cada curs reinventes la roda, perquè el material de l'any anterior és massa rígid per reutilitzar-lo.

El kit intenta donar-hi una resposta digna: recuperar el control de les teves eines de treball.

---

## De la trinxera a l'Starter Kit

La trinxera ha estat el meu despatx, a casa. Els vaults de TCAI i SAD són fruit de caps de setmana i vacances, no d'un projecte d'equip ni de res que s'hagi gestat a la sala de professors. Aquest sistema no és un producte corporatiu ni una recepta màgica: és una obsessió personal que ha crescut a base d'assaig i error.

**El factor Montse.** TCAI el compartim. L'agost de 2026 vaig enllestir el graf del cicle de Cures Auxiliars d'Infermeria i vaig començar a operar-lo amb IA, amb bateries de *prompts* que anava polint i passant a la Montse G., la meva co-docent del torn de tarda. Ella s'atabalava, i era normal: jo li passava una enginyeria que tenia sentit al meu cap tecno-friqui, i ella només volia preparar una bona classe. D'aquí va néixer el **Paquet LLM**: una recepta oberta, transparent i en text pla que ella pot llegir, entendre i retallar o canviar una línia. La Montse és la veritable usuària del sistema, i de moment ens permet anar harmonitzats al matí i a la tarda sense que la tecnologia l'angoixi. Quan completo o millore nodes de TCAI, i sobretot els Paquets LLM, ho faig amb ella. SAD, en canvi, l'evoluciono sol i només per mi.

**Els qui s'hi han apropat.** Els companys coneixen els meus vaults, però la majoria no hi han entrat: és una eina que, avui, només fa servir qui té un perfil molt tècnic, i ho entenc. Només a qui ha mostrat interès li he preparat materials a mida per iniciar-s'hi: en Benet M. (un mòdul de Química des de zero, una matèria que no domino), en César G. (un vault propi de 59 nodes que passen el validador) i l'Ariadna C. (Pedagogia Terapèutica, amb la privacitat de menors com a condició de disseny). Amb la Montse en fan quatre, i els explico amb detall a [`01-casos-us.md`](06-comunitat/01-casos-us.md). L'adopció real no es mesura en clics, sinó en temps, motivació i acompanyament reposat.

**L'autocrítica.** Els meus vaults de TCAI i SAD pateixen de sobreenginyeria: m'hi vaig passar de frenada. L'**OKF Starter Kit** és la meva operació de neteja: l'esquelet mínim que aguanta el sistema.

**Per què el publico.** L'allibero a GitHub per trobar altres *rara avis* com jo, que segur que n'hi ha, i per valorar plegats si això mereix tirar-se endavant. Si t'hi reconeixes, ets exactament qui busco. **El codi és meu; l'estàndard pot ser de tots.** Si vols construir-lo amb mi, el taller és obert.

---

## Què fa diferent aquest mètode?

1. **Text pla (Markdown + YAML).** El teu coneixement viu al teu ordinador, en fitxers lliures. Cap format és etern, però el text pla és el que millor resisteix el pas del temps i s'obre amb qualsevol editor.
2. **El graf com a font de veritat (programació viva).** Les unitats i les activitats s'enllacen entre elles. La programació que demana el centre o Inspecció no és un document que hagis de picar a part: és una vista derivada del teu graf, que revises abans de lliurar-la.
3. **Paquets LLM i dos marcs de referència.** La IA s'opera amb **Paquets LLM**: instruccions en text pla que pots llegir i modificar. El seu ús es descriu amb dos marcs de Juan José de Haro:
   - **[MIAE](https://jjdeharo.github.io/miae/es/)** descriu com es reparteix el treball entre la persona i la IA. Per als materials d'aula treballem al **nivell 3**: la IA proposa un esborrany i el docent el reconstrueix i en pren la decisió final.
   - **[VCER](https://vibe-coding-educativo.github.io/vibe-responsable/ca/)** (*Vibe Coding Educatiu Responsable*) posa condicions als materials que es generen: els artefactes (com presentacions HTML interactives) funcionen 100% offline, no envien dades ni telemetria, es poden fer servir amb teclat i s'alliberen amb llicència lliure.
4. **Un validador que et cuida l'esquena.** Un petit script en Python que comprova el compliment dels Cores: els **8 camps universals** i els **9 tipus universals**, els tipus de família declarats a la teva Convenció, els enllaços interns (cap trencat, cap wiki link), els enums de `visibilitat` i `estat`, la presència de MOC arrel, Handoff i Convenció, i la regla de privacitat de menors. Comprova la forma, no la veritat: que el contingut sigui correcte continua sent feina teva.

---

## Com es veu un node OKF?

Un document d'una activitat o unitat és simplement text net amb metadades clares:

```markdown
---
id: QU20-MP1257-UD-01
type: UnitatDidactica
title: "Unitat 1: Auditoria de seguretat del magatzem"
version: "V1.0"
data_ultima_actualitzacio: "2026-10-29"
authors:
  - "Benet M."
  - "Josep Montañà Piqué"
legal_framework: LOE
credit: "MP1257"
tags:
  - okf/ud
  - okf/mp1257
  - mp1257/magatzem
estat: vigent
---

# Unitat 1: Auditoria de seguretat del magatzem

Aquesta unitat desplega el Resultat d'Aprenentatge RA1 del mòdul.

## Activitats associades
- [A1 · Auditoria de seguretat del magatzem](./02_MP1257_Fitxa_AEA_1.md)
```

I quan vols comprovar que el teu curs encaixa abans de publicar:

```bash
python3 03-eines/validar_yaml.py --ruta 02-exemple-complet
```

```text
| Mètrica | Valor |
|:--------|:-----:|
| Fitxers .md escanejats (nodes OKF) | 14 |
| Fitxers amb errors | 0 |
| Advertències (🟡) | 0 |

## ✅ Resultat

Tots els nodes OKF del vault han passat la validació sense errors.
```

«0 errors» vol dir que el graf compleix les regles de forma. No vol dir que el contingut sigui correcte.

---

## Què conté aquest Starter Kit?

| Carpeta | Què hi ha? | Per a què et serveix? |
|:---|:---|:---|
| **`00-documentacio/`** | Filosofia, arquitectura, FAQ i manuals d'acollida | Per entendre com estructurar el teu pensament docent en xarxa. |
| **`01-cores/`** | Nuclis curriculars oficials (LOMLOE i FP) | L'esquelet legal predefinit, perquè no hagis de picar decrets a mà. |
| **`02-exemple-complet/`** | Un mòdul complet desplegat (MP1519, 14 nodes) | Un mirall de referència real: 5 AEAs, protocol de 3 portes, Paquet LLM i validador determinista. |
| **`03-eines/`** | Validador (`validar_yaml.py`) i snapshot d'estat (`status_snapshot.py`) | El validador comprova el compliment dels Cores: 8 camps universals, 9 tipus universals, tipus de família de la Convenció, enllaços, enums i privacitat. L'snapshot genera un resum de l'estat del repo (branca, commits, validador, tests, nodes) en text pla. |
| **`04-plantilles/`** | 6 plantilles preparades (MOC, UD, PaquetLLM…) | Duplica-les per crear els teus primers nodes en pocs minuts. |
| **`05-exemples-minims/`** | Un vault funcional de 5 nodes (MOC, UD, AEA, Convenció i handoff) | El laboratori més petit possible per provar-ho en 30 minuts. |
| **`06-comunitat/`** | Espai de difusió i l'article d'*eDigital* | Per compartir grafs i experiències entre docents. |

### L'eina d'snapshot

A més del validador, el kit inclou **`status_snapshot.py`**, una eina de només lectura que genera un resum estandarditzat de l'estat del repositori: branca, commits recents, resultat del validador, resultat dels tests i recompte de nodes per tipus.

```bash
python3 03-eines/status_snapshot.py --full
```

És especialment útil quan treballes amb un assistent d'IA: el snapshot és un bloc de text pla que es pot enganxar a la conversa perquè l'assistent vegi l'estat real del repo sense necessitat de fer servir la terminal. Modes disponibles: `--quick`, `--full` (per defecte), `--audit` i `--since <ref>`.

---

## Inici ràpid (30 minuts)

Pots provar el validador ara mateix al teu equip:

```bash
# 1. Clona el repositori
git clone https://github.com/jmonta23-okf/okf-starter-kit.git
cd okf-starter-kit

# 2. Instal·la la dependència del validador (només requereix PyYAML)
pip install pyyaml

# 3. Comprova l'exemple mínim
python3 03-eines/validar_yaml.py --ruta 05-exemples-minims/vault-de-3-nodes
```

Segueix el tutorial pas a pas a la [Guia d'inici ràpid](00-documentacio/04-inici-rapid.md).

---

## Per a qui és (i per a qui no)

- **És per a tu si** ets docent de FP, secundària o primària; vols deixar de picar la mateixa burocràcia cada curs; vols que el teu material viatgi amb tu quan canviïs de centre; i vols treballar amb la IA amb criteri propi i amb eines que pots llegir.
- **No és per a tu si** busques un programa comercial amb botons fets per no haver de pensar en la teva programació, o si et produeix rebuig treballar amb fitxers de text.

---

## Límits coneguts (i per què els dic en veu alta)

Aquest kit és una **proposta d'estàndard** (els Cores) amb una **implementació de referència** (el kit sencer). No és encara un estàndard, perquè un estàndard no el declara una persona: l'adopta una comunitat.

### 1 · La paradoxa de la Montse

La Montse pot fer servir el Paquet LLM, però encara no pot crear el seu propi vault des de zero sense la meva ajuda. En Benet, l'Ariadna i en César també van tenir acompanyament directe. El kit ha reduït la fricció, però no l'ha eliminada: per a un docent sense ningú que l'acompanyi, la corba d'aprenentatge (YAML, Git, terminal) continua sent alta. **És feina pendent, no una cosa resolta.**

### 2 · Proposta d'estàndard o eina personal

Els Cores (`OKF-CORE-CATALA-00`, `OKF-CORE-FP-00`) són una especificació formal: fixen 9 tipus universals, 8 camps universals, enums de visibilitat i estat, sintaxi d'enllaç Markdown relatiu i una declaració d'interoperabilitat. El validador és la implementació de referència, i el DOI de Zenodo en dona persistència.

Però un estàndard necessita també:

- **Comunitat externa**: persones que facin servir els Cores sense que jo les acompanyi. Avui no n'hi ha (factor autobús = 1).
- **Governança**: un procés per decidir canvis. Avui les decisions les prenc jo.
- **Adopció per part d'altres projectes**: que altres centres o eines facin servir els Cores. Avui no passa.
- **Versionat formal de l'especificació**: els Cores ja tenen versió (V1.1.1, V1.0.1), però cal separar-lo del versionat del kit.

Això no es pot decretar: s'ha de guanyar, i és feina de mesos o anys. Mentrestant, allibero els Cores amb DOI i llicència oberta, amb una invitació explícita a adoptar-los o a proposar-ne canvis. Si ningú ho fa, el kit serà una bona eina personal; si algú ho fa, podrà esdevenir un estàndard. No puc decidir per la comunitat: només puc posar les condicions perquè passi.

### 3 · El cost de manteniment

Un vault de 60 nodes demana disciplina. Quan arriba un pic de feina (avaluacions, tutories, famílies), el temps de mantenir el graf competeix amb el temps d'atenció a l'alumnat, i en aquesta competició **el graf perd**. Per a un docent amb 20 hores lectives setmanals i tres tutories, potser no és sostenible. No es resol amb cap eina: es resol amb menys nodes o amb més automatització, i és una decisió de disseny que encara no he pres del tot.

### Què no és aquest kit

- **No és encara un estàndard.** Li falta comunitat, governança i adopció externa.
- **No és una eina per a tothom.** És per a qui vol sobirania digital i està disposat a aprendre eines tècniques. Si busques botons, hi ha eines comercials que ho fan millor.
- **No és un producte acabat.** És un prototip amb DOI, provat per quatre persones, sense comunitat externa ni validació independent. El que veus és el que hi ha.
- **El validador comprova la forma, no la veritat.** Comprova l'adherència als Cores (camps, tipus, enllaços, enums, MOC arrel, Handoff, privacitat), però no pot saber si el contingut docent és correcte: això és el teu criteri professional.
- **No substitueix les eines oficials.** El graf és la teva font de veritat interna; el document per a Inspecció és una vista derivada. Mentre no hi hagi exportació automàtica, caldrà fer el pas a mà (o amb un Paquet LLM que t'ho generi).
- **No és una solució per a la cultura escolar actual.** La cultura escolar demana Word, Drive i plataformes oficials. El kit ofereix una capa de sobirania per al docent, no una substitució de les eines del centre.

Els límits són aquí i no enterrats perquè un projecte que amaga els seus límits no és digne de confiança, i perquè tens dret a saber què t'emportes, encara que sigui gratis. Si et fan dubtar, potser el kit no és per a tu, i està bé. Si els veus com un repte assumible, el taller és obert.

---

## Llicències

- El codi de les eines i del validador té llicència **MIT**.
- Les plantilles, la documentació i els continguts curriculars tenen llicència **Creative Commons Reconeixement-CompartirIgual 4.0 (CC BY-SA 4.0)**.

---

## Com citar aquest projecte

**APA (7a edició):**
> Montañà Piqué, J. (2026). *OKF Starter Kit: una proposta de sistema operatiu per al coneixement curricular docent* (V1.1) [Programari]. Zenodo. https://doi.org/10.5281/zenodo.23823819

**BibTeX:**
```bibtex
@software{montanya2026okf,
  author       = {Montañà Piqué, Josep},
  title        = {OKF Starter Kit: una proposta de sistema operatiu per al coneixement curricular docent},
  year         = {2026},
  version      = {V1.1},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.23823819},
  url          = {https://doi.org/10.5281/zenodo.23823819}
}
```

Per citar el projecte en general, sense versió específica, fes servir el concept DOI: https://doi.org/10.5281/zenodo.23823818

---

## Declaració d'ús d'IA

Aquest kit s'ha desenvolupat en **cocreació amb models de llenguatge** (Claude, DeepSeek, Gemini). No és un producte generat automàticament ni fet només per una persona: és el resultat d'un diàleg continu entre l'autor i diversos models, amb l'autor prenent sempre les decisions crítiques.

**Nivell MIAE declarat: 4 (cocreació).** L'autor ha aportat la visió, la filosofia, el domini curricular, els casos reals i les decisions de disseny. La IA ha generat esborranys, ha proposat estructures, ha comès errors (que l'autor ha detectat i corregit) i ha refinat el text. El nivell 3 és el que proposem per als materials d'aula; el kit mateix, com a obra, és de nivell 4.

Aquesta declaració és coherent amb el que el kit demana als materials que genera: cap material no amaga com s'ha fet. Els detalls complets (metodologia, errors detectats, relació amb VCER) són a la [filosofia](00-documentacio/02-filosofia.md#declaració-dús-dia-en-aquest-kit).

**Què s'envia als models d'IA?** Quan es fa servir un Paquet LLM, el text que s'envia al model és el **contingut del graf** (currículum, activitats, criteris d'avaluació). **Mai dades personals de l'alumnat.** Si el graf conté adaptacions individuals (per exemple, un Pla de Suport Individualitzat), cal anonimitzar-les abans de passar-les al model. El VCER garanteix que els materials generats són 100% offline, però el procés de generació sí que passa per un model al núvol (o local, si es tria un model d'execució local com Ollama o LM Studio). Els detalls complets són a [`08-relacio-amb-estandards.md`](00-documentacio/08-relacio-amb-estandards.md).

---

## Crèdits i agraïments

Aquest kit l'he construït sobretot en solitari, als caps de setmana i a les vacances, però no sense ajuda:

- **Arquitectura i mètode original:** Josep Montañà Piqué.
- **Montse G.** (co-docent de TCAI): la seva sinceritat a l'aula davant la complexitat va fer néixer el Paquet LLM.
- **Benet M.** (Química): va confiar en el mètode per al seu debut docent i em va ajudar a comprovar que l'estructura aguanta fora de la meva especialitat.
- **Ariadna C.** (Pedagogia Terapèutica): la millor aliada en l'exploració de grafs per a Plans Individuals (PI) i adaptacions DUA (Disseny Universal per a l'Aprenentatge).
- **César G.** (Sanitat): la complicitat en la creació del seu propi graf docent autònom.
- **Juan José de Haro:** els marcs MIAE i VCER, que guien el nostre taller digital.

Si fas servir el kit a la teva aula, si crees el graf d'un cicle nou o si tens idees per simplificar-lo, obre un *issue*, comparteix la teva experiència o col·labora a [CONTRIBUTING.md](CONTRIBUTING.md).

Fet amb estima per l'artesania i la dignitat de la professió docent.  
*Josep Montañà Piqué — 2026*
