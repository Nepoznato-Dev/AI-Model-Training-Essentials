<!--
---
# Metadata
title: "Graph Theory"
description: "Graph representations, trees, traversals, shortest paths, minimum spanning trees, network flows, and spectral graph theory"
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
    changes: "Initial deep-dive into graph theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [graph-theory, trees, traversals, shortest-paths, spanning-trees, network-flows, spectral-graph-theory]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Teoria dei grafi
Un **grafo** è una struttura matematica costituita da vertici (nodi) collegati da bordi (collegamenti). Relazioni del modello grafico: reti sociali, mappe stradali, reti neurali, dipendenze, canali di comunicazione. La teoria dei grafi, ovvero lo studio di queste strutture, fornisce algoritmi e teoremi fondamentali per l’informatica, la ricerca operativa e la scienza dei dati.
---

## Concetti fondamentali
### Definizioni
| Termine | Definizione | Notazione |
|------|------------|----------|
| **Grafico** | Una coppia G = (V, E) di vertici e archi | G |
| **Vertice (nodo)** | Un elemento di V | v, u, w |
| **Bordo** | Una connessione tra due vertici | e = (u, v) oppure {u, v} |
| **Ordine** | Numero di vertici | \|V\| = n |
| **Taglia** | Numero di bordi | \|E\| = m|
| **Laurea** | Numero di archi incidenti ad un vertice | deg(v) |
| **Percorso** | Sequenza di vertici distinti collegati da spigoli | v₁, v₂, ..., vₖ |
| **Ciclo** | Un percorso che inizia e finisce nello stesso vertice | v₁ → v₂ → ... → vₖ → v₁ |
| **Connesso** | Esiste un percorso tra ogni coppia di vertici | — |
| **Componente** | Un sottografo connesso massimale | — |
| **Sottografo** | Un grafico formato da un sottoinsieme di V ed E | H ⊆ SOL |
### Tipi di grafici
| Digitare | Descrizione | Esempio |
|------|-------------|---------|
| **Non diretto** | I bordi non hanno direzione | Rete di amicizia |
| **Diretto (digrafo)** | I bordi hanno direzione (archi) | Collegamenti a pagine Web |
| **Ponderato** | I bordi portano valori numerici | Distanze stradali |
| **Non ponderato** | Tutti gli spigoli sono equivalenti | Connessioni sociali |
| **Semplice** | Nessun loop, nessun bordo multiplo | La maggior parte dei grafici dei libri di testo |
| **Multigrafo** | Sono consentiti più bordi tra gli stessi vertici | Rotte di volo (voli multipli tra città) |
| **Completo** | Ogni coppia di vertici è connessa | Kₙ ha n(n−1)/2 archi |
| **Bipartito** | I vertici si dividono in due gruppi; i bordi attraversano solo i gruppi | Matrici di raccomandazione degli articoli utente |
| **Planare** | Può essere disegnato senza attraversamenti dei bordi | Layout del circuito |
| **Albero** | Grafico connesso e aciclico | Alberi decisionali, file system |
| **DAG** | Cicli diretti e non diretti | Pianificazione delle attività, grafici delle dipendenze |
### Il lemma della stretta di mano
La somma di tutti i gradi dei vertici è pari al doppio del numero di bordi:
Σᵥ deg(v) = 2|E|
**Corollario:** Ogni grafico ha un numero pari di vertici di grado dispari.
**Esempio:** In un gruppo di 10 persone in cui ognuno stringe la mano esattamente ad altri 3: Σ deg = 30, quindi |E| = 15 strette di mano in totale.
---

