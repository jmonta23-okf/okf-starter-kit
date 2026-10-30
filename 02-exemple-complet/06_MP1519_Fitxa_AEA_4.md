---
id: MP1519-AEA-04
type: FitxaAEA
title: "Fitxa AEA 4: Arquitectura de Procediments (PCS), Traumatismes i Causes Externes"
subtitle: "Desplegament d'aula: estructura multiaxial de 7 caràcters, 31 operacions arrel, tècniques implícites, traumatismes i intoxicacions vs. RAM (Setmanes 23 a 27 i 32)"
cycle: "CFGS Documentació i Administració Sanitàries (SAD)"
center: "Centre educatiu de referència"
academic_year: "2026-2027"
version: "V2.0-Complet"
data_ultima_actualitzacio: "2026-10-29"
authors:
  - "Josep Montañà Piqué"
legal_framework: "Ordre EDU/10/2020 i RD 768/2014 (LOE)"
credit: "MP1519"
durada: "12 h"
resultats_aprenentatge:
  - "RA7"
  - "RA8"
criteris_avaluacio:
  - "7a"
  - "7b"
  - "7c"
  - "7d"
  - "7e"
  - "7f"
  - "7e*"
  - "8a"
  - "8b"
  - "8c"
  - "8d"
  - "8e"
  - "8f"
  - "8g"
tags:
  - okf/aea
  - okf/sanitat
  - mp1519/aea4
estat: vigent
---

# Fitxa AEA 4: Arquitectura de Procediments (PCS), Traumatismes i Causes Externes

> **Propòsit.** Aquesta unitat d'aprenentatge canvia el model mental de l'alumnat: en procediments quirúrgics no busquem codis a un diccionari, **els construïm eix a eix**. L'alumnat aprèn l'arquitectura multiaxial de 7 caràcters de la CIE-10-PCS, tradueix l'argot dels cirurgians a les 31 Operacions Arrel oficials, aplica les regles de tècniques implícites (B3.1b), convertides (B3.2) i incompletes (B3.3), i domina la patologia d'urgències: el setè caràcter temporal en fractures, l'efecte mirall en causes externes (V-Y) i la seqüenciació oposada entre intoxicacions i reaccions adverses a medicaments (RAM).

---

## 1 · Dades Generals i Context d'Aula

| Camp | Valor |
|:---|:---|
| **Activitat** | AEA 4 — Arquitectura de Procediments (PCS), Traumatismes i Causes Externes |
| **Temporització** | Setmanes 23 a 27 + Setmana 32 (Tercer trimestre) |
| **Durada** | 12 hores presencials (6 sessions de 2 hores) |
| **Resultats d'Aprenentatge** | RA7 (Codificació de procediments PCS) i RA8 (Codificació específica d'urgències) |
| **Pes curricular conjunt** | **24 % de la qualificació final del mòdul** (RA7: 12 % + RA8: 12 %) |
| **Espai lectiu** | Aula d'Informàtica (amb desdoblament de grup i taules de la Secció 0 d'eCIEMaps) |
| **Fita avaluativa** | **Fita 4** (Setmana 27): Prova Escrita PE4 + Avaluació Competencial OC |
| **Recuperació** | Setmana 32: Taller integrador i recuperació contínua integrada dels RA7 i RA8 |

---

## 2 · Criteris d'Avaluació Mobilitzats

Aquesta AEA mobilitza 14 Criteris d'Avaluació oficials del [Catàleg Curricular](./01_MP1519_Cataleg_Curricular.md), amb 7 criteris nuclears de Nivell A:

* **RA7 (12 % · 7 h):**
  * 🔴 **7.1 (7a):** Construcció multiaxial de codis de 7 caràcters a la Secció 0 (Mèdico-Quirúrgica).
  * 🔴 **7.2 (7b):** Aplicació estricta de la Regla de la Mateixa Fila a les taules PCS.
  * 🔴 **7.3 (7c):** Distinció entre operacions arrel: Escissió (B) vs. Resecció (T) vs. Extracció (D).
  * 🔴 **7.4 (7d):** Aplicació de la norma B3.1b: prohibició de codificar tècniques implícites (accessos, sutures).
  * 🟡 **7.5 (7e):** Codificació de procediments convertits (laparoscòpia a obert) amb doble codi.
  * 🟡 **7.6 (7f):** Codificació de biòpsies diagnòstiques mitjançant el qualificador X.
  * 🟢 **7e\***: Consulta de denominacions d'operacions arrel en llengua anglesa instrumental(\*).
