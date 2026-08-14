---
# Metadata
title: "API Design and Integration Failures"
description: "API anti-patterns, breaking changes, versioning failures, cascading failures"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [api, design, integration, failures, lessons-from-failures]
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

# Mga Pagkabigo sa Disenyo ng API at Pagsasama
Ang mga API (Application Programming Interfaces) ay ang connective tissue ng modernong software — hinahayaan nila ang mga serbisyo na makipag-usap, hinahayaan ang mga third party na magsama, at hinahayaan ang mga team na magtrabaho nang nakapag-iisa. Kapag nagkamali ang disenyo ng API, ang mga kahihinatnan ay lilitaw sa bawat system na nakasalalay dito: mga sirang integrasyon, mga kahinaan sa seguridad, pagkadismaya ng developer, at magastos na muling pagsulat. Ang mga pagkabigo sa pagsasama — kung saan ang mga system ay hindi maaaring makipag-usap nang maaasahan — ay kabilang sa mga pinakakaraniwang pinagmumulan ng mga insidente ng produksyon.
---

## Mga Karaniwang Pagkabigo sa Disenyo ng API
### Mga Pagkakamali sa Disenyo
| Pagkakamali | Paglalarawan | Bunga |
|---------|-------------|-------------|
| **Hindi pare-pareho ang pagpapangalan** | `/getUsers`vs`/list_users`vs`/fetch-users`| Pagkalito; mga pagkakamali; mabagal na pag-unlad |
| **Mga overload na endpoint** | Isang endpoint na gumagawa ng 10 iba't ibang bagay batay sa mga parameter | Mahirap intindihin; mahirap subukan; mahirap baguhin |
| **Under-fetching** | Kailangang gumawa ng 5 API call ang kliyente para makakuha ng nauugnay na data | Mabagal; maaksaya; kumplikadong code ng kliyente |
| **Sobrang pagkuha** | Ibinabalik ng API ang lahat ng mga field kapag kailangan lang ng kliyente ng 2 | Nasayang na bandwidth; mabagal sa mobile; panganib sa seguridad (paglalantad ng hindi kinakailangang data) |
| **Walang bersyon** | Na-deploy ang mga paglabag sa pagbabago nang walang babala | Mga kliyente break; galit na mga developer |
| **Mga hindi malinaw na mensahe ng error** | "Error 500: Internal Server Error" na walang mga detalye | Imposibleng i-debug; mabagal na resolution |
| **Nawawalang pagination** | Ibinabalik ng Endpoint ang lahat ng record (maaaring milyon-milyon) | Mga timeout; pagkaubos ng memorya; nag-crash na mga kliyente |
| **Hindi pare-pareho ang mga code ng katayuan** | 200 OK para sa mga error; 500 para sa mga pagkakamali ng kliyente | Hindi matukoy ng mga kliyente ang tagumpay sa kabiguan |
### REST API Anti-Pattern
| Anti-Pattern | Paglalarawan | Mas mahusay na Diskarte |
|-------------|-------------|----------------|
| **Ginagamit ang GET para sa mga mutasyon** | `GET /delete-user?id=5`| Gumamit ng DELETE method |
| **Gumagamit ng POST para sa lahat** | `POST /get-users`; `POST /update-user`| Gumamit ng mga naaangkop na pamamaraan ng HTTP (GET, POST, PUT, PATCH, DELETE) |
| **Ibinabalik ang HTML mula sa API** | Ang API ay nagbabalik ng mga HTML fragment | Ibalik ang JSON; hayaan ang kliyente na mag-render |
| **Lohika ng negosyo sa mga URL** | `/users/active/premium/from-2023`| Gumamit ng mga parameter ng query o katawan ng kahilingan para sa mga kumplikadong filter |
| **Paglalantad ng database schema** | `/api/table_name/column`| Idisenyo ang API sa paligid ng mga mapagkukunan at mga konsepto ng domain, hindi mga talahanayan |
| **Walang HATEOAS / mga link** | Pina-hardcode ng kliyente ang lahat ng URL | Isama ang mga link sa mga kaugnay na mapagkukunan sa mga tugon |
---

