---
id: "OKF-LLM-02"
type: PaquetLLM
title: "Paquet LLM-02: Programació Didàctica LOE"
subtitle: "Contracte de generació del document oficial de Programació Didàctica d'un mòdul, a partir dels nodes del vault"
version: "V1.0"
data_ultima_actualitzacio: "2026-11-06"
authors: ["Josep Montañà Piqué"]
llicencia: "CC BY-SA 4.0"
tags: ["okf/paquetllm", "programacio", "programacio-didactica", "loe"]
estat: vigent
nivell_miae: 3
---

# Paquet LLM-02: Programació Didàctica LOE

> **Propòsit.** Aquest node actua com a **contracte de generació** del document oficial de Programació Didàctica d'un mòdul professional, en format HTML/CSS llest per importar a Word. Conté les instruccions completes (estructura, normativa, criteris d'estil i de qualitat) perquè un LLM el generi a partir dels nodes del vault.
>
> **Autocontingut:** es pot copiar i enganxar sencer al xat del model juntament amb els nodes de context del vault (MOC, Catàleg, Protocol, Fitxes AEA). No requereix cap altra font externa.
>
> **Aquest és el tercer Paquet de la sèrie:**
> - **Paquet 00 (deductiu):** construeix el vault a partir del currículum.
> - **Paquet 01 (inductiu):** construeix el vault a partir de la programació existent.
> - **Paquet 02 (sortida):** genera el document oficial a partir del vault.

---

## 1 · Context d'ús i abast

