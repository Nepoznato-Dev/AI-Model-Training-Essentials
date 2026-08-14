<!--
---
# Metadata
title: "Testing Methodologies"
description: "Unit, integration, E2E, TDD, BDD, test pyramids"
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
tags: [testing, methodologies, coding-and-technology]
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
# Mga Paraan ng Pagsubok
Ang pagsubok ay kung paano ka magkakaroon ng kumpiyansa na gumagana ang iyong code — at higit sa lahat, ang mga pagbabago dito ay hindi masisira kung ano ang gumagana na. Ang mahusay na pagsubok ay nakakakuha ng mga bug bago gawin ng mga gumagamit, mga dokumento na inaasahang pag-uugali, at nagbibigay-daan sa walang takot na refactoring. Sinasaklaw ng file na ito ang buong spectrum ng mga diskarte sa pagsubok, mula sa mga unit test hanggang sa end-to-end na mga pagsubok, at ang mga prinsipyong ginagawang epektibo ang pagsubok.
---

## Ang Testing Pyramid
Inilalarawan ng testing pyramid ang perpektong pamamahagi ng mga pagsubok sa isang proyekto.
```
        /  E2E  \          ← Few; slow; expensive; test the whole system
       /─────────\
      / Integration\       ← Some; test how components work together
     /───────────────\
    /   Unit Tests    \    ← Many; fast; cheap; test individual functions
   /─────────────────────\
```

| Antas | Bilangin | Bilis | Gastos | Ano ang Sinusubok Nito |
|-------|-------|-------|------|--------------|
| **Yunit** | Maraming | Mabilis (ms) | Mababa | Mga indibidwal na function, klase, pamamaraan |
| **Pagsasama** | Ilang | Katamtaman (100ms-s) | Katamtaman | Paano nakikipag-ugnayan ang mga bahagi; mga query sa database; Mga tawag sa API |
| **E2E** | Ilang | Mabagal (segundo-minuto) | Mataas | Ang buong user ay dumadaloy sa totoong system |
---

## Pagsusuri ng Yunit
Pagsubok sa mga indibidwal na unit ng code nang hiwalay.
### Mga Prinsipyo
| Prinsipyo | Paglalarawan |
|-----------|-------------|
| **Mabilis** | Ang bawat pagsubok ay dapat tumakbo sa milliseconds |
| **Nakahiwalay** | Ang mga pagsubok ay hindi nakasalalay sa isa't isa; walang nakabahaging estado |
| **Deterministic** | Parehong input → parehong output sa bawat oras (walang randomness, walang dependency sa oras) |
| **Pagsusuri sa sarili** | Awtomatikong pumasa o nabigo ang pagsubok; walang manu-manong inspeksyon |
| **Napapanahon** | Isinulat sa tabi o bago ang code (TDD) |
### Anatomy ng isang Pagsubok
| Yugto | Paglalarawan |
|-------|-------------|
| **Ayusin** | I-set up ang data ng pagsubok at mga dependency |
| **Act** | Tawagan ang function o paraan na sinusuri |
| **Igiit** | I-verify na tumutugma ang resulta sa mga inaasahan |
### Ano ang Susubukan
| Kategorya | Mga halimbawa |
|----------|---------|
| **Maligayang landas** | Ang mga normal na input ay gumagawa ng mga inaasahang output |
| **Mga edge case** | Walang laman na input, null, zero, maximum na mga halaga, isang elemento |
| **Kaso ng error** | Di-wastong input, nawawalang data, tinanggihan ang pahintulot |
| **Mga kundisyon sa hangganan** | Off-by-one; eksakto sa mga limitasyon |
### Mapanukso at Stubbing
| Termino | Paglalarawan | Kailan Gagamitin |
|------|-------------|-------------|
| **Kutya** | Isang pekeng bagay na nagtatala kung paano ito tinawag na | Pag-verify ng mga pakikipag-ugnayan (tinawag ba ang paraang ito?) |
| **Stub** | Isang pekeng bagay na nagbabalik ng mga paunang natukoy na halaga | Nagbibigay ng data ng pagsubok (ibalik ang user na ito mula sa database) |
| **Spy** | Isang wrapper na nagtatala ng mga tawag sa isang tunay na bagay | Bahagyang pag-verify |
| **Peke** | Isang pinasimple ngunit gumaganang pagpapatupad | In-memory database para sa mga pagsubok |
| Mapanuksong Library | Wika |
|----------------|--------|
| **unittest.mock** | Python |
| **Jest** | JavaScript/TypeScript |
| **Mockito** | Java |
| **Moq** | C# |
| **testify / gomock** | Pumunta |
---

