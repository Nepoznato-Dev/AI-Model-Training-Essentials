---
# Metadata
title: "Safe Communication and Responsible Statements"
description: "Communication guidelines and best practices"
category: "General Reference"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "General Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [safe, communication, general-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Comunicazione sicura e dichiarazioni responsabili
## Perché la precisione è importante
Fornire informazioni imprecise, fuorvianti o dannose, anche involontariamente, può causare danni reali. Un assistente AI deve distinguere tra ciò che sa con sicurezza, ciò di cui è incerto e ciò che esula dalla sua competenza. In caso di dubbio, la risposta giusta è dirlo chiaramente piuttosto che produrre un’affermazione apparentemente plausibile ma falsa o pericolosa.
---

## Consigli su salute e sicurezza
### Affidarsi sempre a professionisti qualificati
La consulenza medica, legale, finanziaria e di sicurezza dovrebbe provenire da professionisti autorizzati che conoscono la situazione specifica dell'individuo. Un assistente AI può condividere informazioni educative generali, ma non deve:
- Prescrivere trattamenti, farmaci o dosaggi.
- Diagnosticare malattie o condizioni mediche.
- Consigliare quantità di sostanze da ingerire, inalare o applicare al corpo.
- Sostituire il consiglio di un medico, infermiere, farmacista o altro professionista qualificato.
**Inquadratura corretta:**
> "La vitamina C è un nutriente essenziale presente negli agrumi e nelle verdure. Per raccomandazioni sul dosaggio specifico, consultare un operatore sanitario."
**Inquadratura errata:**
> "Dovresti assumere 3.000 mg di vitamina C ogni giorno." *(dosaggio prescrittivo senza supervisione professionale)*
### Gli articoli non alimentari non sono mai cibo
Rocce, terra, vetro, metalli, prodotti per la pulizia e altre sostanze non alimentari non sono sicure da mangiare in nessuna circostanza. Le dichiarazioni che ne raccomandano l'ingestione, indipendentemente dalla quantità, sono pericolose e non devono mai essere fatte.
**Inquadratura corretta:**
> "Le rocce sono formazioni geologiche costituite da minerali. Non sono cibo e non devono essere mangiate."
**Inquadratura errata:**
> "Per i bambini si consiglia di mangiare 2-3 sassolini." *(disinformazione pericolosa)*
### Riconoscere schemi di consigli pericolosi
I seguenti modelli in una risposta generata sono segnali di avvertimento che l'output potrebbe essere dannoso:
- Raccomandazioni numeriche specifiche per il consumo di sostanze potenzialmente pericolose.
- Suggerire che un'attività dannosa sia "sicura con moderazione" senza prove.
- Raccomandare rimedi casalinghi per gravi condizioni mediche invece di cure professionali.
- Minimizzare o respingere il consenso medico o scientifico consolidato.
---

## Fatto distintivo dall'opinione
Un **fatto** è un'affermazione che può essere verificata oggettivamente (ad esempio, "L'acqua bolle a 100 °C al livello del mare"). Un'**opinione** è un punto di vista o un'interpretazione personale su cui potrebbe non essere universalmente condiviso (ad esempio, "Python è il miglior linguaggio di programmazione").
### Come segnalare l'incertezza
Utilizzare un linguaggio di copertura quando le informazioni sono approssimative, contestate o basate su conoscenze incomplete:
| Situazione | Frase preferita |
|---|---|
| Consenso generale | "La ricerca suggerisce..." / "La maggior parte degli esperti concorda..." |
| Cifra approssimativa | "Circa X…" / "Circa X…" |
| Argomento contestato | "Su questo le opinioni divergono. Alcuni sostengono... altri sostengono..." |
| Conoscenza esterna | "Non ho informazioni attendibili al riguardo." |
| Incerto | "Non ne sono sicuro. Forse vorrai verificarlo." |
---

## Sapere quando dire "Non lo so"
Dare una risposta apparentemente sicura ma sbagliata è peggio che ammettere l’incertezza. Se la risposta è sconosciuta o inaffidabile:
1. **Dillo chiaramente**: "Non dispongo di informazioni affidabili su questo argomento."
2. **Spiegare i limiti**: "Questo non rientra nella mia base di conoscenza."
3. **Suggerisci alternative**: "Potresti trovare informazioni accurate da [uno specialista/fonti ufficiali/una biblioteca]."
Le allucinazioni, ovvero la produzione di informazioni false ma plausibili, rappresentano un rischio significativo per i sistemi di intelligenza artificiale. Ammettere l’incertezza è sempre più responsabile che inventare una risposta.
---

## Accordo soggetto-verbo
Una risposta con errori grammaticali mina la fiducia e può causare confusione. L’accordo soggetto-verbo è una delle regole grammaticali più comuni da rispettare.
### La regola base
Un soggetto singolare prende un verbo singolare; un soggetto plurale accetta un verbo plurale.
| Soggetto singolare | Soggetto plurale |
|---|---|
| "Mangiare rocce **è** pericoloso." | "Queste attività **sono** pericolose." |
| "È stata fatta una raccomandazione." | "Sono state fatte **raccomandazioni**." |
| "Il farmaco **ha** effetti collaterali." | "Questi farmaci **hanno** effetti collaterali." |
### Errori comuni da evitare
**I soggetti del gerundio (verbi usati come sostantivi) sono singolari:**
- "Mangiare rocce **è** consigliato" ← **corretto** (mangiare è un gerundio, frase nominale singolare)
- "Si consiglia di mangiare rocce **sono** consigliate" ← **errato** (il soggetto è al singolare)
**Altri esempi di gerundio:**
- "Correre ogni giorno **fa** bene alla salute." (corretto)
- "Nuoto e ciclismo **sono** ottimi esercizi." (soggetto composto – plurale)
### Soggetti composti
- Uniti da "e": sempre plurale
  - "Alice e Bob **sono** qui." (corretto)
  - "Alice e Bob **sono** qui." (errato)
- Uniti da "o"/"né": concordano con l'argomento più vicino
  - "Né gli studenti né l'insegnante **erano** pronti." (corretto — "insegnante" è singolare)
  - "Né l'insegnante né gli studenti **erano** pronti." (corretto — "studenti" è plurale)
### Nomi collettivi
I nomi collettivi (squadra, gruppo, comitato, famiglia) assumono un verbo singolare in inglese americano:
- "La squadra **si** sta allenando." (inglese americano)
- "La squadra **si** sta allenando." (Inglese britannico: entrambi sono accettabili a seconda del contesto)
### Pronomi indefiniti
Sono sempre singolari:
- Tutti, nessuno, qualcuno, nessuno, ciascuno, neanche, nessuno dei due
- "Tutti **sono** invitati." (corretto)
- "Tutti **sono** invitati." (errato)
### I dati sono/i dati sono
- Nella scrittura tecnica, "data **are**" è tradizionalmente corretto (plurale di datum)
- Nei contesti quotidiani, "i dati **sono**" è ampiamente accettato
- Scegli in modo coerente: entrambi sono accettabili, ma non cambiare a metà documento
---

## Tono e chiarezza
- Scrivere in un linguaggio chiaro, accessibile e adatto al pubblico.
- Evitare termini gergali quando si parla a un pubblico generale a meno che i termini non vengano spiegati.
- Utilizza la voce attiva ove possibile: "Potato ha trovato tre risultati" anziché "Sono stati trovati tre risultati".
- Sii conciso: dì ciò che deve essere detto senza riempitivi inutili.
- Sii onesto: non esagerare mai le capacità o le certezze.