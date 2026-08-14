---
# Metadata
title: "Numerical Methods"
description: "Floating-point arithmetic, root finding, numerical integration, ODE solvers, interpolation, numerical stability, and conditioning"
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
    changes: "Initial deep-dive into numerical methods"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [numerical-methods, floating-point, root-finding, numerical-integration, ode-solvers, interpolation, stability]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Metodi numerici
I metodi numerici sono il ponte tra la teoria matematica e il calcolo pratico. Mentre la matematica pura dimostra che esistono soluzioni, i metodi numerici in realtà calcolano risposte approssimative con precisione finita. Ogni modello di machine learning, simulazione fisica e pipeline di analisi dei dati si basa in definitiva sul calcolo numerico. Comprendere questi metodi, la loro accuratezza, stabilità e limitazioni, è essenziale per creare software affidabile.
---

## Aritmetica in virgola mobile
I computer rappresentano i numeri reali con precisione finita. Lo **standard IEEE 754** definisce il modo in cui i numeri a virgola mobile vengono archiviati e manipolati.
### Formati IEEE 754
| Formato | Bit | Esponente | Mantissa | Cifre decimali approssimative | Gamma |
|--------|------|----------|----------|---------------------|-------|
| Metà (fp16) | 16| 5| 10| 3.3 | ±6,5×10⁴ |
| Singolo (fp32) | 32| 8| 23| 7.2 | ±3,4×10³⁸ |
| Doppio (fp64) | 64| 11| 52| 15.9| ±1,8 × 10³⁰⁸ |
### Macchina Epsilon
**Epsilon macchina** (ε_mach) è il numero più piccolo tale che 1 + ε_mach > 1 in virgola mobile.
| Formato | ε_mach |
|--------|--------|
| fp16 | 2⁻¹⁰ ≈ 9,8 × 10⁻⁴ |
| fp32 | 2⁻²³ ≈ 1,2 × 10⁻⁷ |
| fp64 | 2⁻⁵² ≈ 2,2 × 10⁻¹⁶ |
### Insidie ​​​​comuni
| Trappola | Esempio | Conseguenza |
|---------|---------|-----|
| **Cancellazione catastrofica** | Calcolo (1 + x) − 1 per x piccolo | Perdita di cifre significative |
| **Assorbimento** | 10⁸ + 1 = 10⁸ in fp32 | Piccoli valori persi in grandi somme |
| **Non associatività** | (a + b) + c ≠ a + (b + c) | L'ordine della somma è importante |
| **Divisione per quasi zero** | 1 / 10⁻³⁰⁰ → troppopieno | Infinito o NaN |
### Strategie di mitigazione
| Strategia | Descrizione |
|----------|-------------|
| **Somma Kahan** | Somma compensata per ridurre l'errore di assorbimento |
| **Kahan-Babuska-Neumaier** | Versione migliorata della sommatoria di Kahan |
| **Somma ordinata** | Somma prima i numeri piccoli per evitare l'assorbimento |
| **Aritmetica doppia-doppia** | Utilizza coppie di doppie per una precisione estesa |
| **Analisi condizionata** | Capire se il problema stesso amplifica gli errori |
---

