<!--
---
# Metadata
title: "Time Series and Forecasting"
description: "ARIMA, Prophet, LSTMs, seasonality, anomaly detection"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
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
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
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
tags: [time, series, forecasting, ai-and-machine-learning]
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
# Serye ng Oras at Pagtataya
Ang data ng serye ng oras ay anumang data na nakolekta sa paglipas ng panahon: mga presyo ng stock, pagbabasa ng temperatura, trapiko sa website, mga numero ng benta, mga monitor ng tibok ng puso, pagkonsumo ng enerhiya. Ang pagtataya ay nangangahulugan ng paghula sa mga halaga sa hinaharap batay sa mga nakaraang pattern. Isa ito sa pinakamahalagang aplikasyon ng data science — at isa sa pinakamahirap, dahil ang hinaharap ay talagang hindi tiyak at ang real-world time series ay puno ng ingay, seasonality, at structural break.
---

## Mga Katangian ng Serye ng Oras
| Bahagi | Paglalarawan | Halimbawa |
|-----------|-------------|---------|
| **Uso** | Pangmatagalang pagtaas o pagbaba | Ang mga pandaigdigang temperatura ay tumataas sa paglipas ng mga dekada |
| **Pamanahon** | Regular, predictable pattern sa mga nakapirming agwat | Tumataas ang benta tuwing Disyembre |
| **Pagbibisikleta** | Mga pagbabagu-bago sa mga hindi nakapirming agwat (kadalasang pang-ekonomiya) | Mga recession tuwing 5-10 taon |
| **Ingay (nalalabi)** | Random na variation na hindi maipaliwanag | Araw-araw na paggalaw ng presyo ng stock |
| **Autocorrelation** | Ang mga kasalukuyang halaga ay nakadepende sa mga nakaraang halaga | Ang temperatura ngayon ay katulad ng kahapon |
### Pagkakatigil
Ang isang time series ay **stationary** kung ang mga istatistikal na katangian nito (mean, variance) ay hindi nagbabago sa paglipas ng panahon. Karamihan sa mga pamamaraan ng pagtataya ay ipinapalagay na walang galaw.
| Pagsubok | Layunin |
|------|---------|
| **Augmented Dickey-Fuller (ADF)** | Sinusuri kung may unit root (hindi nakatigil) |
| **KPSS test** | Sinusuri kung trend-stationary ang serye |
| Pagbabagong-anyo | Kailan Gagamitin |
|--------------|-------------|
| **Pagkakaiba** | Alisin ang trend: y'(t) = y(t) - y(t-1) |
| **Mag-log transform** | I-stabilize ang pagkakaiba-iba (para sa exponential growth) |
| **Panahunang pagkakaiba** | Alisin ang seasonality: y'(t) = y(t) - y(t-s) kung saan s ang haba ng season |
---

## Klasikal na Paraan ng Pagtataya
### Mga Moving Average
| Paraan | Paglalarawan | Pinakamahusay Para sa |
|--------|-------------|----------|
| **Simple Moving Average (SMA)** | Average ng huling N obserbasyon | Nagpapadulas ng maingay na data |
| **Weighted Moving Average** | Mas mataas ang timbang ng mga kamakailang obserbasyon | Kapag mas mahalaga ang kamakailang data |
| **Exponential Moving Average (EMA)** | Exponentially nagpapababa ng mga timbang | Pagsubaybay sa mga uso na may mas kaunting lag |
### Exponential Smoothing
| Paraan | Mga Bahagi | Use Case |
|--------|-----------|----------|
| **Simple (SES)** | Level lang | Walang uso, walang seasonality |
| **Holt's (Doble)** | Level + trend | Data na may trend ngunit walang seasonality |
| **Holt-Winters (Triple)** | Level + trend + seasonality | Data na may parehong trend at seasonality |
### ARIMA at Mga Variant
Ang ARIMA (AutoRegressive Integrated Moving Average) ay ang workhorse ng classical na time series na pagtataya.
| Bahagi | Ibig sabihin | Parameter |
|-----------|---------|-----------|
| **AR (p)** | Regress sa nakaraang p value | Gaano karaming mga nakaraang halaga ang gagamitin |
| **Ako (d)** | Bilang ng mga differencing na hakbang para gawing stationary | Ilang beses ang pagkakaiba |
| **MA (q)** | I-modelo ang error bilang kumbinasyon ng mga nakaraang error | Gaano karaming mga nakaraang error ang gagamitin |
| Variant | Extension | Use Case |
|---------|-----------|----------|
| **SARIMA** | Nagdaragdag ng mga seasonal na bahagi (P, D, Q, s) | Data na may malakas na seasonality |
| **ARIMAX** | Nagdaragdag ng mga panlabas na variable | Kapag alam mo ang tungkol sa mga paparating na kaganapan |
| **VAR** | Multivariate ARIMA; maramihang magkakaugnay na serye | Kapag ang mga variable ay nakakaapekto sa isa't isa |
---

