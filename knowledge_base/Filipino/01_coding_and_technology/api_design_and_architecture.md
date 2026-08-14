---
# Metadata
title: "API Design and Architecture"
description: "REST, GraphQL, gRPC, versioning, auth, API gateways"
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
tags: [api, design, architecture, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Disenyo at Arkitektura ng API
Ang isang API (Application Programming Interface) ay kung paano nakikipag-usap ang mga bahagi ng software sa isa't isa. Ang isang mahusay na dinisenyo na API ay madaling maunawaan, pare-pareho, at kasiyahang magtrabaho kasama. Ang isang hindi maganda ang disenyo ay nagdudulot ng pagkalito, mga bug, at pagkabigo. Sinasaklaw ng file na ito ang mga prinsipyo, pattern, at kasanayan para sa pagbuo ng mga API na talagang gustong gamitin ng mga developer.
---

## REST API Principles
Ang REST (Representational State Transfer) ay ang nangingibabaw na istilo ng arkitektura para sa mga web API. Itinuturing nito ang data bilang **mga mapagkukunan** na tinukoy ng mga URL, at gumagamit ng mga pamamaraan ng HTTP upang gumana sa mga ito.
### Mga Pangunahing Prinsipyo
| Prinsipyo | Paglalarawan |
|-----------|-------------|
| **Mga Mapagkukunan** | Ang lahat ay isang mapagkukunan na may URI (`/users/123`,`/orders/456`) |
| **Mga Paraan ng HTTP** | GET (basahin), POST (lumikha), PUT (palitan), PATCH (partial update), DELETE (alisin) |
| **Kawalan ng Estado** | Ang bawat kahilingan ay naglalaman ng lahat ng impormasyong kailangan; walang server-side session state |
| **Parang Interface** | Pare-parehong pagpapangalan sa mapagkukunan, karaniwang mga pamamaraan, karaniwang mga code ng katayuan |
| **Representasyon** | Maaaring katawanin ang mga mapagkukunan sa maraming format (JSON, XML) |
### Mga Kumbensyon sa Pagpapangalan ng Resource
| Gawin | Huwag |
|----|-------|
| `/users`(pangmaramihang pangngalan) | `/user`(isahan) |
| `/users/123/orders`(nakapugad) | `/getOrdersForUser?id=123`|
| `/products?category=electronics`(query params para sa pagsala) | `/productsByCategory/electronics`|
| Gumamit ng mga gitling:`/user-profiles`| Gumamit ng mga salungguhit:`/user_profiles`|
### Mga Paraan ng HTTP at Idempotency
| Paraan | Layunin | Idempotent? | Ligtas? |
|--------|---------|-------------|-------|
| **KUMUHA** | Magbasa ng mapagkukunan | ✅ Oo | ✅ Oo |
| **POST** | Lumikha ng mapagkukunan | ❌ Hindi | ❌ Hindi |
| **PUT** | Palitan nang buo ang isang mapagkukunan | ✅ Oo | ❌ Hindi |
| **PATCH** | Bahagyang nag-update ng mapagkukunan | ❌ Hindi* | ❌ Hindi |
| **TANGGAL** | Mag-alis ng mapagkukunan | ✅ Oo | ❌ Hindi |
* Maaaring gawing idempotent ang PATCH na may maingat na disenyo.
### Mga Code ng Katayuan ng HTTP
| Code | Ibig sabihin | Kailan Gagamitin |
|------|---------|-------------|
| **200** | OK | Matagumpay na GET, PUT, PATCH, DELETE |
| **201** | Nilikha | Matagumpay na POST (nagawa ang mapagkukunan) |
| **204** | Walang Nilalaman | Matagumpay na DELETE (walang ibabalik) |
| **400** | Masamang Kahilingan | Di-wastong input o maling porma ng kahilingan |
| **401** | Hindi awtorisado | Nawawala o hindi wastong pagpapatunay |
| **403** | Ipinagbabawal | Pinatotohanan ngunit hindi pinahintulutan |
| **404** | Hindi Natagpuan | Walang mapagkukunan |
| **409** | Salungatan | Duplicate na mapagkukunan o salungatan ng estado |
| **422** | Hindi Naprosesong Entity | Wastong JSON ngunit mga error sa semantiko |
| **429** | Napakaraming Kahilingan | Lumampas sa limitasyon ng rate |
| **500** | Error sa Panloob na Server | Hindi inaasahang error sa server |
| **502** | Masamang Gateway | Pagkabigo sa upstream na serbisyo |
| **503** | Hindi Available ang Serbisyo | Pansamantalang labis na karga o pagpapanatili |
---

## API Versioning
Nag-evolve ang mga API. Kapag kailangan mong gumawa ng mga pagbabago, ang pag-bersyon ay nagbibigay-daan sa mga kasalukuyang kliyente na patuloy na gumana.
| Diskarte | Halimbawa | Mga Pros | Cons |
|----------|---------|------|------|
| **URL path** | `/v1/users`,`/v2/users`| Simple, tahasang | Mga pagbabago sa URL bawat bersyon |
| **Parameter ng query** | `/users?version=2`| Flexible | Madaling kalimutan |
| **Header** | `Accept: application/vnd.myapi.v2+json`| Malinis na mga URL | Hindi gaanong natutuklasan |
| **Walang bersyon** | Schema evolution lang | Pinakasimple | Ang mga paglabag sa pagbabago ay nakakaapekto sa lahat |
**Pinakamahusay na kagawian**: gumamit ng URL path versioning (`/v1/`) para sa kalinawan. Suportahan ang kahit isang nakaraang bersyon. Huwag gamitin ang mga lumang bersyon na may malinaw na mga timeline.
---

## Mga Paraan ng Pagpapatunay
| Paraan | Paano Ito Gumagana | Pinakamahusay Para sa |
|--------|-------------|----------|
| **Mga API Key** | Lihim na key sa header (`X-API-Key: abc123`) | Server-to-server, mga simpleng pagsasama |
| **OAuth2** | Delegasyon na nakabatay sa token na may mga saklaw | Third-party na access, mga app na pinapahintulutan ng user |
| **JWT** | Self-contained token na may mga claim | Stateless authentication sa mga serbisyo |
| **Basic Auth** | Base64-encoded username:password | Development lang — hindi kailanman produksyon nang walang TLS |
| **Cookies ng session** | Server-side session ID sa HTTP-only na cookie | Mga tradisyunal na web application |
### Daloy ng OAuth2 (Pinasimple)
1. Nire-redirect ng kliyente ang user sa server ng pahintulot.
2. Nag-log in ang user at nagbibigay ng pahintulot.
3. Nagbabalik ang server ng awtorisasyon ng authorization code.
4. Nagpapalitan ng code ang kliyente para sa access token (at opsyonal na i-refresh ang token).
5. Gumagamit ang kliyente ng access token para tawagan ang API.
6. Kapag nag-expire ang access token, gumamit ng refresh token para makakuha ng bago.
---

## Mga Estilo ng API: REST vs GraphQL vs gRPC
| Tampok | pahinga | GraphQL | gRPC |
|---------|------|---------|------|
| **Format ng Data** | JSON (karaniwan) | JSON | Protobuf (binary) |
| **Mga Endpoint** | Maramihan (isa bawat mapagkukunan) | Isang endpoint | Tinukoy ng .proto file |
| **Sobrang pagkuha** | Karaniwan (makakuha ng higit sa kinakailangan) | Wala (tinukoy ng kliyente ang mga patlang) | Wala (tinukoy ng schema) |
| **Under-fetching** | Nangangailangan ng maraming tawag | Wala (kunin ang eksaktong kailangan) | Wala |
| **Real-time** | Kailangan ng mga WebSocket | Mga built-in na subscription | Built-in na streaming |
| **Pag-cache** | Ang HTTP caching ay natural na gumagana | Mas mahirap i-cache | Limitado |
| **Learning Curve** | Mababa | Katamtaman | Katamtaman–Mataas |
| **Pinakamahusay Para sa** | Mga Pampublikong API, CRUD app | Mga kumplikadong UI, mga mobile app | Mga panloob na microservice, mataas ang pagganap |
---

## Pagination, Pag-filter, at Pag-uuri
Para sa mga endpoint na nagbabalik ng mga listahan:
| Teknik | Halimbawa | Kailan Gagamitin |
|-----------|---------|-------------|
| **Offset/Limit** | `?offset=20&limit=10`| Simple; gumagana para sa maliliit na dataset |
| **Batay sa cursor** | `?cursor=abc123&limit=10`| Malaking dataset; pare-parehong mga resulta |
| **Keyset** | `?created_after=2024-01-01&limit=10`| Napakahusay; nangangailangan ng natatanging key |
```json
// Cursor-based response
{
  "data": [...],
  "pagination": {
    "next_cursor": "abc123",
    "has_more": true
  }
}
```

---

## Paglilimita sa Rate
Protektahan ang iyong API mula sa pang-aabuso at tiyakin ang patas na paggamit.
| Diskarte | Paano Ito Gumagana |
|----------|-------------|
| **Naayos na window** | N kahilingan sa bawat window ng oras (hal., 100/oras) |
| **Sliding window** | Mas butil-butil; binibilang ang mga kahilingan sa rolling window |
| **Token bucket** | Idinagdag ang mga token sa nakapirming rate; bawat kahilingan ay gumagamit ng isang token |
Ibalik ang`429 Too Many Requests`na may mga header:```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1625097600
Retry-After: 60
```

---

## Error sa Paghawak
Ang mga pare-parehong tugon sa error ay ginagawang mas madaling gamitin ang mga API:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "issue": "Invalid email format"
      }
    ]
  }
}
```

**Prinsipyo**: gumamit ng pare-parehong istruktura ng error, magsama ng mga naaaksyunan na mensahe, gumamit ng mga karaniwang HTTP status code, mag-log error sa server-side na may mga correlation ID, at hindi kailanman ilantad ang mga stack trace o panloob na detalye.
---

## Dokumentasyon ng API
| Tool | Paglalarawan |
|------|-------------|
| **OpenAPI (Swagger)** | Pamantayan sa industriya para sa dokumentasyon ng REST API |
| **Swagger UI** | Interactive na dokumentasyon ng API mula sa OpenAPI spec |
| **Kartero** | Pagsubok sa API, dokumentasyon, at pagbabahagi ng koleksyon |
| **Redoc** | Magagandang API reference docs mula sa OpenAPI spec |
| **GraphQL Playground / GraphiQL** | Interactive na paggalugad ng GraphQL |
**Pinakamahusay na kasanayan**: isulat muna ang spec ng OpenAPI (spec-driven na development), pagkatapos ay bumuo ng dokumentasyon at mga SDK ng kliyente mula rito.
---

## Mga Pattern ng API Gateway
Isang API gateway ang nasa pagitan ng mga kliyente at mga serbisyo ng backend, na nagbibigay ng isang entry point.
| Pananagutan | Paglalarawan |
|--------------|-------------|
| **Pagruruta** | Direktang mga kahilingan sa naaangkop na mga serbisyo ng backend |
| **Pagpapatotoo** | I-validate ang mga token sa antas ng gateway |
| **Paglilimita sa Rate** | Ilapat ang mga pandaigdigan o bawat-client na limitasyon |
| **Pagbabago** | Mag-convert sa pagitan ng mga protocol (REST ↔ gRPC) |
| **Pag-cache** | I-cache ang mga karaniwang tugon |
| **Pagsubaybay** | Sentralisadong pag-log at mga sukatan |
| **Pagbabalanse ng Pag-load** | Ipamahagi ang trapiko sa mga pagkakataon ng serbisyo |
| Tool | Uri |
|------|------|
| **Kong** | Open-source API gateway (Batay sa Nginx) |
| **AWS API Gateway** | Ganap na pinamamahalaan, isinama sa AWS |
| **Azure API Management** | Pinamamahalaang gateway na may portal ng developer |
| **Sugo / Istio** | Service mesh na may mga kakayahan sa API gateway |
| **Traefik** | Auto-discovery, Let's Encrypt integration |
---

## Mga Webhook
Hinahayaan ng mga Webhook ang iyong API na itulak ang mga kaganapan sa mga kliyente nang real-time, sa halip na gawin ang mga kliyente na mag-poll para sa mga pagbabago.
| Aspeto | Pinakamahusay na Kasanayan |
|--------|--------------|
| **Paghahatid** | POST kahilingan na may JSON payload sa URL ng kliyente |
| **Seguridad** | Mag-sign payload sa HMAC; bini-verify ng kliyente ang lagda |
| **Pagiging Maaasahan** | Subukan muli ang mga nabigong paghahatid na may exponential backoff |
| **Idempotency** | Isama ang natatanging ID ng kaganapan; pinangangasiwaan ng kliyente ang mga duplicate |
| **Bersyon** | Isama ang bersyon ng API sa webhook payload |
---

## Checklist ng Disenyo
- [ ] Ang mga mapagkukunan ay pangmaramihang pangngalan (`/users`, hindi`/getUser`)
- [ ] Mga pamamaraan ng HTTP na ginamit nang tama (GET para sa mga nabasa, POST para sa mga nilikha, atbp.)
- [ ] Pare-parehong format ng pagtugon sa error
- [ ] Pagbilang ng pahina para sa lahat ng mga endpoint ng listahan
- [ ] Paglilimita sa rate na may malinaw na mga header
- [ ] Tinukoy ang diskarte sa bersyon ng API
- [ ] Authentication at awtorisasyon sa lugar
- [ ] Input validation sa lahat ng endpoint
- [ ] Pinapanatili ang dokumentasyon ng OpenAPI/Swagger
- [ ] Na-configure nang tama ang CORS
- [ ] Ipinapatupad ang HTTPS sa produksyon
- [ ] Idempotency key para sa POST operations kung saan kinakailangan