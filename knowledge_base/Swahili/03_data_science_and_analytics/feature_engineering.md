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

# Uhandisi wa Kipengele
Uhandisi wa vipengele ni mchakato wa kubadilisha data ghafi kuwa uwasilishaji unaofanya miundo ya kujifunza kwa mashine kuwa bora zaidi. Mara nyingi hufafanuliwa kama hatua muhimu zaidi katika bomba la ML - vipengele unavyotoa mfano ni muhimu zaidi kuliko algoriti unayochagua. Muundo rahisi ulio na vipengele vilivyoundwa vyema kwa kawaida utashinda kielelezo changamano na pembejeo mbichi, ambazo hazijachakatwa. Sanaa iko katika kuelewa kikoa na data vizuri vya kutosha kuunda ishara ambazo mtindo unaweza kujifunza kutoka.
---

## Kwa nini Uhandisi wa Kipengele Ni Muhimu
| Sababu | Athari |
|--------|--------|
| **Ubora wa mawimbi** | Vipengele bora = muundo wazi zaidi wa mtindo kujifunza |
| **Urahisi wa mfano** | Vipengele vyema huruhusu mifano rahisi kufanya vizuri; haja ndogo ya usanifu tata |
| **Kasi ya mafunzo** | Vipengele vinavyofaa, vilivyo na vipimo vyema huungana kwa haraka |
| **Ujumla** | Vipengele vilivyo na maelezo ya kikoa husaidia miundo kufanya kazi kwenye data isiyoonekana |
| **Tafsiri** | Vipengele vya maana ni rahisi kueleza wadau |
---

## Aina za Mabadiliko ya Kipengele
### Mabadiliko ya Nambari
| Mabadiliko | Mfumo / Maelezo | Wakati wa Kutumia |
|---------------------------------------------------|
| **Badilisha kumbukumbu** | logi(x) au logi(x + 1) | Usambazaji uliopotoshwa kulia; maadili ya fedha |
| **Mzizi wa mraba** | sqrt(x) | Skew wastani; hesabu data |
| **Box-Cox** | Ubadilishaji wa Parametric ambao hupata mabadiliko bora ya nguvu | Kufanya data kusambazwa zaidi kawaida |
| **Yeo-Johnson** | Kama Box-Cox lakini hushughulikia maadili hasi | Data iliyopinda na thamani hasi |
| **Kiwango** | (x - maana) / std | Vipengele vilivyo na mizani tofauti; algorithms kuchukua hali ya kawaida |
| **Upeo wa chini zaidi** | (x - dakika) / (max - min) | Vipengele vya kufunga kwa [0, 1]; thamani za pikseli za picha |
| **Kuongeza nguvu** | (x - wastani) / IQR | Data na wauzaji |
| **Binning** | Badilisha kuendelea kuwa kategoria | Mahusiano yasiyo ya mstari; miti ya maamuzi |
| **Sifa za polinomia** | x², x³, x₁×x₂ | Kukamata mahusiano yasiyo ya mstari katika miundo ya mstari |
### Usimbaji wa Kitengo
| Usimbaji | Maelezo | Wakati wa Kutumia |
|----------|---------------------------|
| **Usimbaji wa sauti moja** | Unda safu ya jozi kwa kila aina | Makundi ya chini ya kardinali; mifano ya miti hushughulikia asili |
| **Usimbaji lebo** | Agiza nambari kamili kwa kila kategoria | Makundi ya kawaida; mifano ya miti |
| **Usimbaji unaolengwa** | Badilisha kategoria na wastani wa utofauti unaolengwa | Makundi ya juu-kadinali; epuka kulainisha kupita kiasi |
| **Usimbaji wa mara kwa mara** | Badilisha kategoria na hesabu yake au marudio | Wakati frequency yenyewe ni taarifa |
| **Usimbaji binary** | Badilisha kategoria zilizosimbwa kabisa kuwa tarakimu za binary | High-cardinality; inapunguza dimensionality dhidi ya moja-moto |
| **Inapachika** | Jifunze uwakilishi wa vekta mnene | Kadinali ya juu sana; NLP; mifumo ya washauri |
| **Usimbaji wa Hash** | Kategoria za heshi kwa idadi isiyobadilika ya vipengele | Kadinali ya juu sana; kujifunza mtandaoni |
### Vipengele vya Tarehe na Wakati
| Kipengele | Maelezo |
|---------|-------------|
| **Saa ya siku** | Hunasa mifumo ya kila siku (saa ya haraka sana, wakati wa usiku) |
| **Siku ya wiki** | Athari za siku ya wiki dhidi ya wikendi |
| **Mwezi / robo** | Mitindo ya msimu |
| **Ni wikendi** | Bendera ya binary kwa wikendi |
| **Ni likizo** | Bendera ya binary kwa sikukuu za umma |
| **Muda tangu tukio** | Siku tangu ununuzi wa mwisho; saa tangu kuingia mara ya mwisho |
| **Usimbaji wa mzunguko** | sin(2π × saa / 24), cos(2π × saa / 24) — huhifadhi asili ya mduara ya wakati |
---

