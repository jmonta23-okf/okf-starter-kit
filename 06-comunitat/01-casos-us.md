# Casos d'ús

Tres docents, dues etapes, dos marcs legals i una co-docent sense la qual res d'això seria com és. Tots han fet servir OKF per resoldre un problema real, i aquí els explico tal com van anar.

No són un estudi d'impacte ni una vitrina: són proves artesanals fetes amb companys, entre hores o sopant. M'interessa més el que hi ha grinyolat que el que ha sortit bé.

**DOI:** [10.5281/zenodo.23823819](https://doi.org/10.5281/zenodo.23823819) · **Repositori:** [github.com/jmonta23-okf/okf-starter-kit](https://github.com/jmonta23-okf/okf-starter-kit)

> **Nota de privacitat.** Faig servir inicials i no esmento cap centre. Això redueix la possibilitat d'identificar ningú, però no l'elimina, i per això he deixat fora tot el que no calia per entendre cada cas.

---

## El factor Montse: l'origen del Paquet LLM

Abans dels tres casos hi ha una persona que no va crear cap vault i sense la qual el kit no seria el que és: la **Montse G.**

L'agost de 2026 vaig muntar el graf del cicle TCAI (Cures Auxiliars d'Infermeria) i el vaig començar a operar amb IA. Feia bateries de *prompts*, les polia i les hi passava a ella, la meva co-docent del torn de tarda. I la Montse s'atabalava. Era perfectament normal: jo li passava una enginyeria que tenia sentit al meu cap tecno-friqui, i ella només volia preparar una bona classe.

Aquell bany de realitat em va fer veure que el sistema fallava si exigia que tothom fos com jo. D'aquí va néixer el **Paquet LLM**: una recepta oberta, transparent i en text pla que encapsula les instruccions perquè qualsevol company pugui treballar amb la IA. La Montse pot obrir el fitxer, llegir-lo, entendre què li demanem a la màquina i retallar o canviar una línia si vol una activitat diferent.

Ella és la veritable usuària del sistema. El fa servir perquè funciona, i ens permet anar harmonitzats al matí i a la tarda sense que la tecnologia l'angoixi.

**Què en trec.** El kit s'ha de poder fer servir sense ser tecno-friqui. Si només el pot fer servir qui l'ha construït, no serveix.

---

## Benet M.: un mòdul de Química en menys d'una setmana (FP)

**Context.** Docent novell de FP, amb un mòdul de Química: una família professional molt allunyada de la meva (Sanitat). Els materials que havia heretat eren dispersos i incomplets, sense cap mapa general del mòdul. No era un cas excepcional. És el més habitual: el docent nou que hereta una carpeta en lloc d'un sistema.

**Repte.** Estructurar un mòdul sencer **només a partir del currículum oficial** (resultats d'aprenentatge, criteris d'avaluació, hores, continguts) i tenir-lo a punt per fer classe en menys d'una setmana.

**Què vam fer.**

- Un graf complet del mòdul: un node MOC com a porta d'entrada, nodes de crèdit per a cada unitat i el catàleg curricular com a font de veritat.
- **10 activitats minutades**, cadascuna amb la seva durada, el criteri d'avaluació vinculat i l'instrument.
- Criteris oficials traduïts a operacions concretes del laboratori, i taules d'avaluació completes amb pesos i instruments.
- **Paquets LLM** per generar presentacions HTML interactives per a cada unitat i fitxes de pràctiques de laboratori. Hi vam aplicar el marc MIAE: la IA proposava, en Benet ho reconstruïa i ho decidia.

**Com va anar.** En Benet va començar a fer classe la setmana següent amb la programació tancada, els criteris vinculats i els materials de les primeres sessions a punt.

**Què en trec.** L'estructura no depèn de la família professional de qui l'ha creada: jo no domino la Química, i tot i així vam poder bastir el mòdul perquè l'estructura venia de la norma. El contingut científic i les decisions sobre la matèria eren seves, no meves. És un sol cas, però és el que volia comprovar.

---

## César G.: crear el vault i mantenir-lo tu (FP)

**Context.** Docent de Sanitat amb un mòdul propi. No volia mirar-s'ho des de fora: volia aplicar OKF al seu mòdul. La seva pregunta no era «com funciona això?», sinó «com ho faig servir jo sense dependre de ningú?».

**Repte.** Crear un vault autònom des de zero, a partir del currículum oficial i la seva programació, i mantenir-lo ell a partir d'aquell moment.

**Què vam fer.**

- Un curs formatiu de **9 mòduls (M0-M8)** que recorria tot el sistema: del concepte de node al validador, passant per les convencions de nomenclatura, les plantilles, els Cores i els Paquets LLM.
- Cada mòdul acabava amb una pràctica sobre el seu propi mòdul, de manera que el vault creixia mentre ell aprenia.
- Un **Paquet LLM final** que permetia generar el vault sencer a partir de les dades oficials, el mateix mecanisme que fa servir el kit per convertir un currículum en un graf.

**Com va anar.** Un vault de **59 nodes interconnectats que passen el validador sense errors**. Quan va acabar el curs, ja no em necessitava per mantenir-lo, ampliar-lo ni corregir-lo. Això era exactament el que buscàvem.