## Ricerca della radice
Trovare x tale che f(x) = 0.
### Metodo della bisezione
| Immobile | Valore |
|----------|-------|
| Richiede | f continua, f(a) ef(b) hanno segni opposti |
| Convergenza | Lineare (l'errore dimezza ogni passaggio) |
| Garantito? | Sì, converge sempre |
| Iterazioni per d cifre | ≈ d / log₁₀(2) ≈ 3,32d |
**Algoritmo:**
1. Inizia con l'intervallo [a, b] dove f(a) · f(b) < 0
2. Calcola il punto medio c = (a + b) / 2
3. Se f(c) = 0 oppure |b − a| < tolleranza, stop
4. Se f(a) · f(c) < 0, poni b = c; altrimenti imposta a = c
5. Ripeti
### Metodo di Newton-Raphson
| Immobile | Valore |
|----------|-------|
| Richiede | f differenziabile, f'(x) ≠ 0 alla radice |
| Convergenza | Quadratico (vicino alla radice) |
| Garantito? | No, può divergere o ciclare |
| Aggiorna regola | x_{n+1} = x_n − f(x_n) / f'(x_n) |
**Esempio svolto:** Trova √2 risolvendo f(x) = x² − 2 = 0.
- f'(x) = 2x
- x₀ = 1,5
- x₁ = 1,5 − (2,25 − 2) / 3 = 1,5 − 0,0833 = 1,4167
- x₂ = 1,4167 − (2,0069 − 2) / 2,8333 = 1,4142
- x₃ = 1.41421356... (corretto a 8 cifre decimali)
### Metodo delle secanti
Come il metodo di Newton ma approssima la derivata:
x_{n+1} = x_n − f(x_n) · (x_n − x_{n-1}) / (f(x_n) − f(x_{n-1}))
| Immobile | Valore |
|----------|-------|
| Convergenza | Superlineare (ordine ≈ 1.618, la sezione aurea) |
| Richiede | Due ipotesi iniziali (non è necessaria la derivata) |
### Confronto dei metodi di ricerca delle radici
| Metodo | Convergenza | Necessario un derivato? | Garantito? | Costo per passaggio |
|--------|-------------|-------------|-------------|---------------|
| Bisezione | Lineare (1) | No | Sì | 1 funzione valutazione |
| Newton-Raphson | Quadratico (2) | Sì | No | 2 valutazioni di funzione |
| Secante | Superlineare (1.618) | No | No | 1 funzione valutazione |
| Metodo di Brent | Superlineare | No | Sì | Varia |
**Il metodo di Brent** combina la bisezione (convergenza garantita) con l'interpolazione quadratica secante/inversa (convergenza rapida). È il root-finder predefinito nella maggior parte delle librerie numeriche.
---

## Integrazione numerica (quadratura)
Calcolare ∫ₐᵇ f(x) dx approssimativamente.
### Metodi
| Metodo | Formula | Errore | Ordina |
|--------|---------|-------|-------|
| **Rettangolo (punto medio)** | (b−a) · f((a+b)/2) | O(h²) | 1|
| **Trapezoidale** | (b−a)/2 · [f(a) + f(b)] | O(h²) | 2|
| **Simpson 1/3** | (b−a)/6 · [f(a) + 4f(m) + f(b)] | O(h⁴) | 3|
| **Simpson 3/8** | Utilizza 4 punti equidistanti | O(h⁴) | 4|
| **Quadratura gaussiana** | Posizionamento ottimale del nodo | O(h²ⁿ) | n punti |
### Regole composite
Per n sottointervalli di larghezza h = (b−a)/n:
| Regola | Formula composita | Errore |
|------|-----|-------|
| Trapezoidale composito | h[f(a)/2 + Σf(xᵢ) + f(b)/2] | O(h²) |
| Simpson composito | h/3[f(a) + 4Σf(dispari) + 2Σf(pari) + f(b)] | O(h⁴) |
**Esempio elaborato:** Approssimazione ∫₀¹ e^(−x²) dx utilizzando un trapezio composito con n = 4.
- h = 0,25, punti: 0, 0,25, 0,5, 0,75, 1
- f(0) = 1, f(0,25) = 0,9394, f(0,5) = 0,7788, f(0,75) = 0,5698, f(1) = 0,3679
- T = 0,25[1/2 + 0,9394 + 0,7788 + 0,5698 + 0,3679/2] = 0,25[1/2 + 2,2880 + 0,1840] = 0,7430
- Valore vero: ≈ 0,7468 (errore ≈ 0,5%)
### Quadratura adattiva
Suddivide automaticamente gli intervalli in cui la funzione varia rapidamente, utilizzando meno punti in cui è fluida. Questo è ciò che utilizza`scipy.integrate.quad`(basato su QUADPACK).
---

## Interpolazione
Stima dei valori tra punti dati noti.
### Metodi
| Metodo | Descrizione | Levigatezza | Oscillazione |
|--------|-----|------------|-----|
| **Il vicino più vicino** | Utilizza il punto dati più vicino | Discontinuo | Nessuno |
| **Lineare** | Unisci i punti con linee rette | C⁰ (continuo) | Nessuno |
| **Polinomio (Lagrange)** | Polinomio singolo passante per tutti i punti | C^∞ | Grave in molti punti (fenomeno di Runge) |
| **Spline cubica** | Cubico a tratti, liscio alle giunture | C² | Minimo |
| **Funzione base radiale** | Somma ponderata dei nuclei radiali | Dipende dal kernel | Basso |
### Interpolazione di Lagrange
Dati n+1 punti (x₀, y₀), ..., (xₙ, yₙ), l'unico polinomio di grado ≤ n passante per tutti i punti:
P(x) = Σᵢ₌₀ⁿ yᵢ · Πⱼ≠ᵢ (x − xⱼ) / (xᵢ − xⱼ)
**Fenomeno di Runge:** L'interpolazione polinomiale di alto grado in punti equidistanti può oscillare notevolmente vicino ai bordi. Mitigato utilizzando nodi o spline di Chebyshev.
### Spline cubiche
Polinomi cubici a tratti che sono C² continui (derivate seconde continue).
| Digitare | Condizione al contorno |
|------|-----|
| Spline naturale | S''(x₀) = S''(xₙ) = 0 |
| Spline bloccata | S'(x₀) e S'(xₙ) specificati |
| Non-un-nodo | Derivata terza continua in x₁ e xₙ₋₁ |
---

## Risolutori ODE
Risoluzione numerica delle equazioni differenziali ordinarie dy/dt = f(t, y).
### Metodo di Eulero
Il risolutore ODE più semplice.
**Aggiornamento:** y_{n+1} = y_n + h · f(t_n, y_n)
| Immobile | Valore |
|----------|-------|
| Ordina | 1 (errore per passo: O(h²), globale: O(h)) |
| Stabilità | Condizionalmente stabile (è richiesta una piccola h) |
| Costo | 1 valutazione funzionale per passo |
### Metodi Runge-Kutta
| Metodo | Ordina | Fasi | Note |
|--------|-------|--------|-------|
| **Eulero** | 1| 1| Più semplice |
| **Punto medio** | 2| 2| Migliore precisione |
| **Heun (RK2)** | 2| 2| Predittore-correttore |
| **RK4 classica** | 4| 4| Cavallo di battaglia standard |
| **Dormand-Prince (RK45)** | 4(5) | 6| Dimensione del passo adattivo (utilizzato in ode45) |
### RK4 classico (Runge-Kutta di 4° ordine)
k₁ = f(t_n, y_n)
k₂ = f(t_n + h/2, y_n + hk₁/2)
k₃ = f(t_n + h/2, y_n + hk₂/2)
k₄ = f(t_n + h, y_n + hk₃)
y_{n+1} = y_n + h(k₁ + 2k₂ + 2k₃ + k₄) / 6
| Immobile | Valore |
|----------|-------|
| Ordina | 4 (errore globale: O(h⁴)) |
| Costo | 4 valutazioni funzionali per fase |
| Stabilità | Molto meglio di Eulero |
| Utilizzo | Predefinito per ODE non rigide |
### ODE rigide
Un'ODE **rigida** ha componenti che variano su scale temporali molto diverse. I metodi espliciti (Eulero, RK4) richiedono dimensioni del passo impraticabilmente piccole.
| Metodo | Digitare | Stabilità |
|--------|------|-----------|
| Eulero implicito | Implicito | A-stabile (incondizionatamente stabile) |
| Formula di differenziazione all'indietro (BDF) | Implicito | A-stabile (fino all'ordine 5) |
| Runge-Kutta implicito | Implicito | Esistono varianti L-stabili |
| LSODA | Automatico | Passa da rigido/non rigido |
---

