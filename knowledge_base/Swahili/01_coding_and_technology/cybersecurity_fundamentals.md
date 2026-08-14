---
# Metadata
title: "Cybersecurity Fundamentals"
description: "Encryption, TLS, OWASP, secure coding, SDL"
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
tags: [cybersecurity, coding-and-technology]
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
# Misingi ya Usalama Mtandaoni
Usalama ni taaluma ambayo lazima iunganishwe katika kila safu ya mfumo tangu mwanzo, badala ya kuongezwa kama mawazo ya baadaye. Iwe ni kujenga programu ya wavuti, kudhibiti miundombinu, au kusafirisha API, kuelewa mazingira ya tishio na misingi ya ulinzi ni muhimu.
---

## Usimbaji fiche na Siri
### Usimbaji Ulinganifu dhidi ya Usimbaji Fiche
| Andika | Jinsi Inavyofanya Kazi | Kasi | Usambazaji Muhimu | Mifano |
|------|---------------------|----------------|-----------|
| **Ulinganifu** | Kitufe sawa cha usimbaji fiche na usimbuaji | Haraka | Changamoto: jinsi ya kushiriki ufunguo? | AES-256, ChaCha20 |
| **Asymmetric** | Usimbaji fiche wa vitufe vya umma, usimbaji wa ufunguo wa faragha | Polepole | Ufunguo wa umma unaweza kushirikiwa kwa uwazi | RSA, ECC (Elliptic Curve) |
Kwa mazoezi, mifumo mingi hutumia **zote mbili**: usimbaji fiche usiolinganishwa ili kubadilishana kwa usalama ufunguo wa ulinganifu, kisha usimbaji fiche linganifu kwa wingi wa data. Hivi ndivyo TLS/HTTPS inavyofanya kazi.
### Hashing
Hashing ni chaguo la kukokotoa la njia moja: inabadilisha ingizo kuwa mfuatano wa saizi isiyobadilika. Hauwezi kuibadilisha, lakini ingizo sawa kila wakati hutoa matokeo sawa.
| Tumia Kesi | Algorithm Iliyopendekezwa | Epuka |
|----------|---------------------|-------|
| **Hifadhi ya nenosiri** | Argon2id, bcrypt, scrypt | MD5, SHA-1, SHA-256 wazi (haraka sana) |
| **Uadilifu wa data** | SHA-256, SHA-3 | MD5 (iliyovunjika), SHA-1 (iliyovunjika) |
| **Sahihi za kidijitali** | Ed25519, RSA-2048+ | DSA |
### TLS/HTTPS
HTTPS ni HTTP juu ya TLS (Usalama wa Tabaka la Usafiri). Inatoa:
- **Usimbaji fiche**: Data katika usafiri wa umma haiwezi kusomwa na wasikilizaji.
- **Uthibitishaji**: Seva inathibitisha utambulisho wake kupitia cheti.
- **Uadilifu**: Data haiwezi kurekebishwa wakati wa usafirishaji bila kutambuliwa.
Tumia TLS 1.2 au 1.3. Zima TLS 1.0 na 1.1. Washa HSTS (Usalama Mkali wa Usafiri wa HTTP) ili kulazimisha vivinjari kutumia HTTPS kila wakati.
---

## Uthibitishaji na Uidhinishaji
### Uthibitishaji: Wewe ni Nani?
| Mbinu | Kiwango cha Usalama | Tumia Kesi |
|--------|--------------------------|
| **Nenosiri** | Chini-Wastani | Akaunti za msingi (tekeleza herufi 12+, angalia ukiukaji) |
| **MFA (TOTP)** | Juu | Kawaida kwa akaunti nyeti (Google Authenticator, Authy) |
| **Ufunguo wa maunzi (FIDO2/WebAuthn)** | Juu Sana | Akaunti za usalama wa juu (YubiKey) |
| **Biometriska** | Kati-Juu | Kufungua kifaa (alama ya vidole, uso) — si nzuri kama kipengele pekee |
| **OAuth2 / OIDC** | Juu | Kuingia kwa wahusika wengine ("Ingia kwa kutumia Google") |
**Kanuni za nenosiri**: tekeleza urefu wa chini zaidi (herufi 12–16), angalia dhidi ya orodha za nenosiri zilizokiukwa, tumia Argon2id au bcrypt kwa hashing na chumvi kwa kila mtumiaji.
### Uidhinishaji: Unaweza Kufanya Nini?
| Mfano | Maelezo | Mfano |
|-------|-------------|----------|
| **RBAC** (Udhibiti wa Ufikiaji Unaotegemea Wajibu) | Ruhusa zilizopewa majukumu; watumiaji kupata majukumu | Msimamizi, Mhariri, Mtazamaji |
| **ABAC** (Sifa-Kulingana) | Sheria kulingana na sifa za mtumiaji, rasilimali, mazingira | "Wasimamizi wanaweza kuidhinisha maombi ya timu yao" |
| **ACL** (Orodha ya Kidhibiti cha Ufikiaji) | Ruhusa dhahiri kwa kila mtumiaji/rasilimali | Ruhusa za faili (soma/andika/tekeleze) |
**Kanuni ya upendeleo mdogo**: mpe kila mtumiaji, huduma, na uchakate ufikiaji wa chini tu anaohitaji.
### JWT (JSON Web Tokens)
| Kipengele | Pendekezo |
|--------|---------------|
| **Kusaini** | RS256 au ES256 (asymmetric) iliyopendekezwa; HS256 inakubalika kwa siri zinazosimamiwa |
| **Kuisha muda wake** | Dakika 15-60 kwa ishara za ufikiaji; tumia ishara za kuonyesha upya kwa vipindi virefu |
| **Hifadhi** | Vidakuzi vya HTTP pekee (sio Uhifadhi wa ndani - katika hatari ya XSS) |
| **Uthibitishaji** | Thibitisha kila wakati saini, mtoaji, hadhira, na mwisho wa matumizi |
---

