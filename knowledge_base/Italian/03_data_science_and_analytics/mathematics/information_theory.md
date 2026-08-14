---
# Metadata
title: "Information Theory"
description: "Shannon entropy, differential entropy, joint and mutual information, KL divergence, cross-entropy, channel capacity, source coding, compression, and connections to machine learning loss functions"
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
    changes: "Initial deep-dive into information theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [information-theory, entropy, kl-divergence, cross-entropy, mutual-information, channel-capacity, compression, machine-learning]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Teoria dell'informazione
La teoria dell’informazione, fondata da Claude Shannon nel 1948, quantifica l’informazione stessa. Quanto ti dice un messaggio? Quanto puoi comprimere i dati? Quanto velocemente puoi comunicare su un canale rumoroso? Queste domande hanno risposte matematiche precise. Al di là della comunicazione, la teoria dell’informazione è diventata fondamentale per l’apprendimento automatico: l’entropia incrociata è la funzione di perdita predefinita per la classificazione, la divergenza KL misura la somiglianza della distribuzione e le informazioni reciproche guidano la selezione delle caratteristiche.
---

## Entropia
L'**Entropia** misura l'incertezza media o la "sorpresa" di una variabile casuale.
### Entropia di Shannon (discreta)
Per una variabile casuale discreta X con funzione di massa di probabilità p(x):
H(X) = −Σₓ p(x) log₂ p(x)
Unità: **bit** (quando si utilizza log₂) o **nats** (quando si utilizza ln).
| Distribuzione | Entropia | Intuizione |
|-------------|---------|-----------|
| Moneta equa (p = 0,5, 0,5) | 1 po' | Massima incertezza per il risultato binario |
| Moneta distorta (p = 0,9, 0,1) | 0,469 bit | Meno sorprendente: per lo più teste |
| Deterministico (p = 1, 0) | 0 bit | Nessuna incertezza |
| Dado giusto (6 facce) | 2.585 bit | Più risultati = più incertezza |
| Uniforme su n risultati | log₂(n) bit | Entropia massima per n risultati |
### Proprietà dell'Entropia
| Immobile | Dichiarazione |
|----------|-----------|
| Non negatività | H(X) ≥ 0 |
| Massimo | H(X) ≤ log₂(\|X\|) con uguaglianza per distribuzione uniforme |
| Regola della catena | H(X, Y) = H(X) + H(Y \| X) |
| Il condizionamento riduce | H(X \| Y) ≤ H(X) |
| Concavità | H è una funzione concava della distribuzione di probabilità |
### Entropia differenziale (continua)
Per una variabile casuale continua X con densità p(x):
h(X) = −∫ p(x) log p(x) dx
A differenza dell'entropia discreta, l'entropia differenziale può essere **negativa**.
| Distribuzione | Entropia differenziale |
|-------------|---------------------|
| Uniforme su [a,b] | log(b − a) |
| Normale N(μ, σ²) | (1/2) log(2πeσ²) |
| Esponenziale(λ) | 1 − ln(λ) |
---

## Informazioni congiunte, condizionali e reciproche
### Entropia congiunta
H(X, Y) = −Σₓ Σᵧ p(x, y) log p(x, y)
Misura l'incertezza totale della coppia (X, Y).
### Entropia condizionale
H(Y | X) = −Σₓ Σᵧ p(x, y) log p(y | x) = H(X, Y) − H(X)
Misura l’incertezza rimanente su Y dopo aver osservato X.
### Informazioni reciproche
I(X; Y) = Σₓ Σᵧ p(x, y) log [p(x, y) / (p(x)p(y))]
Misura quanto la conoscenza di X ti dice di Y (e viceversa).
| Immobile | Dichiarazione |
|----------|-----------|
| Non negatività | I(X; Y) ≥ 0 |
| Simmetria | I(X; Y) = I(Y; X) |
| Relazione con l'entropia | I(X; Y) = H(X) − H(X \| Y) = H(Y) − H(Y \| X) |
| Relazione con il giunto | I(X; Y) = H(X) + H(Y) − H(X, Y) |
| Indipendenza | I(X; Y) = 0 se e solo se X e Y sono indipendenti |
| Autoinformazione | I(X; X) = H(X) |
### Immagine: il diagramma dell'entropia
```
┌─────────────────────────────────────────┐
│            H(X, Y)                      │
│  ┌──────────────┐  ┌──────────────┐    │
│  │   H(X|Y)     │  │   H(Y|X)     │    │
│  │              │I │              │    │
│  │              │( │              │    │
│  │   H(X)−I    │X │   H(Y)−I    │    │
│  │              │; │              │    │
│  │              │Y │              │    │
│  └──────────────┘  └──────────────┘    │
│         H(X)              H(Y)          │
└─────────────────────────────────────────┘
```

