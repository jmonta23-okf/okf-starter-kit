# Índex de la Documentació d'OKF Starter Kit

> **Benvingut a la base de coneixement d'OKF Starter Kit.**  
> Una proposta de sistema operatiu per al coneixement docent. Menys burocràcia dispersa, més artesania pedagògica.

**DOI:** [10.5281/zenodo.23823819](https://doi.org/10.5281/zenodo.23823819) · **Repositori:** [github.com/jmonta23-okf/okf-starter-kit](https://github.com/jmonta23-okf/okf-starter-kit)

---

## Per on començar? (Itineraris de lectura)

Tria la ruta que millor s'adapti al teu temps i a les teves necessitats actuals:

* 🚀 **Ruta d'Acció Directa (Vull provar-ho ja · 35 minuts):**  
  Llegeix la introducció a **[01 · Què és OKF?](./01-que-es-okf.md)** (5 min) i salta directament al tutorial pràctic de **[04 · Inici ràpid](./04-inici-rapid.md)** (30 min) per crear i validar el teu primer node.

* 🧭 **Ruta Pedagògica i Humanista (Vull entendre el perquè · 30 minuts):**  
  Comença per **[01 · Què és OKF?](./01-que-es-okf.md)**, aprofundeix en la mirada biològica i ontològica a **[02 · Filosofia](./02-filosofia.md)** i resol dubtes habituals a **[06 · Preguntes freqüents (FAQ)](./06-faq.md)**.

* ⚙️ **Ruta d'Enginyeria i Governança (Vull auditar o adaptar el sistema · 45 minuts):**  
  Analitza el model de 4 capes i la convenció mixta a **[03 · Arquitectura](./03-arquitectura.md)**, consulta el codi font a `03-eines/validar_yaml.py`, i repassa la terminologia precisa a **[05 · Glossari](./05-glossari.md)**.

---

## Mapa complet de la documentació

| Fitxer | Nom del document | Què hi trobaràs? | Temps estimat |
|:---|:---|:---|:---:|
| **`01-que-es-okf.md`** | **[Què és OKF?](./01-que-es-okf.md)** | La doble lectura de les sigles, la tirania de les carpetes convencionals i l'anatomia bàsica d'un node. | 10 min |
| **`02-filosofia.md`** | **[Filosofia](./02-filosofia.md)** | La programació viva, la sobirania docent en text pla, el concepte del taller artesanal (MIAE + VCER) i la proposta de SO. | 15 min |
| **`03-arquitectura.md`** | **[Arquitectura](./03-arquitectura.md)** | El model de 4 capes, la topologia del graf, la convenció YAML mixta (EN/CA), els 15 tipus de nodes i el validador estàtic. | 20 min |
| **`04-inici-rapid.md`** | **[Inici ràpid](./04-inici-rapid.md)** | Tutorial pas a pas de 30 minuts per instal·lar les eines, crear el teu primer node i passar la validació a 0 errors. | 30 min |
| **`05-glossari.md`** | **[Glossari](./05-glossari.md)** | Definicions canòniques de la terminologia del kit (Node, MOC, Core, Frontmatter, Graf, Taller, MIAE, VCER...). | 8 min |
| **`06-faq.md`** | **[Preguntes freqüents](./06-faq.md)** | Respostes a dubtes comuns sobre formats, canvis de centre, relació amb la IA, protecció de dades i inspecció. | 10 min |
| **`07-com-compartir.md`** | **[Com compartir](./07-com-compartir.md)** | Guia per publicar el teu vault, aplicar llicències lliures i col·laborar amb la comunitat educativa. | 10 min |

---

## Comunitat i difusió

A més de la documentació central, la carpeta **[06-comunitat/](../06-comunitat/)** conté:

- **[01-casos-us.md](../06-comunitat/01-casos-us.md)** — Els tres casos reals (Benet M. a Química, César G. a Sanitat, Anna C. a Pedagogia Terapèutica), amb el detall de com es va fer cada pas.
- **[02-com-compartir.md](../06-comunitat/02-com-compartir.md)** — Guia pràctica per compartir el kit o el vault (GitHub, Classroom, zip) amb privacitat i coherència.
- **[03-article-edigital.md](../06-comunitat/03-article-edigital.md)** — L'article de difusió per a `comunitat.edigital.cat`: "Del laboratori a la sala de mestres".

---

## Casos reals i projectes de referència

El disseny d'aquest kit s'ha nodrit directament d'implementacions i proves de càrrega reals a la Formació Professional i a l'educació primària públiques catalanes:

1. **La prova de foc en Química (MP 1257 – Emmagatzematge i distribució en el laboratori):**  
   Desplegament complet des de zero per al debut docent d'en **Benet M.** a partir exclusivament del decret oficial. Demostra que el sistema permet estar **operatiu en menys d'una setmana** amb una programació d'aula completa, sessions minutades i presentacions interactives que superen l'avaluació VCER.

2. **El curs de capacitació en Sanitat (MP 1523 – Gestió de la documentació sanitària):**  
   Disseny i transferència metodològica per a en **César G.**, culminant en un vault autònom de **59 nodes interconnectats i validats amb 0 errors**.

3. **L'adaptació a l'educació especial (PTE – Pedagogia Terapèutica):**  
   Col·laboració amb l'**Anna C.**, mestra de PT a primària, per estructurar Plans Individuals (PI) i adaptacions curriculars amb privacitat reforçada per a dades de menors. El resultat és un vault de **62 fitxers** amb 4 tipus de node propis de la família PTE (`PlaSuportIndividualitzat`, `AdaptacioCurricular`, `SequenciaDidactica`, `InformeAvaluacio`).

4. **Els orígens (tres projectes germans):**  
   - **TCAI-OKF** (2025-2026): el graf del cicle de Cures Auxiliars d'Infermeria. On va néixer el Paquet LLM i el "factor Montse".
   - **SAD-GRAF** (2026-2027): el graf del cicle de Documentació Sanitària. On es van conceptualitzar els Cores, les FitxaAEA i els Protocols.
   - **PTE-OKF** (2026-2027): el graf de Pedagogia Terapèutica a primària. On es va reforçar la privacitat per a dades de menors.

De la fricció entre els tres en va sortir el que realment importa: **un esquelet mínim, genèric i obert**.

---

## Memòria històrica del projecte (Handoffs)

Els documents de traspàs de context (*Handoffs*) són **fora del repositori públic** (a `~/Documents/OKF-CATALA/okf-handoffs/`). Són registres immutables del desenvolupament del kit, i no es modifiquen per preservar la traçabilitat de les decisions preses.

| Handoff | Data | Fita |
|:---|:---|:---|
| **HANDOFF-00** | 25/10/2026 | Estructura fundacional, primers 6 commits, Cores i validador inicial. |
| **HANDOFF-01** | 26/10/2026 | Desplegament de les 6 plantilles canòniques i de l'exemple complet MP1519. |
| **HANDOFF-02** | 27/10/2026 | Integració del marc MIAE al PaquetLLM i primer push al repositori privat. |
| **HANDOFF-03** | 28/10/2026 | Consolidació del concepte de taller, la proposta de sistema operatiu i la genealogia del projecte. |
| **HANDOFF-04** | 29/10/2026 | Humanització del to, MIAE + VCER, ontologies i "programació didàctica viva". |
| **HANDOFF-05** | 29/10/2026 | Consolidació V1.1: exemple complet de 11 nodes, privacitat amb inicials. |
| **HANDOFF-06** | 31/10/2026 | Publicació oficial a GitHub i Zenodo. DOI `10.5281/zenodo.23823819`. |

> *Nota: Aquests documents no formen part del repositori públic. Es conserven localment per a ús intern i per a qui hereti el projecte en el futur.*

---

## Com citar aquest projecte

Si fas servir aquest kit en un treball acadèmic, una publicació o un article:

> Montañà Piqué, J. (2026). *OKF Starter Kit: una proposta de sistema operatiu per al coneixement curricular* (V1.1) [Programari]. Zenodo. https://doi.org/10.5281/zenodo.23823819

Per als detalls complets (APA, BibTeX, text pla), consulta la secció **[Com citar aquest projecte](../README.md#com-citar-aquest-projecte)** del README principal.

---

## Com contribuir

Si trobes alguna errada a la documentació, vols proposar una millora a les plantilles o vols compartir el graf del teu propi mòdul, consulta la guia de contribució a **[CONTRIBUTING.md](../CONTRIBUTING.md)** o obre un *issue* al repositori.