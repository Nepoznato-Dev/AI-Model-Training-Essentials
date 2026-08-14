---
# Metadata
title: "Operations Research"
description: "Linear programming formulations, transportation and assignment problems, network flow optimization, integer programming, dynamic programming, queueing theory, inventory models, and scheduling"
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
    changes: "Initial deep-dive into operations research"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [operations-research, linear-programming, transportation-problem, dynamic-programming, queueing-theory, inventory-models, scheduling, network-flow]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "graph_theory.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Ricerca operativa
La ricerca operativa (OR) è l'applicazione di metodi matematici al processo decisionale. Nato durante la seconda guerra mondiale per la logistica militare, ora ottimizza le catene di approvvigionamento, pianifica le compagnie aeree, instrada le flotte di consegna, gestisce gli inventari e alloca le risorse in ogni settore. OR fornisce gli strumenti matematici per prendere le migliori decisioni possibili in presenza di vincoli.
---

## Formulazioni di programmazione lineare
### Modulo standard
Ridurre al minimo il cᵀx
Subject to: Ax = b, x ≥ 0
### Formulazioni LP comuni
**Mix di prodotti:**
- Variabili decisionali: xⱼ = quantità di prodotto j da produrre
- Obiettivo: massimizzare il profitto Σ pⱼxⱼ
- Vincoli: limiti delle risorse Σ aᵢⱼxⱼ ≤ bᵢ
**Problema di dieta:**
- Variabili decisionali: xⱼ = quantità di cibo j da acquistare
- Obiettivo: minimizzare il costo Σ cⱼxⱼ
- Vincoli: fabbisogni nutrizionali Σ nᵢⱼxⱼ ≥ rᵢ
**Problema di fusione:**
- Variabili decisionali: xⱼ = proporzione dell'ingrediente j nella miscela
- Obiettivo: minimizzare i costi
- Vincoli: requisiti di qualità (indice di ottano, resistenza, ecc.)
### Esempio svolto: pianificazione della produzione
Una fabbrica produce i prodotti A e B.
- A richiede 2 ore di manodopera, 1 kg di materiale; profitto $ 30
- B richiede 1 ora di manodopera, 3 kg di materiale; profitto $ 40
- Disponibili: 40 ore di manodopera, 30 kg di materiale
**Formulazione:**
- Massimizza: 30x_A + 40x_B
- Soggetto a: 2x_A + x_B ≤ 40 (manodopera)
- x_A + 3x_B ≤ 30 (materiale)
- x_A, x_B ≥ 0
**Soluzione:** Vertici della regione ammissibile: (0,0), (20,0), (18,4), (0,10)
- (0,0): profitto = 0
- (20,0): profitto = 600
- (18,4): profitto = 700 ← ottimale
- (0,10): profitto = 400
---

## Problema dei trasporti
Spostare merci da m fonti a n destinazioni al costo minimo.
### Formulazione
- Variabili decisionali: xᵢⱼ = quantità spedita dalla sorgente i alla destinazione j
- Obiettivo: ridurre al minimo Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Soggetto a: Σⱼ xᵢⱼ = sᵢ (vincoli di fornitura)
- Σᵢ xᵢⱼ = dⱼ (vincoli di domanda)
- xᵢⱼ ≥ 0
### Metodi di soluzione
| Metodo | Descrizione | Qualità della soluzione iniziale |
|--------|-------------|---------------------|
| **Angolo nord-ovest** | Inizia in alto a sinistra, assegna avidamente | Fattibile ma spesso scadente |
| **Approssimazione di Vogel** | Considerare i costi di penalità | Soluzione iniziale migliore |
| **MODI / Trampolino di lancio** | Migliorare la soluzione iniziale in modo iterativo | Trova ottimale |
### Esempio realizzato
| | D1 | D2 | D3 | Fornitura |
|---|----|----|----|--------|
| S1 | 2| 3| 1| 50|
| S2 | 4| 1| 5| 30|
| S3 | 3| 2| 4| 20|
| Domanda | 40| 30| 30| 100|
---

