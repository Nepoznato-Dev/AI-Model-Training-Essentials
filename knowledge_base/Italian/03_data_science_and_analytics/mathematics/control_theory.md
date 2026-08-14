---
# Metadata
title: "Control Theory"
description: "Transfer functions, block diagrams, feedback loops, PID controllers, stability analysis, state-space representation, and optimal control"
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
    changes: "Initial deep-dive into control theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [control-theory, transfer-functions, pid-controllers, feedback, stability, state-space, optimal-control]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "signal_processing.md"
  - "dynamical_systems.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Teoria del controllo
La teoria del controllo è la matematica che permette ai sistemi di comportarsi nel modo desiderato. Dai termostati agli autopiloti, dai bracci robotici ai reattori chimici, i sistemi di controllo rilevano, decidono e agiscono per mantenere il comportamento desiderato. Il campo fornisce strumenti rigorosi per analizzare stabilità, prestazioni e robustezza, concetti che sono migrati nell’apprendimento per rinforzo, nella regolazione degli iperparametri e nei sistemi adattivi.
---

## Concetti fondamentali
### Circuito aperto e circuito chiuso
| Digitare | Descrizione | Esempio | Vantaggio |
|------|-------------|---------|-----------|
| **A circuito aperto** | Azione di controllo indipendente dall'uscita | Temporizzatore lavatrice | Semplice, non è necessario alcun sensore |
| **A circuito chiuso (feedback)** | L'azione di controllo dipende dall'uscita | Termostato, regolatore di velocità | Respinge i disturbi, robusto |
### Elementi del diagramma a blocchi
| Elemento | Simbolo | Funzione |
|---------|--------|----------|
| **Pianta** | G(s) | Il sistema controllato |
| **Controllore** | C(s) | Calcola l'azione di controllo |
| **Sensore** | H(s) | Misura l'uscita |
| **Giunzione sommatoria** | ⊕ | Errore di calcolo: r − y |
| **Riferimento** | r(t) | Risultato desiderato |
| **Errore** | e(t) = r(t) − y(t) | Differenza tra desiderato ed effettivo |
| **Disturbo** | d(t) | Input indesiderati che colpiscono l'impianto |
### Funzione di trasferimento ad anello chiuso
Per un sistema di feedback negativo standard:
T(s) = C(s)G(s) / (1 + C(s)G(s)H(s))
| Quantità | Formula |
|----------|---------|
| Funzione di trasferimento ad anello aperto | L(s) = C(s)G(s)H(s) |
| Funzione di trasferimento ad anello chiuso | T(s) = L(s)/H(s) / (1 + L(s)) |
| Funzione di trasferimento errori | E(s)/R(s) = 1 / (1 + L(s)) |
| Sensibilità | S(s) = 1 / (1 + L(s)) |
---

## Funzioni di trasferimento
Una **funzione di trasferimento** H(s) = Y(s)/X(s) descrive la relazione input-output di un sistema lineare tempo-invariante (LTI) nel dominio di Laplace.
### Moduli standard
| Sistema | Funzione di trasferimento | Parametri |
|--------|-------------|------------|
| **Primo ordine** | K/(τs + 1) | K = guadagno, τ = costante di tempo |
| **Secondo ordine** | Kωₙ²/(s² + 2ζωₙs + ωₙ²) | ωₙ = frequenza naturale, ζ = rapporto di smorzamento |
| **Integratore** | K/s | — |
| **Differenziatore** | Ks | — |
| **Ritardo** | e^{−sT_d} | T_d = ritardo |
### Comportamento del sistema di secondo ordine
| Rapporto di smorzamento ζ | Comportamento | Posizioni dei poli |
|-----------------|-----------|---------------|
| ζ = 0 | Oscillazione non smorzata | Puro immaginario |
| 0< ζ < 1 | Underdamped (oscillates, decays) | Complex with negative real part |
| ζ = 1 | Critically damped (fastest no-oscillation) | Real, repeated |
| ζ >1 | Sovrasmorzato (lento, nessuna oscillazione) | Reale, distinto |
### Metriche prestazionali (risposta al gradino)
| Metrico | Formula (2° ordine, sottosmorzata) | Descrizione |
|--------|---------------------------|-----|
| Tempo di salita (t_r) | ≈ 1,8/ωₙ | È ora di passare dal 10% al 90% |
| Orario di punta (t_p) | π/(ωₙ√(1−ζ²)) | Tempo al primo massimo |
| Superamento (M_p) | e^{−πζ/√(1−ζ²)} × 100% | Picco massimo sopra il valore finale |
| Tempo di assestamento (t_s) | ≈ 4/(ζωₙ) | Tempo per restare entro il 2% finale |
| Errore a regime | Dipende dal tipo di sistema | Differenza tra desiderato ed effettivo come t → ∞ |
---

