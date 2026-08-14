---
# Metadata
title: "Statistics and Probability"
description: "Probability theory, statistical inference, hypothesis testing, regression, and Bayesian methods"
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Split from mathematics_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [statistics, probability, hypothesis-testing, regression, bayesian-methods, data-analysis]
difficulty_level: "intermediate"
prerequisites:
  - "../mathematics/mathematics.md"
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Statistica e probabilità
Probabilità e statistica sono le basi matematiche della scienza dei dati, dell'apprendimento automatico e della ricerca scientifica. La probabilità ti dice quanto sono probabili gli eventi; le statistiche ti dicono come trarre conclusioni dai dati. Insieme, trasformano l’incertezza in conoscenza quantificabile e gestibile.
---

## Teoria della probabilità
### Concetti fondamentali
| Concetto | Descrizione | Esempio |
|---------|-----|---------|
| **Spazio campione** | Insieme di tutti i possibili risultati | Lanciare un dado: {1, 2, 3, 4, 5, 6} |
| **Evento** | Un sottoinsieme dello spazio campionario | Lanciando un numero pari: {2, 4, 6} |
| **Probabilità** | Numero compreso tra 0 e 1 che misura la verosimiglianza | P(6 lanciati) = 1/6 |
| **Probabilità condizionata** | P(A|B): probabilità che A dato B si sia verificato | P(pioggia | nuvoloso) |
| **Indipendenza** | Eventi in cui uno non influenza l'altro | I lanci delle monete sono indipendenti |
### Regole di probabilità
| Regola | Formula | Caso d'uso |
|------|---------|----------|
| **Regola di aggiunta** | P(A ∪ B) = P(A) + P(B) − P(A ∩ B) | Probabilità di A o B |
| **Regola della moltiplicazione** | P(A ∩ B) = P(A) × P(B|A) | Probabilità di A e B |
| **Regola del complemento** | P(non A) = 1 − P(A) | Probabilità che l'evento non si verifichi |
| **Legge della probabilità totale** | P(A) = Σ P(A|Bᵢ) × P(Bᵢ) | Partizionamento per eventi mutuamente esclusivi |
| **Teorema di Bayes** | P(A|B) = P(B|A) × P(A) / P(B) | Aggiornare le credenze con l'evidenza |
### Distribuzioni di probabilità
| Distribuzione | Digitare | Parametri chiave | Caso d'uso |
|-------------|------|----------------|----------|
| **Normale (gaussiana)** | Continuo | Media (μ), Deviazione standard (σ) | Fenomeni naturali, errori di misurazione |
| **Binomiale** | Discreto | n (prove), p (probabilità) | Il successo/fallimento conta |
| **Poisson** | Discreto | λ (tasso) | Eventi rari nel tempo/spazio |
| **Esponenziale** | Continuo | λ (tasso) | Tempo tra gli eventi |
| **Uniforme** | Entrambi | a, b (limiti) | Risultati altrettanto probabili |
| **Chi-quadrato** | Continuo | k (gradi di libertà) | Test di bontà di adattamento |
| **t-Distribuzione** | Continuo | ν (gradi di libertà) | Inferenza su piccolo campione |
### Proprietà chiave delle distribuzioni
| Immobile | Descrizione |
|----------|-------------|
| **Media (valore atteso)** | Centro di massa della distribuzione: E[X] = Σ xᵢ × P(xᵢ) |
| **Varianza** | Diffusione attorno alla media: Var(X) = E[(X − μ)²] |
| **Deviazione standard** | Radice quadrata della varianza; stesse unità dei dati |
| **Asimmetria** | Asimmetria della distribuzione |
| **Curtosi** | "Tailedness" - quanto sono pesanti le code |
---

## Inferenza statistica
### Statistica descrittiva e inferenziale
| | Descrittivo | Inferenziale |
|---|-----|-----|
| **Scopo** | Riepilogare e descrivere i dati | Trarre conclusioni su una popolazione da un campione |
| **Strumenti** | Media, mediana, moda, deviazione standard, grafici | Test di ipotesi, intervalli di confidenza, regressione |
| **Ambito** | Solo i dati che hai | Generalizzare oltre il campione |
### Quadro di verifica delle ipotesi
| Passo | Descrizione |
|------|-------------|
| 1. **Ipotesi statali** | Ipotesi nulla (H₀): nessun effetto; Alternativa (H₁): l'effetto esiste |
| 2. **Scegli il livello di significatività** | α = 0,05 (convenzionale) |
| 3. **Seleziona prova** | In base al tipo di dati, alla dimensione del campione e alle ipotesi |
| 4. **Calcola la statistica del test** | Dipende dal test scelto |
| 5. **Trova il valore p** | Probabilità di osservare i dati se H₀ è vera |
| 6. **Prendere una decisione** | Se p < α, rifiuta H₀; in caso contrario, non rifiutare H₀ |
### Test statistici comuni
| Prova | Quando usarlo | Cosa confronta |
|------|-------------|-----------------|
| **t-test** | Confronta le medie di 1–2 gruppi | Significato(i) del gruppo rispetto a un valore o tra loro |
| **Test del chi quadrato** | Dati categorici | Frequenze osservate e attese |
| **ANOVA** | Confronta le medie di 3+ ​​gruppi | Varianza tra gruppi e all'interno del gruppo |
| **U Mann-Whitney** | Alternativa non parametrica al test t | Distribuzioni di rango di due gruppi |
| **Correlazione di Pearson** | Relazione lineare tra due variabili continue | valore r da −1 a +1 |
| **Correlazione di Spearman** | Relazione monotona (basata sul rango) | valore ρ per dati ordinali o non normali |
### Intervalli di confidenza
Un intervallo di confidenza fornisce un intervallo di valori plausibili per un parametro della popolazione:
- **IC al 95% per media** (σ noto): x̄ ± 1,96 × (σ / √n)
- **Interpretazione**: "Siamo sicuri al 95% che la vera media della popolazione rientri in questo intervallo"
- **IC più ampio** = maggiore incertezza (campione più piccolo, variabilità più elevata o livello di confidenza più elevato)
---

