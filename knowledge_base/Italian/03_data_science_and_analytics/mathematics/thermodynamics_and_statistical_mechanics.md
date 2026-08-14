---
# Metadata
title: "Thermodynamics and Statistical Mechanics"
description: "Laws of thermodynamics, entropy (thermodynamic and statistical), enthalpy, free energy, Carnot cycle, Boltzmann distribution, partition functions, and connections to information-theoretic entropy"
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
    changes: "Initial deep-dive into thermodynamics and statistical mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [thermodynamics, statistical-mechanics, entropy, enthalpy, free-energy, carnot-cycle, boltzmann, partition-function]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
  - "classical_mechanics.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Termodinamica e Meccanica Statistica
La termodinamica descrive il comportamento macroscopico dei sistemi in termini di temperatura, pressione ed entropia, senza sapere che aspetto hanno gli atomi. La meccanica statistica spiega la termodinamica dal basso verso l'alto: deriva le proprietà macroscopiche dal comportamento microscopico di un gran numero di particelle. Insieme, forniscono la comprensione più profonda di energia, entropia ed equilibrio, concetti che sono migrati nella teoria dell’informazione, nell’apprendimento automatico e oltre.
---

## Variabili termodinamiche e stato
### Variabili di stato
| Variabile | Digitare | Unità | Descrizione |
|----------|------|------|-----|
| Temperatura (T) | Intensivo | Kelvin (K) | Energia cinetica media per particella |
| Pressione (P) | Intensivo | Pascal (Pa) | Forza per unità di superficie |
| Volume (V) | Ampio | m³ | Spazio occupato |
| Energia interna (U) | Ampio | Joule (J) | Energia microscopica totale |
| Entropia (S) | Ampio | J/K | Misura del disordine/microstati |
| Numero di particelle (N) | Ampio | talpe o contare | Quantità di sostanza |
Le variabili **intensive** non dipendono dalle dimensioni del sistema; le variabili **estese** lo fanno.
### Equazione di Stato
Per un gas ideale: PV = nRT = Nk_BT
| Costante | Valore |
|----------|-------|
| R (costante dei gas) | 8.314 J/(mol·K) |
| k_B (costante di Boltzmann) | 1.381 × 10⁻²³ J/K |
| N_A (numero di Avogadro) | 6.022 × 10²³ /mol |
---

## Le leggi della termodinamica
### Legge Zero
Se A è in equilibrio termico con B e B con C, allora A è in equilibrio termico con C.
**Significato:** La temperatura è ben definita e misurabile.
### Prima Legge (Conservazione dell'Energia)
ΔU = Q - W
| Simbolo | Significato |
|--------|---------|
| ∆U | Cambiamento di energia interna |
| D | Calore aggiunto al sistema |
| W | Lavoro svolto dal sistema |
**Forma differenziale:** dU = δQ − δW = δQ − PdV
| Processo | Vincolo | Conseguenza |
|---------|-----------|-----|
| Isocoro | dV = 0 | W = 0, ΔU = Q |
| Isobarico | dP = 0 | W = PΔV |
| Isotermico | dT = 0 | ΔU = 0 (gas ideale), Q = W |
| Adiabatico | δQ = 0 | ∆U = −W |
### Seconda Legge (Entropia)
**Dichiarazione di Clausius:** Il calore non può fluire spontaneamente dal freddo al caldo.
**Dichiarazione Kelvin-Planck:** Nessun motore può convertire tutto il calore in lavoro.
**Dichiarazione di entropia:** Per qualsiasi processo: ΔS_universo ≥ 0
| Tipo di processo | ΔS_universo |
|-------------|-------------|
| Reversibile | = 0|
| Irreversibile (reale) | > 0|
**Variazione di entropia:** dS = δQ_rev / T
### Terza Legge
Poiché T → 0 K, l'entropia di un cristallo perfetto si avvicina allo zero: lim_{T→0} S = 0
**Significato:** Lo zero assoluto è irraggiungibile in passi finiti.
---

## Entropia in profondità
### Entropia termodinamica
S è una funzione di stato. Per un processo reversibile tra gli stati A e B:
ΔS = ∫_A^B δQ_giro / T
**Esempio svolto:** Variazione di entropia quando si riscalda l'acqua da T₁ a T₂ a pressione costante.
ΔS = ∫_{T₁}^{T₂} (mc_p/T) dT = mc_p ln(T₂/T₁)
### Entropia statistica (Boltzmann)
S = k_B lnΩ
dove Ω è il numero di microstati coerenti con il macrostato.
| Macrostato | Microstati (Ω) | Entropia |
|-----------|-----------------|---------|
| Tutto il gas in una metà della scatola | Piccolo | Basso |
| Gas distribuito uniformemente | Molto grande | Alto |
| Cristallo perfetto a 0 K | 1| 0|
**Connessione:** La seconda legge diventa statistica: i sistemi evolvono verso macrostati con più microstati semplicemente perché sono estremamente più probabili.
---