---

## KL Divergenza
La **divergenza di Kullback-Leibler (KL)** misura la differenza tra una distribuzione e un'altra.
D_KL(P || Q) = Σₓ P(x) log [P(x) / Q(x)]
| Immobile | Dichiarazione |
|----------|-----------|
| Non negatività | D_KL(P \|\| Q) ≥ 0 (disuguaglianza di Gibbs) |
| Identità | D_KL(P \|\| Q) = 0 se e solo se P = Q |
| Asimmetria | D_KL(P \|\| Q) ≠ D_KL(Q \|\| P) in generale |
| Non una metrica | Fallisce la simmetria e la disuguaglianza triangolare |
**Interpretazione:** D_KL(P || Q) è il numero aggiuntivo di bit necessari per codificare i dati da P utilizzando un codice ottimizzato per Q.
### Relazione con altre quantità
| Relazione | Formula |
|-------------|---------|
| Entropia incrociata | H(P, Q) = H(P) + D_KL(P \|\| Q) |
| Informazioni reciproche | I(X; Y) = D_KL(P(X,Y) \|\| P(X)P(Y)) |
| KL condizionale | D_KL(P(Y\|X) \|\| Q(Y\|X)) media su X |
---

## Entropia incrociata
**Entropia incrociata** tra le distribuzioni P e Q:
H(P, Q) = −Σₓ P(x) log Q(x) = H(P) + D_KL(P || Q)
### Entropia incrociata come funzione di perdita
Nella classificazione, P è la distribuzione reale (etichetta codificata one-hot) e Q è la distribuzione prevista dal modello.
**Entropia incrociata binaria (BCE):**
L = −[y log(ŷ) + (1−y) log(1−ŷ)]
**Entropia incrociata categoriale:**
L = −Σᵢ yᵢ log(ŷᵢ)
| Scenario | y (vero) | ŷ (previsto) | Perdita |
|----------|----------|---------------|------|
| Corretto, fiducioso | 1| 0,95| 0,051 |
| Corretto, incerto | 1| 0,55| 0,598 |
| Sbagliato, fiducioso | 1| 0,05 | 2.996|
| Sbagliato, incerto | 1| 0,45| 0,799 |
Minimizzare l’entropia incrociata equivale a minimizzare la divergenza KL dalla distribuzione reale, motivo per cui funziona così bene come funzione di perdita.
---

## Capacità del canale
### Modello del canale di comunicazione
```
X → [Channel] → Y
```

- X: variabile casuale di input
- Y: variabile casuale di output
- Canale: definito dalle probabilità condizionali p(y|x)
### Teorema della codifica dei canali rumorosi di Shannon
Per un canale con capacità C, se la velocità di trasmissione R< C, there exists a coding scheme that achieves arbitrarily small error probability. If R >C, una comunicazione affidabile è impossibile.
**Capacità del canale:**
C = max_{p(x)} I(X; Y)
### Esempi di canali importanti
| Canale | Descrizione | Capacità |
|---------|-------------|----------|
| **Binario simmetrico (BSC)** | Capovolge ogni bit con probabilità p | 1 − H(p) bit |
| **Cancellazione binaria (BEC)** | Cancella ogni bit con probabilità ε | 1 − ε bit |
| **Gaussiano (AWGN)** | Y = X + Z, Z ~ N(0, σ²) | (1/2)log(1 + SNR) bit |
| **Binario silenzioso** | Trasmissione perfetta | 1 po' |
---

## Codifica e compressione sorgente
### Teorema della codifica sorgente
Il numero medio di bit necessari per codificare una sorgente è delimitato di seguito dalla sua entropia:
L ≥ H(X)
Un codice ottimo raggiunge L ≈ H(X).
### Codifica Huffman
Un codice **senza prefisso** che assegna codici più brevi a simboli più probabili.
| Simbolo | Probabilità | Codice Huffman | Lunghezza |
|--------|-----|-----|--------|
| A | 0,5 | 0| 1|
| B | 0,25| 10| 2|
| C| 0,125| 110| 3|
| D | 0,125| 111| 3|
Lunghezza media: 0,5(1) + 0,25(2) + 0,125(3) + 0,125(3) = 1,75 bit/simbolo
Entropia: H = 1,75 bit/simbolo (ottimale in questo caso!)
### Compressione senza perdita o con perdita
| Digitare | Principio | Esempi | Limite |
|------|-----------|----------|-------|
| **Senza perdite** | Rimuovere la ridondanza statistica | ZIP, PNG, FLAC | Tasso di entropia H(X) |
| **Perdita** | Rimuovere le informazioni percettivamente irrilevanti | JPEG, MP3, H.264 | Funzione di distorsione della velocità R(D) |
**Teoria della distorsione della velocità:** per una compressione con perdita con distorsione massima D, la velocità minima è R(D) = min I(X; X̂) soggetto a E[d(X, X̂)] ≤ D.
---

