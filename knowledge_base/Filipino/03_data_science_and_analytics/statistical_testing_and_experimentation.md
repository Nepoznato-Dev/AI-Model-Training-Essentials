---
# Metadata
title: "Statistical Testing and Experimentation"
description: "Hypothesis testing, A/B testing, effect size, causal inference"
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
tags: [statistical, testing, experimentation, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Statistical Testing at Experimentation
Ang mga istatistika ay ang gramatika ng agham. Nagbibigay ito sa iyo ng mga tool upang makilala ang mga tunay na pattern mula sa random na ingay, upang masukat kung ang isang pagbabago ay talagang nagpabuti ng mga bagay, at upang gumawa ng mga desisyon sa ilalim ng kawalan ng katiyakan. Sinasaklaw ng file na ito ang mga pangunahing konsepto ng pagsubok sa hypothesis, pang-eksperimentong disenyo, at ang mga karaniwang pitfalls na nagtutulak sa mga tao.
---

## Ang Balangkas ng Pagsusuri ng Hypothesis
Ang bawat pagsusulit sa istatistika ay sumusunod sa parehong lohika:
1. **Sabihin ang null hypothesis (H₀)**: Walang epekto / walang pagkakaiba.
2. **Sabihin ang alternatibong hypothesis (H₁)**: May epekto / pagkakaiba.
3. **Pumili ng antas ng kabuluhan (α)**: Karaniwang 0.05 (5% ang posibilidad ng false positive).
4. **Kolekta ng data at kalkulahin ang isang istatistika ng pagsubok**.
5. **Kalkulahin ang p-value**: Probability na maobserbahan ang resultang ito (o mas matinding) kung totoo ang H₀.
6. **Gumawa ng desisyon**: Kung p < α, tanggihan ang H₀ (statistikong makabuluhan). Kung hindi, mabigong tanggihan ang H₀.
### Mga Pangunahing Konsepto
| Konsepto | Ibig sabihin | Karaniwang Maling Palagay |
|---------|---------|---------------------|
| **p-value** | P(ang data \| H₀ ay totoo) | HINDI "ang posibilidad na ang H₀ ay totoo" |
| **α (antas ng kahalagahan)** | Threshold para sa pagtanggi sa H₀ | Hindi sukatan ng kahalagahan ng epekto |
| **Istatistikong kahalagahan** | Ang resulta ay hindi malamang dahil sa pagkakataon lamang | HINDI ba nangangahulugang praktikal na makabuluhang |
| **Laki ng epekto** | Laki ng naobserbahang epekto | Hiwalay sa p-value; ang isang maliit na epekto ay maaaring maging makabuluhan sa malaking N |
| **Kapangyarihan** | Ang posibilidad ng wastong pagtanggi sa isang maling H₀ | Karaniwang naglalayon ng 80%+ |
| **Confidence interval** | Saklaw ng mga posibleng halaga para sa parameter | Ang 95% CI ay hindi nangangahulugang "95% na posibilidad na ang tunay na halaga ay nasa hanay na ito" |
---

## Mga Uri ng Error
| | Ang H₀ ay Totoo | Ang H₀ ay Mali |
|---|-----------|-------------|
| **Tanggihan ang H₀** | Type I Error (false positive) | ✅ Tama (true positive) |
| **Nabigong tanggihan ang H₀** | ✅ Tama (true negative) | Type II Error (false negative) |
| Error | Simbolo | Ibig sabihin |
|-------|--------|---------|
| **Uri I** | α | Concluding may epekto kapag walang |
| **Uri II** | β | Walang tunay na epekto |
---

## Pagpili ng Tamang Pagsusulit
| Sitwasyon | Pagsubok | Mga pagpapalagay |
|----------|------|-------------|
| Paghambingin ang paraan ng 2 pangkat | **t-test** (independent) | Normal na distribusyon, pantay na pagkakaiba |
| Paghambingin ang paraan ng magkapares na mga obserbasyon | **Paired t-test** | Ang mga pagkakaiba ay karaniwang ipinamamahagi |
| Paghambingin ang paraan ng 3+ na pangkat | **ANOVA** | Normal na distribusyon, pantay na pagkakaiba |
| Ikumpara ang mga kategoryang distribusyon | **Chi-square test** | Sapat na laki ng sample bawat cell |
| Paghambingin ang mga distribusyon (non-parametric) | **Mann-Whitney U** | Walang normality assumption |
| Paghambingin ang 3+ na pangkat (non-parametric) | **Kruskal-Wallis** | Walang normality assumption |
| Subukan ang ugnayan | **Pearson** (linear) o **Spearman** (monotonic) | Pearson: normalidad; Spearman: batay sa ranggo |
| Subukan kung ang data ay sumusunod sa isang pamamahagi | **Kolmogorov-Smirnov** | Patuloy na data |
### Parametric vs Non-Parametric
| | Parametric | Non-Parametric |
|---|-----------|----------------|
| **Mga pagpapalagay** | Ang data ay sumusunod sa isang partikular na distribusyon (karaniwan ay normal) | Walang palagay na pamamahagi |
| **Kapangyarihan** | Mas mataas kapag natugunan ang mga pagpapalagay | Mas mababa, ngunit mas matatag |
| **Kailan gagamitin** | Malaking sample, tinatayang normal na data | Maliit na sample, skewed data, ordinal data |
---

## Mga Detalyadong Pagsusuri
### t-Pagsusulit
Pinaghahambing ang paraan ng dalawang pangkat.
| Variant | Use Case |
|---------|----------|
| **Independent t-test** | Dalawang magkahiwalay na grupo (paggamot vs kontrol) |
| **Paired t-test** | Ang parehong pangkat ay sinukat ng dalawang beses (bago vs pagkatapos) |
| **Isang sample na t-test** | Ihambing ang isang sample na ibig sabihin sa isang kilalang halaga |
```python
from scipy import stats

# Independent t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b)
```

### ANOVA (Pagsusuri ng Pagkakaiba)
Pinaghahambing ang ibig sabihin sa 3 o higit pang mga pangkat. Sinusuri kung hindi bababa sa isang grupo ang ibig sabihin ay naiiba sa iba.
| Uri | Disenyo |
|------|--------|
| **One-way ANOVA** | Isang independent variable na may 3+ level |
| **Two-way ANOVA** | Dalawang malayang variable; sumusubok sa mga epekto ng pakikipag-ugnayan |
| **Mga Paulit-ulit na Panukala ANOVA** | Parehong paksa na sinusukat sa ilalim ng magkaibang kundisyon |
Kung makabuluhan ang ANOVA, mag-follow up gamit ang **post-hoc tests** (Tukey's HSD) para malaman kung aling mga partikular na grupo ang naiiba.
### Chi-Square Test
Sinusuri kung ang dalawang kategoryang variable ay independyente.
| Use Case | Halimbawa |
|----------|---------|
| **Pagsubok sa kalayaan** | Nauugnay ba ang kasarian sa kagustuhan sa produkto? |
| **Goodness of fit** | Ang isang die roll ba ay sumusunod sa isang pare-parehong pamamahagi? |
**Rule of thumb**: ang bawat cell ay dapat magkaroon ng inaasahang bilang na hindi bababa sa 5.
---

## Pagsusuri ng A/B
Ang A/B testing ay ang aplikasyon ng hypothesis testing sa mga desisyon sa negosyo — karaniwang inihahambing ang isang control (A) sa isang variant (B).
### Proseso ng Disenyo
| Hakbang | Paglalarawan |
|------|-------------|
| **1. Tukuyin ang hypothesis** | "Ang pagpapalit ng kulay ng button mula sa asul patungo sa berde ay magpapataas ng click-through rate" |
| **2. Pumili ng sukatan** | Pangunahin: click-through rate. Pangalawa: rate ng conversion, kita. |
| **3. Kalkulahin ang laki ng sample** | Batay sa pinakamababang nakikitang epekto, kapangyarihan (80%), at kabuluhan (5%) |
| **4. Randomise** | Random na italaga ang mga user na kontrolin at gamutin |
| **5. Patakbuhin ang eksperimento** | Mangolekta ng data hanggang sa maabot ang target na laki ng sample |
| **6. Pag-aralan** | Ihambing ang mga sukatan gamit ang naaangkop na istatistikal na pagsubok |
| **7. Magpasya** | Ipatupad kung istatistikal at praktikal na makabuluhan |
### Pagkalkula ng Laki ng Sample
Ang laki ng sample na kailangan mo ay depende sa:
| Salik | Epekto sa Laki ng Sample |
|--------|----------------------|
| **Mas maliit na epekto upang makita** | Kailangan ng higit pang mga sample |
| **Mas mataas na kapangyarihan** | Kailangan ng higit pang mga sample |
| **Mababang antas ng kahalagahan** | Kailangan ng higit pang mga sample |
| **Mas mataas na pagkakaiba** | Kailangan ng higit pang mga sample |
### Mga Karaniwang Pagkakamali sa Pagsubok ng A/B
| Pagkakamali | Bakit Mali |
|---------|----------------|
| **Maagang sumilip** | Ang pagsuri sa mga resulta araw-araw ay nagpapalaki ng false positive rate |
| **Maraming sukatan nang walang pagwawasto** | Sinusuri ang 20 sukatan sa α=0.05 → asahan ang 1 false positive kapag nagkataon |
| **Paghinto bago ang target na N** | Hindi matukoy ng underpowered na pagsubok ang mga tunay na epekto |
| **Hindi pinapansin ang seasonality** | Pagpapatakbo ng pagsusulit sa panahon ng bakasyon kumpara sa normal na linggo |
| **Hindi random na pagtatalaga** | Bias sa pagpili (hal., pagtatalaga ng mga bagong user sa paggamot) |
| **Nakakagulo ang kahalagahan sa kahalagahan** | Ang 0.1% na pagtaas ay maaaring makabuluhan ayon sa istatistika ngunit hindi sulit na ipadala |
---

## Maramihang Paghahambing
Kapag nagpatakbo ka ng maraming pagsubok nang sabay-sabay, ang pagkakataon na magkaroon ng kahit isang maling positibong resulta ay tumataas nang husto.
| Bilang ng mga Pagsusulit | Probability ng ≥1 False Positive (sa α=0.05) |
|----------------|------------------------------------------------|
| 1 | 5% |
| 5 | 23% |
| 10 | 40% |
| 20 | 64% |
### Mga pagwawasto
| Paraan | Paano Ito Gumagana | Kailan Gagamitin |
|--------|-------------|-------------|
| **Bonferroni** | Hatiin ang α sa bilang ng mga pagsubok (α/n) | Konserbatibo; ilang paghahambing |
| **Holm-Bonferroni** | Step-down na pamamaraan; hindi gaanong konserbatibo | Pangkalahatang paggamit |
| **Benjamini-Hochberg (FDR)** | Kinokontrol ang maling rate ng pagtuklas | Maraming pagsubok; pagsusuri ng eksplorasyon |
---

## Laki ng Epekto
Sinasabi sa iyo ng mga P-values ​​*kung* may epekto. Ang laki ng epekto ay nagsasabi sa iyo *kung gaano ito kalaki.
| Sukatin | Para sa | Interpretasyon |
|---------|-----|----------------|
| **Cohen's d** | Pagkakaiba sa pagitan ng dalawang ibig sabihin | 0.2 = maliit, 0.5 = katamtaman, 0.8 = malaki |
| **Pearson's r** | Kaugnayan | 0.1 = maliit, 0.3 = katamtaman, 0.5 = malaki |
| **η² (eta-squared)** | ANOVA | 0.01 = maliit, 0.06 = katamtaman, 0.14 = malaki |
| **Odds Ratio** | Pangkategoryang resulta | 1.0 = walang epekto; >1 o <1 = epekto |
**Palaging iulat ang laki ng epekto kasama ng mga p-value.** Ang isang resulta ay maaaring makabuluhan ayon sa istatistika ngunit halos walang kahulugan.
---

## Bayesian vs Frequentist
| Aspeto | Madalas | Bayesian |
|--------|------------|----------|
| **Probability** | Pangmatagalang dalas ng mga kaganapan | Degree ng paniniwala |
| **Mga Parameter** | Naayos ngunit hindi alam | Mga random na variable na may mga distribusyon |
| **Gumagamit** | p-values, confidence interval, hypothesis tests | Mga pamamahagi sa likuran, mapagkakatiwalaang mga pagitan |
| **Nakaraan** | Walang naunang paniniwala na isinama | Ang tahasang paunang pamamahagi |
| **Interpretasyon** | "Kung inulit natin ang eksperimentong ito ng maraming beses..." | "Given the data, the probability that..." |
| **Lakas** | Layunin, mahusay na itinatag, simple | Intuitive na interpretasyon, isinasama ang dating kaalaman |
| **Kahinaan** | p-values ​​malawak na hindi nauunawaan | Ang pagpili ng nauna ay maaaring subjective |
---

## Mga Pangunahing Kaalaman sa Sanhi ng Hinuha
Ang ugnayan ay hindi sanhi. Ngunit minsan kailangan mong malaman *kung si X ang sanhi ng Y*, hindi lang kung nauugnay sila.
| Paraan | Paglalarawan | Kailan Gagamitin |
|--------|-------------|-------------|
| **Mga random na eksperimento** | Pamantayan ng ginto; inaalis ng random na pagtatalaga ang mga confounder | Kapag maaari mong randomise |
| **Difference-in-Differences (DiD)** | Ikumpara ang mga pagbabago sa paglipas ng panahon sa pagitan ng paggamot at kontrol | Mga pagbabago sa patakaran, natural na mga eksperimento |
| **Regression Discontinuity (RDD)** | Gamitin ang isang cutoff threshold | Mga iskolarsip, mga limitasyon sa pagiging karapat-dapat |
| **Mga Instrumental na Variable (IV)** | Gumamit ng instrumento na nakakaapekto sa paggamot ngunit hindi direktang kinalabasan | Kapag hindi posible ang randomization |
| **Propensity Score Matching** | Itugma ang ginagamot at kontrolin ang mga unit sa mga naobserbahang katangian | Obserbasyonal na pag-aaral |
---

## Mga Karaniwang Pagkakamali sa Istatistika
| Pagkakamali | Paglalarawan |
|---------|-------------|
| **p-hacking** | Sinusubukan ang maraming pagsusuri hanggang sa makita mo ang p < 0.05 |
| **HAY** | Hypothesising Pagkatapos Malaman ang mga Resulta |
| **Survivorship bias** | Tinitingnan lamang ang mga tagumpay (hal., matagumpay na kumpanya) |
| **Kabalintunaan ni Simpson** | Bumabaliktad ang trend kapag pinagsama-sama ang data kumpara sa hinati ayon sa pangkat |
| **Base rate kapabayaan** | Hindi pinapansin ang naunang posibilidad kapag binibigyang kahulugan ang mga resulta |
| **Ecological fallacy** | Paghihinuha ng indibidwal na pag-uugali mula sa data sa antas ng pangkat |
| **Nalilito** | Ipinapaliwanag ng ikatlong variable ang naobserbahang relasyon |
| **Overfitting** | Kinukuha ng modelo ang ingay, hindi signal |
---

## Buod
Ang pagsusuri sa istatistika ay tungkol sa paggawa ng mga desisyon sa ilalim ng kawalan ng katiyakan nang may katapatan sa intelektwal. Palaging sabihin ang iyong mga hypotheses bago mangolekta ng data. Piliin ang tamang pagsubok para sa iyong uri ng data. Iulat ang mga laki ng epekto, hindi lang mga p-value. Tama para sa maraming paghahambing. At tandaan: ang istatistikal na kahalagahan ay hindi katulad ng praktikal na kahalagahan.