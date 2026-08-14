<!--
---
# Metadata
title: "Machine Learning Project Failures"
description: "Data leakage, expectation mismatches, deployment failures, model decay"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ml, project, failures, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Mga Pagkabigo sa Machine Learning Project
Ang mga proyekto sa pag-aaral ng makina ay nabigo sa isang nakakaalarmang rate — iminumungkahi ng mga pagtatantya ng industriya na 60-85% ng mga proyekto ng ML ay hindi na umabot sa produksyon. Ang mga pagkabigo ay hindi karaniwan sa mga algorithm; nasa proseso sila, ang data, ang mga inaasahan, at ang konteksto ng organisasyon. Ang pag-unawa kung bakit nabigo ang mga proyekto ng ML ay mahalaga para sa sinumang gumagawa ng mga ML system, dahil ang mga mode ng pagkabigo ay mahuhulaan at higit na maiiwasan.
---

## Bakit Nabigo ang Mga Proyekto ng ML
### Mga Kategorya ng Pagkabigo
| Kategorya | Bahagi ng mga Pagkabigo | Paglalarawan |
|----------|-------------------|-------------|
| **Mga problema sa data** | ~30% | Hindi sapat ang data, bias, lipas, o hindi naa-access |
| **Kahulugan ng problema** | ~20% | Ang problema sa ML ay hindi tumutugma sa pangangailangan ng negosyo |
| **Hindi tugma sa inaasahan** | ~15% | Inaasahan ng mga stakeholder ang magic; ang katotohanan ay incremental improvement |
| **Pagkabigo sa deployment** | ~15% | Gumagana ang modelo sa mga notebook ngunit hindi ma-produce |
| ** mga isyu sa organisasyon** | ~10% | Walang malinaw na pagmamay-ari; ang koponan ay walang mga kasanayan; walang suporta sa ehekutibo |
| **Pagganap ng modelo** | ~10% | Hindi nakakamit ng modelo ang kinakailangang katumpakan o hindi maganda ang pag-generalize |
---

## Mga Pagkabigong Kaugnay ng Data
### Mga Karaniwang Problema sa Data
| Problema | Paglalarawan | Halimbawa |
|---------|-------------|---------|
| **Hindi sapat na data** | Hindi sapat na mga halimbawa upang matuto ng mga makabuluhang pattern | Pagsasanay ng modelo ng pagtuklas ng panloloko sa 500 transaksyon |
| **Kalidad ng label** | Ang mga label ng pagsasanay ay mali, hindi pare-pareho, o subjective | Mga medikal na larawan na may label ng mga hindi eksperto; mga label ng damdamin na may mababang kasunduan sa inter-rater |
| **Pag-leakage ng data** | Ang impormasyon mula sa hinaharap o target ay tumagas sa mga tampok | Paggamit ng kinalabasan ng customer churn bilang isang feature; kasama ang data ng pagsubok sa pagsasanay |
| **Pagkiling sa pagpili** | Hindi kinakatawan ng data ng pagsasanay ang populasyon ng deployment | Pagsasanay ng medikal na modelo sa data mula sa isang ospital; pag-deploy sa buong bansa |
| **Concept drift** | Ang ugnayan sa pagitan ng mga feature at target ay nagbabago sa paglipas ng panahon | Nagbabago ang pag-uugali ng mamimili pagkatapos ng isang pandemya; modelong sinanay sa pre-pandemic na data |
| **Feature mismatch** | Ang mga tampok na magagamit sa panahon ng pagsasanay ay naiiba sa mga magagamit sa produksyon | Pagsasanay na may mga manu-manong label; Gumagamit ang produksyon ng mga awtomatikong label na may iba't ibang pamamahagi |
| **Imbalance ng klase** | Ang mga target na klase ay lubos na baluktot | 99% negatibo, 1% positibo; natututo ang modelo na laging hulaan ang negatibo |
### Ang Problema sa Data Leakage
| Uri | Paglalarawan | Halimbawa |
|------|-------------|---------|
| **Target na pagtagas** | Ang isang tampok ay magagamit lamang pagkatapos maganap ang target | Ginamit ang "kinalabasan ng paggamot" bilang isang tampok upang mahulaan ang "tagumpay ng paggamot" |
| **Train-test contamination** | Ang data ng pagsubok ay nakakaimpluwensya sa pagsasanay | Pag-scale gamit ang mga pandaigdigang istatistika (kasama ang data ng pagsubok); data augmentation na tumutulo |
| **Sampling bias** | Ang pagsasanay at produksyon ay gumagamit ng iba't ibang sampling | Pagsasanay sa trapiko sa web; pag-deploy sa trapiko ng mobile app |
| **Pre-processing leakage** | Ang hakbang sa preprocessing ay gumagamit ng impormasyon mula sa buong dataset | Imputing ang mga nawawalang value sa global mean (kasama ang data ng pagsubok) |
---