## Analisi di regressione
### Tipi di regressione
| Digitare | Variabile dipendente | Caso d'uso |
|------|-------------|----------|
| **Regressione lineare** | Continuo | Prevedere i prezzi delle case, le vendite |
| **Regressione logistica** | Binario (0/1) | Classificazione: rilevamento spam, diagnosi malattie |
| **Regressione polinomiale** | Continuo (curvo) | Curve di crescita, trend non lineari |
| **Regressione multipla** | Continuo (2+ predittori) | Controllo dei confondenti |
| **Cresta / Lazo** | Continuo (regolarizzato) | Prevenire l'overfitting, selezione delle funzionalità |
### Nozioni di base sulla regressione lineare
Il modello: **y = β₀ + β₁x + ε**
| Componente | Significato |
|-----------|---------|
| β₀ (intercetta) | Valore di y quando x = 0 |
| β₁ (pendenza) | Variazione di y per una variazione di un'unità di x |
| ε (termine di errore) | Variazione inspiegabile |
**Metriche chiave:**
- **R² (coefficiente di determinazione)**: proporzione della varianza spiegata dal modello (da 0 a 1)
- **R² aggiustato**: R² penalizzato per il numero di predittori
- **RMSE**: errore quadratico medio: errore di previsione medio nelle stesse unità di y
### Presupposti di regressione lineare
| Presupposto | Cosa significa | Come controllare |
|-----------|--------------|--------------|
| **Linearità** | La relazione tra X e Y è lineare | Grafici a dispersione |
| **Indipendenza** | Le osservazioni sono indipendenti | Progettazione dello studio |
| **Omoschedasticità** | Varianza costante dei residui | Trame residue |
| **Normalità** | I residui sono distribuiti normalmente | Grafico Q-Q, test di Shapiro-Wilk |
| **Nessuna multicollinearità** | I predittori non sono altamente correlati | VIF (fattore di inflazione della varianza) |
---

## Statistica bayesiana
### Frequentista contro bayesiano
| | Frequentista | Bayesiano |
|---|-------------|----------|
| **Probabilità significa** | Frequenza di lungo periodo | Grado di fede |
| **I parametri sono** | Risolto ma sconosciuto | Variabili casuali con distribuzioni |
| **Utilizzo** | valori p, intervalli di confidenza | Distribuzioni posteriori, intervalli credibili |
| **Punti di forza** | Obiettivo, consolidato | Incorpora conoscenze pregresse, interpretazione intuitiva |
### Teorema di Bayes in pratica
**Posteriore = (Probabilità × Prioritario) / Prova**
Esempio: test medici:
- Prevalenza della malattia: 1% (precedente)
- Sensibilità del test: 95% (tasso di veri positivi)
- Specificità del test: 90% (tasso di veri negativi)
- Se il test è positivo: P(malattia | positivo) = (0,95 × 0,01) / (0,95 × 0,01 + 0,10 × 0,99) ≈ 8,8%
Questo risultato controintuitivo – la maggior parte dei risultati positivi sono falsi positivi quando la malattia è rara – è l’**errore del tasso di base**, e mostra perché il pensiero bayesiano è importante.
---

## Consigli pratici
- **Visualizza sempre i tuoi dati** prima di eseguire qualsiasi test statistico
- **Verifica ipotesi**: le violazioni possono invalidare i risultati
- **La dimensione dell'effetto conta**: un risultato statisticamente significativo può essere praticamente privo di significato
- **La correlazione non è causalità**: anche le correlazioni forti possono avere fattori confondenti
- **Confronti multipli** gonfiano i tassi di falsi positivi: applicare correzioni (Bonferroni, FDR)
- **Riporta gli intervalli di confidenza**, non solo i valori p
---

## Perché è importante
La statistica è la spina dorsale della ricerca scientifica, dell’analisi aziendale e dell’apprendimento automatico. Senza di esso, non è possibile distinguere il segnale dal rumore, identificare gli effetti reali dalle fluttuazioni casuali o fare previsioni con incertezza quantificata. Che tu stia analizzando test A/B, addestrando modelli ML o leggendo articoli di ricerca, l'alfabetizzazione statistica è essenziale.