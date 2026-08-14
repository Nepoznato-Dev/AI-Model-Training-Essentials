<!--
---
# Metadata
title: "Computer Vision Fundamentals"
description: "CNNs, object detection, segmentation, transfer learning"
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
tags: [computer, vision, ai-and-machine-learning]
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
# Misingi ya Maono ya Kompyuta
Maono ya kompyuta huipa mashine uwezo wa kufasiri na kuelewa taarifa zinazoonekana kutoka ulimwenguni - picha, video na data ya 3D. Huwezesha kila kitu kuanzia utambuzi wa uso kwenye simu yako hadi magari yanayojiendesha, uchanganuzi wa picha za matibabu na udhibiti wa ubora wa viwanda. Faili hii inashughulikia dhana za msingi, usanifu, na mbinu.
---

## Jinsi Kompyuta Zinavyoona Picha
### Pikseli na Idhaa
Picha ya dijiti ni gridi ya saizi. Kila pikseli ina nambari za nambari zinazowakilisha ukubwa wa rangi.
| Aina ya Picha | Vituo | Thamani kwa Pixel | Mfano |
|-----------|---------------------------|---------|
| **Kijivu** | 1 | 0 (nyeusi) hadi 255 (nyeupe) | X-rays ya matibabu |
| **RGB** | 3 | Nyekundu, Kijani, Bluu (kila 0–255) | Picha za rangi za kawaida |
| **RGBA** | 4 | RGB + Alpha (uwazi) | Picha zenye asili wazi |
| **HSV** | 3 | Hue, Kueneza, Thamani | Sehemu kulingana na rangi |
Picha ya 1920×1080 RGB ni tensor ya umbo la`(1080, 1920, 3)`— hizo ni pikseli milioni 6.2, kila moja ikiwa na thamani 3.
### Uendeshaji Muhimu
| Operesheni | Maelezo |
|-----------|-------------|
| **Kubadilisha ukubwa** | Weka picha ili kulenga vipimo (bilinear, tafsiri ya jirani-karibu) |
| **Kupunguza ** | Toa eneo linalokuvutia |
| **Urekebishaji** | Ongeza thamani za pikseli hadi [0,1] au [-1,1] kwa mitandao ya neva |
| **Kuongeza** | Panua data ya mafunzo kwa njia bandia (kuzungusha, kugeuza, kugeuza rangi, kupunguza) |
---

## Convolution: Operesheni ya Msingi
Mchanganyiko huteleza kichujio kidogo (kernel) kwenye picha, ikitengeneza bidhaa za nukta katika kila nafasi. Hivi ndivyo CNNs hugundua kingo, muundo na muundo.
### Vigezo vya Ubadilishaji
| Kigezo | Athari |
|-----------|--------|
| **Ukubwa wa Kernel** | 3×3, 5×5, 7×7 — punje kubwa zaidi huchukua ruwaza kubwa zaidi |
| **Hatua** | Ukubwa wa hatua; stride=2 inapunguza vipimo vya matokeo |
| **Kuweka pedi** | Ongeza sufuri kuzunguka mpaka ili kuhifadhi vipimo vya anga |
| **Idadi ya vichungi** | Kila kichujio hujifunza kipengele tofauti (kingo, umbile, muundo wa rangi) |
### Majadiliano yanajifunza nini
| Kina cha Tabaka | Vipengele Vimegunduliwa |
|--------------------------------|
| **Tabaka za awali** | Kingo, pembe, textures rahisi |
| **Tabaka za kati** | Maumbo, sehemu za kitu (magurudumu, macho, majani) |
| **Tabaka za kina** | Dhana za hali ya juu (nyuso, magari, wanyama) |
---