## Entalpia ed energia libera
### Entalpia
H = U + PV
Utile per processi a pressione costante (la maggior parte della chimica e della biologia).
ΔH = Q_p (calore a pressione costante)
### Energia libera di Helmholtz
F = U − TS
| Immobile | Dichiarazione |
|----------|-----------|
| Significato | Lavoro massimo estraibile a T, V costante |
| Equilibrio | Il sistema minimizza F a T costante, V |
| Relazione con la funzione di partizione | F = −k_BT ln Z |
### Energia libera di Gibbs
G = H − TS = U + PV − TS
| Immobile | Dichiarazione |
|----------|-----------|
| Significato | Lavoro massimo di non espansione a T costante, P |
| Equilibrio | Il sistema minimizza G a T costante, P |
| Spontaneità | ΔG < 0 → spontaneo; ΔG = 0 → equilibrio |
| Reazioni chimiche | ΔG = ΔH − TΔS determina la direzione |
### Riepilogo dei potenziali termodinamici
| Potenziale | Variabili naturali | Differenziale | Ridotto a icona quando |
|-----------|-------------|-------------|----------------|
| U (energia interna) | S, V | dU = TdS − PdV | Sistema isolato |
| H (entalpia) | S, P | dH = TdS + VdP | Costante P, adiabatica |
| F (Helmholtz) | T, V | dF = −SdT − PdV | Costante T, V |
| G (Gibbs) | T, P | dG = −SdT + VdP | Costante T, P |
---

## Il ciclo di Carnot
Il **ciclo di Carnot** è il motore termico più efficiente possibile, operando tra le temperature T_H (caldo) e T_C (freddo).
### Quattro fasi
| Palcoscenico | Processo | Cosa succede |
|-------|---------|-----|
| 1 → 2 | Espansione isotermica | Assorbire il calore Q_H dal serbatoio caldo a T_H |
| 2 → 3 | Espansione adiabatica | Il gas si raffredda da T_H a T_C |
| 3 → 4 | Compressione isotermica | Rigettare il calore Q_C nel serbatoio freddo a T_C |
| 4 → 1 | Compressione adiabatica | Il gas si riscalda da T_C a T_H |
### Efficienza di Carnot
η_Carnot = 1 − T_C/T_H
| T_H | T_C | η_Carnot |
|-----|-----|----------|
| 500K| 300K| 40% |
| 1000K| 300K| 70% |
| 300K| 299 K | 0,33%|
**Nessun motore reale può superare l'efficienza di Carnot.** I motori reali sono sempre irreversibili (attrito, turbolenza, differenze finite di temperatura).
---

## Meccanica statistica
### La distribuzione di Boltzmann
Per un sistema in equilibrio termico a temperatura T, la probabilità di trovarsi in un microstato con energia E_i:
P(E_i) = (1/Z) e^{−E_i / k_BT}
dove Z è la **funzione di partizione**:
Z = Σᵢ e^{−E_i / k_BT}
### La funzione di partizione
Z codifica tutte le informazioni termodinamiche sul sistema.
| Quantità | Formula |
|----------|---------|
| Energia libera di Helmholtz | F = −k_BT ln Z |
| Energia media | ⟨E⟩ = −∂(ln Z)/∂β dove β = 1/(k_BT) |
| Entropia | S = k_B(ln Z + β⟨E⟩) |
| Capacità termica | C_V = ∂⟨E⟩/∂T = k_Bβ²(⟨E²⟩ − ⟨E⟩²) |
| Pressione | P = (1/β) ∂(ln Z)/∂V |
### Esempio realizzato: sistema a due Stati
Una particella può trovarsi nello stato 0 (energia 0) o nello stato 1 (energia ε).
Z = 1 + e^{−βε}
| Quantità | Risultato |
|----------|--------|
| P(stato 0) | 1/(1 + e^{−βε}) |
| P(stato 1) | e^{−βε}/(1 + e^{−βε}) |
| ⟨E⟩ | ε/(1 + e^{βε}) |
| Limite T alto (β→0) | ⟨E⟩ → ε/2 (uguale probabilità) |
| Limite T basso (β→∞) | ⟨E⟩ → 0 (stato fondamentale) |
### Teorema di equipartizione
Ogni grado di libertà quadratico contribuisce con ½k_BT all'energia media.
| Sistema | Gradi di libertà | ⟨E⟩ |
|--------|-----|------|
| Gas monoatomico (He) | 3 traslazionale | (3/2)k_BT |
| Gas biatomico (N₂) nella stanza T | 3 trans + 2 rot | (5/2)k_BT |
| Gas biatomico ad alta T | 3 trans + 2 rot + 1 vib | (7/2)k_BT |
| Solido (modello Einstein) | 3 vibrazionali (per atomo) | 3k_BT |
---

