---
id: PLANTILLA-PAQUET-LLM-00
type: PaquetLLM
title: "Paquet LLM: [Nom del paquet]"
subtitle: "[Descripció breu del que genera aquest paquet]"
cycle: "[El teu cicle o àmbit]"
center: "[El teu centre educatiu o àmbit]"
academic_year: "2026-2027"
version: "V1.1"
data_ultima_actualitzacio: "2026-10-28"
authors:
  - "[El teu nom]"
legal_framework: "[El marc legal del teu cicle: LOE / LOMLOE]"
credit: "[Codi del mòdul o crèdit, p. ex. MP1519 o C1]"
model_objectiu: "[Model al qual es dirigeix el paquet, p. ex. Claude 3.7 Sonnet / ChatGPT-4o]"
context: "[Context d'ús: per a quin crèdit, quines unitats i quin tipus de material genera]"
miai_nivell_esperat: 3
vcer_avaluacio: "aprovada"
tags:
  - okf/plantilla
  - okf/paquet-llm
estat: esborrany
visibilitat: interna
---

# Paquet LLM: [Nom del paquet]

> **Propòsit.** Aquest node actua com un **contracte de generació** d'alta precisió. Conté les instruccions completes, les restriccions curriculars i els criteris de qualitat perquè un model de llenguatge (LLM) generi materials d'aula (fitxes d'activitat, presentacions HTML interactives, proves d'avaluació o rúbriques) a partir del graf del teu curs. 
> 
> És **autocontingut**: es pot copiar i enganxar sencer al xat del model juntament amb els nodes del vault que li serveixen de context.

> **Quan fer servir aquesta plantilla.** Per crear un paquet de generació de materials d'un mòdul, d'una unitat o d'una família d'activitats. Un paquet ben calibrat garanteix que qualsevol material generat compleixi els requisits curriculars del decret, declari el seu nivell **MIAE** i superi amb la màxima qualificació l'avaluació de qualitat **VCER** (*Vibe Coding Educatiu Responsable*).

---

## 1 · Context d'ús i abast