## Pagsusuri sa Pagsasama
Pagsubok kung paano gumagana ang maraming bahagi.
| Ano ang Susubukan | Halimbawa |
|-------------|---------|
| **Mga query sa database** | Ang ORM ba ay gumagawa ng tamang SQL? Ginagamit ba ang mga index? |
| **Mga endpoint ng API** | Gumagana ba ang buong ikot ng kahilingan-tugon? |
| **Mga pakikipag-ugnayan sa serbisyo** | Tama ba ang tawag ng serbisyo A sa serbisyo B? |
| **Mga panlabas na dependency** | Gumagana ba ang pagsasama ng gateway ng pagbabayad? |
### Mga diskarte
| Diskarte | Paglalarawan | Trade-off |
|----------|-------------|-----------|
| **Mga totoong dependency** | Gumamit ng totoong database, totoong pila ng mensahe | Pinaka makatotohanan; mas mabagal; mas mahirap i-set up |
| **Mga lalagyan ng pagsubok** | Paikutin ang mga container ng Docker para sa bawat test run | Magandang balanse; maaaring kopyahin |
| **Mga alternatibong nasa memorya** | H2 sa halip na PostgreSQL; in-memory message bus | Mabilis; maaaring makaligtaan ang mga isyu sa totoong mundo |
| **Pagsubok sa kontrata** | I-verify na ginagalang ng mga serbisyo ang kanilang mga kontrata sa API | Nakakakuha ng mga pagbabago sa interface |
---

## End-to-End (E2E) Testing
Pagsubok sa kumpletong system mula sa pananaw ng user.
| Tool | Uri | Pinakamahusay Para sa |
|------|------|----------|
| **mandula** | Pag-aautomat ng browser | Mga aplikasyon sa web; cross-browser |
| **Cypress** | Pag-aautomat ng browser | Mga aplikasyon sa web; karanasan ng developer |
| **Selenium** | Pag-aautomat ng browser | Legacy; malawak na suporta sa wika |
| **Detox** | Mobile E2E | React Native app |
| **Appium** | Mobile E2E | Native at hybrid na mobile app |
| **Maestro** | Mobile E2E | Mga mobile app; simpleng YAML syntax |
| **k6 / Locust** | Pagsubok sa pag-load | Pagganap sa ilalim ng pagkarga |
### E2E Pinakamahuhusay na Kasanayan
| Magsanay | Bakit |
|----------|-----|
| **Subukan ang mga kritikal na landas lamang** | Ang mga pagsusulit sa E2E ay mabagal; tumuon sa kung ano ang pinakamahalaga |
| **Gumamit ng mga pabrika ng data ng pagsubok** | Lumikha ng data ng pagsubok sa programmatically; huwag umasa sa data ng binhi |
| **Maglinis pagkatapos ng mga pagsubok** | Ang bawat pagsubok ay dapat umalis sa system sa isang kilalang estado |
| **Iwasang subukan ang mga detalye ng UI** | Pagsubok ng gawi, hindi mga klase ng CSS o mga posisyon ng elemento |
| **Tumakbo sa CI** | Dapat awtomatikong tumakbo ang mga pagsubok sa E2E sa bawat pagbabago |
---

