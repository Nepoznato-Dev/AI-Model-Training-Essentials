---
# Metadata
title: "AI Ethics and Governance"
description: "AI bias, fairness, accountability, regulation, governance frameworks"
category: "AI and Machine Learning"
subcategory: "Ethics and Safety"
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
    changes: "Moved to ethics_and_safety/ subfolder; added subcategory field"
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
tags: [ai, ethics, governance, ai-and-machine-learning]
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
# AI Etika at Pamamahala
Ang mga AI system ay hindi neutral. Sinasalamin nila ang data kung saan sila sinanay, ang mga halaga ng kanilang mga tagalikha, at ang mga insentibo ng mga organisasyong nagde-deploy sa kanila. Ang etika ay tungkol sa pagtatanong hindi lang "magagawa ba natin ito?" ngunit "dapat ba?" Ang pamamahala ay tungkol sa paglikha ng mga istruktura — mga batas, pamantayan, mga katawan ng pangangasiwa — na tumitiyak na ang AI ay binuo at ginagamit nang responsable. Sinasaklaw ng file na ito ang mga pangunahing etikal na dimensyon ng AI at ang mga balangkas ng pamamahala na lumalabas upang tugunan ang mga ito.
---

## Mga Pangunahing Prinsipyo sa Etika para sa AI
Karamihan sa mga framework ng etika ng AI ay nagtatagpo sa isang hanay ng mga ibinahaging prinsipyo.
| Prinsipyo | Ano ang Ibig Sabihin Nito | Hamon |
|-----------|--------------|-----------|
| **Patas** | Ang AI ay hindi dapat magdiskrimina sa mga protektadong grupo | Ang pagtukoy sa pagiging patas sa matematika ay mahirap; maaaring magkasalungat ang iba't ibang kahulugan ng pagiging patas |
| **Transparency** | Dapat malaman ng mga user kung kailan sila nakikipag-ugnayan sa AI at kung paano ito gumagana | Maaaring paganahin ng buong transparency ang paglalaro; ang mga sistema ng pagmamay-ari ay lumalaban sa pagsisiwalat |
| **Pananagutan** | Dapat maging responsable ang isang tao kapag nagdudulot ng pinsala ang AI | Magkalat ng responsibilidad sa mga developer, deployer, at user |
| **Privacy** | Dapat igalang ng AI ang personal na data at awtonomiya | Kadalasang kasama sa data ng pagsasanay ang personal na impormasyon; salungatan sa privacy at utility |
| **Kaligtasan** | Ang AI ay hindi dapat magdulot ng pisikal o sikolohikal na pinsala | Ang pagtukoy sa pinsala ay nakasalalay sa konteksto; ang mga kaso sa gilid ay hindi mahuhulaan |
| **Pagmamasid ng tao** | Dapat panatilihin ng mga tao ang makabuluhang kontrol | Automation bias ay nangangahulugan na ang mga tao ay nagpapaliban sa AI; ang pangangasiwa ay nagiging rubber-stamping |
---

