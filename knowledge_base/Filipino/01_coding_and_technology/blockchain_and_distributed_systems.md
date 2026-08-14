---
# Metadata
title: "Blockchain and Distributed Systems"
description: "Consensus, smart contracts, DeFi, Byzantine fault tolerance"
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

# Blockchain at Ibinahagi na Sistema
Ang Blockchain ay isang partikular na uri ng distributed system — isang desentralisado, append-only ledger kung saan ang mga talaan (mga bloke) ay iniuugnay ng mga cryptographic na hash. Ang mga distributed system ay ang mas malawak na larangan ng paggawa ng maramihang mga computer na gumagana nang magkasama bilang isa. Ang parehong mga konsepto ay mahalaga para sa pag-unawa sa modernong imprastraktura, mula sa cryptocurrency hanggang sa mga distributed database hanggang sa mga consensus algorithm na nagpapagana ng mga pandaigdigang serbisyo.
---

## Mga Pangunahing Kaalaman sa Distributed Systems
### Bakit Nababahaging Sistema?
| Pagganyak | Paglalarawan |
|-----------|-------------|
| **Scalability** | Magdagdag ng higit pang mga makina upang mahawakan ang higit pang pagkarga |
| **Fault tolerance** | Patuloy na gumagana ang system kahit na nabigo ang ilang makina |
| **Heograpikong pamamahagi** | Paglingkuran ang mga user mula sa mga kalapit na data center |
| **Pagkadalubhasa** | Iba't ibang makina ang humahawak ng iba't ibang gawain |
### Mga Pangunahing Konsepto
| Konsepto | Paglalarawan | Hamon |
|---------|-------------|-----------|
| **Consensus** | Pagkuha ng lahat ng node na sumang-ayon sa isang halaga | Mga partisyon ng network; Mga pagkakamali ng Byzantine |
| **Replikasyon** | Pagkopya ng data sa maraming node | Consistency vs availability |
| **Paghahati (sharding)** | Paghahati ng data sa mga node | Mga hot spot; cross-shard na mga query |
| **Mga modelo ng pagkakapare-pareho** | Mga garantiya tungkol sa kung ano ang nakikita ng iba't ibang mga mambabasa | Ang malakas na pagkakapare-pareho ay mabagal; maaaring mabigla ang mga user sa kalaunan
| **CAP theorem** | Maaari ka lang magkaroon ng 2 sa: Consistency, Availability, Partition tolerance | Sa pagsasagawa, kinakailangan ang pagpapaubaya ng partisyon; piliin ang C o A |
### Ang CAP Theorem
| Pagpipilian | Ano ang Makukuha Mo | Ang Ibinibigay Mo | Halimbawa |
|--------|-------------|----------------|---------|
| **CP** | Consistent + partition-tolerant | Ang ilang mga node ay maaaring hindi magagamit sa panahon ng mga partisyon | HBase, MongoDB, Redis |
| **AP** | Available + partition-tolerant | Maaaring ibalik ng mga nabasa ang lipas na data | Cassandra, DynamoDB, CouchDB |
| **CA** | Consistent + available | Hindi maaaring tiisin ang mga partisyon ng network | Single-node database (hindi tunay na ipinamamahagi) |
---

## Consensus Algorithms
Paano nagkakasundo ang mga distributed node sa estado ng system?
| Algorithm | Uri | Fault Tolerance | Ginamit Sa |
|-----------|------|----------------|---------|
| **Paxos** | Crash fault tolerant | Hanggang f pagkabigo na may 2f+1 node | Google Chubby; pundasyong teorya |
| **Basa** | Crash fault tolerant | Hanggang f pagkabigo na may 2f+1 node | etcd, Consul, TiKV |
| **PBFT** | Byzantine fault tolerant | Hanggang f pagkabigo na may 3f+1 node | Hyperledger Tela |
| **Patunay ng Trabaho** | Byzantine fault tolerant | Depende sa hash power | Bitcoin |
| **Patunay ng Stake** | Byzantine fault tolerant | Depende sa stake | Ethereum 2.0, Cardano |
### Balsa (Pinasimple)
| Tungkulin | Pananagutan |
|------|--------------|
| **Namumuno** | Pinangangasiwaan ang lahat ng mga kahilingan ng kliyente; nagpapadala ng mga log entry sa mga tagasunod |
| **Sumusunod** | Tumutugon sa mga kahilingan ng pinuno; mga boto sa halalan |
| **Kandidato** | Humihiling ng mga boto upang maging pinuno |
1. Magsisimula ang lahat ng node bilang mga tagasunod
2. Kung ang isang tagasunod ay hindi nakarinig mula sa pinuno para sa oras ng halalan, ito ay magiging isang kandidato
3. Humihiling ng mga boto ang mga kandidato; ang may pinakamaraming boto ay nagiging pinuno
4. Ginagaya ng pinuno ang mga log entries sa mga tagasunod
5. Kapag nakumpirma ng mayorya, ang entry ay nakatuon
---

