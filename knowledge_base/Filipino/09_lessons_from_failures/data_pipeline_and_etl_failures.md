---
# Metadata
title: "Data Pipeline and ETL Failures"
description: "Schema drift, duplicate data, validation gaps, pipeline monitoring"
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
tags: [data, pipeline, etl, failures, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Data Pipeline at ETL Failures
Ang mga pipeline ng data ay ang pagtutubero ng mga modernong organisasyon — inililipat nila ang data mula sa mga source system sa pamamagitan ng mga pagbabago sa mga database, warehouse, at lawa kung saan ito ginagamit para sa analytics, machine learning, at paggawa ng desisyon. Kapag nagtatrabaho sila, walang nakakapansin. Kapag nabigo ang mga ito, ang mga pagpapasya ay ginagawa sa lipas na data, ang mga modelo ay nagsasanay sa basura, ang mga ulat ay nagpapakita ng mga imposibleng numero, at ang tiwala sa buong data platform ay nawawala. Ang mga pagkabigo sa pipeline ng data ay kabilang sa mga pinakakaraniwan at pinakamahal na pagkabigo sa mga organisasyong teknolohiya.
---

## Mga Karaniwang Mode ng Pagkabigo
### Mga Isyu sa Kalidad ng Data
| Pagkabigo | Paglalarawan | Epekto | Kahirapan sa Pagtukoy |
|---------|------------|--------|---------------------|
| **Silent data corruption** | Ang data ay nabago nang hindi tama nang walang anumang error na itinataas | Ang mga downstream system ay nagtitiwala sa masamang data; mga desisyon batay sa maling impormasyon | Napakahirap — walang error signal |
| **Skema drift** | Ang source system ay nagbabago ng schema (nagdaragdag, nag-aalis, nagpapalitan ng pangalan ng mga column) | Pipeline break o tahimik na bumaba ng data | Katamtaman — maaaring mabigo ang pipeline o makagawa ng mga bahagyang resulta |
| **Hindi tugma sa uri ng data** | Nagpapadala ang pinagmulan ng string kung saan inaasahan ang integer; mga pagbabago sa katumpakan ng float | Nabigo ang pipeline; pinutol ang data; mga error sa rounding | Katamtaman — maaaring magdulot ng error sa pipeline o banayad na mga isyu sa data |
| **Mga duplicate na tala** | Ang parehong kaganapan ay naproseso nang maraming beses | Napalaki ang bilang; maling pagsasama-sama | Mahirap — bawat tala ay mukhang wasto nang paisa-isa |
| **Null / missing values** | Ang mga inaasahang field ay walang laman | Nabigo ang mga kalkulasyon; ang mga modelo ay gumagawa ng mga maling hula | Medium — depende sa null handling |
| **Mga wala sa saklaw na halaga** | Mga halaga sa labas ng inaasahang mga hangganan (negatibong edad; mga petsa sa hinaharap) | Mga skewed na istatistika; sirang lohika ng negosyo | Medium — nangangailangan ng mga panuntunan sa pagpapatunay |
| **Data na huli na dumating** | Dumarating ang data pagkatapos magsara ang window ng pagproseso | Mga hindi kumpletong resulta; napalampas na mga tala | Mahirap — mukhang kumpleto ang mga resulta ngunit hindi |
### Mga Isyu sa Imprastraktura ng Pipeline
| Pagkabigo | Paglalarawan | Epekto |
|---------|-------------|--------|
| **Kabiguan sa orkestra** | Ang Scheduler (Airflow, Prefect) ay hindi nagti-trigger ng pipeline | Ang data ay lipas na; walang pagproseso na nagaganap |
| **Pagkaubos ng mapagkukunan** | Naubusan ng memory, CPU, o disk ang pipeline | Pag-crash ng pipeline; bahagyang resulta |
| **Kabiguan ng dependency** | Ang upstream system ay pababa o mabagal | Ang pipeline ay naghihintay nang walang katiyakan o nabigo |
| **Mga isyu sa pagkakatugma** | Binabago ng maraming pipeline ang parehong data nang sabay-sabay | Mga kondisyon ng lahi; data corruption |
| **Configuration drift** | Ang mga pagbabago sa kapaligiran (network, mga kredensyal, mga endpoint) ay hindi makikita sa pipeline | Nabigo ang pipeline nang hindi inaasahan |
| **Backpressure** | Dumating ang data nang mas mabilis kaysa sa maaaring iproseso ng pipeline | Lumalaki ang mga pila; pagtaas ng latency |
---

## Pag-aaral ng Kaso
### Pag-aaral ng Kaso 1: Silent Data Duplication
| Aspeto | Paglalarawan |
|--------|--------------|
| **Scenario** | Pinoproseso ng pipeline ng order ng isang e-commerce na kumpanya ang mga kaganapan mula sa isang queue ng mensahe |
| **Ano ang nangyari** | Ang pag-restart ng consumer ay naging sanhi ng muling paggamit ng mga mensahe; walang lohika ng deduplication na umiral |
| **Epekto** | Ang mga numero ng kita ay napalaki ng 15% sa loob ng 3 linggo bago may nakapansin |
| **Root cause** | Walang mga susi ng idempotency; hindi bababa sa isang beses na paghahatid nang walang deduplikasyon |
| **Ayusin** | Nagdagdag ng mga idempotency key batay sa order ID; ipinatupad nang eksakto-isang beses semantics |
| **Aralin** | Ang hindi bababa sa isang beses na paghahatid ay nangangailangan ng deduplikasyon; palaging patunayan ang mga kabuuan laban sa mga source system |
### Pag-aaral ng Kaso 2: Pagbabago ng Schema Breaks Downstream
| Aspeto | Paglalarawan |
|--------|--------------|
| **Scenario** | Binago ng provider ng pagbabayad ang pangalan ng field sa kanilang tugon sa API |
| **Ano ang nangyari** | Ang ETL pipeline ay tahimik na nagsimulang magsulat ng mga null value; walang pagpapatunay ng schema |
| **Epekto** | Ang mga ulat sa pananalapi ay nagpakita ng zero na kita mula sa paraan ng pagbabayad na iyon sa loob ng 2 buwan |
| **Root cause** | Walang pagpapatunay ng schema sa paglunok; ang mga null na halaga ay itinuturing bilang wastong |
| **Ayusin** | Nagdagdag ng pagpapatunay ng schema na may mga alerto; ipinapatupad ang mga kinakailangang field; null checks |
| **Aralin** | Huwag kailanman magtiwala sa mga panlabas na schema upang manatiling matatag; patunayan sa hangganan |
### Case Study 3: Time Zone Catastrophe
| Aspeto | Paglalarawan |
|--------|--------------|
| **Scenario** | Pinagsasama-sama ng isang pandaigdigang kumpanya ang mga pang-araw-araw na sukatan sa mga opisina |
| **Ano ang nangyari** | Ang ilang mga mapagkukunan ay gumamit ng UTC, ang iba ay gumamit ng lokal na oras; hindi nag-normalize ang pipeline |
| **Epekto** | Hindi tumugma ang mga pang-araw-araw na kabuuan; ilang mga transaksyon na binibilang sa maling araw; mali ang pagsasara sa katapusan ng buwan |
| **Root cause** | Walang karaniwang patakaran sa time zone; mga timestamp na hindi pantay na nakaimbak |
| **Ayusin** | Lahat ng timestamp na nakaimbak bilang UTC; conversion sa lokal na oras lamang sa presentation layer |
| **Aralin** | I-standardize sa UTC sa lahat ng dako; maging tahasan ang tungkol sa mga time zone sa bawat hangganan |
---

## Mga Istratehiya sa Pag-iwas
### Pagpapatunay ng Data
| Diskarte | Paglalarawan | Mga Halimbawa ng Tool |
|----------|-------------|--------------|
| **Pagpapatunay ng schema** | I-verify ang data na tumutugma sa inaasahang schema sa bawat yugto | Mahusay na Inaasahan; Deequ; Soda |
| **Mga pagsusuri sa hanay** | Ang mga halaga ay nasa loob ng inaasahang mga hangganan | Mga pasadyang pahayag; mga pagsubok sa dbt |
| **Mga pagsusuri sa pagiging bago** | Ang data ay sapat na kamakailan lamang upang maging kapaki-pakinabang | Pagsubaybay sa mga timestamp; Mga alerto sa SLA |
| **Mga pagsusuri sa volume** | Ang mga bilang ng row ay nasa loob ng inaasahang saklaw | Ang pagtuklas ng anomalya sa mga bilang ng hilera |
| **Referential integrity** | Ang mga dayuhang susi ay tumutugma; walang mga naulilang talaan | Mga hadlang sa SQL; mga tool sa kalidad ng data |
| **Cross-source reconciliation** | Tumutugma ang mga kabuuan sa pagitan ng pinagmulan at target | Mga trabaho sa awtomatikong pagkakasundo |
### Mga Pattern ng Disenyo ng Pipeline
| Pattern | Paglalarawan | Benepisyo |
|---------|-------------|---------|
| **Idempotency** | Ang pagpapatakbo ng pipeline nang maraming beses ay gumagawa ng parehong resulta | Ligtas na muling subukan; walang mga duplicate |
| **Atomicity** | Ang pipeline ay ganap na nagtagumpay o ganap na nabigo (walang bahagyang estado) | Walang kalahating naprosesong data |
| **Pagsusuri** | I-save ang pag-unlad sa bawat yugto; ipagpatuloy mula sa huling checkpoint | Fault tolerance; walang reprocessing |
| **Mga patay na sulat na pila** | Ang mga nabigong talaan ay pumupunta sa isang hiwalay na pila para sa pagsisiyasat | Walang pagkawala ng data; maaaring mag-imbestiga at mag-replay |
| **Mga circuit breaker** | Ihinto ang pagproseso kapag ang downstream ay nabigo | Pigilan ang mga pagkabigo ng cascading |
| **Mga kontrata ng data** | Kasunduan sa pagitan ng mga producer at consumer tungkol sa format ng data | Ang mga pagbabago sa schema ay pinag-ugnay |
### Pagsubaybay at Pag-alerto
| Ano ang Susubaybayan | Bakit | Paano |
|-----------------|-----|-----|
| **Tagal ng pipeline** | Mga problema sa signal ng pagtaas ng tagal | Pagsusuri ng trend; Pagsubaybay sa SLA |
| **Bilang ng hilera** | Ang mga biglaang pagbabago ay nagpapahiwatig ng mga problema | Ikumpara sa mga makasaysayang average |
| **Null rates** | Ang pagtaas ng nulls signal schema o mga isyu sa pinagmulan | Null tracking sa antas ng column |
| **Pagiging bago ng data** | Ang lipas na data ay nangangahulugan na ang pipeline ay hindi tumatakbo | Timestamp ng pinakabagong tala |
| **Downstream na epekto** | Gumagamit ba ng tamang data ang mga ulat at modelo? | End-to-end na lineage ng data |
| **Paggamit ng mapagkukunan** | CPU; memorya; disk; network | Pagsubaybay sa imprastraktura |
---

## Mga Diskarte sa Pagbawi
| Sitwasyon | Diskarte |
|-----------|----------|
| **Nasa warehouse na ang masamang data** | Tukuyin ang apektadong saklaw ng oras; muling iproseso mula sa pinagmulan; abisuhan ang mga mamimili sa ibaba ng agos |
| **Pagkabigo ng pipeline sa kalagitnaan ng pagtakbo** | Ang idempotent na disenyo ay nagbibigay-daan sa ligtas na muling pagtakbo; pinapayagan ng checkpointing ang resume |
| **Nasira ang pipeline ng pagbabago ng schema** | Ayusin ang pagbabagong-anyo; i-backfill ang apektadong data; magdagdag ng schema evolution handling |
| **Silent corruption huli na natuklasan** | Pagsusuri ng sanhi ng ugat; matukoy ang radius ng sabog; muling proseso; magdagdag ng pagsubaybay upang mahuli ang pag-ulit |
| **Pagkawala ng data** | Ibalik mula sa backup; replay mula sa pinagmulan; tasahin kung mababawi ang pagkawala |
---

## Buod
Ang mga pagkabigo ng pipeline ng data ay nasa lahat ng dako at kadalasang mas mahal kaysa sa mga pagkawala ng aplikasyon dahil gumagawa sila ng mga maling sagot sa halip na mga halatang error. Ang silent data corruption, schema drift, duplicate, time zone bug, at nawawalang value ay ang pinakakaraniwang mga salarin. Ang mga pangunahing diskarte sa pag-iwas ay: patunayan ang data sa bawat hangganan (schema, saklaw, dami, pagiging bago); magdisenyo ng mga pipeline upang maging idempotent at atomic; subaybayan ang lahat (tagal, bilang ng hilera, null rate, pagiging bago); gumamit ng mga patay na sulat na pila para sa mga nabigong rekord; at magtatag ng mga kontrata ng data sa pagitan ng mga producer at mga mamimili. Kapag naganap ang mga pagkabigo, ang tugon ay dapat magsama ng root cause analysis, muling pagproseso ng mga apektadong data, abiso ng downstream na mga consumer, at — kritikal na — pagdaragdag ng pagsubaybay upang mahuli ang parehong klase ng pagkabigo sa hinaharap. Ang mga organisasyong nakakakuha ng tama nito ay tinatrato ang mga pipeline ng data na may kahigpitan tulad ng production software: pagsubok, pagsubaybay, pag-alerto, pagtugon sa insidente, at mga post-mortem.