---
id: MP1519-AEA-02
type: FitxaAEA
title: "Fitxa AEA 2: Arquitectura de la CIE-10-ES Diagnòstics i convencions d'eCIEMaps"
subtitle: "Desplegament d'aula: indexació, termes clau, dreceres Z, IAE, Llista Tabular, dummy character X i exclusions (Setmanes 5 a 9)"
cycle: "CFGS Documentació i Administració Sanitàries (SAD)"
center: "Centre educatiu de referència"
academic_year: "2026-2027"
version: "V2.0-Complet"
data_ultima_actualitzacio: "2026-10-29"
authors:
  - "Josep Montañà Piqué"
legal_framework: "Ordre EDU/10/2020 i RD 768/2014 (LOE)"
credit: "MP1519"
durada: "10 h"
resultats_aprenentatge:
  - "RA3"
  - "RA4"
criteris_avaluacio:
  - "3a"
  - "3b"
  - "3c"
  - "3d"
  - "3e"
  - "3f"
  - "4a"
  - "4b"
  - "4c"
  - "4d"
  - "4e"
  - "4f"
  - "4g*"
tags:
  - okf/aea
  - okf/sanitat
  - mp1519/aea2
estat: vigent
---

# Fitxa AEA 2: Arquitectura de la CIE-10-ES Diagnòstics i convencions d'eCIEMaps

> **Propòsit.** Aquesta unitat d'aprenentatge constitueix el nucli operatiu de la codificació de diagnòstics. L'alumnat aprèn a actuar com un veritable detectiu documental: extreure el Terme Clau patològic de la història clínica, utilitzar les dreceres oficials per a condicionants no patològics (Codis Z), navegar amb precisió per l'Índex Alfabètic de Malalties (IAE) i aplicar la **Regla d'Or de la professió**: verificar de manera obligatòria a la Llista Tabular (LT) per assolir la màxima especificitat (5 a 7 caràcters), utilitzar el *dummy character* (X) i interpretar les notes d'incompatibilitat mèdica (*Excluye 1* i *Excluye 2*).

---

## 1 · Dades Generals i Context d'Aula

| Camp | Valor |
|:---|:---|
| **Activitat** | AEA 2 — Arquitectura de la CIE-10-ES Diagnòstics i convencions d'eCIEMaps |
| **Temporització** | Setmanes 5 a 9 (Primer trimestre) |
| **Durada** | 10 hores presencials (5 sessions de 2 hores) |
| **Resultats d'Aprenentatge** | RA3 (Parts de la CIM) i RA4 (Selecció de codis i extracció) |
| **Espai lectiu** | Aula d'Informàtica (amb desdoblament de grup i connexió a eCIEMaps) |
| **Fita avaluativa** | **Fita 2** (Setmana 9): Prova Escrita PE2 + Avaluació Competencial OC (Gimcana del Codi) |

---

## 2 · Criteris d'Avaluació Mobilitzats

Aquesta AEA desplega tots els CAs dels RAs 3 i 4 del [Catàleg Curricular](./01_MP1519_Cataleg_Curricular.md), amb focus prioritari en els criteris nuclears de Nivell A:

* **RA3 (10 % · 6 h):**
  * 🔴 **3.1 (3a):** Navegació eficaç per l'IAE identificant termes principals en negreta.
  * 🔴 **3.2 (3b):** Distinció entre modificadors no essencials `( )` i essencials sagnats.
  * 🟡 **3.3 (3c):** Interpretació de termes relacionals («amb», «en») i remissions (*Véase* / *Véase además*).
  * 🟡 **3.4 (3d):** Aplicació de la prioritat numèrica sobre l'alfabètica a l'IAE.
  * 🔴 **3.5 (3e):** Verificació obligatòria a la Llista Tabular (LT) per a la màxima especificitat.
  * 🔴 **3.6 (3f):** Aplicació estricta de les notes d'exclusió (*Excluye 1* i *Excluye 2*).
* **RA4 (10 % · 6 h):**
  * 🟡 **4.1 (4a):** Anàlisi crítica de l'informe d'alta i documents complementaris (quirúrgics, biòpsies).
  * 🔴 **4.2 (4b):** Extracció del terme clau patològic (mai la localització anatòmica).
  * 🔴 **4.3 (4c):** Ús de les 5 dreceres per a condicionants de salut (Codis Z).
  * 🟡 **4.4 (4d):** Navegació matricial per la Taula de Neoplàsies (topografia $\times$ morfologia).
  * 🔴 **4.5 (4e):** Identificació de codis parcials amb guionet (-) i tancament fins a l'últim dígit.
  * 🔴 **4.6 (4f):** Construcció de codis de 7 caràcters utilitzant la `X` (*dummy character*).
  * 🟢 **4g\***: Consulta de recursos i terminologia en llengua anglesa instrumental(\*).