## Problema di assegnazione
Assegnazione di n lavoratori a n lavori (uno a uno) per ridurre al minimo il costo totale.
### Formulazione
- Variabili decisionali: xᵢⱼ ∈ {0, 1} (1 se il lavoratore i è assegnato al lavoro j)
- Minimizza: Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Soggetto a: Σⱼ xᵢⱼ = 1 (ogni lavoratore ottiene un lavoro)
- Σᵢ xᵢⱼ = 1 (ogni lavoro ottiene un lavoratore)
### Algoritmo ungherese
| Immobile | Valore |
|----------|-------|
| Complessità temporale | O(n³) |
| Ottimale? | Sì |
| Avvicinamento | Riduzione matrice + copertura minima |
**Passaggi:**
1. Sottrarre i minimi di riga da ciascuna riga
2. Sottrarre i minimi di colonna da ciascuna colonna
3. Copri tutti gli zeri con il numero minimo di righe
4. Se linee = n, assegnazione ottima trovata tra zeri
5. Altrimenti, regolare la matrice e ripetere
---

## Ottimizzazione del flusso di rete
### Flusso di costo minimo
Data una rete con capacità e costi ai margini, trovare il flusso che soddisfa le richieste al costo minimo.
**Formulazione:**
- Minimizzare: Σ cᵢⱼxᵢⱼ
- Soggetto a: conservazione del flusso in ciascun nodo
- Vincoli di capacità: 0 ≤ xᵢⱼ ≤ uᵢⱼ
### Percorso più breve come flusso di rete
Il problema del percorso più breve è un caso speciale di flusso di costo minimo (inviare 1 unità da s a t).
### Applicazioni
| Applicazione | Modello di rete |
|-------------|------|
| Filiera | Nodi = magazzini, bordi = rotte di spedizione |
| Comunicazione | Nodi = router, bordi = collegamenti con larghezza di banda |
| Traffico | Nodi = intersezioni, bordi = strade con capacità |
| Gestione del progetto | Reti CPM/PERT |
---

## Programmazione dinamica
**La programmazione dinamica (DP)** risolve problemi complessi suddividendoli in sottoproblemi sovrapposti.
### Principio di ottimalità di Bellman
Una politica ottimale ha la proprietà che qualunque sia lo stato e la decisione iniziale, le restanti decisioni devono costituire una politica ottimale per lo stato risultante.
### Elementi chiave
| Elemento | Descrizione |
|---------|-----|
| **Palco** | Punto decisionale (fase temporale, indice delle voci) |
| **Stato** | Informazioni necessarie per prendere una decisione |
| **Decisione** | Scelta fatta in ogni fase |
| **Ricorrenza** | Valore ottimale allo stadio n in termini di stadio n−1 |
### Problemi DP classici
| Problema | Ricorrenza | Complessità |
|---------|-----------|------------|
| **Fibonacci** | F(n) = F(n−1) + F(n−2) | O(n) con memorizzazione |
| **Zaino** | V(i,w) = max(V(i−1,w), vᵢ + V(i−1,w−wᵢ)) | O(nW) |
| **Percorso più breve** | d(i) = min_j(d(j) + cⱼᵢ) | O(V²) o O(E log V) |
| **Modifica distanza** | D(i,j) = min(D(i−1,j)+1, D(i,j−1)+1, D(i−1,j−1)+costo) | O(mn) |
| **Sottosequenza comune più lunga** | L(i,j) = L(i−1,j−1)+1 se corrisponde, altrimenti max(L(i−1,j), L(i,j−1)) | O(mn) |
| **Moltiplicazione di catene di matrici** | M(i,j) = min_k(M(i,k) + M(k+1,j) + pᵢ₋₁pₖpⱼ) | O(n³) |
### Esempio realizzato: Zaino 0/1
Elementi: {peso: valore} = {(2, 12), (3, 10), (4, 8), (5, 11)}. Capacità W = 7.
V(i, w) = valore massimo utilizzando i primi i elementi con capacità w
| io\w | 0| 1| 2| 3| 4| 5| 6| 7|
|-----|---|---|---|---|---|---|---|---|
| 0| 0| 0| 0| 0| 0| 0| 0| 0|
| 1| 0| 0| 12| 12| 12| 12| 12| 12|
| 2| 0| 0| 12| 12| 12| 22| 22| 22|
| 3| 0| 0| 12| 12| 12| 22| 22| 22|
| 4| 0| 0| 12| 12| 12| 22| 23| 23|
Ottimale: V(4, 7) = 23 (elementi 1 e 4: peso 2+5=7, valore 12+11=23).
---

