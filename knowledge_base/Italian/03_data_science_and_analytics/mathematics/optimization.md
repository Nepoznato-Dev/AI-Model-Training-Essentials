---
# Metadata
title: "Optimization"
description: "Linear programming, convex optimization, gradient descent variants, Lagrange multipliers, KKT conditions, duality, integer programming, and heuristic methods"
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
    changes: "Initial deep-dive into optimization"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [optimization, linear-programming, convex-optimization, gradient-descent, lagrange-multipliers, kkt, duality, integer-programming]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Ottimizzazione
L'ottimizzazione è la matematica con cui si trova la soluzione migliore da un insieme di soluzioni fattibili. Si chiede: data una funzione e dei vincoli, quale input minimizza (o massimizza) l'output? L'ottimizzazione è il motore dell'apprendimento automatico: addestrare un modello significa ridurre al minimo una funzione di perdita. Appare nella ricerca operativa, nell'economia, nella progettazione ingegneristica e praticamente in ogni campo quantitativo.
---

## Formulazione del problema
Un generale **problema di ottimizzazione** ha la forma:
Minimizza f(x)
Soggetto a: gᵢ(x) ≤ 0 (vincoli di disuguaglianza), hⱼ(x) = 0 (vincoli di uguaglianza)
| Termine | Significato |
|------|---------|
| **Funzione obiettivo** f(x) | La quantità da minimizzare (o massimizzare) |
| **Variabili decisionali** x | I valori che possiamo controllare |
| **Regione fattibile** | Insieme di tutti gli x che soddisfano tutti i vincoli |
| **Minimo globale** | X* ammissibile con f(x*) ≤ f(x) per ogni x ammissibile |
| **Minimo locale** | x* ammissibile con f(x*) ≤ f(x) per tutti gli x ammissibili in qualche intorno |
| **Problema convesso** | f è convesso, la regione ammissibile è un insieme convesso (min locale = min globale) |
---