## Mga Pagkabigo sa Depinisyon ng Problema
### Mga Pattern ng Pagkakamali
| Pattern | Paglalarawan | Bunga |
|---------|-------------|-------------|
| **Paglutas ng maling problema** | Kailangan ng negosyo X; binuo ng koponan ang Y | Ang modelo ay teknikal na mabuti ngunit walang silbi |
| **ML kapag sapat na ang mga panuntunan** | Ang problema ay may mga tuntuning deterministiko; Ang ML ay nagdaragdag ng pagiging kumplikado | Over-engineered; mas mahirap mapanatili; hindi gaanong maipaliwanag |
| **ML kapag walang data** | Ang problema ay nangangailangan ng data na hindi pa nakolekta | Hindi makapagsimula ang proyekto; nasayang na buwan sa pagiging posible |
| **Target ng katumpakan nang walang konteksto ng negosyo** | "Kailangan namin ng 95% katumpakan" — ngunit ano ang ibig sabihin nito para sa negosyo? | Natutugunan ng modelo ang katumpakan ngunit hindi nilulutas ang problema sa negosyo |
| **Pagbabalewala sa halaga ng mga error** | Ang mga maling positibo at maling negatibo ay may magkaibang gastos | Ino-optimize ng modelo ang maling sukatan |
| **Walang baseline** | Walang paghahambing sa umiiral na diskarte | Hindi masabi kung ang ML ay talagang mas mahusay kaysa sa isang simpleng heuristic |
---

## Mga Pagkabigo sa Inaasahan
### Ang Hype Cycle sa ML Projects
| Yugto | Paglalarawan | Panganib |
|-------|-------------|------|
| **Kasabikan** | "Aayusin ng AI ang lahat!" | Over-promising; kulang sa mapagkukunan |
| **Patunay ng konsepto** | Gumagana ang modelo sa malinis na data sa mga notebook | Maling pagtitiwala; "ito gumagana!" |
| **Reality check** | Ang data ng produksyon ay magulo; bumaba ang pagganap | Pagkadismaya; "Hindi gumagana ang ML" |
| **Death march** | Sinusubukan ng koponan na pilitin ito sa produksyon | Teknikal na utang; pagkasunog |
| **Pag-abandona o tahimik na pag-deploy** | Kinansela o na-deploy ang proyekto nang walang pagsubaybay | Nasayang na puhunan |
### Pamamahala ng mga Inaasahan
| Diskarte | Paglalarawan |
|----------|-------------|
| **Magsimula sa isang baseline** | Ikumpara sa pinakasimpleng posibleng diskarte (mga panuntunan; pagganap ng tao) |
| **Tukuyin ang mga sukatan ng tagumpay nang maaga** | Mga sukatan ng negosyo (kita; matitipid) hindi lang mga sukatan ng ML (katumpakan; F1) |
| **Paggalugad ng time-box** | Bigyan ang koponan ng 2-4 na linggo upang masuri ang pagiging posible bago gumawa ng |
| **Ipakita ang hindi kayang gawin ng ML** | Maging tapat tungkol sa mga limitasyon; magtakda ng makatotohanang mga inaasahan |
| **Ulitin nang paunti-unti** | I-deploy muna ang isang simpleng modelo; paulit-ulit na mapabuti |
| **Bantayan ang halaga ng mga error** | Isalin ang pagganap ng modelo sa epekto sa negosyo |
---

## Mga Pagkabigo sa Deployment
### Bakit Hindi Nagagawa ng Mga Modelo sa Produksyon
| Problema | Paglalarawan | Solusyon |
|---------|-------------|----------|
| **Notebook sa production gap** | Gumagana ang code sa Jupyter ngunit hindi handa sa produksyon | Mga kasanayan sa MLOps; CI/CD para sa ML; pagsusuri ng code |
| **Mga kinakailangan sa latency** | Masyadong mabagal ang hinuha ng modelo para sa real-time na paggamit | Pag-optimize ng modelo; quantization; pag-cache |
| **Scalability** | Hindi kaya ng modelo ang trapiko ng produksyon | Batch processing; pahalang scaling; modelo na naghahatid ng imprastraktura |
| **Mga puwang sa pagsubaybay** | Walang paraan upang matukoy kapag nasira ang modelo | Pagsubaybay sa drift ng data; pagsubaybay sa pagganap; nagpapaalerto |
| **Pamamahala ng dependency** | Magkaiba ang mga kapaligiran sa pagsasanay at paghahatid | Containerization; mga reproducible na kapaligiran |
| **Walang rollback plan** | Hindi maibabalik sa dating modelo kapag nabigo ang bagong modelo | Rehistro ng modelo; bersyon; awtomatikong rollback |
### Pagkabulok ng Modelo
| Uri | Paglalarawan | Pagtuklas |
|------|-------------|-----------|
| **Data drift** | Ang mga pamamahagi ng tampok na input ay nagbabago | Subaybayan ang mga istatistika ng tampok; KL divergence; PSI |
| **Concept drift** | Relasyon sa pagitan ng mga feature at target na pagbabago | Subaybayan ang katumpakan ng hula sa paglipas ng panahon |
| **Pag-anod ng label** | Kahulugan o pamamahagi ng mga pagbabago sa target | Subaybayan ang mga pamamahagi ng label; ugnayan ng sukatan ng negosyo |
| **Mga pagbabago sa upstream** | Binabago ng data source ang format, timing, o kalidad | Pagpapatunay ng schema; pagsubaybay sa pagiging bago |
---

