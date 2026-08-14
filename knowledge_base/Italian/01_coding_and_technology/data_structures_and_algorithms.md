---
# Metadata
title: "Data Structures and Algorithms"
description: "Arrays, trees, graphs, sorting, searching, complexity"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, structures, algorithms, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Strutture dati e algoritmi
Le strutture dati sono il modo in cui organizziamo i dati in memoria in modo che le operazioni su di essi siano efficienti. Gli algoritmi sono le procedure passo passo per la risoluzione dei problemi. Insieme, costituiscono le fondamenta dell'informatica: ogni programma che tu abbia mai utilizzato si basa su di loro. Scegliere la giusta struttura dati può trasformare un programma incredibilmente lento in uno veloce, e conoscere l’algoritmo giusto può trasformare un problema irrisolvibile in un problema banale.
---

## Strutture dati fondamentali
### Strutture lineari
| Struttura | Accesso | Cerca | Inserisci | Elimina | Caso d'uso |
|-----------|--------|--------|--------|--------|----------|
| **Array** | O(1) per indice | O(n) | O(n) | O(n) | Collezioni a dimensione fissa; accesso casuale |
| **Elenco collegato** | O(n) | O(n) | O(1) in testa | O(1) in testa | dimensione dinamica; inserimenti/eliminazioni |
| **Pila** | O(n) | O(n) | O(1) spingi/pop | O(1) pop | Chiamate di funzioni; disfare; analisi |
| **Coda** | O(n) | O(n) | O(1) accodare | O(1) rimozione dalla coda | Pianificazione delle attività; BFS; code di messaggi |
| **Deque** | O(1) ad entrambe le estremità | O(n) | O(1) ad entrambe le estremità | O(1) ad entrambe le estremità | Finestra scorrevole; furto di lavoro |
### Strutture basate su hash
| Struttura | Cerca | Inserisci | Elimina | Caso d'uso |
|-----------|--------|--------|--------|----------|
| **Tabella hash** | O(1) media | O(1) media | O(1) media | Ricerche di valori-chiave; cache; imposta |
| **Set di hash** | O(1) | O(1) | O(1) | Test di adesione; deduplicazione |
**Collisioni hash**: quando due chiavi si inseriscono nello stesso slot, vengono archiviate in un elenco collegato (concatenamento) o nel successivo slot disponibile (indirizzamento aperto). Buone funzioni hash riducono al minimo le collisioni.
### Strutture ad albero
| Struttura | Cerca | Inserisci | Elimina | Caso d'uso |
|-----------|--------|--------|--------|----------|
| **Albero di ricerca binaria** | O(log n) media | O(log n) | O(log n) | Dati ordinati; query di intervallo |
| **AVL / Albero Rosso-Nero** | O(log n) garantito | O(log n) | O(log n) | Autobilanciamento; utilizzato in mappe/set |
| **Albero B / Albero B+** | O(log n) | O(log n) | O(log n) | Indici di banche dati; file system |
| **Prova** | O(k) dove k = lunghezza della chiave | O(k) | O(k) | Completamento automatico; corrispondenza del prefisso |
| **Heap (binario)** | O(n) | O(log n) | O(log n) | Code prioritarie; programmazione |
### Rappresentazioni grafiche
| Rappresentanza | Spazio | Ricerca bordi | Aggiungi bordo | Iterare i vicini |
|---------------|-------|-----|----------|-----|
| **Matrice di adiacenza** | O(V²) | O(1) | O(1) | O(V) |
| **Elenco adiacenze** | O(V + E) | O(grado) | O(1) | O(grado) |
| **Elenco bordi** | O(E) | O(E) | O(1) | O(E) |
---

## Complessità dell'algoritmo (Big-O)
La notazione Big-O descrive come i requisiti di tempo o spazio di un algoritmo crescono all'aumentare della dimensione dell'input.
| Complessità | Nome | Esempio |
|-----------|------|---------|
| **O(1)** | Costante | Ricerca nella tabella hash; accesso all'array tramite indice |
| **O(log n)** | Logaritmico | Ricerca binaria; operazioni sull'albero equilibrato |
| **O(n)** | Lineare | Ricerca lineare; iterando un array |
| **O(n log n)** | Linearitmica | Unisci ordinamento; ordinamento dell'heap; tipi generici più efficienti |
| **O(n²)** | Quadratico | Ordinamento delle bolle; cicli nidificati sugli stessi dati |
| **O(2^n)** | Esponenziale | Generazione di sottoinsiemi di forza bruta; ingenuo ricorsivo Fibonacci |
| **O(n!)** | Fattoriale | Venditore ambulante (forza bruta); permutazioni |
### Idee sbagliate comuni
| Idea sbagliata | Realtà |
|--------------|---------|
| "O(n) è sempre più veloce di O(n²)" | Per n piccolo, il fattore costante conta di più |
| "Lower Big-O è sempre meglio" | Esistono compromessi spazio-temporali; La ricerca O(1) utilizza la memoria O(n) |
| "Big-O ti dice la velocità esatta" | Descrive il tasso di crescita, non il tempo assoluto |
---

