---
id: PLANTILLA-CONVENCIO-00
type: ConvencioNomenclatura
title: "La teva Convenció de Nomenclatura"
subtitle: "Llista de tipus vàlids, esquema YAML i regles de nomenclatura del teu vault"
cycle: "[El teu cicle o àmbit]"
center: "El teu centre educatiu"
academic_year: "2026-2027"
version: "V1.0.1-Esborrany"
data_ultima_actualitzacio: "2026-10-25"  # Canvia per la data d'avui
authors:
  - "El teu nom"
legal_framework: "[El marc legal del teu cicle]"
tags:
  - okf/plantilla
  - okf/convencio
estat: esborrany
visibilitat: publica
---

# [La teva] Convenció de Nomenclatura

> **Propòsit.** Aquest document defineix les regles que regeixen la creació, nomenclatura, tipologia i estructura de qualsevol node del teu vault. És la **font de veritat única** de la Convenció: cap node no pot existir al vault si no compleix les regles que s'especifiquen aquí.
>
> **Com fer servir aquesta plantilla.** Omple cada secció substituint els textos entre claudàtors `[...]` pel teu contingut. En 15 minuts tindràs una Convenció funcional.

---

## 1 · Propòsit

[Explica per a què serveix aquesta Convenció]

---

## 2 · Tipus de node vàlids

[Taula amb els tipus que faràs servir. Recomanats: MOC, Guia, Protocol, Glossari, UnitatDidactica, FitxaAEA]

| Tipus | Descripció breu |
|:---|:---|
| `MOC` | Map of Content. Índex navegable d'una àrea del vault. |
| `Guia` | Guia d'ús, tutorial o manual d'un subsistema. |
| `Protocol` | Protocol operatiu d'aplicació general. |
| `Glossari` | Recull terminològic amb definicions acordades. |
| `UnitatDidactica` | Unitat Didàctica amb continguts, activitats i avaluació. |
| `FitxaAEA` | Fitxa d'una activitat d'ensenyament-aprenentatge concreta. |
| `PaquetLLM` | Document autocontingut per generar materials d'un crèdit. Requereix `credit`. |

**Regla.** La llista de tipus és **tancada**: cap node no pot declarar un `type:` que no hi sigui. Si cal un tipus nou, s'amplia aquesta Convenció (vegeu §7).

---

## 3 · Camps obligatoris del frontmatter

[Taula amb els camps. Mínim: id, type, title, version, data_ultima_actualitzacio, authors, tags, estat]

| Camp | Tipus | Descripció |
|:---|:---|:---|
| `id` | string | Identificador únic del node. Vegeu §4. |
| `type` | string | Un dels tipus vàlids de §2. |
| `title` | string | Títol llegible del node. |
| `version` | string | Versió del node (per exemple, `V1.0-Esborrany`). |
| `data_ultima_actualitzacio` | string (ISO 8601) | Data de la darrera modificació (`AAAA-MM-DD`). |
| `authors` | array de strings | Autors del node. |
| `tags` | array de strings | Etiquetes de navegació. |
| `estat` | string | `vigent`, `esborrany`, `obsolet` o `arxivat`. |

Pots afegir camps opcionals si ho necessites (per exemple, `subtitle`, `cycle`, `center`, `academic_year` o `legal_framework`).

---

## 4 · Format del camp id

[Defineix el patró: {CODI}-{ÀMBIT}-{NN}]

```
{CODI}-{ÀMBIT}-{NN}
```

| Component | Descripció | Exemple |
|:---|:---|:---|
| `CODI` | Prefix curt del projecte o cicle. | `EX` |
| `ÀMBIT` | Domini o subsistema. | `MOC`, `UD1`, `AEA` |
| `NN` | Número seqüencial de dues xifres. | `00`, `01` |

**Exemples vàlids:**
- `EX-MOC-00` — el MOC arrel del vault
- `EX-UD1-00` — la unitat didàctica 1
- `EX-AEA-01` — la fitxa d'activitat 1

El nom del fitxer `.md` ha de coincidir amb l'`id`, amb l'extensió `.md` afegida.

---

## 5 · Ubicació dels fitxers

[Estructura de carpetes recomanada]

```
El-teu-vault/
├── 00-moc/            → MOC i índexos
├── 01-unitats/        → UnitatDidactica
├── 02-activitats/     → FitxaAEA
├── 03-guies/          → Guia, Protocol
├── 04-glossaris/      → Glossari
└── TRANSVERSALS/      → La teva Convenció i documents de sistema
```

---

## 6 · Enllaços interns

[Sintaxi: [text](./ruta.md)]

Els enllaços interns es fan amb **ruta relativa** des del fitxer origen:

```markdown
[text](./01-unitats/EX-UD1-00.md)
```

---

## 7 · Com ampliar aquesta Convenció

[Passos per afegir un tipus nou]

1. **Detecta la necessitat:** un node existent no encaixa en cap dels tipus de §2.
2. **Documenta el cas:** explica al node per què cap tipus existent és adequat.
3. **Proposa l'ampliació:** incrementa la versió de la Convenció i afegeix el tipus nou amb una definició breu a §2.
4. **Registra el canvi:** afegeix una fila a l'historial de canvis del document.
5. **Verifica dependències:** mira si el tipus nou afecta altres documents del vault.
6. **Segella la nova versió:** canvia el sufix de versió i actualitza la data.

---

**Fi del document.**

*Versió V1.0.1-Esborrany*
