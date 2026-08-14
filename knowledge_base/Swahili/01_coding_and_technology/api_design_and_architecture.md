<!--
---
# Metadata
title: "API Design and Architecture"
description: "REST, GraphQL, gRPC, versioning, auth, API gateways"
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

-->
# Ubunifu wa API na Usanifu
API (Kiolesura cha Kuandaa Programu) ni jinsi vipengele vya programu vinavyozungumza. API iliyoundwa vizuri ni angavu, thabiti, na inafurahisha kufanya kazi nayo. Iliyoundwa vibaya husababisha kuchanganyikiwa, hitilafu, na kufadhaika. Faili hii inashughulikia kanuni, ruwaza, na mbinu za kuunda API ambazo wasanidi wanataka kutumia.
---

## Kanuni za API za REST
REST (Uhamisho wa Jimbo Uwakilishi) ndio mtindo mkuu wa usanifu wa API za wavuti. Huchukulia data kama **rasilimali** zinazotambuliwa na URL, na hutumia mbinu za HTTP kuzifanyia kazi.
### Kanuni za Msingi
| Kanuni | Maelezo |
|-----------|-------------|
| **Nyenzo** | Kila kitu ni rasilimali iliyo na URI ( `/users/123`,`/orders/456`) |
| **Mbinu za HTTP** | PATA (soma), POST (unda), WEKA (badilisha), PATCH (sasisho kidogo), FUTA (ondoa) |
| **Kutokuwa na msimamo** | Kila ombi lina habari zote zinazohitajika; hakuna hali ya kikao cha upande wa seva |
| **Kiolesura Sare** | Kutaja rasilimali thabiti, mbinu za kawaida, misimbo ya hali ya kawaida |
| **Uwakilishi** | Rasilimali zinaweza kuwakilishwa katika miundo mingi (JSON, XML) |
### Mikataba ya Kutaja Nyenzo
| Kufanya | Usifanye |
|----|-------|
| `/users`(nomino ya wingi) | `/user`(umoja) |
| `/users/123/orders`(kiota) | `/getOrdersForUser?id=123`|
| `/products?category=electronics`(vigezo vya swala vya kuchuja) | `/productsByCategory/electronics`|
| Tumia vistari:`/user-profiles`| Tumia underscores:`/user_profiles`|
### Mbinu za HTTP na Upungufu
| Mbinu | Kusudi | Huna uwezo? | Salama? |
|--------|-----------------------|-------|
| **PATA** | Soma rasilimali | ✅ Ndiyo | ✅ Ndiyo |
| **POST** | Unda rasilimali | ❌ Hapana | ❌ Hapana |
| **WEKA** | Badilisha rasilimali kabisa | ✅ Ndiyo | ❌ Hapana |
| **PATCH** | Sasisha rasilimali kwa kiasi | ❌ Hapana* | ❌ Hapana |
| **FUTA** | Ondoa rasilimali | ✅ Ndiyo | ❌ Hapana |
*PATCH inaweza kufanywa kutokuwa na uwezo kwa muundo wa uangalifu.
### Misimbo ya Hali ya HTTP
| Msimbo | Maana | Wakati wa Kutumia |
|------|-----------------------|
| **200** | SAWA | Imefaulu KUPATA, WEKA, KUBAKI, FUTA |
| **201** | Imeundwa | POST Imefaulu (rasilimali imeundwa) |
| **204** | Hakuna Maudhui | Imefaulu KUFUTA (hakuna cha kurudisha) |
| **400** | Ombi baya | Ingizo batili au ombi lenye hitilafu |
| **401** | Isiyoidhinishwa | Uthibitishaji unaokosekana au batili |
| **403** | Imepigwa marufuku | Imethibitishwa lakini haijaidhinishwa |
| **404** | Haikupatikana | Rasilimali haipo |
| **409** | Migogoro | Rudufu mgogoro wa rasilimali au jimbo |
| **422** | Huluki Isiyochakatwa | JSON halali lakini hitilafu za kisemantiki |
| **429** | Maombi Mengi Sana | Kiwango cha juu cha bei kimepitwa |
| **500** | Hitilafu ya Ndani ya Seva | Hitilafu ya seva isiyotarajiwa |
| **502** | Lango Mbaya | Kushindwa kwa huduma ya juu |
| **503** | Huduma Haipatikani | Upakiaji wa muda au matengenezo |
---

