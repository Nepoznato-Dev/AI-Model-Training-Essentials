<!--
---
# Metadata
title: "Recommendation Systems"
description: "Collaborative filtering, content-based, hybrid, matrix factorisation"
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
tags: [recommendation, systems, ai-and-machine-learning]
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

-->
# Mga System ng Rekomendasyon
Ang mga system ng rekomendasyon ay hinuhulaan kung ano ang gusto ng isang user na makita, bilhin, o makipag-ugnayan sa susunod. Pinapagana nila ang mga feed ng nilalaman sa social media, mga mungkahi ng produkto sa mga site ng e-commerce, mga pagpili ng pelikula sa mga streaming platform, at mga resulta ng paghahanap. Sa kabila ng pagiging invisible ng karamihan sa mga user, kabilang sila sa mga pinaka-komersyal na epekto ng AI system sa mundo — tinatantya ng Netflix na ang engine ng rekomendasyon nito ay nakakatipid ng higit sa $1 bilyon bawat taon sa pamamagitan ng pagbabawas ng subscriber churn.
---

## Bakit Mahirap ang Mga Rekomendasyon
| Hamon | Paglalarawan |
|-----------|-------------|
| **Scale** | Milyun-milyong user × milyon-milyong item = bilyun-bilyong posibleng mga pares |
| **Sparsity** | Nakipag-ugnayan ang bawat user sa isang maliit na bahagi ng mga available na item |
| **Malamig na simula** | Ang mga bagong user at bagong item ay walang history ng pakikipag-ugnayan |
| **Mga dynamic na kagustuhan** | Nagbabago ang panlasa ng user sa paglipas ng panahon |
| **Higit pa sa katumpakan** | Ang mga rekomendasyon ay dapat ding iba-iba, nobela, at serendipitous |
| **Mga layunin sa negosyo** | Pag-maximize sa pakikipag-ugnayan ≠ pag-maximize sa kapakanan ng user |
---

## Mga Pangunahing Diskarte
### Collaborative na Pag-filter
Ang ideya: kung ang mga user A at B ay sumang-ayon sa nakaraan, malamang na sila ay sumang-ayon sa hinaharap.
| Uri | Paano Ito Gumagana | Halimbawa |
|------|-------------|---------|
| **Batay sa gumagamit** | Maghanap ng mga katulad na user; inirerekomenda kung ano ang nagustuhan nila | "Nagustuhan din ng mga user na nagustuhan ito..." |
| **Batay sa item** | Maghanap ng mga katulad na item sa kung ano ang nagustuhan ng user | "Nanood ka kasi..." |
| **Matrix factorization** | I-decompose ang matrix ng pakikipag-ugnayan ng user-item sa mga nakatagong salik | SVD, ALS (Alternating Least Squares) |
| Lakas | Kahinaan |
|----------|----------|
| Hindi na kailangang maunawaan ang mga item sa kanilang sarili | Cold start problem: hindi makapagrekomenda ng mga bagong item |
| Kinukuha ang mga kumplikado, implicit na mga kagustuhan | Nangangailangan ng maraming data ng pakikipag-ugnayan |
| Gumagana sa anumang uri ng nilalaman | Bias ng katanyagan: nagrerekomenda ng mga sikat na item |
### Pag-filter na Batay sa Nilalaman
Magrekomenda ng mga item na katulad ng mga nagustuhan na ng user, batay sa mga feature ng item.
| Uri ng Tampok | Halimbawa |
|-------------|---------|
| **Text** | Genre, paglalarawan, mga keyword, cast |
| **Audio** | Tempo, genre, mood (para sa musika) |
| **Visual** | Palette ng kulay, istilo (para sa mga larawan/fashion) |
| **Metadata** | Presyo, tatak, kategorya |
| Lakas | Kahinaan |
|----------|----------|
| Walang malamig na simula para sa mga item (alam ang mga feature) | Hindi makapagrekomenda ng mga item sa labas ng kasalukuyang panlasa ng user |
| Gumagana sa mas kaunting data ng pakikipag-ugnayan | Nangangailangan ng mahusay na tampok na engineering |
| Naipaliliwanag ("inirerekomenda dahil katulad ito ng X") | Mas kaunting serendipity |
### Mga Hybrid Approach
Pinagsasama-sama ng karamihan sa mga sistema ng produksyon ang mga pamamaraang collaborative at content-based.
| Hybrid Strategy | Paglalarawan |
|----------------|------------|
| **Tinimbang** | Pagsamahin ang mga marka mula sa maraming modelo |
| **Lumipat** | Gumamit ng content-based para sa mga bagong user, collaborative para sa mga dati nang user |
| **Cascade** | Gumamit muna ng simpleng modelo, pagkatapos ay pinuhin gamit ang kumplikadong modelo |
| **Kumbinasyon ng tampok** | Pagsamahin ang collaborative at content na mga feature sa iisang modelo |
| **Meta-learning** | Matutunan kung paano pagsamahin ang iba't ibang rekomendasyon |
---