## Programmazione lineare (LP)
Quando sia l'obiettivo che tutti i vincoli sono **lineari**, il problema è un programma lineare.
### Modulo standard
Ridurre al minimo il cᵀx
Soggetto a: Ax ≤ b, x ≥ 0
dove c, x ∈ ℝⁿ, A ∈ ℝᵐˣⁿ, b ∈ ℝᵐ.
### Proprietà
| Immobile | Dichiarazione |
|----------|-----------|
| Convessità | LP è sempre un problema convesso |
| Soluzione ottimale | Sempre in un vertice (punto d'angolo) del politopo ammissibile |
| Esistenza | Se la regione ammissibile è limitata e non vuota, esiste la soluzione ottima |
| Ottimi multipli | Se due vertici sono ottimali, anche ogni punto sul bordo tra di loro è ottimale |
### Il metodo del semplice
Il **metodo del simplesso** (Dantzig, 1947) si muove lungo i bordi del politopo ammissibile da vertice a vertice, migliorando sempre l'obiettivo, fino a raggiungere l'ottimo.
| Immobile | Valore |
|----------|-------|
| Il momento peggiore | O(2ⁿ) (esponenziale — raro nella pratica) |
| Tempo medio | Polinomio per la maggior parte dei problemi pratici |
| Idea chiave | Spostarsi al vertice adiacente con valore obiettivo migliore |
**Algoritmo (panoramica):**
1. Iniziare da una soluzione ammissibile di base (vertice del politopo)
2. Scegli una variabile di ingresso (una che migliori l'obiettivo)
3. Scegli una variabile uscente (mantieni la fattibilità)
4. Pivot: spostati sul nuovo vertice
5. Ripetere finché non esiste alcuna direzione di miglioramento
### Metodi dei punti interni
Alternativa al simplesso: approccio all'ottimo dall'interno della regione ammissibile.
| Immobile | Valore |
|----------|-------|
| Il momento peggiore | Polinomio (O(n³·⁵) per alcune varianti) |
| Prestazioni pratiche | Competitivo con simplex su problemi di grandi dimensioni |
| Idea chiave | Seguire un "percorso centrale" attraverso l'interno |
### Esempio di LP lavorato
**Problema:** Una fabbrica produce sedie (x₁) e tavoli (x₂).
- Profitto: $ 30 per sedia, $ 50 per tavolo
- Legno: 2x₁ + 4x₂ ≤ 100 (piedini disponibili)
- Manodopera: x₁ + 3x₂ ≤ 60 (ore disponibili)
- Massimizza: 30x₁ + 50x₂
**Soluzione (metodo grafico per 2 variabili):**
- Vertici della regione ammissibile: (0,0), (30,0), (40,10), (0,20)
- Valutare l'obiettivo in ciascun vertice:
  - (0,0): profitto = 0
  - (30,0): profitto = 900
  - (40,10): profitto = 1700 ← ottimale
  - (0,20): profitto = 1000
- **Ottimale:** x₁ = 40 sedie, x₂ = 10 tavoli, profitto = $1700
---

## Ottimizzazione convessa
Un problema è **convesso** se la funzione obiettivo è convessa e la regione ammissibile è un insieme convesso.
### Insiemi e funzioni convessi
| Concetto | Definizione |
|---------|------------|
| **Insieme convesso** | Per ogni x, y nell'insieme et ∈ [0,1]: anche tx + (1−t)y è nell'insieme |
| **Funzione convessa** | f(tx + (1−t)y) ≤ tf(x) + (1−t)f(y) per ogni t ∈ [0,1] |
| **Strettamente convesso** | La disuguaglianza è stretta per t ∈ (0,1) e x ≠ y |
**Proprietà chiave:** Per l'ottimizzazione convessa, ogni minimo locale è un minimo globale.
### Funzioni convesse comuni
| Funzione | Convesso? | Dove |
|----------|---------|-------|
| ax + b (lineare) | Sì (e concavo) | Ovunque |
| x² | Sì | ℝ |
| eˣ | Sì | ℝ |
| −log(x) | Sì | x > 0 |
| \|x\|ᵖ (p ≥ 1) | Sì | ℝⁿ |
| max(f₁, f₂) se f₁, f₂ convesso | Sì | Intersezione di domini |
### Discesa gradiente
L'algoritmo di ottimizzazione più fondamentale nell'apprendimento automatico.
**Regola di aggiornamento:** x_{k+1} = x_k − α∇f(x_k)
dove α > 0 è il **tasso di apprendimento** (dimensione del passo).
| Variante | Aggiorna regola | Vantaggio |
|---------|-------------|-----------|
| **Lotto GD** | x ← x − α∇f(x) | Convergenza stabile |
| **GD stocastico (SGD)** | x ← x − α∇fᵢ(x) (un campione) | Veloce per iterazione, sfugge ai minimi locali |
| **Mini-lotto SGD** | x ← x − α(1/|B|)Σᵢ∈B ∇fᵢ(x) | Equilibrio tra batch e stocastico |
| **Slancio** | v ← βv − α∇f(x); x ← x + v | Accelera attraverso le regioni pianeggianti |
| **Adamo** | Tassi di apprendimento adattivo per parametro | Funziona bene fin dall'inizio per il deep learning |
| **RMSprop** | Ridimensiona il tasso di apprendimento eseguendo la media dell'entità del gradiente | Buono per gli RNN |
### Tassi di convergenza
| Metodo | Convesso f | Fortemente convesso f |
|--------|----------|-------------|
| Discesa gradiente | O(1/k) | O((1−μ/L)ᵏ) (lineare) |
| SGD | O(1/√k) | O(1/k) |
| GD accelerato (Nesterov) | O(1/k²) | O((1−√(μ/L))ᵏ) |
dove k = conteggio delle iterazioni, μ = parametro di forte convessità, L = costante di Lipschitz.
### Scelta del tasso di apprendimento
| Strategia | Descrizione |
|----------|-------------|
| Fisso α | Semplice ma può divergere (troppo grande) o convergere lentamente (troppo piccolo) |
| Ricerca riga | Trovare α che minimizzi f(x − α∇f(x)) lungo la direzione del gradiente |
| Orari di decadimento | α_t = α₀ / (1 + βt) oppure α_t = α₀ · βᵗ |
| Riscaldamento | Inizia in piccolo, aumenta, poi decade (comune nell'addestramento dei trasformatori) |
| Adattivo (Adamo) | Tassi di apprendimento per parametro basati sulle statistiche del gradiente |
---

## Ottimizzazione vincolata
### Moltiplicatori di Lagrange
Per il problema: minimizzare f(x) soggetto a h(x) = 0.
**Lagrangiana:** L(x, λ) = f(x) + λh(x)
All'ottimale: ∇ₓL = 0 e ∇_λL = 0 (che dà h(x) = 0).
**Esempio svolto:** Minimizza f(x,y) = x² + y² soggetto a x + y = 1.
- L = x² + y² + λ(x + y − 1)
- ∂L/∂x = 2x + λ = 0 → x = −λ/2
- ∂L/∂y = 2y + λ = 0 → y = −λ/2
- Vincolo: x + y = 1 → −λ = 1 → λ = −1
- Soluzione: x = 1/2, y = 1/2, f = 1/2
### Condizioni KKT
Le **condizioni di Karush-Kuhn-Tucker (KKT)** generalizzano i moltiplicatori di Lagrange a vincoli di disuguaglianza.
Per: minimizzare f(x) soggetto a gᵢ(x) ≤ 0, hⱼ(x) = 0.
**Lagrangiana:** L(x, λ, ν) = f(x) + Σᵢ λᵢgᵢ(x) + Σⱼ νⱼhⱼ(x)
**Condizioni KKT** (necessarie per l'ottimalità):
| Condizione | Equazione |
|-----------|----------|
| Stazionarietà | ∇ₓL = 0 |
| Fattibilità primaria | gᵢ(x) ≤ 0, hⱼ(x) = 0 |
| Doppia fattibilità | λᵢ ≥ 0 |
| Rilassamento complementare | λᵢgᵢ(x) = 0 per ogni i |
**Lasco complementare** significa: se il vincolo gᵢ non è attivo (gᵢ(x) < 0), allora λᵢ = 0 (il vincolo non influenza la soluzione).
Per i problemi convessi che soddisfano la condizione di Slater, le condizioni KKT sono sia necessarie che sufficienti.
---

## Dualità
Ad ogni problema di ottimizzazione (il **primale**) è associato un problema **duale**.
### Dualità debole e forte
| Concetto | Dichiarazione |
|---------|-----------|
| **Doppia funzione** | g(λ, ν) = infₓ L(x, λ, ν) |
| **Doppio problema** | Massimizzare g(λ, ν) soggetto a λ ≥ 0 |
| **Dualità debole** | Ottimo duale ≤ Ottimo primale (vale sempre) |
| **Forte dualità** | Ottimo duale = Ottimo primordiale (vale per problemi convessi con la condizione di Slater) |
| **Gap di dualità** | Ottimo primale − Ottimo duale (zero sotto dualità forte) |
### Perché la dualità è importante
| Applicazione | Come aiuta la dualità |
|-------------|-------------|
| Limiti inferiori | Dual fornisce un certificato di quanto sia buona la soluzione primaria |
| SVM | Il duale del problema SVM porta al trucco del kernel |
| Analisi di sensibilità | Le variabili duali misurano quanto cambia l'ottimo se i vincoli vengono allentati |
| Decomposizione | I problemi più grandi possono essere suddivisi in sottoproblemi più piccoli tramite il doppio |
---

## Programmazione con numeri interi
Quando alcune o tutte le variabili devono essere **intere**, il problema diventa molto più difficile (NP-difficile in generale).
### Tipi
| Digitare | Descrizione |
|------|-------------|
| IP puro | Tutte le variabili devono essere numeri interi |
| IP misto (MIP) | Alcune variabili sono intere, altre continue |
| IP binario | Variabili limitate a {0, 1} |
### Metodi di soluzione
| Metodo | Idea |
|--------|------|
| **Ramo e limite** | Suddividere in sottoproblemi, risolvere i rilassamenti LP, potare |
| **Aerei da taglio** | Aggiungere vincoli lineari per rafforzare il rilassamento LP |
| **Ramo e taglio** | Combina branch-and-bound con piani di taglio |
| **Euristica** | Ricerca avida e locale, ricottura simulata per soluzioni approssimate |
---

## Metodi euristici e metaeuristici
Quando l'ottimizzazione esatta è difficile, le euristiche trovano soluzioni buone (non necessariamente ottimali).
| Metodo | Idea chiave | Ideale per |
|--------|----------|----------|
| **Discesa gradiente** | Seguire la discesa più ripida | Funzioni uniformi e differenziabili |
| **Metodo di Newton** | Utilizza informazioni del secondo ordine (curvatura) | Problemi lisci e ben condizionati |
| **Ricottura simulata** | Accettare soluzioni peggiori con probabilità decrescente | Ottimizzazione globale, combinatoria |
| **Algoritmi genetici** | Evolvere una popolazione utilizzando selezione, crossover, mutazione | Multi-obiettivo, non differenziabile |
| **Sciame di particelle** | Gli agenti esplorano lo spazio, influenzati dalle posizioni più note | Continuo, non convesso |
| **Ottimizzazione bayesiana** | Costruisci un modello surrogato, usa la funzione di acquisizione | Funzioni costose della scatola nera (ottimizzazione degli iperparametri) |
### Metodo di ottimizzazione di Newton
**Regola di aggiornamento:** x_{k+1} = x_k − [H(x_k)]⁻¹ ∇f(x_k)
dove H è la matrice Hessiana (matrice delle derivate seconde).
| Immobile | Valore |
|----------|-------|
| Tasso di convergenza | Quadratico (quasi ottimale) |
| Costo per iterazione | O(n³) per l'inversione dell'Assia |
| Richiede | Due volte differenziabile, Hessiano definito positivo |
| Quasi-Newton (BFGS) | Assia approssimativo dai gradienti | O(n²) per iterazione |
---

## Rilevanza per l'apprendimento automatico e la scienza dei dati
| Concetto di ottimizzazione | Applicazione |
|---------------------|-------------|
| Discesa gradiente | Training di reti neurali, regressione logistica, qualsiasi modello differenziabile |
| SGD e varianti | ML su larga scala (formazione mini-batch), apprendimento online |
| Adamo, RMSprop | Ottimizzatori predefiniti per il deep learning |
| Ottimizzazione convessa | SVM, regressione logistica, LASSO, Ridge (ottimo globale garantito) |
| Moltiplicatori di Lagrange | Apprendimento vincolato, ML equo, allocazione delle risorse |
| Condizioni KKT | Derivazione della SVM duale, comprensione dell'attività dei vincoli |
| Dualità | Trucco del kernel SVM, analisi di sensibilità, metodi di scomposizione |
| Programmazione lineare | Allocazione delle risorse, ottimizzazione del portafoglio, flusso di rete |
| Programmazione intera | Selezione di caratteristiche (binario), scheduling, problemi combinatori |
| Ottimizzazione bayesiana | Ottimizzazione degli iperparametri (Optuna, Hyperopt) |
| Newton/quasi-Newton | Metodi del secondo ordine per problemi medio-piccoli (L-BFGS) |
---

## Riepilogo
| Metodo | Tipo di problema | Garanzie | Scala |
|--------|-----|------------|-------|
| Semplice | Programmazione lineare | Ottimo esatto | Milioni di variabili |
| Punto interno | Convesso (LP, QP, SOCP) | Ottimo esatto | Su larga scala |
| Discesa gradiente | Liscio non vincolato | Converge al min locale | Molto grande (apprendimento profondo) |
| SGD | Rischio empirico su larga scala | Converge (con decadimento) | Enormi set di dati |
| Newton/BFGS | Liscio, due volte differenziabile | Convergenza quadratica | Piccole e medie |
| KKT/Lagrange | Vincolato (convesso) | Esatto alle condizioni | Medio |
| Ramo e legato | Programmazione intera | Ottimo esatto | Piccole e medie |
| Euristica | Qualsiasi (non convesso, combinatorio) | Nessuna garanzia | Varia |
L’ottimizzazione è probabilmente lo strumento matematico più importante nell’apprendimento automatico. Ogni modello che addestri, dalla regressione lineare ai modelli linguistici di grandi dimensioni, implica la risoluzione di un problema di ottimizzazione. Comprendere quando un problema è convesso (ottimo globale garantito), quando la discesa del gradiente converge e come gestire i vincoli fornisce le basi teoriche per progettare, eseguire il debug e migliorare gli algoritmi di apprendimento.