## Test-Driven Development (TDD)
Isulat muna ang pagsubok, pagkatapos ay isulat ang code para makapasa ito.
| Hakbang | Paglalarawan |
|------|-------------|
| **1. Pula** | Sumulat ng isang bagsak na pagsubok na naglalarawan sa nais na gawi |
| **2. Berde** | Isulat ang minimum na code para maipasa ang pagsubok |
| **3. Refactor** | Linisin ang code habang pinananatiling berde ang mga pagsubok |
| Benepisyo | Paglalarawan |
|---------|-------------|
| **Feedback sa disenyo** | Pinipilit ka ng mga pagsubok na isipin ang tungkol sa mga interface bago ang pagpapatupad |
| **Kaligtasan ng regression** | Ang bawat bug ay nakakakuha ng pagsubok; hindi na makakabalik ang bug |
| **Dokumentasyon** | Ang mga pagsusulit ay nagsisilbing buhay na dokumentasyon ng inaasahang pag-uugali |
| **Kumpiyansa** | Ang mataas na saklaw ng pagsubok ay nagbibigay-daan sa walang takot na refactoring |
---

## Pag-unlad na Batay sa Pag-uugali (BDD)
Pinapalawak ng BDD ang TDD sa pamamagitan ng pagsusulat ng mga pagsubok sa natural na wika na naglalarawan ng gawi mula sa pananaw ng user.
### Given-When-Then Format
```
Given a user with an empty shopping cart
When they add a "Python Book" priced at $29.99
Then the cart total should be $29.99
And the cart should contain 1 item
```

| Tool | Wika |
|------|----------|
| **Pipino** | Java, JavaScript, Ruby, at iba pa |
| **Asal** | Python |
| **SpecFlow** | C# |
| **Jest** (with describe/it) | JavaScript |
---

## Iba pang Uri ng Pagsubok
| Uri | Ano ang Sinusubok Nito | Mga tool |
|------|--------------|-------|
| **Pagganap/Pag-load** | Pag-uugali ng system sa ilalim ng pagkarga | k6, JMeter, Locust, Gatling |
| **Seguridad** | Mga kahinaan at mga vector ng pag-atake | OWASP ZAP, Burp Suite, Snyk |
| **Accessibility** | Pagsunod sa WCAG | palakol, Parola, pa11y |
| **Kontrata** | API compatibility sa pagitan ng mga serbisyo | Pact, Spring Cloud Contract |
| **Mutation** | Kalidad ng test suite mismo | Stryker, mutmut, PIT |
| **Visual regression** | Nagbabago ang UI sa pagitan ng mga bersyon | Percy, Chromatic, BackstopJS |
| **Kagulo** | System resilience sa mga pagkabigo | Chaos Monkey, Litmus, Gremlin |
| **Usok** | Basic functionality pagkatapos ng deployment | Mga custom na script; mga pagsusuri sa kalusugan |
| **Babad** | Pag-uugali ng system sa mahabang panahon | Mga pagsubok sa pag-load nang matagal |
---

## Organisasyon ng Pagsubok
| Pattern | Paglalarawan | Kailan Gagamitin |
|---------|-------------|-------------|
| **Co-located** | Mga pagsubok sa tabi ng code na sinubok nila (`src/utils.test.ts`) | Karamihan sa mga proyekto; madaling mahanap |
| **Hiwalay na direktoryo** | Mga pagsubok sa isang`tests/`o`__tests__/`folder | Mga malalaking proyekto; malinaw na paghihiwalay |
| **Mga pansubok na fixture** | Nakabahaging data ng pagsubok sa isang`fixtures/`na direktoryo | Kapag maraming pagsubok ang nangangailangan ng parehong data |
| **Mga kagamitan sa pagsubok** | Mga nakabahaging katulong sa isang`test-utils/`na direktoryo | Kapag kumplikado ang logic ng setup |
---