## Bias sa AI Systems
### Saan Nagmumula ang Bias
| Pinagmulan | Paglalarawan | Halimbawa |
|--------|-------------|---------|
| **Data ng pagsasanay** | Mga makasaysayang bias na naka-encode sa data | Ang pag-hire ng data ay sumasalamin sa nakaraang diskriminasyon → model discriminates |
| **Bis ng label** | Ang mga annotator ng tao ay nagpapataw ng kanilang mga bias | Nagpapatuloy na may mga pangalang "babae" na na-rate na mas mababa ng mga annotator |
| **Pagkiling sa pagpili** | Hindi kinakatawan ng data ang target na populasyon | Ang pagkilala sa mukha ay karaniwang sinanay sa mga mukha na maputi ang balat |
| **Pagkampi sa pagsukat** | Mga tampok na proxy para sa mga protektadong katangian | Nauugnay ang zip code sa lahi |
| **Algorithmic bias** | Ang pag-optimize ay nagpapalaki ng maliliit na bias | Ang isang maliit na agwat sa data ng pagsasanay ay nagiging isang malaking agwat sa mga hula |
### Mga Sukatan ng Pagkamakatarungan
| Sukatan | Kahulugan | Kailan Gagamitin |
|--------|-----------|-------------|
| **Demographic parity** | Ang positibong rate ay pantay sa mga pangkat | Kapag gusto mo ng pantay na resulta |
| **Equalized odds** | Ang tunay na positibong rate at maling positibong rate ay pantay sa mga pangkat | Kapag gusto mo ng pantay na mga rate ng error |
| **Mahuhulaang pagkakapare-pareho** | Ang katumpakan ay pantay sa mga pangkat | Kapag gusto mong magkapareho ang kahulugan ng mga hula para sa lahat ng grupo |
| **Indibidwal na pagkamakatarungan** | Ang mga katulad na indibidwal ay ginagamot nang katulad | Kapag gusto mo ng consistency |
**Impossibility theorem**: sa pangkalahatan ay hindi mo matutugunan ang maraming kahulugan ng pagiging patas nang sabay-sabay. Ang pagpili kung aling sukatan ng pagiging patas ang gagamitin ay mismong isang paghatol sa halaga.
### Pagbabawas ng Bias
| Yugto | Teknik |
|-------|-----------|
| **Pre-processing** | Rebalance ng data ng pagsasanay; alisin ang mga pinapanigang tampok; synthetic oversampling |
| **In-processing** | Magdagdag ng mga hadlang sa pagiging patas sa function ng pagkawala; adversarial debiasing |
| **Pagkatapos ng pagproseso** | Ayusin ang mga limitasyon sa bawat pangkat; i-calibrate ang mga hula |
| **Pagsusuri** | Regular na pag-audit ng patas; pinaghiwa-hiwalay na sukatan ng pagganap |
---

## Kakayahang maipaliwanag
### Bakit Mahalaga ang Pagpapaliwanag
| Dahilan | Paglalarawan |
|--------|--------------|
| **Pagtitiwala** | Kailangang maunawaan ng mga gumagamit kung bakit ginawa ang isang desisyon |
| **Pagde-debug** | Kailangang hanapin at ayusin ng mga developer ang mga error sa modelo |
| **Regulasyon** | "karapatan sa pagpapaliwanag" ng GDPR; Mga kinakailangan sa EU AI Act |
| **Patas** | Hindi mo makikita ang bias nang hindi nauunawaan ang gawi ng modelo |
| **Pananagutan** | Kailangang bigyang-katwiran ng mga organisasyon ang mga awtomatikong desisyon |
### Mga Paraan ng Pagpapaliwanag
| Paraan | Uri | Paano Ito Gumagana | Limitasyon |
|--------|------|-------------|------------|
| **SHAP** | Kahalagahan ng feature | Tinatantya ang kontribusyon ng bawat tampok gamit ang teorya ng laro | computationally mahal; mga pagtatantya |
| **LIMA** | Lokal na kahalili | Angkop sa isang simpleng modelo sa paligid ng hula | Hindi matatag; hindi sumasalamin sa aktwal na lohika ng modelo |
| **Attention visualization** | Panloob na mekanismo | Ipakita kung aling mga input ang pinapasukan ng modelo | Pansin ≠ kahalagahan; maaaring mapanlinlang |
| **Counterfactuals** | Paano-kung pagsusuri | "Kung iba ang feature na ito, magbabago ba ang hula?" | Depende sa makatotohanang counterfactuals |
| **Pagpapatungkol sa tampok** | Mga marka ng kahalagahan | Saliency na mga mapa, pinagsamang mga gradient | Hindi nagpapaliwanag *bakit*; basta *saan* |
---

