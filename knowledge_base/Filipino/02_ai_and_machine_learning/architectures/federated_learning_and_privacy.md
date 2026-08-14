---
# Metadata
title: "Federated Learning and Privacy"
description: "Decentralised training, differential privacy, secure aggregation"
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
tags: [federated, learning, privacy, ai-and-machine-learning]
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

# Federated Learning at Privacy
Ang federated learning ay isang diskarte para sa pagsasanay ng mga modelo ng machine learning sa maraming device o organisasyon nang hindi ibinabahagi ang raw data. Sa halip na magpadala ng data sa isang central server, ang bawat device ay nagsasanay ng isang lokal na modelo at nagbabahagi lamang ng mga update ng modelo (gradients o weights). Pinagsasama-sama ng gitnang server ang mga update na ito upang makagawa ng isang pandaigdigang modelo. Dinisenyo ito ng Google para sa pagsasanay ng mga modelo ng wika ng keyboard sa mga Android phone — at mula noon ito ay naging isang pangunahing pamamaraan para sa pagpapanatili ng privacy ng AI.
---

## Bakit Federated Learning?
| Pagganyak | Paglalarawan | Halimbawa |
|------------|-------------|---------|
| **Privacy ng data** | Ang raw data ay hindi kailanman umaalis sa device | Ang mga rekord ng medikal ay nananatili sa ospital; nananatili ang mga larawan sa telepono |
| **Pagsunod sa regulasyon** | Pinaghihigpitan ng GDPR, HIPAA, at iba pang mga regulasyon ang pagbabahagi ng data | Maaaring makipagtulungan ang mga bangko nang hindi nagbabahagi ng data ng customer |
| **Dami ng data** | Ang paglipat ng data ay mahal at mabagal | Ang pagsasanay sa bilyun-bilyong mga telepono ay hindi praktikal kung kailangang i-upload ang data |
| **Sensitivity ng data** | Ang ilang data ay masyadong sensitibo upang ibahagi, kahit na may pahintulot | Katalinuhan ng pamahalaan; personal na data ng kalusugan |
---

## Paano Gumagana ang Federated Learning
### Ang Pangunahing Protocol (FedAvg)
| Hakbang | Ano ang Mangyayari |
|------|-------------|
| **1. Magsimula** | Ang gitnang server ay lumilikha ng isang pandaigdigang modelo na may mga random na timbang |
| **2. Ipamahagi** | Ipinapadala ng server ang kasalukuyang pandaigdigang modelo sa mga piling device |
| **3. Lokal na pagsasanay** | Sinasanay ng bawat device ang modelo sa lokal na data nito para sa ilang panahon |
| **4. Mag-upload** | Ipinapadala ng mga device ang kanilang na-update na mga timbang ng modelo (hindi data) pabalik sa server |
| **5. Pinagsama-sama** | Ina-average ng server ang mga timbang (Federated Averaging) upang lumikha ng bagong global na modelo |
| **6. Ulitin** | Bumalik sa hakbang 2 hanggang sa magtagpo ang modelo |
```
Server: global_model = average(local_model_1, local_model_2, ..., local_model_n)
```

### Mga Pangunahing Katangian
| Ari-arian | Paglalarawan |
|----------|-------------|
| **Data na hindi IID** | Ang bawat device ay may iba't ibang distribusyon ng data (hindi independyente at magkaparehong distribusyon) |
| **Hindi balanseng data** | Ang ilang mga device ay may maraming data, ang iba ay may napakakaunting |
| **Bahagyang paglahok** | Hindi lahat ng device ay available sa bawat round |
| **Kahusayan sa komunikasyon** | Ang bottleneck ay komunikasyon, hindi computation |
---

## Federated Learning Variants
| Variant | Paglalarawan | Pakinabang |
|---------|-------------|-----------|
| **FedAvg** | Average na timbang ng modelo sa mga device | Simple; gumagana nang maayos para sa data ng IID |
| **FedProx** | Nagdaragdag ng proximal na termino sa lokal na pagsasanay | Mas mahusay para sa hindi IID na data |
| **SCAFFOLD** | Gumagamit ng control variates para itama ang data heterogeneity | Mas mabilis na convergence sa non-IID data |
| **FedSGD** | Tulad ng FedAvg ngunit may isang gradient na hakbang bawat round | Mas mababang gastos sa komunikasyon bawat round |
| **Naka-personalize na FL** | Ang bawat device ay nagpapanatili ng isang personalized na modelo kasama ng global | Mas mahusay na pagganap sa bawat device |
| **Vertical FL** | Iba't ibang feature (hindi magkakaibang sample) sa mga partido | Kapag hawak ng mga partido ang iba't ibang aspeto ng parehong data |
---

