# Com compartir el teu vault

Compartir el teu vault és un dels gestos més valuosos que pots fer com a docent. Però
cal fer-ho amb criteri: què comparteixes, amb qui, i en quines condicions. Aquesta guia
et dona les opcions.

**DOI:** [10.5281/zenodo.23823819](https://doi.org/10.5281/zenodo.23823819) · **Repositori:** [github.com/jmonta23-okf/okf-starter-kit](https://github.com/jmonta23-okf/okf-starter-kit)

(Per a la versió més tècnica — git, remotes, passos de publicació — vegeu la
[documentació central](../00-documentacio/07-com-compartir.md). Aquesta és la versió
"comunitària": pensada per decidir amb seny, no per executar comandes.)

---

## 1 · Abans de compartir: la checklist de privacitat

Abans de tocar cap botó, respon aquestes preguntes:

- [ ] **No hi ha noms d'alumnes.** Cap nom, cap cognom, cap inicial identificable. Ni a les fitxes, ni als comentaris, ni als noms de fitxer.
- [ ] **No hi ha dades personals** ni de l'alumnat ni de companys ni de famílies.
- [ ] **No hi ha noms de centres** (llevat que sigui intencionat i autoritzat).
- [ ] Els nodes amb `dades_personals: true` **no es comparteixen mai** fora del centre.
- [ ] Els PI i informes individuals tenen visibilitat **`restringida`**.
- [ ] Els materials amb dades sensibles estan **anonimitzats** (`anonimitzat: true`).

Si tens dubtes, fes servir la **regla de les inicials**: Benet M., César G., Anna C. El
lector hi guanya en claredat i tu hi guanyes en seguretat. Un cas d'ús amb inicials és
tan convincent com un amb nom complet — i molt més prudent.

## 2 · Opcions per compartir el vault

### GitHub públic — recomanat per a projectes oberts

El vault és visible per a tothom. Ideal per a col·laboracions entre centres o per a la
comunitat: algú altre pot clonar el teu treball, aprendre'n i millorar-lo.

- **Avantatges:** màxima visibilitat, es pot clonar amb una comanda, i el teu treball pot inspirar algú altre.
- **Inconvenient:** qualsevol hi té accés. La checklist de privacitat és innegociable.
- **Quan no:** si el vault conté qualsevol dada d'alumnat, encara que sigui anonimitzada.

### GitHub privat — recomanat per a projectes interns

El vault només és visible per a qui tu convidis. Ideal per a un departament o un centre:
comparteixes la feina amb els companys sense exposar-la.

- **Avantatges:** control d'accés real, eines de col·laboració (suggeriments, comentaris) i una còpia de seguretat fora del teu ordinador.
- **Inconvenient:** cal convidar explícitament cada persona.
- **Quan:** el cas del César G. (FP, Sanitat) és una bona mostra: un vault de departament, compartit entre companys del mateix centre.

### Zip — recomanat per a intercanvis puntuals

Comprimeixes la carpeta i l'envies. Bo per a un substitut o per a un company que no fa
servir Git.

- **Avantatges:** zero configuració, funciona amb qualsevol persona.
- **Inconvenients:** no hi ha control de versions (si l'altre el modifica, no ho sabràs), i cada intercanvi és un fitxer nou.
- **Consell:** abans de comprimir, exclou `EINES/` i qualsevol artefacte del validador; el vault ha de viatjar net.

### Google Classroom / Drive — recomanat per a l'alumnat

El vault es penja com a material. **Compte:** el Classroom no és un bon lloc per a un
vault sencer (massa fitxers). Millor penjar només els nodes que l'alumnat necessita: la
unitat, la fitxa d'activitat, la rúbrica.

La metàfora que funciona: **el vault és la teva cuina; a l'alumnat li serveixes el
plat.** No els ensenyes el rebost sencer.

## 3 · Com compartir el kit (no el vault)

Si has adaptat el kit al teu centre — canviant el nom, afegint Cores propis, modificant
plantilles — pots publicar-lo com a **projecte derivat**. És un dels usos més generosos
que pot tenir el kit: un centre qualsevol pot tenir el seu propi sistema, amb la seva
marca i el seu marc legal.

- La llicència del contingut (CC BY-SA 4.0) t'ho permet, sempre que **citis l'autoria** i mantinguis la mateixa llicència.
- Enllaça al kit original al README del teu projecte derivat: "Aquest projecte deriva de l'OKF Starter Kit".
- Si has fet servir els scripts de `03-eines/`, recorda que el codi és MIT (encara més lliure: pots incorporar-lo fins i tot en projectes tancats).

## 4 · Errors comuns (i com evitar-los)

| Error | Com evitar-lo |
|:---|:---|
| **Compartir un vault amb enllaços trencats** | Abans de compartir, fes un `grep` dels enllaços interns i comprova que cada fitxer referenciat existeix. Un enllaç trencat al teu vault és com una pàgina en blanc al teu dossier |
| **Compartir un vault amb noms reals** | Regla de les inicials. Sempre. Fins i tot si el destí és "només per a companys". La privacitat no es juga amb confiances |
| **Compartir un vault amb `_refs/`** | El vault és autocontingut: `_refs/` són referències internes de treball, no cal que viatgin |
| **Compartir un vault amb `EINES/`** | `EINES/` conté informes del validador: són artefactes de cada execució, no contingut del projecte (el `.gitignore` del kit ja ho té previst) |
| **Compartir el vault sencer amb l'alumnat** | L'alumnat no necessita el vault: necessita els nodes de la seva unitat. Serveix-los el plat, no el rebost |

## 5 · Tres docents, tres decisions

Per veure com s'aplica tot plegat, pensa en els tres casos d'ús de la [carpeta de
casos](./01-casos-us.md):

- **Benet M.** (Química, mòdul sencer des de zero): el seu vault seria un excel·lent **GitHub públic** — materials generals de laboratori, sense dades identificables, útils per a qualsevol professor de la família química.
- **César G.** (Sanitat, 59 nodes): **GitHub privat** amb els companys del seu departament — el treball es comparteix dins del centre, i la col·laboració (comentaris, suggeriments) fa millor el vault.
- **Anna C.** (PTE, dades de menors): **res no surt del centre**. Ni zip, ni públic, ni privat amb persones alienes. El seu vault és restringit per disseny, i la governança del seu `04_Protocol_Governanca.md` ho garanteix.

Tres docents, tres decisions, cap d'elles errònia: la resposta correcta depèn sempre del
contingut, no de la plataforma.

## 6 · I si et demanen el vault a una entrevista?

Cada cop més, els docents porten el seu treball a les entrevistes de selecció. Un vault
OKF és una carta de presentació excel·lent... si el portes bé:

- **Ensenya un extracte, no el vault sencer.** Crea una carpeta amb 3-5 nodes que mostrin el teu millor treball (una unitat, una activitat, una rúbrica).
- **Porta'l al teu portàtil, no al núvol del centre.** El teu treball és teu; no depenguis d'una unitat compartida.
- **Explica què és.** "Aquest és el sistema amb què organitzo la meva programació: el node arrel, el catàleg, una activitat." En dos minuts l'entrevistador entén més del teu mètode que amb un CV.
- **Respecta la privacitat fins i tot aquí.** Si l'extracte conté material d'alumnat (fins i tot anonimitzat), no el portis. La feina de l'aula es queda a l'aula.

## 7 · Compartir sense Git: la via dels fitxers

Per a qui no vol tocar Git, el zip és l'opció natural. Aquests són els passos per fer-ho
bé:

1. **Selecciona què comparteixes.** Normalment no cal el vault sencer: una carpeta amb les unitats del trimestre és prou.
2. **Exclou el que no és contingut.** `EINES/` (informes del validador), `_refs/` (referències internes) i qualsevol node amb visibilitat `restringida`.
3. **Comprimeix.** En la majoria de sistemes, clic dret sobre la carpeta → "Comprimeix". Si tens Git al teu ordinador, pots excloure la carpeta oculta `.git` per estalviar pes.
4. **Posa un nom clar.** `vault-curs-2026-2027-trimestre-1.zip` val més que `carpeta-nova-final-definitiu.zip`.
5. **Acompanya'l d'un README de 5 línies.** Què és, què conté, com s'obre (qualsevol editor de text) i quin node començar a llegir primer.

## 8 · La llicència en 30 segons

- **El codi (scripts de `03-eines/`)** és **MIT**: el pots copiar, modificar i incorporar fins i tot en projectes tancats, sense demanar permís.
- **El contingut (documentació, plantilles, exemples)** és **CC BY-SA 4.0**: el pots copiar, adaptar i compartir, sempre que citis l'autoria i mantinguis la mateixa llicència.
- **En la pràctica**: si fas una plantilla nova, és teva i la pots publicar com vulguis — però si parteixes d'una del kit, cita-ho. Amb una línia al README n'hi ha prou.

## Tancament

Compartir no és una obligació. És una opció. Però si ho fas, fes-ho bé: amb privacitat,
amb coherència, i amb la llicència adequada.

EEl teu coneixement és teu; compartir-lo amb criteri és la millor manera que segueixi
sent teu i que, a més, serveixi a algú altre. Els tres docents dels casos d'ús ho van
entendre així — i els seus vaults, avui, són exemples per a altres.

---

**DOI del projecte:** [10.5281/zenodo.23823819](https://doi.org/10.5281/zenodo.23823819)