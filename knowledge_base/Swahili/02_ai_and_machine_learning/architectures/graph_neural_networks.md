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
# Mitandao ya Neural ya Grafu
Graph Neural Networks (GNNs) ni mitandao ya neural iliyoundwa kufanya kazi kwenye data iliyo na muundo wa grafu - mitandao ya nodi zilizounganishwa kwa kingo. Ingawa mitandao ya kitamaduni ya neva hufanya kazi kwenye gridi (picha) au mfuatano (maandishi), GNN hushughulikia miundo ya uhusiano kiholela: mitandao ya kijamii, grafu za molekuli, grafu za maarifa, mitandao ya barabara, grafu za mapendekezo, na zaidi. Zimekuwa muhimu kwa ugunduzi wa dawa za kulevya, utambuzi wa ulaghai, mifumo ya mapendekezo na kikoa chochote ambapo uhusiano kati ya huluki ni muhimu.
---

## Grafu ni Nini?
| Sehemu | Maelezo | Mfano |
|-----------|-------------|---------|
| **Nodi (vertex)** | Chombo | Mtu, atomi ya molekuli, mji |
| **Makali** | Uhusiano kati ya nodi mbili | Urafiki, dhamana ya kemikali, barabara |
| **Uzito wa makali** | Nguvu au aina ya uhusiano | Umbali, kufanana, uwezo |
| **Vipengele vya nodi** | Sifa za kila nodi | Umri, nambari ya atomiki, idadi ya watu |
| **Vipengele vya makali** | Sifa za kila makali | Aina ya uhusiano, umbali |
| **Matrix ya ukaribu** | Matrix A ambapo A[i][j] = 1 ikiwa nodi i na j zimeunganishwa | Husimba muundo wa grafu |
### Aina za Grafu
| Aina | Maelezo | Mfano |
|------|-------------|----------|
| **Isiyoelekezwa** | Kingo hazina mwelekeo | Mtandao wa urafiki |
| **Imeelekezwa** | Kingo zina mwelekeo (A→B ≠ B→A) | Wafuasi wa Twitter |
| **Uzito** | Kingo zina maadili ya nambari | Mtandao wa barabara na umbali |
| **Inatofautiana** | Aina nyingi za nodi na makali | Grafu ya kitaaluma (karatasi, waandishi, kumbi) |
| **Inayobadilika** | Muundo wa grafu hubadilika kwa wakati | Mtandao wa kijamii unabadilika kwa wakati |
| **Wawili** | Aina mbili za nodi; kingo kati ya aina tu | Grafu ya mapendekezo ya bidhaa ya mtumiaji |
---

## Kwa nini Isiwe Mitandao ya Neural ya Kawaida?
| Mbinu | Kwanini Inashindwa |
|----------|-------------|
| **Mtandao wa kusambaza mlisho** | Inahitaji uingizaji wa ukubwa usiobadilika; grafu hutofautiana kwa ukubwa na muundo |
| **CNN** | Inachukua muundo wa gridi ya taifa; grafu hazina gridi ya kawaida |
| **RNN/Transformer** | Inachukua utaratibu wa mfululizo; grafu hazina mpangilio wa asili |
GNN hutatua hili kwa kufanya kazi moja kwa moja kwenye muundo wa grafu, kuchakata kila nodi katika muktadha wa majirani zake.
---