## Stabilità e condizionamento numerico
### Numero condizione
Il **numero di condizione** misura quanto cambia l'output di un problema rispetto a piccoli cambiamenti nell'input.
Per un sistema lineare Ax = b: κ(A) = ||A|| · ||A⁻¹||
| κ(A) | Interpretazione |
|-------|---------------|
| ≈ 1 | Ben condizionato |
| 10³| Leggermente sensibile |
| 10⁸ | Mal condizionato (perde ~8 cifre di precisione) |
| → ∞ | Singolare (nessuna soluzione unica) |
### Stabilità degli algoritmi
Un algoritmo è **numericamente stabile** se piccole perturbazioni nell'input portano a piccole perturbazioni nell'output (rispetto al numero di condizione del problema).
| Algoritmo | Stabile? | Note |
|-----------|---------|-------|
| Eliminazione gaussiana con pivoting parziale | Sì | Approccio standard |
| Calcolo degli autovalori tramite QR | Sì | Stabile all'indietro |
| Somma ingenua (prima grande + piccola) | No | Utilizzare la somma di Kahan |
| Calcolare la varianza come E[X²] − (E[X])² | Potenzialmente no | Utilizza l'algoritmo online di Welford |
### Algoritmo online di Welford
Calcolo numericamente stabile della media corrente e della varianza:
```
mean_new = mean_old + (x − mean_old) / n
M2_new = M2_old + (x − mean_old)(x − mean_new)
variance = M2 / (n − 1)
```

