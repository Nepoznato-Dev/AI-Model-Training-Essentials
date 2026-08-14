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

# Pag-optimize ng Pagganap
Ang pag-optimize ng pagganap ay ang kasanayan sa paggawa ng software nang mas mabilis — pagbabawas ng mga oras ng pagtugon, pagtaas ng throughput, pagpapababa ng paggamit ng memorya, at pag-aalis ng mga bottleneck. Ito ay isa sa mga pinaka-maimpluwensyang kasanayan na maaaring taglayin ng isang developer, dahil ang mabagal na software ay nawawalan ng mga user, nag-aaksaya ng mga mapagkukunan, at nakakadismaya sa lahat. Ngunit isa rin ito sa pinakakaraniwang ginagawang mali, kung saan ang mga developer ay nag-optimize ng mga maling bagay batay sa intuwisyon sa halip na ebidensya.
---

## Ang Gintong Panuntunan
> **Sukatin muna, i-optimize ang pangalawa.** Huwag kailanman mag-optimize batay sa mga pagpapalagay. I-profile ang code, hanapin ang aktwal na bottleneck, at ayusin iyon.
| Anti-pattern | Bakit Masama |
|-------------|-------------|
| **Napaaga ang pag-optimize** | Gumugugol ng oras sa pagpapabilis ng code na hindi mabagal |
| **Pag-optimize nang walang pagsukat** | Pag-aayos ng maling bottleneck; walang paraan upang i-verify ang pagpapabuti |
| **Isinasakripisyo ang pagiging madaling mabasa para sa bilis** | Ang hindi nababasang code ay nagkakahalaga ng higit sa performance gain |
| **Ini-cache ang lahat** | Stale data, memory bloat, kumplikado |
---

## Pag-profile
Bago mo mapabilis ang isang bagay, kailangan mong malaman *kung saan* ang oras ay ginugugol.
| Uri ng Tool | Ang Sinusukat Nito | Mga halimbawa |
|-----------|----------------|----------|
| **CPU profiler** | Aling mga function ang kumukonsumo ng pinakamaraming oras ng CPU | cProfile (Python), perf (Linux), Chrome DevTools (JS) |
| **Memory profiler** | Paglalaan ng memorya at paglabas | tracemalloc (Python), Valgrind, heaptrack |
| **I/O profiler** | Mga bottleneck ng I/O ng disk at network | iotop, strace, Wireshark |
| **APM (Pagsubaybay sa Pagganap ng Application)** | End-to-end na timing ng kahilingan | Bagong Relic, Datadog, Jaeger |
| **Browser DevTools** | Frontend rendering, JavaScript execution, network | Chrome DevTools, Firefox Profiler |
### Daloy ng Trabaho sa Pag-profile
| Hakbang | Paglalarawan |
|------|-------------|
| 1. Tukuyin ang mabagal na operasyon | Ang mga gumagamit ay nag-uulat ng mabagal na pag-load ng pahina; ang pagsubaybay ay nagpapakita ng mataas na latency |
| 2. I-profile ang buong landas | Hanapin kung aling bahagi ang tumatagal ng pinakamaraming oras |
| 3. Mag-drill down | I-profile ang partikular na bahagi na iyon upang mahanap ang mainit na function |
| 4. Ayusin ang bottleneck | Ilapat ang naaangkop na pag-optimize |
| 5. Sukatin muli | I-verify ang pagpapabuti; suriin para sa mga regression |
---

## Algorithmic Optimization
Ang pinakamalaking tagumpay sa pagganap ay nagmumula sa pagpili ng mas mahuhusay na algorithm, hindi mula sa mga micro-optimization.
| Baguhin | Pagpapabuti |
|--------|-------------|
| Linear na paghahanap O(n) → Hash table lookup O(1) | 100x+ para sa malalaking dataset |
| Nested loop O(n²) → Pagbukud-bukurin + binary na paghahanap O(n log n) | Mga order ng magnitude para sa malaking n |
| Paulit-ulit na pagkalkula → Memoisation / caching | Tinatanggal ang labis na trabaho |
| String concatenation sa isang loop → Builder / join | Iniiwasan ang pagkopya ng quadratic string |
| Unsorted data → Sorted data gamit ang binary search | O(log n) sa halip na O(n) bawat lookup |
---