## Usanifu wa Msingi wa GNN
### Mfumo wa Kupitisha Ujumbe
GNN nyingi hufuata muundo sawa: kila nodi hukusanya taarifa kutoka kwa majirani zake, inachanganya, na kusasisha uwakilishi wake.
| Hatua | Maelezo |
|------|-------------|
| **1. Ujumbe** | Kila nodi hutuma ujumbe kwa majirani zake (kulingana na vipengele vyake vya sasa) |
| **2. Jumla** | Kila nodi hukusanya na kuchanganya ujumbe kutoka kwa majirani wote |
| **3. Sasisha** | Kila nodi husasisha uwakilishi wake kwa kutumia ujumbe uliojumlishwa |
| **4. Rudia** | Fanya hivi kwa tabaka za K → kila nodi inanasa habari kutoka kwa K hupuka |
### Miundo Muhimu ya GNN
| Mfano | Mbinu ya Kukusanya | Ubunifu Muhimu |
|-------|------------------|----------------|
| **GCN** (Mtandao wa Kubadilisha Grafu) | Maana ya sifa za jirani | Rahisi; ufanisi; motisha ya spectral |
| **GraphSAGE** | Sampuli na jumla; inaweza kutumia maana, LSTM, au kuunganisha | Inductive (hushughulikia nodi zisizoonekana); hatari |
| **GAT** (Mtandao wa Kuzingatia Grafu) | Mkusanyiko wa majirani wenye uzito | Hujifunza ni majirani gani muhimu zaidi |
| **GIN** (Mtandao wa Isomorphism wa Grafu) | Jumla ya vipengele vya jirani | Upeo wa kuelezea; inaweza kutofautisha grafu zozote zinazoweza kutofautishwa na jaribio la WL |
| **MPNN** (Ujumbe Unaopita Mtandao wa Neural) | Mfumo wa kupitisha ujumbe wa jumla | Huunganisha anuwai nyingi za GNN |
### Jinsi GCN Hufanya Kazi (Hatua kwa Hatua)
```
For each layer:
  1. For each node, collect features from all neighbours
  2. Multiply by a learnable weight matrix W
  3. Normalise by node degree (so high-degree nodes don't dominate)
  4. Apply non-linearity (ReLU)
  5. This becomes the node's new representation
```

Baada ya tabaka za K, uwakilishi wa kila nodi husimba maelezo kutoka kwa K kuruka mbali kwenye grafu.
---

## Kazi za Kiwango cha Grafu
| Kazi | Maelezo | Mfano |
|------|-------------|----------|
| **Uainishaji wa nodi** | Tabiri lebo ya kila nodi | Panga watumiaji kama roboti au wanadamu |
| **Utabiri wa kiungo** | Tabiri ikiwa makali yapo (au yatakuwepo) | Tabiri kukosa mahusiano; pendekeza miunganisho |
| **Uainishaji wa grafu** | Bashiri lebo ya grafu nzima | Panga molekuli kama sumu au zisizo na sumu |
| **Ugunduzi wa jumuiya** | Tafuta makundi ya nodi zilizounganishwa sana | Tambua vikundi vya kijamii |
| **Kizazi cha grafu** | Tengeneza grafu mpya na mali zinazohitajika | Tengeneza molekuli mpya |
---

##Maombi
### Ugunduzi wa Dawa za Kulevya na Utabiri wa Mali ya Masi
| Kazi | Jinsi GNNs Husaidia |
|------|--------------|
| **Utabiri wa mali ya Masi** | Wakilisha molekuli kama grafu (atomi=nodi, vifungo=kingo); kutabiri sumu, umumunyifu, mshikamano wa kisheria |
| **Muingiliano wa dawa za kulevya** | Mfano wa dawa na malengo kama grafu; kutabiri mwingiliano mbaya |
| **Muundo wa dawa mpya** | Tengeneza riwaya za grafu za molekuli na sifa zinazohitajika |
### Mifumo ya Mapendekezo
| Mbinu | Maelezo |
|----------|-------------|
| **Grafu ya kipengee cha mtumiaji** | Watumiaji na vitu ni nodi; manunuzi/maoni ni kingo |
| **Uchujaji shirikishi unaotegemea grafu** | GNN hueneza mapendeleo kupitia grafu |
| **Mapendekezo ya grafu ya maarifa** | Changanya mapendeleo ya mtumiaji na maarifa ya bidhaa (aina, waigizaji, wakurugenzi) |
### Utambuzi wa Ulaghai
| Maombi | Muundo wa Grafu |
|------------------------------|
| **Ulaghai wa kifedha** | Shughuli zinaunda grafu; mifumo ya ulaghai huibuka kama miundo ya vijitabu |
| **Udanganyifu wa bima** | Wadai, watoa huduma, na sera huunda grafu; pete za walaghai zimegunduliwa |
| **Kuchukua akaunti** | Mifumo ya kuingia huunda grafu; maelewano ya miunganisho isiyo ya kawaida |
### Grafu za Maarifa
| Kazi | Maelezo |
|------|-------------|
| **Utabiri wa kiungo** | Tabiri ukweli unaokosekana (k.m., "Paris ndio mji mkuu wa ?") |
| **Ubora wa huluki** | Amua ikiwa mitajo miwili inarejelea huluki moja |
| **Majibu ya swali** | Nenda kwenye grafu ili kupata majibu |
---