---

## 3 · Continguts Teòrics Nuclears

### 3.1 · El procés d'indexació i el Perfil del Document
La indexació és l'anàlisi sistemàtica de l'episodi assistencial per extreure'n els **tres pilars del Perfil del Document**:
1. **Diagnòstic Principal (DP):** La condició establerta després de l'estudi com a causa responsable de l'admissió a l'hospital.
2. **Diagnòstics Secundaris (DS):** Comorbiditats preexistents, complicacions intrahospitalàries, antecedents personals d'interès i causes externes.
3. **Procediments (P):** Procediment principal (relacionat amb el DP) i procediments secundaris diagnòstics o terapèutics realitzats durant l'episodi.

> ⚠️ **El parany de l'historial antic:** Els procediments quirúrgics realitzats en episodis passats (ex: *«Pacient colecistectomitzada el 2018»*) **mai es codifiquen com a procediments actuals**. Del passat quirúrgic només se'n codifica l'estat residual o l'absència d'òrgan mitjançant un **Codi Z** com a diagnòstic secundari.

### 3.2 · Les fonts documentals i els límits ètics de l'auditor
Tot i que l'**Informe Clínic d'Alta** és el document jurídic marc, el documentalista ha de recórrer a documents complementaris per cercar la màxima especificitat:
* **Informe quirúrgic:** Detalla l'abordatge real, la tècnica quirúrgica exacta (escissió vs. resecció) i les troballes intraoperatòries.
* **Informe d'Anatomia Patològica:** Defineix la histologia del tumor (benigne, maligne, *in situ*, metàstasi).
* **Notes d'infermeria i dietètica:** Aporten paràmetres de suport objectius (estadiatge d'úlceres per pressió, Índex de Massa Corporal).

> ⚠️ **Límit deontològic innegociable:** La consulta de documents complementaris serveix per **especificar**, mai per contradir o modificar un diagnòstic definitiu emès pel metge responsable. Si de la lectura d'una biòpsia es dedueix un diagnòstic diferent del de l'alta, l'auditor té prohibit canviar-lo pel seu compte: **cal obrir una consulta formal al facultatiu (*Query*)**. El documentalista no diagnostica; audita la traçabilitat.

### 3.3 · Extracció del Terme Clau (TC)
El **Terme Clau** és el bitllet d'entrada a l'Índex Alfabètic de Malalties (IAE). Apareix sempre en **negreta** a l'índex.
* **Regla d'or d'extracció:** Es busca sempre pel **nom de la malaltia, lesió o símptoma**, mai per la regió anatòmica.
  * *«Fractura bimal·leolar de turmell dret»* $\rightarrow$ Terme Clau: **Fractura** (mai turmell).
  * *«Estenosi aòrtica calcificada»* $\rightarrow$ Terme Clau: **Estenosi** (mai aorta).
  * *«Carcinoma de cèl·lules renals»* $\rightarrow$ Terme Clau: **Carcinoma** o remissió a **Neoplàsia**.

### 3.4 · El repte dels Codis Z: Les 5 dreceres de cerca
Quan el motiu de codificació no és una malaltia aguda activa, sinó un estat, un antecedent o una circumstància que influeix en la salut (Capítol 21), la cerca intuïtiva fracassa. Cal aplicar les **5 dreceres oficials**:

| Situació clínica documentada | Terme Clau a l'Índex (IAE) | Exemple d'informe | Codi resultant |
|:---|:---:|:---|:---:|
| **1. Antecedent de malaltia curada** | **Història (personal de)** | *«Antecedent de càncer de còlon operat fa 6 anys sense recidiva.»* | `Z85.038` |
| **2. Mutilació o extirpació d'un òrgan** | **Absència (de)** | *«Mastectomia radical esquerra el 2021.»* | `Z90.12` |
| **3. Fàrmacs o dependència crònica** | **Tractament (farmacològic)** o **Ús** | *«Tractament anticoagulant crònic amb Sintrom.»* | `Z79.01` |
| **4. Dispositius mecànics o pròtesis** | **Estat (de)** o **Presència (de)** | *«Portador de marcapassos cardíac bicameral.»* | `Z95.0` |
| **5. Cirurgia suspesa abans d'iniciar** | **Procediment (no realitzat)** | *«Cirurgia anul·lada per infecció respiratòria aguda.»* | `Z53.09` |

