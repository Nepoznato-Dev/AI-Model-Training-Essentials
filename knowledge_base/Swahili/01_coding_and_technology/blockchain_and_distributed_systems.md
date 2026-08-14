---
# Metadata
title: "Blockchain and Distributed Systems"
description: "Consensus, smart contracts, DeFi, Byzantine fault tolerance"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [blockchain, distributed, systems, coding-and-technology]
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
# Blockchain na Mifumo Iliyosambazwa
Blockchain ni aina mahususi ya mfumo unaosambazwa - leja iliyogatuliwa, ya nyongeza pekee ambapo rekodi (vizuizi) huunganishwa kwa heshi za kriptografia. Mifumo iliyosambazwa ni uwanja mpana wa kufanya kompyuta nyingi kufanya kazi pamoja kama moja. Dhana zote mbili ni muhimu kwa kuelewa miundombinu ya kisasa, kutoka sarafu ya cryptocurrency hadi hifadhidata iliyosambazwa hadi algoriti za makubaliano zinazotumia huduma za kimataifa.
---

## Misingi ya Mifumo Iliyosambazwa
### Kwa nini Mifumo Imesambazwa?
| Kuhamasisha | Maelezo |
|-----------|-------------|
| **Scalability** | Ongeza mashine zaidi ili kushughulikia mzigo zaidi |
| **Uvumilivu wa makosa** | Mfumo unaendelea kufanya kazi hata kama baadhi ya mashine zitashindwa |
| **Usambazaji wa kijiografia** | Huhudumia watumiaji kutoka vituo vya data vilivyo karibu |
| **Utaalam** | Mashine tofauti hushughulikia kazi tofauti |
### Dhana Muhimu
| Dhana | Maelezo | Changamoto |
|---------|-------------|-----------|
| **Makubaliano** | Kupata nodi zote kukubaliana juu ya thamani | Sehemu za mtandao; Makosa ya Byzantine |
| **Replication** | Kunakili data kwenye nodi nyingi | Uthabiti dhidi ya upatikanaji |
| **Kugawanya (kugawa)** | Kugawanya data kwenye nodi | Sehemu za moto; maswali mbalimbali |
| **Miundo ya uthabiti** | Dhamana kuhusu kile ambacho wasomaji tofauti huona | Uthabiti wenye nguvu ni polepole; uthabiti wa mwisho unaweza kushangaza watumiaji |
| **nadharia ya CAP** | Unaweza kuwa na 2 pekee kati ya: Uthabiti, Upatikanaji, Ustahimilivu wa Kugawa | Katika mazoezi, uvumilivu wa kizigeu unahitajika; chagua C au A |
### Nadharia ya CAP
| Chaguo | Unachopata | Unaacha Nini | Mfano |
|--------|-------------|----------------|---------|
| **CP** | Thabiti + inayostahimili kizigeu | Baadhi ya nodi huenda zisipatikane wakati wa kugawa | HBase, MongoDB, Redis |
| **AP** | Inapatikana + inayostahimili sehemu | Usomaji unaweza kurudisha data ya zamani | Cassandra, DynamoDB, CouchDB |
| **CA** | Sambamba + inapatikana | Haiwezi kuvumilia sehemu za mtandao | Hifadhidata za nodi moja (hazijasambazwa kikweli) |
---

## Kanuni za Makubaliano
Je! nodi zilizosambazwa zinakubalianaje juu ya hali ya mfumo?
| Algorithm | Andika | Uvumilivu wa Makosa | Inatumika Katika |
|-----------|------|----------------|----------|
| **Paxos** | Inastahimili makosa ya ajali | Hadi kushindwa kwa f kwa nodi 2f+1 | Google Chubby; nadharia ya msingi |
| **Rati** | Inastahimili makosa ya ajali | Hadi kushindwa kwa f kwa nodi 2f+1 | etcd, Balozi, TiKV |
| **PBFT** | Uvumilivu wa makosa wa Byzantine | Hadi kufeli kwa nodi za 3f+1 | Kitambaa cha Hyperledger |
| **Uthibitisho wa Kazi** | Uvumilivu wa makosa wa Byzantine | Inategemea nguvu ya hashi | Bitcoin |
| **Ushahidi wa Mdau** | Uvumilivu wa makosa wa Byzantine | Inategemea dau | Ethereum 2.0, Cardano |
### Rati (Iliyorahisishwa)
| Jukumu | Wajibu |
|------|---------------|
| **Kiongozi** | Hushughulikia maombi yote ya mteja; hutuma maingizo ya kumbukumbu kwa wafuasi |
| **Mfuasi** | Hujibu maombi ya kiongozi; kura katika uchaguzi |
| **Mgombea** | Anaomba kura ili kuwa kiongozi |
1. Nodi zote huanza kama wafuasi
2. Ikiwa mfuasi hatasikia kutoka kwa kiongozi kwa muda wa kuisha kwa uchaguzi, anakuwa mgombea
3. Wagombea wanaomba kura; mwenye kura nyingi anakuwa kiongozi
4. Kiongozi anaiga maingizo ya kumbukumbu kwa wafuasi
5. Wakati wengi wanathibitisha, kuingia kunafanywa
---