## Dhana za Kina za GNN
### Kulainisha Zaidi
| Tatizo | Maelezo | Suluhisho |
|---------|-------------|----------|
| **Kulainisha kupita kiasi** | Baada ya tabaka nyingi, uwakilishi wa nodi zote huwa sawa | Upeo wa kina (tabaka 2-4); tumia viunganisho vya mabaki; tumia Maarifa ya Kuruka |
### Kubwaga kupita kiasi
| Tatizo | Maelezo | Suluhisho |
|---------|-------------|----------|
| **Kubwaga kupita kiasi** | Taarifa kutoka kwa vifundo vya mbali hubanwa kuwa vivekta vya saizi isiyobadilika | Tumia transfoma ya grafu; mkusanyiko wa ngazi |
### Vigeuza Grafu
| Mfano | Kipengele Muhimu |
|-------|-------------|
| **Kigeuza Grafu** | Weka umakini wa Transfoma kwa jozi zote za nodi |
| **GPS** (Mfumo wa Uhamasishaji wa Grafu) | Changanya tabaka za ndani za GNN na tabaka za kimataifa za Transfoma |
| **Graphor** | Ongeza usimbaji wa nafasi kulingana na muundo wa grafu |
### Mitandao ya Grafu Tofauti
| Mfano | Maelezo |
|-------|-------------|
| **R-GCN** | GCN ya Uhusiano; matrices tofauti ya uzito kwa aina tofauti za makali |
| **HAN** | Mtandao wa Kuzingatia Tofauti; tahadhari juu ya aina tofauti za nodi na makali |
| **HetGNN** | Mtandao wa Neural wa Graph Heterogeneous; Hushughulikia aina nyingi za nodi |
---

##Uwezo
| Changamoto | Suluhisho |
|-----------|----------|
| **Grafu kubwa** (mamilioni ya nodi) | Mafunzo ya mini-batch; sampuli za jirani |
| **Kumbukumbu** | Kugawanya grafu kote kwenye GPU |
| **Kasi** | Operesheni ndogo za matrix; maktaba maalumu |
### Mikakati ya Sampuli
| Mkakati | Maelezo |
|----------|-------------|
| **Sampuli za nodi** | Sampuli kikundi kidogo cha nodi na vitongoji vyao vya K-hop |
| **Sampuli za makali** | Sampuli za kingo na nodi wanazounganisha |
| **Sampuli za nguzo** | Gawanya grafu katika makundi; treni kwenye nguzo |
| **Sampuli za matembezi bila mpangilio** | Sampuli za nodi kupitia matembezi ya nasibu kutoka kwa nodi lengwa |
---

## Zana na Mifumo
| Zana | Kusudi |
|------|----------|
| **PyTorch Jiometri (PyG)** | Maktaba maarufu zaidi ya GNN; seti tajiri ya miundo na seti za data |
| **DGL** (Maktaba ya Grafu ya Kina) | Mfumo-agnostic; inasaidia PyTorch, TensorFlow, MXNet |
| **NetworkX** | Algorithms ya grafu ya classical; udanganyifu wa data |
| **OGB** (Fungua Kigezo cha Grafu) | Vigezo vya kawaida na seti za data za utafiti wa GNN |
| **CogDL** | Kujifunza kwa kina kwa grafu; yenye mwelekeo wa utafiti |
| ** Spektral** | Maktaba ya GNN ya TensorFlow/Keras |
---

## Muhtasari
Mitandao ya Neural ya Grafu huongeza mafunzo ya kina hadi data uhusiano - mitandao, molekuli, grafu za maarifa na mfumo wowote ambapo huluki zimeunganishwa. Wanafanya kazi kwa kupitisha ujumbe kati ya majirani, kuruhusu kila nodi kujifunza kutoka kwa muktadha wake wa ndani. GNN wamepata matumizi yao madhubuti katika ugunduzi wa dawa, mifumo ya mapendekezo, utambuzi wa ulaghai na grafu za maarifa. Uga unabadilika kuelekea vigeuza grafu, grafu nyingi tofauti, na mafunzo makubwa kwa mitandao mikubwa ya ulimwengu halisi. Ikiwa data yako ina uhusiano, GNNs labda inafaa kuzingatia.