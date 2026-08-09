---
# Metadata
title: "Graph Neural Networks"
description: "GCNs, GATs, message passing, knowledge graphs, graph tasks"
category: "AI and Machine Learning"
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
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [graph, neural, networks, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Grafico delle reti neurali
Le reti neurali a grafo (GNN) sono reti neurali progettate per operare su dati strutturati a grafo: reti di nodi collegati da bordi. Mentre le reti neurali tradizionali funzionano su griglie (immagini) o sequenze (testo), le GNN gestiscono strutture relazionali arbitrarie: social network, grafici molecolari, grafici della conoscenza, reti stradali, grafici delle raccomandazioni e altro ancora. Sono diventati essenziali per la scoperta di farmaci, il rilevamento di frodi, i sistemi di raccomandazione e qualsiasi ambito in cui le relazioni tra entità contano.
---

## Cos'è un grafico?
| Componente | Descrizione | Esempio |
|-----------|-------------|---------|
| **Nodo (vertice)** | Un'entità | Una persona, l'atomo di una molecola, una città |
| **Bordo** | Una relazione tra due nodi | Amicizia, legame chimico, strada |
| **Peso del bordo** | Forza o tipo di relazione | Distanza, somiglianza, capacità |
| **Caratteristiche del nodo** | Attributi di ciascun nodo | Età, numero atomico, popolazione |
| **Caratteristiche del bordo** | Attributi di ciascun bordo | Tipo di relazione, distanza |
| **Matrice di adiacenza** | Matrice A dove A[i][j] = 1 se i nodi i e j sono connessi | Codifica la struttura del grafico |
### Tipi di grafici
| Digitare | Descrizione | Esempio |
|------|-------------|---------|
| **Non diretto** | I bordi non hanno direzione | Rete di amicizia |
| **Diretto** | I bordi hanno direzione (A→B ≠ B→A) | Seguaci di Twitter |
| **Ponderato** | I bordi hanno valori numerici | Rete stradale con distanze |
| **Eterogeneo** | Tipi multipli di nodi e bordi | Grafico accademico (articoli, autori, luoghi) |
| **Dinamico** | La struttura del grafico cambia nel tempo | Social network in evoluzione nel tempo |
| **Bipartito** | Due tipi di nodi; bordi solo tra i tipi | Grafico dei consigli sugli articoli utente |
---

## Perché non le reti neurali regolari?
| Avvicinamento | Perché fallisce |
|----------|-------------|
| **Rete feed-forward** | Richiede input di dimensione fissa; i grafici variano in dimensioni e struttura |
| **CNN** | Presuppone una struttura a griglia; i grafici non hanno una griglia regolare |
| **RNN/Trasformatore** | Presuppone l'ordine sequenziale; i grafici non hanno un ordinamento naturale |
Le GNN risolvono questo problema operando direttamente sulla struttura del grafo, elaborando ciascun nodo nel contesto dei suoi vicini.
---

## Architetture GNN principali
### Struttura per il passaggio dei messaggi
La maggior parte delle GNN seguono lo stesso schema: ogni nodo raccoglie informazioni dai suoi vicini, le combina e aggiorna la propria rappresentazione.
| Passo | Descrizione |
|------|-------------|
| **1. Messaggio** | Ogni nodo invia un messaggio ai suoi vicini (in base alle sue caratteristiche attuali) |
| **2. Aggregato** | Ogni nodo raccoglie e combina i messaggi di tutti i vicini |
| **3. Aggiornamento** | Ogni nodo aggiorna la propria rappresentazione utilizzando il messaggio aggregato |
| **4. Ripeti** | Fallo per K livelli → ogni nodo cattura informazioni da K salti di distanza |
### Principali modelli GNN
| Modello | Metodo di aggregazione | Innovazione chiave |
|-------|-----|----------------|
| **GCN** (Rete convoluzionale del grafico) | Media delle caratteristiche del vicino | Semplice; efficace; motivazione spettrale |
| **GraficoSAGE** | Campionare e aggregare; può utilizzare mean, LSTM o pooling | Induttivo (gestisce i nodi invisibili); scalabile |
| **GAT** (Rete di attenzione del grafico) | Aggregazione dei vicini ponderata per l'attenzione | Impara quali vicini contano di più |
| **GIN** (Rete di isomorfismo del grafico) | Somma delle caratteristiche vicine | Massimamente espressivo; può distinguere qualsiasi grafico distinguibile dal test WL |
| **MPNN** (Rete neurale che trasmette messaggi) | Quadro generale per lo scambio di messaggi | Unifica molte varianti GNN |
### Come funziona GCN (passo dopo passo)
```
For each layer:
  1. For each node, collect features from all neighbours
  2. Multiply by a learnable weight matrix W
  3. Normalise by node degree (so high-degree nodes don't dominate)
  4. Apply non-linearity (ReLU)
  5. This becomes the node's new representation
```

Dopo K livelli, la rappresentazione di ciascun nodo codifica le informazioni provenienti da K salti nel grafico.
---

## Attività a livello di grafico
| Compito | Descrizione | Esempio |
|------|-------------|---------|
| **Classificazione dei nodi** | Prevedere l'etichetta di ciascun nodo | Classificare gli utenti come bot o umani |
| **Previsione del collegamento** | Prevedere se un bordo esiste (o esisterà) | Prevedere le relazioni mancanti; consigliare collegamenti |
| **Classificazione grafica** | Prevedere un'etichetta per l'intero grafico | Classificare le molecole come tossiche o non tossiche |
| **Rilevamento della comunità** | Trova cluster di nodi densamente connessi | Identificare i gruppi sociali |
| **Generazione di grafici** | Genera nuovi grafici con le proprietà desiderate | Progettare nuove molecole |
---

## Applicazioni
### Scoperta di farmaci e previsione delle proprietà molecolari
| Compito | Come aiutano le GNN |
|------|--------------|
| **Previsione delle proprietà molecolari** | Rappresentare le molecole come grafici (atomi=nodi, legami=spigoli); prevedere tossicità, solubilità, affinità di legame |
| **Interazione farmaco-farmaco** | Modellare farmaci e obiettivi come un grafico; prevedere le interazioni avverse |
| **Progettazione di farmaci de novo** | Genera nuovi grafici molecolari con le proprietà desiderate |
### Sistemi di raccomandazione
| Avvicinamento | Descrizione |
|----------|-------------|
| **Grafico elementi utente** | Gli utenti e gli elementi sono nodi; acquisti/visualizzazioni sono bordi |
| **Filtro collaborativo basato su grafici** | I GNN propagano le preferenze attraverso il grafico |
| **Consigli sul grafico della conoscenza** | Combina le preferenze dell'utente con la conoscenza dell'oggetto (generi, attori, registi) |
### Rilevamento delle frodi
| Applicazione | Struttura del grafico |
|-------------|----------------|
| **Frode finanziaria** | Le transazioni formano un grafico; modelli fraudolenti emergono come strutture di sottografi |
| **Frode assicurativa** | Richiedenti, fornitori e politiche formano un grafico; vengono rilevate reti di truffatori |
| **Acquisizioni di conti** | I modelli di accesso formano un grafico; connessioni anomale segnalano compromissione |
### Grafici della conoscenza
| Compito | Descrizione |
|------|-------------|
| **Previsione del collegamento** | Prevedere i fatti mancanti (ad esempio, "Parigi è la capitale di?") |
| **Delibera dell'ente** | Determina se due menzioni si riferiscono alla stessa entità |
| **Risposta alla domanda** | Naviga nel grafico per trovare le risposte |
---

## Concetti avanzati GNN
### Levigatura eccessiva
| Problema | Descrizione | Soluzione |
|---------|-------------|----------|
| **Levigatura eccessiva** | Dopo molti strati, tutte le rappresentazioni dei nodi diventano simili | Profondità limite (2-4 strati); utilizzare connessioni residue; usa la conoscenza del salto |
### Schiacciamento eccessivo
| Problema | Descrizione | Soluzione |
|---------|-------------|----------|
| **Sovraschiacciamento** | Le informazioni provenienti da nodi distanti vengono compresse in vettori di dimensione fissa | Utilizzare trasformatori grafici; raggruppamento gerarchico |
### Trasformatori di grafici
| Modello | Caratteristica fondamentale |
|-------|-------------|
| **Trasformatore grafico** | Applicare l'attenzione standard del Transformer a tutte le coppie di nodi |
| **GPS** (sistema di guida grafica) | Combina i livelli GNN locali con i livelli Transformer globali |
| **Gragrafo** | Aggiungi la codifica posizionale basata sulla struttura del grafico |
### Reti di grafi eterogenei
| Modello | Descrizione |
|-------|-------------|
| **R-GCN** | GCN relazionale; matrici di peso diverse per diversi tipi di bordo |
| **HAN** | Rete di attenzione eterogenea; attenzione sui diversi tipi di nodi e bordi |
| **HetGNN** | Rete neurale a grafico eterogeneo; gestisce più tipi di nodo |
---

## Scalabilità
| Sfida | Soluzione |
|-----------|----------|
| **Grafici di grandi dimensioni** (milioni di nodi) | Formazione in minibatch; campionamento del vicino |
| **Memoria** | Partizionamento dei grafici tra GPU |
| **Velocità** | Operazioni su matrici sparse; biblioteche specializzate |
### Strategie di campionamento
| Strategia | Descrizione |
|----------|-------------|
| **Campionamento dei nodi** | Campiona un sottoinsieme di nodi e i loro quartieri K-hop |
| **Campionamento dei bordi** | Bordi campione e nodi che collegano |
| **Campionamento cluster** | Partizionare il grafico in cluster; allenarsi sui cluster |
| **Campionamento casuale della passeggiata** | Nodi campione tramite passeggiate casuali dai nodi target |
---

## Strumenti e framework
| Strumento | Scopo |
|------|---------|
| **PyTorch geometrico (PyG)** | Libreria GNN più popolare; ricco set di modelli e set di dati |
| **DGL** (Libreria di grafici profondi) | Indipendente dal contesto; supporta PyTorch, TensorFlow, MXNet |
| **ReteX** | Algoritmi grafici classici; manipolazione dei dati |
| **OGB** (Benchmark del grafico aperto) | Benchmark e set di dati standard per la ricerca sulla GNN |
| **CogDL** | Apprendimento profondo per i grafici; orientato alla ricerca |
| **Spettacolare** | Libreria GNN per TensorFlow/Keras |
---

## Riepilogo
Le reti neurali a grafo estendono il deep learning ai dati relazionali: reti, molecole, grafici della conoscenza e qualsiasi sistema in cui le entità sono connesse. Funzionano trasmettendo messaggi tra vicini, consentendo a ciascun nodo di imparare dal suo contesto locale. Le GNN hanno trovato le loro applicazioni più efficaci nella scoperta di farmaci, nei sistemi di raccomandazione, nel rilevamento delle frodi e nei grafici della conoscenza. Il campo si sta evolvendo verso trasformatori di grafici, grafici eterogenei e formazione scalabile per enormi reti del mondo reale. Se i tuoi dati hanno relazioni, probabilmente vale la pena considerare i GNN.