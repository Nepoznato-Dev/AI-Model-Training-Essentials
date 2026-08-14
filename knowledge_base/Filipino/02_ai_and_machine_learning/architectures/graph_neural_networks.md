---
# Metadata
title: "Graph Neural Networks"
description: "GCNs, GATs, message passing, knowledge graphs, graph tasks"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to architectures/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
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

# Graph Mga Neural Network
Ang Graph Neural Networks (GNNs) ay mga neural network na idinisenyo upang gumana sa graph-structured data — mga network ng mga node na konektado sa pamamagitan ng mga gilid. Habang gumagana ang mga tradisyunal na neural network sa mga grid (mga larawan) o mga pagkakasunud-sunod (teksto), pinangangasiwaan ng mga GNN ang mga arbitraryong istruktura ng relasyon: mga social network, mga molecular graph, mga graph ng kaalaman, mga network ng kalsada, mga graph ng rekomendasyon, at higit pa. Naging mahalaga ang mga ito para sa pagtuklas ng droga, pagtuklas ng panloloko, mga sistema ng rekomendasyon, at anumang domain kung saan mahalaga ang mga ugnayan sa pagitan ng mga entity.
---

## Ano ang Graph?
| Bahagi | Paglalarawan | Halimbawa |
|-----------|-------------|---------|
| **Node (vertex)** | Isang entity | Isang tao, atom ng molekula, isang lungsod |
| **Gilid** | Isang relasyon sa pagitan ng dalawang node | Pagkakaibigan, chemical bond, kalsada |
| **Timbang ng gilid** | Lakas o uri ng relasyon | Distansya, pagkakatulad, kapasidad |
| **Mga tampok ng node** | Mga katangian ng bawat node | Edad, atomic number, populasyon |
| **Mga tampok sa gilid** | Mga katangian ng bawat gilid | Uri ng relasyon, distansya |
| **Adjacency matrix** | Matrix A kung saan ang A[i][j] = 1 kung ang mga node i at j ay konektado | Ine-encode ang istraktura ng graph |
### Mga Uri ng Graph
| Uri | Paglalarawan | Halimbawa |
|------|-------------|---------|
| **Hindi nakadirekta** | Ang mga gilid ay walang direksyon | Network ng pagkakaibigan |
| **Idinirekta** | May direksyon ang mga gilid (A→B ≠ B→A) | Mga tagasubaybay sa Twitter |
| **Tinimbang** | Ang mga gilid ay may mga numerong halaga | Network ng kalsada na may mga distansya |
| **Heterogenous** | Maramihang mga uri ng node at gilid | Akademikong graph (mga papel, may-akda, lugar) |
| **Dynamic** | Ang istraktura ng graph ay nagbabago sa paglipas ng panahon | Ang social network na umuunlad sa paglipas ng panahon |
| **Bipartite** | Dalawang uri ng mga node; mga gilid lamang sa pagitan ng mga uri | Grap ng rekomendasyon ng user-item |
---

## Bakit Hindi Regular na Neural Network?
| Diskarte | Bakit Ito Nabigo |
|----------|-------------|
| **Feed-forward network** | Nangangailangan ng fixed-size na input; iba-iba ang laki at istraktura ng mga graph |
| **CNN** | Ipinagpapalagay ang istraktura ng grid; ang mga graph ay walang regular na grid |
| **RNN/Transformer** | Ipinagpapalagay ang sunud-sunod na pagkakasunud-sunod; ang mga graph ay walang natural na pagkakasunud-sunod |
Niresolba ito ng mga GNN sa pamamagitan ng direktang pagpapatakbo sa istraktura ng graph, pagpoproseso ng bawat node sa konteksto ng mga kapitbahay nito.
---

