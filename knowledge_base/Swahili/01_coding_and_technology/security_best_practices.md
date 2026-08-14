---
# Metadata
title: "Security Best Practices"
description: "OWASP Top 10, input validation, auth, secrets management"
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
tags: [security, best, practices, coding-and-technology]
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

# Mbinu Bora za Usalama
Mwongozo wa vitendo wa kupata programu, miundombinu, na data - kutoka kwa maendeleo hadi uzalishaji.
---

## OWASP 10 Bora (2021) - Muhtasari
1. **Udhibiti Uliovunjwa wa Ufikiaji**: Watumiaji wanaweza kufikia nyenzo ambazo hawapaswi kufikia.
2. **Hitilafu za Kisirisiri**: Usimbaji fiche dhaifu au unaokosekana.
3. **Sindano**: SQL, NoSQL, amri ya OS, au sindano ya LDAP.
4. **Muundo Usio Usalama**: Kasoro za Usanifu.
5. **Mipangilio Mibaya ya Usalama**: Nywila chaguo-msingi, bandari zilizo wazi, makosa ya vitenzi.
6. **Vipengele Vinavyoweza Kuathiriwa na Vilivyopitwa na Wakati**: CVE zinazojulikana katika utegemezi.
7. **Kushindwa kwa Utambulisho na Uthibitishaji**: Nywila dhaifu, usimamizi mbaya wa kipindi.
8. **Programu na Kushindwa kwa Uadilifu wa Data**: Mashambulizi ya msururu wa ugavi, masasisho ambayo hayajasainiwa.
9. **Hitilafu za Uwekaji kumbukumbu na Ufuatiliaji wa Usalama**: Hakuna ugunduzi wa uvunjaji.
10. **Ughushi wa Ombi la Upande wa Seva (SSRF)**: Matumizi mabaya ya seva kufanya maombi kwa mifumo ya ndani.
---

## Uthibitishaji wa Ingizo na Usimbaji wa Pato
### Kanuni za Uthibitishaji
- **Orodha iliyoidhinishwa > Orodha iliyokataliwa**: Bainisha ruwaza zinazoruhusiwa (k.m., regex ya barua pepe) badala ya kuzuia ruwaza mbaya zinazojulikana.
- **Vikomo vya urefu**: Tekeleza urefu wa juu zaidi ili kuzuia kufurika kwa bafa na DoS.
- **Aina ya kuangalia**: Hakikisha nambari kamili ni nambari kamili, booleans ni booleans.
- **Tumia maktaba zilizojaribiwa vyema**: Kwa barua pepe, URL, na uthibitishaji wa tarehe, tumia maktaba za kawaida (k.m.,`email-validator`katika Python,`validator.js`katika Node).
### Usimbaji wa Pato
- **HTML usimbaji**: Encode`<`,`>`,`&`,`"`,`'`ili kuzuia XSS.
- **Uwekaji vigezo vya SQL**: Usiwahi kuunganisha ingizo la mtumiaji katika hoja za SQL. Tumia hoja zilizo na vigezo (taarifa zilizotayarishwa) au ORM.
- **Shell kutoroka **: Epuka kujenga amri shell kutoka pembejeo ya mtumiaji; ikiwa haiwezi kuepukika, tumia`shlex.quote()`au sawa.
---

## Uthibitishaji na Uidhinishaji
### Usimamizi wa Nenosiri
- **Hashing**: Hifadhi manenosiri yenye algoriti kali na ya polepole ya hashing: **Argon2id** (inayopendekezwa), **bcrypt**, **scrypt**, au **PBKDF2**.
- **Kuweka chumvi**: Ongeza chumvi ya kipekee kwa kila mtumiaji.
- **Urefu wa chini zaidi**: Tekeleza angalau vibambo 12–16.
- **MFA (Uthibitishaji wa Mambo Mengi)**: Inahitaji kipengele cha pili (TOTP, SMS, ufunguo wa maunzi) kwa shughuli nyeti.
- **Kupunguza viwango**: Zuia majaribio ya nguvu-katili kwenye sehemu za mwisho za kuingia (k.m., majaribio 5 kwa kila dakika 5 kwa IP/mtumiaji).
### Usimamizi wa Kikao
- Tumia salama, HTTP-pekee, vidakuzi vya SameSite kwa ishara za kikao.
- Weka nyakati zinazofaa za kumalizika muda wake.
- Batilisha vipindi kwenye kuondoka na kubadilisha nenosiri.
- Epuka kufichua vitambulisho vya kipindi katika URL.
### OAuth2 / OIDC
- Tumia maktaba zilizoimarishwa vyema (k.m., Authlib, PyJWT, Passport.js, Spring Security).
- Thibitisha tokeni za kitambulisho vizuri (saini, mtoaji, hadhira, kumalizika kwa muda).
- Tumia vigezo vya hali ili kuzuia CSRF.
- Weka siri za mteja.
### JWT (JSON Web Tokens)
- **Ishara**: Tumia RS256 au ES256 (asymmetric) kwa usalama bora; HS256 (ulinganifu) inakubalika ikiwa siri za pamoja zitadhibitiwa vyema.
- **Thibitisha**: Thibitisha saini kila wakati, mtoaji (`iss`), hadhira (`aud`), na mwisho wa matumizi (`exp`).
- **Weka muda mfupi wa kuisha**: Dakika 15–60 kwa tokeni za ufikiaji; tumia ishara za kuonyesha upya kwa vipindi virefu.
- **Hifadhi kwa usalama**: Usiwahi kuhifadhi JWT kwenye Hifadhi ya ndani (inaweza kuathiriwa na XSS); tumia vidakuzi vya HTTP pekee badala yake.
---

