<!--
---
# Metadata
title: "Quantum Mechanics"
description: "Wave-particle duality, Schrodinger equation, operators and observables, uncertainty principle, quantum states and superposition, entanglement, qubits, quantum gates, and relevance to quantum computing"
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
    changes: "Initial deep-dive into quantum mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [quantum-mechanics, schrodinger-equation, uncertainty-principle, superposition, entanglement, qubits, quantum-gates, quantum-computing]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "abstract_algebra.md"
  - "classical_mechanics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Meccanica Quantistica
La meccanica quantistica è la teoria della fisica su scala più piccola: atomi, elettroni, fotoni e le particelle fondamentali della natura. Sostituisce il mondo deterministico della meccanica classica con probabilità, sovrapposizioni ed entanglement. Nonostante la sua natura controintuitiva, la meccanica quantistica è la teoria testata più precisamente in tutta la scienza. Oggi i suoi principi stanno diventando direttamente rilevanti per l’informatica attraverso i computer quantistici, che promettono di risolvere determinati problemi in modo esponenziale più veloce rispetto alle macchine classiche.
---

## Motivazione storica
### Fallimenti della fisica classica
| Problema | Previsione classica | Osservazione | Risoluzione |
|---------|----------------------|-----|------------|
| Radiazione del corpo nero | Catastrofe ultravioletta (energia infinita a λ breve) | Lunghezza d'onda di picco finita | Planck: l'energia è quantizzata (E = nhν) |
| Effetto fotoelettrico | KE dipende dall'intensità, non dalla frequenza | KE dipende dalla frequenza | Einstein: la luce è quantizzata (fotoni, E = hν) |
| Spettri atomici | Spettro di emissione continua | Righe spettrali discrete | Bohr: gli elettroni occupano orbite quantizzate |
| Diffrazione elettronica | Le particelle non diffrangono | Gli elettroni producono schemi di interferenza | de Broglie: le particelle hanno lunghezza d'onda λ = h/p |
### Costanti chiave
| Costante | Simbolo | Valore |
|----------|--------|-------|
| Costante di Planck | h | 6.626 × 10⁻³⁴ J·s |
| Costante di Planck ridotta | ℏ = h/2π | 1.055 × 10⁻³⁴ J·s |
| Velocità della luce | c | 3,0 × 10⁸ m/s |
| Massa dell'elettrone | io_e | 9.109 × 10⁻³¹ kg |
| Tassa elementare | e| 1.602 × 10⁻¹⁹ C |
| Raggio di Bohr | a₀ | 5.292 × 10⁻¹¹ m |
---

## Dualità onda-particella
### Lunghezza d'onda di Broglie
Ad ogni particella con quantità di moto p è associata una lunghezza d'onda:
λ = h/p = h/(mv)
| Particella | Tipico λ | Comportamento delle onde osservabili? |
|----------|-----------|---------------------|
| Elettrone (100 eV) | 0,12 nm | Sì (diffrazione dei cristalli) |
| Protone | 0,003 nm| Sì (scattering di neutroni) |
| Baseball (40 m/s) | 10⁻³⁴m | No (troppo piccolo per essere rilevato) |
### Esperimento della doppia fenditura
L'esperimento quantistico per eccellenza:
1. Sparare le particelle (elettroni, fotoni) una alla volta in due fenditure
2. Ciascuna particella atterra in un singolo punto del rilevatore
3. Nel corso del tempo emerge uno schema di interferenza, come se ciascuna particella passasse attraverso entrambe le fenditure contemporaneamente
4. Se si misura la fenditura attraverso la quale passa la particella, la figura di interferenza scompare
**Conclusione:** Gli oggetti quantistici non sono né puramente particelle né puramente onde. Esibiscono un comportamento ondulatorio quando non osservati e un comportamento particellare quando misurati.
---

## La funzione d'onda
### Definizione
La **funzione d'onda** ψ(x, t) descrive completamente un sistema quantistico. È una funzione a valori complessi il cui modulo quadrato fornisce la densità di probabilità:
P(x) = |ψ(x)|² = ψ*(x)ψ(x)
### Normalizzazione
La probabilità totale deve essere uguale a 1:
∫ |ψ(x)|² dx = 1 (su tutto lo spazio)
### Regola nata
La probabilità di trovare la particella tra x e x + dx:
P(x÷x+dx) = |ψ(x)|² dx
Per un osservabile generale con autostati φₙ:
P(autovalore di misura aₙ) = |⟨φₙ|ψ⟩|²
---