## Rappresentazioni grafiche
Il modo in cui memorizzi un grafico in memoria determina l'efficienza di ogni algoritmo che esegui su di esso.
| Rappresentanza | Spazio | Ricerca bordi | Iterare i vicini | Ideale per |
|----------------|-------|-----|--------------------|----------|
| **Matrice di adiacenza** | O(n²) | O(1) | O(n) | Grafici densi, test rapidi sui bordi |
| **Elenco adiacenze** | O(n + m) | O(gradi(v)) | O(gradi(v)) | Grafici sparsi, la maggior parte delle reti del mondo reale |
| **Elenco bordi** | O(m) | O(m) | O(m) | Algoritmi semplici, MST di Kruskal |
| **Matrice di incidenza** | O(n · m) | O(m) | O(m) | Algoritmi specializzati |
### Matrice di adiacenza
Una matrice A n × n dove A[i][j] = 1 se esiste il bordo (i,j), 0 altrimenti. Per i grafici ponderati, A[i][j] = peso.
**Proprietà:**
- Simmetrico per grafi non orientati
- Aᵏ[i][j] = numero di cammini di lunghezza k da i a j
- Gli autovalori di A rivelano proprietà strutturali (vedi Teoria dei grafi spettrali)
### Elenco delle adiacenze
Un array (o mappa hash) in cui ciascun vertice v memorizza un elenco dei suoi vicini.
```
Vertex 0: [1, 3]
Vertex 1: [0, 2, 3]
Vertex 2: [1, 3]
Vertex 3: [0, 1, 2]
```

Questa è la rappresentazione più comune per i grafici del mondo reale, che sono tipicamente sparsi (m ≪ n²).
---

## Alberi
Un **albero** è un grafo connesso, aciclico e non orientato. Una **foresta** è un'unione disgiunta di alberi.
### Proprietà degli alberi
Per un albero con n vertici:
- Ha esattamente n − 1 archi
- C'è esattamente un percorso tra due vertici qualsiasi
- La rimozione di qualsiasi bordo lo disconnette
- L'aggiunta di qualsiasi bordo crea esattamente un ciclo
### Tipi di alberi
| Digitare | Descrizione | Applicazione |
|------|-------------|-----|
| **Albero radicato** | Un vertice designato come radice | File system, organigrammi |
| **Albero binario** | Ogni nodo ha al massimo 2 figli | BST, analisi delle espressioni, alberi decisionali |
| **Albero in equilibrio** | L'altezza è O(log n) | Alberi AVL, alberi rosso-neri (database) |
| **Albero di copertura** | Sottografo che include tutti i vertici ed è un albero | Progettazione di reti, algoritmi di approssimazione |
| **Albero di copertura minimo** | Albero di supporto con peso totale minimo del bordo | Progettazione di reti, clustering |
| **Grafico stellare** | Un nodo centrale connesso a tutti gli altri | Reti hub-and-spoke |
### Proprietà dell'albero binario
| Immobile | Formula |
|----------|---------|
| Nodi massimi alla profondità d | 2ᵈ |
| Numero massimo di nodi nell'albero di altezza h | 2ʰ⁺¹ − 1 |
| Altezza minima per n nodi | ⌊log₂(n)⌋ |
| Nodi foglia nell'albero binario completo | Nodi interni + 1 |
### Attraversamenti degli alberi
| Traversata | Ordina | Caso d'uso |
|-----------|-------|----------|
| **Pre-ordine** | Radice → Sinistra → Destra | Copia di un albero, espressione del prefisso |
| **In ordine** | Sinistra → Radice → Destra | Output ordinato da BST |
| **Post-ordine** | Sinistra → Destra → Radice | Eliminazione di un albero, espressione suffissa |
| **Ordine dei livelli (BFS)** | Livello per livello, da sinistra a destra | Percorso più breve nell'albero non ponderato |
---

