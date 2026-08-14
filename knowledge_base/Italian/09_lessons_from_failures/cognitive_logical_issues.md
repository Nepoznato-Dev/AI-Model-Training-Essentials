---
# Metadata
title: "Cognitive Biases and Logical Fallacies"
description: "Reasoning errors and cognitive biases"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cognitive, logical, issues, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "27 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Distorsioni cognitive ed errori logici
Questo documento consolida pregiudizi cognitivi, errori logici ed errori di ragionamento che influenzano sia il processo decisionale umano che i risultati del sistema di intelligenza artificiale.
---

## Distorsioni cognitive
I bias cognitivi sono modelli sistematici di deviazione dalla razionalità nel giudizio e nel processo decisionale. Nello sviluppo di software e nei sistemi di intelligenza artificiale, ciò può portare a decisioni di progettazione inadeguate, requisiti errati e comportamento distorto del modello.
### Bias di conferma
**Che cos'è:** La tendenza a cercare, interpretare e richiamare informazioni in un modo che confermi credenze preesistenti.
**Cattivo esempio in fase di sviluppo:**```python
# Developer believes their algorithm is O(n log n)
def analyze_complexity(code):
    # Only looks for evidence supporting O(n log n)
    sees_divide_and_conquer = True
    sees_recursion = True
    
    # Ignores contradictory evidence
    nested_loop_present = True  # Actually makes it O(n²)
    redundant_computation = True  # Adds extra factor
    
    return "O(n log n)"  # Wrong conclusion
```

**Nelle recensioni del codice:**```markdown
Developer A (senior): "This looks good, nice work!"
Developer B (junior): "This has several potential issues..."

Team accepts Developer A's review without scrutiny but questions Developer B's feedback excessively.
```

**Mitigazione:**
- Cercare attivamente prove smentitrici
- Utilizzare le revisioni del codice cieco
- Incoraggiare le opinioni dissenzienti
- Documentare esplicitamente le ipotesi
### Bias di ancoraggio
**Che cos'è:** Fare troppo affidamento sulla prima informazione incontrata.
**Cattivo esempio:**```markdown
Project Manager: "This feature should take about 2 days."
Developer: (Anchored to 2 days, even though realistic estimate is 5 days)
"Okay, I'll try to finish in 2 days."

Result: Rushed work, technical debt, missed deadlines anyway.
```

**Mitigazione:**
- Ottieni più stime indipendenti
- Utilizzare il poker di pianificazione per la stima
- Considerare intervalli invece di stime puntuali
- Dati storici di riferimento
### Errore sui costi irrecuperabili
**Che cos'è:** Continuare un'impresa grazie alle risorse precedentemente investite (tempo, denaro, impegno), anche quando abbandonare sarebbe meglio.
**Cattivo esempio:**```markdown
"We've already spent 6 months building this custom framework. 
We can't switch to the industry standard now, even though 
it would save us time in the long run."
```

**Mitigazione:**
- Valutare le decisioni in base al valore futuro, non agli investimenti passati
- Rivalutare regolarmente la fattibilità del progetto
- Creare sicurezza psicologica per il pivoting
- Utilizzare criteri oggettivi per continuare/interrompere le decisioni
### Euristica della disponibilità
**Che cos'è:** Sopravvalutare l'importanza delle informazioni facilmente disponibili o recenti.
**Cattivo esempio:**```markdown
"I just read about a SQL injection attack, so we should 
prioritize SQL injection prevention over XSS, even though 
our security audit shows XSS is our bigger risk."
```

**Mitigazione:**
- Utilizzare il processo decisionale basato sui dati
- Consultare modelli completi di minacce
- Guarda le tariffe base e le statistiche
- Evitare pregiudizi legati al passato nella definizione delle priorità
### Effetto Dunning-Kruger
**Che cos'è:** Le persone con scarse capacità in un compito sopravvalutano le proprie capacità; gli esperti potrebbero sottovalutarli.
**Cattivo esempio:**```markdown
Junior Developer: "I've completed a Python tutorial. 
I'm ready to architect our entire microservices platform."

Senior Developer: "I've been building distributed systems for 10 years. 
I'm probably missing something important in this design."
```

**Mitigazione:**
- Incoraggiare l'apprendimento continuo
- Implementare processi di peer review
- Creare programmi di tutoraggio
- Promuovere l'umiltà e la curiosità
---

