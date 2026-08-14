<!--
---
# Metadata
title: "Game Theory"
description: "Strategic-form games, Nash equilibrium, dominant strategies, minimax theorem, cooperative games, Shapley value, mechanism design, auction theory, and connections to multi-agent reinforcement learning"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into game theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [game-theory, nash-equilibrium, minimax, cooperative-games, shapley-value, mechanism-design, auction-theory, multi-agent-rl]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Teoria dei giochi
La teoria dei giochi è la matematica dell’interazione strategica: situazioni in cui il tuo risultato dipende non solo dalle tue scelte, ma da quelle degli altri. Dalle guerre sui prezzi tra aziende alle corse agli armamenti nucleari, dalle aste online alla biologia evolutiva, la teoria dei giochi fornisce gli strumenti per analizzare il conflitto e la cooperazione. È diventato sempre più rilevante per l’apprendimento automatico attraverso l’apprendimento di rinforzo multi-agente, le reti generative avversarie (GAN) e la progettazione di meccanismi per piattaforme online.
---

## Giochi in forma strategica
### Definizione
Un **gioco in forma strategica (forma normale)** è composto da:
- Un insieme di giocatori N = {1, 2, ..., n}
- La strategia imposta S₁, S₂, ..., Sₙ per ogni giocatore
- Funzioni di payoff u₁, u₂, ..., uₙ che mappano i profili strategici su numeri reali
### Esempio: Il dilemma del prigioniero
| | Cooperare (C) | Difetto (D) |
|---|---------------|----|
| **Coopera (C)** | (−1, −1) | (−3, 0) |
| **Difetto (D)** | (0, −3) | (−2, −2) |
| Analisi | Risultato |
|----------|--------|
| Strategia dominante | Difetto (D domina C per entrambi i giocatori) |
| Equilibrio di Nash | (D, D) con profitto (−2, −2) |
| Ottimo sociale | (C, C) con profitto (−1, −1) |
| Dilemma | La razionalità individuale porta all'irrazionalità collettiva |
### Altri giochi classici
**Battaglia dei sessi:**
| | Opera | Calcio |
|---|-------|----------|
| Opera | (2, 1) | (0, 0) |
| Calcio | (0, 0) | (1, 2) |
Due equilibri di Nash: (Opera, Opera) e (Calcio, Football).
**Pollo (Falco-Colomba):**
| | Falco | Colomba |
|---|------|------|
| Falco | (−10, −10) | (5, 0) |
| Colomba | (0, 5) | (1, 1) |
Due equilibri di Nash: (Falco, Colomba) e (Colomba, Falco).
---

## Strategie dominanti
| Concetto | Definizione |
|---------|------------|
| **Strettamente dominante** | La strategia sᵢ offre un profitto maggiore rispetto a qualsiasi altra strategia, indipendentemente dalle scelte degli avversari |
| **Debolmente dominante** | La strategia sᵢ offre un profitto almeno altrettanto alto di qualsiasi altro, e decisamente più alto per alcuni profili di avversari |
| **Strategia dominata** | Una strategia che non è mai la risposta migliore |
**Eliminazione ripetuta delle strategie dominate:**
1. Rimuovere qualsiasi strategia strettamente dominata
2. Ripetere finché non sarà più possibile rimuoverne altri
3. Se rimane un profilo strategico, è l'unico equilibrio di Nash
---

## Equilibrio di Nash
Un **equilibrio di Nash** è un profilo strategico in cui nessun giocatore può migliorare il proprio profitto modificando unilateralmente la propria strategia.
### Definizione
(s₁*, s₂*, ..., sₙ*) è un equilibrio di Nash se per ogni giocatore i:
uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ, s₋ᵢ*) per tutti sᵢ ∈ Sᵢ
### Alla ricerca degli equilibri di Nash (Giochi 2×2)
**Miglior metodo di risposta:**
1. Per ogni colonna, sottolinea la migliore risposta del giocatore 1
2. Per ogni riga, sottolinea la migliore risposta del giocatore 2
3. Le celle in cui entrambi sono sottolineati sono equilibri di Nash
### Esistenza (Teorema di Nash)
Ogni gioco finito ha almeno un equilibrio di Nash (possibilmente in strategie miste).
### Strategie miste
Una **strategia mista** è una distribuzione di probabilità su strategie pure.
| Concetto | Definizione |
|---------|------------|
| Strategia mista σᵢ | Distribuzione di probabilità su Sᵢ |
| Strategia mista NE | Nessun giocatore può migliorare il profitto atteso modificando la propria miscela |
| Supporto | Insieme di strategie pure giocate con probabilità positiva |
**Esempio funzionale: corrispondenza dei penny**
| | Teste | Code |
|---|-------|-------|
| Teste | (1, −1) | (−1, 1) |
| Code | (−1, 1) | (1, −1) |
Nessuna strategia pura NE. NE misto: entrambi giocano H e T con probabilità ½ ciascuno.
---

