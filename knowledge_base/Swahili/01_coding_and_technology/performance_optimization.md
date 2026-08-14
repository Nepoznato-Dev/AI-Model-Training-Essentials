---
# Metadata
title: "Performance Optimisation"
description: "Profiling, caching, CDN, query optimisation, front-end perf"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [performance, optimization, coding-and-technology]
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

# Uboreshaji wa Utendaji
Uboreshaji wa utendakazi ni mazoea ya kufanya programu iwe haraka zaidi - kupunguza nyakati za majibu, kuongeza matokeo, kupunguza utumiaji wa kumbukumbu na kuondoa vikwazo. Ni mojawapo ya ujuzi wenye athari zaidi msanidi programu anaweza kuwa nao, kwa sababu programu polepole hupoteza watumiaji, hupoteza rasilimali, na hufadhaisha kila mtu. Lakini pia ni mojawapo ya makosa yanayofanywa mara nyingi, huku wasanidi programu wakiboresha mambo yasiyofaa kulingana na angavu badala ya ushahidi.
---

## Kanuni ya Dhahabu
> **Pima kwanza, boresha ya pili.** Kamwe usiboresha kulingana na mawazo. Wasifu msimbo, tafuta kizuizi halisi, na urekebishe.
| Kupinga muundo | Kwanini Ni Mbaya |
|---------------------------|
| **Uboreshaji mapema** | Kutumia muda kuharakisha msimbo ambao sio polepole |
| **Kuboresha bila kipimo** | Kurekebisha kizuizi kibaya; hakuna njia ya kuthibitisha uboreshaji |
| **Kutoa dhabihu usomaji kwa kasi** | Msimbo usiosomeka unagharimu zaidi ya faida ya utendakazi |
| **Kuhifadhi kila kitu** | Data ya zamani, kuharibika kwa kumbukumbu, utata |
---

##Kuweka wasifu
Kabla ya kufanya kitu haraka, unahitaji kujua *wakati* unatumika.
| Aina ya Zana | Inapima Nini | Mifano |
|-----------|----------------|----------|
| **Kiweka wasifu wa CPU** | Ni vipengele vipi vinavyotumia muda mwingi wa CPU | cProfile (Python), perf (Linux), Chrome DevTools (JS) |
| **Wasifu wa kumbukumbu** | Ugawaji wa kumbukumbu na uvujaji | tracemalloc (Python), Valgrind, heaptrack |
| **Mtengeneza wasifu wa I/O** | Diski na mtandao I/O vikwazo | iotop, strace, Wireshark |
| **APM (Ufuatiliaji wa Utendaji wa Programu)** | Muda wa ombi la mwisho hadi mwisho | Relic Mpya, Datadog, Jaeger |
| **Vyombo vya Kuvinjari vya Kivinjari** | Utoaji wa mazingira ya mbele, Utekelezaji wa JavaScript, mtandao | Chrome DevTools, Firefox Profiler |
### Mtiririko wa Kazi wa Kuweka Wasifu
| Hatua | Maelezo |
|------|-------------|
| 1. Tambua operesheni polepole | Watumiaji huripoti upakiaji wa ukurasa polepole; ufuatiliaji unaonyesha utulivu wa hali ya juu |
| 2. Wasifu njia kamili | Tafuta ni sehemu gani inachukua muda mwingi |
| 3. Chimba chini | Wasifu sehemu hiyo mahususi ya kupata kitendakazi moto |
| 4. Rekebisha kizuizi | Tumia uboreshaji unaofaa |
| 5. Pima tena | Thibitisha uboreshaji; kuangalia kwa regressions |
---

## Uboreshaji wa Algorithmic
Manufaa makubwa zaidi ya utendakazi yanatokana na kuchagua algoriti bora, si kutoka kwa uboreshaji mdogo.
| Badilisha | Uboreshaji |
|--------|------------|
| Utafutaji wa mstari O(n) → Tafuta jedwali la hash O(1) | 100x+ kwa hifadhidata kubwa |
| Kitanzi kilichowekwa O(n²) → Panga + utafutaji wa binary O(n logi n) | Maagizo ya ukubwa kwa n kubwa |
| Uhesabuji unaorudiwa → Uhifadhi/uhifadhi | Huondoa kazi isiyo ya lazima |
| Muunganisho wa kamba katika kitanzi → Mjenzi / jiunge | Epuka kunakili kamba za pembe nne |
| Data ambayo haijachanganuliwa → Iliyopangwa data kwa utafutaji wa binary | O(logi n) badala ya O(n) kwa kila utafutaji |
---