## Modernong Deep Learning Approach
### Mga Modelong Dalawang-Tore
Ang nangingibabaw na arkitektura para sa malakihang rekomendasyon (ginagamit ng YouTube, Pinterest, Spotify).
| Bahagi | Tungkulin |
|-----------|------|
| **User tower** | Neural network na nag-e-encode ng mga feature at history ng user sa isang embedding |
| **Tore ng item** | Neural network na nag-encode ng mga feature ng item sa isang pag-embed na |
| **Pagkakatulad** | Dot product o cosine na pagkakapareho sa pagitan ng user at mga item embed |
| Hakbang | Paglalarawan |
|------|-------------|
| 1 | Sanayin ang parehong tower na gumawa ng magkatulad na mga pag-embed para sa mga pares ng user-item na nakikipag-ugnayan |
| 2 | Sa oras ng paghahatid, pre-compute item embedddings |
| 3 | Para sa kahilingan ng user, kalkulahin ang pag-embed ng user |
| 4 | Gumamit ng tinatayang pinakamalapit na kapitbahay (ANN) na paghahanap upang mahanap ang pinakakaparehong mga item |
### Mga Modelo ng Pagkakasunud-sunod para sa Mga Rekomendasyon
Ang gawi ng user ay sunud-sunod — ang pinanood mo kahapon ay nakakaimpluwensya sa papanoorin mo ngayon.
| Modelo | Diskarte |
|-------|----------|
| **GRU4Rec** | GRU-based na modelo para sa session-based na mga rekomendasyon |
| **SASRec** | Nakabatay sa sarili na sequential recommender |
| **BERT4Rec** | Bidirectional Transformer para sa mga sequential na rekomendasyon |
| **YouTube DNN** | Tinatrato ng malalim na neural network ang history ng panonood bilang isang sequence |
### Retrieval vs Ranking
Hinahati ng mga modernong sistema ang mga rekomendasyon sa dalawang yugto:
| Yugto | Layunin | Paraan |
|-------|---------|--------|
| **Pagkuha (pagbuo ng kandidato)** | Paliitin ang milyun-milyong item sa ~1,000 kandidato | Dalawang-tower na modelo; ANN paghahanap; mabilis ngunit tinatayang |
| **Pagraranggo (pagmamarka)** | Tumpak na puntos at i-order ang mga kandidato | Malalim na modelo na may maraming mga tampok; mas mabagal ngunit tumpak |
| **Muling pagraranggo** | Isaayos para sa pagkakaiba-iba, mga panuntunan sa negosyo, pagiging bago | Mga bandido sa konteksto; pag-optimize ng hadlang |
---

## Mga Sukatan ng Pagsusuri
| Sukatan | Ang Sinusukat Nito | Kailan Gagamitin |
|--------|-----------------|-------------|
| **Katumpakan@K** | Fraction ng top-K na rekomendasyon na may kaugnayan | Kapag pinapahalagahan mo ang katumpakan ng mga nangungunang pinili |
| **Recall@K** | Fraction ng mga nauugnay na item na matatagpuan sa top-K | Kapag nagmamalasakit ka tungkol sa hindi nawawalang magagandang item |
| **NDCG** (Normalised Discounted Cumulative Gain) | Kalidad ng pagraranggo; mga gantimpala na naglalagay ng mga nauugnay na item nang mas mataas | Kapag mahalaga ang pagkakasunod-sunod ng ranggo |
| **MAP** (Mean Average Precision) | Average na katumpakan sa lahat ng user | Pangkalahatang kalidad ng pagraranggo |
| **Rate ng Hit@K** | Kung lalabas man ang kahit man lang isang nauugnay na item sa top-K | Mga sitwasyong may kaugnayan sa binary |
| **Sakop** | Fraction ng mga item na inirerekumenda | Pagkakaiba-iba at pagiging patas |
| **Serendipity** | Hindi inaasahang ngunit may-katuturang mga rekomendasyon | Kasiyahan ng user |
---

## Ang Cold Start Problem
| Sitwasyon | Hamon | Mga Solusyon |
|----------|-----------|-----------|
| **Bagong user** | Walang history ng pakikipag-ugnayan | Gumamit ng demograpiko; ipakita ang mga sikat na item; gumamit ng mga signal sa konteksto (lokasyon, device, oras) |
| **Bagong item** | Wala pang nakipag-ugnayan dito | Gumamit ng mga tampok ng nilalaman; explore-exploit strategies; mga algorithm ng bandido |
| **Bagong sistema** | Walang data sa lahat | Maglipat ng pag-aaral mula sa mga katulad na domain; i-curate ang paunang nilalaman |
---