## Teoria delle code
La teoria delle code studia le file di attesa: quanto sono lunghe, quanto tempo aspetti e come ridurle entrambe.
### Notazione di Kendall
A/B/c/K/N/D dove:
- A = processo di arrivo (M = Markoviano/Poisson, D = deterministico, G = generale)
- B = processo di servizio (stesse opzioni)
- c = numero di server
- K = capacità (default ∞)
- N = popolazione (default ∞)
- D = disciplina (FIFO, LIFO, Priorità)
### Coda M/M/1 (server singolo)
| Metrico | Formula |
|--------|---------|
| Utilizzo | ρ = λ/μ |
| Numero medio nel sistema | L = ρ/(1−ρ) |
| Tempo medio nel sistema | W = 1/(μ−λ) |
| Numero medio in coda | L_q = ρ²/(1−ρ) |
| Tempo medio di attesa | W_q = ρ/(μ−λ) |
dove λ = tasso di arrivo, μ = tasso di servizio, ρ = utilizzo.
### Coda M/M/c (server multipli)
| Metrico | Formula |
|--------|---------|
| Utilizzo | ρ = λ/(cμ) |
| Probabilità di attesa (Erlang C) | P_w = formula complessa che coinvolge ρ e c |
| Lunghezza media della coda | L_q = P_w · ρ/(1−ρ) |
### Legge di Little
L = λW (numero medio nel sistema = tasso di arrivo × tempo medio)
Ciò vale per QUALSIASI sistema di code, indipendentemente dalla distribuzione degli arrivi/servizi.
### Esempi di applicazioni
| Scenario | Modello coda |
|----------|-------------|
| Call center | M/M/c (agenti c) |
| Richieste del server Web | M/M/1 o M/G/1 |
| Emergenza ospedaliera | M/G/c con priorità |
| Linea di produzione | Rete di code |
| Pianificazione della CPU del computer | Condivisione processore M/M/1 |
---

## Modelli di inventario
### Quantità economica dell'ordine (EOQ)
La quantità di ordine ottimale che riduce al minimo i costi di inventario totali.
Q* = √(2DS/H)
| Variabile | Significato |
|----------|---------|
| D | Domanda annua |
| S | Costo dell'ordine per ordine |
| H | Costo di mantenimento per unità all'anno |
| D* | Quantità ottimale dell'ordine |
**Costo totale a Q*:** TC = √(2DSH)
### Estensioni
| Modello | Estensione |
|-------|-----------|
| **EOQ con sconti** | Gli sconti sulla quantità modificano la funzione di costo |
| **Quantità dell'ordine di produzione** | Articoli prodotti gradualmente, non consegnati tutti in una volta |
| **modello (s, Q)** | Riordina le unità Q quando l'inventario scende al livello s |
| **modello (s, S)** | Ordina fino a S quando l'inventario scende a s |
| **Modello giornalaio** | Domanda incerta e monoperiodale |
### Modello del giornalaio
Quantità di ordine ottimale per inventario deperibile di un singolo periodo:
P(D ≤ Q*) = c_u / (c_u + c_o)
dove c_u = costo in eccesso (perdita di profitto) e c_o = costo in eccesso (spreco).
---