## Blockchain
### Jinsi Blockchain Inafanya kazi
| Sehemu | Maelezo |
|-----------|-------------|
| **Zuia** | Kundi la miamala + metadata + heshi ya kizuizi kilichotangulia |
| **Hashi** | Alama za vidole za siri za yaliyomo kwenye kizuizi |
| **Msururu** | Kila kizuizi kinarejelea heshi ya block iliyopita, na kuunda msururu usiobadilika |
| **Makubaliano** | Washiriki wa mtandao wanakubaliana ni vizuizi vipi vya kuongeza |
| **Mti wa Merkle** | Mti wa heshi muhtasari wa shughuli zote katika block |
### Kwa Nini Blockchain Ni Ngumu Kuingilia
1. Kila kizuizi kina heshi ya kizuizi kilichotangulia
2. Kubadilisha muamala wowote hubadilisha heshi ya kizuizi
3. Hashi iliyobadilishwa huvunja mnyororo - vizuizi vyote vinavyofuata huwa batili
4. Mshambulizi atahitaji kuchimba upya vitalu vyote vinavyofuata NA kudhibiti >50% ya mtandao.
### Aina za Blockchains
| Andika | Ufikiaji | Kithibitishaji | Mfano |
|------|--------|----------------------|
| **Hadharani (isiyo na ruhusa)** | Mtu yeyote anaweza kusoma na kuandika | Makubaliano ya wazi (PoW, PoS) | Bitcoin, Ethereum |
| **Binafsi (imeruhusiwa)** | Ufikiaji wenye vikwazo | Wathibitishaji wanaojulikana | Hyperledger, Corda |
| **Muungano** | Inatawaliwa na kundi la mashirika | Vithibitishaji vilivyochaguliwa | R3 Corda kwa ajili ya benki |
### Mikataba Mahiri
Nambari ya kutekeleza yenyewe iliyohifadhiwa kwenye blockchain ambayo hutumika wakati hali zilizoamuliwa mapema zinatimizwa.
| Jukwaa | Lugha | Kipengele Mashuhuri |
|----------|----------|-----------------|
| **Ethereum** | Mshikamano, Vyper | Mfumo mkubwa wa ikolojia wa mkataba mahiri |
| **Solana** | Kutu, C | Uzalishaji wa juu; ada ya chini |
| **Cardano** | Haskell (Plutus) | Imekaguliwa na rika; uthibitishaji rasmi |
| **Hyperledger** | Go, Java, JavaScript | Biashara; imeruhusiwa |
---

## Cryptocurrency
| Sarafu | Makubaliano | Ugavi | Matumizi ya Msingi |
|----------|--------------------|-------------|
| **Bitcoin** | Uthibitisho wa Kazi | Milioni 21 (iliyopunguzwa) | Hifadhi ya thamani; dhahabu ya dijitali |
| **Ethereum** | Ushahidi wa Dau | Hakuna kofia ngumu | Mikataba ya busara; DeFi; NFTs |
| **Solana** | Uthibitisho wa Hisa + Uthibitisho wa Historia | Hakuna kofia ngumu | Shughuli za kasi ya juu |
| **Cardano** | Uthibitisho wa Hisa (Ouroboros) | Bilioni 45 (zilizopunguzwa) | Mbinu ya kitaaluma; uendelevu |
---

