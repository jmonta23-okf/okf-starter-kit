# Casos d'ús

Tres docents, tres etapes, tres marcs legals. Tots han fet servir OKF per resoldre un
problema real. Aquests són els seus casos.

> **Nota de privacitat.** Els noms són inicials i els centres no s'esmenten, per respectar la privacitat de les persones i dels seus entorns de treball. El kit també s'ho pren seriosament: vegeu el cas de l'Anna, on la privacitat de l'alumnat és una condició de disseny, no un afegit.

---

## Cas 1 — Benet M. i el repte de la Química (MP1257, FP)

### Context

Docent novell de Formació Professional. El seu mòdul pertany a la família d'Operacions
de Laboratori Químic — completament aliena a la de l'autor del kit (Sanitat). Els
materials que havia heretat eren dispersos, incomplets i sense cap estructura
aprofitable: fitxers de noms ambigus, versions que es contradicien i cap mapa general
del mòdul.

En Benet no era un cas excepcional: era el cas **habitual** del docent nou que hereta
una carpeta, no un sistema.

### Repte

Estructurar un mòdul sencer des de zero, a partir **exclusivament del currículum
oficial** — la font normativa: resultats d'aprenentatge, criteris d'avaluació, hores,
continguts — i tenir-lo a punt per començar a impartir classe en **menys d'una
setmana**.

### Què es va fer

- Es va aixecar el graf complet del mòdul amb l'arquitectura OKF: el node MOC com a porta d'entrada, els nodes de crèdit per a cada unitat, i el catàleg curricular com a font de veritat.
- **10 activitats minutades**: cada activitat amb la seva durada, el seu criteri d'avaluació vinculat i el seu instrument.
- **Criteris contextualitzats**: els criteris oficials del currículum, traduïts a operacions concretes del laboratori químic.
- **Taules d'avaluació** completes, amb pesos i instruments, llestes per a la memòria que exigeix la Inspecció.
- **Paquets LLM** per generar les **presentacions HTML interactives** de cada unitat i les **fitxes de pràctiques de laboratori** (amb el marc MIAE: la IA proposava, en Benet reconstruïa i decidia).

### Resultat

> En Benet va poder tenir la programació oficial tancada i estar operatiu, segur i impartint classe amb rigor en menys d'una setmana.

No "va trigar una setmana a començar a preparar": va començar la setmana següent amb la
programació tancada, els criteris vinculats i els materials de les primeres sessions a
punt.

### Què demostra

El sistema és **transferible**: no depèn de la família professional de qui l'ha creat.
Si el currículum oficial és la matèria primera i l'arquitectura OKF és el motlle, el
resultat no depèn del coneixement previ del docent sobre la matèria — en Benet no era
químic de laboratori, i tanmateix el mòdul era rigorós perquè la **font normativa** ho
era.

---

## Cas 2 — César G. i l'autonomia docent (MP1523, FP)

### Context

Docent de Sanitat amb un mòdul propi, que volia aprendre OKF no com a espectador, sinó
per aplicar-lo al seu propi mòdul. La seva pregunta no era "com funciona això?", sinó
"com ho faig servir per al meu crèdit, sense dependre de ningú?".

### Repte

Crear un **vault autònom des de zero**, amb el currículum oficial i la seva pròpia
programació, i mantenir-lo ell mateix a partir d'aquell moment.

### Què es va fer

- Va rebre un curs formatiu de **9 mòduls (M0-M8)** que recorria tot el sistema: del concepte de node al validador, passant per convencions de nomenclatura, plantilles, Cores i Paquets LLM.
- Cada mòdul del curs acabava amb una pràctica sobre el seu propi mòdul, de manera que el vault creixia mentre aprenia.
- El curs acabava amb un **PaquetLLM final** que permetia generar el vault sencer des de les dades oficials — el mateix mecanisme que fa servir el kit per convertir un currículum en un graf.

### Resultat

> Un vault autònom de 59 nodes interconnectats i validats amb 0 errors.

L'autonomia era real: en acabar el curs, en César no necessitava l'autor del kit per a
res. Mantenir, ampliar i corregir el seu vault era feina seva — i això era exactament el
punt.

### Què demostra

El sistema és **aprensible**: no cal ser l'autor del kit, ni cap enginyer, ni cap
"superusuari". Un professor amb ganes de fer les coses bé pot tenir el seu propi vault
funcionant al cap d'un curs de formació. El coneixement del kit no és un misteri: és una
metodologia que s'ensenya, com qualsevol altra.

---

## Cas 3 — Anna C. i la Pedagogia Terapèutica (PTE, Primària)

### Context

Mestra de Pedagogia Terapèutica d'educació primària (1r-6è, tres cicles: Inicial, Mitjà
i Superior), amb les àrees de Matemàtiques i Llengua Catalana. La seva feina és de les
més denses del sistema educatiu: **adaptacions curriculars**, **plans de suport
individualitzat (PI)**, **informes d'avaluació**, coordinació amb tutors i famílies.

### Repte

Estructurar tot això en un vault... **amb una condició afegida**: privacitat reforçada,
perquè el material conté dades de menors. L'Anna no podia organitzar la seva feina amb
un sistema que tractés els PI com si fossin apunts de classe.

### Què es va fer