## Usalama wa API
### Uthibitishaji
- Thibitisha simu za API kila wakati (isipokuwa vidokezo vya umma).
- Pendelea vitufe vya API au tokeni za OAuth2 juu ya uthibitisho wa kimsingi (ambao hutuma kitambulisho kwa kila ombi).
### Kupunguza Kiwango na Kudunda
- Weka viwango vya viwango vya kila mtumiaji na kwa-IP ili kuzuia matumizi mabaya na DoS.
- Rudisha`429 Too Many Requests`na kichwa cha `Retry-After`.
### CORS (Ushiriki wa Rasilimali Asili Mtambuka)
- Ruhusu asili mahususi pekee (kamwe usiwahi`*`katika uzalishaji).
- Thibitisha kichwa cha`Origin`kwenye upande wa seva.
### Uthibitishaji wa Ingizo
- Thibitisha vigezo vyote vya ombi, pamoja na vichwa na mwili.
- Kataa sehemu zisizotarajiwa (`"strict": true`au`additionalProperties: false`katika JSON Schema).
### HTTPS / TLS
- Tekeleza HTTPS katika uzalishaji.
- Tumia HSTS (Usalama Mkali wa Usafiri wa HTTP) ili kulazimisha vivinjari kutumia HTTPS.
- Tumia TLS 1.2 au 1.3 (zima TLS 1.0/1.1).
---

## Usimamizi wa Siri
### Kamwe Siri za Msimbo Ngumu
- Usifanye siri (funguo za API, nywila, URL za hifadhidata) ili kudhibiti chanzo.
- Tumia vigezo vya mazingira au zana za usimamizi wa siri.
### Zana
| Zana | Maelezo |
|------|-------------|
| **HashiCorp Vault** | Kiwango cha biashara, siri zinazobadilika |
| ** Kidhibiti cha Siri za AWS / Vault ya Ufunguo wa Azure / Kidhibiti cha Siri cha GCP ** | Wingu-asili |
| **SOPS** | Simba siri katika faili na uziweke (kwa KMS au GPG) |
| **Siri za Docker** | Kwa hali ya Swarm; Siri za Kubernetes (fikiria kiendesha CSI cha Hifadhi ya Siri za nje) |
### Mzunguko
- Zungusha siri na akaunti za huduma mara kwa mara.
- Otomatiki mzunguko inapowezekana.
---

## Usimamizi wa Utegemezi
### Uchanganuzi wa Athari
| Lugha/Jukwaa | Zana |
|-------------------|--------|
| **Chatu** | `safety`,`pip-audit`,`bandit`|
| **Njia** | `npm audit`,`yarn audit`,`snyk`|
| **Kutu** | `cargo audit`|
| **Nenda** | `govulncheck`|
| **Jenerali** | `Dependabot`(GitHub),`Renovate`,`Trivy`|
### Kuweka alama
- Weka vitegemezi vilivyosasishwa kwa matoleo yaliyotiwa viraka.
- Sanidi maombi ya kuvuta otomatiki kwa sasisho ndogo/kiraka.
- Kagua logi za mabadiliko kwa mabadiliko ya kuvunja.
### Uadilifu wa Mnyororo wa Ugavi
- Tumia faili za kufuli za kifurushi (`package-lock.json`,`Cargo.lock`,`go.sum`) ili kuhakikisha miundo inayoweza kuzaliana.
- Thibitisha hesabu za utegemezi uliopakuliwa.
- Pendelea sajili rasmi na uaminifu wachapishaji walioidhinishwa pekee.
---