## Attraversamenti del grafico
Gli algoritmi attraversanti visitano sistematicamente ogni vertice raggiungibile.
### Ricerca in ampiezza (BFS)
Esplora i vertici strato per strato, utilizzando una **coda**.
| Immobile | Valore |
|----------|-------|
| Struttura dei dati | Coda (FIFO) |
| Complessità temporale | O(V + E) |
| Complessità spaziale | O(V) |
| Trova il percorso più breve? | Sì (grafici non ponderati) |
| Completare? | Sì (esplora tutti i vertici raggiungibili) |
**Algoritmo:**
1. Inizia dal vertice di origine s. Mark ha ricevuto la visita. Accodare s.
2. Mentre la coda non è vuota: rimuovi dalla coda il vertice u. Per ogni vicino v non visitato di u: segna v visitato, accoda v.
**Applicazioni:** percorso più breve in grafici non ponderati, componenti connessi, test di bipartitismo, scansione web.
### Ricerca in profondità (DFS)
Esplora il più in profondità possibile prima di tornare indietro, utilizzando uno **stack** (o ricorsione).
| Immobile | Valore |
|----------|-------|
| Struttura dei dati | Stack (LIFO) / ricorsione |
| Complessità temporale | O(V + E) |
| Complessità spaziale | O(V) |
| Trova il percorso più breve? | No |
| Completare? | Sì (per grafi finiti) |
**Algoritmo:**
1. Inizia dal vertice s. Mark ha ricevuto la visita.
2. Per ogni vicino non visitato v di s: ricorsivamente DFS da v.
**DFS classifica gli spigoli in:**
- **Bordi dell'albero:** parte dell'albero DFS
- **Bordi posteriori:** collega un vertice al suo antenato (indica i cicli)
- **Bordi anteriori:** collega un vertice al suo discendente
- **Bordi incrociati:** collega i vertici in diversi rami
**Applicazioni:** ordinamento topologico, rilevamento di cicli, componenti fortemente connessi, risoluzione di labirinti.
### Confronto tra BFS e DFS
| Criterio | BFS | DFS |
|-----------|-----|-----|
| Strategia | Largo e poi profondo | Profondo e poi largo |
| Memoria | Superiore (negozi di frontiera) | Inferiore (percorso negozi) |
| Percorso più breve (non ponderato) | Garantito | Non garantito |
| Utilizzare quando la soluzione è vicina all'inizio | Meglio | Peggio |
| Da utilizzare quando il grafico è molto profondo | Peggio | Meglio |
| Ordinamento topologico | Variante dell'algoritmo di Kahn | Approccio standard |
---

## Algoritmi del percorso più breve
Trovare il percorso più breve tra i vertici è uno dei problemi grafici più importanti dal punto di vista pratico.
### Algoritmo di Dijkstra
Trova i percorsi più brevi da una singola sorgente a tutti gli altri vertici in un grafico con pesi dei bordi **non negativi**.
| Immobile | Valore |
|----------|-------|
| Pesi dei bordi | Deve essere ≥ 0 |
| Tempo (heap binario) | O((V + E)logV) |
| Tempo (heap di Fibonacci) | O(E + V log V) |
| Avido? | Sì |
| Gestisce i pesi negativi? | No |
**Algoritmo:**
1. Inizializza dist[s] = 0, dist[v] = ∞ per tutti v ≠ s. Coda prioritaria Q con tutti i vertici.
2. Mentre Q non è vuoto: estrai il vertice u con dist minima. Per ogni vicino v di u con peso del bordo w: se dist[u] + w < dist[v], aggiorna dist[v] = dist[u] + w.
**Esempio realizzato:**```
Graph: A --1-- B --2-- C --1-- D
       A --4-- C
       B --1-- D

Shortest paths from A:
A → B: 1 (direct)
A → D: 2 (A→B→D)
A → C: 3 (A→B→C, NOT A→C=4)
```

