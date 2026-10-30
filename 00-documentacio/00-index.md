# Índex de la Documentació d'OKF Starter Kit

> **Benvingut a la base de coneixement d'OKF Starter Kit.**  
> Aquesta carpeta conté tota la documentació conceptual, filosòfica, tècnica i pràctica del sistema.

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

## Casos reals i projectes de referència

El disseny d'aquest kit s'ha nodrit directament d'implementacions i proves de càrrega reals a la Formació Professional pública catalana:

1. **La prova de foc en Química (MP 1257 – Emmagatzematge i distribució en el laboratori):**  
   Desplegament complet des de zero per al debut docent d'en **Benet M.** a partir exclusivament del decret oficial. Demostra que el sistema permet estar **operatiu en menys d'una setmana** amb una programació d'aula completa, sessions minutades i presentacions interactives que superen l'avaluació VCER.
2. **El curs de capacitació en Sanitat (MP 1523 – Gestió de la documentació sanitària):**  
   Disseny i transferència metodològica per a en **César G.**, culminant en un vault autònom de **59 nodes interconnectats i validats amb 0 errors**.
3. **Els orígens (TCAI-OKF i SAD-GRAF):**  
   Els dos projectes germans desenvolupats entre 2025 i 2027 a les famílies de Sanitat i Serveis a la Comunitat d'on s'han destil·lat els Cores i les eines d'aquest kit.

---

## Memòria històrica del projecte (Handoffs)

Aquesta carpeta conté també els documents de traspàs de context (*Handoffs*), que funcionen com a registres immutables del desenvolupament del kit:

* **`HANDOFF-00.md`** (25/10/2026): Estructura fundacional, primers 6 commits, Cores i validador inicial.
* **`HANDOFF-01.md`** (26/10/2026): Desplegament de les 6 plantilles canòniques i de l'exemple complet MP1519.
* **`HANDOFF-02.md`** (27/10/2026): Integració del marc MIAE al PaquetLLM i primer push al repositori privat.
* **`HANDOFF-03.md`** (28/10/2026): Consolidació del concepte de taller, la proposta de sistema operatiu i la genealogia del projecte.

> *Nota: Els documents de Handoff són fotografies històriques congelades en el temps; no es modifiquen per preservar la traçabilitat de les decisions preses.*

---

## Com contribuir

Si trobes alguna errada a la documentació, vols proposar una millora a les plantilles o vols compartir el graf del teu propi mòdul, consulta la guia de contribució a **[CONTRIBUTING.md](../CONTRIBUTING.md)** o obre un *issue* al repositori.