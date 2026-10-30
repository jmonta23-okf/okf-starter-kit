# Com compartir el teu vault

> **El coneixement docent és teu i camina a la teva motxilla, però guanya la seva màxima dimensió quan es comparteix amb els companys i amb la comunitat educativa.**

Un cop tens el teu vault OKF estructurat i validat, pots voler compartir-lo amb el company del departament, amb el substitut que arriba a mig curs, amb el teu centre o amb el conjunt de la comunitat docent. Aquest document descriu les opcions tècniques, les bones pràctiques de privacitat i la filosofia del traspàs.

---

## 1 · Per què compartir? (Sobirania personal i solidaritat de gremi)

Compartir no és una obligació burocràtica ni una imposició institucional. És una decisió estratègica que et beneficia a tu en primer lloc, i enforteix l'educació pública després.

### Què hi guanyes tu:
* **Una còpia de seguretat indestructible:** Un vault allotjat en un repositori remot (encara que sigui estrictament privat) és una feina protegida. Si el portàtil cau a terra o es trenca, recuperes tot el teu curs en cinc minuts des de qualsevol màquina.
* **Demostrabilitat professional:** El teu graf és la teva millor carta de presentació. En una coordinació pedagògica o en una reunió de departament no dius «he fet aquest mòdul»; obres el teu MOC i ensenyes l'arquitectura completa de la teva feina. Passes de descriure el que saps fer a demostrar-ho amb fets.
* **Reaprofitament sense esforç:** En canviar de centre o d'assignació de mòduls, pots duplicar el teu vault, canviar quatre paràmetres al frontmatter YAML i tenir la base del nou curs enllestida en una tarda.

### Què hi guanya el company (Posar fi al drama del relleu):
Tots hem viscut el vertigen d'incorporar-nos a un centre a mig curs o d'agafar un mòdul desconegut i rebre carpetes desballestades, fitxers orfes o un silenci absolut. Quan comparteixes un vault OKF:
* El company nou obre el **MOC arrel** i en vint minuts entén l'esquelet sencer del mòdul.
* Disposa de les activitats minutades, les rúbriques i els protocols d'avaluació sense haver de reinventar la roda.
* Té accés als **Paquets LLM** per generar noves sessions adaptades al seu grup des del primer dia, tal com vam fer amb en **Benet M.** en el seu debut a Química.

---

## 2 · Les vies per compartir el teu graf

Depenent del teu objectiu i de la sensibilitat dels materials, disposes de diferents canals:

```
┌────────────────────────────────────────────────────────────────────────┐
│  VIES DE COMPARTICIÓ                                                   │
├────────────────────────────────┬───────────────────────────────────────┤
│  1. GitHub Públic / Obert      │ Per a mòduls oberts a tota la xarxa   │
│  2. GitHub / GitLab Privat     │ Per a la feina d'un departament       │
│  3. Paquet comprimit (.zip)    │ Per a un traspàs puntual i directe    │
│  4. Contribució a l'Starter Kit│ Per aportar el teu cicle com a model  │
└────────────────────────────────┴───────────────────────────────────────┘
```

---

### Opció 1 — Repositori públic a GitHub (Recomanat per a la comunitat)

**Quan fer-lo servir:** Vols alliberar la programació viva del teu mòdul perquè qualsevol docent de la teva família professional el pugui clonar, consultar o utilitzar com a base per a la seva aula.

