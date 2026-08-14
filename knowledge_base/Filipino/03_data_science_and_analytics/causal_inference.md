<!--
---
# Metadata
title: "Causal Inference"
description: "DAGs, confounders, difference-in-differences, instrumental variables"
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
tags: [causal, inference, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Sanhi ng Hinuha
Ang causal inference ay ang agham ng pagtukoy kung ang isang bagay ay talagang nagdudulot ng isa pa — hindi lang kung may kaugnayan ang mga ito. Sinasabi sa iyo ng ugnayan na ang dalawang variable ay gumagalaw nang magkasama. Sinasabi sa iyo ng sanhi na ang pagbabago ng isa ay magbabago sa isa pa. Napakahalaga ng pagkakaibang ito sa medisina (gumagana ba ang gamot na ito?), patakaran (nababawasan ba ng interbensyong ito ang kahirapan?), negosyo (nagdaragdag ba ang mga benta ng ad campaign na ito?), at agham (ipinapaliwanag ba ng mekanismong ito ang phenomenon?).
---

## Kaugnayan vs Sanhi
| Konsepto | Paglalarawan | Halimbawa |
|---------|-------------|---------|
| **Kaugnayan** | Dalawang variable ang gumagalaw nang magkasama | Ang benta ng ice cream at pagkamatay ng pagkalunod ay parehong tumaas sa tag-araw |
| **Dahilan** | Ang isang variable ay direktang nakakaapekto sa isa pang | Ang paninigarilyo ay nagdudulot ng kanser sa baga |
| **Nalilito** | Ang ikatlong variable ay nagiging sanhi ng parehong | Ang mainit na panahon ay nagdudulot ng parehong pagbebenta ng ice cream at paglangoy (at pagkalunod) |
| **Reverse causation** | Ang epekto ay talagang nagiging sanhi ng dapat na dahilan | Ang mga tao ay bumibili ng mga pandagdag sa kalusugan dahil sila ay may sakit, hindi ang kabaligtaran |
| **Huwad na ugnayan** | Hindi sinasadyang relasyon | Ang pagkonsumo ng per capita na keso ay nauugnay sa mga pagkamatay sa pamamagitan ng pagkakasalubong ng bedsheet |
---

## Ang Framework ng Potensyal na Resulta
### Rubin Causal Model
| Konsepto | Paglalarawan |
|---------|-------------|
| **Mga potensyal na resulta** | Para sa bawat yunit, mayroong resulta kung ginagamot ang Y(1) at isang resulta kung hindi ginagamot Y(0) |
| **Epekto ng paggamot** | Ang pagkakaiba: Y(1) - Y(0) para sa isang partikular na unit |
| **Pangunahing problema** | Hinding-hindi natin mamamasid ang parehong Y(1) at Y(0) para sa parehong yunit — isa lang ang makikita natin |
| **Average Treatment Effect (ATE)** | Ang average ng mga indibidwal na epekto ng paggamot sa buong populasyon |
| **Counterfactual** | Ang hindi naobserbahang kinalabasan — kung ano ang mangyayari sa ilalim ng ibang kundisyon |
### Mga Pangunahing Pagpapalagay
| Pagpapalagay | Ibig sabihin | Paano Masiyahan |
|-----------|--------|----------------|
| **Kawalang-malay (unconfoundedness)** | Ang pagtatalaga ng paggamot ay independiyente sa mga potensyal na resulta, dahil sa mga naobserbahang covariates | Randomization; sukatin ang lahat ng confounder |
| **Positivity (overlap)** | Ang bawat yunit ay may hindi-zero na posibilidad na makatanggap ng alinmang paggamot | Suriin ang covariate overlap sa pagitan ng mga pangkat |
| **SUTVA** (Stable Unit Treatment Value Assumption) | Ang paggamot ng isang yunit ay hindi nakakaapekto sa kinalabasan ng iba; pare-pareho ang paggamot | Walang panghihimasok; walang mga nakatagong bersyon ng paggamot |
| **Consistency** | Ang naobserbahang kinalabasan ay katumbas ng potensyal na resulta sa ilalim ng natanggap na paggamot | Mahusay na tinukoy na paggamot |
---

## Mga Paraan para sa Sanhi ng Hinuha
### Mga Eksperimental na Paraan
| Paraan | Paglalarawan | Lakas | Limitasyon |
|--------|-------------|----------|------------|
| **Randomized na kinokontrol na pagsubok (RCT)** | Random na magtalaga ng mga unit sa paggamot o kontrol | Pamantayan ng ginto; inaalis ang nakakalito | Mahal; minsan hindi etikal; maaaring hindi i-generalize |
| **A/B testing** | RCT sa isang negosyo/tech na konteksto | Simple; mahigpit | Mga panandaliang sukatan; bagong bagay na epekto; panghihimasok |
| **Mga eksperimento sa switchback** | Kahaliling paggamot sa mga yugto ng panahon | Pinangangasiwaan ang panghihimasok sa mga pamilihan | Nangangailangan ng matatag na kapaligiran |
### Quasi-Experimental na Paraan
| Paraan | Paglalarawan | Key Assumption |
|--------|-------------|----------------|
| **Difference-in-differences (DiD)** | Ikumpara ang pagbabago sa mga kinalabasan sa pagitan ng ginagamot at kinokontrol na mga grupo sa paglipas ng panahon | Parallel trend: ang mga grupo ay sumunod sana sa parehong trajectory nang walang paggamot |
| **Regression discontinuity (RD)** | Paghambingin ang mga yunit sa itaas at ibaba lamang ng cutoff ng paggamot | Ang mga unit na malapit sa cutoff ay maihahambing (parang random) |
| **Mga instrumental na variable (IV)** | Gumamit ng variable na nakakaapekto sa paggamot ngunit hindi sa kinalabasan maliban sa pamamagitan ng paggamot | Ang instrumento ay nauugnay sa paggamot; nakakaapekto lamang sa kinalabasan sa pamamagitan ng paggamot |
| **Sintetikong kontrol** | Bumuo ng may timbang na kumbinasyon ng mga control unit upang tumugma sa ginagamot na unit | Ang synthetic na kontrol ay tumpak na kumakatawan sa counterfactual |
| **Propensity score matching** | Itugma ang ginagamot at kontrol na mga unit na may katulad na probabilidad ng paggamot | Lahat ng confounder ay sinusukat at kasama sa propensity model |
### Difference-in-Differences (Visualized)
| Panahon | Ginagamot na Grupo | Control Group | Pagkakaiba |
|--------|--------------|----------------|------------|
| **Pre-treatment** | Y_t_pre | Y_c_pre | Y_t_pre - Y_c_pre |
| **Pagkatapos ng paggamot** | Y_t_post | Y_c_post | Y_t_post - Y_c_post |
| **Pagtatantya ng DiD** | | | (Y_t_post - Y_t_pre) - (Y_c_post - Y_c_pre) |
---

## Directed Acyclic Graphs (DAGs)
Ang mga DAG ay mga visual na tool para sa pag-encode ng mga sanhi ng pagpapalagay at pagtukoy ng mga confounder.
### Mga Pangunahing Istruktura
| Istraktura | Pattern | Implikasyon |
|-----------|---------|-------------|
| **Kadena** | A → B → C | Ang A at C ay nauugnay sa pamamagitan ng B; ang pagkontrol para sa B ay humaharang sa landas |
| **Fork** | A ← B → C | Ang A at C ay nalilito ni B; ang pagkontrol para sa B ay humaharang sa landas |
| **Collider** | A → B ← C | Ang A at C ay independyente; ang pagkontrol para sa B ay nagbubukas ng landas (lumilikha ng huwad na asosasyon) |
### Mga Panuntunan para sa mga DAG
| Panuntunan | Paglalarawan |
|------|-------------|
| **Backdoor criterion** | Upang matantya ang sanhi ng epekto ng X sa Y, harangan ang lahat ng backdoor path (mga landas na may arrow papunta sa X) sa pamamagitan ng pagkokondisyon sa naaangkop na mga variable |
| **Pantayan sa harap ng pinto** | Kung hindi ma-block ang mga backdoor path, gumamit ng mga tagapamagitan: tantyahin ang X → M → Y sa dalawang yugto |
| **Huwag magkondisyon sa mga nakabangga** | Ang pagkontrol para sa isang karaniwang epekto ay nagbubukas ng isang huwad na landas |
| **Huwag magkondisyon sa mga inapo ng mga nakabangga** | Parehong problema sa conditioning sa mismong collider |
---

## Mga Karaniwang Pitfalls
| Pitfall | Paglalarawan | Halimbawa |
|---------|-------------|---------|
| **Inalis ang variable bias** | Nabigong kontrolin para sa isang confounder | Pagtatantya ng edukasyon → kita nang hindi kinokontrol ang kakayahan |
| **Sobrang pagkontrol** | Pagkondisyon sa isang tagapamagitan o nakabangga | Pagkontrol para sa titulo ng trabaho kapag tinatantya ang edukasyon → kita |
| **Pagkiling sa pagpili** | Pagkondisyon sa isang variable na apektado ng paggamot | Pagsusuri lamang ng mga may trabaho kapag nag-aaral ng pagsasanay → sahod |
| **Immortal time bias** | Maling pag-uuri ng tao-oras sa mga pag-aaral ng cohort | Ang mga pasyente ay dapat mabuhay ng sapat na katagalan upang makatanggap ng paggamot |
| **Regression to the mean** | Ang mga extreme value ay may posibilidad na lumipat patungo sa average | Ang mga pasyenteng may sakit ay bumubuti pagkatapos ng paggamot anuman |
| **Pagkiling pagkatapos ng paggamot** | Pagkondisyon sa mga variable na nangyayari pagkatapos ng paggamot | Pagkontrol para sa mga salungat na kaganapan kapag tinatantya ang bisa ng gamot |
---

## Mga Tool at Aklatan
| Tool | Wika | Paglalarawan |
|------|----------|-------------|
| **Gawin Bakit** | Python | Microsoft library; DAG-based causal inference |
| **CausalML** | Python | Uber's library para sa uplift modeling at causal ML |
| **EconML** | Python | Double ML, causal forest, instrumental variable |
| **linearmodels** | Python | IV, mga modelo ng data ng panel, DiD |
| **MatchIt** | R | Propensity score matching |
| **dagitty** | R / web | pagsusuri ng DAG; tukuyin ang mga hanay ng pagsasaayos |
| **CausalImpact** | R / Python | Bayesian structural time series para sa causal inference |
---

## Buod
Ang causal inference ay tungkol sa paglipat nang lampas sa "kung ano ang nangyari" sa "kung ano ang mangyayari kung ang mga bagay ay naiiba." Ang pangunahing hamon ay hindi natin mapapansin ang parehong mga resulta at hindi ginagamot para sa parehong yunit - ang counterfactual ay palaging nawawala. Niresolba ito ng mga random na eksperimento sa pamamagitan ng paggawang maihahambing ang mga treatment at control group. Kapag hindi posible ang randomization, mga quasi-experimental na pamamaraan — DiD, regression discontinuity, instrumental variable, synthetic control — subukang buuin muli ang counterfactual mula sa observational data. Tumutulong ang mga DAG na gawing tahasan ang mga pagpapalagay at tukuyin ang mga tamang variable na kontrolin. Ang pangunahing kasanayan ay ang pag-iisip nang mabuti tungkol sa proseso ng pagbuo ng data: kung ano ang sanhi, ano ang confounder, ano ang collider, at kung ano ang nangyari sa ilalim ng alternatibo.