## Usalama wa Miundombinu
### Firewalls
- Zuia milango yote inayoingia isipokuwa zile zinazohitajika waziwazi (k.m., 80, 443).
- Punguza ufikiaji wa SSH kwa safu maalum za IP (au tumia mwenyeji wa VPN/bastion).
- Tumia vikundi vya usalama (AWS) au NSGs (Azure) kwa udhibiti mzuri.
### Ugumu wa Mfumo wa Uendeshaji
- Tumia masasisho ya usalama mara kwa mara (`sudo apt upgrade`,`yum update`).
- Zima huduma zisizo za lazima na akaunti chaguo-msingi.
- Tumia fail2ban kuzuia majaribio ya nguvu ya kikatili kwenye SSH.
- Ugumu wa SSH: Lemaza kuingia kwa mizizi, tumia maandishi ya msingi-msingi, badilisha bandari chaguo-msingi (hiari).
### Sehemu za Mtandao
- Weka hifadhidata na akiba katika subnets za kibinafsi bila ufikiaji wa mtandao.
- Tumia DMZ kwa huduma zinazotazama umma.
- Tumia kanuni ya upendeleo mdogo kwa ufikiaji wa mtandao.
### Siri katika Miundombinu
- Usihifadhi kamwe siri katika anuwai za mazingira za CI/CD isipokuwa zimesimbwa.
- Tumia majukumu ya IAM ya mtoa huduma wa wingu kwa matukio ya EC2/VM badala ya vitufe vya muda mrefu.
---

## Uwekaji miti na Ufuatiliaji
### Cha Kuingia
- Matukio ya uthibitishaji (mafanikio / kushindwa).
- Maamuzi ya udhibiti wa ufikiaji (kushindwa kwa idhini).
- Vitendo vya Msimamizi (uundaji wa watumiaji, ufutaji, mabadiliko ya ruhusa).
- Mabadiliko ya schema ya Hifadhidata.
- Hitilafu za mfumo na tofauti.
- Maombi na majibu ya API (rekebisha data nyeti).
### Kipi Si cha Kuingia
- Nywila, siri, ishara, PII (Maelezo ya Kibinafsi Yanayotambulika) isipokuwa kwa haraka/kurekebishwa.
- Nambari kamili za kadi ya mkopo.
### Kutahadharisha
- Weka arifa za:
  - Ingizo nyingi zilizoshindwa (nguvu zinazowezekana za kinyama).
  - Mifumo isiyo ya kawaida ya ufikiaji (k.m., kutoka kwa maeneo mapya, saa isiyo ya kawaida).
  - Akaunti mpya za msimamizi zimeundwa.
  - Viwango vya juu vya makosa au kasi ya kusubiri.
- Tumia SIEM (Habari ya Usalama na Usimamizi wa Tukio) kwa uunganisho wa hali ya juu.
### Uhifadhi wa kumbukumbu
- Hifadhi kumbukumbu kwa angalau siku 30-90 kulingana na mahitaji ya udhibiti.
- Hifadhi kumbukumbu katika mfumo wa kati, unaoonekana wazi (k.m., ELK Stack, Splunk, Datadog).
---

## Secure Development Lifecycle (SDL)
1. **Mafunzo**: Hakikisha wasanidi programu wanaelewa udhaifu wa kawaida.
2. **Muundo wa tishio**: Tambua vitisho vinavyoweza kutokea mapema katika muundo.
3. **Linda viwango vya usimbaji**: Tekeleza kupitia linters na orodha za ukaguzi wa misimbo.
4. **SAST** (Jaribio la Usalama la Programu Isiyobadilika): Changanua msimbo wa chanzo ili uone athari za kiusalama (SonarQube, CodeQL).
5. **DAST** (Jaribio la Usalama la Programu Inayobadilika): Changanua programu zinazoendesha (OWASP ZAP, Burp Suite).
6. **SCA** (Uchambuzi wa Muundo wa Programu): Vitegemezi vya kuchanganua.
7. **Upimaji wa kupenya**: Mazoezi ya mara kwa mara ya udukuzi wa maadili.
8. **Fadhila ya hitilafu**: Wahimize watafiti kutoka nje kutafuta udhaifu kwa kuwajibika.
9. **Mpango wa majibu ya tukio**: Kuwa na mpango wazi wa wakati ukiukaji utagunduliwa.
---

## Orodha ya Dharura (Wakati Ukiukaji Unashukiwa)
1. **Usiogope** — bali tenda haraka.
2. **Tenga ** mifumo iliyoathiriwa (tenganisha mtandao ikiwa inahitajika).
3. **Hifadhi ushahidi**: Nasa kumbukumbu, utupaji kumbukumbu na picha za diski.
4. **Tambua** upeo: mifumo ipi, data ipi.
5. **Zungusha** vitambulisho na siri zote zilizoathiriwa.
6. **Rekebisha** uwezekano wa kuathirika.
7. **Waarifu** watumiaji walioathiriwa na mashirika ya udhibiti ikihitajika (ndani ya muda uliowekwa kisheria).
8. **Fanya uchunguzi wa maiti** ili kuelewa chanzo na kuboresha michakato.