## Teorema del Minimax
### Giochi a somma zero
In un **gioco a somma zero**, il guadagno di un giocatore è esattamente la perdita dell'altro: u₁ + u₂ = 0.
### Teorema del Minimax di Von Neumann
Per ogni gioco finito a somma zero a due giocatori:
max_{σ₁} min_{σ₂} u₁(σ₁, σ₂) = min_{σ₂} max_{σ₁} u₁(σ₁, σ₂)
Il **maximin** (miglior caso peggiore per il giocatore 1) è uguale al **minimax** (miglior caso peggiore per il giocatore 2). Questo valore comune è il **valore del gioco**.
### Risolvere giochi a somma zero
Per un gioco 2×2 a somma zero con matrice:
| | L | R |
|---|---|---|
| T | un | b |
| B | c | d |
Strategia mista ottimale del giocatore 1: gioca T con probabilità p = (d−c)/((a−b)+(d−c))
Valore del gioco: v = (ad−bc)/((a−b)+(d−c))
---

## Giochi in forma estesa
I giochi con mosse sequenziali sono rappresentati come **alberi di gioco**.
### Concetti chiave
| Concetto | Definizione |
|---------|------------|
| **Albero del gioco** | Albero che mostra tutte le possibili sequenze di mosse |
| **Set di informazioni** | Insieme di nodi che un giocatore non può distinguere |
| **Informazioni perfette** | Ogni insieme di informazioni è un singleton (tutte le mosse osservabili) |
| **Sottogioco perfetto NE** | Equilibrio di Nash in ogni sottogioco |
| **Induzione all'indietro** | Risolvi dalla fine dell'albero all'indietro |
### Teorema di Zermelo
Nei giochi finiti, con informazione perfetta, a due giocatori senza possibilità: o un giocatore ha una strategia vincente, oppure entrambi possono forzare un pareggio (ad esempio, negli scacchi).
---

## Giochi cooperativi
Nei **giochi cooperativi**, i giocatori possono formare accordi e coalizioni vincolanti.
### Funzione caratteristica
Un gioco cooperativo è definito da una **funzione caratteristica** v: 2^N → ℝ, dove v(S) è il valore che la coalizione S può ottenere.
| Immobile | Definizione |
|----------|------------|
| **Superadditivo** | v(S ∪ T) ≥ v(S) + v(T) per S, T |
| **Convesso** | v(S ∪ {i}) − v(S) ≤ v(T ∪ {i}) − v(T) per S ⊂ T |
### Il Nucleo
Il **core** è l’insieme delle allocazioni in cui nessuna coalizione può migliorare separandosi:
Nucleo = {x ∈ ℝⁿ : Σᵢ∈N xᵢ = v(N), Σᵢ∈S xᵢ ≥ v(S) per ogni S ⊂ N}
Il nucleo potrebbe essere vuoto, nel qual caso non esiste alcuna allocazione stabile.
### Valore di Shapley
Il **valore Shapley** fornisce un'allocazione equa unica basata su contributi marginali:
φᵢ = Σ_{S ⊂ N\{i}} (|S|!(n−|S|−1)!/n!) · [v(S ∪ {i}) − v(S)]
| Immobile | Dichiarazione |
|----------|-----------|
| Efficienza | Σ φᵢ = v(N) (tutti i valori sono distribuiti) |
| Simmetria | Contribuenti uguali ottengono guadagni uguali |
| Giocatore fittizio | I non contributori ottengono zero |
| Additività | φ(v + w) = φ(v) + φ(w) |
**Interpretazione:** il valore Shapley di ciascun giocatore è il suo contributo marginale medio in tutti i possibili ordinamenti di formazione della coalizione.
### Esempio realizzato
Tre giocatori: v(∅) = 0, v({1}) = 0, v({2}) = 0, v({3}) = 0, v({1,2}) = 50, v({1,3}) = 70, v({2,3}) = 60, v({1,2,3}) = 100.
| Giocatore | Contributi marginali (media sugli ordinativi) | Valore Shaley |
|--------|-------------------------------------------|-------|
| 1| (100+50+70+70+50+0)/6 = 56,7 | 37,5 |
| 2| (100+50+60+60+50+0)/6 | 27,5 |
| 3| (100+70+60+70+60+0)/6 | 35,0 |
(Calcolato con precisione utilizzando la formula di Shapley per ciascuna permutazione.)
---