## OWASP 10 Bora (2021)
OWASP Top 10 ndio hati ya kawaida ya uhamasishaji kwa usalama wa programu ya wavuti. Inawakilisha hatari muhimu zaidi:
| # | Hatari | Nini Maana Yake |
|---|------|--------------|
| 1 | **Udhibiti Uliovunjwa wa Ufikiaji** | Watumiaji wanaweza kufikia rasilimali ambazo hawapaswi |
| 2 | **Hitilafu za kriptografia** | Usimbaji fiche dhaifu au unaokosekana kwa data nyeti |
| 3 | **Sindano** | SQL, NoSQL, amri ya OS, au sindano ya LDAP |
| 4 | **Muundo Usio Usalama** | Makosa ya usanifu ambayo hayawezi kurekebishwa na utekelezaji |
| 5 | **Mipangilio Mibaya ya Usalama** | Nenosiri chaguo-msingi, milango wazi, ujumbe wa makosa ya kitenzi |
| 6 | **Vipengele Vinavyoweza Kuathiriwa** | CVE zinazojulikana katika utegemezi |
| 7 | **Uthibitishaji Umeshindwa** | Manenosiri dhaifu, usimamizi mbaya wa kipindi |
| 8 | **Kushindwa kwa Uadilifu** | Mashambulizi ya msururu wa ugavi, masasisho ambayo hayajasainiwa |
| 9 | **Hitilafu za Uwekaji kumbukumbu/Ufuatiliaji** | Hakuna ugunduzi wa ukiukaji |
| 10 | **SSRF** | Seva ilidanganywa kufanya maombi kwa mifumo ya ndani |
---

## Mbinu Salama za Usimbaji
### Uthibitishaji wa Ingizo
| Kanuni | Kwa nini |
|------|-----|
| **Orodha Zilizoidhinishwa > Orodha Zilizofutwa ** | Bainisha kinachoruhusiwa, sio kile ambacho kimezuiwa |
| **Maswali yaliyo na vigezo** | Kamwe usiunganishe ingizo la mtumiaji kwenye SQL - tumia taarifa zilizotayarishwa au ORM |
| **usimbaji wa HTML** | Encode`<`,`>`,`&`,`"`,`'`ili kuzuia XSS |
| **Shell inatoroka** | Epuka kujenga amri za shell kutoka kwa pembejeo ya mtumiaji; tumia`shlex.quote()`|
| **Vikomo vya urefu** | Tekeleza urefu wa juu zaidi ili kuzuia kufurika kwa bafa na DoS |
| **Aina ya kuangalia** | Hakikisha nambari kamili ni nambari kamili, booleans ni booleans |
### Athari za Kawaida
| Mazingira magumu | Mashambulizi | Ulinzi |
|----------------------------------|
| **Sindano ya SQL** | `' OR 1=1 --`katika fomu ya kuingia | Maswali yenye vigezo |
| **XSS** | `<script>alert('hacked')</script>`katika uwanja wa maoni | Usimbaji wa pato, Sera ya Usalama ya Maudhui |
| **CSRF** | Hila kivinjari cha mtumiaji kufanya ombi lisiloidhinishwa | Ishara za CSRF, vidakuzi vya SameSite |
| **Usafiri wa Njia** | `../../etc/passwd`katika kigezo cha faili | Thibitisha na usafishe njia za faili |
| **IDOR** | Badilisha`/user/123`hadi`/user/124`ili kuona data ya mtu mwingine | Uidhinishaji hukagua kila ombi |
---