## Regulasyon ng AI
### EU AI Act (2026)
Ang unang komprehensibong batas ng AI sa mundo.
| Antas ng Panganib | Mga halimbawa | Mga Kinakailangan |
|------------|----------|-------------|
| **Hindi katanggap-tanggap na panganib** | Social na pagmamarka; subliminal na pagmamanipula; real-time na biometric surveillance (may mga exception) | Pinagbawalan |
| **Mataas na panganib** | Medikal na AI; autonomous na mga sasakyan; pagpapatupad ng batas; kritikal na imprastraktura | Pagtatasa ng pagkakaayon; pangangasiwa ng tao; transparency |
| **Limitadong panganib** | Chatbots; deepfakes; mga sistema ng rekomendasyon | Dapat ibunyag ang pagkakasangkot sa AI |
| **Minimal na panganib** | Mga filter ng spam; mga video game; karamihan sa mga AI application | Walang tiyak na mga kinakailangan |
### Iba pang Pamamaraang Pang-regulasyon
| Rehiyon | Diskarte | Katayuan |
|--------|----------|--------|
| **Estados Unidos** | Partikular sa sektor; mga executive order; boluntaryong mga pangako | Fragmented; walang komprehensibong pederal na batas |
| **United Kingdom** | Batay sa mga prinsipyo; mga regulator ng sektor | AI Safety Institute; pro-innovation approach |
| **China** | Mga partikular na regulasyon para sa generative AI, deepfakes, rekomendasyon | Aktibong pagpapatupad; mga kinakailangan sa nilalaman |
| **Canada** | AIDA (Artificial Intelligence and Data Act) | Iminungkahi; katulad ng EU approach |
| **Brazil** | Balangkas ng regulasyon ng AI | Isinasagawa |
---

## Epekto sa Kapaligiran
Ang pagsasanay at pagpapatakbo ng mga modelo ng AI ay kumokonsumo ng enerhiya at bumubuo ng mga carbon emissions.
| Aktibidad | Tinantyang Mga Emisyon | Paghahambing |
|----------|--------------------|------------|
| **Pagsasanay GPT-4** | Tinatayang 50+ tonelada CO₂ | Katumbas ng taunang emisyon ng ilang sasakyan |
| **Pagsasanay ng malaking Transformer** | 280-620 tonelada CO₂ | 5x panghabambuhay na emisyon ng kotse |
| **Pang-araw-araw na hinuha (1M user)** | Patuloy; depende sa laki ng modelo at hardware | Maaaring lumampas sa mga emisyon ng pagsasanay sa paglipas ng panahon |
| **Pagpino ng isang 7B na modelo** | 1-5 toneladang CO₂ | Mahalaga ngunit mas mababa kaysa sa pre-training |
### Pagbabawas
| Diskarte | Epekto |
|----------|--------|
| **Mahusay na hardware** | Ang mga bagong GPU ay mas matipid sa enerhiya sa bawat computation |
| **Pag-optimize ng modelo** | Ang mas maliit, na-quantised na mga modelo ay gumagamit ng mas kaunting enerhiya |
| **Berdeng enerhiya** | Mga power data center na may renewable energy |
| **Mahusay na arkitektura** | Pinaghalo ng mga Eksperto; kalat-kalat na mga modelo; paglilinis |
| **Pag-iiskedyul na alam ang carbon** | Magpatakbo ng pagsasanay kapag ang grid ay pinakamalinis |
---

## Intelektwal na Ari-arian at Copyright
| Isyu | Paglalarawan | Katayuan |
|-------|-------------|--------|
| **Pagsasanay sa mga naka-copyright na gawa** | Mga modelong sinanay sa mga aklat, artikulo, larawan nang walang pahintulot | Mga aktibong demanda; patas na paggamit debate |
| **AI-generated na output** | Sino ang nagmamay-ari ng content na binuo ng AI? | Tanggapan ng Copyright sa US: Ang nilalamang binuo ng AI ay hindi maaaring copyright nang walang sapat na akda ng tao |
| **Paggaya ng istilo** | Maaaring gayahin ng AI ang istilo ng isang artist | Legal na kulay abo; etikal na alalahanin |
| **Mga mekanismo sa pag-opt out** | Pinapayagan ng ilang provider ang mga creator na mag-opt out sa pagsasanay | robots.txt; pag-filter ng nilalaman |
---