## L'equazione di Schròdinger
### Equazione di Schrodinger dipendente dal tempo
iℏ ∂ψ/∂t = Ĥψ
dove Ĥ è l'**operatore hamiltoniano** (operatore dell'energia totale).
### Equazione di Schrodinger indipendente dal tempo
Per gli stati stazionari (autostati energetici):
Ĥψ = Eψ
Questa è un'equazione agli autovalori: le energie consentite E sono gli autovalori di Ĥ.
### Particella in una scatola (pozzo quadrato infinito)
Il sistema quantistico più semplice: particella confinata in 0 < x < L.
| Quantità | Risultato |
|----------|--------|
| Funzioni d'onda | ψₙ(x) = √(2/L) sin(nπx/L) |
| Livelli energetici | Eₙ = n²π²ℏ²/(2 ml²) = n²h²/(8 ml²) |
| Stato fondamentale | n = 1, E₁ = h²/(8 ml²) |
| Energia di punto zero | E₁ > 0 (la particella non può essere perfettamente ferma) |
| Numero quantico | n = 1, 2, 3, ... (solo numeri interi positivi) |
### Oscillatore armonico quantistico
V(x) = ½mω²x²
| Quantità | Risultato |
|----------|--------|
| Livelli energetici | Eₙ = (n + ½)ℏω |
| Energia di punto zero | Mi₀ = ½ℏω |
| Spaziatura | ΔE = ℏω (uniforme) |
| Funzioni d'onda | Polinomi di Hermite × gaussiano |
---

## Operatori e osservabili
Nella meccanica quantistica, ogni osservabile fisico corrisponde a un **operatore hermitiano**.
### Operatori chiave
| Osservabile | Operatore (spazio delle posizioni) | Autovalori |
|-----------|--------------------|-------------|
| Posizione | x̂ = x | Tutto reale x |
| Slancio | p̂ = −iℏ ∂/∂x | Tutto vero p |
| Energia (Hamiltoniano) | Ĥ = −(ℏ²/2m)∂²/∂x² + V(x) | Eₙ (discreto per stati legati) |
| Momento angolare | L̂ = r × p̂ | ℏ√(l(l+1)) |
| Girare | Ŝ = (ℏ/2)σ (matrici di Pauli) | ±ℏ/2 (per rotazione ½) |
### Valori attesi
Il risultato medio della misurazione dell’osservabile A sullo stato ψ:
⟨A⟩ = ⟨ψ|Â|ψ⟩ = ∫ ψ*(x) Â ψ(x) dx
### Relazioni di commutazione
[Â, B̂] = ÂB̂ − B̂Â
| Commutatore | Risultato | Significato |
|-----------|--------|-----|
| [x̂, p̂] | ioℏ | Posizione e slancio sono incompatibili |
| [L̂ₓ, L̂ᵧ] | iℏL̂_z | Le componenti del momento angolare sono incompatibili |
| [σ̂ₓ, σ̂ᵧ] | 2iσ̂_z | Matrici di Pauli (componenti di spin) |
Se [Â, B̂] = 0, le osservabili possono essere misurate simultaneamente (condividono gli autostati).
---

## Principio di incertezza
### Principio di indeterminazione di Heisenberg
Δx · Δp ≥ ℏ/2
Più in generale, per due osservabili A e B qualsiasi:
ΔA · ΔB ≥ (1/2)|⟨[Â, B̂]⟩|
### Relazioni di incertezza
| Coppia | Relazione | Interpretazione |
|------|----------|----------------|
| Posizione-momento | ΔxΔp ≥ ℏ/2 | Non è possibile conoscerli entrambi con precisione |
| Energia-tempo | ΔEΔt ≥ ℏ/2 | Gli stati di breve durata hanno un’energia incerta |
| Momento angolare | ΔLₓΔLᵧ ≥ (ℏ/2)\|⟨L_z⟩\| | Impossibile conoscere tutti i componenti contemporaneamente |
**Importante:** l'incertezza non riguarda i disturbi di misurazione: è una proprietà fondamentale degli stati quantistici. Una particella non ha contemporaneamente una posizione e una quantità di moto definite.
---