## Usalama wa Mtandao
### Firewalls
| Andika | Maelezo |
|------|-------------|
| **Kuchuja pakiti** | Sheria kulingana na IP, bandari, itifaki |
| **Makini** | Inafuatilia hali za uunganisho; kuchuja kwa akili zaidi |
| **Kiwango cha maombi (WAF)** | Hukagua trafiki ya HTTP; huzuia sindano ya SQL, XSS, n.k. |
| **Vikundi vya usalama vya wingu** | Ngome za mtandaoni za matukio ya wingu (AWS SGs, Azure NSGs) |
**Kanuni ya kidole gumba**: zuia trafiki yote inayoingia kwa chaguo-msingi; fungua tu kile kinachohitajika kwa uwazi (80, 443 kwa wavuti).
### Sehemu za Mtandao
Weka hifadhidata na akiba katika subneti za kibinafsi bila ufikiaji wa moja kwa moja wa mtandao. Tumia DMZ kwa huduma zinazoangalia umma (seva za wavuti, sawazisha za mizigo). Tumia kanuni ya upendeleo mdogo kwa ufikiaji wa mtandao.
---

## Usimamizi wa Siri
### Kanuni ya Dhahabu
**Kamwe usiwahi siri za msimbo ngumu.** Hakuna funguo za API, manenosiri au URL za hifadhidata katika msimbo wa chanzo. Hakuna siri katika anuwai za mazingira zilizowekwa kwa Git. Hakuna siri katika picha za Docker.
### Zana
| Zana | Andika | Bora Kwa |
|------|------|----------|
| **HashiCorp Vault** | Meneja wa Siri za Biashara | Siri zenye nguvu, usimbaji fiche kama huduma |
| **Kidhibiti cha Siri za AWS** | Wingu-asili | Mazingira ya AWS |
| ** Vault ya Ufunguo wa Azure ** | Wingu-asili | Mazingira ya Azure |
| **SOPS** | Faili zilizosimbwa kwa njia fiche | Simba siri katika Git (kwa KMS au GPG) |
| **Siri za Docker** | Asili ya kontena | Docker Swarm (kwa K8s, zingatia Hifadhi ya Siri CSI) |
| **dotenv (.env)** | Maendeleo ya mtaa | Maendeleo pekee - kamwe katika uzalishaji au kujitolea |
### Mzunguko
Zungusha siri mara kwa mara na kiotomatiki. Ikiwa siri itafichuliwa (k.m., kujitolea kwa repo ya umma), izungushe mara moja - hata ikiwa unafikiri hakuna mtu aliyeiona.
---

## Usalama wa Utegemezi
Programu yako ni salama tu kama vile utegemezi wake dhaifu zaidi.
### Zana za Kuchanganua
| Lugha | Zana |
|----------|-------|
| **Chatu** | `safety`,`pip-audit`,`bandit`|
| **Node.js** | `npm audit`,`yarn audit`,`snyk`|
| **Kutu** | `cargo audit`|
| **Nenda** | `govulncheck`|
| **Jenerali** | `Dependabot`(GitHub),`Renovate`,`Trivy`|
### Uadilifu wa Mnyororo wa Ugavi
- Tumia faili za kufuli (`package-lock.json`,`Cargo.lock`,`go.sum`) kwa miundo inayoweza kuzaliana.
- Thibitisha hesabu za utegemezi uliopakuliwa.
- Pendelea sajili rasmi na wachapishaji walioidhinishwa.
- Sasisha sasisho ndogo / kiraka kupitia Dependabot au Ukarabati.
---

## Mzunguko wa Maisha ya Maendeleo ya Usalama (SDL)
| Awamu | Shughuli |
|-------|-----------|
| **Mafunzo** | Hakikisha wasanidi programu wanaelewa udhaifu wa kawaida |
| **Muundo wa Tishio** | Tambua vitisho vinavyowezekana wakati wa kubuni |
| **Viwango Salama vya Usimbaji** | Tekeleza kupitia linters na orodha za ukaguzi wa kanuni |
| **MWISHO** | Uchambuzi tuli wa msimbo wa chanzo (SonarQube, CodeQL) |
| **DAST** | Uchambuzi wa nguvu wa programu inayoendesha (OWASP ZAP, Burp Suite) |
| **SCA** | Uchanganuzi wa utunzi wa programu - changanua utegemezi |
| **Upimaji wa Kupenya** | Mazoezi ya mara kwa mara ya udukuzi wa maadili |
| **Fadhila ya Mdudu** | Wahimize watafiti kutoka nje kutafuta udhaifu |
| **Mpango wa Majibu ya Tukio** | Kuwa na mpango wazi wa wakati ukiukaji utagunduliwa |
---

## Orodha ya Dharura
Unaposhuku ukiukaji:
1. **Usiogope** — bali chukua hatua haraka.
2. **Tenga ** mifumo iliyoathiriwa (tenganisha mtandao ikiwa inahitajika).
3. **Hifadhi ushahidi**: kunasa kumbukumbu, utupaji kumbukumbu, picha za diski.
4. **Tambua upeo**: mifumo ipi, data ipi?
5. **Zungusha** vitambulisho na siri zote zilizoathiriwa.
6. **Rekebisha** uwezekano wa kuathirika.
7. **Waarifu** watumiaji na wadhibiti walioathiriwa ikihitajika (ndani ya muda uliowekwa kisheria).
8. **Uchunguzi wa baada ya maiti**: chanzo kikuu cha hati na vipengee vya kushughulikia ndani ya saa 24–48.