## Differential Privacy
Ang differential privacy (DP) ay nagbibigay ng mathematical na garantiya na ang output ng isang algorithm ay hindi naghahayag kung ang data ng sinumang indibidwal ay kasama.
### Pangunahing Kahulugan
Ang mekanismong M ay nakakatugon sa (ε, δ)-differential privacy kung para sa alinmang dalawang dataset D at D' na naiiba sa isang talaan:
```
P(M(D) ∈ S) ≤ e^ε × P(M(D') ∈ S) + Î´
```

| Parameter | Ibig sabihin |
|-----------|---------|
| **ε (epsilon)** | Badyet sa privacy. Mas maliit = mas pribado. Mga karaniwang halaga: 0.1–10. |
| **δ (delta)** | Ang posibilidad ng hindi pagtupad ng garantiya sa privacy. Karaniwang nakatakda sa 1/N (kabaligtaran ng laki ng dataset). |
### Mga Mekanismo para sa Pagdaragdag ng Privacy
| Mekanismo | Paano Ito Gumagana | Use Case |
|-----------|-------------|----------|
| **Mekanismo ng Gaussian** | Magdagdag ng Gaussian noise na na-calibrate sa sensitivity ng query | Mga tuluy-tuloy na halaga (mga timbang ng modelo) |
| **Mekanismo ng Laplace** | Magdagdag ng ingay sa Laplace | Nagbibilang ng mga query |
| **Exponential mechanism** | Pumili ng mga output na may probability na proporsyonal sa kanilang utility | Mga discrete na pagpipilian |
### DP-SGD (Differentially Private Stochastic Gradient Descent)
| Hakbang | Paglalarawan |
|------|-------------|
| 1. Compute per-sample gradients | Sa halip na batch gradients |
| 2. Mga gradient ng clip | Nakatali sa maximum na pamantayan ng bawat gradient (nililimitahan ang anumang impluwensya ng isang sample) |
| 3. Magdagdag ng ingay | Magdagdag ng naka-calibrate na Gaussian na ingay sa pinagsama-samang gradient |
| 4. I-update ang mga parameter | Standard gradient descent step |
| Trade-off | Paglalarawan |
|-----------|-------------|
| **Privacy vs katumpakan** | Ang mas malakas na privacy (mas mababang ε) ay nangangailangan ng mas maraming ingay, na nagpapababa ng katumpakan ng modelo |
| **Privacy kumpara sa oras ng pagsasanay** | Ang mas maraming ingay ay nangangahulugan ng mas mabagal na convergence |
| **Pagsubaybay sa badyet sa privacy** | Ang bawat hakbang sa pagsasanay ay gumagamit ng ilan sa badyet sa privacy; kapag nagastos, hindi na ito mababawi |
---

## Pinagsasama ang Federated Learning sa Differential Privacy
| Layer | Proteksyon |
|-------|-----------|
| **Federated learning** | Nananatili ang raw data sa mga device |
| **Differential privacy** | Maging ang mga pag-update ng modelo ay maingay, na nagpoprotekta sa mga indibidwal na kontribusyon |
| **Secure na pagsasama-sama** | Nakikita lamang ng server ang pinagsama-samang lahat ng mga update, hindi ang mga indibidwal |
Nagbibigay ang kumbinasyong ito ng matibay na garantiya sa privacy: kahit na nakompromiso ang server, hindi nito matukoy kung ginamit ang data ng anumang partikular na indibidwal sa pagsasanay.
---

## Iba Pang Mga Pamamaraan sa Pagpapanatili ng Privacy
### Secure Multi-Party Computation (SMPC)
Maraming partido ang nagku-compute ng isang function sa kanilang pinagsamang data nang hindi inilalantad ang kanilang mga indibidwal na input.
| Tampok | Paglalarawan |
|---------|-------------|
| **Paano ito gumagana** | Hinahati ang data sa mga pagbabahagi na ibinahagi sa mga partido; nangyayari ang pagkalkula sa mga pagbabahagi |
| **Ggarantiya** | Walang partido na natututo ng anuman tungkol sa mga input ng iba |
| **Overhead** | Makabuluhang gastos sa komunikasyon at pagkalkula |
| **Kaso ng paggamit** | Ang mga bangko ay nagko-compute ng magkasanib na mga modelo ng panganib nang hindi nagbabahagi ng data ng customer |
### Homomorphic Encryption (HE)
Magsagawa ng mga pagkalkula nang direkta sa naka-encrypt na data.
| Uri | Ano ang Sinusuportahan Nito | Overhead |
|------|-----------------|----------|
| **Bahagyang SIYA** | Isang operasyon (pagdaragdag O pagpaparami) | Mababa |
| **Medyo SIYA** | Limitadong bilang ng parehong operasyon | Katamtaman |
| **Ganap na SIYA** | Arbitrary na pagkalkula | Napakataas (100-1000x na pagbagal) |
| Application | Paglalarawan |
|-------------|-------------|
| **Pribadong hinuha** | Patakbuhin ang mga modelo ng ML sa naka-encrypt na data; ibalik ang mga naka-encrypt na hula |
| **Naka-encrypt na pagsasanay** | Magsanay sa naka-encrypt na data (karamihan ay teoretikal pa rin para sa malalim na pag-aaral) |
| **Mga pribadong query** | Mag-query ng database nang hindi inilalantad ang query o ang data |
### Trusted Execution Environment (TEEs)
Hardware-based isolation (Intel SGX, ARM Trustzone) na nagpoprotekta sa data kahit na mula sa OS.
| Pakinabang | Limitasyon |
|-----------|------------|
| Malapit sa katutubong pagganap | Nangangailangan ng partikular na hardware |
| Malakas na garantiya ng seguridad | Limitadong memorya (laki ng enclave) |
| Walang cryptographic overhead | Posibleng mga pag-atake sa side-channel |
---