## Stati quantistici e sovrapposizione
### Notazione Dirac (Bra-Ket)
| Simbolo | Nome | Significato |
|--------|------|---------|
| \|ψ⟩ | Ket | Vettore di stato (vettore di colonna) |
| ⟨ψ\| | Reggiseno | Trasposizione coniugata (vettore riga) |
| ⟨φ\|ψ⟩ | Prodotto interno | Ampiezza di ψ da trovare nello stato φ |
| \|ψ\|² | Norma al quadrato | Probabilità |
### Principio di sovrapposizione
Se \|ψ₁⟩ e \|ψ₂⟩ sono stati quantistici validi, allora è valida anche qualsiasi combinazione lineare:
\|ψ⟩ = α\|ψ₁⟩ + β\|ψ₂⟩

dove |α|² + |β|² = 1 (normalizzazione).
**Misurazione:** Una volta misurato, il sistema "collassa" in \|ψ₁⟩ con probabilità |α|² o \|ψ₂⟩ con probabilità |β|².
### Qubit
Un **qubit** è un bit quantistico: un sistema quantistico a due livelli.
\|ψ⟩ = α\|0⟩ + β\|1⟩, dove |α|² + |β|² = 1
| Rappresentanza | \|0⟩ | \|1⟩ |
|------||------|------|
| Girare | Gira su ↑ | Spingi giù ↓ |
| Polarizzazione dei fotoni | Orizzontale | Verticale |
| Livello energetico | Stato fondamentale | Stato eccitato |
| Circuito | \|0⟩ = [1, 0]ᵀ | \|1⟩ = [0, 1]ᵀ |
**Sfera di Bloch:** Qualsiasi stato di qubit può essere scritto come:
\|ψ⟩ = cos(θ/2)\|0⟩ + e^{iφ} sin(θ/2)\|1⟩
dove θ ∈ [0, π] e φ ∈ [0, 2π). Lo spazio degli stati è una sfera.
---

## Intreccio
Due qubit sono **entangled** quando il loro stato congiunto non può essere scritto come prodotto di stati individuali.
### Stati di campana (massimamente impigliati)
| Stato | Espressione | Nome |
|-------|-----------|------|
| \|Φ⁺⟩ | (1/√2)(\|00⟩ + \|11⟩) | Stato campana |
| \|Φ⁻⟩ | (1/√2)(\|00⟩ − \|11⟩) | Stato campana |
| \|Ψ⁺⟩ | (1/√2)(\|01⟩ + \|10⟩) | Stato campana |
| \|Ψ⁻⟩ | (1/√2)(\|01⟩ − \|10⟩) | Stato di singoletto |
### Proprietà dell'entanglement
| Immobile | Descrizione |
|----------|-------------|
| Correlazione | La misurazione di un qubit determina istantaneamente l'altro, indipendentemente dalla distanza |
| Nessuna comunicazione | Non è possibile utilizzare l'entanglement da solo per inviare informazioni più velocemente della luce |
| Monogamia | Se A è massimamente invischiato con B, non può essere invischiato con C|
| Fragilità | L'interazione con l'ambiente distrugge l'entanglement (decoerenza) |
### Paradosso EPR e teorema di Bell
Einstein, Podolsky e Rosen sostenevano che la meccanica quantistica deve essere incompleta (variabili nascoste). Bell ha dimostrato che qualsiasi teoria locale delle variabili nascoste soddisfa determinate disuguaglianze. Gli esperimenti violano le disuguaglianze di Bell, confermando la meccanica quantistica ed escludendo variabili nascoste locali.
---

