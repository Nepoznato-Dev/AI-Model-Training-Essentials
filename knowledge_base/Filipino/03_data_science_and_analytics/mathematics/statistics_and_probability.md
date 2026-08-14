---
# Metadata
title: "Statistics and Probability"
description: "Probability theory, statistical inference, hypothesis testing, regression, and Bayesian methods"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Split from mathematics_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [statistics, probability, hypothesis-testing, regression, bayesian-methods, data-analysis]
difficulty_level: "intermediate"
prerequisites:
  - "../mathematics/mathematics.md"
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Statistics at Probability
Ang probabilidad at istatistika ay ang mathematical na pundasyon ng data science, machine learning, at siyentipikong pananaliksik. Sinasabi sa iyo ng probabilidad kung gaano kalamang ang mga kaganapan; Sinasabi sa iyo ng mga istatistika kung paano gumawa ng mga konklusyon mula sa data. Magkasama, ginagawa nilang nasusukat, mapapamahalaan na kaalaman ang kawalan ng katiyakan.
---

## Teorya ng Probability
### Mga Pangunahing Konsepto
| Konsepto | Paglalarawan | Halimbawa |
|---------|-------------|---------|
| **Sample Space** | Itakda ng lahat ng posibleng resulta | Pag-roll ng die: {1, 2, 3, 4, 5, 6} |
| **Kaganapan** | Isang subset ng sample space | Pag-roll ng even na numero: {2, 4, 6} |
| **Probability** | Numero sa pagitan ng 0 at 1 pagsukat ng posibilidad | P(rolling 6) = 1/6 |
| **Conditional Probability** | P(A|B): ang posibilidad ng A ibinigay na B ay naganap | P(ulan | maulap) |
| **Pagsasarili** | Mga kaganapan kung saan hindi naaapektuhan ng isa ang isa pa | Ang mga coin flips ay independyente |
### Mga Panuntunan sa Probability
| Panuntunan | Formula | Use Case |
|------|---------|----------|
| **Tuntunin sa Pagdaragdag** | P(A ∪ B) = P(A) + P(B) − P(A ∩ B) | Probability ng A o B |
| **Panuntunan ng Multiplikasyon** | P(A ∩ B) = P(A) × P(B|A) | Probability ng A at B |
| **Complement Rule** | P(hindi A) = 1 − P(A) | Probability ng event na hindi naganap |
| **Batas ng Kabuuang Probability** | P(A) = Σ P(A|Bᵢ) × P(Bᵢ) | Paghahati sa pamamagitan ng magkatulad na eksklusibong mga kaganapan |
| **Bayes' Theorem** | P(A|B) = P(B|A) × P(A) / P(B) | Pag-update ng mga paniniwala na may ebidensya |
### Mga Pamamahagi ng Probability
| Pamamahagi | Uri | Mga Pangunahing Parameter | Use Case |
|-------------|------|----------------|----------|
| **Normal (Gaussian)** | Tuloy-tuloy | Mean (μ), Standard deviation (σ) | Natural phenomena, mga error sa pagsukat |
| **Binomial** | Discrete | n (mga pagsubok), p (probability) | Bilang ng tagumpay/kabiguan |
| **Poisson** | Discrete | λ (rate) | Mga bihirang kaganapan sa paglipas ng panahon/espasyo |
| **Exponential** | Tuloy-tuloy | λ (rate) | Oras sa pagitan ng mga kaganapan |
| **Uniporme** | Parehong | a, b (mga hangganan) | Parehong malamang na mga resulta |
| **Chi-Square** | Tuloy-tuloy | k (mga antas ng kalayaan) | Goodness-of-fit na mga pagsubok |
| **t-Pamamahagi** | Tuloy-tuloy | ν (mga antas ng kalayaan) | Maliit na sample na hinuha |
### Mga Pangunahing Katangian ng Mga Pamamahagi
| Ari-arian | Paglalarawan |
|----------|-------------|
| **Mean (Inaasahang Halaga)** | Sentro ng masa ng distribusyon: E[X] = Σ xᵢ × P(xᵢ) |
| **Pagkakaiba** | Kumalat sa paligid ng mean: Var(X) = E[(X − μ)²] |
| **Pamantayang Paglihis** | Square root ng pagkakaiba-iba; parehong mga yunit ng data |
| **Pagipit** | Kawalaan ng simetrya ng pamamahagi |
| **Kurtosis** | "Tailedness" — gaano kabigat ang mga buntot |
---