## Uchapishaji wa API
API hubadilika. Unapohitaji kufanya mabadiliko makubwa, uchapishaji huruhusu wateja waliopo kuendelea kufanya kazi.
| Mkakati | Mfano | Faida | Hasara |
|----------|---------|------|------|
| **Njia ya URL** | `/v1/users`,`/v2/users`| Rahisi, wazi | Mabadiliko ya URL kwa kila toleo |
| **Kigezo cha hoja** | `/users?version=2`| Inayobadilika | Rahisi kusahau |
| **Kichwa** | `Accept: application/vnd.myapi.v2+json`| Safisha URL | Inayoweza kugundulika kidogo |
| **Hakuna toleo** | Mageuzi ya schema pekee | Rahisi | Mabadiliko ya kuvunja huathiri kila mtu |
**Mazoezi bora**: tumia matoleo ya njia ya URL (`/v1/`) kwa uwazi. Inasaidia angalau toleo moja la awali. Acha kutumia matoleo ya zamani yenye rekodi za matukio zilizo wazi.
---

## Mbinu za Uthibitishaji
| Mbinu | Jinsi Inavyofanya Kazi | Bora Kwa |
|--------|-------------|-----------|
| **Vifunguo vya API** | Kitufe cha siri kwenye kichwa (`X-API-Key: abc123`) | Seva-kwa-server, miunganisho rahisi |
| **OAuth2** | Ujumbe kulingana na ishara na upeo | Ufikiaji wa watu wengine, programu zilizoidhinishwa na mtumiaji |
| **JWT** | Tokeni inayojitosheleza yenye madai | Uthibitishaji usio na uraia katika huduma zote |
| **Hadithi ya Msingi** | Jina la mtumiaji lililosimbwa kwa Base64:nenosiri | Maendeleo pekee - kamwe uzalishaji bila TLS |
| **Vidakuzi vya kipindi** | Kitambulisho cha kipindi cha upande wa seva katika kidakuzi cha HTTP pekee | Programu za jadi za wavuti |
### Mtiririko wa OAuth2 (Kilichorahisishwa)
1. Mteja huelekeza mtumiaji kwenye seva ya uidhinishaji.
2. Mtumiaji huingia na kutoa ruhusa.
3. Seva ya uidhinishaji inarudisha msimbo wa uidhinishaji.
4. Msimbo wa kubadilishana mteja kwa tokeni ya ufikiaji (na kwa hiari onyesha tokeni).
5. Mteja hutumia tokeni ya ufikiaji kupiga API.
6. Tokeni ya ufikiaji inapoisha, tumia tokeni ya kuonyesha upya ili kupata mpya.
---

## Mitindo ya API: REST dhidi ya GraphQL dhidi ya gRPC
| Kipengele | PUMZIKA | GraphQL | gRPC |
|---------|------|---------|------|
| **Muundo wa Data** | JSON (kawaida) | JSON | Protobuf (binary) |
| **Vipengele vya mwisho** | Nyingi (moja kwa kila rasilimali) | Mwisho mmoja | Inafafanuliwa na faili ya .proto |
| **Inaleta kupita kiasi** | Kawaida (pata zaidi ya inahitajika) | Hakuna (mteja anabainisha sehemu) | Hakuna (schema-defined) |
| **Inaleta chini kabisa** | Inahitaji simu nyingi | Hakuna (pata kile kinachohitajika) | Hakuna |
| **Wakati halisi** | WebSockets zinahitajika | Usajili uliojumuishwa | Utiririshaji uliojengewa ndani |
| **Kuhifadhi** | Uakibishaji wa HTTP hufanya kazi kawaida | Ngumu zaidi kuweka akiba | Kidogo |
| **Njia ya Kujifunza** | Chini | Kati | Kati-Juu |
| **Bora Kwa** | API za Umma, programu za CRUD | UI tata, programu za simu | Huduma ndogo za ndani, utendaji wa juu |
---

## Kuweka kurasa, Kuchuja, na Kupanga
Kwa vidokezo vinavyorudisha orodha:
| Mbinu | Mfano | Wakati wa Kutumia |
|-----------|---------|-------------|
| **Kupunguza/Kikomo** | `?offset=20&limit=10`| Rahisi; inafanya kazi kwa hifadhidata ndogo |
| **Inayotokana na mshale** | `?cursor=abc123&limit=10`| Seti kubwa za data; matokeo thabiti |
| **Kitufe** | `?created_after=2024-01-01&limit=10`| Ufanisi sana; inahitaji ufunguo wa kipekee |
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

## Kupunguza Viwango
Linda API yako dhidi ya matumizi mabaya na uhakikishe matumizi ya haki.
| Mkakati | Jinsi Inavyofanya Kazi |
|----------|-------------|
| **Dirisha lisilohamishika** | Maombi N kwa kila dirisha la wakati (k.m., 100/saa) |
| **Dirisha la kuteleza** | Punjepunje zaidi; huhesabu maombi kwenye dirisha linalozunguka |
| **Ndoo ya ishara** | Ishara zilizoongezwa kwa kiwango cha kudumu; kila ombi hutumia ishara |
Rudisha`429 Too Many Requests`na vichwa:```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1625097600
Retry-After: 60
```