## Errori logici
Gli errori logici sono errori di ragionamento che minano la validità dell’argomentazione. I modelli di intelligenza artificiale possono produrre risultati contenenti questi errori.
### Ad Hominem (Attacco alla persona)
**Che cos'è:** Attaccare la persona che sostiene una discussione piuttosto che la discussione stessa.
**Cattivo esempio:**```markdown
"This code review is wrong because the reviewer is a junior developer."
```

**Perché non è valido:** La validità del feedback dipende dal suo contenuto, non dall'anzianità del revisore.
### Ricorso all'autorità
**Che cos'è:** Affermare che qualcosa è vero perché lo dice una figura autoritaria, senza prove.
**Cattivo esempio:**```markdown
"This architecture must be correct because Google uses it."
```

**Perché non va bene:** ciò che funziona per Google su larga scala potrebbe non funzionare per il tuo caso d'uso.
### Falsa dicotomia (pensiero in bianco e nero)
**Che cos'è:** Presenta solo due opzioni quando ne esistono di più.
**Cattivo esempio:**```markdown
"We either rewrite everything in Rust or accept that our 
codebase will always be slow and buggy."
```

**Realtà:** esistono molte opzioni tra questi estremi (ottimizzare i percorsi più attivi, utilizzare Rust per componenti specifici, migliorare il codice Python, ecc.)
### Pendio scivoloso
**Che cos'è:** Sostenere che un evento porterà inevitabilmente a una catena di conseguenze negative.
**Cattivo esempio:**```markdown
"If we allow this small technical debt, soon our entire 
codebase will be unmaintainable and the company will fail."
```

**Perché non va bene:** presuppone una progressione inevitabile senza prove; ignora i fattori attenuanti.
### Ragionamento circolare
**Che cos'è:** Usare la conclusione come premessa.
**Cattivo esempio:**```markdown
"Our code is high quality because we write good code."
```

### Post Hoc Ergo Propter Hoc (Falsa Causa)
**Che cos'è:** Supponendo che, poiché B ha seguito A, A ha causato B.
**Cattivo esempio:**```markdown
"We deployed the new feature and then saw increased latency. 
The new feature must be causing the latency."
```

**Realtà:** La correlazione non implica causalità. Altri fattori potrebbero essere responsabili.
### L'uomo di paglia
**Che cos'è:** Rappresentare in modo errato l'argomento di qualcuno per renderlo più facile da attaccare.
**Cattivo esempio:**```markdown
Developer A: "We should add more tests for edge cases."
Developer B: "So you want us to spend all our time writing tests 
and never ship features?"
```

### Errore del carrozzone
**Che cos'è:** Discutere su qualcosa è corretto perché molte persone ci credono.
**Cattivo esempio:**```markdown
"Everyone is using Kubernetes, so we should too."
```

**Perché non è valido:** La popolarità non garantisce l'idoneità alle tue esigenze specifiche.
---

## Fallimenti nel ragionamento nell'intelligenza artificiale
### Errori logici in più fasi
**Cattivo esempio:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Yes, Alice must be a programmer.
```

**Perché non va bene:**
- Commette l'errore di affermare il conseguente
- Alice potrebbe scrivere codice senza essere una programmatrice
- Struttura logica: (P→Q, Q) ⊬ P
**Ragionamento corretto:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Not necessarily. While all programmers write code, not everyone
who writes code is a programmer. Alice could be a student, hobbyist, or
work in another field that involves coding.
```

### Fallimenti nel ragionamento matematico
**Cattivo esempio:**```
User: A bat and ball cost $1.10 together. The bat costs $1 more than the ball.
How much does the ball cost?
Assistant: The ball costs $0.10.
```

**Realtà:** se la palla costa $ 0,10 e la mazza costa $ 1 in più ($ 1,10), il totale sarebbe $ 1,20. La risposta corretta è $ 0,05 per la palla e $ 1,05 per la mazza.
### Errori di ragionamento causale
**Cattivo esempio:**```
User: Ice cream sales and drowning rates both increase in summer. Does ice cream cause drowning?
Assistant: Yes, there appears to be a causal relationship.
```

**Realtà:** Entrambi sono causati da un terzo fattore (clima caldo), non l'uno dall'altro.
---

