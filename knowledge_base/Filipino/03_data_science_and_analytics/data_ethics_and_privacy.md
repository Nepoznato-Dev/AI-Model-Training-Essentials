---
# Metadata
title: "Data Ethics and Privacy"
description: "GDPR, data consent, algorithmic bias, dark patterns, anonymisation"
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
tags: [data, ethics, privacy, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Etika at Privacy ng Data
Ang data ethics ay ang pag-aaral kung paano nakakaapekto ang pangongolekta, pagsusuri, at deployment ng data sa mga karapatan, awtonomiya, at kapakanan ng mga tao. Ang privacy ay ang partikular na alalahanin tungkol sa kung sino ang kumokontrol sa personal na impormasyon at kung paano ito ibinabahagi. Ang mga paksang ito ay lumipat mula sa mga akademikong debate patungo sa mga balita sa harap ng pahina — pagpapatupad ng GDPR, mga paglabag sa data na nakakaapekto sa bilyun-bilyong user, at lumalagong kamalayan ng publiko na ang mga gawi sa data ng mga tech na kumpanya ay may tunay na kahihinatnan para sa demokrasya, pagkakapantay-pantay, at kalayaan ng indibidwal.
---

## Bakit Mahalaga ang Etika ng Data
| Pag-aalala | Paglalarawan | Real-World Epekto |
|---------|-------------|-------------------|
| **Kapitalismo sa pagmamanman** | Pinagkakakitaan ng mga kumpanya ang personal na data sa sukat | Pagkawala ng privacy; pagmamanipula ng pag-uugali |
| **Algorithmic bias** | Ang mga modelong sinanay sa pinapanigang data ay nagpaparami ng bias | Diskriminasyon sa pagkuha, pagpapahiram, pagpupulis |
| **Informed consent** | Hindi naiintindihan ng mga user kung ano ang kanilang sinasang-ayunan | Ang data na nakolekta para sa isang layunin na ginamit para sa isa pang |
| **Mga paglabag sa data** | Nalantad ang sensitibong data sa pamamagitan ng mahinang seguridad | Pagnanakaw ng pagkakakilanlan; pandaraya sa pananalapi; pinsala sa reputasyon |
| **I-filter ang mga bula** | Ang mga personalized na feed ay nagpapatibay sa mga kasalukuyang paniniwala | Polarisasyong pampulitika; maling impormasyon |
| **Madilim na pattern** | Idinisenyo ang UI upang linlangin ang mga user sa pagbabahagi ng data | Mga hindi gustong subscription; hindi sinasadyang pagbabahagi ng data |
---

## Mga Framework at Regulasyon sa Privacy
### Mga Pangunahing Batas sa Privacy
| Regulasyon | Rehiyon | Mga Pangunahing Kinakailangan |
|-----------|--------|-----------------|
| **GDPR** (General Data Protection Regulation) | EU / EEA | Batay sa batas para sa pagproseso; karapatang ma-access; karapatang makalimutan; maaaring dalhin ng data; 72-oras na abiso sa paglabag; multa hanggang 4% ng pandaigdigang kita |
| **CCPA / CPRA** (California Privacy Rights Act) | California, USA | Karapatang malaman; karapatang magtanggal; karapatang mag-opt out sa pagbebenta; limitadong pag-opt-in para sa mga bata |
| **LGPD** (Lei Geral de Proteção de Dados) | Brazil | Katulad ng GDPR; batayan ng batas; mga karapatan sa paksa ng data; Kinakailangan ang DPO |
| **PIPL** (Batas sa Proteksyon ng Personal na Impormasyon) | Tsina | Kinakailangan ang pahintulot; lokalisasyon ng data; mga paghihigpit sa paglipat ng cross-border |
| **POPIA** (Proteksyon ng Personal na Impormasyon Act) | South Africa | Mga kondisyon para sa legal na pagproseso; mga karapatan sa paksa ng data; regulator |
| **DPDP Act** (Digital Personal Data Protection Act) | India | Pahintulot; limitasyon ng layunin; mga pangunahing karapatan ng data; mga obligasyon sa katiwala ng data |
### Mga Pangunahing Prinsipyo ng GDPR
| Prinsipyo | Kinakailangan |
|-----------|-------------|
| **Pagiging makatarungan, pagiging patas, transparency** | Iproseso ang data nang legal; huwag linlangin ang mga gumagamit; maging bukas tungkol sa kung ano ang iyong kinokolekta |
| **Limitasyon ng layunin** | Kolektahin ang data para lamang sa tinukoy, tahasang mga layunin |
| **Pag-minimize ng data** | Kolektahin lamang ang talagang kailangan mo |
| **Katumpakan** | Panatilihing tumpak ang data; itama o tanggalin ang hindi tumpak na data |
| **Limitasyon sa storage** | Huwag panatilihin ang data nang mas mahaba kaysa sa kinakailangan |
| **Integridad at pagiging kumpidensyal** | Secure ang data laban sa hindi awtorisadong pag-access at pagkawala |
| **Pananagutan** | Ipakita ang pagsunod sa lahat ng nasa itaas |
---

## Mga Teknik sa Pagpapanatili ng Privacy
| Teknik | Paano Ito Gumagana | Trade-Off |
|-----------|-------------|-----------|
| **Anonymation** | Alisin ang personally identifiable information (PII) | Mahirap ganap na i-anonymise; panganib sa muling pagkakakilanlan |
| **Pseudonymisation** | Palitan ang mga identifier ng mga pseudonym | Nababaligtad; personal na data pa rin sa ilalim ng GDPR |
| **Differential privacy** | Magdagdag ng naka-calibrate na ingay sa mga resulta ng query | Binabawasan ang katumpakan; nagbibigay ng mathematical privacy guarantee |
| **Federated learning** | Mga modelo ng tren sa device; ibahagi lamang ang mga update sa modelo | Mas mabagal na pagsasanay; komunikasyon sa itaas |
| **Secure na multi-party computation** | Maramihang mga partido ang nagko-compute ng isang function nang hindi inilalantad ang mga input | computationally mahal; kumplikadong ipatupad |
| **Homomorphic encryption** | Magsagawa ng mga pagkalkula sa naka-encrypt na data | Napakabagal; suporta sa limitadong operasyon |
| **Pag-mask ng data** | Itago ang mga bahagi ng data (hal.,`***-**-1234`) | Simple ngunit limitadong proteksyon |
---

## Etikal na Pagkolekta ng Data
### Mga Prinsipyo para sa Etikal na Koleksyon
| Prinsipyo | Paglalarawan |
|-----------|-------------|
| **Informed consent** | Naiintindihan ng mga user kung ano ang kanilang pinahihintulutan; hindi inilibing sa legalese |
| **Transparency ng layunin** | Malinaw na sabihin kung bakit kinokolekta ang data at kung paano ito gagamitin |
| **Minimal na koleksyon** | Kolektahin lamang ang kailangan para sa nakasaad na layunin |
| **Kontrol ng user** | Hayaan ang mga user na i-access, itama, i-download, at tanggalin ang kanilang data |
| **Limitadong pagpapanatili** | Tanggalin ang data kapag hindi na ito kailangan |
| **Pagsusuri ng epekto** | Suriin ang mga potensyal na pinsala bago mangolekta ng sensitibong data |
### Mga Karaniwang Madilim na Pattern
| Pattern | Paglalarawan | Halimbawa |
|---------|-------------|---------|
| **Privacy zuckering** | Dayain ang mga user sa pagbabahagi ng higit pa sa nilalayon nila | Ang "Ibahagi sa mga kaibigan" ay na-pre-check sa panahon ng pag-signup |
| **Roach motel** | Madaling mag-sign up; mahirap kanselahin | Ang pagtanggal ng account ay nangangailangan ng tawag sa telepono o fax |
| **Sapilitang pagpapatuloy** | Ang libreng pagsubok ay nagko-convert sa bayad na walang malinaw na abiso | Lumalabas ang mga singil sa subscription sa credit card |
| **Confirmshaming** | Sisihin ang mga user sa pag-opt in sa | "No thanks, ayokong mag-ipon ng pera" |
| **Mga nakatagong setting** | Ang mga kontrol sa privacy ay nakabaon nang malalim sa mga menu | Nakatago ang pag-opt out sa ilalim ng 5 antas ng mga setting |
---

## Bias at Patas sa Data
| Pinagmulan ng Bias | Paglalarawan | Halimbawa |
|----------------|------------|---------|
| **Pagkiling sa pagpili** | Hindi kinakatawan ng data ang target na populasyon | Pagsasanay ng modelo ng pag-hire sa data mula sa isang demograpiko lamang |
| **Historical bias** | Nakaraang diskriminasyon na na-encode sa data | Mga rekord ng pag-aresto na sumasalamin sa mga nakakiling na gawi sa pagpupulis |
| **Pagkampi sa pagsukat** | Ang mga variable na ginamit bilang mga proxy ay may depekto | Paggamit ng zip code bilang proxy para sa pagiging mapagkakatiwalaan |
| **Pagiging Pagsasama-sama** | Pagtrato sa magkakaibang grupo bilang homogenous | Isang modelo para sa lahat ng etnisidad; binabalewala ang mga pattern na partikular sa pangkat |
| **Survivorship bias** | Tinitingnan lamang ang mga matagumpay na kaso | Pag-aaral ng matagumpay na mga startup habang binabalewala ang mga nabigo |
### Mga Istratehiya sa Pagbabawas
| Diskarte | Paglalarawan |
|----------|-------------|
| **Magkakaibang pangongolekta ng data** | Tiyaking kinakatawan ng data ng pagsasanay ang lahat ng apektadong grupo |
| **Pag-audit ng bias** | Regular na subukan ang mga modelo para sa magkakaibang epekto sa mga pangkat |
| **Mga sukatan ng pagiging patas** | Sukatin ang demographic parity, pantay na pagkakataon, equalized odds |
| **Pagsusuri ng tao** | Ipasuri sa mga tao ang mga desisyon na may mataas na stake |
| **Mga ulat sa transparency** | Mag-publish ng data tungkol sa pagganap ng modelo sa buong demograpiko |
| **Pakikipag-ugnayan sa komunidad** | Isali ang mga apektadong komunidad sa disenyo at pagsusuri |
---

## Pamamahala ng Data
### Mga Tungkulin sa Pamamahala ng Data
| Tungkulin | Pananagutan |
|------|--------------|
| **May-ari ng data** | May pananagutan ang senior leader para sa isang domain ng data |
| **Data steward** | Pang-araw-araw na pamamahala; kalidad; pag-uuri |
| **Data protection officer (DPO)** | Pagsunod sa GDPR; mga pagtatasa ng epekto sa privacy; pakikipag-ugnayan sa mga regulator |
| **Inhinyero ng data** | Mga Pipeline; imbakan; pagbabagong-anyo |
| **Data scientist** | Pagsusuri; pagmomodelo; pag-uulat |
| **Data privacy analyst** | Subaybayan ang pagsunod; pangasiwaan ang mga kahilingan sa paksa ng data |
### Pag-uuri ng Data
| Pag-uuri | Paglalarawan | Pangangasiwa |
|--------------|-------------|----------|
| **Pampubliko** | Maaaring malayang ibahagi | Walang mga paghihigpit |
| **Internal** | Para sa mga empleyado lamang | Mga kontrol sa pag-access; walang panlabas na pagbabahagi |
| **Kumpidensyal** | Sensitibong data ng negosyo | Pag-encrypt; mahigpit na kontrol sa pag-access; audit logging |
| **Pinaghihigpitan** | Lubos na sensitibo; kinokontrol (PII, kalusugan, pananalapi) | Pag-encrypt sa pahinga at sa transit; DLP; minimal na access |
---

## Buod
Ang etika at privacy ng data ay hindi na opsyonal na pagsasaalang-alang — mga legal na kinakailangan ang mga ito, mga kinakailangan sa negosyo, at mga obligasyong moral. Ang GDPR at mga katulad na regulasyon ay nagtatatag ng mga malinaw na panuntunan: mangolekta nang kaunti, gumamit nang malinaw, protektahan nang mahigpit, at bigyan ang mga user ng kontrol. Ginagawang posible ng mga diskarte sa pagpapanatili ng privacy tulad ng differential privacy, federated learning, at encryption na makakuha ng halaga mula sa data nang hindi inilalantad ang mga indibidwal. Ngunit ang teknolohiya lamang ay hindi sapat. Ang mga organisasyon ay nangangailangan ng mga istruktura ng pamamahala ng data, bias na mga kasanayan sa pag-audit, at isang kultura na itinuturing ang personal na data bilang isang bagay na dapat pangasiwaan, hindi lamang pinagsamantalahan. Ang mga kumpanyang makakakuha ng karapatang ito ay makakakuha ng tiwala; ang mga hindi ay mahaharap sa mga multa sa regulasyon, pagsalungat ng publiko, at ang mabagal na pagguho ng pagpayag ng kanilang mga user na magbahagi ng data.