## Kushughulikia Maadili Yanayokosekana
| Mkakati | Maelezo | Wakati wa Kutumia |
|----------|---------------------------|
| **dondosha safu mlalo** | Ondoa safu mlalo zisizo na thamani | Data inayokosekana ni sehemu ndogo; MCAR (kukosa kabisa bila mpangilio) |
| **Dondosha safu wima** | Ondoa vipengele vilivyo na thamani nyingi zinazokosekana | Kipengele mara nyingi hakipo; sio muhimu |
| **Maana / uwekaji wa wastani** | Jaza wastani wa kipengele au wastani | Rahisi; huhifadhi maana lakini inapunguza tofauti |
| **Uwekaji wa hali** | Jaza kategoria na thamani ya mara kwa mara | Vipengele vya kitengo |
| **KNN imputation** | Tumia majirani wa k-karibu kukadiria thamani inayokosekana | Wakati matukio sawa husaidia kutabiri thamani inayokosekana |
| **Uigaji kulingana na modeli** | Funza kielelezo kutabiri maadili yanayokosekana | Sahihi zaidi; gharama ya hesabu |
| **Kiashiria kinakosekana** | Ongeza safu ya jozi inayoashiria upungufu | Wakati kukosa yenyewe ni taarifa |
| **Tafsiri** | Jaza na maadili yaliyoingiliana (linear, spline) | Mfululizo wa wakati; data iliyoagizwa |
---

## Uteuzi wa Kipengele
### Mbinu za Kichujio
| Mbinu | Maelezo |
|--------|-------------|
| **Uhusiano** | Ondoa vipengele vinavyohusiana sana |
| **Kiwango cha tofauti** | Ondoa vipengele vilivyo na tofauti ya karibu sufuri |
| **Habari za kuheshimiana** | Pima maelezo ambayo kila kipengele hutoa kuhusu lengo |
| **Chi-mraba** | Jaribu uhuru kati ya vipengele vya kitengo na lengo |
| **Jaribio la F la ANOVA** | Jaribu ikiwa kipengele cha nambari kinamaanisha kutofautiana katika madarasa lengwa |
### Mbinu za Wrapper
| Mbinu | Maelezo |
|--------|-------------|
| **Sambaza uteuzi** | Anza tupu; ongeza kipengele bora zaidi moja baada ya nyingine |
| **Kuondoa nyuma** | Anza na yote; ondoa kipengele kibaya zaidi kwa wakati mmoja |
| **Kuondoa kipengele cha kujirudia (RFE)** | Kurudia mfano wa treni; ondoa vipengele muhimu zaidi |
### Mbinu Zilizopachikwa
| Mbinu | Maelezo |
|--------|-------------|
| **Udhibiti wa L1 (Lasso)** | Hupunguza uzani wa vipengele visivyohusika hadi sufuri |
| **Umuhimu wa msingi wa miti** | Tumia kipengele cha umuhimu kutoka kwa miundo ya miti |
| **Thamani za SHAP** | Pima mchango wa kila kipengele kwa utabiri |
---

