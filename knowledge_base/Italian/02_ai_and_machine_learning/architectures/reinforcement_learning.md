<!--
---
# Metadata
title: "Reinforcement Learning"
description: "MDPs, Q-learning, policy gradients, RLHF, multi-agent systems"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to architectures/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [reinforcement, learning, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Apprendimento per rinforzo
L'apprendimento per rinforzo (RL) è il modo in cui le macchine imparano a prendere sequenze di decisioni attraverso tentativi ed errori. A differenza dell’apprendimento supervisionato, in cui viene fornita la risposta corretta per ogni esempio, RL fornisce all’agente solo un segnale di ricompensa e l’agente deve capire quali azioni portano ai migliori risultati nel tempo. È l'approccio alla base di AlphaGo, del controllo robotico, dell'intelligenza artificiale di gioco e, in modo critico, dell'RLHF, la tecnica utilizzata per allineare i moderni modelli linguistici di grandi dimensioni con le preferenze umane.
---

## Concetti fondamentali
RL inquadra il processo decisionale come un anello tra un **agente** e un **ambiente**.
| Componente | Ruolo | Esempio |
|-----------|------|---------|
| **Agente** | Il decisore | Un programma di scacchi, un robot, un modello linguistico |
| **Ambiente** | Il mondo con cui interagisce l'agente | La scacchiera, un magazzino, una conversazione |
| **Stato** | La situazione attuale | Posizione della scheda, letture dei sensori del robot, cronologia chat |
| **Azione** | Cosa può fare l'agente | Muovi un pezzo, gira a sinistra, genera un gettone |
| **Ricompensa** | Segnale di feedback (numero scalare) | +1 per vincere, -1 per schiantarsi, punteggio di preferenza umana |
| **Politica** | La strategia mappa gli stati in azioni | "Se il re è minacciato, spostatelo" |
| **Funzione valore** | Ricompensa cumulativa prevista da uno Stato | "Questa posizione nel tabellone vale circa +3 punti" |
### Il ciclo RL
```
Agent observes State → chooses Action → Environment returns new State + Reward
        ↑                                                                         |
        └─────────────────────────────────────────────────────────────────────────┘
```

L'obiettivo dell'agente è massimizzare la **ricompensa cumulativa** nel tempo, non solo la ricompensa immediata. Questo è ciò che rende l’RL fondamentalmente diverso dall’apprendimento supervisionato.
---

## Differenze chiave rispetto ad altri paradigmi di apprendimento
| Aspetto | Apprendimento supervisionato | Apprendimento non supervisionato | Apprendimento per rinforzo |
|--------|-------------|----------------------|----------------------|
| **Segnale** | Etichette corrette per ogni esempio | Nessuna etichetta; trova struttura | Ricompensa scalare, spesso ritardata |
| **Feedback** | Immediato | Nessuno | Ritardato e scarso |
| **Sequenza** | Ogni esempio è indipendente | Ogni esempio è indipendente | Le azioni influenzano gli stati futuri |
| **Gol** | Ridurre al minimo l'errore di previsione | Scopri i modelli | Massimizza la ricompensa cumulativa |
---

## Processi decisionali di Markov (MDP)
Gli MDP sono la struttura matematica per RL. Presumono che il futuro dipenda solo dallo stato attuale, non dalla storia di come ci sei arrivato (la **proprietà di Markov**).
| Componente | Notazione | Significato |
|-----------|----------|---------|
| **Stati** | S | Tutte le possibili situazioni in cui può trovarsi l'agente |
| **Azioni** | A | Tutte le cose che l'agente può fare |
| **Funzione di transizione** | P(s' \| s, a) | Probabilità di raggiungere gli stati s' dopo aver intrapreso l'azione a nello stato s |
| **Funzione premio** | R(s, a, s') | Ricompensa ricevuta per la transizione |
| **Fattore di sconto** | γ (gamma) | Quanto valutare le ricompense future rispetto a quelle immediate (da 0 a 1) |
Il **reso** (premio totale scontato) è:
```
G = R₁ + γR₂ + γ²R₃ + ...
```

Un fattore di sconto elevato (γ prossimo a 1) indica che l'agente è lungimirante. Uno basso significa che è miope.
---

## Algoritmi RL classici
### Metodi basati sul valore
Questi apprendono quanto è buono ogni stato (o coppia stato-azione).
| Algoritmo | Idea chiave | Limitazione |
|-----------|----------|------------|
| **Q-Learning** | Impara una tabella di valori Q: Q(stato, azione) = ricompensa attesa | Non si adatta a spazi di stato di grandi dimensioni |
| **Rete Q profonda (DQN)** | Utilizzare una rete neurale per approssimare i valori Q | Gestisce solo azioni discrete; può essere instabile |
| **DQN doppio** | Correggi il bias di sovrastima di Q-learning | Ancora limitato ad azioni discrete |
Regola di aggiornamento Q-learning:
```
Q(s, a) ← Q(s, a) + α [r + γ max Q(s', a') - Q(s, a)]
```

### Metodi basati su policy
Questi apprendono direttamente la politica (strategia) senza stimare i valori.
| Algoritmo | Idea chiave | Vantaggio |
|-----------|----------|-----------|
| **RAFFORZARE** | Gradiente politico di Monte Carlo; aggiornare la politica in direzione di buoni risultati | Semplice; funziona con azioni continue |
| **PPO** (Ottimizzazione della politica prossimale) | Ritaglia gli aggiornamenti delle policy per evitare modifiche di grandi dimensioni e destabilizzanti | Stabile; ampiamente utilizzato; buona impostazione predefinita |
| **TRPO** | Metodo della regione attendibile per gli aggiornamenti delle politiche | Più principi del PPO; più difficile da implementare |
### Metodi attore-critico
Combina il meglio di entrambi: un **attore** (politica) e un **critico** (funzione di valore).
| Algoritmo | Idea chiave |
|-----------|----------|
| **A2C / A3C** | Vantaggio attore-critico; utilizza la stima del vantaggio per ridurre la varianza |
| **SAC** (Attore-critico morbido) | Massimizzare la ricompensa mantenendo l'esplorazione (regolarizzazione dell'entropia) |
| **TD3** (DDPG doppio ritardato) | Affrontare la sovrastima negli spazi di azione continua |
---

## RLHF: Apprendimento per rinforzo dal feedback umano
RLHF è la tecnica che ha reso possibile ChatGPT. Colma il divario tra un modello in grado di prevedere il testo e uno che produce risultati che gli esseri umani trovano effettivamente utili.
### I tre passi
| Passo | Cosa succede | Uscita |
|------|-------------|--------|
| **1. Ottimizzazione supervisionata (SFT)** | Perfezionare un modello preaddestrato su esempi scritti da persone di alta qualità | Un modello che segue le istruzioni abbastanza bene |
| **2. Formazione sul modello di ricompensa** | Gli esseri umani confrontano coppie di risultati del modello; addestrare un modello per prevedere le preferenze umane | Un modello di ricompensa che assegna un punteggio alla qualità dell'output |
| **3. Ottimizzazione RL** | Utilizzare PPO per mettere a punto il modello SFT per massimizzare i punteggi del modello di ricompensa | Un modello allineato alle preferenze umane |
### Perché RLHF è importante
Senza RLHF, un modello linguistico è come uno studente che ha letto tutti i libri ma non sa come comportarsi in una conversazione. Può generare testo, ma il testo potrebbe essere inutile, tossico o non cogliere del tutto il punto. RLHF insegna al modello *cosa vogliono gli esseri umani*, non solo come appare il testo.
### Varianti e alternative
| Metodo | Descrizione | Vantaggio |
|--------|-------------|-----------|
| **DPO** (Ottimizzazione delle preferenze dirette) | Salta il modello di ricompensa; ottimizzare direttamente la politica a partire dalle preferenze umane | Più semplice; nessun modello di ricompensa separato da addestrare |
| **RLAIF** | Utilizzare l'intelligenza artificiale (anziché gli esseri umani) per generare etichette di preferenza | Più economico dell'etichettatura umana |
| **AI costituzionale** | Utilizzare una serie di principi per guidare il comportamento modello senza etichette umane | Più scalabile; L'approccio di Anthropic |
| **GRPO** (Ottimizzazione della politica relativa di gruppo) | Confrontare i risultati all'interno di un gruppo piuttosto che con un modello separato | Utilizzato in DeepSeek-R1; riduce la necessità di una rete di valore |
---

## Esplorazione vs sfruttamento
Questa è la tensione centrale in RL. **Sfruttamento** significa scegliere azioni che sai che funzionano bene. **Esplorazione** significa provare cose nuove per scoprire strategie potenzialmente migliori.
| Strategia | Come funziona | Scambio |
|----------|-------------|-----------|
| **ε-avido** | Scegli l'azione migliore la maggior parte delle volte; azione casuale con probabilità ε | Semplice ma inefficiente |
| **Esplorazione Boltzmann** | Scegli le azioni in modo probabilistico in base ai loro valori stimati | Più liscio di ε-greedy |
| **UCB** (limite superiore di fiducia) | Preferire azioni con elevata incertezza (ottimismo di fronte all'incertezza) | Buone garanzie teoriche |
| **Regolarizzazione dell'entropia** | Aggiungi un bonus per visitare diversi stati (utilizzato in SAC, PPO) | Incoraggia l'esplorazione naturale |
---

## Apprendimento per rinforzo multi-agente
Quando più agenti apprendono simultaneamente, le dinamiche diventano molto più complesse.
| Scenario | Sfida | Esempio |
|----------|-----------|---------|
| **Cooperativa** | Gli agenti devono coordinarsi; la cessione del credito è difficile | Squadre di calcio robot; reti di sensori distribuite |
| **Competitiva** | Gli avversari si adattano; l'ambiente non è stazionario | IA del gioco (poker, StarCraft); sicurezza informatica |
| **Misto** | Alcuni agenti cooperano, altri competono | Mercati d'asta; sistemi di traffico |
| Algoritmo | Descrizione |
|-----------|-------------|
| **MADDPG** | Versione multi-agente di DDPG; Critico centralizzato, attori decentralizzati |
| **MAPPO** | PPO multiagente; ampiamente utilizzato nella pratica |
| **Gioco autonomo** | Gli agenti si allenano contro copie di se stessi (AlphaGo, AlphaStar) |
---

## Trasferimento da SIM a reale
Addestrare i robot nel mondo reale è lento e pericoloso. Invece, gli agenti si addestrano nella simulazione e si trasferiscono nella realtà.
| Sfida | Soluzione |
|-----------|----------|
| **Gap nella realtà** (simulazione ≠ mondo reale) | Randomizzazione del dominio: variare i parametri fisici durante l'allenamento |
| **Inefficienza del campione** | Utilizza RL basato su modelli o esercitati su simulazioni parallele di grandi dimensioni |
| **Sicurezza** | RL vincolato: penalizzare le azioni non sicure durante l'allenamento |
| **Osservabilità parziale** | Treno con sensori rumorosi e osservazioni ritardate |
Aziende come Boston Dynamics e Tesla utilizzano ampiamente la simulazione, ma il divario tra prestazioni simulate e fisiche rimane una delle maggiori sfide del settore.
---

## Strumenti e framework
| Strumento | Scopo | Ideale per |
|------|---------|----------|
| **Linee di base stabili3** | Pulisci implementazioni Python di PPO, SAC, TD3, DQN | Apprendimento e prototipazione |
| **RLlib** | Libreria RL scalabile basata su Ray | Formazione distribuita su larga scala |
| **CleanRL** | Implementazioni a file singolo per la ricerca | Comprendere profondamente gli algoritmi |
| **Palestra (OpenAI)** | Interfaccia ambientale standardizzata | Definizione dei problemi RL |
| **Palestra Isaac / Laboratorio Isaac** | Simulazione fisica accelerata dalla GPU | Robotica, dalla simulazione alla realtà |
| **TRL** (Libreria Transformer RL) | RLHF, DPO, PPO per modelli linguistici | Allineamento dei LLM |
| **OpenRLHF** | Quadro RLHF distribuito | Addestramento di modelli di grandi dimensioni con RLHF |
---

## Consigli pratici
- **Inizia con PPO.** È l'algoritmo generico più affidabile. Se non sei sicuro di cosa utilizzare, PPO è l'impostazione predefinita.
- **Normalizza le tue ricompense.** La scalabilità delle ricompense influisce notevolmente sulla stabilità dell'allenamento.
- **Utilizza ambienti vettorizzati.** L'esecuzione di molti ambienti in parallelo (ad esempio, 8–64) stabilizza le stime del gradiente e accelera enormemente l'addestramento.
- **Monitora sia la ricompensa che l'entropia.** Se l'entropia scende a zero, il tuo agente ha smesso di esplorare e potrebbe essere bloccato in un livello ottimale locale.
- **La definizione delle ricompense è un'arte.** Progettare la giusta funzione di ricompensa è spesso la parte più difficile. Le ricompense scarse (solo alla fine) rendono l’apprendimento estremamente lento. Ricompense dense e ben strutturate guidano l’agente ma possono introdurre comportamenti non intenzionali.
- **RLHF è fragile.** Piccole modifiche al modello di ricompensa o agli iperparametri PPO possono causare grandi cali di qualità. DPO è un'alternativa più stabile se non è necessaria la pipeline RLHF completa.
---

## Riepilogo
L’apprendimento per rinforzo è lo studio di come gli agenti imparano a prendere decisioni attraverso l’interazione. Si va dagli algoritmi classici come Q-learning ai moderni metodi RL profondi come PPO e SAC, e è alla base di alcuni dei più importanti progressi recenti nell'intelligenza artificiale, dal gioco all'allineamento del modello linguistico. La sfida principale rimane la stessa: come si apprende il comportamento ottimale quando il feedback è ritardato, scarso e rumoroso? La risposta – tentativi ed errori, guidati da una matematica intelligente – si rivela una delle idee più potenti di tutta l’intelligenza artificiale.