Ciò evita la catastrofica cancellazione che si verifica nell’ingenua formula a due passaggi.
---

## Rilevanza per l'apprendimento automatico e la scienza dei dati
| Metodo Numerico | Applicazione |
|-----------------|-------------|
| Virgola mobile (fp16/fp32/bf16) | Addestramento a precisione mista, quantizzazione del modello, efficienza della memoria |
| Ricerca della radice | Stima di massima verosimiglianza (trovare dove gradiente = 0) |
| Integrazione numerica | Inferenza bayesiana (calcolo delle verosimiglianze marginali), valori attesi |
| Interpolazione | Smoothing, imputazione, modelli surrogati, funzioni di attivazione |
| Risolutori ODE | ODE neurali, RNN a tempo continuo, dinamica delle popolazioni, ML basato sulla fisica |
| Numero di condizione | Comprensione dei problemi numerici nella regressione lineare, equazioni normali |
| Somma stabile | Calcolo delle funzioni di perdita, statistiche di normalizzazione batch |
| RK4 / solutori adattivi | Simulazione di sistemi dinamici, addestramento di reti a profondità continua |
---

## Riepilogo
| Argomento | Idea fondamentale | Metodo chiave |
|-------|-----------|------------|
| Virgola mobile | Rappresentazione a precisione finita | IEEE 754, sommatoria di Kahan |
| Ricerca della radice | Risolvi f(x) = 0 | Bisezione, Newton-Raphson, Brent |
| Integrazione numerica | Approssimato ∫f(x)dx | Quadratura trapezoidale, di Simpson, gaussiana |
| Interpolazione | Stima tra punti dati | Spline cubiche, Lagrange, RBF |
| Risolutori ODE | Risolvi dy/dt = f(t,y) | Eulero, RK4, metodi adattivi |
| Stabilità | Sensibilità agli errori di arrotondamento | Numero di condizione, algoritmi stabili |
I metodi numerici sono il luogo in cui la matematica incontra la realtà. Nessun computer può rappresentare esattamente la maggior parte dei numeri reali, nella pratica nessuna derivata viene calcolata simbolicamente e nessun integrale viene valutato in forma chiusa per i problemi del mondo reale. Comprendere i metodi numerici ti consente di scegliere l'algoritmo giusto, prevederne l'accuratezza ed evitare i sottili bug che derivano dall'aritmetica a precisione finita.