"""
Conformitat estricta amb OKF v0.3 sobre el repositori real (abast /, respectant
/.okfignore). Converteix en un test permanent i reproduïble al CI la
verificació estricta que el Bloc 3/3 va fer amb un script temporal.

Escaneja TOTS els .md del repo (fora de les carpetes de /.okfignore i dels
directoris ocults) i en classifica cada un en un dels tres buckets de la regla
d'exclusió per defecte de l'especificació v0.3:

  - `index.md`          -> ha de declarar okf_version "0.3" + title/description/
                           license i tots els enllaços relatius han de resoldre.
  - .md amb `type:`     -> YAML 1.2 parsejable (BOM, claus duplicades i errors
                           inclosos via `validar_yaml.extreure_yaml`), enllaços
                           relatius del cos (fora de blocs de codi) resolts,
                           `superseded_by` (des d'arrel `/` o relatiu al fitxer)
                           resolt i `sources[].resource` resolt.
  - .md sense `type:`   -> s'omet sense error (README, CHANGELOG, CONTRIBUTING,
                           LICENSE, manuals): no són nodes OKF v0.3.

Els camins `/`-anchored (p. ex. `/README.md`) es resolen des de l'arrel del
bundle, com fa el validador per a `superseded_by`.
"""

import os
import re
from pathlib import Path

import validar_yaml as v

REPO_ARREL = Path(__file__).resolve().parent.parent

# Llocs fixos que han d'estar sempre en scope.
INDEX_MINIM = 4  # arrel + 02-exemple-complet + 05-exemples-minims + 07-exemple-mp1519
NODES_MINIM = 32
SOURCES_MINIM = 6  # les 6 fonts que declara 11-conformitat-okf-v03.md


def _dirs_okfignore():
    """Directoris exclosos segons `/.okfignore` (convenció comunitària no
    normativa de l'especificació v0.3)."""
    excl = set()
    p = REPO_ARREL / ".okfignore"
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                excl.add(line.rstrip("/"))
    return excl


def _fitxers_md_en_scope():
    """Tots els .md del repo fora de /.okfignore i dels directoris ocults."""
    excl = _dirs_okfignore()
    out = []
    for root, dirs, files in os.walk(REPO_ARREL):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in excl]
        for f in files:
            if f.endswith(".md"):
                out.append(Path(root) / f)
    return sorted(out)


def _resoldre(ref, directori):
    """Resol una referència: `/`-anchored des de l'arrel del bundle, altrament
    relativa al directori del fitxer. Talla els fragments '#...'."""
    ref = ref.split("#", 1)[0].strip()
    if not ref:
        return None
    if ref.startswith("/"):
        return os.path.normpath(os.path.join(REPO_ARREL, ref.lstrip("/")))
    return os.path.normpath(os.path.join(directori, ref))


def _enllacos_trencats(ruta):
    """Enllaços relatius del cos (fora de blocs de codi ```) que no resolen."""
    cos = v.extreure_cos_md(str(ruta))
    trencats = []
    in_fence = False
    for num, line in enumerate(cos.split("\n"), 1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)\)", line):
            desti = m.group(1)
            if desti.startswith(("http://", "https://", "mailto:", "#")):
                continue
            p = _resoldre(desti, ruta.parent)
            if p and not os.path.exists(p):
                trencats.append((desti, num))
    return trencats


def _superseded_trencats(data, ruta):
    """Camins de `superseded_by` (string o llista) que no resolen."""
    ss = data.get("superseded_by")
    if ss is None:
        return []
    refs = ss if isinstance(ss, list) else [ss]
    trencats = []
    for ref in refs:
        if not isinstance(ref, str) or not ref.strip():
            continue
        if ref.startswith(("http://", "https://", "mailto:", "#")):
            continue
        p = _resoldre(ref, ruta.parent)
        if p and not os.path.exists(p):
            trencats.append(ref)
    return trencats