### Algoritmo di Bellman-Ford
Gestisce i pesi dei bordi **negativi** e rileva i cicli negativi.
| Immobile | Valore |
|----------|-------|
| Pesi dei bordi | Qualsiasi (rileva cicli negativi) |
| Complessità temporale | O(V · E) |
| Complessità spaziale | O(V) |
| Gestisce i cicli negativi? | Sì (rileva e segnala) |
**Algoritmo:**
1. Inizializza dist[s] = 0, dist[v] = ∞ per tutti v ≠ s.
2. Ripeti V − 1 volte: per ogni arco (u, v) con peso w: se dist[u] + w < dist[v], aggiorna dist[v].
3. Controllare i cicli negativi: se qualche bordo può ancora essere rilassato, esiste un ciclo negativo.
### Algoritmo di Floyd-Warshall
Trova i percorsi più brevi tra **tutte le coppie** di vertici.
| Immobile | Valore |
|----------|-------|
| Complessità temporale | O(V³) |
| Complessità spaziale | O(V²) |
| Gestisce i pesi negativi? | Sì (ma non cicli negativi) |
| Avvicinamento | Programmazione dinamica |
**Ricorrenza:** dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) per ogni vertice intermedio k.
### Guida alla selezione dell'algoritmo
| Scenario | Algoritmo |
|----------|-----------|
| Fonte unica, pesi non negativi | Dijkstra |
| Fonte unica, possibili pesi negativi | Bellman-Ford |
| Tutte le coppie, grafico denso | Floyd-Warshall |
| Tutte le coppie, grafico sparso | Esegui Dijkstra da ogni vertice |
| Grafico non ponderato | BFS |
| DAG (nessun ciclo) | Ordinamento topologico + rilassamento |
| A* (guidato euristica) | A* ricerca (per l'individuazione del percorso con una buona euristica) |
---

## Alberi di copertura minimi
Un **albero di copertura minimo (MST)** collega tutti i vertici con un peso totale minimo del bordo.
### Proprietà
- Un MST ha esattamente n − 1 archi (per n vertici)
- Esiste un MST se e solo se il grafico è connesso
- Un grafico con pesi degli spigoli distinti ha un MST unico
- MST soddisfa la **proprietà del taglio**: il bordo di peso minimo che attraversa qualsiasi taglio appartiene al MST
- MST soddisfa la **proprietà del ciclo**: il fronte di peso massimo in qualsiasi ciclo non appartiene al MST
### Algoritmo di Kruskal
| Immobile | Valore |
|----------|-------|
| Strategia | Goloso: aggiungi i bordi in ordine di peso |
| Struttura dei dati | Insieme disgiunto (unione-trova) |
| Complessità temporale | O(E log E) |
| Ideale per | Grafici sparsi |
**Algoritmo:**
1. Ordina tutti i bordi in base al peso.
2. Per ogni bordo (in ordine): se aggiungendolo non crea un ciclo (controlla con union-find), aggiungilo a MST.
3. Arresta quando vengono selezionati n − 1 bordi.
### Algoritmo di Prim
| Immobile | Valore |
|----------|-------|
| Strategia | Greedy: fai crescere l'albero da un vertice iniziale |
| Struttura dei dati | Coda prioritaria (heap minimo) |
| Complessità temporale | O(E log V) con heap binario |
| Ideale per | Grafici densi |
**Algoritmo:**
1. Inizia da qualsiasi vertice. Contrassegnalo come parte del MST.
2. Aggiungere ripetutamente il bordo di peso minimo che collega un vertice nel MST a un vertice esterno ad esso.
3. Fermarsi quando tutti i vertici sono inclusi.
### Applicazioni MST
| Applicazione | Come aiuta MST |
|-------------|-------|
| Progettazione della rete | Posare un minimo di cavi/tubi per collegare tutte le posizioni |
| Clustering | Rimuovi i k − 1 archi MST più lunghi per ottenere k cluster |
| Algoritmi di approssimazione | 2-approssimazione per la metrica TSP |
| Segmentazione delle immagini | Raggruppare i pixel per MST di somiglianza cromatica |
| Eliminazione delle funzionalità | Rimuovere le funzionalità ridondanti utilizzando MST del grafico di correlazione |
---

## Flusso di rete
I problemi di flusso di rete modellano il movimento delle risorse attraverso un sistema.
### Definizione della rete di flusso
Una **rete di flusso** è un grafico diretto con:
- A **sorgente** vertice s (produce flusso)
- A **sink** vertice t (consuma flusso)
- **Capacità** c(u,v) ≥ 0 su ciascun bordo
- **Flusso** f(u,v) soddisfacente:
  - **Vincolo di capacità:** 0 ≤ f(u,v) ≤ c(u,v)
  - **Conservazione del flusso:** flusso in entrata = flusso in uscita ad ogni vertice eccetto s e t
### Problema di flusso massimo
Trovare il flusso totale massimo da s a t.
**Metodo Ford-Fulkerson:**
1. Sebbene esista un cammino aumentante da s a t nel grafo residuo:
2. Trova la capacità del collo di bottiglia lungo il percorso
3. Aumentare il flusso lungo il percorso in misura corrispondente al collo di bottiglia
4. Aggiornare le capacità residue
| Algoritmo | Complessità temporale | Note |
|-----------|----------------|-------|
| Ford-Fulkerson (DFS) | O(m · f*) dove f* è la portata massima | Non può terminare con capacità irrazionali |
| Edmonds-Karp (BFS) | O(V · E²) | Termina sempre, sceglie il percorso aumentante più breve |
| Algoritmo di Dinic | O(V² · E) | Utilizza il blocco dei flussi; O(V^(1/2) · E) per le capacità unitarie |
### Teorema del taglio minimo del flusso massimo
Il **flusso massimo** da s a t è uguale alla capacità di **taglio minimo** che separa s da t.
A **taglio** (S, T) suddivide i vertici in S (contenente s) e T (contenente t). La capacità di taglio è la somma delle capacità dei bordi da S a T.
**Applicazioni di portata massima:**
- Abbinamento bipartito (assegnare i lavoratori ai lavori)
- Segmentazione delle immagini (separare il primo piano dallo sfondo)
- Eliminazione nel baseball (la squadra X può ancora vincere?)
- Affidabilità della rete (massimo throughput dati)
### Corrispondenza bipartita tramite flusso massimo
Dato un grafo bipartito G = (L ∪ R, E):
1. Aggiungi sorgenti con bordi a tutti i vertici in L (capacità 1)
2. Aggiungi sink t con bordi da tutti i vertici in R (capacità 1)
3. Impostare tutte le capacità dei bordi originali su 1
4. Portata massima = corrispondenza massima
---

## Teoria dei grafici spettrali
La teoria dei grafi spettrali studia i grafi attraverso gli autovalori e gli autovettori delle matrici associate al grafo.
### Matrici chiave
| Matrice | Definizione | Cosa cattura |
|--------|------------|------------|
| **Matrice di adiacenza** A | A[i][j] = 1 se esiste l'arco (i,j) | Modello di connettività |
| **Matrice dei titoli** D | Diagonale; D[i][i] = gradi(i) | Importanza dei vertici per grado |
| **Laplaciano** L = D − A | L[i][j] = −1 se spigolo, deg(i) sulla diagonale | Fluidità delle funzioni sul grafico |
| **Laplaciano normalizzato** L_norm = D^(−1/2) L D^(−1/2) | Versione invariante di scala | Struttura comunitaria |
### Autovalori del Laplaciano
Il laplaciano L è semidefinito positivo, quindi tutti gli autovalori sono ≥ 0.
| Autovalore | Significato |
|------------|---------|
| λ₁ = 0 | Sempre zero; l'autovettore è il vettore costante |
| λ₂ (connettività algebrica) | > 0 se e solo se il grafico è connesso; più grande = meglio connesso |
| Numero di autovalori nulli | Uguale al numero di componenti collegati |
| λₙ | Relativo al grado massimo e all'espansione del grafico |
### Applicazioni dei metodi spettrali
| Applicazione | Metodo |
|-------------|--------|
| **Partizionamento del grafico** | Utilizzare gli autovettori di L per dividere il grafico in parti bilanciate |
| **Rilevamento della comunità** | Clustering spettrale: incorpora i vertici utilizzando gli autovettori inferiori, quindi cluster |
| **PageRank** | Autovettore della matrice di adiacenza (o matrice di transizione) del grafo web |
| **Disegno grafico** | Posizionare i vertici utilizzando gli autovettori del Laplaciano |
| **Apprendimento semi-supervisionato** | Propagare le etichette utilizzando il grafo Laplaciano (propagazione delle etichette) |
| **Reti neurali a grafo** | Convoluzioni spettrali: filtrare i segnali sui grafici utilizzando autovettori di L |
### Disuguaglianza di Cheeger
Mette in relazione il secondo autovalore λ₂ con l'**espansione** del grafico (quanto è ben connesso):
λ₂ / 2 ≤ h(G) ≤ √(2λ₂)
dove h(G) è la costante di Cheeger (numero isoperimetrico). Ciò significa che λ₂ misura approssimativamente quanto sia difficile dividere il grafico in due parti: un aspetto fondamentale per il clustering.
---

## Strutture grafiche speciali
| Grafico | Vertici | Bordi | Proprietà |
|-------|----------|-------|------------|
| Completa Kₙ | n | n(n−1)/2 | Ogni coppia collegata; diametro 1|
| Ciclo Cₙ | n | n | 2-regolare; connesso |
| Sentiero Pₙ | n | n−1 | Albero; diametro n−1 |
| Ipercubo Qₖ | 2ᵏ | k·2ᵏ⁻¹ | k-regolare; diametrok; bipartito |
| Bipartito completo K_{m,n} | m+n | m·n | Ogni vertice in una parte si collega a tutti nell'altra |
| Grafico di Petersen | 10| 15| 3-regolare; diametro 2; non planare; nessun ciclo hamiltoniano |
---

## Rilevanza per l'apprendimento automatico e la scienza dei dati
| Concetto di grafico | Applicazione |
|---------------|-------------|
| BFS/DFS | Web crawling, analisi dei social network, etichettatura dei componenti connessi |
| Dijkstra / A* | Pianificazione del percorso, individuazione del percorso tramite intelligenza artificiale del gioco, navigazione robotica |
| Albero di copertura minimo | Clustering (collegamento singolo), selezione delle funzionalità, progettazione della rete |
| Portata massima/taglio minimo | Segmentazione delle immagini, corrispondenza bipartita, assegnazione dei consigli |
| Metodi spettrali | Clustering spettrale, reti neurali a grafo, riduzione della dimensionalità (automappe laplaciane) |
| PageRank | Posizionamento nei motori di ricerca, analisi dell'influenza nei social network |
| DAG | Reti bayesiane, inferenza causale, pianificazione delle attività, grafici di calcolo nel deep learning |
| Grafi bipartiti | Matrici di articoli utente nei sistemi di raccomandazione, mercati a due facce |
| Strutture ad albero | Alberi decisionali, foreste casuali, clustering gerarchico, navigazione nel file system |
| Rappresentazioni grafiche | Grafici della conoscenza (Wikidata, DBpedia), grafici molecolari (scoperta di farmaci), reti di citazioni |
---

## Riepilogo
| Argomento | Idea fondamentale | Algoritmo chiave / Risultato |
|-------|-----------|----------------------|
| Fondamenti | Vertici, spigoli, gradi, traiettorie | Lemma della stretta di mano |
| Rappresentazioni | Come memorizzare i grafici | Matrice di adiacenza vs lista di adiacenza |
| Alberi | Grafi aciclici connessi | n vertici → n−1 spigoli |
| Traversate | Esplorazione sistematica dei vertici | BFS (percorso più breve), DFS (esplorazione profonda) |
| Percorsi più brevi | Rotte a peso minimo | Dijkstra, Bellman-Ford, Floyd-Warshall |
| Albero di copertura minimo | Il modo più economico per connettere tutti i vertici | Di Kruskal, di Prim |
| Flusso di rete | Produttività massima | Ford-Fulkerson, teorema del taglio minimo del flusso massimo |
| Teoria spettrale | Gli autovalori rivelano la struttura | Autovalori laplaciani, clustering spettrale |
La teoria dei grafi è probabilmente il ramo della matematica più direttamente applicabile alla moderna scienza dei dati. Social network, grafi della conoscenza, strutture molecolari, grafi di calcolo in strutture di deep learning, risoluzione delle dipendenze, sistemi di raccomandazione: sono tutti fondamentalmente problemi di grafi. Gli algoritmi qui trattati non sono solo teorici; vengono eseguiti su larga scala nei sistemi di produzione ogni giorno.