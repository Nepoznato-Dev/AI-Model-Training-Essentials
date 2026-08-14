---
# Metadata
title: "Stochastic Processes"
description: "Random variables review, Markov chains, random walks, Brownian motion, Poisson processes, martingales, Monte Carlo methods, and MCMC"
category: "Data Science and Analytics"
subcategory: "Mathematics"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial deep-dive into stochastic processes"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [stochastic-processes, markov-chains, random-walks, brownian-motion, poisson-processes, martingales, monte-carlo, mcmc]
difficulty_level: "advanced"
prerequisites:
  - "statistics_and_probability.md"
  - "real_analysis.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Processi stocastici
Un **processo stocastico** è una raccolta di variabili casuali indicizzate dal tempo (o dallo spazio). Mentre la teoria della probabilità studia i singoli eventi casuali, i processi stocastici studiano come la casualità si evolve nel tempo. Modellano i prezzi delle azioni, la lunghezza delle code, la diffusione delle malattie, la generazione del linguaggio e le dinamiche di formazione dei modelli di apprendimento automatico.
---

## Fondazioni
### Definizione
Un processo stocastico {X_t : t ∈ T} è una famiglia di variabili casuali definite su uno spazio di probabilità comune. T è il **insieme di indici** (tempo):
- **Tempo discreto:** T = {0, 1, 2, ...}
- **Tempo continuo:** T = [0, ∞)
Lo **spazio degli stati** S è l'insieme dei possibili valori che X_t può assumere.
### Proprietà chiave
| Immobile | Definizione |
|----------|------------|
| **Stazionarietà** | Distribuzione congiunta di (X_{t₁}, ..., X_{tₖ}) uguale a (X_{t₁+τ}, ..., X_{tₖ+τ}) |
| **Indipendenza** | X_t indipendente da X_s per t ≠ s |
| **Ergodicità** | Le medie temporali convergono alle medie d'insieme |
| **Proprietà Markov** | Il futuro dipende solo dal presente, non dal passato |
| **Martingala** | Il valore futuro atteso è uguale al valore corrente |
---

## Catene di Markov
Una **catena di Markov** è un processo stocastico in cui lo stato futuro dipende solo dallo stato attuale (proprietà senza memoria).
### Catene di Markov a tempo discreto (DTMC)
P(X_{n+1} = j | X_n = i, X_{n-1} = i_{n-1}, ...) = P(X_{n+1} = j | X_n = i) = p_{ij}
La **matrice di transizione** P ha elementi p_{ij} = P(vai a j | attualmente in i).
| Immobile | Dichiarazione |
|----------|-----------|
| Somme di riga | Ogni riga ha come somma 1: Σⱼ p_{ij} = 1 |
| Transizione in n passaggi | P(X_{n+m} = j | X_m = i) = (Pⁿ)_{ij} |
| Distribuzione stazionaria | πP = π (autovettore sinistro con autovalore 1) |
### Classificazione degli Stati
| Termine | Definizione |
|------|-----------|
| **Ricorrente** | La catena ritorna allo stato i con probabilità 1 |
| **Transitorio** | Probabilità diversa da zero di non tornare mai più |
| **Assorbente** | p_{ii} = 1 (una volta entrato, non esce mai) |
| **Periodo** | GCD dei tempi di restituzione; periodo 1 = aperiodico |
| **Comunicare** | Gli stati i e j possono raggiungersi |
### Distribuzione stazionaria
Per una catena di Markov ricorrente positiva e irriducibile, la distribuzione stazionaria π esiste, è unica e soddisfa:
πP = π, Σᵢ πᵢ = 1
**Interpretazione:** πᵢ = proporzione di lungo periodo del tempo trascorso nello stato i.
**Esempio funzionale:** Modello meteorologico con stati {Sereno, Pioggia}.
P = [[0,9, 0,1], [0,5, 0,5]] (righe: da soleggiato, da piovoso)
Distribuzione stazionaria: πP = π
- π₁ = 0,9π₁ + 0,5π₂
- π₂ = 0,1π₁ + 0,5π₂
- π₁ + π₂ = 1
- Risoluzione: π₁ = 5/6 ≈ 0,833, π₂ = 1/6 ≈ 0,167
### Convergenza alla stazionarietà
Per una catena ricorrente irriducibile, aperiodica e positiva:
- Pⁿ → Π (matrice con tutte le righe uguali a π) come n → ∞
- **Tempo di miscelazione:** Numero di passaggi finché la distribuzione non è vicina a π
- **Gamma spettrale:** 1 − |λ₂| (dove λ₂ è il secondo autovalore più grande) determina la velocità di miscelazione
### Catene di Markov a tempo continuo (CTMC)
Le transizioni avvengono in tempi casuali governati da distribuzioni esponenziali.
| Concetto | Descrizione |
|---------|-----|
| **Matrice dei tassi Q** | q_{ij} ≥ 0 per i ≠ j; q_{ii} = −Σ_{j≠i} q_{ij} |
| **Probabilità di transizione** | P(t) = e^{Qt} (esponenziale di matrice) |
| **Distribuzione stazionaria** | πQ = 0 |
| **Tempo di attesa** | Il tempo nello stato i è Exp(−q_{ii}) |
---

