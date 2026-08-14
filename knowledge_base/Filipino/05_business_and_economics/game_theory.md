---
# Metadata
title: "Game Theory and Strategic Thinking"
description: "Nash equilibrium, prisoner's dilemma, mechanism design, auctions"
category: "Business and Economics"
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
reviewed_by: "Business & Economics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [game, theory, business-and-economics]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Game Theory at Strategic Thinking
Ang teorya ng laro ay ang matematikal na pag-aaral ng mga madiskarteng pakikipag-ugnayan — mga sitwasyon kung saan ang iyong kinalabasan ay nakasalalay hindi lamang sa kung ano ang iyong ginagawa, ngunit sa kung ano ang ginagawa ng iba. Nalalapat ito sa lahat ng dako: kumpetisyon sa negosyo, relasyon sa internasyonal, mga auction, negosasyon, evolutionary biology, at pang-araw-araw na desisyon tulad ng pagpili ng ruta sa trapiko. Ang pangunahing insight ay ang mga makatwirang aktor sa mga madiskarteng sitwasyon ay hindi lamang nag-o-optimize ng kanilang sariling diskarte - inaasahan nila kung ano ang gagawin ng iba, at ang iba ay ginagawa ang parehong.
---

## Mga Pangunahing Konsepto
### Pangunahing Terminolohiya
| Termino | Kahulugan |
|------|-----------|
| **Laro** | Anumang sitwasyon na may dalawa o higit pang mga gumagawa ng desisyon (mga manlalaro) na ang mga pagpipilian ay nakakaapekto sa mga resulta ng bawat isa |
| **Manlalaro** | Isang gumagawa ng desisyon sa laro |
| **Diskarte** | Isang kumpletong plano ng aksyon para sa bawat sitwasyon na maaaring lumitaw |
| **Kabayaran** | Ang kinalabasan na natatanggap ng isang manlalaro mula sa isang partikular na kumbinasyon ng mga diskarte |
| **Nash equilibrium** | Isang hanay ng mga diskarte kung saan walang manlalaro ang makakapagpabuti ng kanilang kabayaran sa pamamagitan ng unilateral na pagbabago ng kanilang diskarte |
| **Namumuno na diskarte** | Isang diskarte na pinakamahusay anuman ang ginagawa ng ibang mga manlalaro |
| **Zero-sum game** | Ang pakinabang ng isang manlalaro ay eksaktong pagkatalo ng iba |
| **Non-zero-sum game** | Ang mga manlalaro ay maaaring lahat ay makakuha o lahat ay matalo |
| **Cooperative game** | Ang mga manlalaro ay maaaring bumuo ng mga umiiral na kasunduan |
| **Larong hindi kooperatiba** | Walang umiiral na mga kasunduan; bawat manlalaro ay kumikilos sa pansariling interes |
---

## Mga Klasikong Laro
### Prisoner's Dilemma
Arestado ang dalawang suspek. Ang bawat isa ay maaaring makipagtulungan (manatiling tahimik) o magkasala (magkumpisal).
| | B Nakikiisa | B Mga Depekto |
|---|-------------|-----------|
| **A Nakipagtulungan** | A: 1 taon, B: 1 taon | A: 10 taon, B: libre |
| **A Mga Depekto** | A: libre, B: 10 taon | A: 5 taon, B: 5 taon |
| Pananaw | Paglalarawan |
|---------|-------------|
| **Namumuno na diskarte** | Ang depekto ay nangingibabaw para sa parehong mga manlalaro |
| **Nash equilibrium** | Parehong depekto (5 taon bawat isa) |
| **Pareto optimal** | Parehong nagtutulungan (1 taon bawat isa) |
| **Aralin** | Ang mga makatwirang desisyon ng indibidwal ay maaaring humantong sa sama-samang mas masahol na resulta |
### Iba pang Klasikong Laro
| Laro | Paglalarawan | Nash Equilibrium | Aralin |
|------|-------------|----------------|--------|
| **Manok (Hawk-Dove)** | Dalawang driver ang tumungo sa isa't isa; lumihis o dumiretso | Isang swerve, isa dumiretso | Brinkmanship; kredibilidad ng pangako |
| **Stag Hunt** | Manghuli ng stag nang sama-sama (mataas na kabayaran) o manghuli ng liyebre nang mag-isa (mababang bayad) | Parehong stag o parehong liyebre | Koordinasyon; magtiwala |
| **Labanan ng mga Kasarian** | Mas gusto ng dalawang manlalaro ang magkaibang kinalabasan ngunit gustong mag-coordinate | Parehong pumunta sa parehong kaganapan | Maramihang equilibria; kung sino ang unang gumagalaw ay may kalamangan |
| **Ultimatum game** | Naghahati ng pera ang nagmumungkahi; tinatanggap o tinatanggihan ng tumutugon (parehong walang nakuha) | Nag-aalok ang nagmumungkahi ng pinakamababa; tinatanggap ng tagatugon | Tinatanggihan ng mga tao ang mga hindi patas na alok (hindi makatwiran ngunit karaniwan) |
| **Laro ng pampublikong kalakal** | Mag-ambag sa isang shared pool o libreng sakay | Lahat ay libreng sakay | Trahedya ng mga karaniwang tao; kailangan para sa pagpapatupad |
---