## Controller PID
Il **controllore PID** è il controllore più utilizzato nell'industria (oltre il 90% dei controllori industriali).
### Formula PID
u(t) = K_p e(t) + K_i ∫₀ᵗ e(τ)dτ + K_d de(t)/dt
Nel dominio di Laplace: C(s) = K_p + K_i/s + K_d s
| Termine | Effetto | Troppo | Troppo poco |
|------|--------|----------|------------|
| **Proporzionale (K_p)** | Reagisce all'errore attuale | Oscillazione, instabilità | Risposta lenta, errore grave |
| **Integrale (K_i)** | Elimina l'errore di stato stazionario | Superamento, oscillazione | Offset persistente |
| **Derivata (K_d)** | Predice l'errore futuro (smorzamento) | Amplificazione del rumore | Scarsa reiezione ai disturbi |
### Metodi di regolazione PID
| Metodo | Avvicinamento |
|--------|----------|
| **Ziegler-Nichols** | Aumentare K_u fino all'oscillazione; utilizzare K_u e il periodo P_u per impostare i guadagni |
| **Cohen-Coon** | Basato sui parametri di risposta al gradino (guadagno, costante di tempo, tempo morto) |
| **IMC (Controllo del Modello Interno)** | Basato sul modello di processo; fornisce una buona robustezza |
| **Sintonizzazione automatica** | Identificazione online + ottimizzazione (molti controller moderni) |
| **Manuale** | Inizia solo con K_p, aggiungi K_i per rimuovere l'offset, aggiungi K_d per lo smorzamento |
### Regole di Ziegler-Nichols
1. Imposta K_i = K_d = 0
2. Aumentare K_p fino all'oscillazione sostenuta: guadagno ultimo K_u, periodo P_u
3. Imposta i guadagni:
| Controllore | K_p | K_i | K_d |
|-----------|-----|-----|-----|
| P| 0.5K_u | — | — |
| P.I. | 0.45K_u | 1.2K_u/P_u | — |
| PID | 0.6K_u | 2K_u/P_u | K_u P_u/8 |
---

## Analisi di stabilità
Un sistema è **stabile** se il suo output rimane limitato per input limitati (stabilità BIBO).
### Stabilità basata sui pali
| Condizione | Stabilità |
|-----------|-----------|
| Tutti i poli nel semipiano sinistro (Re(s)< 0) | Stable |
| Any pole in right half-plane (Re(s) >0) | Instabile |
| Poli sull'asse immaginario (Re(s) = 0) | Marginalmente stabile (o instabile per ripetuto) |
### Criterio di Routh-Hurwitz
Determina la stabilità senza calcolare esplicitamente i poli. Costruisce la matrice Routh dai coefficienti polinomiali caratteristici.
**Regola:** Il numero di cambiamenti di segno nella prima colonna è uguale al numero di poli del semipiano destro.
### Criterio di stabilità di Nyquist
Traccia la risposta in frequenza ad anello aperto L(jω) nel piano complesso.
**Regola:** Il sistema a circuito chiuso è stabile se il diagramma di Nyquist circonda il punto (−1, 0) in senso antiorario un numero di volte pari al numero di poli instabili a circuito aperto.
**Margine di guadagno:** Quanto guadagno può aumentare prima dell'instabilità (distanza dal grafico a −1 sull'asse reale).
**Margine di fase:** quanto può aumentare il ritardo di fase prima dell'instabilità (angolo dal grafico al cerchio unitario al crossover del guadagno).
### Analisi del diagramma di Bode
Traccia il guadagno (dB) e la fase (gradi) rispetto alla frequenza (scala logaritmica).
| Metrico | Definizione | Valore desiderato |
|--------|-----------|---------------|
| **Margine di guadagno (GM)** | Aumento del guadagno per raggiungere 0 dB alla fase = −180° | >6dB|
| **Margine di fase (PM)** | Fase al crossover del guadagno (0 dB) + 180° | > 45°|
| **Guadagno crossover** | Frequenza dove guadagno = 0 dB | — |
| **Incrocio di fase** | Frequenza dove fase = −180° | — |
---

## Rappresentazione dello Spazio-Stato
Per i sistemi MIMO (multi-input multi-output), la forma dello spazio degli stati è più naturale delle funzioni di trasferimento.
### Modulo standard
ẋ(t) = Ax(t) + Bu(t) (equazione di stato)
y(t) = Cx(t) + Du(t) (equazione di uscita)
| Matrice | Nome | Dimensioni |
|--------|------|-----------|
| A | Matrice sistema/stato | n×n |
| B | Matrice di input | n×m |
| C| Matrice di output | p×n |
| D | Matrice feedthrough | p×m |
### Funzione di trasferimento dallo spazio degli stati
G(s) = C(sI − A)⁻¹B + D
### Controllabilità e osservabilità
| Immobile | Prova | Significato |
|----------|------|---------|
| **Controllabile** | Rango[C_B] = n (dove C_B = [B, AB, A²B, ...]) | Può dirigersi verso qualsiasi stato |
| **Osservabile** | Rango[O_B] = n (dove O_B = [C; CA; CA²; ...]) | Può determinare lo stato dall'output |
Un sistema deve essere controllabile per essere stabilizzabile tramite feedback e osservabile per la stima dello stato.
### Feedback sullo stato
u = −Kx + r (feedback a stato completo)
Ad anello chiuso: ẋ = (A − BK)x + Br
**Posizionamento dei poli:** scegli K in modo tale che A − BK abbia gli autovalori desiderati (poli).
---

