<!--
---
# Metadata
title: "Electromagnetism"
description: "Electric and magnetic fields, Coulomb's law, Gauss's law, Faraday's law, Ampere's law, Maxwell's equations, electromagnetic waves, and RLC circuits"
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
    changes: "Initial deep-dive into electromagnetism"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [electromagnetism, maxwell-equations, electric-fields, magnetic-fields, electromagnetic-waves, circuits, gauss-law, faraday]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "classical_mechanics.md"
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
# Elettromagnetismo
L’elettromagnetismo è lo studio dei campi elettrici e magnetici e delle loro interazioni. Unificato da Maxwell nel 1860, l'elettromagnetismo spiega la luce, l'elettricità, il magnetismo, le onde radio e la struttura degli atomi. Fu la prima forza fondamentale ad essere pienamente compresa matematicamente, e le sue equazioni ispirarono la relatività speciale di Einstein e la moderna teoria dei campi.
---

## Campi elettrici
### Legge di Coulomb
La forza tra due cariche puntiformi q₁ e q₂ separate dalla distanza r:
**F** = (1/4πε₀) · (q₁q₂/r²) · r̂
| Costante | Valore |
|----------|-------|
| ε₀ (permittività dello spazio libero) | 8.854 × 10⁻¹² F/m |
| 1/4πε₀ (costante di Coulomb k) | 8.988 × 10⁹ N·m²/C² |
### Definizione di campo elettrico
**E** = **F**/q (forza per carica unitaria)
Per una carica puntiforme Q: **E** = (1/4πε₀) · (Q/r²) · r̂
### Linee del campo elettrico
| Immobile | Regola |
|----------|------|
| Direzione | Punta lontano dalle cariche positive, verso quelle negative |
| Densità | Linee più vicine = campo più forte |
| Attraversamento | Le linee del campo non si incrociano mai |
| Conduttori | Le linee incontrano la superficie perpendicolarmente |
### Potenziale elettrico (tensione)
V = −∫ **E** · d**l** (la differenza di potenziale è l'integrale negativo di E)
**E** = −∇V (il campo è il gradiente negativo del potenziale)
Per una carica puntiforme: V = (1/4πε₀) · Q/r
| Concetto | Formula | Unità |
|---------|---------|------|
| Energia potenziale | U = qV | Joule |
| Elettronvolt | 1 eV = 1.602 × 10⁻¹⁹ J | Unità energetica |
| Superficie equipotenziale | Superficie dove V è costante | E è perpendicolare ad esso |
---

## Legge di Gauss
### Dichiarazione
Il flusso elettrico totale attraverso qualsiasi superficie chiusa è uguale alla carica racchiusa divisa per ε₀:
∮ **E** · d**A** = Q_enc / ε₀
In forma differenziale: ∇ · **E** = ρ/ε₀
### Utilizzo della legge di Gauss
La legge di Gauss è particolarmente utile quando la simmetria consente di estrarre E dall'integrale.
| Simmetria | Superficie gaussiana | Risultato |
|----------|-----------|--------|
| Sferico | Sfera | E = Q/(4πε₀r²) esterno |
| Cilindrico (carica di linea) | Cilindro | E = λ/(2πε₀r) |
| Planare (foglio infinito) | Portapillole | E = σ/(2ε₀) |
| Tra piastre parallele | Portapillole | E = σ/ε₀ |
---

## Conduttori e condensatori
### Conduttori nell'equilibrio elettrostatico
| Immobile | Spiegazione |
|----------|-------------|
| E = 0 dentro | Gli addebiti vengono riorganizzati per annullare il campo interno |
| Tutta la carica in superficie | Nessun costo netto all'interno |
| E perpendicolare alla superficie | Nessuna componente tangenziale (altrimenti le cariche si spostano) |
| Equipotenziale in tutto | Stessa V ovunque all'interno e in superficie |
### Condensatori
Un **condensatore** immagazzina energia in un campo elettrico tra due conduttori.
| Configurazione | Capacità |
|--------------|-------------|
| Piastre parallele | C = ε₀A/d |
| Cilindrico | C = 2πε₀L / ln(b/a) |
| Sferico | C = 4πε₀ab / (b−a) |
| Formula | Espressione |
|---------|------------|
| Tensione di carica | Q = CV |
| Energia immagazzinata | U = ½CV² = ½Q²/C |
| Densità energetica | u = ½ε₀E² |
| Combinazione di serie | 1/C_totale = 1/C₁ + 1/C₂ + ... |
| Combinazione parallela | C_totale = C₁ + C₂ + ... |
### Dielettrici
L'inserimento di un dielettrico (materiale isolante) con κ costante aumenta la capacità: C = κC₀.
---

## Campi magnetici
### Forza magnetica
**F** = q(**v** × **B**) (forza di Lorentz, componente magnetica)
| Immobile | Dichiarazione |
|----------|-----------|
| Direzione | Perpendicolare sia a v che a B (regola della mano destra) |
| Lavoro svolto | Zero (la forza è perpendicolare alla velocità) |
| Movimento circolare | Raggio r = mv/(qB) nel campo B uniforme |
### Legge di Biot-Savart
Il campo magnetico dovuto ad un piccolo elemento di corrente:
d**B** = (μ₀/4π) · I(d**l** × r̂) / r²
| Costante | Valore |
|----------|-------|
| μ₀ (permeabilità dello spazio libero) | 4π × 10⁻⁷ T·m/A |
### Legge di Ampere
∮ **B** · d**l** = μ₀I_enc
In forma differenziale: ∇ × **B** = μ₀**J**
**Applicazioni:**
| Configurazione | Campo B |
|--------------|---------|
| Filo dritto lungo | B = μ₀I/(2πr) |
| Solenoide (interno) | B = μ₀nI |
| Toroide (interno) | B = μ₀NI/(2πr) |
---

## Induzione elettromagnetica
### Legge di Faraday
Un flusso magnetico variabile induce una forza elettromotrice (EMF):
FEM = −dΦ_B/dt
dove Φ_B = ∫ **B** · d**A** è il flusso magnetico.
In forma differenziale: ∇ × **E** = −∂**B**/∂t
**Legge di Lenz:** I campi elettromagnetici indotti si oppongono alla variazione di flusso (il segno meno).
### Applicazioni dell'induzione
| Applicazione | Principio |
|-------------|-----------|
| Generatore | Bobina rotante nel campo B → FEM alternata |
| Trasformatore | Modifica della corrente nel primario → FEM nel secondario |
| Induttore | Si oppone ai cambiamenti di corrente: EMF = −L(dI/dt) |
| Correnti parassite | Correnti indotte nei conduttori sfusi (frenatura, riscaldamento) |
### Induttori
| Formula | Espressione |
|---------|------------|
| Collegamento del flusso | Φ = LI|
| Energia immagazzinata | U = ½LI²|
| Combinazione di serie | L_totale = L₁ + L₂ + ... |
| Combinazione parallela | 1/L_totale = 1/L₁ + 1/L₂ + ... |
---

## Equazioni di Maxwell
Le equazioni di Maxwell uniscono l'elettricità e il magnetismo in un'unica teoria.
### In forma integrale
| Equazione | Nome | Dichiarazione |
|----------|------|-----------|
| ∮ **E** · d**A** = Q/ε₀ | Legge di Gauss (elettrica) | Flusso elettrico = carica racchiusa |
| ∮ **B** · d**A** = 0 | Legge di Gauss (magnetica) | Nessun monopolio magnetico |
| ∮ **E** · d**l** = −dΦ_B/dt | Legge di Faraday | Cambiare B induce E |
| ∮ **B** · d**l** = μ₀I + μ₀ε₀ dΦ_E/dt | Legge di Ampere-Maxwell | La E attuale e mutevole produce B |
### In forma differenziale
| Equazione | Nome | Espressione |
|----------|------|------------|
| Gauss (elettrico) | ∇ · **E** = ρ/ε₀ |
| Gauss (magnetico) | ∇ · **B** = 0 |
| Faraday | ∇ × **E** = −∂**B**/∂t |
| Ampere-Maxwell | ∇ × **B** = μ₀**J** + μ₀ε₀ ∂**E**/∂t |
### La corrente di spostamento
L'aggiunta chiave di Maxwell: il termine μ₀ε₀ ∂**E**/∂t (corrente di spostamento). Ciò garantisce la conservazione della carica e prevede le onde elettromagnetiche.
---

## Onde elettromagnetiche
Nel vuoto (senza cariche, senza correnti), le equazioni di Maxwell producono equazioni d'onda:
∇²**E** = μ₀ε₀ ∂²**E**/∂t²
∇²**B** = μ₀ε₀ ∂²**B**/∂t²
**Velocità della luce:** c = 1/√(μ₀ε₀) ≈ 3 × 10⁸ m/s
### Proprietà delle onde EM
| Immobile | Descrizione |
|----------|-------------|
| Trasversale | E e B sono perpendicolari tra loro e alla direzione di propagazione |
| In fase | E e B raggiungono i massimi simultaneamente |
| Rapporto di grandezza | E = cB |
| Flusso energetico | S = (1/μ₀)**E** × **B** (vettore Poynting) |
| Intensità | I = ⟨S⟩ = E₀²/(2μ₀c) |
### Lo spettro elettromagnetico
| Digitare | Lunghezza d'onda | Frequenza | Fonte |
|------|-----------|-----------|--------|
| Radio | > 1 metro| < 300 MHz | Antennas |
| Microwave | 1 mm − 1 m | 300 MHz − 300 GHz | Magnetrons, klystrons |
| Infrared | 700 nm − 1 mm | 300 GHz − 430 THz | Thermal radiation |
| Visible | 400 − 700 nm | 430 − 750 THz | Atomic transitions |
| Ultraviolet | 10 − 400 nm | 750 THz − 30 PHz | Hot objects, stars |
| X-ray | 0.01 − 10 nm | 30 PHz − 30 EHz | Electron deceleration |
| Gamma ray | < 0.01 nm | >30 EHz | Processi nucleari |
---

## Circuiti CA
### Componenti del circuito RLC
| Componente | Relazione tensione-corrente | Impedenza |
|-----------|---------------|-----------|
| Resistore (R) | V =IR | Z_R = R |
| Induttore (L) | V = L(dI/dt) | Z_L = jωL |
| Condensatore (C) | I = C(dV/dt) | Z_C = 1/(jωC) |
### Impedenza e risonanza
Impedenza totale (serie RLC): Z = R + j(ωL − 1/ωC)
|ω| = √(R² + (ωL − 1/ωC)²)
**Risonanza:** Quando ωL = 1/ωC → ω₀ = 1/√(LC)
- Alla risonanza: l'impedenza è minima (= R), la corrente è massima
- **Fattore di qualità:** Q = ω₀L/R (nitidezza della risonanza)
### Potenza nei circuiti CA
| Quantità | Formula |
|----------|---------|
| Potenza media | P_avg = V_rms · I_rms · cos φ |
| Fattore di potenza | cosφ = R/\|Z\| |
| Tensione efficace | V_rms = V₀/√2 |
---

## Rilevanza per l'apprendimento automatico e la scienza dei dati
| Concetto EM | Applicazione |
|-----------|-------------|
| Equazioni di Maxwell | Reti neurali informate dalla fisica, elettromagnetismo computazionale |
| Equazione delle onde | Fondamenti dell'elaborazione del segnale, motivazione dell'analisi di Fourier |
| Spettro elettromagnetico | Dati dei sensori (telecamere a infrarossi, radar, immagini satellitari) |
| Circuiti CA / impedenza | Comprendere l'hardware che esegue ML (alimentatori, integrità del segnale) |
| Vettore di puntamento | Flusso di energia nella comunicazione wireless (rilevante per IoT/edge ML) |
| Legge di Gauss | Analogo alla divergenza nel calcolo vettoriale, utilizzato nelle simulazioni di fluidodinamica |
| Condensatori/induttori | Calcolo analogico per reti neurali, hardware neuromorfico |
| Risonanza | Progettazione di filtri, analisi nel dominio della frequenza, metodi spettrali |
| Problemi sui valori al contorno | Metodi agli elementi finiti, simulazioni basate su mesh |
| Calcolo vettoriale (∇·, ∇×) | Strumenti matematici essenziali utilizzati nella teoria ML |
---

## Riepilogo
| Legge | Cosa dice | Forma differenziale |
|-----|-------------|-----|
| Gauss (elettrico) | Le cariche creano una divergenza del campo elettrico | ∇ · E = ρ/ε₀ |
| Gauss (magnetico) | Nessun monopolio magnetico | ∇ · B = 0 |
| Faraday | Cambiando B si crea l'arricciatura E | ∇ × E = −∂B/∂t |
| Ampere-Maxwell | La E attuale e quella che cambia creano l'arricciatura B | ∇ × B = μ₀J + μ₀ε₀∂E/∂t |
L’elettromagnetismo è la teoria fisica più completa e ben testata mai costruita. Le sue equazioni, solo quattro, descrivono tutto, dall'elettricità statica alla luce, al comportamento di ogni dispositivo elettronico mai costruito. Per i data scientist, la comprensione dell'elettromagnetismo fornisce una profonda intuizione dei fenomeni ondulatori, del calcolo vettoriale e della fisica che è alla base di tutto l'hardware informatico moderno.