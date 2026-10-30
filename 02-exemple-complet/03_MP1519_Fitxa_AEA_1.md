---
id: MP1519-AEA-01
type: FitxaAEA
title: "Fitxa AEA 1: El Sistema d'Informació Sanitari i l'estandardització de la dada clínica"
subtitle: "Desplegament d'aula: DIKW, CMBD, GRD, SNOMED CT vs. CIM-10-ES i l'art del mapeig (Setmanes 1 a 4)"
cycle: "CFGS Documentació i Administració Sanitàries (SAD)"
center: "Centre educatiu de referència"
academic_year: "2026-2027"
version: "V2.0-Complet"
data_ultima_actualitzacio: "2026-10-29"
authors:
  - "Josep Montañà Piqué"
legal_framework: "Ordre EDU/10/2020 i RD 768/2014 (LOE)"
credit: "MP1519"
durada: "8 h"
resultats_aprenentatge:
  - "RA1"
  - "RA2"
criteris_avaluacio:
  - "1a"
  - "1b"
  - "1c"
  - "1d"
  - "1e"
  - "1f"
  - "2a"
  - "2b"
  - "2c"
  - "2d"
  - "2e"
  - "2f"
tags:
  - okf/aea
  - okf/sanitat
  - mp1519/aea1
estat: vigent
---

# Fitxa AEA 1: El Sistema d'Informació Sanitari i l'estandardització de la dada clínica

> **Propòsit.** Aquesta unitat d'aprenentatge estableix els fonaments de la professió de documentalista clínic: comprendre que darrere de cada dada mèdica hi ha un impacte assistencial, jurídic i financer. L'alumnat aprèn a diferenciar dades clíniques i administratives, a entendre com el CMBD nodreix el finançament hospitalari via GRD i a dominar el pas del llenguatge natural mèdic a terminologies (SNOMED CT) i classificacions (CIM-10-ES) mitjançant el mapeig.

---

## 1 · Dades Generals i Context d'Aula

| Camp | Valor |
|:---|:---|
| **Activitat** | AEA 1 — El SIS i l'estandardització de la dada clínica |
| **Temporització** | Setmanes 1 a 4 (Primer trimestre) |
| **Durada** | 8 hores presencials (4 sessions de 2 hores) |
| **Resultats d'Aprenentatge** | RA1 (Caracterització del SIS) i RA2 (Maneig de classificacions) |
| **Espai lectiu** | Aula d'Informàtica (amb desdoblament de grup per ràtio reduïda) |
| **Fita avaluativa** | **Fita 1** (Setmana 4): Prova Escrita PE1 + Avaluació Competencial OC |

---

## 2 · Criteris d'Avaluació Mobilitzats

Aquesta AEA mobilitza la totalitat dels CAs dels dos primers Resultats d'Aprenentatge del [Catàleg Curricular](./01_MP1519_Cataleg_Curricular.md), amb especial incidència en els criteris nuclears de Nivell A:

* **RA1 (8 % · 5 h):**
  * 🔴 **1.1 (1a):** Utilitat del SIS per a ciutadans, clínics i gestors.
  * 🔴 **1.2 (1b):** Classificació de dades en clíniques, administratives i econòmiques.
  * 🟡 **1.3 (1c):** Circuits d'informació i fluxos intercentres.
  * 🔴 **1.4 (1d):** Estructura i finalitat del CMBD (RAE-CMBD a Catalunya).
  * 🟡 **1.5 (1e):** Relació entre informe d'alta, codificació, GRD i facturació a CatSalut.
  * 🔴 **1.6 (1f):** Jerarquia de la dada a la informació i al coneixement (Piràmide DIKW).
* **RA2 (8 % · 5 h):**
  * 🔴 **2.1 (2a):** Problemes de dispersió i fragmentació del llenguatge natural.
  * 🟡 **2.2 (2b):** Llenguatges documentals i normalització mèdica.
  * 🔴 **2.3 (2c):** Diferenciació entre terminologia (SNOMED CT) i classificació (CIM-10-ES).
  * 🔴 **2.4 (2d):** Processos de mapatge (mapping) 1:1, 1:N i N:1.
  * 🟡 **2.5 (2e):** Estructura de la CIAP-2 (primària) i CIE-O-3 (oncologia).
  * 🟢 **2.6 (2f):** Evolució històrica de la CIE-9 a la CIE-10.

---

## 3 · Continguts Teòrics Nuclears

