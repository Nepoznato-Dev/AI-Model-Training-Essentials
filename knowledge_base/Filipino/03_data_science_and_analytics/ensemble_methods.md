---
# Metadata
title: "Ensemble Methods"
description: "Bagging, boosting, stacking, voting, random forests, XGBoost"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ensemble, methods, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Mga Paraan ng Ensemble
Pinagsasama-sama ng mga pamamaraan ng ensemble ang maraming modelo ng machine learning para makagawa ng mas mahuhusay na hula kaysa sa anumang solong modelo na maaaring makamit nang mag-isa. Ang intuwisyon ay diretso: kung mayroon kang ilang mga modelo na ang bawat isa ay medyo tumpak ngunit gumagawa ng iba't ibang mga error, ang pagsasama-sama ng kanilang mga hula ay magkansela ng mga indibidwal na pagkakamali at magbubunga ng mas matatag na resulta. Ang mga ensemble ay nasa likod ng karamihan sa mga mapagkumpitensyang solusyon sa pag-aaral ng makina at nananatiling ilan sa mga pinaka maaasahang diskarte sa mga sistema ng produksyon.
---

## Bakit Nagtatrabaho ang Ensembles
| Prinsipyo | Paglalarawan |
|-----------|-------------|
| **Karunungan ng maraming tao** | Maramihang hindi perpektong pagtatantya, na-average, ay mas mahusay kaysa sa anumang solong pagtatantya |
| **Bias-variance trade-off** | Maaaring bawasan ng mga ensemble ang pagkakaiba-iba (bagging) o bias (boosting) nang hindi isinasakripisyo ang iba pang |
| **Pagkakaiba-iba ng error** | Kung ang mga modelo ay gumawa ng iba't ibang mga error, ang pagsasama-sama ng mga ito ay makakakansela ng mga indibidwal na pagkakamali |
| **Pagpapakinis ng hangganan ng desisyon** | Lumilikha ang maraming modelo ng mas matatag na ibabaw ng desisyon kaysa sa isang modelo |
---

## Bagging (Bootstrap Aggregating)
### Paano Ito Gumagana
| Hakbang | Paglalarawan |
|------|-------------|
| **1. Bootstrap sampling** | Gumuhit ng maraming random na sample (na may kapalit) mula sa data ng pagsasanay |
| **2. Mga modelo ng base ng tren** | Sanayin ang isang modelo sa bawat sample ng bootstrap (karaniwang mga puno ng desisyon) |
| **3. Pinagsama-sama** | Para sa regression: average na mga hula. Para sa pag-uuri: boto ng karamihan |
### Mga Pangunahing Katangian
| Katangian | Paglalarawan |
|--------------|-------------|
| **Binabawasan ang pagkakaiba** | Ang pag-average ay nagpapakinis ng mga indibidwal na pagbabago ng modelo |
| **Parallel na pagsasanay** | Ang bawat batayang modelo ay independiyente; maaaring sanayin nang sabay-sabay |
| **Pagsusuri sa labas ng bag** | Ang bawat sample ay naiwan sa ilang mga sample ng bootstrap; gamitin ang mga iyon para sa pagpapatunay |
| **Dekorasyon** | Ang random na pagpili ng feature sa bawat split ay binabawasan ang ugnayan sa pagitan ng mga puno |
### Random na Kagubatan
| Aspeto | Paglalarawan |
|--------|--------------|
| **Base learner** | Mga puno ng desisyon |
| **Susing karagdagan** | Sa bawat hati, isaalang-alang lamang ang isang random na subset ng mga tampok (karaniwang sqrt(n_features)) |
| **Bakit ito gumagana** | Ang pagpili ng random na tampok ay nag-uugnay sa mga puno, na ginagawang mas matatag ang grupo |
| **Mga Hyperparameter** | Bilang ng mga puno; max depth; min sample bawat dahon; max na mga tampok |
| **Lakas** | Pinangangasiwaan ang high-dimensional na data; matatag sa outliers; nagbibigay ng kahalagahan ng tampok |
| **Kahinaan** | Hindi gaanong maipaliwanag kaysa sa mga punong kahoy; maaaring mag-overfit sa maingay na mga gawain sa regression |
---