## Uhandisi wa Kipengele Maalum cha Kikoa
### Vipengele vya Maandishi
| Kipengele | Maelezo |
|---------|-------------|
| **TF-IDF** | Masafa ya muda yaliyopimwa kwa marudio ya hati kinyume |
| **Upachikaji wa maneno** | Vekta mnene zinazonasa maana ya kisemantiki (Word2Vec, GloVe) |
| **Tabia n-gramu** | Nasa ruwaza za neno ndogo; muhimu kwa makosa ya uchapaji na mofolojia |
| **Takwimu za maandishi** | Urefu; hesabu ya maneno; hesabu ya sentensi; wastani wa urefu wa neno |
| **Alama za usomaji** | Flesch-Kincaid; Fahirisi ya ukungu wa bunduki |
### Vipengele vya Mfululizo wa Wakati
| Kipengele | Maelezo |
|---------|-------------|
| **Vipengele vya kuchelewa ** | Thamani za awali: y(t-1), y(t-7), y(t-30) |
| **Takwimu zinazoendelea** | Maana, std, min, max juu ya dirisha |
| **Tofauti** | y(t) - y(t-1); kunasa mtindo |
| **Tofauti ya msimu** | y(t) - y(t-12) kwa data ya kila mwezi na msimu wa kila mwaka |
| **Masharti manne** | Masharti ya sine na cosine ya mifumo ya msimu |
### Vipengele vya Picha (Masomo ya Kabla ya Kina)
| Kipengele | Maelezo |
|---------|-------------|
| **HOG** (Histogram of Oriented Gradients) | Usambazaji wa maelekezo makali |
| **LBP** (Miundo ya Ndani ya Binary) | Maelezo ya muundo |
| **SIFT** (Mabadiliko ya Kipengele Kisichobadilika kwa Kiwango) | Vifafanuzi vya msingi |
| **Histogramu za rangi** | Usambazaji wa rangi katika picha |
---

## Mbinu Bora za Uhandisi
| Mazoezi | Maelezo |
|----------|-------------|
| **Epuka uvujaji wa data** | Kamwe usitumie maelezo ya siku zijazo au seti ya jaribio ili kuunda vipengele |
| **Weka kila kitu** | Rekodi ni mabadiliko gani yalitumika na kwa nini |
| **Toleo la vipengele vyako** | Fuatilia mabadiliko ya kipengele pamoja na mabadiliko ya muundo |
| **Thibitisha na bila** | Jaribu kama kipengele kipya kinaboresha utendakazi wa muundo |
| **Weka iweze kuzaliana** | Mabomba ya uhandisi ya kipengele yanapaswa kuwa ya kuamua na yanayoweza kurudiwa |
| **Fuatilia mteremko wa kipengele** | Usambazaji wa vipengele unaweza kubadilika kwa muda; kufuatilia na kutoa mafunzo upya |
---

## Muhtasari
Uhandisi wa kipengele ni pale maarifa ya kikoa hukutana na ujifunzaji wa mashine. Ni mchakato wa kubadilisha data mbichi - yenye fujo, isiyo kamili, ya hali ya juu - kuwa uwasilishaji safi na wa kuarifu ambao wanamitindo wanaweza kujifunza kutoka kwao. Mabadiliko ya nambari hushughulikia skew na mizani. Usimbaji wa kitengo hubadilisha lebo kuwa miundo ya nambari inaweza kutumia. Vipengele vya tarehe hunasa ruwaza za muda. Mikakati ya thamani inayokosekana hushughulikia data isiyokamilika. Uteuzi wa kipengele huondoa kelele na upungufu. Wahandisi wa vipengele bora zaidi hufikiri kama wapelelezi: wanauliza ni mawimbi gani yanapaswa kuwepo kwenye data, mahali ambapo mawimbi hayo yanaweza kufichwa, na jinsi ya kuzitoa kwa njia ambayo ni ya uaminifu (hakuna uvujaji wa data), inayoweza kuzaliana, na yenye nguvu kubadilika kadri muda unavyopita.