## Hifadhidata Zilizosambazwa
| Hifadhidata | Usanifu | Uthabiti | Bora Kwa |
|----------|--------------------------|----------|
| **Cassandra** | Safu wima pana; rika-kwa-rika | Tunaweza (hatimaye kwa akidi) | Kiwango cha juu cha maandishi; mfululizo wa saa |
| **MongoDB** | Hati; replica seti | Hatimaye (na chaguo la uthabiti wa sababu) | Ratiba inayobadilika; maendeleo ya haraka |
| **CockroachDB** | SQL iliyosambazwa; Makubaliano ya raft | Nguvu | SQL iliyosambazwa; kupelekwa kimataifa |
| **TiDB** | SQL iliyosambazwa; Raft (kupitia TiKV) | Nguvu | MySQL-sambamba; kuongeza mlalo |
| **DynamoDB** | Muhimu-thamani; kusimamiwa | Hatimaye (au nguvu na usomaji thabiti) | Bila seva; AWS-imeunganishwa |
| **Spanner** | SQL iliyosambazwa; Paks | Nguvu | Wingu la Google; uthabiti wa kimataifa |
---

## Mifumo ya Mfumo Iliyosambazwa
| Muundo | Maelezo | Tumia Kesi |
|---------|-------------|----------|
| **Uchaguzi wa kiongozi** | Chagua nodi moja ya kuratibu | Kiongozi wa raft; Mlinzi wa Zoo |
| **Replication** | Nakili data ya kupunguzwa kazi na usome kuongeza | Nakala za hifadhidata; CDN |
| **Kushiriki** | Data ya kugawanya kulingana na safu muhimu au heshi | Hifadhidata kubwa |
| **RamaniPunguza** | Gawanya hesabu kwenye nodi; matokeo ya jumla | Usindikaji mkubwa wa data |
| **Itifaki ya porojo** | Nodi mara kwa mara hushiriki hali na wenzao nasibu | Uanachama wa nguzo; utambuzi wa kushindwa |
| **Ahadi ya awamu mbili** | Kuratibu shughuli katika nodi nyingi | Hifadhidata zilizosambazwa |
| **Muundo wa Saga** | Msururu wa miamala ya ndani yenye vitendo vya kufidia | Miamala ya huduma ndogo |
| **Kivunja mzunguko** | Acha kupiga huduma iliyoshindwa; kushindwa haraka | Ustahimilivu; kuzuia kushindwa kwa kasi |
---

## Changamoto katika Mifumo Inayosambazwa
| Changamoto | Maelezo | Kupunguza |
|-----------|---------------------------|
| **Sehemu za mtandao** | Nodi haziwezi kuwasiliana | biashara ya CAP; jaribu tena na backoff |
| **Kipindi cha saa** | Nodi tofauti zina saa tofauti | Tumia saa za mantiki; NTP; epuka kutegemea saa ya ukutani |
| **Makosa ya Byzantine** | Nodi zinazodanganya au kutenda kiholela | Makubaliano ya BFT; blockchain |
| **Mgawanyiko wa ubongo** | Vifundo viwili vyote vinafikiri wao ni kiongozi | Uzio; maamuzi kulingana na akidi |
| **Kushindwa kwa kushindwa** | Kushindwa moja huchochea wengine | Wavunjaji wa mzunguko; bulkheads; udhalilishaji wa neema |
| **Uwiano wa data** | Kuweka nakala katika kusawazisha | Mifano ya uthabiti; utatuzi wa migogoro |
---

## Muhtasari
Mifumo iliyosambazwa ni jinsi programu ya kisasa inavyosawazisha, kustahimili kushindwa, na kuwahudumia watumiaji duniani kote. Algorithms ya makubaliano (Raft, Paxos) huhakikisha nodi zinakubali. Blockchains huongeza uthibitishaji wa siri na ugatuaji ili kuunda leja zisizoaminika. Hifadhidata zilizosambazwa (Cassandra, CockroachDB, DynamoDB) hushughulikia data kwa kiwango. Biashara ya kimsingi - iliyonaswa na nadharia ya CAP - ni kati ya uthabiti na upatikanaji wakati mtandao hauwezi kutegemewa. Kuelewa dhana hizi ni muhimu kwa kujenga mifumo inayofanya kazi kwa kiwango cha mtandao.