## Mga Pagkabigo sa Seguridad
### Mga Karaniwang Kahinaan sa API
| Kahinaan | Paglalarawan | Halimbawa |
|--------------|-------------|---------|
| **Sirang pagpapatotoo** | Hindi maayos na nabe-verify ng API ang pagkakakilanlan | Nawawalang pagpapatunay ng token; tinanggap ang mga nag-expire na token |
| **Sobrang pagkakalantad ng data** | Ang API ay nagbabalik ng higit pang data kaysa sa mga pangangailangan ng kliyente | Ang endpoint ng user ay nagbabalik ng mga hash ng password at mga panloob na ID |
| **Pagtatalaga ng misa** | Maaaring magtakda ang kliyente ng mga field na hindi nila dapat |  Pinapayagan ng`PATCH /user`ang pagtatakda ng`role: "admin"`|
| **Iksyon** | Ang input ng user ay binibigyang kahulugan bilang code | SQL iniksyon; Iniksyon ng NoSQL; command injection |
| **IDOR** (Insecure Direct Object Reference) | Pag-access sa mga mapagkukunan sa pamamagitan ng pagpapalit ng ID sa URL | `/api/users/5`→ baguhin sa`/api/users/6`upang makita ang data ng ibang tao |
| **Nawawala ang paglilimita sa rate** | Walang limitasyon sa mga tawag sa API | Brute force; pagtanggi sa serbisyo; pag-scrape |
| **Maling configuration ng CORS** | Masyadong pinahihintulutan ang cross-origin na pag-access | `Access-Control-Allow-Origin: *`sa mga na-authenticate na endpoint |
### Mga Pagkabigo sa Pagpapatunay at Awtorisasyon
| Pagkabigo | Paglalarawan | Epekto |
|---------|-------------|--------|
| **Mga naka-hardcode na kredensyal** | Mga API key o password sa source code | Tumagas sa pamamagitan ng kontrol ng bersyon; naa-access sa lahat ng mga developer |
| **Walang pag-expire ng token** | Ang mga token ay hindi kailanman mawawalan ng bisa | Ang ninakaw na token ay nagbibigay ng permanenteng access |
| **Mahina ang mga secret key** | Maikli o predictable signing keys | Maaaring mapeke ang mga token |
| **Walang saklaw / mga pahintulot** | Ang lahat ng mga token ay may ganap na access | Nakompromiso na token = buong pag-access sa system |
| **Pagla-log ng sensitibong data** | Mga token o password sa mga log | Maa-access ng sinumang may access sa log |
| **Hindi pare-parehong awtorisasyon** | Sinusuri ng ilang mga endpoint ang mga pahintulot; ang iba ay hindi | Hindi awtorisadong pag-access sa pamamagitan ng hindi nababantayang mga endpoint |
---

## Mga Pagkabigo sa Pagsasama
### Mga Isyu sa Distributed System Integration
| Pagkabigo | Paglalarawan | Halimbawa |
|---------|-------------|---------|
| **Mahigpit na pagkakabit** | Ang mga serbisyo ay nakasalalay sa panloob na mga detalye ng pagpapatupad ng bawat isa | Ang pagpapalit ng database ng isang serbisyo ay masira ang tatlong iba pa |
| **Kasabay na chain** | Serbisyong A ay tumatawag B tumatawag C tumawag D; naiipon ang latency | 200ms + 300ms + 500ms = 1 segundong oras ng pagtugon |
| **Walang circuit breaker** | Ang hindi pagtupad sa serbisyo ay nagdudulot ng mga cascading failure | Mabagal ang Serbisyo D; lahat ng upstream services ay nauubos ang kanilang mga thread sa paghihintay |
| **No retry logic** | Ang mga pansamantalang kabiguan ay nagiging permanente | Network blip = nabigong transaksyon; kailangang subukang muli ng user nang manu-mano |
| **Sobrang pagsubok muli** | Sinusubukang muli nang walang pag-urong sa mga serbisyo sa pagbawi | Dumadagundong kawan problema |
| **Walang idempotency** | Ang muling pagsubok sa isang non-idempotent na operasyon ay lumilikha ng mga duplicate | Dalawang beses na sinisingil ang pagbabayad; dalawang beses na ginawa ang order |
| **Mga sorpresa sa huli na pagkakapare-pareho** | Nagbabasa ang kliyente ng lipas na data pagkatapos ng pagsulat | Profile ng mga update ng user; nagre-refresh ng pahina; ipinapakita pa rin ang lumang data |
### Mga Pagkabigo sa Pagsasama ng Third-Party
| Pagkabigo | Paglalarawan | Pagbabawas |
|---------|-------------|------------|
| **Mga pagbabago sa Vendor API** | Binabago ng third-party ang kanilang API nang walang abiso | Pinning ng bersyon; abstraction layer; pagsubaybay sa mga changelog ng vendor |
| **Paglilimita sa rate** | Pinipigilan ng third-party ang iyong mga kahilingan | Pag-cache; humiling ng pagpila; pakikipagnegosasyon sa mas mataas na limitasyon |
| **downtime ng vendor** | Hindi available ang serbisyo ng third-party | Mga circuit breaker; fallback na pag-uugali; multi-vendor na diskarte |
| **Nagbabago ang format ng data** | Binabago ng third-party ang format ng tugon | Pagpapatunay ng schema; layer ng pagbabagong-anyo; mga alerto sa mga pagbabago sa format |
| **Paghinto sa paggamit nang walang landas ng paglipat** | Inalis ng vendor ang endpoint na walang katumbas na | Manatiling may kaalaman; mapanatili ang abstraction; magplano ng mga migrasyon nang maaga |
---