## Mga Istratehiya sa Pag-cache
Ang pag-cache ay nag-iimbak ng mga resulta ng pagkalkula kaya hindi na kailangang muling kalkulahin ang mga ito.
| Uri ng Cache | Lokasyon | Bilis | Habambuhay |
|-----------|----------|-------|----------|
| **CPU cache** | L1/L2/L3 | ~1 ns | Awtomatikong |
| **In-memory** | Application RAM (dict, HashMap) | ~100 ns | Hanggang sa maalis o mapaalis |
| **Ibinahagi ang cache** | Redis, Memcached | ~1 ms | Nako-configure ang TTL |
| **CDN** | Mga Edge server sa buong mundo | ~10-50 ms | Nako-configure ang TTL |
| **Cache ng browser** | Browser ng user | ~1 ms | Mga header ng HTTP cache |
| **Cache ng query sa database** | Database o ORM level | ~1-10 ms | Hanggang sa magbago ang data |
### Mga Pattern ng Caching
| Pattern | Paglalarawan | Kailan Gagamitin |
|---------|-------------|-------------|
| **Cache-side** | Sinusuri ng application ang cache; naglo-load mula sa DB sa miss; mga tindahan sa cache | Pinaka-karaniwan; simple |
| **Write-through** | Sumulat sa cache at DB nang sabay-sabay | Kapag nagbabasa >> nagsusulat; mahalaga ang pagkakapare-pareho |
| **Isulat-sa likod** | Sumulat sa cache; asynchronous na sumulat sa DB | Mataas na write throughput; ilang panganib sa pagkawala ng data |
| **TTL (Oras para Mabuhay)** | Mag-e-expire ang mga entry sa cache pagkatapos ng isang takdang oras | Kapag pana-panahong nagbabago ang data |
| **Invalidation** | Tahasang alisin ang mga lipas na entry sa cache | Kapag alam mo nang eksakto kung kailan nagbabago ang data |
### Cache Invalidation
Ang dalawang pinakamahirap na problema sa computer science: cache invalidation, pagbibigay ng pangalan sa mga bagay, at off-by-one na mga error.
| Diskarte | Paglalarawan |
|----------|-------------|
| **Batay sa TTL** | Mag-e-expire ang mga entry pagkatapos ng N segundo; simple ngunit maaaring maghatid ng lipas na data |
| **Batay sa kaganapan** | Magpapawalang-bisa kapag nagbago ang data; mas kumplikado ngunit tumpak |
| **Batay sa bersyon** | Magsama ng numero ng bersyon; pagtaas sa mga pagbabago |
| **Batay sa tag** | Tag kaugnay na mga entry sa cache; ipawalang-bisa ang lahat ng mga entry na may tag |
---

## Pag-optimize ng Database
Ang mga database ay madalas na pinakamalaking bottleneck sa mga web application.
| Teknik | Paglalarawan | Epekto |
|-----------|-------------|--------|
| **Pag-i-index** | Magdagdag ng mga index sa mga column na ginamit sa WHERE, JOIN, ORDER BY | 10-1000x mas mabilis na mga query |
| **Pag-optimize ng query** | Iwasan ang SELECT *; gamitin ang EXPLAIN upang suriin ang mga query | Bawasan ang I/O |
| **Connection pooling** | Muling gumamit ng mga koneksyon sa database sa halip na lumikha ng mga bago | Tanggalin ang koneksyon sa itaas |
| **Magbasa ng mga replika** | I-ruta ang mga query sa pagbasa sa mga replica na database | Ipamahagi ang read load |
| **Paghahati** | Hatiin ang malalaking talahanayan sa mas maliliit na partisyon | Mas mabilis na mga query sa malalaking dataset |
| **Denormalisasyon** | Magdagdag ng kalabisan data upang maiwasan ang mga pagsali | Mas mabilis na pagbabasa; mas mabagal ang pagsusulat |
| **Materialised view** | Pre-computed na mga resulta ng query | Mga instant na kumplikadong query |
| **N+1 prevention** | Gumamit ng mga JOIN, sabik na naglo-load, o mga batch na query | Tanggalin ang libu-libong query |
---

## Concurrency at Paralelismo
| Konsepto | Paglalarawan | Kailan Gagamitin |
|---------|-------------|-------------|
| **Threading** | Maramihang mga thread sa loob ng iisang proseso | I/O-bound na mga gawain (network, disk) |
| **Multiprocessing** | Maramihang mga proseso (bypasses GIL sa Python) | Mga gawaing nakatali sa CPU |
| **Async/naghihintay** | Multitasking ng kooperatiba; solong thread | High-concurrency na I/O (mga web server) |
| **GPU computing** | Libu-libong parallel cores | Mga operasyon ng matrix; pagproseso ng imahe; ML |
### Async vs Threading
| Aspeto | Async/Await | Pag-thread |
|--------|------------|-----------|
| **Modelo** | Kooperatiba (kontrol sa pagbubunga ng mga gawain) | Preemptive (pinapalitan ng OS ang mga thread) |
| **Overhead** | Napakababa (walang paglipat ng konteksto) | Mas mataas (paggawa ng thread, paglipat ng konteksto) |
| **Pagiging kumplikado** | Mas simpleng pangangatwiran (iisang thread) | Kondisyon ng lahi, deadlock, lock |
| **Pinakamahusay para sa** | Maraming kasabay na I/O operations | Pag-block ng mga operasyon na hindi maaaring gawing async |
| **Limitasyon** | Hindi magagamit ang CPU-bound na code nang hindi bina-block ang | Nililimitahan ng GIL sa Python ang totoong paralelismo |
---

