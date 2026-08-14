---
# Metadata
title: "Ensemble Methods"
description: "Bagging, boosting, stacking, voting, random forests, XGBoost"
category: "Data Science and Analytics"
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ensemble, methods, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Metodi d'insieme
I metodi ensemble combinano più modelli di machine learning per produrre previsioni migliori di quelle che un singolo modello potrebbe ottenere da solo. L’intuizione è semplice: se si hanno diversi modelli che sono ciascuno piuttosto accurato ma commettono errori diversi, combinando le loro previsioni si annulleranno i singoli errori e si produrrà un risultato più robusto. Gli ensemble sono alla base delle soluzioni di machine learning più competitive e rimangono alcune delle tecniche più affidabili nei sistemi di produzione.
---

## Perché gli ensemble funzionano
| Principio | Descrizione |
|-----------|-------------|
| **Saggezza delle folle** | Stime imperfette multiple, mediate, sono migliori di qualsiasi stima singola |
| **Compromesso bias-varianza** | Gli ensemble possono ridurre la varianza (bagging) o il bias (boost) senza sacrificare l'altro |
| **Diversità degli errori** | Se i modelli commettono errori diversi, la loro combinazione annulla gli errori individuali |
| **Livellamento dei confini decisionali** | Più modelli creano una superficie decisionale più solida di un modello |
---

## Bagging (aggregazione bootstrap)
### Come funziona
| Passo | Descrizione |
|------|-------------|
| **1. Campionamento bootstrap** | Disegna più campioni casuali (con sostituzione) dai dati di addestramento |
| **2. Modelli base del treno** | Addestra un modello su ciascun campione bootstrap (tipicamente alberi decisionali) |
| **3. Aggregato** | Per la regressione: previsioni medie. Per la classificazione: voto a maggioranza |
### Caratteristiche principali
| Caratteristico | Descrizione |
|---------------|-------------|
| **Riduce la varianza** | La media attenua le fluttuazioni dei singoli modelli |
| **Formazione parallela** | Ogni modello base è indipendente; possono essere addestrati simultaneamente |
| **Valutazione fuori borsa** | Ogni campione viene escluso da alcuni campioni bootstrap; utilizzare quelli per la convalida |
| **Decorrelazione** | La selezione casuale delle caratteristiche ad ogni suddivisione riduce la correlazione tra gli alberi |
### Foresta casuale
| Aspetto | Descrizione |
|--------|-------------|
| **Studente base** | Alberi decisionali |
| **Aggiunta chiave** | Ad ogni suddivisione, considera solo un sottoinsieme casuale di funzionalità (tipicamente sqrt(n_features)) |
| **Perché funziona** | La selezione casuale delle caratteristiche decorrela gli alberi, rendendo l'insieme più robusto |
| **Iperparametri** | Numero di alberi; profondità massima; campioni minimi per foglia; caratteristiche massime |
| **Punti di forza** | Gestisce dati ad alta dimensione; robusto ai valori anomali; fornisce l'importanza delle funzionalità |
| **Punti deboli** | Meno interpretabile dei singoli alberi; può sovrapporsi a compiti di regressione rumorosi |
---

## Potenziamento
### Come funziona
| Passo | Descrizione |
|------|-------------|
| **1. Primo modello del treno** | Addestra un modello base (spesso un albero poco profondo/"ceppo") sui dati |
| **2. Identificare gli errori** | Trova in quali istanze il modello ha sbagliato |
| **3. Addestra il prossimo modello** | Formare un nuovo modello focalizzato sugli errori (riponderato o adattato ai residui) |
| **4. Combina in sequenza** | Ogni nuovo modello corregge gli errori accumulati di tutti i modelli precedenti |
| **5. Ripeti** | Continua per un numero specificato di round |
### Potenziamento degli algoritmi
| Algoritmo | Funzione di perdita | Caratteristica fondamentale |
|-----------|--------------|-----|
| **AdaBoost** | Esponenziale | Ripesa le istanze classificate erroneamente; semplice; sensibile al rumore |
| **Amplificazione gradiente** | Qualsiasi perdita differenziabile | Si adatta ai residui (gradiente di perdita); più flessibile |
| **XGBoost** | Potenziamento del gradiente regolarizzato | regolarizzazione L1/L2; gradienti del secondo ordine; ottimizzazione hardware |
| **LightGBM** | Campionamento unilaterale basato su gradiente | Crescita fogliare; basato su istogrammi; veloce su set di dati di grandi dimensioni |
| **CatBoost** | Potenziamento ordinato | Gestisce le funzionalità categoriche in modo nativo; riduce il sovradattamento |
### Potenziamento vs Bagging
| Dimensione | Insaccamento | Potenziamento |
|-----------|---------|----------|
| **Formazione** | Parallelo | Sequenziale |
| **Focus** | Riduce la varianza | Riduce i pregiudizi |
| **Modelli base** | Alta varianza e bassa distorsione (alberi profondi) | Bassa varianza, alta distorsione (alberi poco profondi/ceppi) |
| **Combinazione** | Uguale peso | Ponderato in base alle prestazioni |
| **Sovradattamento** | Meno incline | Può adattarsi eccessivamente se troppi giri |
| **Sensibilità al rumore** | Robusto | Sensibile ai dati rumorosi |
---