## Collegamenti ad altri campi
### Teoria dell'informazione e termodinamica
| Concetto | Teoria dell'informazione | Termodinamica |
|---------|-----|----------------|
| Entropia | Entropia di Shannon H(X) | Entropia di Boltzmann S = k_B ln W |
| Entropia massima | Distribuzione uniforme | Equilibrio termico |
| Divergenza KL | Differenza di distribuzione | Differenza di energia libera |
| Informazioni reciproche | Informazioni condivise | Correlazioni nei sistemi fisici |
Le forme matematiche sono identiche: Shannon ha deliberatamente preso in prestito il termine "entropia" dalla meccanica statistica.
### Teoria e statistica dell'informazione
| Concetto | Applicazione |
|---------|-----|
| Massima probabilità | Equivalente a ridurre al minimo la divergenza KL dalla distribuzione empirica a quella del modello |
| Informazioni Fisher | Curvatura della divergenza KL; limite inferiore della varianza dello stimatore (Cramér-Rao) |
| Lunghezza minima della descrizione (MDL) | Selezione del modello riducendo al minimo la lunghezza totale della codifica |
| AIC/BIC | Criteri approssimativi di selezione del modello basato su KL |
---

## Rilevanza per l'apprendimento automatico e la scienza dei dati
| Concetto IT | Applicazione ML |
|-----------|----------------|
| Perdita di entropia incrociata | Perdita di classificazione per default (binaria e multiclasse) |
| Divergenza KL | Perdita VAE (termine di regolarizzazione), abbinamento della distribuzione, distillazione |
| Informazioni reciproche | Selezione delle caratteristiche (MIFS), apprendimento della rappresentazione (InfoMax), districamento |
| Entropia | Criterio di suddivisione dell'albero decisionale (guadagno di informazioni), esplorazione in RL (massima entropia RL) |
| Capacità del canale | Complessità della comunicazione, comprensione dei limiti della generalizzazione |
| Codifica sorgente | Compressione dei dati per l'archiviazione e la trasmissione, codifica efficiente |
| Entropia massima | Classificatori MaxEnt, selezione preventiva nell'inferenza bayesiana |
| Distorsione della velocità | Comprensione dei compromessi nella compressione con perdita e quantizzazione nelle reti neurali |
| Informazioni Fisher | Discesa del gradiente naturale, comprensione della sensibilità dei parametri |
| MDL/AIC/BIC | Selezione del modello, prevenzione del sovradattamento |
---

## Riepilogo
| Quantità | Formula (discreta) | Significato |
|----------|-------------|---------|
| Entropia H(X) | −Σ p(x) log p(x) | Incertezza media |
| Entropia congiunta H(X,Y) | −Σ p(x,y) log p(x,y) | Incertezza totale della coppia |
| Entropia condizionata H(Y\|X) | H(X,Y) − H(X) | Incertezza rimanente su Y dato X |
| Informazione reciproca I(X;Y) | H(X) − H(X\|Y) | Informazioni condivise tra X e Y |
| Divergenza KL D_KL(P\|\|Q) | Σ P(x) log(P(x)/Q(x)) | "Distanza" tra le distribuzioni |
| Entropia incrociata H(P,Q) | −Σ P(x) log Q(x) | Codifica del costo utilizzando una distribuzione errata |
| Capacità del canale C | massimo I(X;Y) | Massima velocità di comunicazione affidabile |
La teoria dell’informazione fornisce i limiti fondamentali di ciò che può essere appreso, compresso e comunicato. Per i professionisti dell’apprendimento automatico, spiega perché l’entropia incrociata funziona come una funzione di perdita, come misurare la qualità delle rappresentazioni apprese e come pensare al compromesso tra complessità del modello e adattamento dei dati. Le intuizioni di Shannon del 1948 rimangono rilevanti tanto per l'intelligenza artificiale moderna quanto lo sono per le telecomunicazioni.