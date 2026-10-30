# Què és OKF?

> **Imagina que tota la teva feina docent —la programació d'aula, les activitats de taller, els criteris d'avaluació i les rúbriques— deixés d'estar atrapada en documents de Word aïllats i passés a comportar-se com una xarxa viva.** Una xarxa on cada peça té un carnet d'identitat clar, sap amb quins criteris es connecta i s'actualitza sense trencar la resta del curs.

Això és **OKF**.

---

## 1 · La idea en dues lectures: Format obert i Marc organitzat

Les sigles **OKF** tenen una doble lectura que explica perfectament el doble propòsit d'aquest kit:

### La base tècnica: *Open Knowledge Format*
El juny de 2026, l'ecosistema tecnològic (amb Google Cloud al capdavant) va formalitzar l'**Open Knowledge Format**: una especificació oberta per emmagatzemar coneixement corporatiu en fitxers Markdown senzills amb capçaleres YAML. L'objectiu era resoldre el gran taló d'Aquil·les de la intel·ligència artificial: les al·lucinacions provocades per la informació desordenada. En lloc d'apostar per bases de dades vectorials opaques o plataformes privatives, la indústria va demostrar que **el text pla estructurat és la manera més fiable perquè un agent d'IA comprengui el context real d'un projecte sense inventar-se res**.

Aquest kit adopta aquesta mateixa filosofia: **zero dependències, zero formats propietaris, màxima compatibilitat.**

### La dimensió docent: *Organized Knowledge Framework*
Però a l'escola pública no només necessitem un format d'arxiu; necessitem un **marc de treball pedagògic**. D'aquí neix la nostra segona lectura:
* **Organized (Organitzat):** Perquè superem el caos d'apilar documents en carpetes i donem a la programació d'aula una estructura de xarxa auditable.
* **Knowledge (Coneixement):** Perquè el centre no és la tecnologia, sinó el teu saber docent: com contextualitzes els criteris oficials, com dissenyes les activitats d'aprenentatge i com avalues.
* **Framework (Marc de treball):** Perquè no és una aplicació tancada, sinó una caixa d'eines que pots adaptar al teu cicle, a la teva matèria i a la teva manera de fer classe.

---

## 2 · La tirania de les carpetes tradicionals

Per què ens costa tant mantenir al dia els materials d'un curs? Perquè **les carpetes ens obliguen a mentir**.

En un sistema de carpetes convencional, un fitxer només pot viure en un sol lloc a la vegada. I aquí comença el dilema de cada inici de curs:
* Una fitxa de pràctiques d'auditoria, on ha d'anar? A la carpeta `Unitat 1`, a la carpeta `Activitats`, o a la carpeta `Avaluació Summativa`?
* Si la guardes a `Unitat 1`, desapareix de la vista d'avaluació.
* Si la dupliques per tenir-la a tots dos llocs, abans del segon trimestre ja hauràs modificat una de les còpies i l'altra haurà quedat obsoleta.

A la realitat de l'aula, **el coneixement docent no és un calaix; és un graf.** Una activitat respon a un Criteri d'Avaluació oficial, utilitza un recurs de taller determinat, s'avalua amb una rúbrica específica i s'emmarca en una unitat didàctica concreta. 

OKF trenca la rigidesa de les carpetes: **cada document és un node lliure que s'enllaça amb tots els nodes amb què manté una relació pedagògica real.**

---

## 3 · L'anatomia d'un node OKF

Un node OKF no requereix cap programari especial. És simplement un fitxer de text `.md` (Markdown) dividit en dues parts complementàries:

```markdown
---
id: SAN-MP1519-UD-01
type: UnitatDidactica
title: "Unitat 1: Gestió de mostres biològiques"
version: "V1.0"
academic_year: "2026-2027"
legal_framework: "LOE"
credit: "MP1519"
data_ultima_actualitzacio: "2026-10-28"
authors:
  - "Docent de Sanitat"
tags:
  - okf/ud
  - mp1519/mostres
estat: vigent
---

# Unitat 1: Gestió de mostres biològiques

Aquesta unitat desplega el Resultat d'Aprenentatge RA1 del mòdul.

## Activitats d'aula associades
- [Fitxa AEA 01: Recepció i registre de la mostra](../02-exemple-complet/03_MP1519_Fitxa_AEA_1.md)
- [Protocol de bioseguretat al laboratori](./MP1519_Protocol_Bioseguretat.md)
```

Aquesta estructura amaga una potència enorme:

1. **La capçalera YAML (entre els dos `---`):** És el carnet d'identitat del fitxer. Està escrit en un format estructurat que tant una persona com un ordinador (un script de validació o un model de llenguatge) poden interpretar en mil·lisegons. Defineix qui és el document, de quin tipus és, quin marc legal l'empara i en quin estat es troba.
2. **El cos en Markdown:** És el text didàctic en llenguatge natural. Clar, estructurat amb encapçalaments, llistes i enllaços relatius estàndard que connecten directament amb altres fitxers del teu curs.