## Responsableng Pagbubunyag
| Prinsipyo | Paglalarawan |
|-----------|-------------|
| **Pre-deployment testing** | Red teaming, bias audits, safety evaluations before release |
| **Unti-unting pag-deploy** | Magsimula sa limitadong pag-access; palawakin habang ipinapakita ang kaligtasan |
| **Pag-uulat ng insidente** | Magdokumento at magbahagi ng impormasyon tungkol sa mga pagkabigo at pinsala |
| **Mga bug bounty** | Gantimpalaan ang mga panlabas na mananaliksik para sa paghahanap ng mga kahinaan |
| **Mga modelong card** | Mga kakayahan ng modelo ng dokumento, limitasyon, at nilalayon na paggamit |
---

## Data Provenance
| Pag-aalala | Paglalarawan |
|---------|-------------|
| **Transparency ng data ng pagsasanay** | Karamihan sa mga modelo ng hangganan ay hindi nagbubunyag ng kanilang data ng pagsasanay |
| **Pahintulot** | Ginamit ba ang data ng mga indibidwal nang may kaalaman at pahintulot nila? |
| **Paglason sa data** | Maaari bang mag-inject ng malisyosong data ang mga attacker sa mga training set? |
| **Mga dataset card** | Dokumentasyon ng komposisyon ng dataset, mga paraan ng pagkolekta, at mga limitasyon |
| **Watermarking** | Ang pag-embed ng mga invisible marker sa nilalamang binuo ng AI upang makilala ito |
---

## Practical Ethics Frameworks
### Para sa Mga Nag-develop ng AI
| Tanong | Bakit Mahalaga |
|----------|----------------|
| **Sino ang maaaring mapahamak ng sistemang ito?** | Kinikilala ang mga apektadong stakeholder |
| **Ano ang mangyayari kung mali ang modelo?** | Tinatasa ang halaga ng mga error |
| **Maaari bang ipaliwanag ang mga desisyon ng modelo?** | Tinutukoy ang mga kinakailangan sa pagpapaliwanag |
| **Kinatawan ba ang data ng pagsasanay?** | Mga pagsusuri para sa pagpili at pagkiling sa pagsukat |
| **Ano ang mga failure mode?** | Inaasahan ang mga gilid na kaso at maling paggamit |
| **Paano susubaybayan ang system?** | Mga plano para sa patuloy na pangangasiwa |
### Para sa Mga Organisasyong Nag-deploy ng AI
| Magsanay | Paglalarawan |
|----------|-------------|
| ** AI governance board** | Cross-functional team na nagsusuri ng mga deployment ng AI |
| **Mga pagtatasa ng epekto** | Suriin ang mga potensyal na pinsala bago i-deploy |
| **Mga proseso ng pangangasiwa ng tao** | I-clear ang mga escalation path kapag gumawa ng mga error ang AI |
| **Mga regular na pag-audit** | Tingnan kung may bias, drift, at hindi sinasadyang mga kahihinatnan |
| **Mga channel ng feedback ng user** | Pahintulutan ang mga apektadong tao na mag-ulat ng mga problema |
| **Dokumentasyon** | Panatilihin ang mga talaan ng mga desisyon ng modelo at katwiran |
---

## Buod
Ang etika at pamamahala ng AI ay mga kinakailangan sa engineering. Ang bias, opacity, gastos sa kapaligiran, at mga paglabag sa privacy ay hindi lamang etikal na alalahanin; ang mga ito ay mga depekto na nagdudulot ng tunay na pinsala. Mabilis na umuunlad ang landscape ng pamamahala, kasama ang EU AI Act na nagtatakda ng pandaigdigang pamantayan. Ang regulasyon lamang ay hindi sapat — ang pagiging patas, pagpapaliwanag, at pananagutan ay dapat isama sa pang-araw-araw na gawain ng bawat AI developer. Ang pangunahing tanong ay kung paano bumuo ng mga sistema na karapat-dapat sa pagtitiwala.