- Un vault de **62 fitxers alineats amb el core català** (el nucli LOMLOE del kit, que fixa les regles mínimes per a l'educació bàsica).
- **4 tipus de família PTE propis**, creats per a la seva feina: `PlaSuportIndividualitzat`, `AdaptacioCurricular`, `SequenciaDidactica` i `InformeAvaluacio` — els tipus de node que el kit no portava de sèrie i que ella va definir.
- **Regles de privacitat explícites**: els nodes públics declaren `dades_personals: false`; els nodes amb dades sensibles porten `anonimitzat: true`; els PI i els informes tenen visibilitat **`restringida`** (només per a la mestra i les persones autoritzades).
- **Governança formal**: un `04_Protocol_Governanca.md` que fixa qui pot veure què i com es tracten les dades — la mateixa figura que un centre tindria en un pla de protecció de dades, aplicada al nivell del vault.

### Resultat

> Un vault complet, amb governança formal, que respecta la privacitat de l'alumnat i és alineat amb el core català.

L'Anna no va haver de triar entre organitzar i protegir: les dues coses eren una de
sola.

### Què demostra

El sistema és **transversal** — FP + Primària, LOE + LOMLOE — i **ètic**: la privacitat
no és un afegit de darrera hora, és una **condició de disseny**. El kit no t'obliga a
escollir entre organitzar bé el teu coneixement i protegir els teus alumnes: fa les dues
coses alhora.

> Si vols veure el detall tècnic d'aquest vault de PT — els tipus de node, la convenció, el protocol de governança — el document de referència és el `PTE-HANDOFF-00` (handoff del projecte). Aquí només n'expliquem l'essència.

---

## Quatre lliçons dels tres casos

1. **El currículum oficial és prou bo com a font de veritat.** Els tres docents van partir del mateix punt: el document normatiu del seu mòdul o àrea. Res de materials fantasma: l'estructura la dona la norma, i el docent hi posa la vida.
2. **La privacitat es dissenya, no s'afegeix.** L'Anna no va "posar contrasenyes" al final: va construir el vault amb les regles de visibilitat des del primer dia. Resultat: cap node sensible va arribar mai a ser públic, perquè mai no hi estava previst.
3. **L'autonomia s'aprèn, no es regala.** El cas d'en César demostra que el kit es pot ensenyar: 9 mòduls, un vault propi, zero dependències al final. Un docent autònom és un docent que es queda.
4. **El coneixement és del docent, no del centre.** Els tres casos parteixen de la mateixa filosofia del kit: el coneixement estructurat és teu i viatja amb tu. Que el centre se'n beneficiï és una conseqüència, no la causa.

## Els números del kit, de cop

| Xifra | Què és |
|:---|:---|
| 1 setmana | Temps de desplegament del mòdul d'en Benet (MP1257) |
| 10 activitats | Activitats minutades del mòdul d'en Benet |
| 9 mòduls | Mòduls del curs formatiu (M0-M8) que va rebre en César |
| 59 nodes | Nodes del vault d'en César, validats amb 0 errors |
| 62 fitxers | Fitxers del vault de l'Anna, alineats amb el core català |
| 4 tipus | Tipus de node de família PTE creats per a la feina de l'Anna |
| 2 marcs legals | LOE (FP) i LOMLOE (Primària) coberts pels tres casos |
| 3 docents | Persones reals que han fet servir el kit — i la llista no es tanca aquí |

## Glossari mínim per entendre els casos

- **Node**: fitxer Markdown amb un bloc de dades (frontmatter) que el descriu. La peça bàsica del graf.
- **Vault**: el conjunt de nodes interconnectats d'un docent o d'un projecte.
- **Core**: el nucli normatiu que fixa les regles mínimes per a un àmbit (Català/LOMLOE, FP/LOE).
- **Visibilitat**: el camp que controla qui pot veure un node (`publica`, `interna`, `restringida`...).
- **Validador**: l'eina que comprova que tots els nodes compleixen les regles. "0 errors" vol dir que el graf és vàlid.

## Què tenen en comú els tres casos

| Cas | Etapa | Marc legal | Repte principal | Resultat | Què demostra |
|:---|:---|:---|:---|:---|:---|
| Benet M. (Química) | FP | LOE | Muntar un mòdul sencer des de zero en menys d'una setmana | Mòdul operatiu amb 10 activitats minutades | Transferible |
| César G. (Sanitat) | FP | LOE | Aprendre OKF i crear un vault propi autònom | 59 nodes validats amb 0 errors | Aprensible |
| Anna C. (PTE) | Primària | LOMLOE | Vault amb adaptacions i PI, amb privacitat de menors | 62 fitxers amb governança i privacitat | Transversal i ètic |

## Com es documenten aquests casos (i per què són de fiar)

Cada cas s'ha documentat amb el mateix rigor que el kit exigeix als nodes:

- **Observació directa**: els casos s'han seguit durant el procés, no reconstruït a posteriori de memòria.
- **Evidències del vault**: les xifres (10 activitats, 59 nodes, 62 fitxers) provenen dels vaults reals, validats amb 0 errors pel mateix validador del kit.
- **Anonimització escrupolosa**: inicials, sense centres, sense dades identificables — perquè la privacitat no és només un document d'aquesta carpeta, és una pràctica.
- **Honestedat**: cap d'aquests casos promet transformacions instantànies ni substitueix la feina docent. El kit no fa la feina per tu: la fa possible.

## I tu, quin cas seràs?

Els tres casos tenen una cosa en comú que no és evident en les taules: **cap dels tres
va esperar que algú els resolgués el problema**. Van agafar el currículum oficial, una
estructura i una setmana de feina — i van construir.

El kit no fa la feina per tu. Et dona la manera de fer-la **una vegada i bé**, de manera
que el resultat sigui teu, portàtil i millorable. El cas de la teva matèria, la teva
etapa i el teu alumnat no és al document: és el pròxim que s'hi pot afegir.

Tres docents, tres etapes, tres marcs legals. Tots han fet servir OKF per resoldre un
problema real. Junts demostren que el kit no és una eina per a una sola família
professional ni per a una sola etapa: és una eina per a qualsevol docent que vulgui
**recuperar la sobirania sobre el seu coneixement**.