## Passeggiate casuali
Una **passeggiata casuale** è un percorso formato da passi casuali successivi.
### Passeggiata casuale semplice
X_n = X_{n-1} + Z_n, dove Z_n ∈ {+1, −1} con probabilità p, q = 1−p.
| Immobile | p = 1/2 (simmetrico) | p ≠ 1/2 (distorto) |
|----------|---------------------|-------------|
| E[X_n] | 0| n(2p−1) |
| Var[X_n] | n | 4npq |
| Ritorni all'origine? | Sì (con probabilità 1) | No (si allontana) |
| Ricorrente? | Sì (in 1D e 2D) | No |
### Passeggiata casuale nelle dimensioni superiori
| Dimensione | Ricorrente? | Intuizione |
|-----------|------------|------------|
| 1D | Sì | "Un ubriaco ritrova sempre la strada di casa" |
| 2D | Sì | "Un uccello ubriaco ritrova sempre la strada di casa" |
| 3D+ | No | "Un passerotto ubriaco non ritrova mai la strada di casa" |
### Connessione al moto browniano
Scalare una passeggiata casuale: sia S_n = ΣZ_i. Quindi come dimensione del passo → 0 e passi → ∞:
S_{⌊nt⌋} / √n → B(t) (moto browniano, per il teorema di Donsker)
---

## Moto Browniano
**Moto browniano** (processo di Wiener) B(t) è il limite temporale continuo di una passeggiata casuale.
### Definizione
B(t) soddisfa:
1. B(0) = 0
2. B(t) ha cammini continui
3. Incrementi indipendenti: B(t) − B(s) è indipendente da B(s) − B(r) per r < s < t
4. B(t) − B(s) ~ N(0, t − s) (incrementi gaussiani)
### Proprietà chiave
| Immobile | Dichiarazione |
|----------|-----------|
| E[B(t)] | = 0|
| Var[B(t)] | = t |
| Cov[B(s), B(t)] | = min(s, t) |
| Da nessuna parte differenziabile | I cammini sono continui ma non hanno derivata |
| Dimensione frattale | Il grafico ha dimensione di Hausdorff 3/2 |
| Proprietà Markov | Il futuro dipende solo dalla posizione attuale |
| Martingala | E[B(t) | F_s] = B(s) per s < t |
### Moto Browniano geometrico
S(t) = S(0) exp((μ − σ²/2)t + σB(t))
Questo è il modello standard per i prezzi delle azioni nel quadro Black-Scholes.
- μ: deriva (rendimento atteso)
- σ: volatilità
---