## Controllo ottimale
### Regolatore lineare quadratico (LQR)
Minimizzare: J = ∫₀^∞ (xᵀQx + uᵀRu) dt
dove Q ≥ 0 (costo statale) e R > 0 (costo di controllo).
**Soluzione:** u = −Kx dove K = R⁻¹BᵀP, e P risolve l'**equazione algebrica di Riccati:**
AᵀP + PA − PBR⁻¹BᵀP + Q = 0
| Sintonia | Effetto |
|--------|--------|
| Aumenta Q | Risposta più rapida, maggiore sforzo di controllo |
| Aumenta R | Risposta più lenta, minore sforzo di controllo |
| Q ≫ R | Controllo aggressivo (come K_p alto) |
### Filtro di Kalman
Lo stimatore ottimo dello stato per sistemi lineari con rumore gaussiano.
**Modello di sistema:**
ẋ = Ax + Bu + w (rumore di processo w ~ N(0, Q))
y = Cx + v (rumore di misura v ~ N(0, R))
**Equazioni del filtro di Kalman:**
- Prevedi: x̂⁻ = Ax̂ + Bu, P⁻ = APAᵀ + Q
- Aggiornamento: K = P⁻Cᵀ(CP⁻Cᵀ + R)⁻¹, x̂ = x̂⁻ + K(y − Cx̂⁻), P = (I − KC)P⁻
Il filtro di Kalman è il doppio LQR: minimizza la varianza dell'errore di stima.
---

## Rilevanza per l'apprendimento automatico e la scienza dei dati
| Concetto di teoria del controllo | Applicazione |
|----------------------|-----|
| Controllo del feedback | Tassi di apprendimento adattivo, stabilizzazione della formazione |
| Regolatori PID | Ottimizzazione degli iperparametri, controllo della temperatura nei data center |
| Modelli nello spazio degli stati | Modellazione di serie temporali, reti neurali ricorrenti |
| Filtro Kalman | Tracking, fusione di sensori, stima dello stato, previsione di serie temporali |
| LQR / controllo ottimale | Apprendimento per rinforzo (controllo LQG), robotica |
| Analisi di stabilità | Dinamiche di training dei GAN, convergenza degli algoritmi RL |
| Controllabilità/osservabilità | Comprensione dell'espressività delle RNN, identificazione del sistema |
| Funzioni di trasferimento | Comprendere le CNN come filtri lineari, analisi nel dominio della frequenza |
| Nyquist/Bode | Analisi di robustezza per sistemi adattivi |
| Posizionamento dei pali | Progettare dinamiche di sistemi appresi (ODE neurali) |
---

## Riepilogo
| Concetto | Idea fondamentale | Strumento chiave |
|---------|-----------|----------|
| Feedback | Utilizzare l'output per correggere l'input | Funzione di trasferimento ad anello chiuso |
| Funzione di trasferimento | Relazione input-output nel dominio s | G(s) = Y(s)/X(s) |
| Controllo PID | Proporzionale + Integrale + Derivata | Il controller industriale più utilizzato |
| Stabilità | Output limitato per input limitato | Routh-Hurwitz, Nyquist, Bode |
| Spazio degli stati | Rappresentanza interna dello Stato | ẋ = Ax + Bu, y = Cx + Du |
| Controllabilità | Possiamo raggiungere qualsiasi stato? | Test del rango sulla matrice di controllabilità |
| Osservabilità | Possiamo dedurre lo stato? | Test del rango sulla matrice di osservabilità |
| LQR | Feedback sullo stato ottimale | Equazione di Riccati |
| Filtro Kalman | Stima dello stato ottimale | Ciclo di previsione-aggiornamento |
La teoria del controllo è la matematica che permette ai sistemi di fare quello che vuoi: in modo affidabile, robusto ed efficiente. I suoi principi di feedback, stabilità e ottimalità si sono rivelati universali, apparendo in campi che vanno dalla robotica all’apprendimento per rinforzo, dall’economia alla biologia. Per i data scientist, la teoria del controllo fornisce il linguaggio per comprendere i sistemi adattivi, progettare procedure di formazione stabili e costruire agenti intelligenti che interagiscono con ambienti dinamici.