* **RA8 (12 % · 7 h):**
  * 🔴 **8.1 (8a):** Assignació del 7è caràcter temporal en fractures i lesions (A inicial, D subsegüent, S seqüela).
  * 🟡 **8.2 (8b):** Codificació de TCE vinculant la pèrdua de consciència i l'escala de Glasgow (`R40.24-`).
  * 🟡 **8.3 (8c):** Construcció de la seqüència de causes externes (mecanisme + lloc Y92 + activitat Y93 + estatus Y99).
  * 🔴 **8.4 (8d):** Aplicació de l'efecte mirall: coincidència del 7è caràcter de la causa amb el de la lesió.
  * 🟡 **8.5 (8e):** Diferenciació de seqüenciació entre intoxicació (codi T a DP) i RAM (manifestació a DP).
  * 🟡 **8.6 (8f):** Vinculació obligatòria de complicacions de cures (T80-T88) amb causa externa (Y83-Y84).
  * 🔴 **8.7 (8g):** Prohibició d'assignar codis Z38 com a DP en nadons al Sistema Nacional de Salut.

---

## 3 · Continguts Teòrics Nuclears

### 3.1 · El canvi de xip: La CIE-10-PCS no es busca, es construeix
A diferència de la classificació de malalties, el sistema **CIE-10-PCS** (*Procedure Coding System*) és un llenguatge formal multiaxial. L'Índex Alfabètic de Procediments (IAP) no conté codis complets: només serveix per identificar quina **Taula de 7 caràcters** cal obrir.

* **Normes generals B1.1 i B1.3:** Tots els codis tenen **exactament 7 caràcters alfanumèrics**.
* **Lletres prohibides:** Les lletres **`I`** i **`O`** mai s'utilitzen al PCS per evitar confusions visuals amb els números `1` i `0`.
* **Estructura multiaxial de la Secció 0 (Mèdico-Quirúrgica):**

| Posició | Eix de classificació | Significat clínic | Valors habituals |
|:---:|:---|:---|:---|
| **1** | **Secció** | Àmbit general del procediment | `0` = Mèdico-Quirúrgica |
| **2** | **Sistema orgànic** | Regió corporal o aparell | `D` Aparell digestiu, `T` Urinari, `F` Hepatobiliar... |
| **3** | **Operació Arrel** | Objectiu clínic fonamental de l'acte | Una de les 31 Operacions Arrel (`B`, `T`, `D`, `J`...) |
| **4** | **Localització anatòmica** | Òrgan o estructura concreta | `T` Vesícula biliar, `J` Apèndix... |
| **5** | **Abordatge** | Via d'accés utilitzada pel cirurgià | `0` Obert, `4` Percutani endoscòpic, `8` Orifici natural endoscòpic... |
| **6** | **Dispositiu** | Material que es deixa implantat | `Z` Cap dispositiu, `J` Empelt sintètic... |
| **7** | **Qualificador** | Finalitat addicional o especificitat | `X` Diagnòstic (biòpsia), `Z` Cap qualificador |

> ⚠️ **La Regla de la Mateixa Fila (Inviolable):**  
> Dins d'una taula de la CIE-10-PCS, un cop escollits els caràcters 1, 2 i 3 (capçalera de la taula), **els caràcters 4t, 5è, 6è i 7è s'han d'escollir obligatòriament de la MATEIXA FILA HORITZONTAL**. Està terminantment prohibit combinar un abordatge d'una fila amb una localització anatòmica d'una altra fila.

---

### 3.2 · Les 31 Operacions Arrel: La clau del tercer caràcter
El documentalista ha de traduir el text narratiu de l'informe quirúrgic a una de les 31 Operacions Arrel estandarditzades. Es divideixen en 4 grans famílies lògiques:

#### Família 1: Accions per extirpar o prendre part o la totalitat d'un teixit
* **Escissió (`B`):** Tallar per extirpar una porció (un tros) d'una estructura corporal sense substitució (ex: biòpsia hepàtica, resecció d'un pòlip de còlon, quadrantectomia de mama).
* **Resecció (`T`):** Tallar per extirpar la **totalitat** d'una estructura anatòmica completa (ex: apendicectomia, colecistectomia total, mastectomia radical, nefrectomia total).
* **Extracció (`D`):** Treure o desprendre una substància o estructura arrencant o estirant sense tallar (ex: aspiració de moll d'os, extirpació d'ungla, part instrumentalitzat).
* **Destrucció (`5`):** Erradicació física total o parcial d'una estructura sense extirpar-la (ex: cauterització de verruga, fulguració d'úlcera, crioteràpia de pòlip).
* **Amputació (`6`):** Separar una extremitat del cos (ex: amputació infracondília de cama). ⚠️ No confondre amb Alteració (`0`).