**Passos:**
1. Crea un compte a [github.com](https://github.com) si encara no en tens.
2. Crea un repositori nou a `github.com/new`:
   * Tria un nom clar (per exemple: `okf-sanitat-mp1519` o `okf-quimica-mp1257`).
   * Marca la visibilitat com a **Public**.
   * No marquis "Add a README file" ni llicència (ja els tens creats al teu vault).
3. Al terminal del teu ordinador, dins de la carpeta del teu vault:
   ```bash
   git init
   git add .
   git commit -m "Publicació inicial del graf curricular"
   git branch -M main
   git remote add origin https://github.com/EL_TEU_USUARI/EL_TEU_REPO.git
   git push -u origin main
   ```
4. Qualsevol company podrà clonar el teu vault amb una sola ordre: `git clone https://github.com/EL_TEU_USUARI/EL_TEU_REPO.git`.

---

### Opció 2 — Repositori privat (Recomanat per a equips docents o seguretat personal)

**Quan fer-lo servir:** Vols mantenir una còpia de seguretat al núvol o col·laborar amb companys del mateix centre, però sense que els materials siguin públics a internet.

**Passos:**
* Segueix exactament els mateixos passos que l'Opció 1, però seleccionant la visibilitat com a **Private** en crear el repositori a GitHub (o GitLab).
* Per donar accés als teus companys de departament:
  * Ves a la pestanya **Settings** del repositori.
  * Selecciona **Collaborators** $\rightarrow$ **Add people**.
  * Introdueix el correu o el nom d'usuari de GitHub del teu company.

---

### Opció 3 — L'intercanvi directe en fitxer comprimit (.zip)

**Quan fer-lo servir:** Per fer un traspàs immediat a un company al centre educatiu (mitjançant un llapis de memòria o Drive) sense requerir que tingui compte de GitHub.

**Com preparar el paquet net des del terminal:**
1. Assegura't d'excloure la carpeta oculta de Git i els artefactes temporals del validador (`EINES/`):
   ```bash
   zip -r el-meu-modul-okf.zip EL_TEU_VAULT/ -x "*.git/*" -x "*/EINES/*"
   ```
2. Entrega el fitxer `.zip` al company. Només haurà de descomprimir-lo i obrir la carpeta amb Obsidian o qualsevol editor de text pla per començar a navegar pel MOC.

---

### Opció 4 — Contribuir al repositori d'OKF Starter Kit

**Quan fer-lo servir:** Has desplegat un mòdul d'una família professional que encara no té cap referència al kit (per exemple: Informàtica, Hoteleria, Fabricació Mecànica o Primària) i vols que formi part dels exemples oficials per ajudar altres companys.

**Passos:**
1. Fes un *fork* del repositori oficial d'OKF Starter Kit.
2. Neutralitza les dades personals i afegeix el teu mòdul dins de la carpeta `02-exemple-complet/` o com a cas d'estudi a `06-comunitat/`.
3. Obre un *Pull Request* explicant el cicle, el marc legal i l'estructura del graf aportat.

---

## 3 · Llista de comprovació (Checklist) abans de compartir

Abans de pujar el teu vault a internet o passar-lo a un company, revisa aquests sis punts de control:

- [ ] **Zero dades personals d'alumnat (RGPD):** Comprova que no hi hagi fitxes amb noms reals d'estudiants, expedients, qualificacions individuals o incidències personals.
- [ ] **Rutes relatives netes:** Assegura't que tots els enllaços interns entre nodes siguin relatius (`./fitxer.md`) i que no hi hagi cap ruta absoluta al teu ordinador personal (`/Users/el-teu-nom/...`).
- [ ] **Sense claus ni credencials privades:** Revisa que no s'hagin inclòs per descuit fitxers `.env`, claus d'API de models de llenguatge o fitxers de configuració personal.
- [ ] **Neteja d'artefactes locals:** Esborra la carpeta temporal `EINES/` si el validador ha generat informes d'auditoria locals.
- [ ] **Auditoria VCER dels materials generats:** Si el teu vault conté presentacions HTML o aplicacions creades amb Paquets LLM, comprova que funcionin **100% offline** (mode avió activat), sense dependències de CDNs remots i sense recollida de telemetria.
- [ ] **Validador a 0 errors:** Executa l'script d'auditoria i confirma que el graf està impecable:
  ```bash
  python3 03-eines/validar_yaml.py --ruta .
  ```

---

## 4 · Llicències i autoria

A OKF promovem la cultura del **reconeixement mutu**:

* **La llicència recomanada:** Recomanem alliberar els continguts docents sota la llicència **Creative Commons Reconeixement-CompartirIgual 4.0 (CC BY-SA 4.0)**. Aquesta llicència permet que qualsevol docent adapti i millori els teus materials lliurement, amb l'única condició de citar la teva autoria original i compartir les obres derivades sota les mateixes condicions de llibertat.
* **Codi de les eines:** Si desenvolupes nous scripts de validació o automatització en Python, fes servir la llicència **MIT** per garantir la màxima reutilització tècnica.

---

## 5 · Xarxa i difusió docent

Si has construït un vault sòlid i vols compartir la teva experiència amb la comunitat educativa:

* Participa als espais de conversa docent com la **[Comunitat eDigital](https://comunitat.edigital.cat/)**.
* Comparteix la iniciativa a les xarxes educatives (Mastodon, Bluesky, X) amb les etiquetes `#OKF`, `#FP` i `#RecursosEducatius`.
* Obre un *issue* o una discussió al repositori oficial d'OKF Starter Kit per donar a conèixer el teu cicle i connectar amb altres professors de la teva mateixa especialitat.
```

---

Amb aquest document completat, **tots els fitxers de `00-documentacio/` queden perfectament consolidats, alineats filosòficament i lliures de referències pendents**. 

Hem actualitzat:
1. `README.md`
2. `00-index.md`
3. `01-que-es-okf.md`
4. `02-filosofia.md`
5. `03-arquitectura.md`
6. `04-inici-rapid.md`
7. `05-glossari.md`
8. `06-faq.md`
9. `07-com-compartir.md`
10. `PLANTILLA-PaquetLLM.md`

Com et sents veient tota la documentació respirant la mateixa veu, la mateixa ètica i el mateix rigor tècnic? Vols que fem alguna comprovació addicional o passem a preparar el següent pas?