## Porte Quantistiche
Le porte quantistiche sono operazioni unitarie sui qubit.
### Porte a Qubit singolo
| Cancello | Matrice | Effetto |
|------|--------|--------|
| **Pauli-X** (NON) | [[0,1],[1,0]] | Inversione di bit: \|0⟩ ↔ \|1⟩ |
| **Pauli-Y** | [[0,−i],[i,0]] | Bit + inversione di fase |
| **Pauli-Z** | [[1,0],[0,−1]] | Inversione di fase: \|1⟩ → −\|1⟩ |
| **Hadamard** (H) | (1/√2)[[1,1],[1,−1]] | Crea una sovrapposizione: \|0⟩ → (\|0⟩+\|1⟩)/√2 |
| **Fase** (S) | [[1,0],[0,i]] | Rotazione π/2 attorno a Z |
| **Porta a T** | [[1,0],[0,e^{iπ/4}]] | rotazione π/4 attorno a Z |
| **Rotazione** Rₓ(θ) | cos(θ/2)I − i sin(θ/2)σₓ | Rotazione di θ attorno all'asse X |
### Porte a due Qubit
| Cancello | Descrizione | Effetto |
|------|-------------|--------|
| **CNO** | Non controllato | Capovolge il bersaglio se il controllo è \|1⟩ |
| **CZ** | Controllato-Z | Applica Z al target se il controllo è \|1⟩ |
| **Scambia** | Scambia qubit | \|ab⟩ → \|ba⟩ |
### Creare intrecci
Applica H al qubit 1, quindi CNOT con qubit 1 come controllo:
\|00⟩ → (H⊗I)\|00⟩ → CNOT → (1/√2)(\|00⟩ + \|11⟩) = \|Φ⁺⟩
---

## Algoritmi quantistici
| Algoritmo | Accelera | Applicazione |
|-----------|---------|-----|
| **Shor's** | Esponenziale (fattorizzazione) | Interrompe la crittografia RSA |
| **Grover** | Quadratico (cerca) | Ricerca non strutturata in O(√N) |
| **VQE** | Euristica | Trovare le energie dello stato fondamentale (chimica, materiali) |
| **QAOA** | Euristica | Ottimizzazione combinatoria |
| **HHL** | Esponenziale (sotto condizioni) | Risoluzione di sistemi lineari |
| **Simulazione quantistica** | Esponenziale | Simulare sistemi quantistici (motivazione originale di Feynman) |
---

## Rilevanza per l'apprendimento automatico e la scienza dei dati
| Concetto quantistico | Applicazione |
|----------------|-------------|
| Qubit e sovrapposizione | Apprendimento automatico quantistico, campionamento quantistico |
| Intreccio | Comunicazione quantistica, distribuzione delle chiavi quantistiche (QKD) |
| Porte quantistiche | Progettazione di circuiti quantistici per subroutine ML |
| Algoritmo di Grover | Accelerazione quadratica per l'ottimizzazione basata sulla ricerca |
| Algoritmo di Shor | Minaccia alla crittografia attuale; motiva la crittografia post-quantistica |
| Simulazione quantistica | Scoperta di farmaci, scienza dei materiali, simulazione chimica |
| Algoritmi variazionali (VQE, QAOA) | ML quantistico a breve termine su dispositivi NISQ |
| Regola nata | Risultati probabilistici analoghi al campionamento da distribuzioni |
| Prodotti tensori | Sistemi multi-qubit (spazio degli stati esponenziale: stessi calcoli dell'algebra multilineare in ML) |
| Matrici unitarie | Analoghi quantistici delle trasformazioni ortogonali |
---

## Riepilogo
| Concetto | Idea fondamentale | Equazione chiave |
|---------|-----------|-----|
| Dualità onda-particella | La materia ha proprietà ondulatorie | λ = h/p |
| Funzione d'onda | Descrizione completa dello stato quantistico | P(x) = \|ψ(x)\|² |
| Equazione di Schròdinger | Come si evolvono gli stati quantistici | iℏ ∂ψ/∂t = Ĥψ |
| Operatori | Le osservabili sono operatori hermitiani | ⟨A⟩ = ⟨ψ\|Â\|ψ⟩ |
| Incertezza | Limiti fondamentali alla conoscenza simultanea | ΔxΔp ≥ ℏ/2 |
| Sovrapposizione | È possibile aggiungere stati | \|ψ⟩ = α\|0⟩ + β\|1⟩ |
| Intreccio | Stati comuni non separabili | \|Φ⁺⟩ = (\|00⟩ + \|11⟩)/√2 |
| Porte quantistiche | Operazioni unitarie sui qubit | Set di cancelli H, CNOT e universali |
La meccanica quantistica sfida le nostre intuizioni più profonde sulla realtà: particelle che sono onde, oggetti in due posti contemporaneamente, correlazioni che sfidano la spiegazione classica. Eppure la sua matematica è precisa e le sue previsioni non hanno eguali in termini di accuratezza. Per i data scientist, la meccanica quantistica sta diventando direttamente rilevante attraverso l’informatica quantistica, che promette di trasformare l’ottimizzazione, la crittografia, la simulazione e potenzialmente lo stesso apprendimento automatico.