<!--
---
# Metadata
title: "Dynamical Systems"
description: "Ordinary and partial differential equations, phase portraits, equilibrium and stability, Lyapunov functions, chaos theory, Lorenz attractor, bifurcation diagrams, and PDEs"
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
    changes: "Initial deep-dive into dynamical systems"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [dynamical-systems, ode, pde, phase-portraits, stability, chaos, lorenz-attractor, bifurcation, lyapunov]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
  - "numerical_methods.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Sistemi Dinamici
Un **sistema dinamico** descrive come uno stato si evolve nel tempo secondo una regola fissa. Dalle orbite planetarie alle dinamiche delle popolazioni, dai modelli meteorologici all’addestramento delle reti neurali, la teoria dei sistemi dinamici fornisce il linguaggio e gli strumenti per comprendere come cambiano le cose. Questo file tratta le equazioni differenziali ordinarie (ODE), le equazioni differenziali parziali (PDE), l'analisi di stabilità, il caos e le biforcazioni.
---

## Equazioni differenziali ordinarie (ODE)
Un'ODE mette in relazione una funzione con le sue derivate rispetto a una singola variabile indipendente (solitamente il tempo).
### Classificazione
| Immobile | Tipi |
|----------|-------|
| **Ordine** | Derivata più alta presente (1° ordine, 2° ordine, ecc.) |
| **Lineare vs Non lineare** | Lineare: y'' + p(t)y' + q(t)y = g(t); Non lineare: qualsiasi altra cosa |
| **omogeneo** | g(t) = 0 (nessun termine forzante) |
| **Autonomo** | Nessuna dipendenza temporale esplicita: dy/dt = f(y) |
| **Coefficienti costanti** | p, q sono costanti |
### ODE del primo ordine
**Forma generale:** dy/dt = f(t, y)
| Digitare | Modulo | Metodo risolutivo |
|------|------|-----------------|
| Separabile | dy/dt = g(t)h(y) | Separa e integra: ∫dy/h(y) = ∫g(t)dt |
| Primo ordine lineare | dy/dt + p(t)y = q(t) | Fattore di integrazione: μ(t) = e^(∫p dt) |
| Esatto | M(t,y)dt + N(t,y)dy = 0 con ∂M/∂y = ∂N/∂t | Trova la funzione potenziale F(t,y) |
| Bernoulli | dy/dt + p(t)y = q(t)yⁿ | Sostituisci v = y^(1−n) per linearizzare |
**Esempio elaborato (fattore di integrazione):** Risolvi dy/dt + 2y = e^(−t), y(0) = 1.
- Fattore di integrazione: μ(t) = e^(∫2 dt) = e^(2t)
- Moltiplica: d/dt[e^(2t)y] = e^(2t) · e^(−t) = e^t
- Integra: e^(2t)y = e^t + C
- y(t) = e^(−t) + Ce^(−2t)
- Condizione iniziale: y(0) = 1 → 1 = 1 + C → C = 0
- Soluzione: y(t) = e^(−t)
### ODE lineari del secondo ordine
**Forma generale:** ay'' + by' + cy = g(t)
**Caso omogeneo** (g ​​= 0): Risolvi l'equazione caratteristica ar² + br + c = 0.
| Discriminante | Radici | Soluzione generale |
|-------------|-------|------------|
| b² > 4ac (sovrasmorzato) | Due reali distinti r₁, r₂ | y = C₁e^(r₁t) + C₂e^(r₂t) |
| b² = 4ac (smorzato in modo critico) | Radice reale ripetuta r | y = (C₁ + C₂t)e^(rt) |
| b² < 4ac (sottosmorzato) | Radici complesse α ± βi | y = e^(αt)(C₁ cos βt + C₂ sin βt) |
**Interpretazione fisica:** Un sistema massa-molla-smorzatore mx'' + bx' + kx = 0.
- Overdamped: smorzamento pesante, nessuna oscillazione (chiudiporta)
- Smorzamento critico: ritorno più rapido senza oscillazioni (obiettivo di progettazione delle sospensioni dell'auto)
- Underdamped: oscilla con ampiezza decrescente (corda di chitarra)
### Sistemi di ODE
Molti sistemi reali coinvolgono più variabili interagenti:
dx/dt = f(x, y)
dy/dt = g(x, y)
Questo può essere scritto in forma vettoriale: d**x**/dt = **F**(**x**)
**Sistemi lineari:** d**x**/dt = A**x**, dove A è una matrice.
La soluzione dipende dagli autovalori di A:
| Autovalori | Comportamento |
|-------------|-----------|
| Entrambi reali, negativi | Nodo stabile (tutte le traiettorie convergono all'origine) |
| Entrambi reali, positivi | Nodo instabile |
| Segni reali, opposti | Punto di sella (instabile) |
| Parte reale complessa, negativa | Spirale stabile (oscillazione smorzata) |
| Parte reale complessa e positiva | Spirale instabile |
| Puro immaginario | Centro (orbite chiuse) |
---

## Ritratti in fase
Un **ritratto di fase** visualizza le traiettorie di un sistema dinamico nello spazio degli stati (senza risolverlo esplicitamente).
### Caratteristiche principali
| Caratteristica | Descrizione |
|---------|-----|
| **Punto fisso (equilibrio)** | Dove dx/dt = 0 (nessun movimento) |
| **Traiettoria** | Percorso tracciato dal sistema nello spazio degli stati |
| **Clina nulla** | Curva in cui la derivata di una componente è zero |
| **Ciclo limite** | Orbita chiusa isolata (oscillazione autosostenuta) |
| **Bacino di attrazione** | Insieme di condizioni iniziali che portano ad un dato attrattore |
| **Separatrice** | Confine tra diversi bacini di attrazione |
### Modello Predatore-Preda (Lotka-Volterra)
dx/dt = αx − βxy (preda)
dy/dt = δxy − γy (predatore)
**Punti fissi:**
1. (0, 0) — estinzione (punto di sella)
2. (γ/δ, α/β) — coesistenza (centro — orbite chiuse)
Il sistema presenta oscillazioni periodiche: aumenta la preda → aumentano i predatori → diminuisce la preda → diminuiscono i predatori → il ciclo si ripete.
---

## Analisi di stabilità
### Stabilità lineare
Per un punto fisso x*, linearizzalo attorno ad esso: sia u = x − x*, quindi du/dt ≈ J(x*)u dove J è la matrice Jacobiana.
**Criterio di stabilità:** Il punto fisso è:
- **Stabile** se tutti gli autovalori di J hanno parte reale negativa
- **Instabile** se qualsiasi autovalore ha parte reale positiva
- **Marginalmente stabile** se gli autovalori hanno zero parti reali (è necessaria un'analisi non lineare)
### Stabilità di Lyapunov
**Il metodo diretto di Lyapunov** determina la stabilità senza linearizzazione.
Una **funzione di Lyapunov** V(x) soddisfa:
1. V(x*) = 0 e V(x) > 0 per x ≠ x* (definito positivo)
2. dV/dt ≤ 0 lungo le traiettorie (non crescente)
| Condizione | Conclusione |
|-----------|------------|
| dV/dt< 0 (negative definite) | Asymptotically stable |
| dV/dt ≤ 0 (negative semi-definite) | Stable (but may not converge) |
| dV/dt >0 | Instabile |
**Esempio elaborato:** Sistema dx/dt = −x + y², dy/dt = −y.
- Prova V(x,y) = x² + y² (funzione di tipo energetico)
- dV/dt = 2x(−x + y²) + 2y(−y) = −2x² + 2xy² − 2y²
- Vicino all'origine: dV/dt ≈ −2x² − 2y² < 0 (per y piccoli, prevale −2y²)
- Conclusione: l'origine è localmente asintoticamente stabile
---

## Teoria del caos
Il **caos** è deterministico e tuttavia imprevedibile: il sistema segue regole precise, ma piccole differenze nelle condizioni iniziali portano a risultati molto diversi.
### Requisiti per il Caos
| Immobile | Descrizione |
|----------|-------------|
| deterministico | Nessuna casualità – governata da equazioni esatte |
| Sensibile alle condizioni iniziali | Le traiettorie vicine divergono esponenzialmente |
| Limitato | Le traiettorie non sfuggono all'infinito |
| Non periodico | Non si ripete mai esattamente |
### Il sistema Lorenz
Il classico esempio di caos deterministico:
dx/dt = σ(y − x)
dy/dt = x(ρ − z) − y
dz/dt = xy − βz
Con parametri standard σ = 10, ρ = 28, β = 8/3:
- Il sistema ha tre punti fissi, tutti instabili
- Le traiettorie orbitano attorno a un punto fisso, quindi passano improvvisamente all'altro
- Il risultato è l'**attrattore di Lorenz** — uno strano attrattore con struttura frattale
**Esponente di Lyapunov:** Misura il tasso di divergenza delle traiettorie vicine.
- Esponente di Lyapunov positivo → caos
- Per il sistema Lorenz con parametri standard: esponente più grande ≈ 0,9 > 0
### La mappa logistica
Un semplice sistema discreto che presenta caos:
x_{n+1} = rx_n(1 − x_n)
| Parametro r | Comportamento |
|-------------|-----------|
| 0 < r < 1 | La popolazione si estingue (x → 0) |
| 1 < r < 3 | Punto fisso stabile in x = 1 − 1/r |
| 3 < r < 3.449 | Oscillazione del periodo 2 |
| 3.449 < r < 3.544 | Oscillazione del periodo 4 |
| 3.544 < r < 3.570 | Periodo-8, 16, 32, ... (cascata del raddoppio del periodo) |
| r ≈ 3.570 | Inizio del caos |
| 3.570 < r < 4 | Per lo più caotico, con finestre periodiche |
| r = 4| Completamente caotico su [0, 1] |
### Effetto farfalla
Il nome popolare per la dipendenza sensibile dalle condizioni iniziali. Nei sistemi meteorologici (modellati dalle equazioni di Lorenz), una farfalla che sbatte le ali in Brasile potrebbe scatenare un tornado in Texas, non perché sia ​​la farfalla a provocarlo, ma perché piccole perturbazioni crescono in modo esponenziale.
---

## Teoria della biforcazione
Una **biforcazione** è un cambiamento qualitativo nel comportamento del sistema quando un parametro viene variato.
### Tipi di biforcazioni
| Biforcazione | Forma normale | Cosa succede |
|-------------|-------------|--------------|
| **Nodo a sella** | dx/dt = r − x² | Due punti fissi appaiono/scompaiono |
| **Transcritico** | dx/dt = rx − x² | Due punti fissi si scambiano stabilità |
| **Forcone (supercritico)** | dx/dt = rx − x³ | Un punto stabile si divide in due stabili + uno instabile |
| **Forcone (subcritico)** | dx/dt = rx + x³ | Crollo dei rami instabili (spesso catastrofico) |
| **Hopf** | Sistema 2D | Il punto fisso diventa instabile, appare il ciclo limite |
### Diagramma della biforcazione
Un grafico di punti fissi rispetto al valore del parametro, che mostra la stabilità (solido = stabile, tratteggiato = instabile). Il diagramma di biforcazione della mappa logistica rivela il percorso di raddoppio del periodo verso il caos e la famosa **costante di Feigenbaum** δ ≈ 4,669 (rapporto universale tra successivi intervalli di biforcazione).
---

## Equazioni alle derivate parziali (PDE)
Le PDE coinvolgono funzioni di più variabili e le loro derivate parziali.
### Classificazione delle PDE lineari del secondo ordine
Per Au_xx + 2Bu_xy + Cu_yy + ... = 0:
| Digitare | Condizione | Comportamento | Esempio |
|------|-----------|-----------|---------|
| **Ellittica** | B² − AC< 0 | Steady-state, no time dependence | Laplace's equation: ∇²u = 0 |
| **Parabolic** | B² − AC = 0 | Diffusion, smoothing over time | Heat equation: u_t = αu_xx |
| **Hyperbolic** | B² − AC >0 | Propagazione delle onde, preserva le caratteristiche nitide | Equazione delle onde: u_tt = c²u_xx |
### L'equazione del calore
∂u/∂t = α ∂²u/∂x²
Modelli di diffusione del calore, diffusione della popolazione, pricing delle opzioni (Black-Scholes).
| Immobile | Dichiarazione |
|----------|-----------|
| Levigatura | Le soluzioni diventano fluide all'istante, anche da dati iniziali discontinui |
| Principio del massimo | La temperatura massima si verifica al confine o al momento iniziale |
| Reversibilità temporale | Irreversibile: non può funzionare all'indietro |
### L'equazione delle onde
∂²u/∂t² = c² ∂²u/∂x²
Modella corde vibranti, suono, onde elettromagnetiche.
| Immobile | Dichiarazione |
|----------|-----------|
| Propagazione | Le perturbazioni viaggiano a velocità c |
| Reversibilità | Reversibile nel tempo |
| Soluzione d'Alembert | u(x,t) = f(x−ct) + g(x+ct) (sovrapposizione onde sinistra/destra) |
### Equazione di Laplace
∇²u = ∂²u/∂x² + ∂²u/∂y² = 0
Le soluzioni (funzioni armoniche) rappresentano la temperatura stazionaria, il potenziale elettrostatico, il flusso del fluido incomprimibile.
| Immobile | Dichiarazione |
|----------|-----------|
| Proprietà del valore medio | u(x₀) = media di u su qualsiasi cerchio centrato in x₀ |
| Principio del massimo | Nessun massimo o minimo interno |
| Unicità | Interamente determinato dalle condizioni al contorno |
---

## Rilevanza per l'apprendimento automatico e la scienza dei dati
| Concetto DS | Applicazione |
|-----------|-------------|
| ODE | ODE neurali (reti a profondità continua), dinamiche di rete ricorrenti |
| Analisi di stabilità | Dinamica dell'allenamento della discesa del gradiente (la perdita diminuisce stabilmente?) |
| Funzioni di Lyapunov | Dimostrazione della convergenza degli algoritmi di apprendimento, stabilità dell'apprendimento per rinforzo |
| Caos | Comprendere la sensibilità nelle RNN (gradienti di fuga/esplosione), previsioni meteorologiche |
| Biforcazione | Transizioni di fase nell'apprendimento (grokking), cambiamenti di regime nelle dinamiche formative |
| PDE | Modelli di diffusione (modelli generativi basati su punteggi), reti neurali informate dalla fisica |
| Equazione del calore | Processi di diffusione nella modellazione generativa, grafico smoothing laplaciano |
| Equazione delle onde | Elaborazione dati sismici, modellazione del segnale audio |
| Lotka-Volterra | Dinamiche della popolazione, epidemiologia, agenti ML concorrenti |
| Ritratti di fase | Visualizzazione delle dinamiche del panorama delle perdite, comprensione della formazione GAN |
---

## Riepilogo
| Argomento | Idea fondamentale | Strumento chiave |
|-------|-----------|----------|
| ODE | Funzioni e loro derivate temporali | Equazioni caratteristiche, fattori di integrazione |
| Sistemi di ODE | Variabili interagenti multiple | Analisi degli autovalori dello Jacobiano |
| Ritratti di fase | Visualizzare la dinamica nello spazio degli stati | Punti fissi, linee nulle, cicli limite |
| Stabilità | Il sistema tornerà all’equilibrio? | Linearizzazione, funzioni di Lyapunov |
| Caos | Imprevedibilità deterministica | Esponenti di Lyapunov, attrattori strani |
| Biforcazioni | Cambiamenti qualitativi con parametri | Forme normali, diagrammi di biforcazione |
| PDE | Funzioni di più variabili | Calore, onde ed equazioni di Laplace |
La teoria dei sistemi dinamici è la matematica del cambiamento. Spiega perché alcuni sistemi si stabilizzano, perché alcuni oscillano e perché altri si comportano in modo caotico. Per i data scientist, fornisce strumenti per comprendere le dinamiche di addestramento, progettare algoritmi stabili, modellare serie temporali e costruire la prossima generazione di modelli di machine learning basati sulla fisica.