---
# Metadata
title: "Feature Engineering"
description: "Transformations, encodings, feature selection, dimensionality reduction"
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
tags: [feature, engineering, data-science-and-analytics]
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

# Feature Engineering
Ang feature engineering ay ang proseso ng pagbabago ng raw data sa mga representasyon na ginagawang mas epektibo ang mga modelo ng machine learning. Madalas itong inilalarawan bilang pinakamahalagang hakbang sa pipeline ng ML — ang mga feature na ibinibigay mo sa isang modelo ay mas mahalaga kaysa sa algorithm na pipiliin mo. Ang isang simpleng modelo na may mahusay na pagkakagawa ng mga tampok ay karaniwang hihigit sa isang kumplikadong modelo na may hilaw, hindi naprosesong mga input. Ang sining ay nakasalalay sa pag-unawa sa parehong domain at sa data nang sapat upang lumikha ng mga senyales na matututuhan ng modelo.
---

## Bakit Mahalaga ang Feature Engineering
| Salik | Epekto |
|--------|--------|
| **Kalidad ng signal** | Mas mahusay na mga tampok = mas malinaw na mga pattern para matutunan ng modelo |
| **Pagiging simple ng modelo** | Hinahayaan ng magagandang feature ang mas simpleng mga modelo na gumanap nang maayos; mas kaunting pangangailangan para sa mga kumplikadong arkitektura |
| **Bilis ng pagsasanay** | Mas mabilis na nagsasama-sama ang mga nauugnay at mahusay na sukat na feature |
| **Paglalahat** | Ang mga feature na may kaalaman sa domain ay tumutulong sa mga modelo na gumana sa hindi nakikitang data |
| **Pagbibigay-kahulugan** | Ang mga makabuluhang feature ay mas madaling ipaliwanag sa mga stakeholder |
---

## Mga Uri ng Mga Pagbabagong Tampok
### Mga Pagbabagong Numerikal
| Pagbabagong-anyo | Formula / Paglalarawan | Kailan Gagamitin |
|--------------|----------------------|-------------|
| **Mag-log transform** | log(x) o log(x + 1) | Pakanan ang mga pamamahagi; halaga ng pera |
| **Square root** | sqrt(x) | Katamtamang hilig; bilangin ang data |
| **Box-Cox** | Parametric transform na nakakahanap ng pinakamahusay na power transformation | Ginagawang mas normal na ipinamamahagi ang data |
| **Yeo-Johnson** | Tulad ng Box-Cox ngunit pinangangasiwaan ang mga negatibong halaga | Nakabaluktot na data na may mga negatibong halaga |
| **Pag-standardize** | (x - mean) / std | Mga tampok na may iba't ibang mga kaliskis; mga algorithm na ipinapalagay ang normalidad |
| **Min-max scaling** | (x - min) / (max - min) | Mga tampok na nagbubuklod sa [0, 1]; mga halaga ng pixel ng larawan |
| **Matatag na pag-scale** | (x - median) / IQR | Data na may mga outlier |
| **Binning** | I-convert ang tuloy-tuloy sa kategoryang | Non-linear na relasyon; mga puno ng desisyon |
| **Mga tampok na polynomial** | x², x³, x₁×x₂ | Pagkuha ng mga non-linear na relasyon sa mga linear na modelo |
### Mga Kategorya na Encoding
| Encoding | Paglalarawan | Kailan Gagamitin |
|----------|-------------|-------------|
| **One-hot encoding** | Lumikha ng binary column para sa bawat kategorya | Mga kategoryang low-cardinality; pinangangasiwaan ng mga modelong nakabatay sa puno |
| **Pag-encode ng label** | Magtalaga ng integer sa bawat kategorya | Ordinal na mga kategorya; mga modelong nakabatay sa puno |
| **Target encoding** | Palitan ang kategorya ng mean ng target na variable | High-cardinality na mga kategorya; iwasan ang overfitting sa pagpapakinis |
| **Dalas na pag-encode** | Palitan ang kategorya ng bilang o dalas nito | Kapag ang dalas mismo ay nagbibigay-kaalaman |
| **Binary encoding** | I-convert ang mga integer-encoded na kategorya sa binary digit | High-cardinality; binabawasan ang dimensionality kumpara sa one-hot |
| **Pag-embed** | Alamin ang siksik na representasyon ng vector | Napakataas na cardinality; NLP; mga sistema ng tagapagrekomenda |
| **Hash encoding** | Mga kategorya ng hash sa isang nakapirming bilang ng mga tampok | Napakataas na cardinality; online na pag-aaral |
### Mga Tampok ng Petsa at Oras
| Tampok | Paglalarawan |
|---------|-------------|
| **Oras ng araw** | Kinukuha ang mga pang-araw-araw na pattern (oras ng pagmamadali, oras ng gabi) |
| **Araw ng linggo** | Weekday vs weekend effect |
| **Buwan / quarter** | Pana-panahong mga pattern |
| **Ay weekend** | Binary flag para sa katapusan ng linggo |
| **Ay holiday** | Binary flag para sa mga pampublikong holiday |
| **Oras mula noong kaganapan** | Mga araw mula noong huling pagbili; oras mula noong huling pag-login |
| **Cyclical encoding** | sin(2π × oras / 24), cos(2π × oras / 24) — pinapanatili ang pabilog na kalikasan ng oras |
---