## Mikakati ya Uhifadhi
Duka za akiba zimekokotoa matokeo kwa hivyo hazihitaji kuhesabiwa tena.
| Aina ya Akiba | Mahali | Kasi | Maisha |
|-----------|----------|-------|----------|
| **Kache ya CPU** | L1/L2/L3 | ~ns 1 | Otomatiki |
| **Katika kumbukumbu** | RAM ya programu (dict, HashMap) | ~100 ns | Hadi kuondolewa au kufukuzwa |
| **Kache iliyosambazwa** | Redis, Memcached | ~ms 1 | TTL inayoweza kusanidiwa |
| **CDN** | Seva za makali duniani kote | ~10-50 ms | TTL inayoweza kusanidiwa |
| **Kache ya kivinjari** | Kivinjari cha mtumiaji | ~ms 1 | Vichwa vya akiba vya HTTP |
| **Kache ya hoja ya hifadhidata** | Hifadhidata au kiwango cha ORM | ~ms 1-10 | Hadi data ibadilike |
### Miundo ya Akiba
| Muundo | Maelezo | Wakati wa Kutumia |
|---------|---------------------------|
| **Kando ya akiba** | Maombi hukagua kashe; mizigo kutoka kwa DB kwa kukosa; maduka katika kache | Ya kawaida zaidi; rahisi |
| **Andika** | Andika kwa akiba na DB wakati huo huo | Anaposoma >> anaandika; uthabiti muhimu |
| **Andika-nyuma** | Andika kwa kache; andika kwa usawa kwa DB | Kiwango cha juu cha maandishi; hatari fulani ya kupoteza data |
| **TTL (Muda wa Kuishi)** | Maingizo ya akiba yanaisha baada ya muda uliowekwa | Wakati data inabadilika mara kwa mara |
| **Batili** | Ondoa kwa uwazi maingizo ya akiba ya zamani | Wakati unajua hasa wakati data inabadilika |
### Uthibitishaji wa Akiba
Matatizo mawili magumu zaidi katika sayansi ya kompyuta: kubatilisha akiba, kutaja vitu, na makosa ya moja kwa moja.
| Mkakati | Maelezo |
|----------|-------------|
| **TTL-msingi** | Maingizo yanaisha baada ya sekunde N; rahisi lakini inaweza kutoa data ya zamani |
| **Inayoendeshwa na tukio** | Batilisha data inapobadilika; ngumu zaidi lakini sahihi |
| **Kulingana na toleo** | Jumuisha nambari ya toleo; ongezeko la mabadiliko |
| **Msingi wa lebo** | Tag maingizo ya akiba yanayohusiana; kubatilisha maingizo yote kwa lebo |
---

## Uboreshaji Hifadhidata
Hifadhidata mara nyingi ndio kizuizi kikubwa katika programu za wavuti.
| Mbinu | Maelezo | Athari |
|-----------|-------------|--------|
| **Kuashiria** | Ongeza faharasa kwenye safu wima zinazotumika katika WHERE, JIUNGE, ORDER BY | 10-1000x maswali ya haraka |
| **Uboreshaji wa hoja** | Epuka CHAGUA *; tumia EXPLAIN kuchanganua maswali | Punguza I/O |
| **Kuunganisha muunganisho** | Tumia tena miunganisho ya hifadhidata badala ya kuunda mpya | Ondoa kichwa cha muunganisho |
| **Soma nakala** | Sambaza hoja zilizosomwa kwa hifadhidata za nakala | Sambaza mzigo uliosomwa |
| **Kugawanyika** | Gawanya meza kubwa katika sehemu ndogo | Maswali ya haraka kwenye hifadhidata kubwa |
| **Denormalisation** | Ongeza data isiyohitajika ili kuepuka kujiunga | Inasoma haraka zaidi; polepole anaandika |
| **Mionekano ya nyenzo** | Matokeo ya swali lililokokotwa mapema | Maswali changamano ya papo hapo |
| **N+1 kinga** | Tumia JOIN, upakiaji wa hamu, au hoja za kundi | Ondoa maelfu ya maswali |
---

## Concurrency na Usambamba
| Dhana | Maelezo | Wakati wa Kutumia |
|---------|---------------------------|
| **Uzi** | Nyuzi nyingi ndani ya mchakato mmoja | Kazi za I/O-zilizofungwa (mtandao, diski) |
| **Uchakataji mwingi** | Michakato mingi (inapita GIL kwenye Python) | Kazi zinazofungamana na CPU |
| **Async/subiri** | Ushirikiano wa multitasking; thread moja | I/O ya sarafu ya juu (seva za wavuti) |
| **GPU kompyuta** | Maelfu ya cores sambamba | Operesheni za matrix; usindikaji wa picha; ML |
### Async dhidi ya Threading
| Kipengele | Async/Subiri | Uandishi |
|--------|------------|-----------|
| **Mfano** | Ushirika (udhibiti wa mavuno ya kazi) | Preemptive (OS hubadilisha nyuzi) |
| **Kichwa** | Chini sana (hakuna ubadilishaji wa muktadha) | Juu (uundaji wa nyuzi, ubadilishaji wa muktadha) |
| **Utata** | Hoja rahisi (uzi moja) | Masharti ya mbio, kufuli, kufuli |
| **Bora kwa** | Shughuli nyingi za I/O zinazofanana | Inazuia shughuli ambazo haziwezi kufanywa kuwa za kusawazisha |
| **Kizuizi** | Haiwezi kutumia msimbo unaofungamana na CPU bila kuzuia | GIL katika Python inapunguza usawa wa kweli |
---

