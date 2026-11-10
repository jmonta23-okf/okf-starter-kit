# RFC-OKF-03: Completitud normativa del graf de dues capes

> **Estat:** Document de planificació (v0.1), implementat a la V1.3.
> **Data original:** 3 de novembre de 2026.
> **Àmbit:** `01-cores/`, `02-exemple-complet/`, `03-eines/`, `04-plantilles/`, `07-exemple-mp1519/`, `09-graf-curricular/`.
> **Compatibilitat:** Core OKF v1.1.0 + Validador v1.2.0 + Guia de Programació LOE (juny 2024).

---

## 1 · Què és aquest document?

Aquest és el **document de planificació** que va originar els canvis de la **V1.3** del kit. Es va escriure el 3 de novembre de 2026, abans de la implementació, i descriu les 9 accions que es van considerar per donar suport normatiu complet al graf de dues capes (catàleg ↔ fitxes AEA).

**No és una especificació vigent.** És un document històric que explica **per què** es van prendre les decisions de la V1.3. La font de veritat és:
- El **codi** (`03-eines/validar_yaml.py`).
- El **CHANGELOG** (`CHANGELOG.md`), secció `[V1.3]`.
- Les **plantilles** (`04-plantilles/`).

**Nota sobre errors coneguts:** el document original v0.1 contenia algunes imprecisions (per exemple, confonia `Y035` amb el mismatch de versió a §4.2 i §6.3). Aquest resum **no les reprodueix**: recull només les decisions que es van implementar i les que es van descartar, amb els motius.

---

## 2 · Context: per què calia la V1.3?

La V1.2 havia introduït l'arquitectura de dues capes (catàleg + fitxes AEA), però tenia tres limitacions:

1. **Els criteris d'avaluació eren llistes de strings**, no podien expressar si un criteri era contextualitzat, afegit o tenia un origen concret.
2. **Els instruments d'avaluació eren rutes a documents**, no estructuraven quins criteris avaluava cada instrument.
3. **L'auditoria no distingia** entre CAs coberts per fitxes analítiques i fitxes de síntesi, ni detectava CAs afegits no referenciats.

La V1.3 va resoldre aquestes tres limitacions amb un **format nou de criteris i instruments**, i amb **nous codis d'error** (Y040-Y052).

---

## 3 · Les 9 accions del RFC (6 adoptades, 3 rebutjades)

El RFC original proposava 9 accions. Després de la revisió, se'n van adoptar 6 i se'n van rebutjar o modificar 3:

| Acció original | Decisió | Motiu |
|:---|:---|:---|
| Eliminar `naturalesa` | ❌ **Suavitzar** | És una salvaguarda anti-joc de números; es fa opcional i emet warning (`Y046`) |
| Eliminar `cataleg_versio` | ⚠️ **Deprecar** | Cost *breaking* alt; es depreca a la v1.3, s'elimina a la v1.4 |
| Eliminar `--strict-versio` | ⚠️ **Deprecar** | No-op amb warning |
| Eliminar Y035/Y036 | ⚠️ **Deprecar** | Warning en lloc d'error |
| Implementar `contextualitzat` | ✅ **Sí** | Base normativa clara (Requisit C de la Guia) |
| Implementar CAs afegits (`codi: null`) | ✅ **Sí** | Base normativa clara (Requisit D de la Guia) |
| Unificar font de veritat CAs (frontmatter XOR cos) | ❌ **No** | Les tres opcions eren pitjors que l'estat actual |
| Implementar `instruments_avaluacio` estructurat | ✅ **Sí** | Compleix Requisit E de la Guia (traçabilitat CA→Instrument) |
| Notació decimal com a canònica | ✅ **Sí** | Simplifica la validació; les lletres són vista derivada |

---

## 4 · Què es va implementar a la V1.3

Els canvis implementats es poden resumir en 4 blocs:

### 4.1 · Format nou de `criteris:`