## Statistical Inference
### Descriptive vs. Inferential Statistics
| | Naglalarawan | Hinuha |
|---|-------------|-------------|
| **Layunin** | Ibuod at ilarawan ang data | Gumawa ng mga konklusyon tungkol sa isang populasyon mula sa isang sample |
| **Mga Tool** | Mean, median, mode, standard deviation, chart | Mga pagsusuri sa hypothesis, mga agwat ng kumpiyansa, regression |
| **Saklaw** | Tanging ang data na mayroon ka | Pag-generalize nang lampas sa iyong sample |
### Balangkas ng Pagsusuri ng Hypothesis
| Hakbang | Paglalarawan |
|------|-------------|
| 1. **Mga hypotheses ng estado** | Null hypothesis (H₀): walang epekto; Alternatibong (H₁): umiiral ang epekto |
| 2. **Pumili ng antas ng kahalagahan** | α = 0.05 (kumbensyonal) |
| 3. **Pumili ng pagsubok** | Batay sa uri ng data, laki ng sample, at mga pagpapalagay |
| 4. **Kalkulahin ang istatistika ng pagsubok** | Depende sa pagsusulit na napili |
| 5. **Hanapin ang p-value** | Ang posibilidad ng pagmamasid sa data kung ang H₀ ay totoo |
| 6. **Magpasya** | Kung p < α, tanggihan ang H₀; kung hindi, mabibigong tanggihan ang H₀ |
### Mga Karaniwang Pagsusuri sa Istatistika
| Pagsubok | Kailan Gagamitin | Ano ang Inihahambing Nito |
|------|-------------|----------------|
| **t-test** | Paghambingin ang paraan ng 1–2 pangkat | Ang ibig sabihin ng (mga) pangkat sa isang halaga o sa bawat isa |
| **Chi-square test** | Pangkategoryang data | Naobserbahan kumpara sa mga inaasahang frequency |
| **ANOVA** | Paghambingin ang paraan ng 3+ na pangkat | Between-group vs. within-group variance |
| **Mann-Whitney U** | Non-parametric na alternatibo sa t-test | Pamamahagi ng ranggo ng dalawang pangkat |
| **Pearson correlation** | Linear na relasyon sa pagitan ng dalawang tuluy-tuloy na variable | r value mula −1 hanggang +1 |
| **Karelasyon ng Spearman** | Monotonic na relasyon (batay sa ranggo) | ρ value para sa ordinal o hindi normal na data |
### Mga Pagitan ng Kumpiyansa
Ang agwat ng kumpiyansa ay nagbibigay ng hanay ng mga posibleng halaga para sa isang parameter ng populasyon:
- **95% CI para sa mean** (kilalang σ): x̄ ± 1.96 × (σ / √n)
- **Interpretasyon**: "Kami ay 95% kumpiyansa na ang totoong populasyon ay nasa loob ng pagitan na ito"
- **Malawak na CI** = mas kawalang-katiyakan (mas maliit na sample, mas mataas na pagkakaiba-iba, o mas mataas na antas ng kumpiyansa)
---