## Mga Uri ng Laro
### Ayon sa Timing
| Uri | Paglalarawan | Halimbawa |
|------|-------------|---------|
| **Sabay** | Sabay-sabay na gumagalaw ang mga manlalaro (o hindi nalalaman ang galaw ng iba) | Bato-papel-gunting; mga selyadong bid na auction |
| **Sequential** | Ang mga manlalaro ay gumagalaw nang paisa-isa; mamaya ang mga manlalaro ay nagmamasid sa mga naunang galaw | Chess; mga desisyon sa pagpasok sa merkado |
| **Inulit** | Ang parehong laro ay nilalaro nang maraming beses | Paulit-ulit na problema ng bilanggo; patuloy na kumpetisyon sa negosyo |
### Sa pamamagitan ng Impormasyon
| Uri | Paglalarawan | Halimbawa |
|------|-------------|---------|
| **Perpektong impormasyon** | Alam ng lahat ng manlalaro ang lahat ng nakaraang galaw | Chess; mga pamato |
| **Hindi perpektong impormasyon** | Nakatago ang ilang galaw | Poker; kumpetisyon sa negosyo |
| **Kumpletong impormasyon** | Alam ng lahat ng manlalaro ang lahat ng kabayaran at diskarte | Karamihan sa mga laro sa aklat-aralin |
| **Hindi kumpletong impormasyon** | Ang ilang mga kabayaran o uri ay hindi alam | Mga Auction; negosasyon |
---

## Mga Konsepto ng Solusyon
### Nash Equilibrium
| Aspeto | Paglalarawan |
|--------|--------------|
| **Kahulugan** | Walang manlalaro ang makakapagpabuti ng kanilang kabayaran sa pamamagitan ng pagbabago ng kanilang diskarte nang mag-isa |
| **Paano mahahanap** | Para sa bawat manlalaro, maghanap ng pinakamahusay na tugon sa mga diskarte ng iba; kung saan silang lahat ay nagsalubong ay ang Nash equilibrium |
| **Pag-iral** | Ang bawat may hangganang laro ay may hindi bababa sa isang Nash equilibrium (maaaring sa magkahalong diskarte) |
| **Kakaiba** | Ang mga laro ay maaaring magkaroon ng maramihang Nash equilibria; lumitaw ang mga problema sa koordinasyon |
| **Limitasyon** | Hindi sinasabi sa iyo ng Nash equilibrium kung aling equilibrium ang pipiliin; hindi isinasaalang-alang ang pagiging patas |
### Dominant Strategy Equilibrium
| Hakbang | Paglalarawan |
|------|-------------|
| **1. Tukuyin ang mga estratehiya** | Ilista ang lahat ng magagamit na diskarte para sa bawat manlalaro |
| **2. Maghanap ng mga nangingibabaw na diskarte** | Isang diskarte na pinakamainam anuman ang ginagawa ng iba |
| **3. Kung lahat ng manlalaro ay may isa** | Ang kumbinasyon ay ang nangingibabaw na diskarte ekwilibriyo |
| **4. Kung hindi** | Gumamit ng inuulit na pag-aalis ng mga dominated na diskarte o Nash equilibrium |
### Backward Induction (Sequential Games)
| Hakbang | Paglalarawan |
|------|-------------|
| **1. Iguhit ang puno ng laro** | Mga node = mga punto ng desisyon; sangay = mga aksyon |
| **2. Magsimula sa dulo** | Tukuyin ang pinakamainam na pagpipilian ng huling manlalaro sa bawat terminal node |
| **3. Trabaho nang paurong** | Sa bawat naunang node, piliin ang aksyon na humahantong sa pinakamahusay na kinalabasan |
| **4. Resulta** | Subgame perpektong equilibrium — pinakamainam na diskarte sa bawat punto ng desisyon |
---