## Processi di Poisson
Un **processo di Poisson** N(t) conta il numero di eventi che si verificano in [0, t].
### Definizione
N(t) ~ Poisson(λt), dove λ è la frequenza (eventi per unità di tempo).
| Immobile | Dichiarazione |
|----------|-----------|
| N(0) = 0 | — |
| Incrementi indipendenti | Gli eventi in intervalli disgiunti sono indipendenti |
| Incrementi stazionari | N(t+s) − N(s) ~ Poisson(λt) |
| E[N(t)] | = λt |
| Var[N(t)] | = λt |
| Inter-arrivi | Distribuito esponenzialmente: T_i ~ Exp(λ) |
### Generalizzazioni
| Variante | Descrizione |
|---------|-----|
| **Non omogeneo** | La velocità λ(t) varia con il tempo |
| **Composto Poisson** | Ogni evento ha una dimensione casuale: S(t) = Σᵢ₌₁^{N(t)} Yᵢ |
| **Misura casuale di Poisson** | Punti nello spazio-tempo, non solo nel tempo |
| **Multivariata** | Tipi di eventi multipli con possibili interazioni |
---

## Martingale
Una **martingala** è un gioco leale: il valore futuro atteso, date tutte le informazioni attuali, è uguale al valore attuale.
### Definizione
{X_n} è una martingala rispetto alla filtrazione {F_n} se:
1. X_n è F_n-misurabile (adattato)
2. E[|X_n|] < ∞ (integrabile)
3. E[X_{n+1} | F_n] = X_n (gioco corretto)
| Variante | Condizione | Interpretazione |
|---------|-----------|----------------|
| **Martingala** | E[X_{n+1} | F_n] = X_n | Gioco giusto |
| **Submartingala** | E[X_{n+1} | F_n] ≥ X_n | Gioco favorevole (tendenza rialzista) |
| **Supermartingala** | E[X_{n+1} | F_n] ≤ X_n | Partita sfavorevole (tendenza al ribasso) |
### Teoremi chiave
| Teorema | Dichiarazione |
|---------|-----------|
| **Arresto facoltativo** | Nelle condizioni E[X_T] = E[X_0] per un tempo di arresto T |
| **Convergenza** | Una martingala delimitata converge quasi sicuramente |
| **Massima disuguaglianza** | P(max_{k≤n} X_k ≥ λ) ≤ E[X_n] / λ (di Doob) |
---

## Metodi Monte Carlo
I **metodi Monte Carlo** utilizzano il campionamento casuale per stimare quantità deterministiche.
### Idea di base
Per stimare E[f(X)] dove X ~ P:
1. Disegna N campioni: x₁, x₂, ..., x_N da P
2. Calcola: Î = (1/N) Σᵢ f(xᵢ)
3. Per la legge dei grandi numeri: Î → E[f(X)] come N → ∞
**Errore:** Errore standard = σ_f / √N, dove σ_f² = Var[f(X)]
### Tecniche di riduzione della varianza
| Tecnica | Idea | Accelera |
|-----------|------|---------|
| **Campionamento di importanza** | Campione da Q invece che da P, peso per P/Q | Può essere drammatico |
| **Varianti antitetiche** | Utilizzare le coppie (x, −x) per annullare la varianza | ~2x |
| **Il controllo varia** | Sottrarre la funzione di aspettativa nota correlata con f | Varia |
| **Campionamento stratificato** | Dividi il dominio, campiona ogni strato | Riduce la varianza |
| **Rao-Blackwell** | Condizione su statistiche sufficienti | Aiuta sempre |
---