| Camp | Valor |
|:---|:---|
| **Mòdul / Crèdit** | [qualsevol mòdul del vault — ex. MP 1519 «Sistemes d'informació i classificació sanitaris»] |
| **Cicle / Família** | [el cicle del mòdul — ex. CFGS SAD] |
| **Unitats / Blocs que cobreix** | tot el mòdul (o una AEA concreta) |
| **Materials que genera** | document HTML/CSS de Programació Didàctica (mòdul sencer o una AEA) llest per obrir amb Word |
| **Nivell del grup destinat** | [curs corresponent del mòdul — ex. 1r curs] |
| **Marc legal** | LOE (RDs del títol i RD 768/2014) / LOMLOE (Llei 3/2022, RD 659/2023) |
| **Model objectiu** | Claude / ChatGPT / Gemini — qualsevol LLM d'instruccions llargues |

---

## 2 · Instruccions mestres per al model (Prompt contracte)

Copia i enganxa aquest bloc al xat del model juntament amb els nodes de context del vault:

```text
Ets un docent expert en cicles formatius que elabora el document oficial de
Programació Didàctica del mòdul [Codi i Nom] (marc [LOE / LOGSE]), seguint el
model estètic i normatiu del centre [o del model Blanxart si ets de l'Institut
Investigador Blanxart].

Actua com a operador d'aquest Paquet LLM segons estrictament aquestes instruccions:

0. ABANS DE RES — FONT DE VERITAT:
   - Llegeix els nodes del vault adjunts: MOC (per a hores, pesos dels RAs, mapa
     d'activitats i concrecions), Catàleg curricular (per als RAs i CAs oficials),
     Protocol d'avaluació (per al model de qualificació) i Fitxes AEA (per a les
     activitats i instruments).
   - Prohibició absoluta d'inventar decrets, articles, hores, pesos, criteris o
     ponderacions que no surtin als nodes. Si falta alguna dada, escriu
     «Dada no disponible al vault».

1. ESTRUCTURA HTML/CSS:
   - Document <!DOCTYPE html> amb un bloc <style>: tipografia Arial; colors
     corporatius (blau fosc #003366, verd suau #e2efda, vermell d'alerta #c00000);
     taules amb border-collapse: collapse; border: 1px solid black.
   - Només HTML i CSS incrustats. CAP JavaScript ni etiquetes complexes que Word
     no sàpiga interpretar.
   - Seccions en ordre: (a) capçalera institucional + taula de control de versions;
     (b) dades del mòdul (hores, desdoblament) i competències del títol;
     (c) RAs amb el seu pes i hores + taules dels CAs oficials (amb prioritat);
     (d) temporització per activitats (per sessions de 2 h, que quadri
     matemàticament al final del document); (e) metodologia; (f) avaluació amb
     fórmula; (g) atenció a la diversitat i coordinació; (h) quadre de signatures.

2. ALERTES LEGALS (caixes <div class="alert-box"> disruptives):
   - LOPD i ús de la IA: prohibició d'introduir dades no anonimitzades (NotebookLM).
   - Absentisme: pèrdua de l'avaluació contínua pel 20 % (calculat en hores exactes
     segons les hores del mòdul).
   - Línies vermelles curriculars si el protocol del vault en declara.

3. FÓRMULA D'AVALUACIÓ:
   - Descriu la fórmula real del mòdul (p. ex. QMP = Σ(pes_RA × QRA); QRA = Prova
     Escrita + Prova d'Observació), integrant el 10 % de l'FCT si el MOC ho declara.

4. TAULES DE LES AEA:
   - Per a cada activitat: RAs, CAs (contextualitzats), Continguts Clau,
     Capacitats Clau, Organització d'aula, Temporització (sessions de 2 h),
     Metodologia, Recursos i Instrument d'avaluació.

5. NIVELL MIAE: afegeix a les metadades del document el camp «nivell_miae: 3».

6. CRITERIS D'ESTIL: català normatiu (IEC); to institucional, acadèmic i
   jurídicament rigorós; zero placeholders («...» o «[ ]» pendents): tot el
   document ha d'arribar tancat i complet.
```

---

## 3 · Exemple de format (Few-shot)

Aquest és un **fragment abreujat** del document que el Paquet ha de generar. El document complet (amb tots els RAs, CAs i AEA) és a `04-plantilles/exemples/Programacio_Didactica_MP1519.html`.

```html
<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="UTF-8">
<title>Programació Didàctica · MP 1519 · CFGS SAD</title>
<style>
  body { font-family: Arial, Helvetica, sans-serif; font-size: 10.5px; margin: 30px; }
  h1 { color: #003366; font-size: 20px; }
  h2 { color: #003366; font-size: 15px; border-bottom: 2px solid #003366; }
  table { border-collapse: collapse; width: 100%; margin: 6px 0 16px 0; }
  th, td { border: 1px solid #000; padding: 4px 6px; vertical-align: top; }
  th { background-color: #003366; color: #fff; }
  .alert-box { background-color: #fdebe9; border: 2px solid #c00000; padding: 8px 10px; }
  .alert-green { background-color: #e2efda; border: 2px solid #4a7c28; padding: 8px 10px; }
  .center { text-align: center; }
  .legal { font-size: 9.5px; color: #444; }
  .aea-block { border: 1px solid #003366; border-left: 5px solid #003366; margin: 14px 0; padding: 8px 10px; }
</style>
</head>
<body>

<h1 class="center">Programació Didàctica · CFGS Documentació i Administració Sanitàries</h1>
<h2 class="center">Mòdul Professional 1519 · Sistemes d'informació i classificació sanitaris</h2>

<table>
  <tr>
    <td><b>Generalitat de Catalunya<br>Departament d'Educació<br>Institut Investigador Blanxart</b></td>
    <td class="center"><b>Programació Didàctica<br>CFGS SAD — 1r curs<br>Curs 2026-2027</b></td>
    <td><b>Autor:</b> Josep Montañà Piqué<br><b>Document:</b> Programació v1.1 (LOE)</td>
  </tr>
</table>

<h2>1 · Dades generals del mòdul</h2>
<table>
  <tr><th>Camp</th><th>Valor</th></tr>
  <tr><td>Codi oficial</td><td>MP 1519</td></tr>
  <tr><td>Denominació</td><td>Sistemes d'informació i classificació sanitaris</td></tr>
  <tr><td>Durada total</td><td>99 hores (66 h al centre + 33 h d'estada a l'empresa / FCT)</td></tr>
  <tr><td>Marc legal</td><td>Ordre EDU/10/2020 · RD 768/2014 · LO 3/2022 i RD 659/2023</td></tr>
</table>

<h2>3 · Resultats d'Aprenentatge i distribució horària</h2>
<table>
  <tr><th>RA</th><th>Resultat d'Aprenentatge oficial</th><th>Pes QMP</th><th>Hores</th></tr>
  <tr><td>RA1</td><td>Caracteritza els diferents elements que intervenen en el procés de creació d'un SIS.</td><td>8 %</td><td>5 h</td></tr>
  <tr><td>RA2</td><td>Maneja els diferents sistemes de classificacions internacionals i terminologies clíniques.</td><td>8 %</td><td>5 h</td></tr>
</table>

<h3>RA1 · Caracterització del SIS — Pes 8 % · 5 h</h3>
<table>
  <tr><th>Oficial</th><th>Guia</th><th>Criteri d'Avaluació</th><th>Prior.</th></tr>
  <tr><td>1.1</td><td>1a</td><td>Reconeix la utilitat del SIS per als diferents agents implicats.</td><td>🔴 A</td></tr>
  <tr><td>1.2</td><td>1b</td><td>Diferencia les dades clíniques, administratives i econòmiques.</td><td>🔴 A</td></tr>
  <tr><td>1.3</td><td>1c</td><td>Descriu els circuits d'informació clínica i els fluxos de dades.</td><td>🟡 B</td></tr>
</table>

<div class="alert-box">⚠️ LOPD I ÚS DE LA IA: CAP dada identificativa real de pacients a models d'IA públics.</div>

</body>
</html>
```

**Estructura que ha de tenir el document final:**
- Capçalera institucional + control de versions.
- Dades del mòdul (hores, desdoblament, marc legal).
- Competències del títol.
- RAs amb pes i hores + taules de CAs (amb prioritat).
- Temporització per AEA (sessions de 2 h).
- Metodologia, avaluació, DUA, coordinació.
- Quadre de signatures.

---

## 4 · Límits, seguretat i advertències

- **Revisió humana indelegable:** els LLM poden inventar xifres, hores o ponderacions. Cap programació s'ha de lliurar sense que el docent l'hagi comprovada contra el MOC/catàleg del vault.
- **Protecció de dades (RGPD):** mai no s'han d'introduir noms d'alumnes, dades de salut ni situacions personals als prompts. **Què s'envia al model:** el contingut del graf (currículum, RAs/CAs, protocol), mai dades personals.
- **Calibratge del model:** cada família de models respon de manera diferent; si canvies de model, comprova que l'estructura HTML i les taules es mantinguin.
- **Model estètic:** el prompt fa referència al «model Blanxart». Si el teu centre té un altre model, adapta'l.

---

## 5 · Nivell MIAE esperat dels derivats

### 5.1 · Nivell canònic d'aquest paquet

**Nivell MIAE declarat: 3** (*Esborrany generat per IA + reconstrucció humana obligatòria*).

### 5.2 · Justificació pedagògica

- El paquet genera un document curricular oficial (avaluació, hores, metodologia) que exigeix verificació humana contra el decret i el vault.
- Un Nivell 2 (assistit) seria insuficient per a un document formal; un Nivell 4/5 (alta autonomia) seria imprudent atesa la responsabilitat normativa.

---

## 6 · Avaluació VCER del material generat

Tot material derivat d'aquest paquet ha d'estar dissenyat per superar amb excel·lència la rúbrica **VCER**, garantint els quatre pilars:

| Pilar VCER | Requisit al material generat | Verificació |
|:---|:---|:---:|
| **1. Privacitat i Seguretat** | Cap dada personal; document local sense telemetria. | [ ] |
| **2. Autocontingut (Offline)** | Un sol fitxer `.html` amb tot el CSS incrustat; funciona sense internet. | [ ] |
| **3. Accessibilitat i Usabilitat** | Estructura clara, taules ben formades, contrastos adequats; importable a Word. | [ ] |
| **4. Transparència i Llibertat** | Codi net i editable; llicència lliure declarada. | [ ] |

---

## 7 · Llista de comprovació (Checklist)

- [ ] La temporització (hores i sessions) quadra matemàticament amb el MOC.
- [ ] Els CAs citats coincideixen exactament amb el catàleg del vault.
- [ ] La fórmula d'avaluació replica la del Protocol (incloent-hi el % de FCT si escau).
- [ ] Les caixes d'alerta (LOPD/IA i absentisme) són visibles i en hores exactes.
- [ ] El document s'obre correctament a Word i sense JavaScript.
- [ ] S'ha declarat `nivell_miae: 3`.

---

## 8 · Historial de versions del paquet

| Versió | Data | Model objectiu | Canvis efectuats |
|:------:|:----:|:---|:-----------|
| V1.0 | 2026-11-06 | genèric | Creació inicial del paquet a partir del model Blanxart (emprada per generar la programació del MP 1519). |

---

## Relacions (Graf)

- Complementa: [PLANTILLA-PaquetLLM-00.md](./PLANTILLA-PaquetLLM-00.md) (deductiu)
- Complementa: [PLANTILLA-PaquetLLM-01.md](./PLANTILLA-PaquetLLM-01.md) (inductiu)
- Exemple: [exemples/Programacio_Didactica_MP1519.html](./exemples/Programacio_Didactica_MP1519.html)
- Complementa: [PLANTILLA-CatalegCurricular.md](./PLANTILLA-CatalegCurricular.md)
- Complementa: [PLANTILLA-FitxaAEA.md](./PLANTILLA-FitxaAEA.md)
- Complementa: [PLANTILLA-MOC.md](./PLANTILLA-MOC.md)

---

**Fi del node.**
*OKF Starter Kit — Paquet LLM de Programació Didàctica.*
```