## Utendaji wa Mbele
| Mbinu | Maelezo | Athari |
|-----------|-------------|--------|
| **Mainisho** | Ondoa nafasi nyeupe na ufupishe majina tofauti | 20-40% faili ndogo |
| **Kuunganisha** | Changanya faili nyingi katika maombi machache | Maombi machache ya HTTP |
| **Kugawanya msimbo** | Pakia tu msimbo unaohitajika kwa ukurasa wa sasa | Upakiaji wa awali wa haraka |
| **Kupakia kwa uvivu** | Pakia picha na vijenzi vinapohitajika | Utoaji wa haraka wa awali |
| **Mti unaotikisika** | Ondoa msimbo ambao haujatumiwa kutoka kwa vifurushi | Vifurushi vidogo zaidi |
| **Uboreshaji wa picha** | Tumia WebP/AVIF; picha za msikivu; upakiaji wa uvivu | 50-80% picha ndogo |
| **CDN** | Kutumikia mali tuli kutoka kwa seva makali | Muda wa chini wa kusubiri kimataifa |
| **HTTP/2 na HTTP/3** | Multiplexing; ukandamizaji wa kichwa; 0-RTT | Itifaki ya haraka zaidi |
| **Wafanyakazi wa huduma** | Mali ya akiba kwa matumizi ya nje ya mtandao; arifa kwa kushinikiza | Ziara za kurudia haraka |
---

## Uboreshaji wa Kumbukumbu
| Mbinu | Maelezo |
|-----------|-------------|
| **Kuunganisha vitu** | Tumia tena vitu badala ya kuunda vipya |
| **Inatiririsha** | Sindika data katika vipande badala ya kupakia kila kitu kwenye kumbukumbu |
| **Jenereta / viboreshaji** | Thamani ya mavuno moja baada ya nyingine badala ya orodha za majengo |
| **Faili zilizopangwa kwa kumbukumbu** | Fikia faili kubwa bila kuzipakia kabisa |
| **Urekebishaji wa ukusanyaji wa taka** | Rekebisha vigezo vya GC kwa mzigo wako wa kazi |
| **Chaguo la muundo wa data** | Tumia safu badala ya orodha zilizounganishwa kwa eneo la kache; tumia seti kwa majaribio ya uanachama |
---

## Uboreshaji wa Mtandao
| Mbinu | Maelezo |
|-----------|-------------|
| **Mfinyazo** | gzip, brotli kwa majibu ya HTTP |
| **Tumia tena muunganisho** | Viunganisho vya kuweka-hai; HTTP/2 kuzidisha |
| **Omba kuunganishwa** | Changanya simu nyingi za API kuwa moja |
| **Pagination** | Pakia data katika kurasa badala ya zote mara moja |
| **Mfinyazo wakati wa kupumzika** | Finya data katika hifadhidata na kache |
| **Chaguo la itifaki** | gRPC (binary, efficient) vs REST (inayosomeka na binadamu) |
---

## Ufuatiliaji na Tahadhari
| Kipimo | Inachokuambia |
|--------|------------------|
| **P50 / P95 / P99 muda wa kusubiri** | Muda wa kujibu kwa asilimia mbalimbali |
| **Mapitio** | Maombi kwa sekunde |
| **Kiwango cha makosa** | Asilimia ya maombi ambayo hayakufaulu |
| **Utumiaji wa CPU** | Kiasi gani cha uwezo wa usindikaji kinatumika |
| **Matumizi ya kumbukumbu** | matumizi ya RAM; inakaribia mipaka? |
| **Muda wa hoja wa hifadhidata** | Hoja za polepole zinazohitaji uboreshaji |
---

## Muhtasari
Uboreshaji wa utendaji ni mchakato wa kimfumo: pima, tambua kizuizi, rekebisha, pima tena. Mafanikio makubwa zaidi yanatokana na uboreshaji wa algorithmic na kuondoa kazi isiyo ya lazima - sio kutoka kwa uboreshaji mdogo. Uakibishaji, uorodheshaji wa hifadhidata, na upatanisho ni zana zenye nguvu zaidi. Utendaji wa mazingira ya mbele unategemea kupunguza ukubwa wa upakiaji na safari za kwenda na kurudi. Na sheria muhimu zaidi daima ni sawa: usifikiri - wasifu.