## Pagpapalakas
### Paano Ito Gumagana
| Hakbang | Paglalarawan |
|------|-------------|
| **1. Sanayin ang unang modelo** | Sanayin ang isang batayang modelo (kadalasan ay isang mababaw na puno / "stump") sa data |
| **2. Tukuyin ang mga error** | Hanapin kung aling mga pagkakataon ang modelo ay nagkamali |
| **3. Sanayin ang susunod na modelo** | Sanayin ang isang bagong modelo na nakatuon sa mga pagkakamali (muling natimbang o nalalabi) |
| **4. Pagsamahin nang sunud-sunod** | Itinatama ng bawat bagong modelo ang mga naipon na error ng lahat ng nakaraang modelo |
| **5. Ulitin** | Magpatuloy para sa isang tinukoy na bilang ng mga round |
### Pagpapalakas ng Algorithms
| Algorithm | Pag-andar ng Pagkawala | Pangunahing Tampok |
|-----------|--------------|-------------|
| **AdaBoost** | Exponential | Re-weights misclassified mga pagkakataon; simple; sensitibo sa ingay |
| **Gradient Boosting** | Anumang naiba-iba na pagkawala | Umaangkop sa mga nalalabi (gradient ng pagkawala); mas nababaluktot |
| **XGBoost** | Regularized gradient boosting | L1/L2 regularisasyon; second-order gradients; pag-optimize ng hardware |
| **LightGBM** | Nakabatay sa gradient na one-side sampling | Paglago ng dahon; batay sa histogram; mabilis sa malalaking dataset |
| **CatBoost** | Nag-order ng pagpapalakas | Pinangangasiwaan ang mga tampok na kategorya nang natively; binabawasan ang overfitting |
### Boosting vs Bagging
| Dimensyon | Bagging | Pagpapalakas |
|-----------|---------|----------|
| **Pagsasanay** | Parallel | Sequential |
| **Pokus** | Binabawasan ang pagkakaiba | Binabawasan ang bias |
| **Mga base na modelo** | High-variance, low-bias (malalim na puno) | Low-variance, high-bias (mababaw na puno / tuod) |
| **Kumbinasyon** | Pantay na timbang | Natimbang ayon sa pagganap |
| **Overfitting** | Hindi gaanong madaling kapitan ng sakit | Maaaring mag-overfit kung masyadong maraming round |
| **Pagiging sensitibo sa ingay** | Matatag | Sensitibo sa maingay na data |
---

## Nakasalansan
### Paano Ito Gumagana
| Hakbang | Paglalarawan |
|------|-------------|
| **1. Mga modelo ng base ng tren** | Sanayin ang magkakaibang modelo (hal., random na kagubatan, SVM, neural network, gradient boosting) |
| **2. Bumuo ng mga hula** | Gumamit ng mga out-of-fold na hula (cross-validation) bilang input feature |
| **3. Sanayin ang meta-model** | Sanayin ang pangalawang antas na modelo sa mga hula ng batayang modelo |
| **4. Panghuling hula** | Ang mga base na modelo ay hinuhulaan; meta-modelo pinagsasama ang kanilang mga hula |
### Mga Pinakamahuhusay na Kasanayan sa Pag-stack
| Magsanay | Dahilan |
|----------|--------|
| **Gumamit ng magkakaibang baseng modelo** | Ang iba't ibang mga algorithm ay gumagawa ng iba't ibang mga error; pagkakaiba-iba ay ang buong punto |
| **Gumamit ng cross-validation para sa mga batayang hula** | Pinipigilan ang meta-model mula sa pag-aaral na pagsamantalahan ang mga overfit na base model |
| **Panatilihing simple ang meta-model** | Logistic regression o mababaw na puno; ang mga batayang modelo ay gumagawa ng mabigat na pag-aangat |
| **Isama ang mga raw na feature sa meta-model** | Minsan nakakatulong na bigyan din ang meta-model ng access sa mga orihinal na feature |
---