## Algoritmi di ordinamento
| Algoritmo | Migliore | Nella media | Peggiore | Spazio | Stabile | Sul posto |
|-----------|------|---------|-------|-------|--------|----------|
| **Ordinamento bolle** | O(n) | O(n²) | O(n²) | O(1) | Sì | Sì |
| **Ordinamento inserimento** | O(n) | O(n²) | O(n²) | O(1) | Sì | Sì |
| **Ordinamento selezione** | O(n²) | O(n²) | O(n²) | O(1) | No | Sì |
| **Unisci ordinamento** | O(n log n) | O(n log n) | O(n log n) | O(n) | Sì | No |
| **Ordinamento rapido** | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Sì |
| **Ordinamento heap** | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Sì |
| **Tim Ordina** | O(n) | O(n log n) | O(n log n) | O(n) | Sì | No |
**Consiglio pratico**: usa l'ordinamento integrato nella tua lingua (`sorted()` di Python,`Array.sort()`di JavaScript). Usano algoritmi altamente ottimizzati (Tim Sort, Introsort) che gestiscono tutti i casi limite.
---

## Algoritmi di ricerca
| Algoritmo | Struttura dei dati | Complessità | Requisito |
|-----------|---------------|------------|-----|
| **Ricerca lineare** | Qualsiasi | O(n) | Nessuno |
| **Ricerca binaria** | Array ordinato | O(log n) | I dati devono essere ordinati |
| **Ricerca nella tabella hash** | Tabella hash | O(1) media | Buona funzione hash |
| **BFS** (Ricerca in ampiezza) | Grafico/albero | O(V + E) | Percorso più breve non ponderato |
| **DFS** (Ricerca approfondita) | Grafico/albero | O(V + E) | Ricerca del percorso; rilevamento del ciclo |
| **Dijkstra** | Grafico ponderato | O((V + E)logV) | Pesi non negativi; percorso più breve |
| **A* Cerca** | Grafico ponderato | O((V + E)logV) | Guidato euristica; ottimo con euristica ammissibile |
---

## Modelli di algoritmi chiave
| Modello | Descrizione | Problemi di esempio |
|---------|-------------|-----------------|
| **Dividi e conquista** | Suddividere il problema in sottoproblemi; risolvere ricorsivamente; combinare | Unisci ordinamento; ordinamento rapido; ricerca binaria |
| **Programmazione dinamica** | Suddividere in sottoproblemi sovrapposti; risultati nella cache | Fibonacci; zaino; sottosuccessione comune più lunga |
| **Goloso** | Effettuare la scelta ottimale a livello locale in ogni fase | quello di Dijkstra; Codifica di Huffman; selezione attività |
| **Fare marcia indietro** | Prova le possibilità; annullare le scelte sbagliate; provare alternative | Risolutore di sudoku; N-regine; permutazioni |
| **Finestra scorrevole** | Mantenere una finestra di elementi; farlo scorrere attraverso i dati | Sottoarray di somma massima di dimensione K; sottostringa più lunga senza ripetizioni |
| **Due puntatori** | Utilizza due puntatori che si muovono l'uno verso l'altro o nella stessa direzione | Somma delle coppie nell'array ordinato; rimuovere i duplicati |
| **Ricerca binaria sulla risposta** | Ricerca binaria nello spazio delle risposte | Assegnare un numero minimo di pagine; mucche aggressive |
---

## Quando usare cosa
| Problema | Struttura dei dati | Algoritmo |
|---------|---------------|-----------|
| Ricerca rapida del valore-chiave | Tabella hash/dizionario | Hashing |
| Mantieni l'ordine | BST bilanciato (TreeMap, std::set) | Operazioni sugli alberi |
| Elaborazione basata sulla priorità | Heap/coda prioritaria | Operazioni sull'heap |
| Percorso più breve (non ponderato) | Grafico (lista di adiacenze) | BFS |
| Percorso più breve (ponderato) | Grafico (lista di adiacenze) | Dijkstra / A* |
| Test di adesione | Set hash / filtro Bloom | Hashing |
| Corrispondenza prefisso | Prova | Prova attraversamento |
| Intervalli di query | Albero di segmento / albero di Fenwick | Operazioni sugli alberi |
| Cache LRU | Mappa hash + elenco doppiamente collegato | Operazioni combinate |
| Componenti collegati | Unione di insiemi disgiunti (Unione-Trova) | Unione e Trova |
---

## Riepilogo
Le strutture dei dati e gli algoritmi non sono solo argomenti di interviste: sono gli elementi costitutivi di un software efficiente. Array e tabelle hash gestiscono la maggior parte delle esigenze quotidiane. Alberi e grafici gestiscono dati gerarchici e relazionali. L'ordinamento e la ricerca sono problemi risolti nelle librerie standard. I modelli algoritmici – divide et impera, programmazione dinamica, greedy, backtracking – sono strategie riutilizzabili per affrontare nuovi problemi. L'abilità chiave non è memorizzare gli algoritmi; significa riconoscere quale modello si adatta a un determinato problema e scegliere la struttura dati giusta per il lavoro.