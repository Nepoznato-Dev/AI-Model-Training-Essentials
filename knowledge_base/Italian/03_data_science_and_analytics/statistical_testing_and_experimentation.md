<!--
---
# Metadata
title: "Statistical Testing and Experimentation"
description: "Hypothesis testing, A/B testing, effect size, causal inference"
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
tags: [statistical, testing, experimentation, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Test statistici e sperimentazione
La statistica è la grammatica della scienza. Fornisce gli strumenti per distinguere modelli reali dal rumore casuale, per misurare se un cambiamento ha effettivamente migliorato le cose e per prendere decisioni in condizioni di incertezza. Questo file copre i concetti fondamentali della verifica delle ipotesi, della progettazione sperimentale e delle insidie ​​​​comuni che inciampano le persone.
---

## Il quadro di verifica delle ipotesi
Ogni test statistico segue la stessa logica:
1. **Enunciare l'ipotesi nulla (H₀)**: non c'è alcun effetto/nessuna differenza.
2. **Enunciare l'ipotesi alternativa (H₁)**: C'è un effetto/una differenza.
3. **Scegliere un livello di significatività (α)**: Solitamente 0,05 (5% di possibilità di falsi positivi).
4. **Raccogliere dati e calcolare una statistica di test**.
5. **Calcola il valore p**: probabilità di osservare questo risultato (o un risultato più estremo) se H₀ è vero.
6. **Prendere una decisione**: Se p < α, rifiutare H₀ (statisticamente significativo). Altrimenti, non rifiutare H₀.
### Concetti chiave
| Concetto | Significato | Malinteso comune |
|---------|---------|---------------------|
| **valore p** | P(dati \| H₀ è vero) | NON "la probabilità che H₀ sia vera" |
| **α (livello di significatività)** | Soglia per rifiutare H₀ | Non una misura dell'importanza dell'effetto |
| **Rilevanza statistica** | Risultato improbabile per pura casualità | NON significa praticamente significativo |
| **Dimensione dell'effetto** | Entità dell'effetto osservato | Separato dal valore p; un effetto piccolo può essere significativo con N | grandi
| **Potenza** | Probabilità di rifiutare correttamente un falso H₀ | In genere puntare all'80%+ |
| **Intervallo di confidenza** | Intervallo di valori plausibili per il parametro | Un IC del 95% non significa "probabilità del 95% che il valore reale rientri in questo intervallo" |
---

## Tipi di errori
| | H₀ è vero | H₀ è falso |
|---|-----------|------------|
| **Rifiuta H₀** | Errore di tipo I (falso positivo) | ✅ Corretto (vero positivo) |
| **Non rifiutare H₀** | ✅ Corretto (vero negativo) | Errore di tipo II (falso negativo) |
| Errore | Simbolo | Significato |
|-------|--------|---------|
| **Tipo I** | α | Concludere che c'è un effetto quando non c'è |
| **Tipo II** | β | Manca un effetto reale |
---

## Scegliere il test giusto
| Scenario | Prova | Ipotesi |
|----------|------|-----|
| Confronta le medie di 2 gruppi | **t-test** (indipendente) | Distribuzione normale, varianza uguale |
| Confronta le medie delle osservazioni accoppiate | **T-test accoppiato** | Le differenze sono distribuite normalmente |
| Confronta le medie di 3+ ​​gruppi | **ANOVA** | Distribuzione normale, varianza uguale |
| Confronta le distribuzioni categoriali | **Test del chi quadrato** | Dimensione del campione sufficiente per cella |
| Confronta distribuzioni (non parametriche) | **U Mann-Whitney** | Nessun presupposto di normalità |
| Confronta 3+ gruppi (non parametrici) | **Kruskal-Wallis** | Nessun presupposto di normalità |
| Prova di correlazione | **Pearson** (lineare) o **Spearman** (monotonico) | Pearson: normalità; Spearman: basato sul rango |
| Verifica se i dati seguono una distribuzione | **Kolmogorov-Smirnov** | Dati continui |
### Parametrico e non parametrico
| | Parametrico | Non parametrico |
|---|-----------|---------------|
| **Ipotesi** | I dati seguono una distribuzione specifica (solitamente normale) | Nessuna ipotesi di distribuzione |
| **Potenza** | Più alto quando le ipotesi sono soddisfatte | Più basso, ma più robusto |
| **Quando usarlo** | Campioni di grandi dimensioni, dati approssimativamente normali | Piccoli campioni, dati distorti, dati ordinali |
---

## Test specifici in dettaglio
### t-Test
Confronta le medie di due gruppi.
| Variante | Caso d'uso |
|---------|----------|
| **T-test indipendente** | Due gruppi separati (trattamento vs controllo) |
| **T-test accoppiato** | Stesso gruppo misurato due volte (prima vs dopo) |
| **T-test per un campione** | Confronta una media campionaria con un valore noto |
```python
from scipy import stats

# Independent t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b)
```

### ANOVA (Analisi della varianza)
Confronta le medie di 3 o più gruppi. Verifica se almeno una media del gruppo differisce dal resto.
| Digitare | Progettazione |
|------|--------|
| **ANOVA unidirezionale** | Una variabile indipendente con 3+ livelli |
| **ANOVA bidirezionale** | Due variabili indipendenti; verifica gli effetti di interazione |
| **Misure ripetute ANOVA** | Stessi soggetti misurati in condizioni diverse |
Se l'ANOVA è significativo, proseguire con **test post-hoc** (HSD di Tukey) per scoprire quali gruppi specifici differiscono.
### Test del chi quadrato
Verifica se due variabili categoriali sono indipendenti.
| Caso d'uso | Esempio |
|----------|---------|
| **Test di indipendenza** | Il genere è associato alla preferenza del prodotto? |
| **Buon adattamento** | Il lancio di un dado segue una distribuzione uniforme? |
**Regola pratica**: ogni cella deve avere un conteggio previsto di almeno 5.
---

## Test A/B
Il test A/B è l'applicazione del test di ipotesi alle decisioni aziendali, in genere confrontando un controllo (A) con una variante (B).
### Processo di progettazione
| Passo | Descrizione |
|------|-------------|
| **1. Definire ipotesi** | "Cambiare il colore del pulsante da blu a verde aumenterà la percentuale di clic" |
| **2. Scegli metrica** | Principale: percentuale di clic. Secondario: tasso di conversione, entrate. |
| **3. Calcola la dimensione del campione** | Basato sull'effetto minimo rilevabile, sulla potenza (80%) e sulla significatività (5%) |
| **4. Randomizzare** | Assegna in modo casuale gli utenti al controllo e al trattamento |
| **5. Esegui esperimento** | Raccogliere i dati fino al raggiungimento della dimensione del campione target |
| **6. Analizzare** | Confrontare le metriche utilizzando test statistici appropriati |
| **7. Decidi** | Implementare se statisticamente e praticamente significativo |
### Calcolo della dimensione del campione
La dimensione del campione necessaria dipende da:
| Fattore | Effetto sulla dimensione del campione |
|--------|----------------------|
| **Effetto più piccolo da rilevare** | Hai bisogno di più campioni |
| **Potenza superiore** | Hai bisogno di più campioni |
| **Livello di significatività inferiore** | Hai bisogno di più campioni |
| **Varianza più elevata** | Hai bisogno di più campioni |
### Errori comuni nei test A/B
| Errore | Perché è sbagliato |
|---------|---------------|
| **Sbirciare presto** | Il controllo quotidiano dei risultati aumenta il tasso di falsi positivi |
| **Metriche multiple senza correzione** | Testare 20 metriche con α=0,05 → aspettarsi 1 falso positivo per caso |
| **Fermo prima del bersaglio N** | Il test sottodimensionato non è in grado di rilevare effetti reali |
| **Tralasciando la stagionalità** | Esecuzione di un test durante un periodo festivo rispetto a una settimana normale |
| **Assegnazione non casuale** | Bias di selezione (ad esempio, assegnazione di nuovi utenti al trattamento) |
| **Confondere significato con importanza** | Un aumento dello 0,1% può essere statisticamente significativo ma non vale la pena di realizzarlo |
---

## Confronti multipli
Quando si eseguono molti test contemporaneamente, la possibilità di almeno un falso positivo aumenta notevolmente.
| Numero di test | Probabilità di ≥1 falso positivo (a α=0,05) |
|----------------|----------------------------------------------------|
| 1| 5%|
| 5| 23% |
| 10| 40% |
| 20| 64% |
### Correzioni
| Metodo | Come funziona | Quando usarlo |
|--------|-------------|-----|
| **Bonferroni** | Dividi α per il numero di test (α/n) | conservatore; pochi confronti |
| **Holm-Bonferroni** | Procedura di riduzione; meno conservatore | Uso generale |
| **Benjamini-Hochberg (FDR)** | Controlla il tasso di rilevamento di falsi | Molti test; analisi esplorativa |
---

## Dimensione dell'effetto
I valori P ti dicono *se* esiste un effetto. La dimensione dell'effetto ti dice *quanto è grande*.
| Misura | Per | Interpretazione |
|---------|-----|------|
| **La morte di Cohen** | Differenza tra due medie | 0,2 = piccolo, 0,5 = medio, 0,8 = grande |
| **R di Pearson** | Correlazione | 0,1 = piccolo, 0,3 = medio, 0,5 = grande |
| **η² (eta-quadrato)** | ANOVA | 0,01 = piccolo, 0,06 = medio, 0,14 = grande |
| **Rapporto quote** | Risultati categoriali | 1,0 = nessun effetto; >1 o <1 = effetto |
**Riportare sempre la dimensione dell'effetto insieme ai valori p.** Un risultato può essere statisticamente significativo ma praticamente privo di significato.
---

## Bayesiano vs Frequentista
| Aspetto | Frequentista | Bayesiano |
|--------|------------|----------|
| **Probabilità** | Frequenza degli eventi nel lungo periodo | Grado di fede |
| **Parametri** | Risolto ma sconosciuto | Variabili casuali con distribuzioni |
| **Utilizzo** | valori p, intervalli di confidenza, test di ipotesi | Distribuzioni posteriori, intervalli credibili |
| **Precedente** | Nessuna convinzione precedente incorporata | Distribuzione preventiva esplicita |
| **Interpretazione** | "Se ripetessimo più volte questo esperimento..." | "Dati i dati, la probabilità che..." |
| **Punti di forza** | Obiettivo, consolidato, semplice | Interpretazione intuitiva, incorpora conoscenze pregresse |
| **Punti deboli** | valori p ampiamente fraintesi | La scelta del preventivo può essere soggettiva |
---

## Nozioni di base sull'inferenza causale
La correlazione non è causalità. Ma a volte è necessario sapere *se X ha causato Y*, non solo se sono associati.
| Metodo | Descrizione | Quando usarlo |
|--------|-------------|-----|
| **Esperimenti randomizzati** | Standard aureo; l'assegnazione casuale elimina i confondenti | Quando puoi randomizzare |
| **Differenza nelle differenze (DiD)** | Confrontare i cambiamenti nel tempo tra trattamento e controllo | Cambiamenti politici, esperimenti naturali |
| **Discontinuità di regressione (RDD)** | Sfruttare una soglia di interruzione | Borse di studio, soglie di ammissibilità |
| **Variabili strumentali (IV)** | Utilizzare uno strumento che influenzi direttamente il trattamento ma non il risultato | Quando la randomizzazione non è possibile |
| **Corrispondenza del punteggio di propensione** | Abbinare le unità trattate e controllare le caratteristiche osservate | Studi osservazionali |
---

## Errori statistici comuni
| Errore | Descrizione |
|---------|-----|
| **p-hacking** | Provando molte analisi finché non trovi p < 0,05 |
| **HARKING** | Fare ipotesi dopo che i risultati sono noti |
| **Bias di sopravvivenza** | Guardando solo ai successi (ad esempio, aziende di successo) |
| **Il paradosso di Simpson** | La tendenza si inverte quando i dati vengono aggregati anziché suddivisi per gruppo |
| **Trasgressione del tasso di base** | Ignorare la probabilità a priori nell'interpretazione dei risultati |
| **Errore ecologico** | Inferire il comportamento individuale dai dati a livello di gruppo |
| **Confusione** | Una terza variabile spiega la relazione osservata |
| **Sovradattamento** | Il modello cattura il rumore, non il segnale |
---

## Riepilogo
I test statistici riguardano il prendere decisioni in condizioni di incertezza con onestà intellettuale. Esponi sempre le tue ipotesi prima di raccogliere dati. Scegli il test giusto per il tuo tipo di dati. Riporta le dimensioni degli effetti, non solo i valori p. Corretto per confronti multipli. E ricorda: la significatività statistica non è la stessa cosa della significatività pratica.