## Pagsusuri ng Pagbabalik
### Mga Uri ng Regression
| Uri | Dependent Variable | Use Case |
|------|--------------------|----------|
| **Linear Regression** | Tuloy-tuloy | Paghuhula ng mga presyo ng bahay, mga benta |
| **Logistic Regression** | Binary (0/1) | Pag-uuri: pagtuklas ng spam, diagnosis ng sakit |
| **Polynomial Regression** | Tuloy-tuloy (kurba) | Mga kurba ng paglago, mga hindi linear na uso |
| **Multiple Regression** | Tuloy-tuloy (2+ predictor) | Pagkontrol para sa mga confounder |
| **Taytay / Lasso** | Tuloy-tuloy (regularized) | Pag-iwas sa overfitting, pagpili ng tampok |
### Mga Pangunahing Kaalaman sa Linear Regression
Ang modelo: **y = β₀ + β₁x + ε**
| Bahagi | Ibig sabihin |
|-----------|---------|
| β₀ (harang) | Halaga ng y kapag x = 0 |
| β₁ (slope) | Baguhin ang y para sa isang unit na pagbabago sa x |
| ε (error term) | Hindi maipaliwanag na pagkakaiba-iba |
**Mga pangunahing sukatan:**
- **R² (coefficient of determination)**: Proporsyon ng variance na ipinaliwanag ng modelo (0 hanggang 1)
- **Inayos na R²**: R² pinarusahan para sa bilang ng mga predictor
- **RMSE**: Root mean squared error — average na error sa hula sa parehong mga unit gaya ng y
### Mga Pagpapalagay ng Linear Regression
| Pagpapalagay | Ano ang Ibig Sabihin Nito | Paano Suriin |
|-----------|--------------|--------------|
| **Linearity** | Ang ugnayan sa pagitan ng X at Y ay linear | Mga scatter plot |
| **Pagsasarili** | Ang mga obserbasyon ay independyente | Disenyo ng pag-aaral |
| **Homoscedasticity** | Patuloy na pagkakaiba-iba ng mga nalalabi | Mga natitirang plot |
| **Normality** | Ang mga nalalabi ay karaniwang ipinamamahagi | Q-Q plot, Shapiro-Wilk test |
| **Walang multicollinearity** | Ang mga manghuhula ay hindi lubos na nakakaugnay | VIF (Variance Inflation Factor) |
---

## Bayesian Statistics
### Frequentist vs. Bayesian
| | Madalas | Bayesian |
|---|-------------|----------|
| **Probability means** | Pangmatagalang dalas | Degree ng paniniwala |
| **Ang mga parameter ay** | Naayos ngunit hindi alam | Mga random na variable na may mga distribusyon |
| **Gumagamit** | p-values, mga pagitan ng kumpiyansa | Mga pamamahagi sa likuran, mapagkakatiwalaang mga pagitan |
| **Lakas** | Layunin, mahusay na itinatag | Incorporates dating kaalaman, intuitive interpretasyon |
### Bayes' Theorem in Practice
**Posterior = (Likelihood × Nauna) / Ebidensya**
Halimbawa — medikal na pagsusuri:
- Pagkalat ng sakit: 1% (nauna)
- Test sensitivity: 95% (true positive rate)
- Pagtitiyak ng pagsubok: 90% (totoong negatibong rate)
- Kung nagpositibo ka: P(sakit | positibo) = (0.95 × 0.01) / (0.95 × 0.01 + 0.10 × 0.99) ≈ 8.8%
Ang counterintuitive na resultang ito — karamihan sa mga positibong resulta ay mga false positive kapag ang sakit ay bihira — ay ang **base rate fallacy**, at ipinapakita nito kung bakit mahalaga ang Bayesian thinking.
---

## Mga Praktikal na Tip
- **Palaging ilarawan ang iyong data** bago magpatakbo ng anumang istatistikal na pagsubok
- **Suriin ang mga pagpapalagay** — ang mga paglabag ay maaaring magpawalang-bisa sa mga resulta
- **Mahalaga ang laki ng epekto** — ang isang makabuluhang resulta sa istatistika ay maaaring halos walang kahulugan
- **Ang ugnayan ay hindi sanhi** — kahit na ang malakas na ugnayan ay maaaring magkaroon ng mga confounder
- **Maraming paghahambing** magpalaki ng mga maling positibong rate — maglapat ng mga pagwawasto (Bonferroni, FDR)
- **Mag-ulat ng mga agwat ng kumpiyansa**, hindi lang mga p-value
---

## Bakit Ito Mahalaga
Ang mga istatistika ay ang backbone ng siyentipikong pananaliksik, analytics ng negosyo, at machine learning. Kung wala ito, hindi mo masasabi ang signal mula sa ingay, matukoy ang mga tunay na epekto mula sa mga random na pagbabago, o gumawa ng mga hula na may hindi tiyak na dami. Sinusuri mo man ang mga pagsubok sa A/B, nagsasanay ng mga modelo ng ML, o nagbabasa ng mga research paper, mahalaga ang statistical literacy.