## Pag-aaral ng Kaso
### Pag-aaral ng Kaso 1: Ang API na Ibinalik ang Lahat
| Aspeto | Paglalarawan |
|--------|--------------|
| **Scenario** | Ibinalik ng user API ng kumpanya ng SaaS ang lahat ng field ng user kabilang ang panloob na metadata |
| **Ano ang nangyari** | Walang field filtering; Kasama sa tugon ang mga hash ng password, panloob na tala, at mga flag ng admin |
| **Epekto** | Natuklasan ng mga mananaliksik sa seguridad ang pagkakalantad; pampublikong pagsisiwalat; Pagsisiyasat ng GDPR |
| **Root cause** | Na-serialize ng API ang buong modelo ng database nang walang pag-filter |
| **Ayusin** | Mga tahasang modelo ng pagtugon; field-level na kontrol sa pag-access; pagsusuri sa seguridad ng lahat ng mga endpoint |
| **Aralin** | Huwag kailanman direktang ilantad ang iyong modelo ng database sa pamamagitan ng isang API; gumamit ng mga DTO (Data Transfer Objects) |
### Pag-aaral ng Kaso 2: Ang Cascading Failure
| Aspeto | Paglalarawan |
|--------|--------------|
| **Scenario** | Isang arkitektura ng microservices na may kasabay na inter-service na komunikasyon |
| **Ano ang nangyari** | Isang serbisyo ang nakaranas ng paghina ng database; naghintay ng mga tugon sa upstream services; naubos na ang mga thread pool |
| **Epekto** | Kumpletuhin ang pagkawala ng system sa loob ng 45 minuto; lahat ng serbisyong apektado |
| **Root cause** | Walang mga circuit breaker; walang mga timeout; kasabay na chain ng dependency |
| **Ayusin** | Mga circuit breaker; mga timeout; async na komunikasyon kung saan posible; mga bulkhead |
| **Aralin** | Ang mga magkakasabay na tawag sa pagitan ng mga serbisyo ay lumilikha ng mga marupok na kadena; disenyo para sa kabiguan |
---

## Pinakamahuhusay na Kasanayan
### Checklist ng Disenyo ng API
| Lugar | Magsanay |
|------|----------|
| **Pagpapangalan** | Gumamit ng mga pangngalan para sa mga mapagkukunan; Mga pamamaraan ng HTTP para sa mga aksyon; pare-parehong kombensiyon sa pagbibigay ng pangalan |
| **Bersyon** | Bersyon mula sa unang araw; gumamit ng URL versioning (`/v1/`) o header versioning |
| **Pagination** | Palaging pahinain ang listahan ng mga endpoint; gumamit ng cursor-based pagination para sa malalaking dataset |
| **Error sa pangangasiwa** | Pare-parehong format ng error; isama ang mga error code; magbigay ng mga naaaksyunan na mensahe |
| **Paglilimita sa rate** | Ipatupad ang mga limitasyon sa rate; ibalik ang 429 na may retry-after header |
| **Idempotency** | Suportahan ang mga idempotency key para sa mga endpoint ng mutation |
| **Dokumentasyon** | OpenAPI / Swagger spec; panatilihin itong na-update; magbigay ng mga halimbawa |
| **Pagsubok** | Mga pagsubok sa kontrata; mga pagsusulit sa pagsasama; mga pagsubok sa kontrata na hinimok ng consumer |
| **Pagsubaybay** | Pagsubaybay sa latency; mga rate ng error; throughput; kalusugan ng dependency |
| **Pagtigil sa paggamit** | Ipahayag nang maaga ang mga paghinto; magbigay ng mga gabay sa paglilipat |
---

## Buod
Ang mga pagkabigo sa disenyo ng API ay mula sa kosmetiko (hindi pantay-pantay na pagpapangalan) hanggang sa sakuna (mga kahinaan sa seguridad, mga pagkabigo ng cascading). Ang pinakakaraniwang mga pagkakamali sa disenyo — mga overload na endpoint, sobrang pagkuha, nawawalang pagination, hindi malinaw na mga error — ay nagpapahirap sa mga API na gamitin at mapanatili. Mga pagkabigo sa seguridad — sirang pagpapatotoo, IDOR, pagtatalaga ng masa, labis na pagkakalantad ng data — ilantad ang mga system sa pag-atake. Mga pagkabigo sa pagsasama — mahigpit na pagkakabit, magkasabay na mga kadena, nawawalang mga circuit breaker, walang pagka-idempotency — lumikha ng mga marupok na sistema kung saan ang isang pagkabigo ay dumadaloy sa mga serbisyo. Ang mga pagsasama ng third-party ay nagdaragdag ng panlabas na panganib: mga pagbabago sa API, paglilimita sa rate, at downtime ng vendor. Ang mga estratehiya sa pag-iwas ay mahusay na naitatag: gumamit ng mga tahasang modelo ng pagtugon; bersyon mula sa unang araw; magpatupad ng mga circuit breaker at timeout; disenyo para sa idempotency; patunayan at sanitize ang lahat ng mga input; subaybayan ang lahat; at ituring ang mga kontrata ng API bilang mga umiiral na kasunduan na nangangailangan ng koordinasyon upang baguhin. Ang pinakamahusay na mga API ay nakakainip — predictable, pare-pareho, well-documented, at nababanat sa pagkabigo.