### 3.5 · L'excepció oncològica: La Taula de Neoplàsies
Davant de qualsevol procés tumoral (*càncer, tumor, neoplàsia, blastoma*), l'Índex Alfabètic remet a la **Taula de Neoplàsies**. És una estructura matricial que requereix creuar dues coordenades:
1. **Eix anatòmic vertical:** Localització del tumor (Topografia).
2. **Eix de comportament horitzontal (6 columnes):** Maligne primari, Maligne secundari (metàstasi), Ca *in situ*, Benigne, Comportament incert o Comportament no especificat.
* A la CIE-O-3, el comportament es codifica amb el 5è dígit de la morfologia: `/0` Benigne, `/1` Incert, `/2` *In situ*, `/3` Maligne primari, `/6` Maligne metastàsic.

### 3.6 · Navegació per l'Índex Alfabètic de Malalties (IAE)
Localitzat el Terme Principal en negreta, cal seguir la jerarquia visual de sagnat:
* **Modificadors no essencials entre parèntesis `( )`:** Paraules que poden aparèixer o no a l'informe clínic; **no alteren el codi assignat** (ex: *Pneumònia (aguda) (doble)* manté el mateix codi base).
* **Modificadors essencials sagnats (subentrades):** Modifiquen el codi final de manera obligatòria. Indiquen etiologia, localització o gravetat.
* **Termes relacionals («amb», «en»):** Expressen presumpció de relació causal. Precedeixen a codis de combinació.
* **Instruccions de remissió:** *Véase* (remissió imperativa; no hi ha codi sota aquella entrada) vs. *Véase además* (suggeriment per cercar termes alternatius).
* ⚠️ **Regla d'auditoria: Prioritat numèrica.** A les llistes sagnades de l'IAE, els números tenen prioritat sobre les lletres (ex: *Diabetis tipus 1* o *tipus 2* apareix abans que les entrades alfabètiques).

### 3.7 · Verificació a la Llista Tabular (LT) i especificitat màxima
> ⚠️ **La Regla d'Or de la codificació clínica:**  
> L'Índex Alfabètic només localitza el codi orientatiu. **Està terminantment prohibit codificar directament des de l'Índex.**  
> La confirmació de la lateralitat, l'extensió, les notes d'inclusió i les instruccions obligatòries **NOMÉS es poden verificar a la Llista Tabular**.

* **Codis de 3 caràcters:** Només s'admeten com a vàlids si la categoria no disposa de cap subdivisió addicional.
* **El guionet terminal (-):** Adverteix que el codi és incomplet i requereix obligatòriament caràcters addicionals (lateralitat, causa o evolució).
* **El setè caràcter i el Dummy Character (X):**  
  Als capítols 19 (Lesions) i 20 (Causes Externes), és preceptiu assignar un 7è caràcter d'estadi temporal:
  * `A`: Contacte inicial (mentre el pacient rep tractament actiu).
  * `D`: Contacte subsegüent (fases de recuperació, canvis de guix, rehabilitació).
  * `S`: Seqüela (efecte tardà un cop superada la fase aguda).  
  Si la categoria només té 4 o 5 caràcters i la norma exigeix un 7è caràcter, s'ha d'inserir el caràcter auxiliar **`X`** com a farciment fins a assolir la setena posició (ex: `S82.0XXA`). Un codi sense aquesta `X` és invàlid i rebutjat pel CMBD.

### 3.8 · Notes d'exclusió a la Llista Tabular
Tenen rang de compliment legal obligatori:
* **Excluye 1 (Exclusió pura i mútua):** Les dues patologies són incompatibles mèdicament (ex: hèrnia congènita vs. adquirida). **Mai es poden codificar juntes al mateix episodi.**
* **Excluye 2 (No inclòs aquí):** Indica que la patologia esmentada no forma part de la definició d'aquest codi, però ambdues poden coexistir. **Es poden codificar juntes si l'informe recull les dues condicions.**

---

## 4 · Casos Clínics Oberts (ABP)