## Strategie di miglioramento
### Per il processo decisionale umano
1. **Formazione di sensibilizzazione**: impara a riconoscere i pregiudizi comuni
2. **Utilizzo delle liste di controllo**: utilizzare liste di controllo decisionali per contrastare i pregiudizi
3. **Team diversi**: includi persone con prospettive diverse
4. **Pre-mortem**: immagina il fallimento e lavora a ritroso per identificare le cause
5. **Documentazione**: registrare la motivazione per una revisione successiva
### Per sistemi di intelligenza artificiale
1. **Suggerimento della catena di pensieri**: chiedere al modello di mostrare i passaggi di ragionamento
2. **Autocorrezione**: chiedi al modello di rivedere e criticare le sue risposte
3. **Verifica formale**: utilizzare strumenti di ragionamento simbolico per la logica critica
4. **Scomposizione**: suddividi i problemi complessi in passaggi più piccoli
5. **Strumenti esterni**: utilizza calcolatrici e risolutori per compiti matematici
6. **Campioni multipli**: genera risposte multiple e confronta
---

## Argomenti correlati
- **Errori AI/LLM**: consulta`ai_llm_failures.md`per allucinazioni e problemi di ragionamento
- **Fonti contraddittorie**: consultare la documentazione sulla valutazione delle informazioni contrastanti
- **Pensiero critico**: applica questi concetti per valutare argomentazioni e prove
- **Prompt Engineering**: consulta`../02_artificial_intelligence/prompt_engineering.md`per le tecniche volte a ridurre gli errori di ragionamento
---

## Ulteriori pregiudizi cognitivi nello sviluppo del software
### Pregiudizi sullo status quo
**Che cos'è:** Preferenza per il mantenimento dello stato attuale; ogni cambiamento è percepito come una perdita.
**Cattivo esempio:**```markdown
Team Lead: "Should we upgrade to Python 3.12? It has performance improvements 
and security fixes."

Developer: "Python 3.8 works fine. Why risk breaking things?"

Reality: Staying on an older version increases technical debt, security risks,
and makes future upgrades harder.
```

**Mitigazione:**
- Quantificare i costi di non cambiamento
- Imposta programmi di aggiornamento regolari
- Creare ambienti di sperimentazione sicuri
- Inquadrare i cambiamenti come opportunità, non come minacce
### Pregiudizio sull'ottimismo
**Che cos'è:** Sottovalutare tempi, costi e rischi sovrastimando i benefici.
**Cattivo esempio:**```markdown
Project Plan:
- Development: 2 weeks (realistic: 4 weeks)
- Testing: 3 days (realistic: 1 week)
- Bug fixes: 2 days (realistic: 1-2 weeks)
- Contingency: None

Result: Project takes 3x longer than planned.
```

**Mitigazione:**
- Utilizzare le previsioni delle classi di riferimento (confrontare con progetti passati simili)
- Aggiungere buffer di contingenza (20-50%)
- Condurre la pre-mortem
- Tieni traccia dell'accuratezza della stima nel tempo
### Bias di sopravvivenza
**Che cos'è:** Concentrarsi sugli esempi di successo ignorando i fallimenti.
**Cattivo esempio:**```markdown
"Look at all these successful startups that didn't do market research!
We don't need market research either."

Reality: Many more startups failed without market research, but they're 
not visible because they didn't survive.
```

**Mitigazione:**
- Studia sia i successi che i fallimenti
- Cerca tariffe base e statistiche
- Considera i dati invisibili
- Evitare esempi di selezione selettiva
### Errore fondamentale di attribuzione
**Che cos'è:** Attribuire il comportamento degli altri al carattere piuttosto che alle circostanze.
**Cattivo esempio:**```markdown
"That developer made a bug because they're careless."

Reality: The bug might be due to unclear requirements, time pressure,
lack of testing infrastructure, or fatigue.
```

**Mitigazione:**
- Considerare i fattori situazionali
- Praticare l'empatia
- Concentrarsi sui sistemi, non sugli individui
- Utilizzare autopsie irreprensibili
### Pregiudizio del senno di poi
**Che cos'è:** Dopo che si è verificato un evento, credere che fosse prevedibile da sempre.
**Cattivo esempio:**```markdown
After production outage:
"I knew that deployment was risky. This was totally predictable."

Reality: The outcome wasn't obvious beforehand; hindsight makes it seem clear.
```

**Mitigazione:**
- Documentare le previsioni prima dei risultati
- Esaminare il contesto decisionale, non solo i risultati
- Evita la cultura del "te l'avevo detto".
- Concentrarsi sul miglioramento dei processi, non sull'attribuzione di colpe
---