## Blockchain
### Paano Gumagana ang Blockchain
| Bahagi | Paglalarawan |
|-----------|-------------|
| **Harangan** | Isang batch ng mga transaksyon + metadata + hash ng nakaraang block |
| **Hash** | Cryptographic na fingerprint ng mga nilalaman ng block |
| **Kadena** | Tinutukoy ng bawat bloke ang hash ng nakaraang bloke, na lumilikha ng hindi nababagong chain |
| **Consensus** | Sumasang-ayon ang mga kalahok sa network kung aling mga bloke ang idaragdag |
| **Punong merkle** | Puno ng mga hash na nagbubuod sa lahat ng mga transaksyon sa isang bloke |
### Bakit Mahirap Pakialaman ang Blockchain
1. Ang bawat bloke ay naglalaman ng hash ng nakaraang bloke
2. Ang pagpapalit ng anumang transaksyon ay nagbabago sa hash ng block
3. Ang binagong hash ay sumisira sa kadena — lahat ng kasunod na mga bloke ay nagiging hindi wasto
4. Kakailanganin ng isang attacker na muling minahan ang lahat ng kasunod na block AT kontrolin ang >50% ng network
### Mga Uri ng Blockchain
| Uri | Access | Validator | Halimbawa |
|------|--------|-----------|---------|
| **Pampubliko (walang pahintulot)** | Kahit sino ay maaaring magbasa at magsulat | Buksan ang pinagkasunduan (PoW, PoS) | Bitcoin, Ethereum |
| **Pribado (pinahintulutan)** | Pinaghihigpitang pag-access | Mga kilalang validator | Hyperledger, Corda |
| **Consortium** | Pinamamahalaan ng isang grupo ng mga organisasyon | Mga napiling validator | R3 Corda para sa pagbabangko |
### Mga Matalinong Kontrata
Self-executing code na nakaimbak sa blockchain na tumatakbo kapag natugunan ang mga paunang natukoy na kundisyon.
| Platform | Wika | Kapansin-pansing Tampok |
|----------|----------|-----------------|
| **Ethereum** | Solidity, Vyper | Pinakamalaking smart contract ecosystem |
| **Solana** | kalawang, C | Mataas na throughput; mababang bayad |
| **Cardano** | Haskell (Plutus) | Peer-reviewed; pormal na pagpapatunay |
| **Hyperledger** | Pumunta, Java, JavaScript | Enterprise; pinahintulutan |
---

## Cryptocurrency
| Pera | Pinagkasunduan | Supply | Pangunahing Paggamit |
|----------|-----------|--------|-------------|
| **Bitcoin** | Katibayan ng Trabaho | 21 milyon (nakalimitahan) | Tindahan ng halaga; digital na ginto |
| **Ethereum** | Katibayan ng Stake | Walang hard cap | Mga matalinong kontrata; DeFi; Mga NFT |
| **Solana** | Patunay ng Stake + Patunay ng Kasaysayan | Walang hard cap | Mataas na bilis ng mga transaksyon |
| **Cardano** | Katibayan ng Stake (Ouroboros) | 45 bilyon (nakalimitahan) | diskarte sa akademiko; pagpapanatili |
---