**El resultat:** Tens un document que pots llegir a qualsevol pantalla, imprimir en paper, o passar a una eina d'IA perquè sàpiga exactament a quina part del currículum pertany sense haver-l'hi d'explicar des de zero.

---

## 4 · De l'arxiu mort al taller de creació

Molts docents acumulen gigabytes de materials al núvol que mai més tornen a obrir. OKF fa el camí contrari: transformar el coneixement emmagatzemat en un **actiu operatiu**.

Amb aquest kit pots recórrer cinc dimensions de treball:

```
┌────────────────────────────────────────────────────────┐
│  5. IMAGINAR   Dissenyar dinàmiques que abans no feies │
│  4. CREAR      Bastir mòduls desconeguts en pocs dies  │
│  3. COMPARTIR  Traspàs net i transparent a companys    │
│  2. OPERAR     Generació ètica d'aula (MIAE + VCER)    │
│  1. ORGANITZAR Posar ordre i traçabilitat al graf      │
└────────────────────────────────────────────────────────┘
```

### 1 · Organitzar
Converteixes la teva programació d'aula en una xarxa de nodes connectats. Ja saps sempre a quin criteri respon cada tasca i s'han acabat els enllaços trencats, les rúbriques desconnectades o les versions perdudes.

### 2 · Operar (El gran salt)
Connectes els teus nodes als **Paquets LLM**. Però operar el coneixement amb IA no vol dir fer una generació descontrolada. Vol dir aplicar **Vibe Coding Educatiu Responsable (VCER)** sota el marc **MIAE**:
* **Criteri MIAE (Nivell 3):** La IA treballa com a ajudant d'artesania proposant esborranys sobre el graf, però la supervisió, l'ajust i la decisió final sempre són teves.
* **Filtre VCER:** Els materials generats (com les presentacions HTML interactives) són **100% offline**, respecten la privacitat de l'alumnat (zero rastreig o telemetria), són universalment accessibles per teclat i s'alliberen amb llicència lliure.

### 3 · Compartir
El teu curs no depèn de la teva memòria ni s'esvaeix si canvies de destí. Si arriba un company nou a fer una substitució, li entregues el vault del mòdul: en vint minuts pot navegar pel mapa de continguts (MOC), entendre com s'avalua i començar a fer classe amb serenitat.

### 4 · Crear
Pots agafar un mòdul nou (fins i tot d'un cicle que no és la teva especialitat de base) i, seguint l'estructura dels Cores normatius i les plantilles, aixecar una programació d'aula completa, sòlida i lliurable a inspecció en pocs dies, com vam fer amb el mòdul de Química per a en Benet M.

### 5 · Imaginar
Com que el sistema és text pla obert i no depèn de cap plataforma tancada, **el taller no té sostre**. A mesura que la tecnologia i la teva experiència avancin, el teu ventall de possibilitats s'amplia sense haver de canviar d'eina.

---

## 5 · Què NO és OKF?

Per evitar malentesos, val la pena deixar clar què **no** trobaràs aquí:

* **No és una aplicació comercial amb botons màgics:** No hi ha menús desplegables ni formularis web que intentin endevinar la teva feina. És artesania digital: fitxers de text i eines senzilles, transparents i sota el teu control.
* **No és una base de dades tancada:** No necessites servidors, ni configuracions informàtiques complexes, ni connexió a internet per treballar. Els arxius són teus i viuen a la teva màquina.
* **No és un generador automàtic de burocràcia sense criteri:** OKF no substitueix el criteri docent. La IA és un operador estricte sota les teves ordres; el disseny, el to i l'avaluació final sempre són teus.
* **No és el projecte empresarial de ningú:** No depens que cap empresa mantingui el servei gratuït. Si demà tanquen totes les plataformes tecnològiques del món, els teus documents Markdown continuaran obrint-se exactament igual.

---

## 6 · Què necessites per començar?

La barrera d'entrada és deliberadament mínima:

1. **Un editor de text còmode:** Recomanem [Obsidian](https://obsidian.md) (perquè permet explorar el graf de connexions de manera visual) o [VS Code](https://code.visualstudio.com/), però qualsevol editor de text pla és suficient.
2. **Python instal·lat:** Per poder executar l'script `validar_yaml.py`, que comprova que cap enllaç del teu curs estigui trencat i que no falti cap camp obligatori.
3. **El decret oficial del teu mòdul:** El marc legal de referència per fixar els Resultats d'Aprenentatge i Criteris d'Avaluació bàsics.

---

## Següents passos

* Per conèixer les conviccions docents, l'origen en les ontologies clíniques i la visió de l'ofici, llegeix **[Filosofia](./02-filosofia.md)**.
* Per veure com s'articulen les 4 capes del sistema, els identificadors i la convenció mixta de metadades, consulta **[Arquitectura](./03-arquitectura.md)**.
* Per crear el teu primer node i validar-lo en menys de mitja hora, vés directe a l'**[Inici ràpid](./04-inici-rapid.md)**.
```