## Impilazione
### Come funziona
| Passo | Descrizione |
|------|-------------|
| **1. Modelli base del treno** | Addestrare diversi modelli (ad esempio, foresta casuale, SVM, rete neurale, potenziamento del gradiente) |
| **2. Genera previsioni** | Utilizzare le previsioni out-of-fold (convalida incrociata) come funzionalità di input |
| **3. Metamodello del treno** | Addestrare un modello di secondo livello sulle previsioni dei modelli base |
| **4. Pronostico finale** | I modelli di base prevedono; il meta-modello combina le loro previsioni |
### Migliori pratiche per l'impilamento
| Pratica | Motivo |
|----------|--------|
| **Utilizza diversi modelli base** | Algoritmi diversi commettono errori diversi; il punto centrale è la diversità |
| **Utilizza la convalida incrociata per le previsioni di base** | Impedisce al metamodello di imparare a sfruttare i modelli base sovraadattati |
| **Mantieni il meta-modello semplice** | Regressione logistica o albero superficiale; i modelli base fanno il lavoro pesante |
| **Includi funzionalità grezze nel metamodello** | A volte è utile dare al metamodello l'accesso anche alle funzionalità originali |
---

## Votazione e media
### Votazione difficile (classificazione)
| Modello | Pronostico |
|-------|-----------|
| Modello A | Classe 1 |
| Modello B | Classe 0 |
| Modello C | Classe 1 |
| **Voto a maggioranza** | **Classe 1** |
### Votazione soft (classificazione)
| Modello | P(Classe 0) | P(Classe 1) |
|-------|-----------|-----------|
| Modello A | 0,3 | 0,7 |
| Modello B | 0,6 | 0,4 |
| Modello C | 0,4 | 0,6 |
| **Media** | **0,43** | **0,57** |
| **Previsione** | | **Classe 1** |
### Media ponderata
| Modello | Peso | Pronostico |
|-------|--------|-----------|
| Modello A | 0,5 | 0,8 |
| Modello B | 0,3 | 0,6 |
| Modello C | 0,2 | 0,9 |
| **Media ponderata** | | 0,5×0,8 + 0,3×0,6 + 0,2×0,9 = 0,76 |
---

## Guida pratica
### Quando utilizzare quale ensemble
| Scenario | Metodo consigliato |
|----------|-------------|
| **Riferimento rapido; dati tabellari** | Foresta casuale |
| **Massima precisione; dati tabellari** | XGBoost / LightGBM / CatBoost |
| **Dati disturbati** | Insaccamento (il potenziamento sovradimensionerà il rumore) |
| **Interpretabilità necessaria** | Modello singolo o piccolo insieme con importanza caratteristica |
| **Diversi tipi di modelli** | Impilamento o votazione |
| **Apprendimento online** | Metodi di streaming ensemble; potenziamento adattivo |
| **Dati sbilanciati** | Foresta casuale bilanciata; incentivazione sensibile ai costi |
### Strategie di diversità d'insieme
| Strategia | Descrizione |
|----------|-------------|
| **Algoritmi diversi** | Combina modelli basati su alberi, lineari e neurali |
| **Caratteristiche diverse** | Addestrare modelli su diversi sottoinsiemi di funzionalità |
| **Diversi sottoinsiemi di dati** | Insaccamento; sottocampionamento |
| **Diversi iperparametri** | Stesso algoritmo con varie configurazioni |
| **Diversi periodi di tempo** | Treno in diverse finestre orarie |
---

## Riepilogo
I metodi ensemble funzionano perché combinano più modelli imperfetti in un unico predittore robusto. Il bagging (foreste casuali) riduce la varianza addestrando i modelli in parallelo sui campioni bootstrap e sulla media. Il potenziamento (XGBoost, LightGBM, CatBoost) riduce la distorsione addestrando i modelli in sequenza, ciascuno correggendo gli errori precedenti. L'impilamento utilizza un meta-modello per combinare diversi modelli base. Votazione e media sono gli insiemi più semplici. Il filo conduttore è la diversità: gli insiemi funzionano meglio quando i modelli che li compongono sono individualmente ragionevoli ma commettono errori diversi. In pratica, il gradient boosting sui dati tabulari è spesso l’approccio singolo con le prestazioni più elevate, mentre l’impilamento di modelli diversi spinge ulteriormente la precisione nelle competizioni e nelle applicazioni ad alto rischio.