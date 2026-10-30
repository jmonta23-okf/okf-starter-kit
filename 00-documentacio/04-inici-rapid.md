# Inici ràpid — 30 minuts

Aquest tutorial et porta de zero a tenir un vault OKF operatiu i validat al teu ordinador en **30 minuts**. No necessites cap coneixement previ d'OKF: només saber obrir un terminal bàsic i un editor de text.

| | |
|:---|:---|
| **Temps estimat** | 30 minuts |
| **Requisits previs** | Python 3.9+, Git i un editor de text (Obsidian, VS Code o el que prefereixis) |
| **Resultat final** | Un vault funcional amb els teus primers nodes validats amb 0 errors |

---

## 1 · Comprovar les eines (2 minuts)

Abans de començar, comprova des del terminal del teu ordinador que disposes de Python i Git:

```bash
python3 --version    # Ha de retornar Python 3.9 o superior
git --version        # Ha de mostrar la versió de Git instal·lada
```

*Si et falta alguna eina:*
- **macOS:** Si tens Homebrew, executa `brew install python git`.
- **Linux (Ubuntu/Debian):** Executa `sudo apt install python3 python3-pip git`.
- **Windows:** Descarrega els instal·ladors oficials des de [python.org](https://python.org) i [git-scm.com](https://git-scm.com).

---

## 2 · Descarregar el kit (2 minuts)

Clona el repositori oficial al teu ordinador i entra a la carpeta del projecte:

```bash
git clone https://github.com/jmonta23-okf/okf-starter-kit.git
cd okf-starter-kit
```

Si llistes el contingut de la carpeta (`ls`), veuràs aquesta estructura neta:

```text
okf-starter-kit/
├── README.md              # Portada i manifest del projecte
├── 00-documentacio/       # Guies, filosofia, arquitectura i glossari
├── 01-cores/              # Marcs normatius oficials (FP i LOMLOE)
├── 02-exemple-complet/    # Mòdul sencer desplegat (Sanitat, MP1519)
├── 03-eines/              # El validador estàtic en Python (validar_yaml.py)
├── 04-plantilles/         # Les 6 plantilles canòniques per crear nodes
├── 05-exemples-minims/    # El laboratori de proves (vault de 3 nodes)
└── 06-comunitat/          # Espai de compartició comunitària
```

---

## 3 · Instal·lar la dependència (1 minut)

L'única dependència externa que necessita el validador és la llibreria `pyyaml`:

```bash
pip install pyyaml
```

*(Si el teu sistema utilitza l'àlies `pip3`, executa `pip3 install pyyaml`).*

---

## 4 · Explorar el vault mínim (3 minuts)

Per entendre el mètode sense aclaparar-te, hem preparat el vault més petit possible a `05-exemples-minims/vault-de-3-nodes/`:

```text
vault-de-3-nodes/
├── 00_C1_MOC.md              # Node arrel (Map of Content)
├── 01_C1_Unitat_Didactica.md  # Unitat didàctica del curs
└── 02_C1_Fitxa_Activitat.md  # Fitxa d'activitat d'aula
```

Obre el fitxer arrel `00_C1_MOC.md` amb el teu editor de text (o mostra'l al terminal amb `cat 05-exemples-minims/vault-de-3-nodes/00_C1_MOC.md`):

```markdown
---
id: C1-MOC-00
type: MOC
title: "Map of Content: El meu curs d'exemple"
subtitle: "Node arrel del vault d'exemple"
cycle: "CFGM Cures Auxiliars d'Infermeria (TCAI)"
center: "El teu centre educatiu"
academic_year: "2026-2027"
version: "V1.0-Esborrany"
data_ultima_actualitzacio: "2026-10-28"
authors:
  - "El teu nom"
legal_framework: "Decret 203/1997"
tags:
  - okf/exemple
  - okf/moc
estat: vigent
---

# Map of Content: El meu curs d'exemple

Aquest és el node arrel del vault. Des d'aquí s'enllacen tots els altres nodes.

## Nodes del curs

- [Unitat 1: Introducció](./01_C1_Unitat_Didactica.md) — Primera unitat del curs
- [Fitxa d'activitat 1](./02_C1_Fitxa_Activitat.md) — Una fitxa d'activitat
```

Fixa't en les dues parts:
1. **Frontmatter YAML (entre els dos `---`):** Les metadades del document. Diu quin tipus de fitxer és, qui l'ha creat i quin marc legal té.
2. **Cos Markdown (a sota):** El text que llegim les persones, amb els enllaços relatius (`./01_C1_Unitat_Didactica.md`) que teixeixen el graf.

---

## 5 · Executar el validador (2 minuts)

Ara comprovem la integritat del vault executant l'script d'auditoria sobre aquesta carpeta:

```bash
python3 03-eines/validar_yaml.py --ruta 05-exemples-minims/vault-de-3-nodes
```

**Resultat esperat al teu terminal:**

```text
# Informe de Validació YAML — OKF Starter Kit
**Ruta del vault:** 05-exemples-minims/vault-de-3-nodes
**Script:** validar_yaml.py v1.0.1

## Resum Executiu

| Mètrica | Valor |
|:--------|:-----:|
| Fitxers .md escanejats (nodes OKF) | 3 |
| Fitxers amb errors | 0 |
| Errors crítics (🔴) | 0 |
| Errors alts (🟠) | 0 |
| Advertències (🟡) | 0 |

## ✅ Resultat

Tots els nodes OKF del vault han passat la validació sense errors.
```

Si veus el missatge verd de **0 errors**, el teu entorn està perfectament configurat.

---

## 6 · Trencar el sistema expressament (4 minuts)

El validador no és un tràmit burocràtic; és el teu assistent de seguretat. Farem una prova provocant un error per veure com t'avisa.

Obre el fitxer `05-exemples-minims/vault-de-3-nodes/01_C1_Unitat_Didactica.md` amb el teu editor i canvia el format de la versió:

```yaml
# Canvia això:
version: "V1.0-Esborrany"

# Per això (un format incorrecte):
version: "1.0"
```

Desa el fitxer i torna a passar el validador:

```bash
python3 03-eines/validar_yaml.py --ruta 05-exemples-minims/vault-de-3-nodes
```

El validador s'aturarà immediatament i t'assenyalarà el problema:

```text
## Errors Detectats

| # | Fitxer                      | Codi | Gravetat | Descripció                                               | Acció             |
|:-:|:----------------------------|:----:|:--------:|:---------------------------------------------------------|:------------------|
| 1 | `01_C1_Unitat_Didactica.md` | Y009 | 🟡       | Versió '1.0' no segueix el patró 'V<maj>.<min>[.<patch>]'| Corregir la versió |
```

---

## 7 · Corregir l'error (2 minuts)

Torna a editar el fitxer i restableix el valor canònic:

```yaml
version: "V1.0-Esborrany"
```

Torna a validar:

```bash
python3 03-eines/validar_yaml.py --ruta 05-exemples-minims/vault-de-3-nodes
```

Tornaràs a tenir **0 errors**. Així de senzill: el validador t'indica la incidència, la corregeixes i el teu graf torna a estar blindat.

---

## 8 · Crear el teu primer node nou (6 minuts)

Ara afegirem un node nou per comprovar com creix el graf.

1. Crea un fitxer nou a `05-exemples-minims/vault-de-3-nodes/03_C1_Fitxa_Activitat_2.md`.
2. Enganxa-hi aquest contingut:

```markdown
---
id: C1-AEA-02
type: FitxaAEA
title: "Activitat 2: Rentat de mans quirúrgic"
subtitle: "Procediment pràctic d'asèpsia a l'aula d'infermeria"
cycle: "CFGM Cures Auxiliars d'Infermeria (TCAI)"
center: "El teu centre educatiu"
academic_year: "2026-2027"
version: "V1.0-Esborrany"
data_ultima_actualitzacio: "2026-10-28"
authors:
  - "El teu nom"
legal_framework: "Decret 203/1997"
credit: "C1"
tags:
  - okf/activitat
  - c1/asepsia
estat: esborrany
---

# Activitat 2: Rentat de mans quirúrgic

En aquesta activitat l'alumnat practica la tècnica del rentat de mans quirúrgic seguint el protocol del centre.

## Enllaços de retorn
- Tornar al mapa general: [00_C1_MOC.md](./00_C1_MOC.md)
```

3. Ara enllaça aquest nou node des del MOC: obre `05-exemples-minims/vault-de-3-nodes/00_C1_MOC.md` i afegeix a la llista d'activitats:

```markdown
- [Fitxa d'activitat 2: Rentat de mans](./03_C1_Fitxa_Activitat_2.md) — Segona pràctica d'aula
```

4. Executa de nou el validador:

```bash
python3 03-eines/validar_yaml.py --ruta 05-exemples-minims/vault-de-3-nodes
```

**Veuràs que el sistema ara escaneja 4 nodes i confirma 0 errors.** Has expandit el teu graf correctament.

---

## 9 · Què has après en aquesta sessió?

En només 30 minuts has dominat els fonaments d'OKF:
* **L'anatomia d'un node:** Metadades YAML a la capçalera + contingut en text pla Markdown a sota.
* **La topologia del graf:** Com s'enllacen els fitxers mitjançant rutes relatives senzilles encapçalades pel MOC.
* **El paper del validador:** Com auditar el teu curs en 2 segons per assegurar-te que no faltin camps obligatoris ni hi hagi inconsistències.

---

## 10 · Següents passos

Un cop completat aquest laboratori, tens diferents camins segons el que vulguis fer:

* **Veure un mòdul sencer real:**  
  Executa el validador sobre l'exemple complet del kit:
  ```bash
  python3 03-eines/validar_yaml.py --ruta 02-exemple-complet
  ```
  Veuràs com s'estructura un mòdul sencer (el MP1519 de Sanitat) amb 6 nodes complets, incloent-hi el catàleg curricular, protocols d'avaluació i el **Paquet LLM** d'aula.

* **Obrir el vault a Obsidian per veure el graf visual:**  
  Descarrega [Obsidian](https://obsidian.md), fes clic a *«Open folder as vault»* i selecciona la carpeta `okf-starter-kit`. Prem `Ctrl+G` (o `Cmd+G` a Mac) per obrir la vista de graf i veure la xarxa neuronal de connexions del teu curs.

* **Aprofundir en la documentació conceptual:**
  * **[Què és OKF?](./01-que-es-okf.md)** — La reflexió sobre la tirania de les carpetes i la doble lectura d'OKF.
  * **[Filosofia](./02-filosofia.md)** — La mirada de biòleg, les ontologies clíniques i la programació didàctica com a organisme viu.
  * **[Arquitectura](./03-arquitectura.md)** — El model de 4 capes, la convenció YAML mixta (EN/CA) i el tàndem MIAE + VCER.
  * **[Preguntes freqüents (FAQ)](./06-faq.md)** — Com resoldre dubtes sobre inspecció, privacitat i adaptació a altres etapes.

* **Crear el teu propi mòdul des de zero:**  
  Ves a la carpeta `04-plantilles/`, copia `PLANTILLA-MOC.md` a la carpeta del teu nou curs i comença a bastir el teu propi taller docent.

---

**Enhorabona! Ja formes part de la comunitat OKF.**
```
