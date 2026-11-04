# MP 1519 — Exemple Complet de Desplegament OKF

> **Mòdul Professional 1519: Sistemes d'informació i classificació sanitaris**
> *Cicle Formatiu de Grau Superior en Documentació i Administració Sanitàries (SAD) — Marc LOE*

Aquest directori és l'**exemple complet** del OKF Starter Kit: un mòdul professional sencer organitzat en un graf de text pla i metadades YAML, que demostra l'arquitectura de **dues capes** (catàleg curricular normatiu + fitxes d'avaluació).

## Què conté

El mòdul es desplega en **14 nodes** encapçalats pel MOC:

| # | Fitxer | Tipus | Descripció |
|:--:|:--|:--:|:--|
| **00** | [00_MP1519_MOC.md](./00_MP1519_MOC.md) | `MOC` | Node arrel: dades, pesos dels 8 RAs i mapa de les 5 activitats. |
| **01** | [01_MP1519_Cataleg_Curricular.md](./01_MP1519_Cataleg_Curricular.md) | `CatalegCurricular` | Marc normatiu i 52 CAs oficials (format nou de `criteris:`). |
| **02** | [02_MP1519_Protocol_Avaluacio.md](./02_MP1519_Protocol_Avaluacio.md) | `Protocol` | Sistema d'avaluació (model de tres portes, rúbrica i micro-rúbrica). |
| **03–07** | [03](./03_MP1519_Fitxa_AEA_1.md) a [07](./07_MP1519_Fitxa_AEA_5.md) | `FitxaAEA` | Les 5 activitats, cadascuna amb `instruments_avaluacio` (1 instrument `I1`). |
| **08** | [08_MP1519_Paquet_LLM.md](./08_MP1519_Paquet_LLM.md) | `PaquetLLM` | Contracte d'enginyeria d'IA anti-al·lucinació. |
| **09** | [09_MP1519_Arquitectura_DualUser.md](./09_MP1519_Arquitectura_DualUser.md) | `Guia` | Manual de la IA Co-Docent. |
| **10** | [10_MP1519_Validador_CIE10ES.md](./10_MP1519_Validador_CIE10ES.md) | `EinaTecnica` | Validador de domini determinista (CIE-10-ES). |
| **11** | [11_MP1519_Ecosistema_Automatitzacio.md](./11_MP1519_Ecosistema_Automatitzacio.md) | `EinaTecnica` | Integració amb Google Workspace. |
| **12** | [12_MP1519_Convencio.md](./12_MP1519_Convencio.md) | `ConvencioNomenclatura` | Convenció amb àlies i tipus de família. |
| **13** | [13_MP1519_Handoff.md](./13_MP1519_Handoff.md) | `DocumentHandoff` | Traspàs de curs. |

## Validar l'exemple

Des de l'arrel del repositori:

```bash
python3 03-eines/validar_yaml.py --ruta 02-exemple-complet
```

Ha de donar **0 errors**.

## Auditar la cobertura curricular

```bash
python3 03-eines/validar_yaml.py --ruta 02-exemple-complet --audit
```

Mostra les mètriques de cobertura (CAs al decret, avaluats/coberts, orfes, inexistents, contextualitzats i afegits) i el veredicte COBERT/INCOMPLET.

## Referència

La guia completa de l'arquitectura de dues capes és a [`00-documentacio/09-graf-curricular.md`](../00-documentacio/09-graf-curricular.md).