#### Família 2: Accions sobre diàmetres i tubulars
* **Dilatació (`7`):** Eixamplar un orifici o llum d'un òrgan tubular (ex: angioplàstia coronària amb baló).
* **Oclusió (`L`):** Tancar completament la llum d'un òrgan tubular (ex: lligadura de trompes de Fal·lopi).
* **Restricció (`V`):** Estrenyiment parcial d'un orifici o llum tubular (ex: cerclatge cervical).

#### Família 3: Accions sobre cossos o càlculs
* **Extirpació (`C`):** Treure un cos estrany o càlcul sense tallar ni perforar l'òrgan (ex: retirada de pròtesi, extracció de cos estrany corneal).
* **Fragmentació (`F`):** Trencar un càlcul o material sòlid en fragments menors (ex: litotrípsia per ultrasons de càlcul renal).

#### Família 4: Exploració i Reparació
* **Inspecció (`J`):** Exploració visual o manual d'una regió corporal (ex: laparoscòpia exploradora, gastroscòpia diagnòstica).
* **Reparació (`Q`):** Retornar una estructura al seu estat funcional normal quan no aplica cap altra operació arrel (ex: sutura de ferida superficial, hèrnia sense malla).

---

### 3.3 · Normes Crítiques de Quiròfan

* **Norma B3.1b (Tècniques Implícites):** Els passos preparatoris, les vies d'accés necessàries per visualitzar el camp operatori i el tancament per plànols **no es codifiquen mai per separat**.
  * *Exemple:* A una *«Laparotomia exploradora, apendicectomia i sutura de paret abdominal»*, la incisió i la sutura són tècniques implícites. **Només es codifica la Resecció d'apèndix** (`0DTJ0ZZ` o `0DTJ4ZZ`).
* **Norma B3.2 (Procediments Convertits):** Quan una intervenció s'inicia per via percutània o endoscòpica però per complicacions s'ha de reconvertir a cirurgia oberta, **es codifiquen obligatòriament 2 codis**:
  1. La **Inspecció** per via endoscòpica (`J`).
  2. L'**Operació Arrel definitiva** per via oberta (`0`).
* **Norma B3.3 (Procediments Incomplets):** Si una cirurgia se suspèn abans d'assolir l'objectiu arrel, es codifica exclusivament l'abast assolit; si només s'ha obert i mirat, **es degrada a Inspecció (`J`)**.
* **La Biòpsia (Qualificador X):** La biòpsia no és una operació arrel. Es codifica com a **Escissió (`B`)** o **Extracció (`D`)** amb el 7è caràcter **`X` (Diagnòstic)**. Si en la mateixa sessió es practica una biòpsia i posteriorment la resecció total de l'òrgan, es codifiquen ambdós procediments (Norma B3.4b).

---

## 4 · Patologia d'Urgències: Traumatismes i Causes Externes