def _sources_trencats(data, ruta):
    """`sources[].resource` que no resol a un fitxer real."""
    srcs = data.get("sources")
    if not isinstance(srcs, list):
        return []
    trencats = []
    for i, src in enumerate(srcs):
        if not isinstance(src, dict) or not src.get("resource"):
            continue
        res = src["resource"]
        if res.startswith(("http://", "https://", "mailto:", "#")):
            continue
        p = _resoldre(res, ruta.parent)
        if p and not os.path.exists(p):
            trencats.append((i, res))
    return trencats


def test_index_md_conformes_a_v03():
    """Tots els index.md: frontmatter v0.3 (okf_version/title/description/license)
    i enllaços relatius del cos resolts."""
    errors = []
    indexes = [p for p in _fitxers_md_en_scope() if p.name == "index.md"]
    assert len(indexes) >= INDEX_MINIM

    for p in indexes:
        data, errs = v.extreure_yaml(str(p))
        if data is None:
            errors.append(f"{p}: YAML no parsejable ({errs})")
            continue
        for k in ("okf_version", "title", "description", "license"):
            if not data.get(k):
                errors.append(f"{p}: falta '{k}'")
        if data.get("okf_version") != "0.3":
            errors.append(f"{p}: okf_version = {data.get('okf_version')!r}")
        tr = _enllacos_trencats(p)
        if tr:
            errors.append(f"{p}: enllaços relatius trencats: {tr}")

    assert not errors, "\n".join(errors)


def test_nodes_amb_type_parseables_i_sense_enllacos_trencats():
    """Tot .md amb `type:`: YAML parsejable, enllaços del cos (fora de blocs de
    codi) resolts i superseded_by resolt."""
    errors = []
    nodes = 0
    for p in _fitxers_md_en_scope():
        if p.name == "index.md":
            continue
        data, errs = v.extreure_yaml(str(p))
        if not isinstance(data, dict) or "type" not in data:
            continue
        nodes += 1
        if errs:
            errors.append(f"{p}: YAML: {errs}")
        tr = _enllacos_trencats(p)
        if tr:
            errors.append(f"{p}: enllaços del cos trencats: {tr}")
        sst = _superseded_trencats(data, p)
        if sst:
            errors.append(f"{p}: superseded_by trencat: {sst}")

    assert nodes >= NODES_MINIM
    assert not errors, "\n".join(errors)


def test_md_sense_type_s_ometen_sense_error():
    """Els .md sense `type:` (README, CHANGELOG, CONTRIBUTING, LICENSE, manuals,
    HANDOFF...) s'ometen sense error: no són nodes OKF v0.3."""
    esperats = {"README.md", "CHANGELOG.md", "CONTRIBUTING.md", "LICENSE.md"}
    omesos = []
    for p in _fitxers_md_en_scope():
        if p.name == "index.md":
            continue
        data, _errs = v.extreure_yaml(str(p))
        if not isinstance(data, dict) or "type" not in data:
            omesos.append(p)
    assert esperats <= {p.name for p in omesos}
    # L'absència de `type:` no exigeix frontmatter: cap error en classificar-los.


def test_sources_resource_resolen_a_fitxers_reals():
    """Tot `sources[].resource` (com a 11-conformitat-okf-v03.md) resol a un
    fitxer real del repo."""
    errors = []
    trobades = 0
    for p in _fitxers_md_en_scope():
        if p.name == "index.md":
            continue
        data, _errs = v.extreure_yaml(str(p))
        if not isinstance(data, dict):
            continue
        trencats = _sources_trencats(data, p)
        trobades += sum(
            1 for src in (data.get("sources") or [])
            if isinstance(src, dict) and src.get("resource")
        )
        if trencats:
            for i, res in trencats:
                errors.append(f"{p}: sources[{i}].resource '{res}' no resol")

    assert trobades >= SOURCES_MINIM
    assert not errors, "\n".join(errors)