### 3.1 · De la dada al coneixement: La piràmide DIKW
A la gestió hospitalària, la informació s'estructura en una jerarquia ascendent:
* **Dada (Data):** Un valor mínim aïllat sense context ni unitats que no permet prendre cap decisió (ex: `145`, `Positiu`).
* **Informació:** Una dada dotada de context, paràmetres i propòsit (ex: *«Troponines I d'alta sensibilitat en sèrum: 145 ng/L a les 03:00 h»*).
* **Coneixement:** Informació processada, comparada amb patrons clínics i experiència mèdica que permet l'acció terapèutica (ex: *«La pacient presenta una síndrome coronària aguda amb elevació enzimàtica: cal activar el Codi Infart»*).

> ⚠️ **La dada òrfena:** Una dada clínica, per exacta que sigui, es converteix en una dada òrfena si no està vinculada a les dades administratives d'identificació (Número d'Història Clínica - NHC i número d'episodi). Una dada òrfena és nul·la a efectes legals, estadístics i de facturació.

### 3.2 · El Sistema d'Informació Sanitari (SIS) i tipologia de dades
Segons l'OMS, el SIS és el mecanisme integral per recollir, processar, analitzar i transmetre la informació necessària per a la planificació i gestió sanitària. Les dades que hi conviuen es divideixen en:
1. **Dades clíniques:** Descriuen l'estat del pacient i l'assistència (símptomes, diagnòstics, procediments quirúrgics, analítiques).
2. **Dades administratives:** Aporten la identitat jurídica i temporal (edat, sexe, municipi, CIP, data i hora d'ingrés/alta, motiu de l'alta).
3. **Dades econòmiques:** Reflecteixen el cost i el reemborsament del procés, calculades a partir de les dues anteriors.

### 3.3 · El CMBD i el finançament hospitalari per GRD
El **Conjunt Mínim Bàsic de Dades (CMBD)** —a Catalunya gestionat sota el **RAE-CMBD**— és el registre oficial que recull les dades clíniques i administratives de cada alta hospitalària, cirurgia major ambulatòria (CMA) i hospital de dia.

> ⚠️ **Alerta d'auditoria:** El CMBD és exclusiu de l'**Atenció Especialitzada**. L'Atenció Primària disposa de sistemes propis (com l'**eCAP**) i no alimenta el registre del CMBD.