## Altri errori logici
### Appello alla novità
**Che cos'è:** Supporre che qualcosa sia migliore perché è più recente.
**Cattivo esempio:**```markdown
"We should rewrite our entire backend in the latest framework. 
It's the newest, so it must be better."

Reality: Newer doesn't mean better for your specific use case.
Mature technologies often have better support and stability.
```

### Ricorso alla tradizione
**Che cos'è:** Discutere su qualcosa è corretto perché è sempre stato fatto in questo modo.
**Cattivo esempio:**```markdown
"We've always deployed on Fridays at 5 PM. We shouldn't change that."

Reality: Just because something is traditional doesn't make it optimal.
(Actually, deploying on Friday at 5 PM is generally considered bad practice!)
```

### Tu Quoque (Appello all'ipocrisia)
**Che cos'è:** Respingere le critiche sottolineandone l'incoerenza.
**Cattivo esempio:**```markdown
Senior Dev: "You should write tests for this code."
Junior Dev: "But you don't write tests for your code either!"

Reality: The validity of the advice is independent of who gives it.
```

### Domanda caricata
**Che cos'è:** Porre una domanda che contiene un presupposto.
**Cattivo esempio:**```markdown
"Why did you write such terrible code for this module?"

Reality: The question assumes the code is terrible, putting the respondent
on the defensive regardless of actual code quality.
```

### Nessun vero scozzese
**Che cos'è:** Fare un'eccezione a un'affermazione universale quando contestata.
**Cattivo esempio:**```markdown
Person A: "No professional developer writes code without tests."
Person B: "But John is a professional developer and doesn't write tests."
Person A: "Well, no TRUE professional developer writes code without tests."

Reality: This redefines the category to exclude counterexamples rather 
than revising the claim.
```

### Errore genetico
**Cos'è:** Giudicare qualcosa in base alla sua origine piuttosto che al merito attuale.
**Cattivo esempio:**```markdown
"That library came from a small startup, so it can't be enterprise-grade."

Reality: The origin doesn't determine current quality. Evaluate based on
actual characteristics, not source.
```

### Errore della via di mezzo
**Che cos'è:** Presupporre che la verità sia sempre nel mezzo tra due estremi.
**Cattivo esempio:**```markdown
Developer A: "We should add comprehensive error handling."
Developer B: "Error handling isn't important, skip it."
Compromise: "Let's add some error handling, but not too much."

Reality: One position might be clearly correct. Compromise isn't always wise.
```

---

## Distorsioni cognitive nei sistemi di intelligenza artificiale
### Distorsioni dei dati di addestramento
I modelli di intelligenza artificiale ereditano i pregiudizi presenti nei dati di addestramento.
**Esempio:**```markdown
Training data contains: "The doctor said..." (mostly male pronouns)
                       "The nurse said..." (mostly female pronouns)

Model learns: Doctors are typically male, nurses are typically female.

Result: Model exhibits gender bias in profession associations.
```

**Mitigazione:**
- Controllare i dati di formazione per individuare eventuali pregiudizi
- Utilizzare tecniche di debiasing
- Test per uscite distorte
- Raccolta dati diversificata
### Pregiudizio dell'automazione
**Che cos'è:** Affidarsi eccessivamente a sistemi automatizzati, anche quando sono sbagliati.
**Esempio:**```markdown
AI suggests code with a subtle bug.
Developer accepts it without review because "the AI is usually right."

Result: Bug makes it to production.
```

**Mitigazione:**
- Mantenere la supervisione umana
- Incoraggiare la valutazione critica dei risultati dell'IA
- Non considerare l'IA come infallibile
- Implementare processi di revisione
### Illusione di comprensione
**Cos'è:** Credere di capire come funziona un'intelligenza artificiale quando non è così.
**Esempio:**```markdown
User: "The AI understands what I mean, it's like talking to a person."

Reality: LLMs predict tokens based on patterns, they don't truly 
"understand" in the human sense. This illusion leads to over-trust.
```

**Mitigazione:**
- Istruire gli utenti sui limiti dell'intelligenza artificiale
- Sii trasparente su come funzionano i sistemi
- Evitare di antropomorfizzare l'IA
- Stabilire aspettative adeguate
---