## Exploration vs Exploitation
| Diskarte | Paglalarawan | Trade-off |
|----------|-------------|-----------|
| **ε-matakaw** | Ipakita ang mga random na item na may posibilidad na ε | Simple ngunit hindi epektibo |
| **Thompson sampling** | Sample mula sa posterior distribution ng kalidad ng item | May prinsipyo; magandang teoretikal na katangian |
| **Upper Confidence Bound (UCB)** | Mas gusto ang mga item na may mataas na kawalan ng katiyakan | Magandang balanse ng eksplorasyon at pagsasamantala |
| **Mga bandido sa konteksto** | Pag-explore na nakakondisyon sa konteksto ng user | Mas mahusay kaysa sa blind exploration |
| **Pag-iniksyon ng pagkakaiba-iba** | Sadyang isama ang magkakaibang o nobelang mga item | Simple; maaaring bawasan ang panandaliang pakikipag-ugnayan |
---

## Bias at Pagkamakatarungan
| Uri ng Bias | Paglalarawan | Epekto |
|-----------|-------------|--------|
| **Pagkiling sa popularidad** | Mas inirerekumenda ang mga sikat na item, nagiging mas sikat | Ang mga long-tail na item ay kulang sa serbisyo |
| **Pagkiling sa pagpili** | Natututo ang mga modelo mula sa mga naobserbahang pakikipag-ugnayan, hindi lahat ng posibleng | Nakahilig sa mga aktibong user |
| **Pagkiling sa posisyon** | Ang mga item na ipinapakita sa mas matataas na posisyon ay nakakakuha ng mas maraming pag-click anuman ang kalidad | Pinapatibay ang mga nangungunang posisyon |
| ** bias sa pagkakalantad** | Ang mga item na ipinakita ay nakakakuha ng higit pang signal ng pagsasanay | Feedback loop |
| **Demograpikong bias** | Nag-iiba ang mga rekomendasyon sa mga demograpiko sa hindi patas na paraan | Diskriminasyon; mahinang karanasan para sa ilang grupo |
### Mga Istratehiya sa Pagbabawas
| Diskarte | Paglalarawan |
|----------|-------------|
| **Inverse propensity weighting** | Mga sikat na item sa pagbaba ng timbang sa pagsasanay |
| **Debiasing layer** | Magdagdag ng debiasing component sa modelong |
| **Mga hadlang sa pagiging patas** | Magdagdag ng mga hadlang upang matiyak ang pantay na pagtrato |
| **Magkakaibang rekomendasyon** | Tahasang mag-optimize para sa pagkakaiba-iba kasama ng kaugnayan |
| **Pag-audit at pagsubaybay** | Regular na suriin ang mga rekomendasyon para sa bias sa mga pangkat |
---

## Mga Halimbawa ng Industriya
| Kumpanya | System | Diskarte |
|---------|--------|----------|
| **Netflix** | Mga rekomendasyon sa pelikula/TV | Two-tower retrieval + deep ranking + contextual bandits para sa likhang sining |
| **YouTube** | Mga rekomendasyon sa video | Malalim na neural network para sa pagbuo ng kandidato; hiwalay na modelo ng pagraranggo |
| **Spotify** | Mga rekomendasyon sa musika | Collaborative na pag-filter + NLP sa mga playlist + audio analysis |
| **Amazon** | Mga rekomendasyon sa produkto | Item-to-item collaborative na pag-filter; isinapersonal sa sukat |
| **TikTok** | Maikling video feed | Reinforcement learning; malakas na diin sa paggalugad |
| **Pinterest** | Mga visual na rekomendasyon | Dalawang-tower na modelo; visual na pagkakatulad |
---

## Mga Tool at Framework
| Tool | Layunin |
|------|---------|
| **TensorFlow Recommenders (TFRS)** | Dalawang-tower na modelo, pagbawi, pagraranggo |
| **PyTorch RecSys** | Mga modelo ng rekomendasyong nakatuon sa pananaliksik |
| **Surpresa** | Classical collaborative na pag-filter (SVD, NMF, KNN) |
| **Implicit** | Mabilis na collaborative na pag-filter para sa implicit na feedback (ALS, BPR) |
| **Faiss** (Meta) | Tinatayang pinakamalapit na paghahanap ng kapitbahay sa sukat |
| **Milvus / Pinecone / Weaviate** | Mga database ng vector para sa paghahanap ng pagkakatulad |
| **Recbole** | Comprehensive rekomendasyon pananaliksik library |
| **Merlin** (NVIDIA) | Pipeline ng rekomendasyong pinabilis ng GPU |
---

## Buod
Ang mga sistema ng rekomendasyon ay kabilang sa mga pinaka-maimpluwensyang AI application sa industriya. Nag-evolve ang field mula sa simpleng collaborative na pag-filter tungo sa malalim na pag-aaral ng mga arkitektura na pinagsasama-sama ang kasaysayan ng user, nilalaman ng item, mga signal sa konteksto, at mga layunin sa negosyo. Gumagamit ang mga modernong system ng pipeline ng retrieval-ranking-re-ranking, na may dalawang-tower na modelo para sa mabilis na pagbuo ng kandidato at malalim na mga modelo para sa tumpak na pagmamarka. Ang mga hamon — malamig na pagsisimula, pagkiling, paggalugad, at pagbabalanse sa kasiyahan ng user sa mga layunin sa negosyo — ay nananatiling aktibong bahagi ng pananaliksik at engineering.