## Progettazione del meccanismo
La **progettazione del meccanismo** è la "teoria dei giochi inversa": invece di analizzare determinati giochi, progetta giochi che producono i risultati desiderati.
### Il Principio della Rivelazione
Qualsiasi meccanismo che raggiunga il risultato desiderato può essere sostituito da un **meccanismo di rivelazione diretta** in cui dire la verità è un equilibrio di Nash.
### Teoria delle aste
| Tipo di asta | Regole | Equivalenza dei ricavi |
|-------------|-------|----------------------|
| **Primo prezzo in busta chiusa** | Il miglior offerente vince e paga la sua offerta | Tutte le aste standard producono le stesse entrate previste |
| **Seconda offerta sigillata (Vickrey)** | Vince il miglior offerente e paga la seconda offerta più alta | (sotto valori privati ​​indipendenti) |
| **Inglese (ascendente)** | Il prezzo aumenta; primo ad accettare vince | — |
| **Olandese (discendente)** | Il prezzo scende; primo ad accettare vince | — |
### Asta Vickrey (secondo prezzo)
**Strategia dominante:** Fai un'offerta al tuo vero valore.
| Immobile | Dichiarazione |
|----------|-----------|
| Offerte veritiere | Strategia debolmente dominante |
| Efficienza | L'oggetto va al miglior offerente |
| Entrate | Stessi ricavi attesi del primo prezzo (Teorema dell'equivalenza dei ricavi) |
### Progettazione ottimale dell'asta (Myerson)
L'asta che massimizza le entrate:
- Assegna all'offerente con la **valutazione virtuale** più alta
- Imposta un prezzo di riserva
- Valutazione virtuale: ψ(v) = v − (1−F(v))/f(v)
---

## Connessioni al machine learning
### Reti avversarie generative (GAN)
I GAN sono un gioco a due giocatori tra un generatore G e un discriminatore D:
min_G max_D V(D, G) = E[log D(x)] + E[log(1 − D(G(z)))]
| Concetto di teoria dei giochi | Equivalente GAN |
|---------------------|-----------|
| Gioco a somma zero per due giocatori | Generatore vs discriminatore |
| Equilibrio di Nash | G genera dati reali, D emette ½ ovunque |
| Minimax | La funzione obiettivo GAN |
| Collasso della modalità | Mancato raggiungimento dell'equilibrio |
### Apprendimento per rinforzo multi-agente (MARL)
| Concetto | Applicazione MARL |
|---------|-----------------|
| Equilibrio di Nash | Politiche stabili in ambienti multi-agente |
| Minimax | Politiche robuste contro gli avversari avversari |
| Giochi cooperativi | Formazione della coalizione, ripartizione dei compiti |
| Valore Shaley | Cessione del credito (quale agente ha contribuito cosa?) |
| Progettazione del meccanismo | Progettare incentivi in ​​sistemi multi-agente |
| Gioco fittizio | Algoritmo di apprendimento convergente all'equilibrio di Nash |
### Altre connessioni ML
| Applicazione | Strumento di teoria dei giochi |
|-------------|-----------|
| Progettazione di aste pubblicitarie (Google, Facebook) | Progettazione dei meccanismi, teoria delle aste |
| Progettazione del mercato (Uber, Airbnb) | Teoria dell'abbinamento, progettazione del meccanismo |
| Robustezza contraddittoria | Giochi a somma zero tra attaccante e difensore |
| Divisione equa | Valore Shapley, allocazione senza invidia |
| Apprendimento federato | Teoria dei giochi cooperativi per la misurazione del contributo |
| Sistemi di raccomandazione | Progettazione di meccanismi per l'elicitazione di preferenze veritiere |
---

## Riepilogo
| Concetto | Idea fondamentale | Risultato chiave |
|---------|-----------|------------|
| Giochi in forma strategica | Giocatori, strategie, payoff | Rappresentazione della matrice del gioco |
| Strategie dominanti | Meglio indipendentemente dagli altri | Eliminazione iterata |
| Equilibrio di Nash | Nessuna deviazione unilaterale redditizia | Esiste in ogni gioco finito |
| Strategie miste | Randomizza sulle azioni | Teorema di esistenza di Nash |
| Minimax | Miglior caso peggiore (somma zero) | Teorema del minimax di Von Neumann |
| Forma estesa | Mosse sequenziali | Induzione all'indietro, perfezione del sottogioco |
| Giochi cooperativi | Coalizioni vincolanti | Nucleo, valore Shapley |
| Progettazione del meccanismo | Progettare giochi per ottenere risultati | Principio di rivelazione, aste ottimali |
| Teoria dell'asta | Vendere tramite concorso | Equivalenza dei ricavi, asta Vickrey |
La teoria dei giochi è la matematica del pensiero strategico. In un mondo sempre più popolato da agenti IA interagenti, mercati automatizzati e sistemi avversari, la teoria dei giochi fornisce gli strumenti essenziali per prevedere il comportamento, progettare meccanismi e costruire robusti sistemi multi-agente. Per i data scientist, spiega come funzionano i GAN, come le aste online generano miliardi di entrate e come costruire sistemi di intelligenza artificiale che funzionino bene in ambienti competitivi.