## Mga Makabagong ML Approach
### Mga Modelong Nakabatay sa LSTM at RNN
| Modelo | Arkitektura | Pakinabang |
|-------|-------------|-----------|
| **LSTM** | Long Short-Term Memory network | Kinukuha ang long-range na temporal na dependencies |
| **GRU** | Gated Recurrent Unit (mas simpleng LSTM) | Mas mabilis na pagsasanay; katulad na pagganap |
| **Seq2Seq** | Encoder-decoder para sa serye ng oras | Flexible na haba ng input/output |
| **Temporal Convolutional Network (TCN)** | Dilated causal convolutions | Parallel na pagsasanay; mahabang receptive field |
### Propeta (Meta)
Isang praktikal na tool sa pagtataya na idinisenyo para sa serye ng oras ng negosyo.
| Tampok | Paglalarawan |
|---------|-------------|
| **Pagbubulok** | Trend + seasonality + holidays |
| ** Flexible** | Pinangangasiwaan ang nawawalang data, outlier, at structural break |
| **Naipaliwanag** | Ang mga bahagi ay nababasa ng tao |
| **Awtomatiko** | Mga makatwirang default; kaunting tuning ang kailangan |
| Lakas | Limitasyon |
|----------|------------|
| Mahusay para sa mga sukatan ng negosyo (benta, mga user) | Hindi perpekto para sa napakataas na dalas ng data |
| Pinangangasiwaan ang mga pista opisyal at espesyal na kaganapan | Ipinapalagay ang additive o multiplicative seasonality |
| Matatag sa outlier | Hindi gaanong tumpak kaysa sa malalim na pag-aaral para sa mga kumplikadong pattern |
### Mga Modelong Nakabatay sa Transformer
| Modelo | Pangunahing Tampok |
|-------|-------------|
| **Informer** | ProbSparse pansin para sa mahabang sequence |
| **Autoformer** | Auto-correlation mechanism para sa series decomposition |
| **PatchTST** | Mga patch sa serye ng oras; channel-independent |
| **TimesFM** (Google) | Modelo ng pundasyon para sa serye ng oras; pre-trained sa magkakaibang data |
| **Chronos** (Amazon) | Tokenise time series; gumagamit ng LLM-style architecture |
---

## Anomaly Detection sa Time Series
Pag-detect ng mga hindi pangkaraniwang pattern na lumilihis sa inaasahang pag-uugali.
| Paraan | Diskarte | Use Case |
|--------|----------|----------|
| **Istatistika** | Z-score, IQR, mga control chart | Simple, mahusay na nauunawaan |
| **Isolation Forest** | Nakabatay sa puno; ibinubukod ang mga anomalya sa pamamagitan ng random na paghahati | Multivariate anomaly detection |
| **LOF** (Local Outlier Factor) | Nakabatay sa density; inihahambing ang lokal na density sa mga kapitbahay | Kapag ang mga anomalya ay nasa mga low-density na rehiyon |
| **Autoencoders** | Error sa muling pagtatayo; mataas na error = anomalya | Kumplikado, hindi linear na mga pattern |
| **LSTM-based** | Hulaan ang susunod na hakbang; malaking pagkakamali sa hula = anomalya | Mga sequential anomalya |
### Mga Application
| Domain | Ano ang Kahulugan ng mga Anomalya |
|--------|--------------------|
| **Pananalapi** | Panloloko, pag-crash ng market, pag-crash ng flash |
| **Pangangalaga sa kalusugan** | Abnormal na tibok ng puso, simula ng seizure |
| **Paggawa** | Kabiguan ng kagamitan, mga depekto sa kalidad |
| **Cybersecurity** | Mga pagtatangka sa pagpasok, pag-atake ng DDoS |
| **Imprastraktura** | Overload ng server, mga pagkabigo sa network |
---

