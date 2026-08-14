<!--
---
# Metadata
title: "Classical Mechanics"
description: "Newton's laws, free-body diagrams, work-energy theorem, conservation laws, Lagrangian mechanics, Hamiltonian mechanics, rigid body dynamics, and orbital mechanics"
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
    changes: "Initial deep-dive into classical mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [classical-mechanics, newton, lagrangian, hamiltonian, conservation-laws, orbital-mechanics, rigid-body]
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

-->
# Meccanica Classica
La meccanica classica descrive il movimento degli oggetti sotto l'influenza di forze. Dalle mele che cadono ai pianeti in orbita, dalle corde vibranti alle particelle in collisione, i suoi principi governano il mondo macroscopico. Al di là delle sue applicazioni fisiche, la meccanica classica ha dato vita al calcolo delle variazioni, alla geometria simplettica e alla struttura hamiltoniana che è alla base della meccanica quantistica e dell’ottimizzazione moderna.
---

## Meccanica newtoniana
### Le tre leggi di Newton
| Legge | Dichiarazione | Forma matematica |
|-----|-----------|-------------|
| **Prima (Inerzia)** | Un oggetto rimane fermo o in moto uniforme a meno che non subisca l'azione di una forza | Se F_net = 0, allora v = costante |
| **Secondo (F = ma)** | La forza è uguale alla massa per l'accelerazione | **F** = m**a** = m(d²**x**/dt²) |
| **Terzo (Azione-Reazione)** | Ad ogni azione corrisponde una reazione uguale e contraria | **F**₁₂ = −**F**₂₁ |
### Diagrammi di corpo libero
Un **diagramma di corpo libero** isola un oggetto e mostra tutte le forze che agiscono su di esso.
**Forze comuni:**
| Forza | Formula | Direzione |
|-------|---------|-----------|
| Gravità (vicino alla Terra) | F =mg| Verso il basso |
| Forza normale | N | Perpendicolare alla superficie |
| Attrito (statico) | f_s ≤ μ_s N | Si oppone al movimento imminente |
| Attrito (cinetico) | f_k = μ_k N | Si oppone al movimento |
| Primavera (legge di Hooke) | F = −kx | Ripristinare (verso l'equilibrio) |
| Tensione | T | Lungo la corda/corda |
| Trascina | F_d = ½C_dρAv² | Si oppone alla velocità |
### Esempio realizzato: Blocco in pendenza
Un blocco di massa m su un piano inclinato privo di attrito con angolo θ.
- Forze: gravità (mg verso il basso), forza normale (N perpendicolare alla superficie)
- Scomporre la gravità: mg sin θ (lungo il pendio), mg cos θ (in superficie)
- N = mg cos θ (nessun movimento perpendicolare alla superficie)
- Accelerazione lungo il pendio: a = g sin θ
---

## Metodi energetici
### Lavoro ed energia cinetica
**Lavoro** compiuto da una forza: W = ∫ **F** · d**r**
**Teorema Lavoro-Energia:** W_netto = ΔKE = ½mv₂² − ½mv₁²
### Energia potenziale
| Forza | Energia potenziale | Note |
|-------|-----------------|-------|
| Gravità (vicino alla superficie) | U = mgh | h = altezza sopra riferimento |
| Gravità (generale) | U = −GMm/r | Zero all'infinito |
| Primavera | U = ½kx² | x = spostamento dall'equilibrio |
| Elettrostatico | U = kq₁q₂/r | Carica simile: U positiva |
### Conservazione dell'energia
Se agiscono solo forze conservative: E = KE + PE = costante
½mv₁² + U₁ = ½mv₂² + U₂
**Esempio realizzato:** Una palla lasciata cadere da un'altezza h.
- Iniziale: KE = 0, PE = mgh
- Poco prima di toccare terra: KE = ½mv², PE = 0
- Conservazione: mgh = ½mv² → v = √(2gh)
### Energia
P = dW/dt = **F** · **v** (velocità di lavoro svolto)
---

## Slancio e collisioni
### Momento lineare
**p** = m**v**
Seconda legge di Newton (forma alternativa): **F** = d**p**/dt
### Conservazione della quantità di moto
In assenza di forze esterne: la quantità di moto totale si conserva.
| Tipo di collisione | KE Conservato? | Momento conservato? |
|---------------|---------------|---------------------|
| **Elastico** | Sì | Sì |
| **Anelastico** | No | Sì |
| **Perfettamente anelastico** | No (perdita massima) | Sì (gli oggetti restano attaccati) |
**Colpo elastico 1D:** Due masse m₁, m₂ con velocità iniziali u₁, u₂:
- v₁ = ((m₁−m₂)u₁ + 2m₂u₂) / (m₁+m₂)
- v₂ = ((m₂−m₁)u₂ + 2m₁u₁) / (m₁+m₂)
### Momento angolare
**L** = **r** × **p** = m(**r** × **v**)
Coppia: **τ** = d**L**/dt = **r** × **F**
**Conservazione:** In assenza di coppia esterna, il momento angolare si conserva.
---

## Meccanica Lagrangiana
La formulazione **Lagrangiana** sostituisce le forze con l'energia, fornendo un quadro più elegante e generale.
### La Lagrangiana
L = T − V (energia cinetica meno energia potenziale)
### Principio di minima azione (principio di Hamilton)
Il percorso effettivo intrapreso da un sistema tra i tempi t₁ e t₂ minimizza (più precisamente, rende stazionario) l’**azione**:
S = ∫_{t₁}^{t₂} L(q, q̇, t) dt
### Equazioni di Eulero-Lagrange
La condizione δS = 0 dà:
d/dt(∂L/∂q̇) − ∂L/∂q = 0
per ogni coordinata generalizzata q.
**Esempio lavorato:** Pendolo semplice (lunghezza l, massa m, angolo θ dalla verticale).
- T = ½ml²θ̇²
- V = −mgl cos θ
- L = ½ml²θ̇² + mgl cos θ
- ∂L/∂θ = −mgl sin θ
- ∂L/∂θ̇ = ml²θ̇ → d/dt(∂L/∂θ̇) = ml²θ̈
- Eulero-Lagrange: ml²θ̈ + mgl sin θ = 0 → θ̈ + (g/l) sin θ = 0
### Vantaggi della Meccanica Lagrangiana
| Vantaggio | Spiegazione |
|-----------|-------------|
| Indipendente dalle coordinate | Funziona con qualsiasi sistema di coordinate |
| Gestisce i vincoli in modo naturale | Non è necessario calcolare le forze vincolanti |
| Simmetria → conservazione | Il teorema di Noether collega le simmetrie alle quantità conservate |
| Si generalizza facilmente | Ai campi, alla relatività, alla meccanica quantistica |
---

## Meccanica Hamiltoniana
La formulazione **Hamiltoniana** è una riformulazione della meccanica lagrangiana che utilizza posizioni e momenti (invece di posizioni e velocità).
### L'Hamiltoniano
H = Σᵢ pᵢq̇ᵢ − L = T + V (per la maggior parte dei sistemi meccanici)
dove pᵢ = ∂L/∂q̇ᵢ sono i **momenti generalizzati**.
### Equazioni di Hamilton
q̇ᵢ = ∂H/∂pᵢ
ṗᵢ = −∂H/∂qᵢ
Queste sono 2n ODE del primo ordine (rispetto a n equazioni di Eulero-Lagrange del secondo ordine).
**Esempio svolto:** Oscillatore armonico (massa m, costante elastica k).
- H = p²/(2m) + ½kx²
- ẋ = ∂H/∂p = p/m → p = mẋ (come previsto)
- ṗ = −∂H/∂x = −kx → mẍ = −kx (Legge di Hooke)
### Parentesi di Poisson
Per le funzioni f(q, p) e g(q, p):
{f, g} = Σᵢ (∂f/∂qᵢ · ∂g/∂pᵢ − ∂f/∂pᵢ · ∂g/∂qᵢ)
| Immobile | Dichiarazione |
|----------|-----------|
| Evoluzione del tempo | df/dt = {f, H} + ∂f/∂t |
| Conservazione | f si conserva se e solo se {f, H} = 0 (e ∂f/∂t = 0) |
| Parentesi fondamentali | {qᵢ, pⱼ} = δᵢⱼ, {qᵢ, qⱼ} = 0, {pᵢ, pⱼ} = 0 |
**Collegamento alla meccanica quantistica:** Le parentesi di Poisson diventano commutatori: {f, g} → (1/iℏ)[f̂, ĝ]
---

## Leggi di conservazione e teorema di Noether
### Teorema di Noether
Ad ogni simmetria continua della Lagrangiana corrisponde una quantità conservata.
| Simmetria | Quantità conservata |
|----------|-------------|
| Invarianza di traslazione temporale | Energia |
| Invarianza di traslazione spaziale | Momento lineare |
| Invarianza rotazionale | Momento angolare |
| Invarianza di calibro | Carica elettrica |
Questo è uno dei risultati più profondi di tutta la fisica: collega la geometria dello spaziotempo alle leggi fondamentali di conservazione.
---

## Dinamica del corpo rigido
Un **corpo rigido** è un oggetto in cui tutte le distanze interne rimangono fisse.
### Concetti chiave
| Concetto | Formula | Descrizione |
|---------|---------|-----|
| **Momento di inerzia** | I = Σmᵢrᵢ² oppure I = ∫r² dm | Resistenza all'accelerazione rotazionale |
| **KE rotazionale** | KE = ½Iω² | Energia di rotazione |
| **Momento angolare** | L = Iω | Analogo rotazionale di p = mv |
| **Coppia** | τ = Iα | Analogo rotazionale di F = ma |
### Momenti di inerzia (forme comuni)
| Forma | Asse | Io |
|-------|------|---|
| Sfera solida | Attraverso il centro | (2/5)MR² |
| Sfera cava | Attraverso il centro | (2/3)MR² |
| Cilindro solido | Lungo l'asse | (1/2)MR² |
| Asta sottile | Attraverso il centro, perpendicolare | (1/12)ML² |
| Asta sottile | Attraverso l'estremità, perpendicolare | (1/3)ML² |
| Disco | Attraverso il centro, perpendicolare | (1/2)MR² |
---

## Meccanica orbitale
### Leggi di Keplero
| Legge | Dichiarazione |
|-----|-----------|
| **Prima (ellissi)** | I pianeti si muovono su ellissi con il Sole in un fuoco |
| **Secondo (Aree pari)** | Una linea che collega il Sole al pianeta percorre aree uguali in tempi uguali |
| **Terza (armonica)** | T² ∝ a³ (periodo al quadrato proporzionale al semiasse maggiore al cubo) |
### Energia orbitale
E = ½mv² − GMm/r
| E| Tipo di orbita |
|---|-----------|
| E< 0 | Elliptical (bound) |
| E = 0 | Parabolic (escape trajectory) |
| E >0 | Iperbolico (non legato) |
### Velocità di fuga
v_fuga = √(2GM/R)
Per la Terra: v_escape ≈ 11,2 km/s
---

## Rilevanza per l'apprendimento automatico e la scienza dei dati
| Concetto di meccanica | Applicazione |
|------------------|-------------|
| Le leggi di Newton | Motori fisici nelle simulazioni, intelligenza artificiale dei giochi, robotica |
| Metodi energetici | Modelli basati sull'energia, reti di Hopfield, macchine di Boltzmann |
| Meccanica lagrangiana | Reti neurali informate dalla fisica, controllo ottimale, ottimizzazione della traiettoria |
| Meccanica hamiltoniana | Reti neurali hamiltoniane (HNN), integratori simplettici per la simulazione |
| Leggi di conservazione | Bias induttivi nei modelli ML, reti neurali equivarianti |
| Teorema di Noether | Apprendimento automatico sensibile alla simmetria, apprendimento profondo geometrico |
| Dinamica del corpo rigido | Simulazione robotica, dinamica molecolare, animazione 3D |
| Meccanica orbitale | Posizionamento satellitare (GPS per ML basato sulla posizione), progettazione di missioni spaziali |
| Spazio delle fasi (Hamiltoniano) | Comprensione dei sistemi dinamici, reti di attrattori |
| Calcolo delle variazioni | Trasporto ottimale, modellazione generativa (flowmatching) |
---

## Riepilogo
| Quadro | Equazione fondamentale | Forza |
|-----------|--------------|----------|
| Newtoniano | **C** = m**a** | Analisi della forza intuitiva e diretta |
| Lagrangiana | d/dt(∂L/∂q̇) − ∂L/∂q = 0 | Senza coordinate, gestisce i vincoli |
| Hamiltoniano | q̇ = ∂H/∂p, ṗ = −∂H/∂q | Struttura simplettica, si collega a QM |
| Leggi di conservazione | Teorema di Noether | Connessione profonda di conservazione della simmetria |
La meccanica classica non riguarda solo palline che cadono e pendoli che oscillano. Le sue strutture matematiche – la meccanica lagrangiana e hamiltoniana – sono tra le idee più influenti in tutta la scienza. Si generalizzano alla meccanica quantistica, alla teoria dei campi e persino al moderno apprendimento automatico, dove i modelli basati sull’energia e le reti neurali informate sulla fisica attingono direttamente a queste formulazioni secolari.