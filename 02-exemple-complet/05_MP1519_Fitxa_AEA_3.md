---
id: MP1519-AEA-03
type: FitxaAEA
title: "Fitxa AEA 3: Normativa General de Diagnòstics i Indicador POA"
subtitle: "Desplegament d'aula: definició UHDDS de Diagnòstic Principal, incertesa, empat clínic, consultes al facultatiu (Query) i marcadors POA (Setmanes 11 a 21)"
cycle: "CFGS Documentació i Administració Sanitàries (SAD)"
center: "Centre educatiu de referència"
academic_year: "2026-2027"
version: "V2.0-Complet"
data_ultima_actualitzacio: "2026-10-29"
authors:
  - "Josep Montañà Piqué"
legal_framework: "Ordre EDU/10/2020 i RD 768/2014 (LOE)"
credit: "MP1519"
durada: "22 h"
resultats_aprenentatge:
  - "RA5"
  - "RA6"
criteris_avaluacio:
  - "5a"
  - "5b"
  - "5c"
  - "5d"
  - "5e"
  - "5f"
  - "5g"
  - "6a"
  - "6b"
  - "6c"
  - "6d"
  - "6e"
  - "6f"
  - "6g"
  - "6h"
tags:
  - okf/aea
  - okf/sanitat
  - mp1519/aea3
estat: vigent
---

# Fitxa AEA 3: Normativa General de Diagnòstics i Indicador POA

> **Propòsit.** Aquesta unitat d'aprenentatge és la columna vertebral del MP 1519 (representa el 40 % de la qualificació del mòdul). L'alumnat assoleix la capacitat d'auditar i prendre decisions legals sobre l'episodi assistencial: aplicar la definició oficial UHDDS del Diagnòstic Principal (DP), resoldre empats clínics, gestionar la incertesa a l'alta, dominar l'ordre de seqüenciació etiològica («la locomotora i els vagons») i assignar amb precisió quirúrgica l'Indicador POA (Present On Admission), protegint l'hospital de penalitzacions per complicacions intrahospitalàries.

---

## 1 · Dades Generals i Context d'Aula

| Camp | Valor |
|:---|:---|
| **Activitat** | AEA 3 — Normativa General de Diagnòstics i Indicador POA |
| **Temporització** | Setmanes 11 a 21 (Segon trimestre) |
| **Durada** | 22 hores presencials (11 sessions de 2 hores) |
| **Resultats d'Aprenentatge** | RA5 (Normativa de codificació) i RA6 (Codificació de diagnòstics i POA) |
| **Pes curricular conjunt** | **40 % de la qualificació final del mòdul** (RA5: 20 % + RA6: 20 %) |
| **Espai lectiu** | Aula d'Informàtica (amb desdoblament de grup i accés a eCIEMaps) |
| **Fita avaluativa** | **Fita 3** (Setmana 21): Prova Escrita PE3 + Avaluació Competencial OC |
| **Recuperació** | Setmana 22: Recuperació contínua integrada dels RA5 i RA6 |

---

## 2 · Criteris d'Avaluació Mobilitzats

Aquesta AEA mobilitza 15 Criteris d'Avaluació oficials del [Catàleg Curricular](./01_MP1519_Cataleg_Curricular.md), amb 6 criteris nuclears de Nivell A:

* **RA5 (20 % · 12 h):**
  * 🔴 **5.1 (5a):** Aplicació de la definició oficial UHDDS del Diagnòstic Principal.
  * 🔴 **5.2 (5b):** Norma de símptomes vs. diagnòstics confirmats (Secció A.5.1).
  * 🟡 **5.3 (5c):** Codificació com a confirmats dels diagnòstics de sospita a l'alta hospitalària (A.5.2).
  * 🟡 **5.4 (5d):** Excepcions a la sospita: prohibició de codificar sospita en COVID-19 i VIH.
  * 🔴 **5.5 (5e):** Resolució d'empats clínics (dues afeccions concurrents) maximitzant el GRD.
  * 🟡 **5.6 (5f):** Manteniment de la patologia com a DP en procediments cancel·lats (Z53 / A.5.5).
  * 🟡 **5.7 (5g):** Respecte rigorós de l'ordre *«Codifique primero»* / *«Use código adicional»*.
