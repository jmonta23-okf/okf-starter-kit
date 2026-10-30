# Preguntes freqüents (FAQ)

Les respostes als dubtes més habituals quan un docent descobreix el mètode OKF.

---

## 1 · Sobre el mètode i el kit en general

### Per què hauria d'invertir temps a fer OKF si ja tinc els meus documents a Drive o a carpetes?

Perquè el teu coneixement és **el teu actiu professional**, no una propietat del centre ni d'una plataforma al núvol. Invertir temps a estructurar el teu curs amb OKF et dona quatre guanys immediats que les carpetes d'ofimàtica mai et donaran:

1. **Portabilitat total:** Quan canviïs de centre o de curs, t'emportes la teva carpeta al portàtil nou i en una tarda tens la feina muntada i ubicada. No tornes a començar de zero.
2. **Demostrabilitat i traçabilitat:** Davant d'una coordinació o d'una revisió pedagògica, no has d'obrir deu carpetes per justificar una nota: mostres el graf i ensenyes la traçabilitat directa (Criteri d'Avaluació $\rightarrow$ Activitat $\rightarrow$ Rúbrica $\rightarrow$ Instrument de qualificació).
3. **Reaprofitament real:** Adaptar un mòdul al curs següent és qüestió d'un matí ajustant dates i criteris als nodes corresponents, no de passar-te tres setmanes refent documents de Word de 80 pàgines.
4. **Operativitat (El taller docent):** Els teus materials deixen de ser apunts morts en un calaix. Amb els **Paquets LLM**, els teus nodes es converteixen en la matèria primera per generar presentacions d'aula, fitxes d'exercicis, adaptacions per a necessitats educatives o proves summatives en minuts, mantenint sempre el teu criteri i control.

Que el centre també se'n beneficiï (mitjançant un traspàs net si algun dia marxes) és una **conseqüència** positiva, no la raó principal per la qual val la pena fer-ho. El primer beneficiari ets tu.

### Modifico el currículum oficial si faig servir OKF?

**No, en absolut.** El currículum oficial (el decret publicat al DOGC o al BOE) és prescriptiu i és el primer nivell de concreció. A OKF, aquest marc legal queda fixat de manera immutable a la carpeta `01-cores/`.

El que tu construeixes i governes amb OKF és la teva **Programació Didàctica d'aula** (el segon i tercer nivell de concreció): com contextualitzes aquests criteris, quines activitats d'aprenentatge dissenyes, quins instruments d'avaluació tries i quins protocols de taller apliques. El currículum oficial és el codi genètic comú; la teva programació en graf és l'organisme viu que s'adapta al teu grup.

### Com li presento la programació a Inspecció o a la direcció del centre si em demanen el document oficial?

A Inspecció no li has d'entregar el teu vault ni carpetes amb fitxers Markdown. A OKF, **el graf és la teva font de veritat interna, i la programació oficial és només una vista derivada**.

A través dels Paquets LLM (o d'eines senzilles de conversió com Pandoc o scripts d'Apps Script), pots compilar els nodes del teu mòdul en un document formal de Word (`.docx`), Google Docs o PDF amb la portada institucional, l'índex oficial de la Guia de programació i totes les taules d'activitats perfectament maquetades. Trigaràs cinc minuts a generar-lo, i tindràs la certesa absoluta que no hi ha cap error de ponderació ni cap criteri inventat.

### És OKF un sistema operatiu?

**Metafòricament sí, literalment no.** OKF no és un programari executable que s'instal·li a la barra de tasques ni gestiona circuits físics. Però fa exactament la mateixa funció que un sistema operatiu: **proporciona una capa d'abstracció estàndard**.

Igual que el sistema operatiu del teu ordinador posa ordre perquè els teus programes no col·lisionin amb el maquinari, OKF posa ordre entre el decret legal i la teva aula perquè les eines (com la IA o els teus propis guions) puguin operar amb precisió.

| Capa d'un Sistema Operatiu | Equivalent a OKF |
|:---|:---|
| **Maquinari** | El decret curricular cru (DOGC / BOE) |
| **Sistema de fitxers** | El vault (nodes en text pla, MOC arrel, enllaços relatius) |
| **Kernel / Estàndards** | Els Cores normatius + la Convenció de Nomenclatura |
| **API i comprovació** | L'esquema YAML + el validador automàtic en Python |
| **Drivers** | Les plantilles canòniques (MOC, UD, FitxaAEA, Protocol...) |
| **Aplicacions d'usuari** | Els Paquets LLM i els generadors de materials d'aula |