**Què en trec.** El kit s'aprèn: no cal ser enginyer ni el seu autor. Dit això, «sense errors» vol dir que el graf compleix les regles de forma, no que el contingut sigui impecable. Això només ho pot dir qui domina la matèria, que és ell.

---

## Anna C.: Pedagogia Terapèutica i privacitat de menors (Primària)

**Context.** Mestra de Pedagogia Terapèutica a primària (1r-6è, tres cicles), amb les àrees de Matemàtiques i Llengua Catalana. La seva feina és de les més denses del sistema: adaptacions curriculars, plans de suport individualitzat (PI), informes d'avaluació i coordinació amb tutors i famílies.

**Repte.** Estructurar-ho tot en un vault amb una condició afegida: **privacitat reforçada**, perquè el material conté dades de menors. No es podien tractar els PI com si fossin apunts de classe.

**Què vam fer.**

- Un vault de **62 fitxers** alineats amb el core català (el nucli LOMLOE del kit, que fixa les regles mínimes per a l'educació bàsica).
- **Quatre tipus de node propis** de Pedagogia Terapèutica, que el kit no portava de sèrie i que ella va definir: `PlaSuportIndividualitzat`, `AdaptacioCurricular`, `SequenciaDidactica` i `InformeAvaluacio`.
- **Regles de privacitat explícites**: els nodes públics declaren `dades_personals: false`, els que tenen dades sensibles porten `anonimitzat: true`, i els PI i els informes tenen visibilitat `restringida`.
- Un `04_Protocol_Governanca.md` que fixa qui pot veure què i com es tracten les dades, inspirat en el que un centre tindria en un pla de protecció de dades.

**Com va anar.** Un vault complet amb governança formal, on la privacitat va ser una condició de disseny des del primer dia i no una cosa afegida al final. L'Anna no va haver de triar entre organitzar i protegir.

**Què en trec.** El sistema serveix també fora de la FP, amb un altre marc legal (LOMLOE) i amb un alumnat molt més vulnerable. Les regles del vault no substitueixen la política de protecció de dades del centre ni el criteri de la mestra: són una barrera addicional, no l'única.

> El detall tècnic d'aquest vault (tipus de node, convenció, protocol) és al `PTE-HANDOFF-00`.

---

## En resum

| | Etapa | Marc legal | Repte | Com va anar |
|:---|:---|:---|:---|:---|
| **Montse G.** (TCAI) | FP | LOE | Treballar amb IA sense ser perfil tècnic | Va fer néixer el Paquet LLM |
| **Benet M.** (Química) | FP | LOE | Un mòdul sencer des de zero en menys d'una setmana | 10 activitats minutades, mòdul operatiu |
| **César G.** (Sanitat) | FP | LOE | Aprendre OKF i crear un vault propi | 59 nodes que passen el validador |
| **Anna C.** (PT) | Primària | LOMLOE | Adaptacions i PI amb privacitat de menors | 62 fitxers amb governança |

## Quatre idees que se'n desprenen

1. **El currículum oficial és una bona font de veritat.** Els tres casos parteixen del mateix punt: el document normatiu. L'estructura la dona la norma i el docent hi posa la vida.
2. **La privacitat es dissenya des del principi.** No es posen contrasenyes al final, es defineix la visibilitat de cada node des del primer dia.
3. **L'autonomia s'aprèn.** El cas d'en César mostra que el kit es pot ensenyar: 9 mòduls, un vault propi i cap dependència al final.
4. **El factor humà dona sentit a la tecnologia.** La Montse no va crear cap vault, però la seva sinceritat va obligar a repensar el sistema.

## Com llegir aquests casos

Són els d'un sol observador, jo, i cal llegir-los amb aquest límit al cap:

- Les xifres (10 activitats, 59 nodes, 62 fitxers) vénen dels vaults reals, i el validador del kit comprova la forma, no la veritat del contingut.
- No hi ha cap avaluació externa. Són tres docents i una co-docent que ho han provat, no una mostra.
- Cap dels casos no promet transformacions instantànies, ni substitueix la feina docent: el kit la fa possible, no la fa per tu.

## Glossari mínim

- **Node**: fitxer Markdown amb un bloc de dades (*frontmatter*) que el descriu. La peça bàsica del graf.
- **Vault**: el conjunt de nodes interconnectats d'un docent o d'un projecte.
- **Core**: el nucli normatiu que fixa les regles mínimes d'un àmbit (Català/LOMLOE, FP/LOE).
- **Visibilitat**: el camp que controla qui pot veure un node (`publica`, `interna`, `restringida`…).
- **Validador**: l'eina que comprova que tots els nodes compleixen les regles. «0 errors» vol dir que el graf és vàlid de forma, no que el contingut sigui correcte.

## I tu?

Cap dels quatre va esperar que algú els resolgués el problema. La Montse va dir «això no funciona» i em va fer repensar el sistema. En Benet va agafar el currículum i una setmana de feina. En César va fer els 9 mòduls. L'Anna va dissenyar la privacitat des del primer dia.

El cas de la teva matèria, la teva etapa i el teu alumnat encara no hi és, i és el pròxim que s'hi pot afegir. Si vols explicar-lo, obre un issue al [repositori](https://github.com/jmonta23-okf/okf-starter-kit/issues) o escriu-me. El taller és obert.
