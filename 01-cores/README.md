# Nuclis (Cores)

Aquesta carpeta conté els dos nuclis normatius del OKF Starter Kit. Un **core** (o nucli) és un document que fixa les regles mínimes que han de complir tots els vaults d'un mateix àmbit educatiu. Garanteixen que dos vaults diferents siguin **interoperables**.

## Els dos Cores

| Core | Àmbit | Marc legal |
|:---|:---|:---|
| **`OKF-CORE-CATALA-00.md`** | Educació bàsica (infantil, primària, ESO, CFGB) | LOMLOE (Decret 175/2022 + Decret 480/2024) |
| **`OKF-CORE-FP-00.md`** | Formació Professional (grau bàsic, mitjà i superior) | LOE (LO 3/2022 + RD 659/2023) |

Són **germans**: comparteixen els 9 tipus universals i els 8 camps universals, però tenen marcs legals diferents. Un vault de FP pot heretar el Core FP; un vault d'ESO pot heretar el Core Català. Tots dos comparteixen la mateixa estructura bàsica.

## Com es fan servir?

Els Cores **no es modifiquen**. Són documents de referència. Quan crees el teu propi vault:

1. **Llegeix** el Core del teu àmbit per entendre quins tipus de node pots fer servir i quins camps són obligatoris.
2. **Crea la teva Convenció de Nomenclatura** (a partir de `04-plantilles/PLANTILLA-ConvencioNomenclatura.md`) i fes que **hereti** el Core. Al camp `## 2 · Tipus de node vàlids` de la teva Convenció, pots dir: *"A més dels tipus universals del Core Català, aquest vault afegeix els tipus següents..."*.
3. **Valida** amb el validador del kit (`03-eines/validar_yaml.py`). El validador accepta els tipus dels dos Cores.

## Per què dos Cores i no un?

Perquè el marc legal és diferent:
- **LOMLOE** (educació bàsica) fa servir "competències específiques", "sabers", "situacions d'aprenentatge".
- **LOE** (FP) fa servir "resultats d'aprenentatge", "criteris d'avaluació", "mòduls professionals".

Si féssim un sol Core, hauríem de triar una terminologia i forçar l'altra a adaptar-s'hi. Amb dos Cores germànics, cada àmbit té el seu vocabulari, però comparteixen l'estructura.

## Notes sobre aquests Cores

- **Són una adaptació** dels Cores originals del projecte TCAI-OKF. S'han eliminat les referències a altres vaults (ESO, PTE, SAD, TCAI, CURS-FP) que no existeixen en aquest kit.
- **La marca s'ha neutralitzat** (`center: "Centre educatiu (Catalunya)"`) perquè el kit és genèric. Si vols fer servir el teu centre, canvia'l al teu vault, no aquí.
- **Si el teu centre té un marc legal diferent** (per exemple, batxillerat, formació d'adults, ensenyaments artístics), pots crear el teu propi Core seguint l'estructura d'aquests dos.

## Llicència

Els dos Cores es distribueixen sota **CC BY-SA 4.0**, com la resta de contingut del kit.