## Pagboto at Pag-average
### Mahirap na Pagboto (Pag-uuri)
| Modelo | Hula |
|-------|-----------|
| Modelo A | Klase 1 |
| Modelo B | Klase 0 |
| Modelo C | Klase 1 |
| **Boto ng karamihan** | **Klase 1** |
### Malambot na Pagboto (Pag-uuri)
| Modelo | P(Class 0) | P(Class 1) |
|-------|-----------|-----------|
| Modelo A | 0.3 | 0.7 |
| Modelo B | 0.6 | 0.4 |
| Modelo C | 0.4 | 0.6 |
| **Karaniwan** | **0.43** | **0.57** |
| **Paghula** | | **Klase 1** |
### Weighted Averaging
| Modelo | Timbang | Hula |
|-------|--------|-----------|
| Modelo A | 0.5 | 0.8 |
| Modelo B | 0.3 | 0.6 |
| Modelo C | 0.2 | 0.9 |
| **Weighted average** | | 0.5×0.8 + 0.3×0.6 + 0.2×0.9 = 0.76 |
---

## Praktikal na Patnubay
### Kailan Gamitin ang Aling Ensemble
| Sitwasyon | Inirerekomendang Paraan |
|----------|--------------------|
| **Mabilis na baseline; data ng talahanayan** | Random Forest |
| ** Pinakamataas na katumpakan; data ng talahanayan** | XGBoost / LightGBM / CatBoost |
| **Maingay na data** | Bagging (mapapalaki ang ingay ng pagpapalakas) |
| **Kailangan ang pagbibigay-kahulugan** | Isang modelo o maliit na grupo na may kahalagahan ng tampok |
| **Magkakaibang uri ng modelo** | Pagsasalansan o pagboto |
| **Online na pag-aaral** | Mga pamamaraan ng streaming ensemble; adaptive boosting |
| **Hindi balanseng data** | Balanseng Random Forest; cost-sensitive boosting |
### Ensemble Diversity Strategies
| Diskarte | Paglalarawan |
|----------|-------------|
| **Iba't ibang algorithm** | Pagsamahin ang tree-based, linear, at neural na mga modelo |
| **Iba't ibang feature** | Sanayin ang mga modelo sa iba't ibang feature subset |
| **Iba't ibang data subset** | Bagging; subsampling |
| **Iba't ibang hyperparameter** | Parehong algorithm na may iba't ibang configuration |
| **Iba't ibang yugto ng panahon** | Magsanay sa iba't ibang mga window ng oras |
---

## Buod
Gumagana ang mga pamamaraan ng ensemble dahil pinagsama-sama ng mga ito ang maraming hindi perpektong modelo sa isang solong mahusay na predictor. Binabawasan ng bagging (random forest) ang pagkakaiba-iba sa pamamagitan ng mga modelo ng pagsasanay na kahanay sa mga sample ng bootstrap at pag-average. Ang Boosting (XGBoost, LightGBM, CatBoost) ay binabawasan ang bias sa pamamagitan ng mga modelo ng pagsasanay nang sunud-sunod, bawat isa ay nagwawasto sa mga nakaraang error. Gumagamit ang stacking ng meta-model upang pagsamahin ang magkakaibang mga base na modelo. Ang pagboto at pag-average ay ang pinakasimpleng ensemble. Ang karaniwang thread ay pagkakaiba-iba: pinakamahusay na gumagana ang mga ensemble kapag ang kanilang mga component model ay indibidwal na makatwiran ngunit gumawa ng iba't ibang mga error. Sa pagsasagawa, ang gradient boosting sa tabular data ay kadalasan ang pinakamataas na gumaganap na solong diskarte, habang ang pagsasalansan ng magkakaibang mga modelo ay nagtutulak ng higit pang katumpakan sa mga kumpetisyon at mga application na may mataas na stakes.