## Saklaw ng Code
| Sukatan | Ang Sinusukat Nito | Limitasyon |
|--------|-----------------|------------|
| **Sakop ng linya** | Porsiyento ng mga linya ng code na isinagawa ng mga pagsubok | Hindi sinusukat ang kalidad ng mga pahayag |
| **Sakop ng sangay** | Porsiyento ng mga sangay (kung/iba) ang kinuha | Mas mahusay kaysa sa saklaw ng linya; hindi pa rin nahuhuli ang lahat ng mga bug |
| **Path coverage** | Porsiyento ng mga execution path na kinuha | Pinaka masinsinan; exponential sa kumplikadong code |
| **Mutation score** | Porsiyento ng mga mutasyon na nakuha ng mga pagsubok | Pinakamahusay na sukatan ng kalidad ng pagsubok |
**Target**: 80% line coverage ay isang makatwirang default. Ngunit ang coverage ay isang gabay, hindi isang layunin — 100% coverage na may mahinang assertions ay mas masahol pa kaysa sa 70% coverage na may masusing pagsubok.
---

## Patuloy na Pagsasama at Pagsubok
| Magsanay | Paglalarawan |
|----------|-------------|
| **Patakbuhin ang lahat ng unit test sa bawat commit** | Mabilis na feedback; nahuhuli agad ang mga regression |
| **Magpatakbo ng mga pagsubok sa pagsasama sa PR** | Nakakakuha ng mga isyu na hindi nakuha ng mga pagsubok sa unit |
| **Patakbuhin ang mga pagsusulit sa E2E gabi-gabi o sa pagsasama sa main** | Mabagal ngunit masinsinan |
| **Mabilis na nabigo** | Itigil ang pipeline sa unang pagkabigo na makatipid ng oras |
| **Patakaran sa flaky test** | I-quarantine o tanggalin kaagad ang mga patumpik-tumpik na pagsubok; huwag na huwag pansinin |
| **Pagsubok sa paralelisasyon** | Magpatakbo ng mga pagsubok nang magkatulad upang mabawasan ang oras ng CI |
---

## Mga Praktikal na Tip
- **Malinaw na sinusuri ang pangalan.** Sinasabi sa iyo ng`test_calculates_tax_for_high_earner`kung ano ang nasira.  Walang sinasabi sa iyo ang `test_1`.
- **Isang assertion bawat pagsubok (kapag praktikal).** Ginagawang madaling masuri ang mga pagkabigo.
- **Huwag subukan ang mga detalye ng pagpapatupad.** Subukan ang gawi. Kung refactor mo ang mga internal, hindi dapat masira ang mga pagsubok.
- **Iwasang subukan ang code ng third-party.** Kutya ang mga panlabas na aklatan; subukan ang pakikipag-ugnayan ng iyong code sa kanila.
- **Gawin ang mga pagsubok nang mabilis.** Kung ang iyong test suite ay tumatagal ng 10 minuto, hihinto ang mga developer sa pagpapatakbo nito. Mag-optimize nang walang humpay.
- **Tanggalin ang mga patay na pagsubok.** Ang mga pagsubok na palaging pumasa o sumusubok sa tinanggal na code ay ingay.
- **Itrato ang test code tulad ng production code.** Dapat itong mabasa, mapanatili, at maayos ang pagkakaayos.
---

## Buod
Ang pagsubok ay hindi opsyonal — ito ay kung paano ka bumuo ng software na hindi nasisira. Ginagabayan ka ng testing pyramid patungo sa maraming mabilis na unit test, ilang integration test, at ilang E2E test. Nagbibigay ang TDD at BDD ng mga structured na diskarte. Ang panunuya ay naghihiwalay ng mga yunit para sa pagsubok. Sinusukat ng saklaw ng code ang lawak ngunit hindi ang lalim. Ang pinakamahalagang prinsipyo ay ito: kung hindi ito susubukan, ito ay sira — hindi mo pa lang alam.