## Mga Advanced na Konsepto
### Pinaghalong Istratehiya
| Konsepto | Paglalarawan | Halimbawa |
|---------|-------------|---------|
| **Halong diskarte** | Pag-random sa pagitan ng mga aksyon ayon sa mga probabilidad | Rock-paper-scissors: laruin ang bawat isa na may 1/3 na posibilidad |
| **Bakit randomise?** | Pinipigilan ang mga kalaban na mahulaan ang iyong galaw | Mga sipa ng parusa sa football; mga pagsusuri sa buwis |
| **Halong diskarte Nash equilibrium** | Ang bawat manlalaro ay walang malasakit sa pagitan ng kanilang mga purong diskarte | Hindi maaaring pagsamantalahan ng alinmang manlalaro ang iba pang |
### Paulit-ulit na Laro at Folk Theorem
| Konsepto | Paglalarawan |
|---------|-------------|
| **Naulit na sa wakas** | Ang backward induction ay nagbubukas ng kooperasyon; katulad ng one-shot game | Ang pagtalikod sa huling round ay lumalaganap pabalik |
| **Inulit na walang hanggan** | Ang pakikipagtulungan ay maaaring mapanatili sa pamamagitan ng mga banta ng hinaharap na kaparusahan | Tit-for-tat; mabangis na mga diskarte sa pag-trigger |
| **Folk theorem** | Anumang indibidwal na makatwirang kabayaran ay maaaring maging isang Nash equilibrium sa isang walang katapusan na paulit-ulit na laro | Ang kooperasyon ay posible kung ang hinaharap ay mahalaga
| **Discount factor** | Magkano ang halaga ng mga manlalaro sa hinaharap na mga kabayaran; mas mataas = mas maraming kooperasyon | Ang mga pasyenteng manlalaro ay higit na nagtutulungan |
### Disenyo ng Mekanismo (Reverse Game Theory)
| Konsepto | Paglalarawan |
|---------|-------------|
| **Layunin** | Idisenyo ang mga panuntunan ng isang laro upang makamit ang ninanais na resulta |
| **Mga Application** | Mga Auction; sistema ng pagboto; disenyo ng kontrata; disenyo ng merkado |
| ** Prinsipyo ng paghahayag** | Anumang resulta na makakamit ng anumang mekanismo ay maaaring makamit sa pamamagitan ng isang makatotohanang direktang mekanismo |
| **Halimbawa** | Vickrey auction (second-price sealed-bid) — ang pagbi-bid ng iyong tunay na halaga ay isang nangingibabaw na diskarte |
---

## Mga Application
### Negosyo
| Application | Konsepto ng Teorya ng Laro | Pananaw |
|-------------|--------------------|---------|
| **Kumpetisyon sa presyo** | Dilemma ng bilanggo | Ang mga digmaan sa presyo ay nasaktan sa parehong mga kumpanya; tacit collusion sa paulit-ulit na laro |
| **Pagpasok sa merkado** | Sunod-sunod na laro; pangako | Ang banta ng nanunungkulan na labanan ang pagpasok ay kapani-paniwala lamang kung sila ay namuhunan sa kapasidad |
| **Mga Auction** | Disenyo ng mekanismo | Ang mga auction sa pangalawang presyo ay nakakakuha ng mga tunay na halaga; ang spectrum auction ay nakalikom ng bilyun-bilyon |
| **Negosasyon** | Larong bargaining; Nash ekwilibriyo | Hatiin ang sobra; first-mover advantage sa ultimatum games |
| **Pagsenyas** | Modelo ng edukasyon ni Spence | Ang mga mamahaling signal ay kapani-paniwala dahil hindi kayang bayaran ng mga uri ng mababang kalidad |
### Internasyonal na Relasyon
| Application | Konsepto ng Teorya ng Laro | Pananaw |
|-------------|--------------------|---------|
| **Mga karera ng armas** | Dilemma ng bilanggo | Ang magkabilang panig ay mas mabuting magdis-arma ngunit hindi mapagkakatiwalaan ang isa't isa |
| **Mga digmaang pangkalakalan** | Paulit-ulit na laro | Tit-for-tat: makipagtulungan hanggang sa magkamali ang iba, pagkatapos ay gumanti |
| **Mga kasunduan sa klima** | Pampublikong kalakal na laro | Ang libreng pagsakay ay makatuwiran; kailangan ng mga mekanismo ng pagpapatupad |
| **Pagpigil** | manok; mapagkakatiwalaang pangako | Ang mutually assured destruction ay isang Nash equilibrium |
---

## Buod
Pinag-aaralan ng teorya ng laro ang mga madiskarteng pakikipag-ugnayan kung saan nakadepende ang iyong kinalabasan sa mga aksyon ng iba. Ang Nash equilibrium — kung saan walang manlalaro ang nakikinabang sa pagbabago ng diskarte lamang — ay ang pangunahing konsepto ng solusyon. Ang mga klasikong laro tulad ng dilemma ng bilanggo ay nagpapakita na ang mga makatuwirang indibidwal na desisyon ay maaaring magdulot ng sama-samang masamang resulta. Ang mga sequential na laro ay nalulutas sa pamamagitan ng backward induction. Ang mga paulit-ulit na laro ay maaaring mapanatili ang kooperasyon sa pamamagitan ng banta ng kaparusahan sa hinaharap. Kasama sa mga pinaghalong diskarte ang randomization upang manatiling hindi mahuhulaan. Binabaliktad ng disenyo ng mekanismo ang tanong: sa halip na hulaan ang mga resulta, nagdidisenyo ito ng mga panuntunan upang makamit ang ninanais na mga resulta (tulad ng sa mga auction). Ang mga aplikasyon ay sumasaklaw sa negosyo (pagpepresyo, pagpasok, mga auction), pulitika (pagboto, mga kasunduan), biology (evolutionary stable na estratehiya), at pang-araw-araw na buhay. Ang pangunahing aral ay ang diskarte ay hindi lamang tungkol sa kung ano ang iyong ginagawa - ito ay tungkol sa pag-asa kung ano ang gagawin ng iba, alam na ginagawa nila ang parehong.