## Mga Ibinahagi na Database
| Database | Arkitektura | Consistency | Pinakamahusay Para sa |
|----------|-------------|-------------|----------|
| **Cassandra** | Malapad na hanay; peer-to-peer | Tunable (sa wakas sa korum) | Mataas na write throughput; serye ng oras |
| **MongoDB** | Dokumento; replica set | Sa wakas (na may opsyon sa pagkakapare-pareho ng sanhi) | Flexible na schema; mabilis na pag-unlad |
| **CockroachDB** | Ibinahagi ang SQL; Pinagkasunduan ng balsa | Malakas | Ibinahagi ang SQL; pandaigdigang deployment |
| **TiDB** | Ibinahagi ang SQL; Balsa (sa pamamagitan ng TiKV) | Malakas | MySQL-compatible; pahalang na pag-scale |
| **DynamoDB** | Key-value; pinamamahalaan | Sa wakas (o malakas na may pare-parehong pagbabasa) | Walang server; AWS-integrated |
| **Spanner** | Ibinahagi ang SQL; Paxos | Malakas | Google Cloud; pandaigdigang pagkakapare-pareho |
---

## Mga Pattern ng Distributed System
| Pattern | Paglalarawan | Use Case |
|---------|-------------|----------|
| **Paghalal ng pinuno** | Pumili ng isang node upang i-coordinate | Pinuno ng balsa; ZooKeeper |
| **Replikasyon** | Kopyahin ang data para sa redundancy at basahin ang scaling | Mga replika ng database; CDN |
| **Sharding** | Partition data ayon sa key range o hash | Mga malalaking database |
| **MapReduce** | Hatiin ang pagkalkula sa mga node; pinagsama-samang mga resulta | Malaking pagpoproseso ng data |
| **Protocol ng tsismis** | Pana-panahong ibinabahagi ng mga node ang estado sa mga random na kapantay | Cluster membership; pagtukoy ng kabiguan |
| **Two-phase commit** | Mag-coordinate ng mga transaksyon sa maraming node | Mga naipamahagi na database |
| **Saga pattern** | Serye ng mga lokal na transaksyon na may bayad na mga aksyon | Mga transaksyon sa microservice |
| **Circuit breaker** | Itigil ang pagtawag sa isang bagsak na serbisyo; mabilis mabigo | Katatagan; maiwasan ang mga pagkabigo ng cascading |
---

## Mga Hamon sa Mga Distributed System
| Hamon | Paglalarawan | Pagbabawas |
|-----------|-------------|------------|
| **Mga partisyon sa network** | Hindi maaaring makipag-ugnayan ang mga node | CAP trade-off; subukan muli gamit ang backoff |
| **Clock skew** | Ang iba't ibang mga node ay may iba't ibang orasan | Gumamit ng mga lohikal na orasan; NTP; iwasang umasa sa oras ng wall-clock |
| **Byzantine faults** | Mga node na nagsisinungaling o kumikilos nang arbitraryo | pinagkasunduan ng BFT; blockchain |
| **Nahati ang utak** | Dalawang node ang parehong iniisip na sila ang pinuno | Bakod; mga desisyong nakabatay sa korum |
| **Mga pagkabigo sa pag-cascade** | Ang isang pagkabigo ay nag-trigger sa iba | Mga circuit breaker; mga bulkhead; magandang pagkasira |
| **Pagkakapare-pareho ng data** | Pagpapanatiling naka-sync ang mga replika | Mga modelo ng pagkakapare-pareho; paglutas ng salungatan |
---

## Buod
Ang mga distributed system ay kung paano sumusukat ang modernong software, nakakaligtas sa mga pagkabigo, at nagsisilbi sa mga user sa buong mundo. Tinitiyak ng mga algorithm ng pinagkasunduan (Raft, Paxos) na sumasang-ayon ang mga node. Ang mga blockchain ay nagdaragdag ng cryptographic na pag-verify at desentralisasyon upang lumikha ng mga hindi mapagkakatiwalaang ledger. Ang mga distributed database (Cassandra, CockroachDB, DynamoDB) ay humahawak ng data sa sukat. Ang pangunahing trade-off — nakuha ng CAP theorem — ay nasa pagitan ng consistency at availability kapag ang network ay hindi mapagkakatiwalaan. Ang pag-unawa sa mga konseptong ito ay mahalaga para sa pagbuo ng mga system na gumagana sa sukat ng internet.