### 4.1 · El setè caràcter temporal en lesions (Capítol 19, codis S i T)
Tota lesió traumàtica requereix especificar la fase evolutiva de l'atenció:
* **`A` (Contacte inicial):** El pacient està rebent el tractament actiu per a la lesió (ingrés d'urgències, cirurgia, col·locació de guix).
* **`D` (Contacte subsegüent):** Visites posteriors durant la fase de curació o consolidació (canvi de guix, retirada de material de sutura, rehabilitació).
* **`S` (Seqüela):** Efecte tardà o complicació permanent que sorgeix un cop la lesió primària ja ha consolidat (ex: coixesa per fractura antiga). Requereix codi de la seqüela de DP + codi de la lesió original amb `S` de DS.

### 4.2 · Causes Externes de Morbiditat (Capítol 20, codis V a Y)
Permeten descriure les circumstàncies de l'accident o agressió. L'ordre de seqüenciació és:
$$\text{Mecanisme causal (V00-X58)} \longrightarrow \text{Lloc de l'esdeveniment (Y92)} \longrightarrow \text{Activitat (Y93)} \longrightarrow \text{Estat laboral (Y99)}$$

> ⚠️ **La Regla de l'Efecte Mirall:**  
> El 7è caràcter de la Causa Externa **ha de coincidir obligatòriament** amb el 7è caràcter de la lesió principal que ha provocat (si la fractura porta `A`, la caiguda porta `A`).

> 🛑 **Prohibicions absolutes en Causes Externes:**
> 1. Els codis de lloc (Y92), activitat (Y93) i estat (Y99) **MAI s'apliquen** a intoxicacions, reaccions adverses a medicaments (RAM) ni complicacions de cures mèdiques.
> 2. Els codis residuals de lloc no especificat (`Y92.9`) o activitat no especificada (`Y93.9`) estan **prohibits** a l'auditoria RAE-CMBD (generen rebuig per manca de qualitat).

### 4.3 · El gran dilema: Intoxicació vs. Reacció Adversa a Medicaments (RAM)

| Criteri d'auditoria | Intoxicació (Enverinament) | Reacció Adversa a Medicament (RAM) |
|:---|:---|:---|
| **Definició clínica** | Fàrmac pres de manera incorrecta: sobredosi, error de pauta, ingesta accidental, interacció no pautada o autolesió. | Fàrmac administrat a la dosi correcta i seguint la prescripció mèdica que provoca un efecte nociu imprevist. |
| **Columna de la Taula de Fàrmacs** | Columnes 1 a 4 (Accidental, Autolesió, Agressió, Indeterminat). | **Columna 5** (*Efecto adverso*). |
| **Diagnòstic Principal (DP)** | **El codi T del fàrmac** (ex: `T39.1X1A`). | **La manifestació clínica** (ex: *Hepatotoxicitat* `K71.9`). |
| **Diagnòstic Secundari (DS)** | La manifestació clínica o el símptoma produït. | **El codi T del fàrmac amb 5è caràcter 5** (ex: `T39.1X5A`). |
| **Causes externes (Y92/Y93)** | **PROHIBIDES**. | **PROHIBIDES**. |

---

## 5 · Casos Clínics Oberts (ABP)

### Cas Obert 6 · El tub espatllat i l'excés de zel quirúrgic
* **Escenari:** Un pacient ingressa per a la reparació programada d'una hèrnia inguinal dreta i una colonoscòpia amb extirpació de pòlip de còlon descendent. A quiròfan, el cirurgià introdueix el colonoscopi, però abans de visualitzar el pòlip, el sistema de vídeo de la torre endoscòpica s'avaria i la colonoscòpia s'ha de suspendre. Tot seguit, es practica la reparació oberta de l'hèrnia inguinal dreta amb incisió, col·locació de malla de polipropilè i sutura de paret per plànols.
* **El dilema de l'auditor:** Un documentalista principiant pretén facturar 4 procediments: *1. Escissió de pòlip colònic, 2. Incisió quirúrgica, 3. Reparació d'hèrnia amb malla, 4. Sutura cutània*.
* **Resolució guiada (Normes B3.1b i B3.3):**
  1. La incisió i la sutura són **tècniques implícites** (Norma B3.1b): prohibit codificar-les a part.
  2. L'extirpació del pòlip no es va arribar a realitzar. Per la Norma B3.3 (procediment incomplet), la colonoscòpia frustrada **es degrada a Inspecció endoscòpica d'intestí gros inferior** (`0DJD8ZZ`).
  3. L'hèrnia amb malla es codifica com a **Suplement d'hèrnia inguinal dreta amb teixit sintètic** (`0YU50JZ`).
  4. **Codis finals validats:** `0YU50JZ` (procediment principal) + `0DJD8ZZ` (procediment secundari).

### Cas Obert 7 · La trampa de la laminectomia descompressiva
* **Escenari:** Informe quirúrgic: *«Laminectomia descompressiva de vèrtebra lumbar L4 per alliberar arrel nerviosa comprimida per hèrnia discal.»* El codificador busca a l'índex «Laminectomia» i troba la taula `0QB0` (Excisió d'os lumbar). Considera el cas tancat amb aquest únic codi. L'auditor en cap rebutja l'expedient per omissió del procediment fonamental.
* **Resolució guiada (Norma B3.18 - Codificació Múltiple):**
  * La laminectomia (treure el tros d'os de la làmina vertebral) és l'accés físic per aconseguir l'objectiu terapèutic real: desatapar i alliberar el nervi espinal atrapat. Com que ambdós actes tenen objectius arrel diferents i afecten estructures anatòmiques diferents (nervi vs. os), **cal assignar codificació múltiple obligatòria**:
  1. **Alliberament d'arrel nerviosa raquídia lumbar per via oberta:** Operació Arrel Alliberament (`01N90ZZ`).
  2. **Excisió de vèrtebra lumbar per via oberta:** Operació Arrel Escissió (`0QB00ZZ`).

### Cas Obert 8 · El Paracetamol: Dues històries idèntiques?
* **Escenari:**
  * **Pacient A:** Ingressa a Urgències en coma i amb fracàs hepàtic fulminant després d'haver ingerit voluntàriament 20 pastilles de Paracetamol de 1 g amb intenció autolítica.
  * **Pacient B:** Ingressa a Digestologia per insuficiència hepàtica aguda apareguda després de prendre durant tres dies la dosi prescrita pel seu metge (1 g cada 8 hores) per a una odontàlgia.
* **El dilema de l'auditor:** Mateix fàrmac, mateix òrgan diana danyat. Es codifiquen igual?
* **Resolució guiada (Diferenciació Intoxicació vs. RAM):**
  * **Pacient A (INTOXICACIÓ PER AUTOLESIÓ):**
    * **DP:** Enverinament per analgèsics no opioides (Paracetamol), autolesió intencionada, contacte inicial (**`T39.1X2A`**).
    * **DS:** Insuficiència hepàtica aguda (`K72.00`).
    * *Causes externes (lloc/activitat):* **PROHIBIDES**.
  * **Pacient B (REACCIÓ ADVERSA A DOSI TERAPÈUTICA - RAM):**
    * **DP:** Insuficiència hepàtica aguda induïda per fàrmacs (**`K72.00`**).
    * **DS:** Efecte advers de paracetamol, contacte inicial (**`T39.1X5A`**).
    * *Causes externes (lloc/activitat):* **PROHIBIDES**.

---

## 6 · Bateria d'Activitats d'Aula i Exercicis de Quiròfan

### Activitat 4.1 · Traducció a Operacions Arrel de la CIE-10-PCS
Identifica l'Operació Arrel normativa per a cadascuna de les següents descripcions quirúrgiques:
1. `«Lobectomia superior dreta pulmonar per carcinoma.»` $\rightarrow$ **Escissió (`B`)** *(és una porció del pulmó total).*
2. `«Pneumonectomia total esquerra.»` $\rightarrow$ **Resecció (`T`)** *(és l'òrgan complet).*
3. `«Artroscòpia de genoll amb aspiració de líquid sinovial.»` $\rightarrow$ **Extracció (`D`)** *(estirar líquid sense tallar).*
4. `«Fulguració per radiofreqüència de pòlips vaginals.»` $\rightarrow$ **Destrucció (`5`)** *(erradicació sense extirpació).*
5. `«Colecistectomia total laparoscòpica.»` $\rightarrow$ **Resecció (`T`)**.

### Activitat 4.2 · Auditoria de Procediments Convertits
Cirurgià descriu: *«Iniciem colecistectomia laparoscòpica. Davant la presència d'adherències massives que impedeixen el control hemostàtic, es reconverteix a laparotomia oberta subcostal dreta, completant l'extirpació total de la vesícula.»*
* **Auditoria:** S'assignen dos codis obligatoris:
  1. `0FT40ZZ`: Resecció de vesícula biliar per via oberta (procediment final).
  2. `0FJ44ZZ`: Inspecció d'arbre biliar per via percutània endoscòpica (la laparoscòpia convertida).

### Activitat 4.3 · Fractura i Causa Externa amb Efecte Mirall
Pacient de 42 anys arriba a Urgències amb fractura diafisària de fèmur dret tancada després de caure d'una bastida mentre treballava a la construcció d'un edifici.
1. Codi de la fractura (Contacte inicial): **`S72.301A`** (requereix 7è caràcter `A`).
2. Causa externa - Mecanisme: Caiguda des de bastida $\rightarrow$ `W12.XXXA` (observa l'**efecte mirall** amb la lletra `A`).
3. Causa externa - Lloc: Construcció d'edifici $\rightarrow$ `Y92.61`.
4. Causa externa - Activitat: Treball a la construcció $\rightarrow$ `Y93.H1`.
5. Causa externa - Estat: Treball remunerat $\rightarrow$ `Y99.0`.

---

## 7 · Prompts per a NotebookLM (Quadern de Normativa)

Prompts d'auditoria per executar sobre el *Manual de Procedimientos* (Secció 0) i el Capítol A de la 6a edició de la CIE-10-ES carregat al Quadern:

* **Prompt 4.1 (Tècniques implícites B3.1b):**  
  > *«Actua com un auditor del CMBD d'un hospital quirúrgic. Et passo aquesta narració: 'Laparotomia exploradora, alliberament d'adherències intestinals, hemostàsia meticulosa i tancament de paret amb sutura contínua de monofilament'. D'acord amb la norma B3.1b sobre tècniques implícites de la CIE-10-PCS (6a edició, 2026), quins passos han de ser descartats i quin procediment s'ha de facturar com a Operació Arrel final? Cita la taula de procediments aplicable.»*
* **Prompt 4.2 (Intoxicació versus Efecte Advers):**  
  > *«Actua com un supervisor de codificació d'urgències. Elabora una guia ràpida per a nous documentalistes que aclareixi la regla d'or de la seqüenciació oposada entre intoxicacions i reaccions adverses a medicaments (RAM). Explica per quina raó està terminantment prohibit assignar codis de lloc (Y92) o activitat (Y93) en una intoxicació medicamentosa.»*

---

## 8 · Seqüenciació Minutada de les 6 Sessions (12 hores)

```
Sessió 1 (Setm. 23 · 2h): La lògica multiaxial de la CIE-10-PCS, Secció 0 i la Regla de la Mateixa Fila.
Sessió 2 (Setm. 24 · 2h): Les Operacions Arrel d'extirpació (Escissió B, Resecció T, Extracció D, Amputació 6).
Sessió 3 (Setm. 25 · 2h): Normes de quiròfan: tècniques implícites (B3.1b), convertits (B3.2) i Cas Obert 6.
Sessió 4 (Setm. 26 · 2h): Codificació múltiple de procediments, biòpsies diagnòstiques (X) i Cas Obert 7.
Sessió 5 (Setm. 27 · 2h): Patologia d'Urgències: fractures, Glasgow, causes externes, Fals Amic #6 i Fita 4 (PE4).
Sessió 6 (Setm. 32 · 2h): Taller de resolució Intoxicacions vs. RAM (Cas Obert 8) i recuperació contínua RA7-RA8.
```

---

## 9 · Avaluació de la Fita 4 (Setmana 27)

L'AEA 4 s'avalua a la Setmana 27 mitjançant:

1. **Prova Escrita Competencial (PE4 — 70 % de la nota de fita):**  
   * Examen individual *Open Book* d'auditoria quirúrgica mitjançant eCIEMaps.
   * Construcció multiaxial de 5 procediments de quiròfan a partir de protocols operatoris reals (aplicant B3.1b i conversió) + codificació de 2 casos d'urgències (traumatisme amb causa externa i intoxicació vs. RAM).
2. **Observació Competencial (OC — 30 % de la nota de fita):**  
   * Avaluació del dossier d'exercicis de procediments PCS i aplicació de la matriu C1-C6 (destacant C1 Rigor tècnic a la regla de la mateixa fila i C2 Autonomia en la selecció de l'operació arrel).

---

## 10 · Relacions del Graf (Enllaços interns)

- **[00_MP1519_MOC.md](./00_MP1519_MOC.md)** — Node arrel i mapa general del mòdul.
- **[01_MP1519_Cataleg_Curricular.md](./01_MP1519_Cataleg_Curricular.md)** — Criteris d'Avaluació oficials dels RAs 7 i 8.
- **[02_MP1519_Protocol_Avaluacio.md](./02_MP1519_Protocol_Avaluacio.md)** — Regles d'avaluació de la Fita 4 i fórmules de ponderació.
- **[05_MP1519_Fitxa_AEA_3.md](./05_MP1519_Fitxa_AEA_3.md)** — Unitat anterior: Normativa General de Diagnòstics i POA.
- **[07_MP1519_Fitxa_AEA_5.md](./07_MP1519_Fitxa_AEA_5.md)** — Següent unitat: Projecte Integrador d'Auditoria d'Expedients Sanitaris.
- **[08_MP1519_Paquet_LLM.md](./08_MP1519_Paquet_LLM.md)** — Operador d'IA amb el blindatge anti-al·lucinació de la Secció 8 (Falsos Amics 3, 4 i 6).
```