## Casi di studio
### Caso di studio 1: bias di conferma nella scelta dell'architettura
**Incidente:** un team ha scelto un'architettura di microservizi per una piccola applicazione.
**Causa principale:** Il responsabile del team aveva letto diversi articoli che elogiavano i microservizi e 
hanno cercato solo informazioni che confermassero questa scelta, ignorando gli avvertimenti sulla complessità.
**Impatto:**
- Enormi spese generali per un team di 3 sviluppatori
- La complessità della distribuzione è aumentata di 10 volte
- Prestazioni ridotte a causa delle chiamate di rete
- Progetto ritardato di 6 mesi
**Lezione:** Valuta le architetture in base al tuo contesto specifico, non solo 
testimonianze positive. Considerare esplicitamente i compromessi.
### Caso di studio 2: costi irrecuperabili nel sistema legacy
**Incidente:** l'azienda ha continuato a mantenere un CRM personalizzato per 5 anni 
nonostante alternative migliori.
**Causa principale:** "Abbiamo già investito 2 milioni di dollari, non possiamo abbandonarlo adesso."
**Impatto:**
- Costo di manutenzione annuale: $ 500.000
- Costo opportunità: impossibile utilizzare funzionalità moderne
- Problemi di fidelizzazione dei talenti (gli sviluppatori volevano lavorare con la tecnologia moderna)
- Costo totale in 5 anni: 4,5 milioni di dollari contro 1,5 milioni di dollari per l'alternativa SaaS
**Lezione:** Gli investimenti passati sono affondati. Prendi decisioni basate sul valore futuro.
### Caso di studio 3: Euristica della disponibilità nella sicurezza
**Incidente:** il team ha dato priorità alla difesa da un attacco recentemente pubblicizzato 
vettore ignorando le minacce più probabili.
**Causa principale:** la recente copertura giornalistica ha reso altamente disponibile un tipo di minaccia 
nella memoria, distorcendo la valutazione del rischio.
**Impatto:**
- Spesi $ 100.000 per mitigare le minacce a bassa probabilità
- La violazione effettiva si è verificata tramite il vettore trascurato
- Costo di ripristino: $ 500.000+
**Lezione:** Utilizza la modellazione delle minacce basata sui dati e non la definizione delle priorità basata sull'attualità.
---

## Esercizi pratici
### Esercizio sul rilevamento dei bias
Rivedi le decisioni recenti e chiedi:
1. Quali ipotesi abbiamo fatto?
2. Quali prove contraddicono la nostra conclusione?
3. Abbiamo considerato più opzioni o ci siamo ancorati alla prima idea?
4. Stiamo continuando a causa del valore futuro o degli investimenti passati?
5. Cosa consiglieremmo se qualcun altro ce lo chiedesse?
### Individuazione degli errori logici
Esercitati a identificare gli errori nelle discussioni quotidiane:
```markdown
Statement: "If we don't adopt AI now, we'll be left behind forever."

Analysis: This is a slippery slope fallacy. It assumes inevitable 
progression to being "left behind" without evidence. Also presents 
a false dichotomy (adopt AI or be left behind).
```

### Tecnica pre-mortem
Prima di iniziare un progetto:
1. Immagina che siano 6 mesi nel futuro
2. Il progetto è fallito clamorosamente
3. Scrivi la storia del motivo per cui ha fallito
4. Lavorare all'indietro per prevenire queste modalità di fallimento
Ciò contrasta il pregiudizio dell’ottimismo e l’euristica della disponibilità.
---

## Strumenti e framework
### Modello di diario delle decisioni
```markdown
Date: [When]
Decision: [What we decided]
Context: [Situation and constraints]
Options Considered: [Alternatives evaluated]
Expected Outcome: [What we think will happen]
Confidence Level: [How sure we are]
Review Date: [When to revisit]

[Later] Actual Outcome: [What actually happened]
Lessons Learned: [What we'd do differently]
```

### Lista di controllo dei pregiudizi
Prima di prendere decisioni importanti:
- [ ] Abbiamo cercato prove smentitrici?
- [ ] Siamo ancorati alle informazioni iniziali?
- [ ] I costi irrecuperabili ci influenzano?
- [ ] Siamo troppo sicuri delle nostre stime?
- [ ] Abbiamo considerato i tassi base?
- [ ] Stiamo cadendo nel bias di disponibilità/recency?
- [ ] Faremmo la stessa scelta se iniziassimo da capo?
### Esercizio della squadra rossa
Incaricare qualcuno di discutere contro la decisione proposta:
- Il loro ruolo è trovare i difetti
- Devono presentare punti di vista alternativi
- Esercitazioni di gruppo rispondendo alle critiche in modo costruttivo
- Documenti sollevati e affrontati
Ciò contrasta il pregiudizio di conferma e il pensiero di gruppo.