* **RA6 (20 % · 12 h):**
  * 🔴 **6.1 (6a):** Assignació correcta dels valors de l'indicador POA (S, N, D, I, E).
  * 🔴 **6.2 (6b):** Diferenciació de complicacions sorgides durant l'ingrés (POA: N) de comorbiditats (POA: S).
  * 🟡 **6.3 (6c):** Prohibició de situar com a DP una complicació intrahospitalària en ingrés programat.
  * 🟡 **6.4 (6d):** Identificació de categories i codis Z exempts de POA (categoria E).
  * 🟡 **6.5 (6e):** Detecció d'ambigüitats i elaboració de consultes formals no inductives al metge (*Query*).
  * 🟡 **6.6 (6f):** Disseny del Perfil del Document complet (DP + diagnòstics secundaris rellevants).
  * 🟡 **6.7 (6g):** Diferenciació entre comorbiditats actives (DS) i símptomes irrellevants («soroll clínic»).
  * 🔴 **6.8 (6h):** Aplicació de la regla del VIH: un cop categoria C/SIDA, manteniment de per vida del codi `B20`.

---

## 3 · Continguts Teòrics Nuclears

### 3.1 · El mapa mental de la codificació de diagnòstics
La codificació clínica és un procés seqüencial en 4 passos que combina mecànica de recerca amb judici legal:
$$\text{Terme Clau} \longrightarrow \text{Índex Alfabètic (IAE)} \longrightarrow \text{Verificació Tabular (LT)} \longrightarrow \mathbf{\text{Decisió Normativa (DP + POA)}}$$

### 3.2 · El Diagnòstic Principal (DP): La definició oficial UHDDS
Segons l'estàndard internacional UHDDS (*Uniform Hospital Discharge Data Set*), adoptat pel Ministeri de Sanitat:
> *«El Diagnòstic Principal és l'afecció que, després de l'estudi pertinent, s'estableix com a **causa responsable de l'admissió del pacient a l'hospital**.»*

* **Què NO és el DP:**
  * ❌ No és la malaltia més greu de l'episodi.
  * ❌ No és la malaltia que acaba provocant la mort del pacient a planta.
  * ❌ No és la complicació sorgida durant l'estada hospitalària.
* **Què SÍ és el DP:**
  * ✅ És el motiu clínic que va justificar l'ingrés al llit hospitalari.