Per això en diem «una proposta de sistema operatiu»: no és fum comercial, és una arquitectura neta per a la teva feina.

### Cal saber programar per fer servir OKF?

**No.** El 95% del temps treballaràs escrivint text normal en format Markdown (encapçalaments amb `#`, llistes amb guions i enllaços senzills). 

L'única part tècnica és una línia que s'executa al terminal de l'ordinador per comprovar que no t'hagis deixat cap camp obligatori:

```bash
python3 03-eines/validar_yaml.py --ruta 02-exemple-complet
```

Si no has obert mai un terminal, la [Guia d'inici ràpid (30 minuts)](./04-inici-rapid.md) t'acompanya pas a pas des de zero. La prova és que companys novells que no venien de la informàtica (com el cas d'en **Benet M.** a Química) han estat capaços de desplegar mòduls sencers en pocs dies.

### Quant de temps es triga a implementar un mòdul sencer?

Depèn de la base de la qual parteixis:
* **Entendre el sistema i crear el teu primer node:** 30 minuts (amb l'Inici ràpid).
* **Estructurar un mòdul complet des de zero (amb decrets i 10 activitats):** Entre 15 i 25 hores de feina ben enfocada.
* **El guany:** Un cop estructurat, el manteniment setmanal de les classes es redueix a minuts, i l'inici del curs següent es resol en una sola jornada.

---

## 2 · Sobre la Intel·ligència Artificial i el Taller (MIAE + VCER)

### Puc fer servir OKF sense cap mena d'Intel·ligència Artificial?

**I tant que sí.** OKF és, abans que res, un sistema d'arquitectura del coneixement sobirà. Molts docents l'utilitzen exclusivament per tenir les seves programacions ordenades, auditables i interconnectades a Obsidian o VS Code, sense connectar-hi cap model d'IA.

La IA és només un operador opcional del taller, mai un requisit obligatori.

### Què és un Paquet LLM i per què és diferent d'escriure un prompt a ChatGPT?

Un *prompt* improvisat a ChatGPT sol donar respostes genèriques, amb activitats poc adaptades a la realitat del teu centre i que sovint al·lucinen terminologia d'altres comunitats autònomes o lleis derogades.

Un **Paquet LLM** és un **contracte d'enginyeria pedagògica**:
1. Té accés tancat als teus nodes del vault (la teva font de veritat).
2. Té restriccions expresses que li impedeixen inventar decrets o criteris.
3. Té plantilles de sortida obligatòries (per exemple, generar una presentació en HTML pur de 15 diapositives amb mode ponent i dreceres de teclat, o fitxes en format Word editable).

### Què signifiquen les sigles MIAE i VCER?

Són els dos filtres de qualitat ètica i tècnica que incorporen els Paquets LLM d'OKF:
* **MIAE (Marc per a la Integració de la IA en Educació):** Audita el **procés** de treball. Fixa el nivell de supervisió humana. A OKF treballem amb **Nivell 3** (*esborrany IA + reconstrucció humana*): la IA proposa l'estructura sobre les teves dades, però el docent revisa, ajusta i valida sempre abans d'imprimir o avaluar.
* **VCER ([Vibe Coding Educatiu Responsable](https://vibe-coding-educativo.github.io/vibe-responsable/ca/)):** Audita l'**artefacte resultant** que arriba a l'alumnat. Garanteix que qualsevol aplicació o presentació generada funcioni **100% offline**, no reculli cap dada de l'alumnat, sigui accessible per teclat i s'alliberi amb llicència lliure.

### Amb quins models d'IA és compatible?

El sistema és **agnòstic de model**. Pots copiar el teu Paquet LLM i el context del teu vault a qualsevol eina:
* Models comercials punters: Claude (Anthropic), ChatGPT (OpenAI), Gemini (Google).
* Models lliures o d'execució local: Mistral, Llama, Qwen (executats al teu propi ordinador amb Ollama o LM Studio sense enviar cap byte a internet).

---

## 3 · Sobre la privacitat, les dades i el RGPD

### Les dades de l'alumnat estan protegides amb aquest sistema?

**Absolutament, per disseny.** OKF aplica el principi de *privacitat des del disseny*:
1. El teu vault curricular viu al teu disc dur; no hi ha servidors al núvol emmagatzemant la teva feina.
2. Els nodes d'OKF tracten sobre **currículum, activitats i criteris**, mai sobre expedients personals d'alumnes.
3. El protocol VCER prohibeix que els materials generats facin cap crida externa o recullin telemetria dels estudiants.

### Puc fer servir qualsevol eina d'IA per tractar incidències o notes d'alumnes?

**Molt de compte.** Per a la generació de materials didàctics (activitats, presentacions, rúbriques) no hi ha cap risc de privacitat perquè no es tracten dades de persones.

Ara bé, si mai utilitzes un model per redactar informes d'avaluació individuals o gestionar incidències de convivència:
* **Mai introdueixis noms, cognoms, DNI o dades de salut.**
* Assegura't d'utilitzar eines que compleixin el RGPD europeu i els acords de tractament de dades (DPA) homologats pel Departament d'Educació. Models com DeepSeek, amb servidors sota legislacions opaques que no compleixen els estàndards europeus de protecció de menors, no s'han d'utilitzar mai amb dades d'alumnat.

---

## 4 · Sobre el funcionament tècnic del graf

### Per què alguns camps YAML són en anglès i d'altres en català?

És una decisió d'arquitectura conscient per compatibilitzar la tècnica amb la realitat docent:
* **En anglès (Framework):** `id`, `type`, `title`, `version`, `authors`, `tags`, `academic_year`. Són metadades universals reconegudes per qualsevol estàndard internacional (Dublin Core, GitHub, parsers d'IA).
* **En català (Domini pedagògic):** `data_ultima_actualitzacio`, `credit`, `durada`, `resultats_aprenentatge`, `criteris_avaluacio`, `estat`. És la terminologia curricular que qualsevol docent de Catalunya identifica immediatament.

Pots consultar la justificació completa a l'[Arquitectura del sistema (§4)](./03-arquitectura.md#4--la-convenció-yaml-mixta-en--ca).

### Necessito internet per treballar cada dia?

**No.** El text pla i el validador en Python s'executen completament en local a la teva màquina. Només et caldrà connexió si vols fer còpies de seguretat a un repositori remot de GitHub o si consultes un model d'IA al núvol.

### Què passa si m'equivoco en escriure un node?

No passa res: el validador et cuida les espatlles. Quan executis `python3 03-eines/validar_yaml.py`, el terminal t'indicarà exactament el fitxer, el codi d'error i l'acció que has de fer:

```text
| # | Fitxer                     | Codi | Gravetat | Descripció                              | Acció                 |
|:-:|:---------------------------|:----:|:--------:|:----------------------------------------|:----------------------|
| 1 | 03_MP1519_Fitxa_AEA_1.md   | Y002 | 🔴       | Camp obligatori 'legal_framework' absent| Afegir el camp al YAML |
```

### El validador em diu que un fitxer no comença amb `---`. Com ho soluciono?

El format YAML exigeix que la primera línia absoluta del fitxer sigui exactament els tres guions `---`. Si tens una línia en blanc a l'inici o un espai abans dels guions, el validador donarà l'error `Y001`. Només has d'obrir el fitxer i esborrar la línia en blanc inicial.

### Puc fer servir el kit amb Obsidian o altres editors de text?

**Sí, és l'entorn ideal.** Tot i que pots fer servir VS Code, Sublime Text o el bloc de notes del teu sistema, [Obsidian](https://obsidian.md) és especialment recomanable perquè:
* Renderitza nativament els enllaços interns de Markdown.
* Disposa de la vista de graf (Graph View), on podràs veure visualment com la teva programació es desplega com una xarxa neuronal de nodes connectats.

---

## 5 · Sobre el context i compartir

### El kit és exclusiu per a Formació Professional o per a Catalunya?

**No.** El kit s'ha forjat a la Formació Professional catalana perquè la FP té una estructura curricular molt nítida (RA, CA, continguts i ponderacions), però el mètode és universal:
* Es pot fer servir a **Secundària (ESO), Batxillerat, Primària o la Universitat**.
* Es pot aplicar a qualsevol comunitat autònoma o país: només cal definir el marc normatiu corresponent als `01-cores/`.

### Puc compartir el meu graf amb altres docents o publicar-lo?

I tant, aquesta és l'essència del projecte. El coneixement didàctic guanya valor quan es comparteix:
* Pots compartir una carpeta comprimida en `.zip` amb el substitut que arriba al teu departament.
* Pots crear un repositori obert a GitHub perquè docents de la teva mateixa especialitat d'arreu del territori puguin aprofitar les teves activitats i aportar-hi millores.

Per conèixer com llicenciar i publicar el teu vault, consulta la guia **[Com compartir](./07-com-compartir.md)**.

---

## Encara et queda algun dubte?

* Consulta el **[Glossari canònic](./05-glossari.md)** per aclarir la definició exacta de cada concepte.
* Obre un *issue* o pregunta a la comunitat a través del nostre repositori a GitHub.
```

