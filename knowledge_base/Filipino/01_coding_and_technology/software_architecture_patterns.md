<!--
---
# Metadata
title: "Software Architecture Patterns"
description: "Monolith, microservices, event-driven, DDD, caching, SOLID"
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
tags: [software, architecture, patterns, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Mga Pattern ng Arkitektura ng Software
Ang arkitektura ay ang hanay ng mga istrukturang desisyon tungkol sa kung paano inorganisa ang isang sistema — anong mga bahagi mayroon ito, kung paano sila nakikipag-usap, at kung saan ang mga responsibilidad. Ang magandang arkitektura ay ginagawang madaling maunawaan, baguhin, at sukatin ang isang sistema. Ang masamang arkitektura ay nagpapahirap sa bawat pagbabago. Sinasaklaw ng file na ito ang mga pangunahing pattern, kung kailan gagamitin ang bawat isa, at ang mga trade-off na kasangkot.
---

## Monolith vs Microservices
Ito ang pinakapangunahing desisyon sa arkitektura, at ito ay nagkakahalaga ng pagkuha ng tama.
| Aspeto | Monolith | Mga Microservice |
|--------|----------|----------------|
| **Istruktura** | Isang unit na nade-deploy | Maraming maliliit, independiyenteng na-deploy na mga serbisyo |
| **Data** | Nakabahaging database | Ang bawat serbisyo ay nagmamay-ari ng data nito |
| **Komunikasyon** | In-process na function na mga tawag | Mga tawag sa network (HTTP, gRPC, pagmemensahe) |
| **Pagsusukat** | I-scale ang buong application | I-scale ang mga indibidwal na serbisyo |
| **Deployment** | Single release cycle | Mga independiyenteng deployment |
| **Pagiging kumplikado** | Mas madaling bumuo sa simula | Pagiging kumplikado ng pagpapatakbo (networking, pagsubaybay) |
| **Pinakamahusay Para sa** | Mga maliliit na koponan, mga produktong maagang yugto | Malaking koponan, kumplikadong mga domain, mataas na sukat |
### Kailan Magsisimula sa isang Monolith
Karamihan sa mga application ay dapat magsimula bilang isang monolith. Mas simple itong buuin, subukan, i-deploy, at i-debug. Maaari mong i-extract ang mga serbisyo anumang oras sa ibang pagkakataon kapag mayroon kang mas malinaw na larawan ng mga hangganan ng iyong domain. Ito ay tinatawag minsan na "modular monolith" — isang monolith na may malinis na panloob na mga hangganan na nagpapadali sa pagkuha sa ibang pagkakataon.
### Kailan Dapat Mag-Microservice
Isaalang-alang ang mga microservice kapag:
- Ang mga koponan ay sapat na malaki na ang koordinasyon ay nagiging isang bottleneck.
- Ang iba't ibang bahagi ng system ay may ibang mga kinakailangan sa pag-scale.
- Kailangan mo ng independiyenteng pag-deploy ng mga bahagi.
- Ang iyong domain ay may malinaw na hangganan na konteksto (tingnan ang DDD sa ibaba).
---

## Layered Architecture (N-Tier)
Ang pinakakaraniwang pattern ng arkitektura. Ang code ay isinaayos sa mga layer, bawat isa ay may partikular na responsibilidad.
```
â”Œ─────────────────────────┐
│   Presentation Layer    │  ← UI, controllers, API endpoints
├─────────────────────────┤
│   Application Layer     │  ← Use cases, orchestration
├─────────────────────────┤
│   Domain Layer          │  ← Business logic, entities
├─────────────────────────┤
│   Infrastructure Layer  │  ← Database, external services, file I/O
└─────────────────────────┘
```

| Layer | Pananagutan | Panuntunan |
|-------|----------------|------|
| **Pagtatanghal** | Pangasiwaan ang mga kahilingan ng user/HTTP | Maaari lamang tumawag sa Application layer |
| **Aplikasyon** | I-orkestrate ang mga kaso ng paggamit | Maaaring tumawag sa Domain layer |
| **Domain** | Pangunahing lohika ng negosyo | Hindi dapat umasa sa ibang mga layer |
| **Imprastraktura** | Mga teknikal na alalahanin | Nagpapatupad ng mga interface na tinukoy sa Domain |
**Pangunahing panuntunan**: ang mga dependency ay tumuturo sa loob. Hindi alam ng layer ng Domain ang tungkol sa database o sa web framework.
---

## Arkitekturang Nababatay sa Kaganapan
Ang mga bahagi ay nakikipag-ugnayan sa pamamagitan ng paglabas at pagtugon sa **mga kaganapan** — mga bagay na nangyari.
| Pattern | Paglalarawan |
|---------|-------------|
| **Abiso sa Kaganapan** | Ang Serbisyo A ay naglalabas ng "OrderPlaced"; serbisyo B, C, D react |
| **Pagkuha ng Kaganapan** | I-imbak ang lahat ng mga pagbabago sa estado bilang isang pagkakasunud-sunod ng mga kaganapan (hindi lamang kasalukuyang estado) |
| **CQRS** | Paghiwalayin ang read model (mga query) mula sa write model (commands) |
### Pagkuha ng Kaganapan
Sa halip na iimbak ang "kasalukuyang estado" sa isang database, iimbak ang bawat pagbabago ng estado bilang isang kaganapan:
```
OrderCreated(order_id=123, total=$50)
OrderPaid(order_id=123, payment_id=456)
OrderShipped(order_id=123, tracking=ABC)
```

Mga Benepisyo: kumpletong audit trail, kakayahang muling buuin ang anumang nakaraang estado, na-decoupled na mga mamimili. Mga Hamon: ebolusyon ng schema ng kaganapan, pagiging pare-pareho sa huli, pagiging kumplikado ng pag-debug.
### CQRS (Command Query Responsibility Segregation)
| Gilid | Layunin | Database |
|------|---------|----------|
| **Utos (Isulat)** | Pangasiwaan ang mga mutasyon; ipatupad ang mga panuntunan sa negosyo | Na-optimize para sa pagsusulat (na-normalize) |
| **Query (Basahin)** | Ihatid ang mga kahilingan sa pagbasa | Na-optimize para sa mga nabasa (na-denormalize) |
Ang CQRS ay natural na nagpapares sa Event Sourcing: ang mga kaganapan mula sa bahagi ng pagsusulat ay inaasahang magiging read-optimized na mga view.
---

## Mga Queue ng Mensahe at Mga Broker ng Kaganapan
Kapag ang mga serbisyo ay kailangang makipag-usap nang asynchronous, ang mga pila ng mensahe ay ang backbone.
| Tool | Uri | Pinakamahusay Para sa |
|------|------|----------|
| **Apache Kafka** | Naipamahagi na log ng kaganapan | High-throughput event streaming, event sourcing |
| **RabbitMQ** | Message broker na may routing | Mga pila ng gawain, kumplikadong mga pattern ng pagruruta |
| **AWS SQS** | Pinamamahalaang pila | AWS-native, simpleng queuing |
| **AWS SNS** | Pub/sub notification | Fan-out sa maraming subscriber |
| **Google Pub/Sub** | Pinamamahalaang pub/sub | GCP-native na event streaming |
| **Redis Stream** | Magaan na stream | Simpleng pag-log ng kaganapan, pag-cache ng mga kaso ng paggamit |
### Mga Pattern ng Pagmemensahe
| Pattern | Paglalarawan |
|---------|-------------|
| **Point-to-Point** | Isang producer, isang consumer bawat mensahe |
| **Mag-publish/Mag-subscribe** | Isang producer, maraming subscriber |
| **Kahilingan/Tugon** | Synchronous-style sa async na transportasyon |
| **Dead Letter Queue** | Ang mga mensaheng nabigo sa pagproseso ay pumupunta sa isang hiwalay na pila para sa inspeksyon |
---

## Domain-Driven Design (DDD)
Ang DDD ay isang madiskarteng diskarte sa disenyo ng software na nakasentro sa code sa mga konsepto ng negosyo sa halip na mga teknikal na alalahanin.
### Mga Pangunahing Konsepto
| Konsepto | Paglalarawan |
|---------|-------------|
| **Bounded Context** | Isang hangganan kung saan pare-pareho ang modelo ng domain (hal., "Pag-order", "Pagpapadala", "Pagsingil") |
| **Ubiquitous Language** | Nakabahaging bokabularyo sa pagitan ng mga developer at mga eksperto sa domain |
| **Mga Pinagsama-sama** | Mga grupo ng mga kaugnay na entity na itinuturing bilang isang unit para sa mga pagbabago sa data |
| **Entity** | Mga bagay na may pagkakakilanlan (hal., isang User na may user_id) |
| **Mga Bagay na May Halaga** | Mga bagay na walang pagkakakilanlan; tinukoy ng kanilang mga katangian (hal., Pera, Address) |
| **Mga Kaganapan sa Domain** | Isang bagay na nangyari sa domain (hal., OrderPlaced) |
| **Layer ng Anti-Corruption** | Layer ng pagsasalin sa pagitan ng iyong domain at mga panlabas na system |
### Kapag Tumulong ang DDD
Pinakamahalaga ang DDD kapag kumplikado ang domain ng negosyo — isipin ang e-commerce, logistik, serbisyong pinansyal, pangangalaga sa kalusugan. Kung simple ang iyong domain (isang blog, isang todo app), sobra-sobra ang DDD.
---

## Mga Istratehiya sa Pag-cache
Ang pag-cache ay isa sa mga pinaka-epektibong paraan upang mapabuti ang pagganap, ngunit ipinakikilala nito ang pagiging kumplikado sa paligid ng pagkakapare-pareho.
| Diskarte | Paglalarawan | Trade-off |
|----------|-------------|-----------|
| **Cache-Aside** | Sinusuri muna ng application ang cache; naglo-load mula sa DB sa miss | Simple; tuluyang pagkakapare-pareho |
| **Write-Through** | Sumulat sa cache at DB nang sabay-sabay | Consistent; mas mabagal ang pagsusulat |
| **Isulat-Sa Likod** | Sumulat sa cache; async sumulat sa DB | Mabilis na pagsusulat; panganib ng pagkawala ng data |
| **Read-Through** | Ang cache ay naglo-load mula sa DB sa miss transparently | Mas simple kaysa sa cache-aside |
### Ano ang Cache
| Layer | Ano | Mga tool |
|-------|------|-------|
| **CDN** | Mga static na asset, mga tugon sa API | CloudFront, Cloudflare |
| **Aplikasyon** | Nakalkula ang mga resulta, data ng session | Redis, Memcached |
| **Database** | Mga resulta ng query, madalas na ina-access na mga row | Query cache, materialized view |
Ang **Cache invalidation** ay kilalang mahirap. Mga karaniwang diskarte: TTL (time-to-live), event-driven invalidation (clear cache on data change), at LRU (least recently used) eviction.
---

## Mga Pattern ng Disenyo
### SOLID na Prinsipyo
| Prinsipyo | Ano ang Ibig Sabihin Nito |
|-----------|--------------|
| **S** — Iisang Pananagutan | Ang isang klase ay dapat magkaroon ng isang dahilan upang baguhin ang |
| **O** — Bukas/Sarado | Bukas para sa extension, sarado para sa pagbabago |
| **L** — Liskov Substitution | Ang mga subtype ay dapat na mapalitan para sa kanilang mga batayang uri |
| **I** — Interface Segregation | Maraming partikular na interface > isang pangkalahatang layunin na interface |
| **D** — Dependency Inversion | Depende sa abstractions, hindi concretions |
### Mga Karaniwang Pattern
| Pattern | Layunin | Halimbawa |
|---------|--------|---------|
| **Singleton** | Tiyaking may isang instance lang ang isang klase | Pool ng koneksyon sa database |
| **Pabrika** | Lumikha ng mga bagay nang hindi tinukoy ang eksaktong klase | `UserFactory.create(type="admin")`|
| **Nagmamasid** | Abisuhan ang mga dependent kapag nagbago ang estado | Mga tagapakinig ng kaganapan, pub/sub |
| **Diskarte** | Magpalit ng mga algorithm sa runtime | Diskarte sa Pagbabayad: CreditCard, PayPal, Crypto |
| **Repository** | Abstract na pag-access ng data sa likod ng malinis na interface | `UserRepository.find_by_id(123)`|
| **Dekorador** | Magdagdag ng gawi sa dynamic na paraan | Logging decorator sa paligid ng isang serbisyo |
| **Adapter** | Gawing gumagana ang mga hindi tugmang interface | Legacy API adapter |
---

## Pagpili ng Tamang Arkitektura
Walang pangkalahatang "pinakamahusay" na arkitektura. Ang tamang pagpipilian ay nakasalalay sa:
| Salik | Paboran ang Monolith Kapag... | Paboran ang Microservices Kapag... |
|--------|----------------------|--------------------------------|
| **Laki ng koponan** | < 10 developers | >20 developer, maramihang mga koponan |
| **Pagiging kumplikado ng domain** | Simple o mahusay na nauunawaan | Kumplikado, maraming may hangganan na konteksto |
| **Mga kinakailangan sa sukat** | Uniform scaling pangangailangan | Ang iba't ibang bahagi ay nangangailangan ng iba't ibang sukat |
| **Deployment cadence** | Single release cycle | Kailangan ang mga independiyenteng deployment |
| **Pagkakaiba-iba ng teknolohiya** | Maayos ang isang stack | Iba't ibang serbisyo ang nangangailangan ng iba't ibang teknolohiya |
**Praktikal na payo**: magsimula sa isang modular monolith. I-extract lang ang mga serbisyo kapag mayroon kang malinaw na pangangailangan at malinaw na mga hangganan ng domain. Ang mga napaaga na microservice ay isa sa mga pinakakaraniwang pagkakamali sa arkitektura sa industriya.