### 3.3 · Símptomes vs. Diagnòstics Confirmats (Norma A.5.1)
* Els codis de símptomes, signes i troballes anormals (Capítol 18, codis R) **no s'han de codificar com a Diagnòstic Principal si la causa subjacent ha estat diagnosticada i confirmada** a l'alta.
* *Exemple:* Si un informe diu *«Dolor epigàstric agut i vòmits per Úlcera gàstrica sagnant»*, el DP és l'úlcera gàstrica (`K25.0`). El dolor i els vòmits són símptomes integrals i **no es codifiquen per separat**.
* *Excepció:* Si el pacient és donat d'alta o traslladat sense que s'hagi arribat a cap diagnòstic etiològic (ex: *«Febre d'origen desconegut»* $\rightarrow$ `R50.9`), aleshores el símptoma és obligatòriament el DP.

### 3.4 · Diagnòstics de sospita a l'alta (Norma A.5.2) i les seves excepcions
* Si en el moment de l'alta hospitalària el diagnòstic està documentat com a *«probable»*, *«sospita de»*, *«compatible amb»*, *«qüestionable»* o *«a descartar»*, **es codifica exactament com si estigués confirmat**.
* ⚠️ **Aquesta norma només aplica a pacients hospitalitzats (amb ingrés).** A consultes externes o urgències sense ingrés, la sospita no es codifica mai com a malaltia confirmada; es codifica el símptoma que ha motivat la visita.
* 🛑 **EXCEPCIONS CRÍTIQUES ABSOLUTES (Prohibició de sospita):**
  1. **COVID-19:** El codi `U07.1` exigeix confirmació analítica de laboratori (PCR/antígens). La sospita de COVID-19 es codifica com a contacte (`Z20.822`) o afecció respiratòria.
  2. **Infecció per VIH / SIDA:** Exigeix sempre confirmació serològica. La sospita mai es codifica com a `B20`.

### 3.5 · Empat clínic i diagnòstics contrastats (Normes A.5.3 i A.5.4)
* **Dues afeccions que compleixen per separat la definició de DP (Empat):** Si un pacient ingressa amb dues malalties agudes simultànies (ex: *Fractura de fèmur* i *Insuficiència cardíaca descompensada*) i ambdues han motivat l'ingrés i han consumit recursos diagnòstics i terapèutics similars, **qualsevol d'elles pot ser seleccionada com a DP**. En aquest cas, l'auditor documentalista tria la que maximitza la coherència del GRD.
* **Diagnòstics contrastats (*«A versus B»*):** Si el metge anota a l'alta *«Diverticulitis aguda versus Càncer de còlon»*, es codifiquen ambdues afeccions; la primera serà el DP i la segona el DS.

### 3.6 · Tractament cancel·lat abans d'iniciar la intervenció (Norma A.5.5)
Quan un pacient ingressa de manera programada per a una cirurgia o tractament i aquest se suspèn abans d'iniciar-se per una contraindicació mèdica (ex: una infecció aguda) o per voluntat del pacient:
* **El Diagnòstic Principal continua sent la patologia original** que va motivar l'ingrés (la que s'havia d'operar).
* **Diagnòstic Secundari 1:** La causa o complicació que ha motivat la cancel·lació.
* **Diagnòstic Secundari 2:** Codi Z de procediment no realitzat:
  * `Z53.09`: Procediment no realitzat per contraindicació mèdica.
  * `Z53.20`: Procediment no realitzat per decisió del pacient / fòbia.

### 3.7 · L'ordre estricte: La locomotora i els vagons
Quan la Llista Tabular inclou instruccions de seqüenciació etiològica, l'ordre de codificació té rang de llei:
1. **`Codifique primero la enfermedad subyacente` (La Locomotora):** La malaltia causal ha d'ocupar obligatòriament la primera posició de diagnòstic.
2. **`Use código adicional` (El Vagó):** El codi que porta aquesta nota no pot anar mai sol ni com a Diagnòstic Principal; ha d'anar immediatament darrere de la causa.
3. *Exemple:* A la neuropatia diabètica, primer es codifica la Diabetis tipus 2 (`E11.40`) com a locomotora i després la polineuropatia (`G63`) com a vagó. Invertir l'ordre invalida el registre del CMBD.

---

## 4 · L'Indicador POA (Present On Admission)

L'indicador POA avalua la qualitat hospitalària i determina si una malaltia ja era present en el moment exacte en què el pacient va ingressar o si s'ha adquirit durant l'estada hospitalària.

### 4.1 · Els 5 valors oficials del marcador POA

| Valor | Literal | Criteri d'assignació | Exemple d'informe |
|:---:|:---|:---|:---|
| **S** | **Sí** (Present a l'admissió) | La patologia ja existia abans de l'ingrés, o es trobava en període d'incubació documentat. | HTA prèvia, diabetis crònica, fractura per caiguda al carrer. |
| **N** | **No** (Sorgit durant l'ingrés) | Condició clínica que no existia a l'ingrés i que ha aparegut a planta o a quiròfan (complicació). | Infecció de ferida quirúrgica al 4t dia, flebitis de catèter, caiguda de llit. |
| **D** | **Dubtós / Desconegut** | La documentació clínica és insuficient per determinar si era present o no. | Estat confusional detectat a les 24 h sense dades prèvies. |
| **I** | **Indeterminat** | Clínicament és impossible saber si el procés s'havia iniciat abans de l'ingrés. | Malaltia infecciosa amb període d'incubació variable. |
| **E** | **Exempt** | Categories que no tenen temporalitat patològica. | Codis Z de situació, antecedents personals, determinants socials. |

> ⚠️ **Fals Amic #2 (Regla d'or d'ingressos programats):**  
> En un ingrés programat per a una intervenció quirúrgica, una complicació intrahospitalària (marcada amb **POA: N**) **MAI pot ser seleccionada com a Diagnòstic Principal (DP)**, per més greu que hagi estat o per més que hagi perllongat l'estada a la UCI.  
> El DP és SEMPRE la patologia motiu de l'admissió (**POA: S**). La complicació és un Diagnòstic Secundari (**POA: N**).

---

## 5 · Ambigüitat Documental i Consultes al Facultatiu (Query)

Quan la història clínica conté contradiccions mèdiques, dades il·legibles o diagnòstics no expressats amb claredat, el documentalista ha d'emetre una consulta formal (*Query*):
* **Principi de neutralitat:** La consulta mai pot ser inductiva (*«Oi que aquesta febre era una pneumònia nosocomial?»* ❌).
* **Estructura d'una Query correcta:**
  1. Exposició objectiva de les dades documentades (analítiques, imatge, tractament administrat).
  2. Pregunta oberta amb opcions clíniques equilibrades.
  3. Petició de signatura i registre a l'expedient abans de tancar l'auditoria.

---

## 6 · Cas Clínic Obert (ABP)

### Cas Obert 5 · El diagnòstic amagat i la factura perduda
* **Escenari:** Un pacient de 74 anys amb antecedents d'hipertensió arterial ingressa de manera programada a Traumatologia per a la col·locació d'una pròtesi total de genoll a causa d'una gonartrosi primària severa bilateral. A planta, vuit hores abans de baixar a quiròfan, el pacient desenvolupa dispnea sobtada, ortopnea i crepitants pulmonars. Es diagnostica una Insuficiència Cardíaca Congestiva (ICC) descompensada. Se suspèn immediatament la cirurgia, el pacient és traslladat a la Unitat de Cures Intensives durant 4 dies per a estabilització hemodinàmica i finalment rep l'alta a domicili sense haver estat operat del genoll.
* **El dilema de l'auditor:** Un documentalista inexpert proposa com a Diagnòstic Principal la *Insuficiència Cardíaca Congestiva*, argumentant que ha estat la malaltia més greu, la que ha motivat l'ingrés a la UCI i la que ha consumit més del 90 % dels recursos de l'episodi.
* **Resolució guiada (Norma A.5.5 i Fals Amic #2):**
  1. La proposta de l'auditor inexpert és errònia i seria rebutjada pel RAE-CMBD. El pacient va ingressar per operar-se de l'artrosi; per tant, el Diagnòstic Principal és obligatòriament la **Gonartrosi primària bilateral** (`M17.0`), amb **POA: S**.
  2. La descompensació cardíaca és una patologia concurrent que s'ha manifestat a l'hospital; es codifica com a Diagnòstic Secundari: **Insuficiència cardíaca congestiva** (`I50.9`), amb **POA: S** (ja que era una cardiopatia subjacent prèvia a l'ingrés).
  3. Cal afegir el codi de procediment no realitzat com a diagnòstic secundari: **Procediment no realitzat per contraindicació mèdica** (`Z53.09`), amb **POA: E**.

---

## 7 · Bateria d'Activitats d'Aula i Exercicis d'Auditoria

### Activitat 3.1 · Selecció del Diagnòstic Principal (UHDDS)
Determina el DP en cadascuna de les següents altes hospitalàries:
1. Pacient ingressat per hemorràgia digestiva alta. La gastroscòpia confirma una úlcera duodenal sagnant activa.  
   $\rightarrow$ **DP:** Úlcera duodenal amb hemorràgia (`K26.0`). Els vòmits en pòsit de cafè o la melena són símptomes i no es codifiquen (Norma A.5.1).
2. Pacient traslladat a planta des d'Urgències amb diagnòstic d'alta de «Febre prolongada de 3 setmanes sense focus confirmat».  
   $\rightarrow$ **DP:** Febre d'origen desconegut (`R50.9`), atès que no s'ha assolit cap diagnòstic confirmat.
3. Pacient ingressat per sospita de colecistitis aguda litiàsica. A l'ecografia es confirma litiasi vesicular sense signes inflamatoris aguts.  
   $\rightarrow$ **DP:** Litiasi vesicular sense colecistitis (`K80.20`), atès que la sospita s'ha descartat per la prova d'imatge.

### Activitat 3.2 · Matriu d'Assignació de l'Indicador POA
Assigna el valor POA (S, N, D, I o E) a cadascun dels diagnòstics d'aquest episodi d'ingrés per colecistectomia programada:
* `K80.00` (Colecistitis aguda litiàsica) $\rightarrow$ **POA: S** *(motiu de l'admissió).*
* `I10` (Hipertensió arterial essencial) $\rightarrow$ **POA: S** *(comorbiditat crònica preexistent).*
* `T81.41XA` (Infecció superficial de ferida quirúrgica laparoscòpica al 5è dia d'ingrés) $\rightarrow$ **POA: N** *(infecció nosocomial sorgida durant l'hospitalització).*
* `Z86.73` (Història personal d'ictus isquèmic fa 4 anys) $\rightarrow$ **POA: E** *(antecedent exempt).*

### Activitat 3.3 · La regla del VIH («Un cop B20, sempre B20»)
* Un pacient amb diagnòstic serològic de VIH asimptomàtic va patir fa vuit anys una tuberculosi pulmonar greu (patologia de Categoria C definidora de SIDA). Actualment té càrrega viral indetectable i limfòcits CD4 normals gràcies al tractament antiretroviral. Ingressa per una hèrnia discal.
* **Auditoria:** Queda **terminantment prohibit** codificar la situació com a infecció asimptomàtica (`Z21`). Per normativa oficial espanyola, un cop un pacient ha patit una malaltia de Categoria C, manté de per vida el codi **`B20`** (Malaltia per VIH) com a diagnòstic secundari.

---

## 8 · Prompts per a NotebookLM (Quadern de Normativa)

Prompts d'auditoria per executar sobre el Capítol A de la 6a edició de la CIE-10-ES carregat al Quadern:

* **Prompt 3.1 (L'indicador POA en complicacions quirúrgiques):**  
  > *«Actua com un auditor del Ministeri de Sanitat d'Espanya. D'acord amb la secció A.8.1 del Manual Oficial (6a edició CIE-10-ES, 2026), elabora una taula comparativa que expliqui la diferència jurídica i assistencial entre assignar un POA 'S' versus un POA 'N' en una infecció de catèter venós central. Cita literalment els criteris del manual que prohibeixen situar aquest codi com a Diagnòstic Principal en un ingrés programat.»*
* **Prompt 3.2 (Els diagnòstics de sospita i les seves excepcions):**  
  > *«Actua com un supervisor de codificació clínica. Explica detalladament per quina raó la normativa general permet codificar com a confirmades les sospites d'alta en pacients hospitalitzats (Norma A.5.2), però prohibeix expressament fer-ho en cas de sospita d'infecció per COVID-19 o VIH. Cita les seccions del manual que regulen ambdues excepcions.»*

---

## 9 · Seqüenciació Minutada de les 11 Sessions (22 hores)

```
Sessió 1 (Setm. 11 · 2h): Mapa normatiu i la definició UHDDS del Diagnòstic Principal (DP).
Sessió 2 (Setm. 12 · 2h): Símptomes vs. diagnòstics confirmats (A.5.1) i febre d'origen desconegut.
Sessió 3 (Setm. 13 · 2h): Incertesa a l'alta hospitalària (A.5.2) i excepcions absolutes (COVID/VIH).
Sessió 4 (Setm. 14 · 2h): L'empat clínic (A.5.3 i A.5.4): dues malalties concurrents i selecció de GRD.
Sessió 5 (Setm. 15 · 2h): Procediments cancel·lats per contraindicació mèdica (A.5.5 / Z53). Cas Obert 5.
Sessió 6 (Setm. 16 · 2h): L'ordre etiològic: "Codifique primero" vs. "Use código adicional".
Sessió 7 (Setm. 17 · 2h): L'Indicador POA (I): Marcadors S, N, D, I, E (Secció A.8.1).
Sessió 8 (Setm. 18 · 2h): L'Indicador POA (II): Complicacions intrahospitalàries i el Fals Amic #2.
Sessió 9 (Setm. 19 · 2h): Ambigüitat documental, elaboració de consultes al metge (Query) i soroll clínic.
Sessió 10 (Setm. 20 · 2h): Taller d'auditoria integral d'informes d'alta complexes (Open Book amb eCIEMaps).
Sessió 11 (Setm. 21 · 2h): Tancament i Avaluació de la Fita 3: Prova Escrita PE3 + Recollida Dossier OC.
```

---

## 10 · Avaluació de la Fita 3 (Setmana 21)

La Fita 3 és l'avaluació més determinant del curs (tanca els RA5 i RA6) i s'estructura en:

1. **Prova Escrita Competencial (PE3 — 70 % de la nota de fita):**  
   * Examen individual *Open Book* mitjançant eCIEMaps.
   * Auditoria de 5 informes d'alta mèdics reals amb paranys normatius (tractaments suspesos, diagnòstics de sospita, empat de dues malalties concurrents, complicacions nosocomials amb POA N i aplicació de la regla del VIH).
2. **Observació Competencial (OC — 30 % de la nota de fita):**  
   * Avaluació del dossier d'exercicis i resolució de queries d'auditoria mitjançant la matriu C1-C6 (especial atenció a C1 Rigor tècnic i C3 Seguretat de la dada clínica).

---

## 11 · Relacions del Graf (Enllaços interns)

- **[00_MP1519_MOC.md](./00_MP1519_MOC.md)** — Node arrel i mapa general del mòdul.
- **[01_MP1519_Cataleg_Curricular.md](./01_MP1519_Cataleg_Curricular.md)** — Criteris d'Avaluació oficials dels RAs 5 i 6.
- **[02_MP1519_Protocol_Avaluacio.md](./02_MP1519_Protocol_Avaluacio.md)** — Regles d'avaluació de la Fita 3 i fórmules QRA.
- **[04_MP1519_Fitxa_AEA_2.md](./04_MP1519_Fitxa_AEA_2.md)** — Unitat anterior: Arquitectura de la CIE-10-ES Diagnòstics.
- **[06_MP1519_Fitxa_AEA_4.md](./06_MP1519_Fitxa_AEA_4.md)** — Següent unitat: Procediments PCS i Causes Externes.
- **[08_MP1519_Paquet_LLM.md](./08_MP1519_Paquet_LLM.md)** — Operador d'IA amb el blindatge anti-al·lucinació de la Secció 8 i els 10 Falsos Amics.
```