## Mga Pangunahing Arkitektura ng GNN
### Framework sa Pagpasa ng Mensahe
Karamihan sa mga GNN ay sumusunod sa parehong pattern: ang bawat node ay nangongolekta ng impormasyon mula sa mga kapitbahay nito, pinagsasama ito, at ina-update ang sarili nitong representasyon.
| Hakbang | Paglalarawan |
|------|-------------|
| **1. Mensahe** | Ang bawat node ay nagpapadala ng mensahe sa mga kapitbahay nito (batay sa mga kasalukuyang tampok nito) |
| **2. Pinagsama-sama** | Ang bawat node ay nangongolekta at nagsasama-sama ng mga mensahe mula sa lahat ng mga kapitbahay |
| **3. Update** | Ang bawat node ay nag-a-update ng sarili nitong representasyon gamit ang pinagsama-samang mensahe |
| **4. Ulitin** | Gawin ito para sa mga K layer → bawat node ay kumukuha ng impormasyon mula sa K hops away |
### Mga Pangunahing Modelo ng GNN
| Modelo | Paraan ng Pagsasama-sama | Pangunahing Pagbabago |
|---------------------|---------------------|----------------|
| **GCN** (Graph Convolutional Network) | Mean ng mga tampok ng kapitbahay | Simple; epektibo; parang multo pagganyak |
| **GraphSAGE** | Sample at pinagsama-samang; maaaring gumamit ng mean, LSTM, o pooling | Inductive (hinahawakan ang hindi nakikitang mga node); nasusukat |
| **GAT** (Graph Attention Network) | Pagsasama-sama ng kapitbahay na may timbang na pansin | Natutunan kung aling mga kapitbahay ang pinakamahalaga |
| **GIN** (Graph Isomorphism Network) | Kabuuan ng mga tampok ng kapitbahay | Pinakamataas na nagpapahayag; maaaring makilala ang anumang mga graph na nakikilala ng WL test |
| **MPNN** (Message Passing Neural Network) | Pangkalahatang balangkas ng pagpasa ng mensahe | Pinag-iisa ang maraming variant ng GNN |
### Paano Gumagana ang GCN (Step by Step)
```
For each layer:
  1. For each node, collect features from all neighbours
  2. Multiply by a learnable weight matrix W
  3. Normalise by node degree (so high-degree nodes don't dominate)
  4. Apply non-linearity (ReLU)
  5. This becomes the node's new representation
```

Pagkatapos ng mga K layer, ang representasyon ng bawat node ay nag-encode ng impormasyon mula sa K hops palayo sa graph.
---

## Mga Gawain sa Antas ng Graph
| Gawain | Paglalarawan | Halimbawa |
|------|-------------|---------|
| **Pag-uuri ng node** | Hulaan ang label ng bawat node | Uriin ang mga user bilang mga bot o tao |
| **Paghula ng link** | Hulaan kung ang isang gilid ay umiiral (o iiral) | Hulaan ang mga nawawalang relasyon; magrekomenda ng mga koneksyon |
| **Pag-uuri ng graph** | Hulaan ang isang label para sa buong graph | Uriin ang mga molekula bilang nakakalason o hindi nakakalason |
| **Deteksyon ng komunidad** | Maghanap ng mga kumpol ng makapal na konektadong mga node | Kilalanin ang mga pangkat ng lipunan |
| **Pagbuo ng graph** | Bumuo ng mga bagong graph na may ninanais na mga katangian | Magdisenyo ng mga bagong molekula |
---

## Mga Application
### Pagtuklas ng Gamot at Paghula sa Molecular Property
| Gawain | Paano Tumutulong ang mga GNN |
|------|--------------|
| **Molecular property prediction** | Kinakatawan ang mga molekula bilang mga graph (atoms=nodes, bonds=edges); hulaan ang toxicity, solubility, binding affinity |
| **Pakikipag-ugnayan ng droga-droga** | Magmodelo ng mga gamot at target bilang isang graph; hulaan ang masamang pakikipag-ugnayan |
| **De novo na disenyo ng gamot** | Bumuo ng mga nobelang molecular graph na may mga gustong katangian |
### Sistema ng Rekomendasyon
| Diskarte | Paglalarawan |
|----------|-------------|
| **Grap ng user-item** | Ang mga user at item ay mga node; ang mga pagbili/pagtingin ay mga gilid |
| **Graph-based collaborative na pag-filter** | Ang mga GNN ay nagpapalaganap ng mga kagustuhan sa pamamagitan ng graph |
| **Mga rekomendasyon sa graph ng kaalaman** | Pagsamahin ang mga kagustuhan ng user sa kaalaman sa item (mga genre, aktor, direktor) |
### Pagtuklas ng Panloloko
| Application | Istruktura ng Graph |
|-------------|----------------|
| **Pandaraya sa pananalapi** | Ang mga transaksyon ay bumubuo ng isang graph; lumilitaw ang mga mapanlinlang na pattern bilang mga istruktura ng subgraph |
| **Pandaraya sa insurance** | Ang mga naghahabol, tagapagkaloob, at mga patakaran ay bumubuo ng isang graph; ang mga ring ng mga manloloko ay nakita |
| **Pagkuha ng account** | Ang mga pattern sa pag-login ay bumubuo ng isang graph; maanomalyang koneksyon signal kompromiso |
### Mga Graph ng Kaalaman
| Gawain | Paglalarawan |
|------|-------------|
| **Paghula ng link** | Hulaan ang mga nawawalang katotohanan (hal., "Ang Paris ay ang kabisera ng ?") |
| **Resolusyon ng entity** | Tukuyin kung ang dalawang pagbanggit ay tumutukoy sa parehong entity |
| **Pagsagot sa tanong** | Mag-navigate sa graph upang mahanap ang mga sagot |
---