## Pangangasiwa sa mga Nawawalang Halaga
| Diskarte | Paglalarawan | Kailan Gagamitin |
|----------|-------------|-------------|
| **I-drop ang mga row** | Alisin ang mga row na may mga nawawalang value | Ang nawawalang data ay isang maliit na bahagi; MCAR (walang ganap na random) |
| **I-drop ang mga column** | Alisin ang mga feature na may masyadong maraming nawawalang value | Ang tampok ay halos nawawala; hindi mahalaga |
| **Mean / median imputation** | Punan ng mean o median ng feature na | Simple; pinapanatili ang ibig sabihin ngunit binabawasan ang pagkakaiba |
| **Mode imputation** | Punan ayon sa kategorya ang pinakamadalas na halaga | Mga tampok na kategorya |
| **KNN imputation** | Gumamit ng k-pinakamalapit na kapitbahay upang tantyahin ang nawawalang halaga | Kapag nakakatulong ang mga katulad na pagkakataon na mahulaan ang nawawalang halaga |
| **Imputation na nakabatay sa modelo** | Sanayin ang isang modelo upang mahulaan ang mga nawawalang halaga | Mas tumpak; computationally mahal |
| **Nawawalang indicator** | Magdagdag ng binary column na nag-flag ng kawalan | Kapag ang kawalan mismo ay nagbibigay-kaalaman |
| **Interpolation** | Punan ng mga interpolated na halaga (linear, spline) | Serye ng oras; iniutos na data |
---

## Pinili ng Tampok
### Mga Paraan ng Filter
| Paraan | Paglalarawan |
|--------|--------------|
| **Kaugnayan** | Alisin ang mga tampok na lubos na nauugnay sa isa't isa |
| **Batas ng pagkakaiba-iba** | Alisin ang mga feature na may halos zero na pagkakaiba |
| **Mutual na impormasyon** | Sukatin ang impormasyon na ibinibigay ng bawat tampok tungkol sa target |
| **Chi-squared** | Subukan ang pagsasarili sa pagitan ng mga tampok na kategorya at target |
| **ANOVA F-test** | Subukan kung ang ibig sabihin ng numerical feature ay naiiba sa mga target na klase |
### Mga Paraan ng Wrapper
| Paraan | Paglalarawan |
|--------|--------------|
| **Ipasa ang pagpili** | Magsimulang walang laman; idagdag ang pinakamahusay na tampok nang paisa-isa |
| **Paatras na pag-aalis** | Magsimula sa lahat; alisin ang pinakamasamang feature nang paisa-isa |
| **Recursive feature elimination (RFE)** | Paulit-ulit na modelo ng tren; alisin ang hindi gaanong mahahalagang tampok |
### Mga Naka-embed na Paraan
| Paraan | Paglalarawan |
|--------|--------------|
| **L1 regularization (Lasso)** | Pinapababa ang mga hindi nauugnay na timbang ng tampok sa zero |
| **Kahalagahang nakabatay sa puno** | Gamitin ang kahalagahan ng tampok mula sa mga modelo ng puno |
| **Mga halaga ng SHAP** | Sukatin ang kontribusyon ng bawat tampok sa mga hula |
---