Els criteris d'avaluació dels catàlegs passen de **llista de strings** a **llista de diccionaris** amb 6 camps:

```yaml
criteris:
  RA1:
    - codi: "1.1"
      guia: "1a"
      descripcio: "[Text literal del decret]"
      contextualitzat: false
      afegit: false
      origen: null
```

Els CAs afegits poden tenir un `id` estable (format `{catalog_id}-RA{N}-ADD-{NN}`) per poder ser referenciats des de les fitxes.

### 4.2 · Format nou d'`instruments_avaluacio`

Els instruments de les fitxes AEA passen de **llista de rutes** a **llista de diccionaris** amb 3 camps:

```yaml
instruments_avaluacio:
  - codi: "I1"
    descripcio: "Observació competencial amb llista de control"
    criteris: ["1.1", "1.2"]
```

### 4.3 · Nous codis d'error (Y040-Y052)

| Codi | Descripció | Severitat |
|:---|:---|:---:|
| `Y040` | `contextualitzat` no és boolean | 🟠 Alta |
| `Y042` | `codi: null` sense `afegit: true` | 🔴 Crític |
| `Y043` | `afegit: true` sense `guia` | 🔴 Crític |
| `Y044` | `afegit` + `contextualitzat` redundants | 🟡 Mitjana |
| `Y045` | CA afegit no referenciat per cap FitxaAEA | 🟡 Mitjana |
| `Y046` | CA només cobert per fitxes de síntesi | 🟡 Mitjana |
| `Y048` | `criteris[RA]` no és una llista | 🟠 Alta |
| `Y050` | Codi d'instrument duplicat | 🟠 Alta |
| `Y051` | Instrument sense cap criteri | 🟡 Mitjana |
| `Y052` | Criteri sense cap instrument | 🟡 Mitjana |

### 4.4 · `--audit` actualitzat

L'auditoria curricular ara calcula:
- `CAs coberts` (analítics + síntesi).
- `CAs contextualitzats (*)`.
- `CAs afegits pel docent`.
- `Y045` i `Y046` per catàleg (no globalment).

Es mantenen `CAs avaluats (analítics)` i `Mismatch de versió` per compatibilitat enrere amb `status_snapshot.py`.

---

## 5 · Errors coneguts del document original

El document original v0.1 tenia algunes imprecisions que es van corregir durant la implementació:

- **`Y035` no és el mismatch de versió.** És l'àlies de tipus duplicat. El mismatch de versió no té codi Y; és una mètrica de `--audit`.
- **La taula de les 9 accions** barrejava `Y035` amb el mismatch de versió a §4.2 i §6.3.
- **El recompte de codis** al document original era incorrecte (28 → 38, no 28 → 30).

Aquests errors **no s'han reproduït** en aquest resum. La font de veritat és el codi i el CHANGELOG.

---

## 6 · Enllaços

- **CHANGELOG:** [`CHANGELOG.md`](../CHANGELOG.md), secció `[V1.3]`.
- **Plantilla de catàleg:** [`04-plantilles/PLANTILLA-CatalegCurricular.md`](../04-plantilles/PLANTILLA-CatalegCurricular.md).
- **Plantilla de fitxa AEA:** [`04-plantilles/PLANTILLA-FitxaAEA.md`](../04-plantilles/PLANTILLA-FitxaAEA.md).
- **Validador:** [`03-eines/validar_yaml.py`](../03-eines/validar_yaml.py).
- **Graf curricular:** [`00-documentacio/09-graf-curricular.md`](09-graf-curricular.md).

---

## 7 · Referències

- **RFC-OKF-03 v0.1** (document original, fora del repo).
- **HANDOFF-09** (pre-V1.3) i **HANDOFF-10** (post-V1.3), a `~/Documents/OKF-CATALA/okf-handoffs/`.
- **Reial Decret 768/2014** (MP 1519).
- **Guia de Programació LOE** (juny 2024).