## Collegamento alla teoria dell'informazione
### Entropia di Shannon ed entropia termodinamica
| Aspetto | Entropia di Shannon H(X) | Entropia termodinamica S |
|--------|---------------------|------------------------|
| Definizione | −Σ pᵢ log pᵢ | k_B ln Ω (o −k_B Σ pᵢ ln pᵢ) |
| Massimo quando | Distribuzione uniforme | Equilibrio termico |
| Misure | Incertezza/contenuto informativo | Numero di microstati accessibili |
| Unità | Bit o nat | J/K |
**Formula dell'entropia di Gibbs:** S = −k_B Σᵢ pᵢ ln pᵢ (identico nella forma all'entropia di Shannon)
### Principio della massima entropia
Entrambi i campi utilizzano lo stesso principio: la distribuzione che meglio rappresenta il nostro stato di conoscenza è quella che massimizza l’entropia soggetta a vincoli noti.
| Vincolo | Distribuzione risultante |
|-----------|----------------------|
| Media conosciuta | Distribuzione esponenziale |
| Media e varianza note | Distribuzione gaussiana |
| Energia conosciuta ⟨E⟩ | Distribuzione di Boltzmann |
| Nessun vincolo | Distribuzione uniforme |
### Principio di Landauer
Cancellando un bit di informazione si dissipano almeno k_BT ln 2 di energia sotto forma di calore. Ciò collega l’elaborazione delle informazioni direttamente alla termodinamica: il calcolo ha un costo energetico fondamentale.
---

## Rilevanza per l'apprendimento automatico e la scienza dei dati
| Concetto Thermo/StatMech | Applicazione |
|-----------------------|-------------|
| Distribuzione di Boltzmann | Funzione Softmax, modelli basati sull'energia, ricottura simulata |
| Funzione partizione | Costante di normalizzazione nei modelli probabilistici, intrattabile in generale |
| Energia libera | Inferenza variazionale (minimizzare l'energia libera variazionale = minimizzare la divergenza KL) |
| Entropia | Regolarizzazione, esplorazione in RL (massima entropia RL), alberi decisionali |
| Principio di massima entropia | Classificatori MaxEnt, selezione preventiva, stima della distribuzione |
| Ricottura simulata | Ottimizzazione globale riducendo gradualmente la "temperatura" |
| Meccanica statistica | Comprendere le transizioni di fase nell'apprendimento (grokking, doppia discesa) |
| Equipartizione | Comprendere la distribuzione dell'energia nelle simulazioni fisiche |
| Principio di Landauer | Limiti fondamentali del calcolo, calcolo reversibile |
| Campionamento di Gibbs | Metodo MCMC direttamente ispirato alla meccanica statistica |
| Temperatura (in softmax) | Controlla la casualità delle previsioni: P(i) ∝ exp(z_i/T) |
---

## Riepilogo
| Legge/Concetto | Idea fondamentale | Formula |
|------------|-----------|---------|
| Legge zero | La temperatura è ben definita | Transitività dell'equilibrio termico |
| Prima legge | L'energia si conserva | ΔU = Q − W |
| Seconda legge | L'entropia dell'universo aumenta | ΔS ≥ 0 |
| Terza legge | Lo zero assoluto è irraggiungibile | S → 0 come T → 0 |
| Entropia di Boltzmann | L'entropia conta i microstati | S = k_B ln Ω |
| Distribuzione di Boltzmann | Probabilità di stati energetici | P ∝ e^{−E/k_BT} |
| Funzione partizione | Codifica tutte le informazioni termodinamiche | Z = Σ e^{−E_i/k_BT} |
| Energia libera | Lavori utili disponibili | F = U − TS, G = H − TS |
| Efficienza di Carnot | Massima efficienza del motore termico | η = 1 − T_C/T_H |
La termodinamica e la meccanica statistica sono i luoghi in cui la fisica incontra la teoria dell'informazione. La stessa entropia che governa i motori termici governa la compressione dei dati. La stessa distribuzione di Boltzmann che descrive le molecole di gas alimenta lo strato softmax in ogni classificatore. Comprendere queste connessioni ti offre una visione unificata di fisica, probabilità e apprendimento automatico.