## Mga Sukatan ng Pagsusuri
| Sukatan | Formula (konsepto) | Kailan Gagamitin |
|--------|---------------------|-------------|
| **MAE** (Mean Absolute Error) | Average ng ganap na mga error | Interpretable; parehong mga yunit ng data |
| **RMSE** (Root Mean Squared Error) | Square root ng average na squared errors | Mas pinarurusahan ang malalaking error |
| **MAPE** (Mean Absolute Percentage Error) | Average ng ganap na porsyento ng mga error | Kapag mahalaga ang kamag-anak na error |
| **SMAPE** (Symmetric MAPE) | Symmetric na bersyon ng MAPE | Mas mahusay na pinangangasiwaan ang mga value na malapit sa zero |
| **MASE** (Mean Absolute Scaled Error) | MAE na may kaugnayan sa isang walang muwang na hula | Paghahambing sa iba't ibang serye |
---

## Praktikal na Daloy ng Trabaho
| Hakbang | Paglalarawan |
|------|-------------|
| **1. I-explore** | I-plot ang serye; tukuyin ang trend, seasonality, outliers |
| **2. Mabulok** | Paghiwalayin sa trend, seasonal, at natitirang bahagi |
| **3. Stationarise** | Ilapat ang differencing o pagbabago kung kinakailangan |
| **4. Hati** | Time-based split (hindi kailanman random na split para sa time series) |
| **5. Baseline** | Magsimula sa isang walang muwang na hula (huling halaga, pana-panahong walang muwang) |
| **6. Modelo** | Subukan ang mga klasikal na pamamaraan (ARIMA, Propeta), pagkatapos ay ang mga pamamaraan ng ML |
| **7. Suriin** | Gumamit ng mga naaangkop na sukatan; ihambing sa baseline |
| **8. Ulitin** | Magdagdag ng mga feature, subukan ang iba't ibang modelo, i-tune ang mga hyperparameter |
---

## Mga Tool at Aklatan
| Tool | Layunin |
|------|---------|
| **statsmodels** | Klasikong serye ng oras (ARIMA, ETS, decomposition) |
| **Propeta** (Meta) | Pagtataya ng serye ng oras ng negosyo |
| **sktime** | Pinag-isang interface ng ML para sa serye ng oras |
| **Mga Darts** | Comprehensive forecasting library (classical + deep learning) |
| **GluonTS** (Amazon) | Probabilistic time series modelling |
| **NeuralProphet** | Propeta na may mga bahagi ng neural network |
| **tsfresh** | Awtomatikong pagkuha ng tampok na serye ng oras |
| **pandas** | Pagmamanipula at resampling ng serye ng oras |
---

## Buod
Pinagsasama ng pagtataya ng serye ng oras ang mga klasikal na istatistika sa modernong machine learning. Ang mga klasikal na pamamaraan (ARIMA, exponential smoothing, Propeta) ay nabibigyang-kahulugan, mabilis, at kadalasang tumpak. Ang mga deep learning method (LSTM, Transformers) ay kumukuha ng mga kumplikadong pattern ngunit nangangailangan ng higit pang data at pag-tune. Ang mga pangunahing prinsipyo ay nananatiling pareho anuman ang pamamaraan: unawain ang istraktura ng iyong data (trend, seasonality, ingay), ihambing sa isang simpleng baseline, suriin gamit ang mga naaangkop na sukatan, at isaalang-alang ang katotohanan na ang hinaharap ay hindi eksaktong uulitin ang nakaraan.