## Usanifu wa CNN
Mageuzi ya usanifu wa CNN yanasimulia hadithi ya maendeleo ya kina ya kujifunza katika maono ya kompyuta.
| Usanifu | Mwaka | Ubunifu Muhimu |
|--------------------|---------------|
| **LeNet-5** | 1998 | CNN ya kwanza ya vitendo; utambuzi wa tarakimu |
| **AlexNet** | 2012 | Deep CNN inashinda ImageNet; ReLU, kuacha shule, mafunzo ya GPU |
| **VGGNet** | 2014 | Misongeo 3×3 iliyopangwa kwa rafu (zaidi zaidi = bora) |
| **GoogLeNet (Kuanzishwa)** | 2014 | Moduli za kuanzishwa (ukubwa wa chujio sambamba); tabaka 22 |
| **ResNet** | 2015 | Ruka miunganisho (kujifunza kwa mabaki); 152+ tabaka |
| **EfficientNet** | 2019 | Kuongeza kiwango cha pamoja (kina + upana + azimio) |
| **ConvNeXt** | 2022 | ResNet ya Kisasa; ushindani na Transfoma |
### Kwa nini ResNet Ilibadilisha Kila Kitu
Kabla ya ResNet, kutoa mafunzo kwa mitandao ya kina sana ilikuwa karibu kutowezekana kwa sababu ya shida ya kutoweka kwa gradient. ResNet ilianzisha **ruka miunganisho** (pia inaitwa miunganisho ya mabaki): ingizo kwenye safu huongezwa kwa matokeo yake.
```
output = F(x) + x    # Skip connection
```

Wazo hili rahisi liliruhusu mitandao iliyo na tabaka 152+ kufunzwa vyema, na sasa ni ya kawaida katika takriban usanifu wote wa kina.
---

## Kazi za Msingi za Maono
### Uainishaji wa Picha
Weka lebo kwa picha nzima.
| Mfano | Mbinu |
|-------|-----------|
| CNNs (ResNet, EfficientNet) | Mbinu ya jadi; usahihi bora |
| Vision Transfoma (ViT) | Chunguza picha kama mlolongo wa viraka; Kisimbaji cha kibadilishaji |
| Kuhamisha Mafunzo | Rekebisha muundo uliofunzwa mapema kwenye mkusanyiko wako wa data |
### Utambuzi wa Kitu
Tafuta na uainisha vitu vingi ndani ya picha, kwa kutumia visanduku vya kufunga.
| Mfano | Aina | Kasi |
|-------|------|-------|
| **R-CNN** | Hatua mbili (pendekezo + uainishaji) | Polepole |
| **R-CNN ya haraka** | Imeboreshwa kwa hatua mbili | Kati |
| **Haraka zaidi ya R-CNN** | Mtandao wa Pendekezo la Mkoa + kigunduzi | Kati |
| **YOLO** (v1–v10) | Hatua moja; tabiri masanduku + madarasa kwa kupita moja | Haraka sana |
| **DETR** | Transformer-msingi; hakuna masanduku ya nanga | Kati |
**YOLO** (Unaangalia Mara Moja Pekee) ndiyo njia ya kwenda kwa utambuzi wa wakati halisi. **R-CNN ya kasi** inapendekezwa wakati usahihi ni muhimu zaidi ya kasi.
### Sehemu ya Picha
Kuainisha kila pikseli katika picha.
| Aina | Maelezo | Tumia Kesi |
|------|-------------|-----------|
| **Sehemu ya Semantiki** | Kila pikseli hupata lebo ya darasa | Kuendesha gari kwa uhuru (barabara, gari, watembea kwa miguu) |
| **Sehemu ya Tukio** | Kila pikseli + kitambulisho cha mfano wa kitu | Kuhesabu vitu, picha za matibabu |
| **Panoptic Segmentation** | Mfano wa Semantiki + umeunganishwa | Uelewa wa kina wa eneo |
Miundo muhimu: U-Net (upigaji picha wa kimatibabu), Mask R-CNN (mfano), DeepLab (semantic), Muundo wa Sehemu Chochote (SAM - mgawanyiko wa ulimwengu wote).
### Kizazi cha Picha
| Mbinu | Maelezo | Mifano |
|----------|------------------------|
| **GAN** | Jenereta dhidi ya mbaguzi mafunzo ya wapinzani | StyleGAN, CycleGAN |
| **VAE** | Jifunze usambazaji fiche; sampuli ya kuzalisha | Visimbaji Kiotomatiki tofauti |
| **Miundo ya Usambazaji** | Mara kwa mara kelele za nasibu | Usambazaji Imara, DALL-E, Midjourney |
Miundo ya usambaaji kwa kiasi kikubwa imepita GAN kwa ubora wa kutengeneza picha.
---

