# OKF Starter Kit

> **Una proposta de sistema operatiu per al coneixement curricular docent.**  
> El currículum com un graf de text pla: llegible, versionable i teu.  
> I una invitació oberta a construir, entre tots, un estàndard educatiu lliure.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE.md)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-blue.svg)](LICENSE.md)
[![Status: V1.3](https://img.shields.io/badge/Status-V1.3-yellow.svg)](CHANGELOG.md)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23823818.svg)](https://doi.org/10.5281/zenodo.23823818)
[![Language: Català](https://img.shields.io/badge/Language-Catal%C3%A0-red.svg)](#)

---

## Índex
- [Què és això, de docent a docent?](#què-és-això-de-docent-a-docent)
- [D'on surt la idea?](#don-surt-la-idea)
- [El problema de cada setembre](#el-problema-de-cada-setembre)
- [De la trinxera a l'Starter Kit](#de-la-trinxera-a-lstarter-kit)
- [Què fa diferent aquest mètode?](#què-fa-diferent-aquest-mètode)
- [Tres portes d'entrada (i una de sortida)](#tres-portes-dentrada-i-una-de-sortida)
- [Com és un node OKF?](#com-és-un-node-okf)
- [Què conté aquest repositori?](#què-conté-aquest-repositori)
- [Inici ràpid en 10 minuts](#inici-ràpid-en-10-minuts)
- [Límits coneguts i honestedat](#límits-coneguts-i-honestedat)
- [Llicències i citació](#llicències-i-citació)
- [Declaració d'ús d'IA](#declaració-dús-dia)
- [Crèdits i agraïments](#crèdits-i-agraïments)

---

## Què és això, de docent a docent?

L'**OKF Starter Kit** no és cap programari comercial que hagis d'instal·lar ni cap plataforma amb subscripció al núvol. És una metodologia oberta per estructurar programacions, activitats, criteris d'avaluació i recursos didàctics en **fitxers de text pla (Markdown)** interconnectats en forma de graf.

Igual que un sistema operatiu gestiona els recursos d'una màquina, aquest kit posa ordre a la complexitat curricular perquè puguis treballar-hi amb rigor i coherència. 

Quan el teu coneixement docent està estructurat i validat, pots connectar-hi models de llenguatge mitjançant els **Paquets LLM**: instruccions en text pla que pots auditar, retallar o adaptar. L'objectiu és senzill: que la feina docent deixi de ser un cementiri de fitxers Word oblidats i torni a ser un taller viu.

---

## D'on surt la idea?

Soc del 74, biòleg de formació i professor de Formació Professional a la xarxa pública des del 2008. Abans treballava en control microbiològic a la indústria farmacèutica, on el que no estava registrat, validat i traçat, senzillament no existia.

El 2015, sent interí, em va tocar el mòdul de Codificació Sanitària. Treballant amb ontologies mèdiques (CIM-10, SNOMED-CT) em va caure la fitxa: **el currículum funciona exactament com una biologia**. Està format per resultats d'aprenentatge, criteris d'avaluació, continguts i activitats que depenen els uns dels altres. Cap concepte no viu aïllat. I tanmateix, el continuem gestionant en documents Word lineals de 15 o 20 pàgines, esquemàtics i pensats per al tràmit, que no recullen la riquesa real de l'aula i queden obsolets cada curs

**La gènesi amb Google OKF (juny de 2026):** Quan Google Cloud va publicar l'especificació *Open Knowledge Format* (un model obert i minimalista per compartir bases de coneixement mitjançant Markdown i capçaleres YAML per a agents d'IA), vaig veure clar que allò que proposaven per a l'àmbit corporatiu era la solució idònia per al currículum. 

Aquest repositori és un **perfil curricular català de l'especificació OKF**: respecta l'estàndard base (el camp `type`) i hi afegeix **9 tipus universals** i **8 camps mínims** per a la governança educativa. 

* **Relació amb altres marcs:** Dialoga conceptualment amb CASE, LRMI i Schema.org, però prioritza la sobirania del docent. No pretén substituir els aplicatius oficials (com Esfer@ o SAGA), sinó oferir una font de veritat des d'on generar automàticament imports massius (detalls a [`00-documentacio/08-relacio-amb-estandards.md`](00-documentacio/08-relacio-amb-estandards.md)).

---

## El problema de cada setembre

Tots coneixem la inèrcia d'inici de curs:
- 50 fitxers dispersos al Drive: `Programacio_v2_definitiva_OK.docx`, exàmens desconnectats de la seva pauta i activitats sense criteris clars.
- Modifiques un criteri al gener i has de recordar quins dotze documents has d'obrir a mà per actualitzar-lo.
- Si fas una substitució, sovint reps un calaix desendreçat o el buit absolut.
- Cada any reinventem la roda perquè el material heretat és massa rígid per reutilitzar-lo.

El kit busca recuperar el control sobre les nostres pròpies eines de treball.

---

## De la trinxera a l'Starter Kit

Aquest kit és fruit de caps de setmana i vacances a la trinxera de casa, no d'un encàrrec institucional. Neix d'una obsessió personal sotmesa a la prova del cotó amb companys reals:

* **El factor Montse:** A l'agost de 2026 vaig muntar el graf del cicle TCAI (Cures Auxiliars d'Infermeria) per operar-lo amb IA. Quan li vaig passar les bateries de *prompts* a la Montse G., la meva co-docent de la tarda, es va atabalar amb tota la raó: jo li passava una enginyeria pensada per al meu cap tecnològic, i ella només volia preparar una bona classe. D'aquí va néixer el **Paquet LLM**: una recepta transparent en text pla que ella pot llegir, ajustar o retallar sense tocar cap línia de codi. La Montse és la veritable usuària del sistema: gràcies a ella treballem coordinats matí i tarda sense angoixa tecnològica.
* **Proves fora de la zona de confort:** Amb en Benet M. vam construir de zero el mòdul de Química (una especialitat que jo no domino) per provar que l'estructura sosté qualsevol matèria; amb en César G. vam validar l'escalabilitat d'un vault propi de 59 nodes; i amb l'Ariadna C. vam explorar l'encaix amb la Pedagogia Terapèutica i el Disseny Universal per a l'Aprenentatge (DUA), fent de la privacitat dels menors una condició sagrada de disseny ([`06-comunitat/01-casos-us.md`](06-comunitat/01-casos-us.md)).
* **L'autocrítica:** Els meus vaults personals patien de sobreenginyeria. L'**OKF Starter Kit** és la neteja necessària: l'esquelet mínim per sostenir el curs sense afegir pes inútil.

---

## Què fa diferent aquest mètode?

1. **Text pla (Markdown + YAML):** El teu coneixement viu al teu disc dur, en fitxers lliures i duradors que podràs obrir d'aquí a vint anys amb qualsevol editor.
2. **El graf com a font de veritat:** Les unitats i les activitats s'enllacen en xarxa. La programació que lliures al centre o a Inspecció deixa de ser un document burocràtic a part per esdevenir una vista derivada directa del teu graf.
3. **Paquets LLM sota marcs ètics d'aula:** Operem la IA amb els marcs formulats per Juan José de Haro:
   - **[MIAE](https://jjdeharo.github.io/miae/es/) (Nivell 3):** La IA només proposa esborranys. El docent reconstrueix, valida críticament i pren la decisió final.
   - **[VCER](https://vibe-coding-educativo.github.io/vibe-responsable/ca/) (*Vibe Coding Educatiu Responsable*):** Els materials d'aula generats han de ser 100% *offline*, sense telemetria d'alumnat, accessibles per teclat i amb llicència lliure.
4. **Validació determinista:** Un script en Python comprova l'estructura dels Cores: camps obligatoris, coherència de tipus, integritat d'enllaços relatius (zero enllaços trencats, sense dependència de wikilinks propietaris) i governança estructural (`MOC.md`, `Handoff.md`, `Convencio.md`). 

---

## Tres portes d'entrada (i una de sortida)

El kit no té una única manera de començar. Té **tres Paquets LLM** que cobreixen tot el cicle, des de la construcció del vault fins al document oficial:

| Paquet | Enfocament | Punt de partida | Punt d'arribada | Fitxer |
|:---|:---|:---|:---|:---|
| **Paquet 00** | **Deductiu** | Currículum oficial | Vault construït | [`PLANTILLA-PaquetLLM-00.md`](04-plantilles/PLANTILLA-PaquetLLM-00.md) |
| **Paquet 01** | **Inductiu** | Programació existent | Vault construït | [`PLANTILLA-PaquetLLM-01.md`](04-plantilles/PLANTILLA-PaquetLLM-01.md) |
| **Paquet 02** | **Sortida** | Vault construït | Document oficial (Word) | [`PLANTILLA-PaquetLLM-02.md`](04-plantilles/PLANTILLA-PaquetLLM-02.md) |

**Quin trio?**

- **Tens una programació feta** (Word, PDF, Excel) i vols convertir-la en un vault OKF sense reescriure-la → **Paquet 01** (inductiu).
- **Comences de zero** (mòdul nou) o vols repensar la programació des del currículum → **Paquet 00** (deductiu).
- **Ja tens el vault construït** i vols generar el document oficial per a Inspecció → **Paquet 02** (sortida).

Els dos primers camins porten al mateix lloc: un vault OKF validat. La diferència és el punt de partida i el grau de formalitat del resultat. El camí inductiu preserva la feina existent; el deductiu produeix un graf formalment més perfecte. El tercer tanca el cercle: converteix el vault en el document que has de lliurar.

**Exemple de sortida:** [`04-plantilles/exemples/Programacio_Didactica_MP1519.html`](04-plantilles/exemples/Programacio_Didactica_MP1519.html) — una Programació Didàctica completa en HTML/CSS, llesta per importar a Word.

---

## Com és un node OKF?

Un document d'activitat o d'unitat és text net acompanyat d'unes metadades clares. Aquí tens un exemple de **Fitxa AEA** (el tipus de node que fa servir la família LOE):

```markdown
---
id: SAD-MP1519-AEA-01
type: FitxaAEA
title: "AEA 1: El SIS i l'estandardització de la dada clínica"
version: "V1.0"
data_ultima_actualitzacio: "2026-11-06"
authors:
  - "Josep Montañà Piqué"
llicencia: "CC BY-SA 4.0"
legal_framework: LOE
modul: "MP1519"
criteris_avaluacio: ["1.1", "1.2", "1.3", "1.4"]
instruments_avaluacio:
  - codi: "I1"
    descripcio: "Observació competencial amb llista de control"
    criteris: ["1.1", "1.2", "1.3", "1.4"]
tags:
  - okf/aea
  - okf/mp1519
estat: vigent
---

# AEA 1: El SIS i l'estandardització de la dada clínica

Aquesta activitat desplega el Resultat d'Aprenentatge RA1 del mòdul.

## Activitats associades
- [Protocol d'avaluació](./02_MP1519_Protocol_Avaluacio.md)
- [Catàleg curricular](./01_MP1519_Cataleg_Curricular.md)
```

I quan vols verificar la coherència estructural abans de tancar el trimestre:

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

*(«0 errors» confirma que el graf compleix les regles de forma i enllaç; el rigor pedagògic del contingut continua sent responsabilitat del docent).*

---

## Què conté aquest repositori?

| Carpeta | Contingut | Utilitat pedagògica |
|:---|:---|:---|
| **`00-documentacio/`** | Filosofia, arquitectura, manuals d'acollida i ROADMAP | Guia conceptual per pensar el teu currículum en xarxa, i full de ruta del projecte. |
| **`01-cores/`** | Nuclis curriculars oficials (LOMLOE i FP) | L'esquelet normatiu per no haver de picar decrets a mà. |
| **`02-exemple-complet/`** | Mòdul complet desplegat (MP1519, 14 nodes) | Exemple de referència: 5 AEAs, protocol de 3 portes, Paquet LLM i validador. |
| **`07-exemple-mp1519/`** | Variant en dues capes del mòdul MP1519 | Model centrat en catàleg + fitxes d'activitat (amb MOC detallat). |
| **`03-eines/`** | Validador (`validar_yaml.py`) i snapshot (`status_snapshot.py`) | Eines de consola per auditar la salut del graf i obtenir resums per a la IA. |
| **`04-plantilles/`** | Plantilles de nodes (MOC, UD, AEA, els 3 Paquets LLM…) | Models llestos per duplicar i omplir en pocs minuts. |
| **`05-exemples-minims/`** | Vault de prova reduït (5 nodes, carpeta `vault-de-3-nodes`) | El banc de proves més petit possible per arrencar sense aclaparar-se. Inclou un **[ZIP descarregable del mini-vault](05-exemples-minims/vault-de-3-nodes.zip)**. |
| **`06-comunitat/`** | Casos d'ús reals i article d'anàlisi docent | Experiències d'aula i documentació divulgativa. |

### Eines d'auditoria i diagnosi

* **Snapshot d'estat (`status_snapshot.py`):** Genera un bloc resum de text pla amb l'estat del repositori (branques, commits, tests i recompte de nodes) ideal per enganxar directament a un xat d'IA.
* **Auditoria curricular (`--audit`):** Executant `python3 03-eines/validar_yaml.py --ruta . --audit`, el motor creua el catàleg normatiu amb les activitats, comptabilitzant la cobertura exacta de Criteris d'Avaluació (CAs coberts, orfes o afegits pel docent) emetent alertes de traçabilitat (`Y045`, `Y046`, `Y052`).

---

## Inici ràpid en 10 minuts

### Vols començar sense clonar tot el repositori?

Descarrega el **[mini-vault en ZIP](05-exemples-minims/vault-de-3-nodes.zip)** (5 nodes) i obre'l directament a Obsidian o al teu editor preferit. És la manera més ràpida de veure l'estructura d'un vault OKF sense instal·lar res. *(Nota: la carpeta es diu `vault-de-3-nodes` per raons històriques, però conté 5 nodes.)*

Pots validar el teu primer mini-graf localment:

```bash
# 1. Clona el repositori
git clone https://github.com/jmonta23-okf/okf-starter-kit.git
cd okf-starter-kit

# 2. Instal·la l'única dependència necessària (PyYAML)
pip install pyyaml

# 3. Executa la validació sobre el vault mínim
python3 03-eines/validar_yaml.py --ruta 05-exemples-minims/vault-de-3-nodes
```

```text
| Mètrica | Valor |
|:--------|:-----:|
| Fitxers .md escanejats (nodes OKF) | 5 |
| Fitxers amb errors | 0 |
| Advertències (🟡) | 0 |

## ✅ Resultat
Tots els nodes OKF del vault han passat la validació sense errors.
```

Per a un recorregut guiat, consulta la [Guia d'inici ràpid](00-documentacio/04-inici-rapid.md).

---

## Límits coneguts i honestedat

Un projecte públic ha de ser transparent amb les seves febleses. L'OKF Starter Kit és una proposta d'estàndard amb una implementació de referència, però avui té limitacions clares:

1. **La corba de l'autonomia (El Factor Montse):** La Montse opera amb èxit els Paquets LLM a l'aula, però encara requereix acompanyament per crear un vault des de zero. Per a un docent sense familiaritat amb Markdown, Git o la terminal, la barrera d'entrada continua sent alta. Els Paquets 00 i 01 redueixen aquesta barrera, però no l'eliminen.
2. **Estàndard vs. Eina personal:** Els Cores fixen una especificació tècnica formal arxiu a Zenodo, però un estàndard només existeix si hi ha una comunitat externa que l'adopta i en governa els canvis de forma autònoma. Avui el factor autobús encara és 1.
3. **El cost del manteniment:** Mantenir un graf gran demana constància. En moments punta del trimestre (avaluacions, entrevistes de tutoria), el temps docent és escàs i el graf corre el perill de quedar desfasat si no s'automatitza prou.
4. **Comprovació formal, no de contingut:** L'eina verifica metadades, camps i rutes d'enllaços. La idoneïtat pedagògica del que hi ha escrit continuarà sent sempre patrimoni del teu criteri professional.

---

## Llicències i citació

* **Codi i eines:** Llicència **MIT** (lliure per reutilitzar, modificar i distribuir).
* **Plantilles, documentació i exemples curriculars:** **Creative Commons Reconeixement-CompartirIgual 4.0 (CC BY-SA 4.0)**.

**Com citar el projecte (APA 7a edició):**
> Montañà Piqué, J. (2026). *OKF Starter Kit: una proposta de sistema operatiu per al coneixement curricular docent* (V1.3) [Programari]. Zenodo. https://doi.org/10.5281/zenodo.23964880

*(Per citar el concepte global del projecte de manera independent de la versió: [https://doi.org/10.5281/zenodo.23823818](https://doi.org/10.5281/zenodo.23823818)).*

---

## Declaració d'ús d'IA

Aquest kit és fruit d'una **cocreació reflexiva amb models de llenguatge** (Claude, DeepSeek, Gemini). No és codi generat en pilot automàtic, sinó un diàleg continu on l'autor humà ha pres totes les decisions crítiques de disseny, arquitectura i supervisió pedagògica.

* **Nivell MIAE declarat del projecte:** **Nivell 4 (Cocreació)** per a la construcció del kit com a obra. Per als materials que genereu per als alumnes a l'aula, el kit prescriu mantenir-se estrictament al **Nivell 3 (Supervisió docent)**.
* **Privacitat estricta (Zero dades personals):** El text que s'envia als models en operar un Paquet LLM és exclusivament **estructura curricular i disseny pedagògic**. Al graf **MAI hi ha dades personals d'estudiants**. Les adaptacions i suports educatius (com el DUA o els Plans Individuals) s'articulen com a bancs d'estratègies abstractes i models tipificats, mai associats a noms ni historials individuals.

---

## Crèdits i agraïments

Construït amb el suport i l'aprenentatge compartit amb companys d'ofici:

* **Josep Montañà Piqué:** Disseny, arquitectura i implementació.
* **Montse G.** (Sanitat - TCAI): La seva sinceritat a l'aula davant la complexitat tècnica va ser l'espurna que va fer néixer els Paquets LLM.
* **Benet M.** (Química): La confiança per desplegar el seu primer mòdul docent sencer dins d'aquest graf.
* **Ariadna C.** (Pedagogia Terapèutica): La complicitat per dissenyar estructures curriculars inclusives respectant al 100% la privacitat.
* **César G.** (Sanitat): L'audàcia de fer créixer un vault docent autònom de gairebé seixanta nodes.
* **Juan José de Haro:** El mestratge dels marcs MIAE i VCER, que aporten el criteri ètic a aquest taller.

Si vols col·laborar obrint nous cicles, polint les eines o proposant simplificacions a la convenció, revisa [CONTRIBUTING.md](CONTRIBUTING.md).

Fet amb estima per l'artesania i la dignitat de la professió docent.  
*Josep Montañà Piqué — 2026*
```