## Pianificazione
### Programmazione del Job Shop
| Notazione | Significato |
|----------|---------|
| n/m/J/C_max | n posti di lavoro, m macchine, job shop, minimizza makespan |
| Negozio di flusso | Tutti i lavori visitano le macchine nello stesso ordine |
| Negozio di lavoro | Ogni lavoro ha la propria sequenza macchina |
| Negozio aperto | Nessun vincolo di ordinazione |
### Regole di priorità
| Regola | Descrizione | Effetto |
|------|-------------|--------|
| FCFS | Primo arrivato, primo servito | Giusto, ma non ottimale |
| SPT | Prima il tempo di elaborazione più breve | Riduce al minimo il completamento medio |
| EDD | Prima data di scadenza prima | Riduce al minimo il ritardo massimo |
| CR | Rapporto critico (scadenza residua/tempo di lavorazione) | Equilibrato |
| LPT | Prima il tempo di elaborazione più lungo | Buono per makespan su macchine parallele |
### Algoritmo di Johnson (flusso di lavoro a 2 macchine)
Per n lavori su 2 macchine, riducendo al minimo il makespan:
1. Trova il lavoro con il tempo di elaborazione più breve
2. Se è sulla macchina 1, pianificalo prima; se sulla macchina 2, pianificalo per ultimo
3. Rimuovi quel lavoro e ripeti
Ottimale per 2 macchine; NP-hard per 3+ macchine.
---

## Rilevanza per l'apprendimento automatico e la scienza dei dati
| O concetto | Applicazione |
|-----------|-------------|
| Programmazione lineare | Allocazione delle risorse, ottimizzazione del portafoglio, allocazione del budget pubblicitario |
| Trasporto/incarico | Logistica, abbinamento ride-sharing, assegnazione compiti |
| Flusso di rete | Ottimizzazione della supply chain, instradamento del traffico dei data center |
| Programmazione dinamica | Allineamento di sequenze (bioinformatica), algoritmo di Viterbi (HMM), RL (equazione di Bellman) |
| Teoria delle code | Pianificazione della capacità del server, modellazione della latenza, allocazione delle risorse cloud |
| Modelli di inventario | Integrazione della previsione della domanda, supply chain ML |
| Pianificazione | Orchestrazione della pipeline ML, pianificazione dei processi GPU, pianificazione della ricerca degli iperparametri |
| Programmazione intera | Selezione delle funzionalità (binario), selezione del modello, progettazione della rete |
---

## Riepilogo
| Argomento | Problema fondamentale | Metodo chiave |
|-------|-------------|------------|
| Formulazioni LP | Ottimizza l'obiettivo lineare con vincoli | Simplesso, punto interno |
| Trasporti | Spedire merci al costo minimo | MODI, trampolino di lancio |
| Compito | Abbina i lavoratori ai posti di lavoro | Algoritmo ungherese |
| Flusso di rete | Flusso del percorso attraverso una rete | Algoritmi di flusso a costo minimo |
| Programmazione dinamica | Sottoproblemi sovrapposti | Principio di Bellman, memorizzazione |
| Teoria delle code | Analisi della linea di attesa | M/M/1, Legge di Little |
| Inventario | Quando e quanto ordinare | EOQ, giornalaio |
| Pianificazione | Lavori in sequenza su macchine | Regole di priorità, algoritmo di Johnson |
La ricerca operativa trasforma il processo decisionale dall’arte alla scienza. Formulando matematicamente i problemi del mondo reale, OR fornisce soluzioni dimostrabilmente ottimali (o quasi ottimali) a problemi di logistica, pianificazione, allocazione delle risorse e pianificazione che interessano ogni settore. Per i data scientist, i metodi OR completano l’apprendimento automatico: mentre il machine learning prevede, l’OR prescrive e, insieme, costituiscono la base di sistemi decisionali intelligenti.