## Mga Regulasyon sa Privacy at ML
| Regulasyon | Rehiyon | Epekto sa ML |
|------------|--------|-------------|
| **GDPR** | EU | Karapatan sa pagpapaliwanag; pagliit ng data; pahintulot para sa pagproseso; karapatang burahin |
| **CCPA** | California | Karapatang malaman, magtanggal, at mag-opt out sa pagbebenta ng data |
| **HIPAA** | US (pangangalaga sa kalusugan) | Mahigpit na kontrol sa data ng kalusugan; mga kinakailangan sa pag-alis ng pagkakakilanlan |
| **PIPL** | Tsina | Lokalisasyon ng data; mga kinakailangan sa pahintulot; mga panuntunan sa paglipat ng cross-border |
| **AI Act** | EU | Mga kinakailangan sa transparency; pag-uuri ng panganib; mga ipinagbabawal na gawi |
### Epekto sa ML Workflows
| Prinsipyo ng GDPR | Implikasyon ng ML |
|----------------|----------------|
| **Pag-minimize ng data** | Kolektahin lamang ang kailangan; tulong ng federated learning |
| **Limitasyon ng layunin** | Hindi magagamit muli ang data nang walang bagong pahintulot |
| **Karapatang burahin** | Kailangang makapag-alis ng data ng isang tao mula sa isang sinanay na modelo (machine unlearning) |
| **Karapatang magpaliwanag** | Ang mga modelo ay dapat na sapat na nabibigyang-kahulugan upang ipaliwanag ang mga indibidwal na hula |
| **Privacy ayon sa disenyo** | Ang privacy ay dapat na binuo sa mga system mula sa simula |
---

## Mga hamon
| Hamon | Paglalarawan |
|-----------|-------------|
| **Gastos sa komunikasyon** | Ang pagpapadala ng mga update sa modelo sa milyun-milyong device ay mahal |
| **Data na hindi IID** | Ang mga device ay may iba't ibang distribusyon ng data, na nakakasira sa convergence |
| **Mga Straggler** | Ang mga mabagal na device ay naantala ang buong round |
| **Privacy-utility trade-off** | Ang mas malakas na privacy ay nangangahulugan ng mas masamang pagganap ng modelo |
| **Pag-atake ng pagkalason** | Maaaring sirain ng mga masasamang kalahok ang pandaigdigang modelo |
| **Pagkuha ng modelo** | Kahit na ang mga nakabahaging pag-update ng modelo ay maaaring mag-leak ng impormasyon tungkol sa data ng pagsasanay |
| **Pagkakaiba ng hardware** | Ang iba't ibang device ay may iba't ibang kakayahan sa pag-compute |
---

## Mga Tool at Framework
| Tool | Layunin |
|------|---------|
| **Bulaklak** | Open-source federated learning framework; balangkas-agnostiko |
| **TensorFlow Federated** | FL framework ng Google para sa mga modelong TensorFlow |
| **PySyft** (OpenMined) | ML na nagpapanatili ng privacy sa PyTorch |
| **FATE** (Webank) | Industrial-grade federated learning platform |
| **LEAF** | Benchmark suite para sa federated learning research |
| **Opacus** (Meta) | Differential privacy para sa PyTorch |
| **Ang TF Privacy ng Google** | Differential privacy para sa TensorFlow |
---

## Buod
Tinutugunan ng federated learning at mga diskarte sa pagpapanatili ng privacy ang isang pangunahing tensyon: paano ka bubuo ng mga mahuhusay na modelo ng AI kapag ang data ay ipinamamahagi, sensitibo, o kinokontrol? Ang federated learning ay nagpapanatili ng data sa mga device at nagbabahagi lamang ng mga update ng modelo. Ang pagkakaiba ng privacy ay nagdaragdag ng mga mathematical na garantiya na ang mga indibidwal na kontribusyon ay hindi matukoy. Ang secure na pag-compute at homomorphic na pag-encrypt ay higit pa, na nagbibigay-daan sa pag-compute sa naka-encrypt na data. Ang bawat diskarte ay may mga gastos — overhead ng komunikasyon, pinababang katumpakan, gastos sa computational — ngunit magkasama silang bumubuo ng isang toolkit para sa pagbuo ng AI na gumagalang sa privacy habang natututo pa rin mula sa data ng mundo.