**El circuit clinicofinancer:**
$$\text{Informe d'alta} \xrightarrow{\text{Codificació del documentalista}} \text{Dades al CMBD} \xrightarrow{\text{Software agrupador}} \text{GRD} \xrightarrow{\text{Pes econòmic}} \text{Facturació a CatSalut}$$

Si el documentalista comet una errada d'omissió i no codifica una complicació o comorbiditat greu com a Diagnòstic Secundari (DS), el programari assigna un **Grup Relacionat pel Diagnòstic (GRD)** de menor complexitat (sense severitat). Com a conseqüència, el centre sanitari pot deixar d'ingressar milers d'euros per una atenció que sí que va dispensar.

### 3.4 · El problema del llenguatge natural
El text lliure utilitzat pels metges a les notes clíniques genera una enorme dispersió semàntica. Expressions com *«atac de cor»*, *«infart agut de miocardi»*, *«síndrome coronària»* o *«IAMSEST»* descriuen la mateixa realitat bàsica, però per a un ordinador són cadenes de text independents. Sense normalització, és impossible agregar dades epidemiològiques ni comparar l'activitat entre hospitals.

### 3.5 · Terminologies vs. Classificacions
Per normalitzar el llenguatge sanitari s'utilitzen dos instruments complementaris:

| Criteri comparatiu | Terminologies clíniques (SNOMED CT) | Classificacions internacionals (CIM-10-ES) |
|:---|:---|:---|
| **Propòsit fonamental** | Descriure la realitat clínica amb el màxim detall. | Agrupar i categoritzar la informació en calaixos estadístics. |
| **Àmbit d'ús principal** | El metge i la infermera a temps real (Història Clínica). | L'auditor documentalista, la gestió i la salut pública. |
| **Granularitat** | Infinita (desenes de milers de conceptes atòmics). | Finita i estructurada (categories i subcategories). |
| **Comportament de la dada** | Obre el ventall a combinacions lliures. | Agrupa i redueix el detall per permetre l'anàlisi. |

*Altres classificacions d'ús obligatori:*
* **CIAP-2 (Classificació Internacional de l'Atenció Primària):** Estructurada en 17 capítols. Permet classificar simultàniament la raó de consulta, el problema de salut atès i la intervenció del metge de família.
* **CIE-O-3 (Oncologia):** Classificació en dues dimensions: **Topografia** (òrgan afectat, codi de 3 caràcters) i **Morfologia** (histologia i comportament cel·lular, codi de 5 caràcters on el 5è dígit defineix la conducta: `/0` benigne, `/1` incert, `/2` *in situ*, `/3` maligne primari, `/6` metàstasi).

### 3.6 · L'art del mapeig (Mapping)
El mapeig és la traducció controlada entre terminologies (SNOMED CT) i la classificació oficial (CIM-10-ES):
* **Mapeig 1:1:** Un concepte SNOMED correspon exactament a una categoria CIM (ex: *Apendicitis aguda* $\rightarrow$ `K35`).
* **Mapeig 1:N:** Un sol concepte clínic requereix diversos codis CIM per expressar etiologia i manifestació.
* **Mapeig N:1:** Diversos conceptes descriptius diferents es condensen en un únic calaix de classificació.

> ⚠️ **El mite del mapeig automàtic:** Un ordinador no pot codificar de manera autònoma sense supervisió humana perquè desconeix les normes de seqüenciació (*«Excluye 1»*, *«Codifique primero»* o la selecció del Diagnòstic Principal). Aquesta decisió d'auditoria és la que fonamenta la professió del Tècnic en Documentació Sanitària.

---

## 4 · Casos Clínics Oberts (ABP)

### Cas Obert 1 · El problema del Dr. Vidal i la dada òrfena
* **Escenari:** A les 04:15 h, el Dr. Vidal atén a Urgències una pacient que arriba en ambulància amb dolor toràcic opressiu. Redacta a mà a la seva evolució: *«Dona de 68 anys. TA 175/95 mmHg, pols 110 bpm. Troponines I d'alta sensibilitat: 180 ng/L. Electrocardiograma amb descens del segment ST a derivacions V4-V6. S'administra doble antiagregació i es trasllada a UCI.»* L'endemà, el sistema informàtic hospitalari rebutja la càrrega del registre per a l'auditoria del RAE-CMBD.
* **Resolució guiada:** La informació clínica és d'una gran precisió tècnica, però és incapaç de vincular-se a una identitat legal i temporal: falten el **Número d'Història Clínica (NHC)** o CIP de la pacient i el **número d'episodi d'admissió**. En absència de dades administratives, la dada clínica es converteix en una **dada òrfena**: és clínicament vàlida a la capçalera del malalt, però legalment i financerament inexistent per al SIS.

### Cas Obert 2 · La torre de Babel hospitalària (SNOMED vs. CIM)
* **Escenari:** A la comissió d'històries clíniques d'un hospital d'alta tecnologia, el cap d'Urgències protesta: *«A la meva pantalla faig servir SNOMED CT i anoto amb tota precisió: 'Dolor precordial intens', 'Irradiació a mandíbula' i 'Diaforesis profusa'. No entenc per què el servei de Documentació Sanitària elimina aquest detall i ho resumeix tot amb el codi R07.9 de la CIM-10-ES.»*
* **Resolució guiada:** Metge i auditor tenen raó en els seus àmbits respectius. El metge necessita la hipergranularitat de SNOMED per al diagnòstic diferencial i la seguretat clínica immediata. El documentalista sanitari necessita la CIM-10-ES per agregar milers de casos en calaixos comparables, assignar el pes mitjà del GRD i permetre que el centre cobri l'assistència al CatSalut. El mapeig és la passarel·la que connecta tots dos mons.

---

## 5 · Bateria d'Activitats d'Aula i Exercicis

### Activitat 1.1 · Diferenciació DIKW a la pràctica clínica
Classifica cadascun dels fragments extrets d'històries clíniques en **Dada (D)**, **Informació (I)** o **Coneixement (C)**:
1. `«Glucèmia basal: 240 mg/dL en dejú.»` $\rightarrow$ **Informació (I)** *(valor amb magnitud i context temporal).*
2. `«Davant la triada de polidípsia, poliúria i pèrdua de pes amb glucèmia de 240 mg/dL, s'inicia pauta d'insulina per Diabetis Mellitus Tipus 1 debutant.»` $\rightarrow$ **Coneixement (C)** *(informació integrada que genera judici clínic).*
3. `«0,85.»` $\rightarrow$ **Dada (D)** *(xifra nua sense context ni unitats).*

### Activitat 1.2 · Tipologia de dades al circuit hospitalari
Un informe d'alta recull: *«Pacient de 52 anys, resident a Terrassa (CIP: PUIM1234567890), ingressat el 10/10/2026 i donat d'alta el 14/10/2026 per Apendicectomia laparoscòpica per apendicitis aguda flegmonosa. Facturació imputada per CatSalut: 3.850 €.»*
* **Dades clíniques:** Apendicitis aguda flegmonosa (diagnòstic), apendicectomia laparoscòpica (procediment).
* **Dades administratives:** Edat (52 anys), residència (Terrassa), CIP, dates d'ingrés i alta (estada: 4 dies).
* **Dades econòmiques:** Facturació imputada (3.850 €), tarifa associada al GRD corresponent.

### Activitat 1.3 · Mapeig de llenguatges documentals
Relaciona cada eina amb la seva definició i cas d'ús:
* **SNOMED CT:** Terminologia clínica de referència per a l'entrada de dades a temps real a l'estació mèdica.
* **CIM-10-ES:** Classificació internacional oficial per al tancament de l'informe d'alta i enviament al CMBD.
* **CIAP-2:** Classificació utilitzada a l'atenció primària orientada al motiu de consulta de l'usuari.
* **CIE-O-3:** Classificació de doble eix (Topografia + Morfologia) per a registres de tumors.

---

## 6 · Prompts per a NotebookLM (Quadern de Normativa)

Prompts que l'alumnat pot executar sobre el Quadern de Normativa carregat exclusivament amb el Capítol A de la 6a edició de la CIE-10-ES:

* **Prompt 1.1 (L'auditor financer i el GRD):**  
  > *«Actua com un auditor financer d'un hospital públic català. Explica de manera senzilla com el procés de codificació que realitza un Tècnic en Documentació Sanitària alimenta el RAE-CMBD i com aquesta informació es transforma en un GRD que permet al centre cobrar els serveis prestats al CatSalut. Basa la teva explicació exclusivament en els principis del Capítol A de la CIE-10-ES.»*
* **Prompt 1.2 (La justificació de la pèrdua de detall):**  
  > *«Actua com un estadístic del Ministeri de Sanitat. Un facultatiu es queixa que la CIM-10-ES 'elimina' la riquesa semàntica de les seves anotacions de SNOMED CT en reduir múltiples símptomes a una sola categoria de diagnòstic. Argumenta per quines raons de salut pública i comparabilitat internacional és imprescindible aquest procés d'agrupació tabular.»*

---

## 7 · Seqüenciació Minutada de les 4 Sessions (8 hores)

```
Sessió 1 (Setmana 1 · 2 h)      Sessió 2 (Setmana 2 · 2 h)      Sessió 3 (Setmana 3 · 2 h)      Sessió 4 (Setmana 4 · 2 h)
┌──────────────────────────┐    ┌──────────────────────────┐    ┌──────────────────────────┐    ┌──────────────────────────┐
│ DIKW i el SIS hospitalari│    │ Normalització i llenguatge│   │ L'art del mapeig clínic  │    │ Tancament i Avaluació    │
│ • Piràmide DIKW (30 min) │    │ • Ambigüitat text (30 min│    │ • Tipus 1:1, 1:N, N:1    │    │ • Resolució dubtes       │
│ • Dades administratives  │    │ • SNOMED vs CIM (40 min) │    │   (45 min)               │    │   (20 min)               │
│   i CMBD (40 min)        │    │ • CIAP-2 i CIE-O-3       │    │ • Cas Obert 2 (30 min)   │    │ • Prova Escrita PE1      │
│ • Cas Obert 1 (30 min)   │    │   (30 min)               │    │ • Taller de mapatge      │    │   Open Book (60 min)     │
│ • Activitat 1.1 (20 min) │    │ • Activitat 1.2 (20 min) │    │   amb eCIEMaps (45 min)  │    │ • Recollida Dossier OC   │
└──────────────────────────┘    └──────────────────────────┘    └──────────────────────────┘    └──────────────────────────┘
```

---

## 8 · Avaluació de la Fita 1 (Setmana 4)

L'assoliment d'aquesta AEA 1 culmina a la Setmana 4 i s'avalua mitjançant:

1. **Prova Escrita Competencial (PE1 — 70 % de la nota de fita):**  
   * Examen individual *Open Book* amb preguntes conceptuals i de raonament sobre el SIS, la piràmide DIKW, el finançament per GRD i exercicis pràctics de mapatge SNOMED $\rightarrow$ CIM.
   * Correcció analítica mitjançant la micro-rúbrica de 2 punts per qüestió (justificació, procés, impacte i vocabulari).
2. **Observació Competencial (OC — 30 % de la nota de fita):**  
   * Avaluació del dossier d'exercicis completat a l'aula d'informàtica mitjançant la matriu C1-C6 (Rigor en el mapatge, autonomia a eCIEMaps, diligència de lliurament i to professional).

---

## 9 · Relacions del Graf (Enllaços interns)

- **[00_MP1519_MOC.md](./00_MP1519_MOC.md)** — Node arrel i mapa general del mòdul.
- **[01_MP1519_Cataleg_Curricular.md](./01_MP1519_Cataleg_Curricular.md)** — Criteris d'Avaluació oficials dels RAs 1 i 2.
- **[02_MP1519_Protocol_Avaluacio.md](./02_MP1519_Protocol_Avaluacio.md)** — Regles d'avaluació de la Fita 1 i rúbrica OC.
- **[04_MP1519_Fitxa_AEA_2.md](./04_MP1519_Fitxa_AEA_2.md)** — Següent unitat: Arquitectura de la CIE-10-ES Diagnòstics.
- **[08_MP1519_Paquet_LLM.md](./08_MP1519_Paquet_LLM.md)** — Operador d'IA per generar exercicis addicionals de mapatge.
```