## Pagganap ng Frontend
| Teknik | Paglalarawan | Epekto |
|-----------|-------------|--------|
| **Minification** | Alisin ang whitespace at paikliin ang mga variable na pangalan | 20-40% mas maliliit na file |
| **Bundling** | Pagsamahin ang maramihang mga file sa mas kaunting mga kahilingan | Mas kaunting mga kahilingan sa HTTP |
| **Paghahati ng code** | I-load lamang ang code na kailangan para sa kasalukuyang page | Mas mabilis na paunang pagkarga |
| **Lazy loading** | Mag-load ng mga larawan at bahagi kapag kailangan ang mga ito | Mas mabilis na paunang pag-render |
| **Pag-alog ng puno** | Alisin ang hindi nagamit na code mula sa mga bundle | Mas maliliit na bundle |
| **Pag-optimize ng larawan** | Gumamit ng WebP/AVIF; tumutugon na mga larawan; tamad na naglo-load | 50-80% mas maliliit na larawan |
| **CDN** | Maghatid ng mga static na asset mula sa mga edge server | Mas mababang latency sa buong mundo |
| **HTTP/2 at HTTP/3** | Multiplexing; compression ng header; 0-RTT | Mas mabilis na protocol overhead |
| **Mga manggagawa sa serbisyo** | Mga asset ng cache para sa offline na paggamit; push notification | Mas mabilis na umuulit na pagbisita |
---

## Pag-optimize ng Memory
| Teknik | Paglalarawan |
|-----------|-------------|
| **Pagsasama-sama ng bagay** | Gumamit muli ng mga bagay sa halip na lumikha ng mga bago |
| **Pag-stream** | Iproseso ang data sa mga tipak sa halip na i-load ang lahat sa memorya |
| **Mga Generator / iterator** | Magbigay ng mga halaga nang paisa-isa sa halip na bumuo ng mga listahan |
| **Mga file na naka-memorya** | I-access ang malalaking file nang hindi ganap na nilo-load ang mga ito |
| **Pag-tune ng koleksyon ng basura** | Isaayos ang mga parameter ng GC para sa iyong workload |
| **Pagpipilian sa istruktura ng data** | Gumamit ng mga array sa halip na mga naka-link na listahan para sa cache locality; gumamit ng mga set para sa pagsubok ng membership |
---

## Network Optimization
| Teknik | Paglalarawan |
|-----------|-------------|
| **Compression** | gzip, brotli para sa mga tugon sa HTTP |
| **Muling paggamit ng koneksyon** | Manatiling buhay na mga koneksyon; HTTP/2 multiplexing |
| **Humiling ng batching** | Pagsamahin ang maramihang mga tawag sa API sa isang |
| **Pagination** | Mag-load ng data sa mga page sa halip na sabay-sabay |
| **Pag-compress sa pahinga** | I-compress ang data sa mga database at cache |
| **Pagpipilian sa protocol** | gRPC (binary, efficient) vs REST (nababasa ng tao) |
---

## Pagsubaybay at Pag-alerto
| Sukatan | Ang Sinasabi Nito sa Iyo |
|--------|------------------|
| **P50 / P95 / P99 latency** | Oras ng pagtugon sa iba't ibang percentile |
| ** Throughput** | Mga kahilingan sa bawat segundo |
| **Rate ng error** | Porsiyento ng mga nabigong kahilingan |
| **Paggamit ng CPU** | Gaano karaming kapasidad sa pagpoproseso ang ginagamit |
| **Paggamit ng memory** | pagkonsumo ng RAM; lumalapit sa limitasyon? |
| **Tagal ng query sa database** | Mabagal na mga query na nangangailangan ng pag-optimize |
---

## Buod
Ang pag-optimize ng pagganap ay isang sistematikong proseso: sukatin, tukuyin ang bottleneck, ayusin ito, sukatin muli. Ang pinakamalaking panalo ay nagmumula sa mga algorithmic na pagpapabuti at pag-aalis ng hindi kinakailangang gawain — hindi mula sa mga micro-optimization. Ang pag-cache, database indexing, at concurrency ay ang pinakamakapangyarihang tool. Ang pagganap ng frontend ay nakasalalay sa pagliit ng laki ng kargamento at mga round trip. At ang pinakamahalagang tuntunin ay palaging pareho: huwag hulaan — profile.