## Catena Markov Monte Carlo (MCMC)
MCMC costruisce una catena di Markov la cui distribuzione stazionaria è la distribuzione target. Dopo un periodo di "rodaggio", i campioni si avvicinano al bersaglio.
### Algoritmo di Metropolis-Hastings
| Passo | Azione |
|------|--------|
| 1| Stato attuale: x_t |
| 2| Proporre: x* ~ q(x* \| x_t) (distribuzione della proposta) |
| 3| Rapporto di accettazione: α = min(1, [π(x*)q(x_t\|x*)] / [π(x_t)q(x*\|x_t)]) |
| 4| Accetta con probabilità α: x_{t+1} = x* (accetta) oppure x_t (rifiuta) |
**Caso speciale — Algoritmo di Metropolis:** Proposta simmetrica q(x*|x) = q(x|x*), quindi α = min(1, π(x*)/π(x_t)).
### Campionamento di Gibbs
Un caso speciale di Metropolis-Hastings in cui ciascuna variabile viene aggiornata dalla sua distribuzione condizionale completa.
Per l'obiettivo π(x₁, x₂, ..., xₖ):
1. Esempio x₁^{(t+1)} ~ π(x₁ | x₂^{(t)}, ..., xₖ^{(t)})
2. Esempio x₂^{(t+1)} ~ π(x₂ | x₁^{(t+1)}, x₃^{(t)}, ..., xₖ^{(t)})
3. Continuare per tutte le variabili
4. Ripeti
| Immobile | Dichiarazione |
|----------|-----------|
| Accetta sempre | α = 1 (nessuna fase di rifiuto) |
| Richiede | Possibilità di campionare da ogni condizionale completo |
| Convergenza | Garantito per catene irriducibili e aperiodiche |
### Diagnostica MCMC
| Diagnostica | Scopo |
|-----------|---------|
| **Traccia traccia** | Controllo visivo della miscelazione e della stazionarietà |
| **Autocorrelazione** | Misura la dipendenza dal campione (si desidera una bassa autocorrelazione) |
| **Gelman-Rubin (R̂)** | Confronta più catene; R̂ < 1,05 suggerisce convergenza |
| **Dimensione effettiva del campione** | N_eff = N/(1 + 2Σρₖ); tiene conto dell'autocorrelazione |
| **Burn-in** | Scartare i campioni iniziali prima che la catena raggiunga la stazionarietà |
---

## Rilevanza per l'apprendimento automatico e la scienza dei dati
| Processo stocastico | Applicazione |
|-------------------|-------------|
| Catene di Markov | PageRank (camminata casuale sul grafico web), generazione di testo (modelli n-grammi), MCMC |
| Passeggiate casuali | Node2Vec e DeepWalk (embedding di grafi), esplorazione in RL |
| Moto Browniano | Modellazione del prezzo delle azioni, modelli di diffusione nell'intelligenza artificiale generativa |
| Processi di Poisson | Modellazione degli arrivi di eventi (clic, fallimenti), teoria delle code |
| Martingale | Matematica finanziaria, dimostrazione della convergenza di SGD (approssimazione stocastica) |
| Montecarlo | Stima dei valori attesi, inferenza bayesiana, apprendimento per rinforzo (valutazione delle politiche) |
| MCMC (Metropoli-Hastings) | Campionamento a posteriori bayesiano, programmazione probabilistica (Stan, PyMC) |
| Campionamento di Gibbs | Modelli topici (LDA), reti bayesiane, denoising delle immagini |
| Diagnostica MCMC | Garantire un'inferenza affidabile da modelli probabilistici |
---

## Riepilogo
| Processo | Spazio statale | Tempo | Proprietà chiave |
|---------|-----|------|------|
| Catena di Markov | Discreto/continuo | Discreto/continuo | Senza memoria (proprietà di Markov) |
| Passeggiata casuale | ℤᵈ | Discreto | Somma dell'i.i.d. passi |
| Moto Browniano | ℝ | Continuo | Incrementi gaussiani, cammini continui |
| Processo di Poisson | ℕ | Continuo | Processo di conteggio con lacune esponenziali |
| Martingala | ℝ | Discreto/continuo | Gioco corretto (E[X_{t+1}|F_t] = X_t) |
I processi stocastici sono la matematica della casualità nel tempo. Essi sono alla base della moderna inferenza bayesiana (MCMC), dell’apprendimento per rinforzo (processi decisionali di Markov), della modellazione generativa (modelli di diffusione), della matematica finanziaria e della teoria delle code. Comprendere questi processi ti offre gli strumenti per modellare l'incertezza in modo dinamico, non solo come un'istantanea, ma man mano che si evolve.