## Mga Pagkabigo sa Organisasyon
| Pagkabigo | Paglalarawan | Pag-iwas |
|---------|-------------|------------|
| **Walang malinaw na pagmamay-ari** | Walang mananagot para sa modelo sa produksyon | Magtalaga ng mga may-ari ng modelo; tukuyin ang RACI |
| **Siloed team** | Ang mga data scientist ay bumuo ng mga modelo; inhinyero deploy; walang nakikipag-usap | Mga cross-functional na koponan; ibinahaging layunin |
| **Walang MLOps maturity** | Walang rehistro ng modelo; walang CI/CD; walang pagsubaybay | Mamuhunan sa imprastraktura ng MLOps nang paunti-unti |
| **Mga hindi makatotohanang timeline** | "Bumuo ng production ML system sa loob ng 2 linggo" | Paggalugad ng time-box; umulit; makipag-usap sa pagiging kumplikado |
| **Kakulangan ng kadalubhasaan sa domain** | Hindi naiintindihan ng ML team ang problema sa negosyo | I-embed ang mga eksperto sa domain sa mga ML team |
| **Walang balangkas ng pagsusuri** | Hindi masabi kung gumagana ang modelo sa produksyon | Tukuyin ang mga sukatan ng negosyo; mag-set up ng mga dashboard; mga regular na pagsusuri |
---

## Mga Aral na Natutunan
### Ang Checklist ng Proyekto ng ML
| Yugto | Susing Tanong |
|-------|-------------|
| **Kahulugan ng problema** | Problema ba talaga ito sa ML? Ano ang baseline? Ano ang hitsura ng tagumpay? |
| **Pagsusuri ng data** | Mayroon ba tayong sapat na data? Kinatawan ba ito? Maaasahan ba ang mga label? |
| **Pagiging posible** | Maaari ba tayong bumuo ng gumaganang prototype sa loob ng 2-4 na linggo? Ano ang mga panganib? |
| **Pag-unlad** | Mayroon bang data leakage? Ginagamit ba natin ang tamang sukatan ng pagsusuri? |
| **Pre-production** | Gumagana ba ito sa data ng produksyon? Ito ba ay sapat na mabilis? Ito ba ay sinusubaybayan? |
| **Deployment** | Maaari ba tayong bumalik? Sino ang on-call? Ano ang mangyayari kapag ito ay bumababa? |
| **Pagkatapos ng pag-deploy** | Sinusubaybayan ba natin ang drift? Sinusubaybayan ba ang mga sukatan ng negosyo? Mayroon bang plano sa muling pagsasanay? |
---

## Buod
Ang mga proyekto ng ML ay nabigo hindi dahil ang mga algorithm ay masyadong mahirap, ngunit dahil ang proseso sa kanilang paligid ay nasira. Ang mga problema sa data — hindi sapat na data, hindi magandang label, pagtagas, drift — ang dahilan ng pinakamalaking bahagi ng mga pagkabigo. Mga pagkabigo sa pagtukoy ng problema — paglutas ng maling problema, paggamit ng ML kung kailan sapat na ang mga panuntunan, pagwawalang-bahala sa halaga ng mga pagkakamali — pag-aaksaya ng mga buwan ng pagsisikap. Mga pagkabigo sa inaasahan — labis na pangako, kulang sa paghahatid, hindi pamamahala sa mga stakeholder — sirain ang tiwala ng organisasyon sa ML. Ang mga pagkabigo sa pag-deploy — mga puwang sa notebook-to-production, mga isyu sa latency, walang pagsubaybay — ay nangangahulugan na ang mga modelong gumagana sa development ay hindi kailanman lumilikha ng halaga sa produksyon. Ang mga pagkabigo ng organisasyon — walang pagmamay-ari, mga siled na koponan, walang mga MLOp — ginagawang imposibleng magtagumpay sa istruktura. Ang antidote ay disiplinadong pagsasanay: magsimula sa isang baseline; paggalugad ng time-box; patunayan ang data nang mahigpit; suriin para sa pagtagas; tukuyin ang mga sukatan ng negosyo; unti-unting i-deploy; patuloy na subaybayan; at umulit. Ang pinakamahusay na mga koponan ng ML ay gumugugol ng mas maraming oras sa data at proseso kaysa sa mga modelo.