## Mga Advanced na Konsepto ng GNN
### Over-Smoothing
| Problema | Paglalarawan | Solusyon |
|---------|-------------|----------|
| **Sobra-smoothing** | Pagkatapos ng maraming layer, ang lahat ng representasyon ng node ay nagiging magkatulad | Limitahan ang lalim (2-4 na layer); gumamit ng mga natitirang koneksyon; gamitin ang Jumping Knowledge |
### Over-Squashing
| Problema | Paglalarawan | Solusyon |
|---------|-------------|----------|
| **Sobra-squashing** | Ang impormasyon mula sa malalayong node ay na-compress sa fixed-size na mga vector | Gumamit ng mga graph transformer; hierarchical pooling |
### Mga Transformer ng Graph
| Modelo | Pangunahing Tampok |
|-------|-------------|
| **Graph Transformer** | Ilapat ang karaniwang pansin ng Transformer sa lahat ng mga pares ng node |
| **GPS** (Graph Prompting System) | Pagsamahin ang mga lokal na layer ng GNN sa mga global na layer ng Transformer |
| **Graphormer** | Magdagdag ng positional encoding batay sa istraktura ng graph |
### Mga Heterogenous Graph Network
| Modelo | Paglalarawan |
|-------|-------------|
| **R-GCN** | Relational GCN; iba't ibang mga matrice ng timbang para sa iba't ibang uri ng gilid |
| **HAN** | Heterogenous Attention Network; pansin sa iba't ibang uri ng node at gilid |
| **HetGNN** | Heterogenous Graph Neural Network; humahawak ng maraming uri ng node |
---

## Scalability
| Hamon | Solusyon |
|-----------|----------|
| **Malalaking graph** (milyong-milyong node) | Mini-batch na pagsasanay; kapitbahay sampling |
| **Memory** | Paghahati ng graph sa mga GPU |
| **Bilis** | Kalat-kalat na mga operasyon ng matrix; mga dalubhasang aklatan |
### Mga Istratehiya sa Pagsa-sample
| Diskarte | Paglalarawan |
|----------|-------------|
| **Pagsa-sample ng node** | Mag-sample ng subset ng mga node at ang kanilang mga K-hop neighborhood |
| **Edge sampling** | Mga sample na gilid at ang mga node na kanilang ikinonekta |
| **Cluster sampling** | Hatiin ang graph sa mga cluster; tren sa mga kumpol |
| **Random walk sampling** | Mga halimbawang node sa pamamagitan ng mga random na paglalakad mula sa mga target na node |
---

## Mga Tool at Framework
| Tool | Layunin |
|------|---------|
| **PyTorch Geometric (PyG)** | Pinakatanyag na library ng GNN; rich set ng mga modelo at dataset |
| **DGL** (Deep Graph Library) | Framework-agnostic; sumusuporta sa PyTorch, TensorFlow, MXNet |
| **NetworkX** | Mga algorithm ng klasikal na graph; pagmamanipula ng data |
| **OGB** (Open Graph Benchmark) | Mga karaniwang benchmark at dataset para sa pananaliksik sa GNN |
| **CogDL** | Malalim na pag-aaral para sa mga graph; nakatuon sa pananaliksik |
| **Spektral** | GNN library para sa TensorFlow/Keras |
---

## Buod
Ang Graph Neural Networks ay nagpapalawak ng malalim na pag-aaral sa relational data — mga network, molekula, mga graph ng kaalaman, at anumang sistema kung saan konektado ang mga entity. Gumagana sila sa pamamagitan ng pagpasa ng mga mensahe sa pagitan ng mga kapitbahay, na nagpapahintulot sa bawat node na matuto mula sa lokal na konteksto nito. Natagpuan ng mga GNN ang kanilang pinakamalakas na aplikasyon sa pagtuklas ng droga, mga sistema ng rekomendasyon, pagtuklas ng panloloko, at mga graph ng kaalaman. Ang field ay umuusbong patungo sa mga graph transformer, magkakaibang mga graph, at scalable na pagsasanay para sa napakalaking real-world network. Kung may mga ugnayan ang iyong data, malamang na sulit na isaalang-alang ang mga GNN.