## Hamisha Mafunzo kwa Maono
Kufundisha CNN kutoka mwanzo kunahitaji data kubwa na kukokotoa. Mafunzo ya kuhamisha hukuruhusu kuanza na muundo ambao tayari umefunzwa kwenye mamilioni ya picha (ImageNet) na uisanishe vizuri kwa kazi yako mahususi.
###Hatua
1. **Chagua muundo uliofunzwa mapema** (ResNet50, EfficientNet-B0, ViT).
2. **Badilisha kichwa cha uainishaji** na chako (kulingana na idadi yako ya madarasa).
3. **Fanya safu za mapema** (zinanasa vipengele vya kawaida kama vile kingo).
4. **rekebisha vizuri** kwenye seti yako ya data ukitumia kiwango cha chini cha kujifunza.
5. **Anzisha kuganda polepole** ikiwa unahitaji marekebisho zaidi.
Mbinu hii mara kwa mara hufanikisha usahihi wa juu kwa kuwa na picha chache kama 1,000-10,000 zilizo na lebo.
---

## Uboreshaji wa data
Uboreshaji hupanua hifadhidata yako ya mafunzo kwa kutumia mabadiliko.
| Kuongeza | Athari | Wakati wa Kutumia |
|----------------------|-------------|
| **Mazao bila mpangilio** | Punguza hadi eneo la nasibu | Karibu kila wakati |
| **Flip mlalo** | Picha ya kioo | Wakati mwelekeo haujalishi |
| **Mzunguko** | Zungusha kwa pembe nasibu | Wakati vitu vinapoonekana kwa pembe yoyote |
| **Jitter ya rangi** | Rekebisha mwangaza, utofautishaji, kueneza kwa nasibu | Wakati taa inatofautiana |
| **Kufuta bila mpangilio** | Mask mikoa random | Inaboresha uimara |
| **Changanya / CutMix** | Changanya picha na lebo mbili | Udhibiti |
Maktaba:`torchvision.transforms`,`albumentations`,`imgaug`,`tf.keras.preprocessing`.
---

## Zana na Mifumo
| Zana | Kusudi |
|------|----------|
| **FunguaCV** | Operesheni za kawaida za CV (kuchuja, kugundua makali, mabadiliko ya kijiometri) |
| **mwenge** | Mifano ya maono ya PyTorch, mabadiliko, hifadhidata |
| **tf.keras.applications** | Miundo iliyofunzwa mapema katika TensorFlow/Keras |
| **Ultralytics (YOLOv8/v11)** | Utambuzi wa kitu, sehemu, uainishaji |
| **Uso wa Kukumbatiana (transfoma)** | Vision Transfoma, SegFormer, DETR |
| **Sehemu Chochote (SAM)** | Sehemu ya picha ya jumla kutoka kwa Meta |
| **Albamu** | Maktaba ya kuongeza picha ya haraka na rahisi |
---

## Vidokezo Vitendo
- **Anza na ujifunzaji wa kuhamisha.** Kuweka vizuri muundo uliofunzwa mapema hushinda mafunzo kutoka mwanzo katika karibu kila hali.
- **Rekebisha ingizo zako.** Linganisha urekebishaji ambao mtindo wa mafunzo ya awali unatarajia (kwa kawaida ImageNet mean/std).
- **Tumia vipimo vinavyofaa.** Usahihi wa mkusanyiko wa data uliosawazishwa; F1, mAP, au IoU kwa kazi zisizo na usawa au utambuzi.
- **Onyesha data yako.** Angalia sampuli za picha, angalia usambazaji wa darasa, kagua utabiri wa mifano.
- **Ongeza kwa busara.** Tekeleza mageuzi ambayo yanaeleweka kwa kikoa chako pekee (usipindue picha za matibabu wima).
- **Fuatilia uwekaji kupita kiasi.** Ikiwa usahihi wa mafunzo ni wa juu lakini uthibitisho ni mdogo, ongeza ongezeko au ongeza walioacha shule.