## Domain-Specific Feature Engineering
### Mga Tampok ng Teksto
| Tampok | Paglalarawan |
|---------|-------------|
| **TF-IDF** | Ang dalas ng termino na natimbang ng kabaligtaran na dalas ng dokumento |
| **Mga pag-embed ng salita** | Mga siksik na vector na kumukuha ng semantikong kahulugan (Word2Vec, GloVe) |
| **Character n-grams** | Kunin ang mga pattern ng sub-salita; kapaki-pakinabang para sa mga typo at morpolohiya |
| **Mga istatistika ng teksto** | Haba; bilang ng salita; bilang ng pangungusap; average na haba ng salita |
| **Mga marka ng pagiging madaling mabasa** | Flesch-Kincaid; Gunning fog index |
### Mga Tampok ng Serye ng Oras
| Tampok | Paglalarawan |
|---------|-------------|
| **Lag features** | Mga nakaraang value: y(t-1), y(t-7), y(t-30) |
| **Rolling statistics** | Mean, std, min, max sa ibabaw ng isang window |
| **Pagkakaiba** | y(t) - y(t-1); kumukuha ng trend |
| **Panahunang pagkakaiba** | y(t) - y(t-12) para sa buwanang data na may taunang seasonality |
| **Apat na termino** | Mga termino ng sine at cosine para sa mga seasonal pattern |
### Mga Tampok ng Larawan (Pre-Deep Learning)
| Tampok | Paglalarawan |
|---------|-------------|
| **HOG** (Histogram of Oriented Gradients) | Pamamahagi ng mga direksyon sa gilid |
| **LBP** (Mga Lokal na Binary Pattern) | Paglalarawan ng texture |
| **SIFT** (Scale-Invariant Feature Transform) | Keypoint descriptors |
| **Mga histogram ng kulay** | Pamamahagi ng mga kulay sa larawan |
---

## Mga Pinakamahuhusay na Kasanayan sa Feature Engineering
| Magsanay | Paglalarawan |
|----------|-------------|
| **Iwasan ang pagtagas ng data** | Huwag kailanman gumamit ng impormasyon mula sa hinaharap o ang set ng pagsubok upang lumikha ng mga tampok |
| **Idokumento ang lahat** | Itala kung anong mga pagbabago ang inilapat at bakit |
| **Bersyon ng iyong mga tampok** | Subaybayan ang mga pagbabago sa feature kasama ng mga pagbabago sa modelo |
| **Patunayan na mayroon at wala** | Subukan kung ang isang bagong tampok ay talagang nagpapabuti sa pagganap ng modelo |
| **Panatilihin itong maaaring kopyahin** | Ang mga feature na pipeline ng engineering ay dapat na deterministiko at nauulit |
| **Subaybayan ang feature drift** | Maaaring magbago ang mga pamamahagi ng feature sa paglipas ng panahon; subaybayan at sanayin muli |
---

## Buod
Ang feature engineering ay kung saan natutugunan ng kaalaman ng domain ang machine learning. Ito ang proseso ng pagbabago ng raw data — magulo, hindi kumpleto, high-dimensional — sa malinis, nagbibigay-kaalaman na mga representasyon na maaaring matutunan ng mga modelo. Ang mga numerical transformation ay humahawak ng skew at scale. Kino-convert ng mga kategoryang encoding ang mga label sa mga numerong magagamit ng mga modelo. Ang mga feature ng petsa ay kumukuha ng mga temporal na pattern. Ang mga nawawalang diskarte sa halaga ay pinangangasiwaan ang hindi kumpletong data. Ang pagpili ng feature ay nag-aalis ng ingay at kalabisan. Ang pinakamahuhusay na feature engineer ay nag-iisip na parang mga detective: nagtatanong sila kung anong mga signal ang dapat na nasa data, kung saan maaaring itago ang mga signal na iyon, at kung paano i-extract ang mga ito sa paraang tapat (walang data leakage), maaaring kopyahin, at matatag na magbago sa paglipas ng panahon.