---

## Kushughulikia Hitilafu
Majibu ya makosa thabiti hufanya API kuwa rahisi zaidi kufanya kazi nayo:
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

**Kanuni**: tumia muundo wa hitilafu thabiti, ni pamoja na ujumbe unaoweza kutekelezeka, tumia misimbo ya kawaida ya hali ya HTTP, hitilafu za kumbukumbu upande wa seva na vitambulisho vya uwiano, na usiwahi kufichua ufuatiliaji wa rafu au maelezo ya ndani.
---

## Hati za API
| Zana | Maelezo |
|------|-------------|
| **OpenAPI (Swagger)** | Kiwango cha sekta ya uhifadhi wa nyaraka za API ya REST |
| **Swagger UI** | Hati shirikishi za API kutoka specifikationer OpenAPI |
| **Mtume** | Jaribio la API, uhifadhi wa nyaraka, na kushiriki mkusanyiko |
| **Redoc** | Hati nzuri za kumbukumbu za API kutoka kwa OpenAPI spec |
| **Uwanja wa Michezo wa GraphQL / GraphiQL** | Utafutaji mwingiliano wa GraphQL |
**Mazoezi bora**: andika kielelezo cha OpenAPI kwanza (maendeleo yanayoendeshwa na mahususi), kisha toa hati na SDK za mteja kutoka kwayo.
---

## Miundo ya Lango la API
Lango la API hukaa kati ya wateja na huduma za nyuma, kutoa sehemu moja ya kuingilia.
| Wajibu | Maelezo |
|-----------------------------|
| **Uelekezaji** | Maombi ya moja kwa moja kwa huduma zinazofaa za nyuma |
| **Uthibitishaji** | Thibitisha tokeni kwenye kiwango cha lango |
| **Kikomo cha Viwango** | Tekeleza vikomo vya kimataifa au kwa kila mteja |
| **Mabadiliko** | Badilisha kati ya itifaki (REST ↔ gRPC) |
| **Kuhifadhi** | Akiba ya majibu ya kawaida |
| **Ufuatiliaji** | Uwekaji miti wa kati na vipimo |
| **Kusawazisha Mizigo** | Sambaza trafiki katika matukio ya huduma |
| Zana | Andika |
|------|------|
| **Kong** | Lango la API la chanzo-wazi (msingi wa Nginx) |
| **Lango la AWS API** | Imesimamiwa kikamilifu, imeunganishwa na AWS |
| **Usimamizi wa API ya Azure** | Lango linalodhibitiwa na lango la msanidi |
| **Mjumbe / Istio** | Matundu ya huduma yenye uwezo wa lango la API |
| **Traefik** | Ugunduzi otomatiki, Wacha Tusimba ujumuishaji |
---

## Mitandao
Webhooks huruhusu API yako kusukuma matukio kwa wateja katika muda halisi, badala ya kufanya kura ya maoni kwa wateja kwa mabadiliko.
| Kipengele | Mazoezi Bora |
|--------|--------------|
| **Uwasilishaji** | POST ombi na malipo ya JSON kwa URL ya mteja |
| **Usalama** | Saini mizigo ya malipo na HMAC; mteja anathibitisha sahihi |
| **Kuegemea** | Jaribu tena uwasilishaji ulioshindwa na urejesho wa kielelezo |
| **Upungufu** | Jumuisha kitambulisho cha kipekee cha tukio; mteja hushughulikia nakala |
| **Matoleo** | Jumuisha toleo la API katika upakiaji wa mtandao |
---

## Orodha ya Usanifu
- [ ] Rasilimali ni nomino za wingi (`/users`, si`/getUser`)
- [ ] Mbinu za HTTP zinazotumiwa kwa usahihi (PATA kwa usomaji, POST kwa uundaji, n.k.)
- [ ] Umbizo la jibu la hitilafu thabiti
- [ ] Pagination kwa orodha zote za mwisho
- [ ] Kuweka kikomo kwa vichwa vilivyo wazi
- [ ] mkakati wa uchapishaji wa API umefafanuliwa
- [ ] Uthibitishaji na uidhinishaji mahali
- [ ] Uthibitishaji wa ingizo kwenye ncha zote
- [ ] Hati za OpenAPI/Swagger zimedumishwa
- [ ] CORS imesanidiwa ipasavyo
- [ ] HTTPS inatekelezwa katika uzalishaji
- [ ] Vifunguo vya kutokuwa na uwezo kwa shughuli za POST inapohitajika