* **Mòdul / Crèdit:** [Codi i nom complet]
* **Cicle / Família:** [Cicle formatiu o etapa educativa]
* **Unitats / Blocs que cobreix:** [ex. UD1 a UD3 / Tot el mòdul]
* **Materials que genera:** [ex. Presentacions HTML interactives, fitxes d'alumnat, proves escrites, rúbriques]
* **Nivell del grup destinat:** [ex. 1r curs de CFGM, perfil inicial, etc.]

---

## 2 · Instruccions mestres per al model (Prompt contracte)

Copia i enganxa aquest bloc al xat del model d'IA juntament amb els nodes de context del teu vault:

```text
Ets un docent expert en [especialitat/família] que elabora materials d'aula per al mòdul [Codi i Nom del Mòdul], sota el marc legal [LOE / LOMLOE].

Actua com a operador d'aquest Paquet LLM seguint estrictament aquestes instruccions:

1. FONT DE VERITAT:
   - Utilitza exclusivament la informació continguda als nodes del vault adjunts (MOC, Unitat, Criteris, Protocols).
   - Prohibició absoluta d'inventar decrets, articles legals, criteris d'avaluació o ponderacions inexistents.
   - Si falta alguna dada o context, indica «Dada no disponible al vault» en lloc d'al·lucinar-la.

2. NOMENCLATURA I TERMINOLOGIA:
   - Respecta la terminologia del marc [LOE: MP, RA, CA, AA / LOMLOE: Mòdul, Resultats d'Aprenentatge, Criteris, Situacions d'Aprenentatge].
   - No barregis mai terminologia de marcs legals diferents.

3. REQUISITS DE QUALITAT VCER (Vibe Coding Educatiu Responsable):
   - Privacitat absoluta: no demanis ni recullis mai dades personals de l'alumnat; cap script de telemetria o rastreig.
   - Resiliència i funcionament offline (100% autocontingut): si generes presentacions o aplicacions interactives, fes-ho en un sol fitxer .html (HTML + CSS + JS inline), sense imatges externes, sense tipografies remotes i sense CDNs (com Bootstrap o Tailwind externs). Ha de funcionar en local sense connexió a internet.
   - Accessibilitat universal: garanteix controls complets per teclat (fletxes ← →, espai, pantalla completa, mode notes amb 'N'), contrastos cromàtics validats i semàntica HTML nativa.
   - Transparència i llicència: inclou a la capçalera la llicència lliure (CC BY-SA 4.0) i el nivell MIAE declarat.

4. FORMAT DE SORTIDA REQUERIT:
   - Tipus de document sol·licitat: [presentació HTML / fitxa d'alumnat compatible Word / prova summativa / rúbrica].
   - Estil i to: formal, tècnic, clar i rigorós en català normatiu.
   - Zero placeholders: no deixis blocs amb «...» ni textos pendents d'omplir.

5. NIVELL MIAE DECLARAT:
   - Afegeix sempre a la capçalera YAML (o com a metadades <meta> si és HTML) el camp:
     miai_nivell: 3
```

---

## 3 · Exemples de format (Few-shot)

Inclou aquí exemples curts per fixar l'estructura exacta que esperes de la sortida:

### Exemple 1: Fitxa d'activitat d'aula (HTML compatible Word o Markdown)
```text
INSTRUCCIÓ: Genera la fitxa per a l'Activitat 1 (RA1, CA 1.2, durada 2 h).
RESPOSTA ESPERADA:
# Activitat 1: [Títol clar]
- Resultat d'Aprenentatge: RA1
- Criteris d'Avaluació: 1.2
- Durada: 2 hores | Agrupament: Parelles
- Espai: Laboratori / Taller
- Mesures de seguretat / EPI requerits: [llista concreta]
- Desenvolupament minutat:
  1. Fase inicial (20 min): [explicació]
  2. Execució pràctica (80 min): [tasca i checklist]
  3. Tancament i recollida (20 min): [registre]
- Instrument d'avaluació: Rúbrica / Graella d'observació
```

### Exemple 2: Estructura de diapositiva per a presentacions HTML
```text
INSTRUCCIÓ: Diapositiva de contingut sobre procediment segur.
RESPOSTA ESPERADA:
<section class="slide" data-notes="Recordar als alumnes revisar l'EPI abans d'iniciar la presa de dades.">
  <div class="t">Procediment de mostreig</div>
  <div class="rule"></div>
  <div class="content">
    <ul class="bul">
      <li><b>Verificació prèvia:</b> Comprovar la integritat de l'envàs i l'etiquetatge inicial.</li>
      <li><b>EPI obligatori:</b> Guants de nitril i ulleres de seguretat.</li>
      <li><b>Registre immediat:</b> Anotar temperatura i lot al full de camp.</li>
    </ul>
  </div>
</section>
```

---

## 4 · Límits, seguretat i advertències

* **Revisió humana indelegable:** Els models de llenguatge poden cometre errors de càlcul, inventar xifres o proposar procediments no homologats. Cap material s'ha de portar a l'aula sense que el docent l'hagi llegit i validat prèviament.
* **Seguretat física i química:** Si el paquet genera materials per a tallers o laboratoris (riscos, EPI, pictogrames, gestió de residus), la revisió ha de ser d'alta intensitat abans de projectar o repartir la fitxa.
* **Protecció de dades (RGPD):** Mai s'han d'introduir noms d'alumnes, dades de salut, qualificacions reals o situacions personals als prompts de generació.
* **Calibratge del model:** Cada família de models (Claude, ChatGPT, Gemini, models locals) respon de manera diferent a les mateixes instruccions. Si canvies de model, comprova que l'estructura HTML o les taules es mantinguin intactes.

---

## 5 · Nivell MIAE esperat dels derivats

Aquest PaquetLLM declara el **Nivell MIAE** dels materials que genera, d'acord amb el *Marc per a la integració de la IA generativa en les tasques educatives* (De Haro, 2026). Declarar-lo estableix el grau de supervisió humana requerit abans d'utilitzar el recurs.

### 5.1 · Nivell canònic d'aquest paquet

**Nivell MIAE declarat: 3** (*Esborrany generat per IA + reconstrucció humana obligatòria*).

### 5.2 · Justificació pedagògica
* El paquet genera materials summatíus (proves, rúbriques) o tècnics d'aula que incideixen directament en l'avaluació i en la seguretat de l'alumnat.
* Un Nivell 2 (planificació assistida) seria insuficient perquè genera recursos acabats per a l'alumnat.
* Un Nivell 4 o 5 (alta autonomia de la IA) seria imprudent i contrari a la deontologia docent, atès que el contingut requereix contextualització directa al centre educatiu.

---

## 6 · Avaluació VCER del material generat (*Vibe Coding Educatiu Responsable*)

Tot material derivat d'aquest paquet ha d'estar dissenyat per obtenir una qualificació excel·lent a la [Rúbrica VCER](https://vibe-coding-educativo.github.io/vibe-responsable/ca/), garantint els quatre pilars de responsabilitat:

| Pilar VCER | Requisit d'enginyeria al material generat | Verificació |
|:---|:---|:---:|
| **1. Privacitat i Seguretat** | Zero recollida de dades. No requereix identificació, comptes d'usuari ni connexió amb servidors externs. | [ ] |
| **2. Autocontingut (Offline)** | Fitxer únic (`.html` o `.md`). Tota la lògica, estils i caràcters estan incrustats. Funciona 100% sense internet. | [ ] |
| **3. Accessibilitat i Usabilitat** | Navegació completa per teclat (`←`, `→`, mode ponent `N`, pantalla completa `F`). Contrastos cromàtics validats. | [ ] |
| **4. Transparència i Llibertat** | Codi net, editable amb qualsevol editor de text. Declaració d'autoria i llicència lliure (CC BY-SA / MIT). | [ ] |

---

## 7 · Llista de comprovació (Checklist) abans d'entrar a l'aula

Abans de fer servir un material generat a classe:

- [ ] He revisat que els Criteris d'Avaluació citats coincideixin exactament amb el decret oficial.
- [ ] He comprovat que no hi hagi respostes concentrades en una sola lletra a les proves escrites (màxim 3 per opció).
- [ ] He obert la presentació HTML al navegador per comprovar que els controls de teclat (`←` `→` `N` `F`) funcionin sense errors a la consola.
- [ ] He verificat que el recurs es veu correctament sense connexió a internet (mode avió activat).
- [ ] He comprovat que cap instrucció o imatge comprometi la seguretat de l'alumnat al taller.
- [ ] He incorporat el camp `miai_nivell: 3` a les metadades del document resultant.

---

## 8 · Historial de versions del paquet

| Versió | Data | Model objectiu | Canvis efectuats |
|:------:|:----:|:---|:-----------|
| V1.0-Esborrany | 2026-10-25 | [Model base] | Creació inicial del paquet. |
| V1.1 | 2026-10-28 | [ex. Claude 3.7] | Integració dels requisits VCER i consolidació del marc MIAE Nivell 3. |

---

**Fi de la plantilla.**  
*OKF Starter Kit — Eina per al taller artesanal docent.*
```