### Cas Obert 3 · La pacient sense mama i el parany de l'Índex
* **Escenari:** Dona de 61 anys acudeix a consulta de revisió ambulatòria. A l'alta s'anota: *«Pacient asimptomàtica intervinguda fa tres anys de càncer de mama esquerra amb mastectomia total. Mamografia de control sense evidència de recidiva tumoral.»* Un codificador inexpert cerca a l'Índex per «Mastectomia» (no troba codi diagnòstic) o per «Càncer de mama» (assignant un tumor actiu, cosa absolutament falsa que altera l'estadística del centre).
* **Resolució guiada:** El Terme Clau no és la malaltia ni la cirurgia passada; és l'estat residual: **Absència (de)**.
  1. Terme Principal a l'IAE: `Absència (de)` $\rightarrow$ subentrada `mama(s) i mugró(ns)` $\rightarrow$ subentrada `unilateral`.
  2. Verificació a la Llista Tabular: Categoria `Z90.1`. Per especificar la mama esquerra cal afegir el 5è dígit.
  3. Codi final validat: **`Z90.12`** (Absència adquirida de mama i mugró esquerres) + **`Z85.3`** (Història personal de neoplàsia maligna de mama).

### Cas Obert 4 · El parany de l'Apendicitis: L'especificitat perduda
* **Escenari:** Un informe d'alta d'Urgències conclou: *«Apendicitis aguda amb peritonitis localitzada resolta mitjançant cirurgia.»* El documentalista escriu al cercador electrònic tota la frase de cop i assigna el primer resultat que apareix: `K35.80` (*Apendicitis aguda no especificada*). A l'auditoria interna del RAE-CMBD, el codi és marcat com a error greu de baixa especificitat.
* **Resolució guiada:** Mai s'ha de cercar la frase completa en bloc. Cal extreure el Terme Principal i navegar pels modificadors essencials:
  1. Terme Principal a l'IAE: **Apendicitis**.
  2. Modificador essencial sagnat 1: `aguda`.
  3. Modificador essencial sagnat 2: `amb peritonitis`.
  4. Modificador essencial sagnat 3: `localitzada`.
  5. Verificació tabular: Codi **`K35.30`** (*Apendicitis aguda amb peritonitis localitzada, sense perforació ni gangrena*). L'assignació de `K35.80` implicava una pèrdua de pes al GRD hospitalari.

---

## 5 · Bateria d'Activitats d'Aula i Gimcana del Codi

### Activitat 2.1 · Extracció del Terme Clau
Identifica el Terme Clau (TC) per cercar a l'IAE en cadascun dels següents diagnòstics:
1. `«Colecistitis alitiàsica crònica»` $\rightarrow$ **Colecistitis** (mai vesícula).
2. `«Hernia inguinal dreta estrangulada»` $\rightarrow$ **Hèrnia** (mai inguinal).
3. `«Insuficiència renal crònica estadi 4»` $\rightarrow$ **Insuficiència**.
4. `«Antecedent familiar de neoplàsia de còlon»` $\rightarrow$ **Història (familiar de)**.

### Activitat 2.2 · Modificadors no essencials vs. essencials
Analitza l'entrada d'Índex: `Pneumònia (aguda) (doble) (febre) (purulenta) J18.9`
* Els termes entre parèntesis són **modificadors no essencials**: si l'informe diu *«pneumònia aguda purulenta»*, el codi continua sent `J18.9` llevat que una subentrada sagnada essencial especifiqui l'agent causal (ex: *per Streptococcus pneumoniae* $\rightarrow$ `J13`).

### Activitat 2.3 · L'ús del Dummy Character (X)
Construeix el codi per a: *«Fractura de ròtula dreta, tancada, en pacient atès al servei d'urgències (visita inicial)»*.
1. Terme Clau a l'IAE: `Fractura` $\rightarrow$ `ròtula` $\rightarrow$ `dreta`. Ens condueix a la categoria tabular `S82.0-`.
2. A la Llista Tabular comprovem que la fractura tancada de ròtula dreta ocupa el codi `S82.001-`.
3. La categoria exigeix un 7è caràcter per a contacte inicial (`A`). Com que `S82.001` té 6 caràcters, s'afegeix directament: **`S82.001A`**.
4. *Cas alternatiu:* Si la categoria fos `S82.0` (4 caràcters) i no tingués subdivisions de lateralitat, el codi s'hauria de construir amb dues `X`: **`S82.0XXA`**.

---

## 6 · Prompts per a NotebookLM (Quadern de Normativa)

Prompts d'auditoria per executar sobre el Capítol A de la 6a edició de la CIE-10-ES carregat al Quadern:

* **Prompt 2.1 (Dreceres de Codis Z):**  
  > *«Actua com un supervisor d'auditoria clínica CIM-10-ES (6a edició, 2026). Un informe mèdic recull: 'Pacient exfumador des de fa 5 anys, portador de pròtesi mecànica mitral i sota tractament crònic amb Sintrom'. Indica quins tres Termes Clau oficials cal buscar a l'Índex Alfabètic per a cadascuna d'aquestes tres situacions. Cita la secció del manual oficial que justifica l'ús d'aquests codis Z.»*
* **Prompt 2.2 (El dummy character i el 7è dígit):**  
  > *«Actua com un formador d'auditors. Explica pas a pas a un documentalista novell per què l'omissió del caràcter de farciment 'X' en un codi de lesió del Capítol 19 provoca un error invalidant al RAE-CMBD del Ministeri de Sanitat. Posa un exemple comparant un codi correcte amb dummy character i el seu equivalent mal format.»*

---

## 7 · Seqüenciació Minutada de les 5 Sessions (10 hores)

```
Sessió 1 (Setm. 5 · 2h)    Sessió 2 (Setm. 6 · 2h)    Sessió 3 (Setm. 7 · 2h)    Sessió 4 (Setm. 8 · 2h)    Sessió 5 (Setm. 9 · 2h)
┌──────────────────────┐   ┌──────────────────────┐   ┌──────────────────────┐   ┌──────────────────────┐   ┌──────────────────────┐
│ Indexació i Perfil   │   │ Navegació per l'IAE  │   │ Llista Tabular i X   │   │ La Gimcana del Codi  │   │ Tancament i Fita 2   │
│ • Els 3 pilars doc.  │   │ • Terme Principal i  │   │ • Verificació oblig. │   │ • Resolució en viu   │   │ • Resolució dubtes   │
│   (40 min)           │   │   modificadors sagnats│  │   tabular (40 min)   │   │   de 15 diagnòstics  │   │   final (20 min)     │
│ • Les 5 dreceres de  │   │   (40 min)           │   │ • El 7è caràcter i   │   │   complexos amb      │   │ • Prova Escrita PE2  │
│   codis Z (40 min)   │   │ • Taula Neoplàsies   │   │   el dummy X (40 min)│   │   paranys d'Índex    │   │   Open Book eCIEMaps │
│ • Cas Obert 3        │   │   (40 min)           │   │ • Notes Excluye 1    │   │   (80 min)           │   │   (60 min)           │
│   (40 min)           │   │ • Activitat 2.1 (40) │   │   i 2 (Cas Obert 4)  │   │ • Debat d'auditoria  │   │ • Recollida Dossier  │
└──────────────────────┘   └──────────────────────┘   └──────────────────────┘   └──────────────────────┘   └──────────────────────┘
```

---

## 8 · Avaluació de la Fita 2 (Setmana 9)

L'AEA 2 es clou a la Setmana 9 amb els següents instruments:

1. **Prova Escrita Competencial (PE2 — 70 % de la nota de fita):**  
   * Examen individual *Open Book* amb accés lliure a eCIEMaps.
   * Resolució de 10 casos d'extracció de diagnòstics i codis Z amb paranys d'Índex, exigència de justificació tabular i aplicació de notes d'exclusió.
2. **Observació Competencial (OC — 30 % de la nota de fita):**  
   * Avaluació del dossier pràctic de la «Gimcana del Codi» mitjançant la matriu C1-C6 (destacant el C1 Rigor tècnic en la verificació tabular i el C2 Autonomia en el maneig d'exclusions).

---

## 9 · Relacions del Graf (Enllaços interns)

- **[00_MP1519_MOC.md](./00_MP1519_MOC.md)** — Node arrel i mapa general del mòdul.
- **[01_MP1519_Cataleg_Curricular.md](./01_MP1519_Cataleg_Curricular.md)** — Criteris d'Avaluació oficials dels RAs 3 i 4.
- **[02_MP1519_Protocol_Avaluacio.md](./02_MP1519_Protocol_Avaluacio.md)** — Fórmules de qualificació de la Fita 2 i criteris C1-C6.
- **[03_MP1519_Fitxa_AEA_1.md](./03_MP1519_Fitxa_AEA_1.md)** — Unitat anterior: Estandardització i Mapeig.
- **[05_MP1519_Fitxa_AEA_3.md](./05_MP1519_Fitxa_AEA_3.md)** — Següent unitat: Normativa General de Diagnòstics i Indicador POA.
- **[08_MP1519_Paquet_LLM.md](./08_MP1519_Paquet_LLM.md)** — Operador d'IA per generar bateries d'exercicis de Gimcana.
```
