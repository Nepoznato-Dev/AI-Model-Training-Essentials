<!--
---
# Metadata
title: "Security Best Practices"
description: "OWASP Top 10, input validation, auth, secrets management"
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

-->
# Pinakamahusay na Kasanayan sa Seguridad
Isang praktikal na gabay sa pag-secure ng mga application, imprastraktura, at data — mula sa pag-unlad hanggang sa produksyon.
---

## Nangungunang 10 ng OWASP (2021) — Pangkalahatang-ideya
1. **Broken Access Control**: Maa-access ng mga user ang mga mapagkukunang hindi nila dapat.
2. **Cryptographic Failures**: Mahina o nawawalang encryption.
3. **Injection**: SQL, NoSQL, OS command, o LDAP injection.
4. **Insecure Design**: Mga depekto sa arkitektura.
5. **Security Misconfiguration**: Mga default na password, bukas na port, verbose error.
6. **Vulnerable at Outdated na Mga Bahagi**: Mga kilalang CVE sa mga dependency.
7. **Mga Pagkabigo sa Pagkilala at Pagpapatunay**: Mahina ang mga password, maling pamamahala sa session.
8. **Mga Pagkabigo sa Integridad ng Software at Data**: Mga pag-atake sa supply chain, hindi napirmahang mga update.
9. **Mga Pagkabigo sa Pag-log sa Seguridad at Pagsubaybay**: Walang pagtuklas ng mga paglabag.
10. **Server-Side Request Forgery (SSRF)**: Pang-aabuso sa server upang gumawa ng mga kahilingan sa mga panloob na system.
---

## Input Validation at Output Encoding
### Mga Panuntunan sa Pagpapatunay
- **Whitelist > Blacklist**: Tukuyin ang mga pinapayagang pattern (hal., regex para sa email) sa halip na i-block ang mga kilalang hindi magandang pattern.
- **Mga limitasyon sa haba**: Magpatupad ng mga maximum na haba upang maiwasan ang mga buffer overflow at DoS.
- **Type checking**: Tiyaking integer ang mga integer, mga boolean ang mga boolean.
- **Gumamit ng mga mahusay na nasubok na aklatan**: Para sa email, URL, at pagpapatunay ng petsa, gumamit ng mga karaniwang aklatan (hal.,`email-validator`sa Python,`validator.js`sa Node).
### Output Encoding
- **HTML encoding**: I-encode ang`<`,`>`,`&`,`"`,`'`upang maiwasan ang XSS.
- **SQL parameterization**: Huwag kailanman pagsamahin ang input ng user sa mga query sa SQL. Gumamit ng mga naka-parameter na query (mga inihandang pahayag) o isang ORM.
- **Shell escaping**: Iwasan ang pagbuo ng mga shell command mula sa user input; kung hindi maiiwasan, gumamit ng`shlex.quote()`o katulad nito.
---

## Pagpapatunay at Awtorisasyon
### Pamamahala ng Password
- **Hashing**: Mag-imbak ng mga password na may malakas, mabagal na algorithm ng pag-hash: **Argon2id** (ginustong), **bcrypt**, **scrypt**, o **PBKDF2**.
- **Pag-aasin**: Magdagdag ng kakaibang asin bawat user.
- **Minimum na haba**: Ipatupad ang hindi bababa sa 12–16 na character.
- **MFA (Multi-Factor Authentication)**: Nangangailangan ng pangalawang salik (TOTP, SMS, hardware key) para sa mga sensitibong operasyon.
- **Paglilimita sa rate**: Pigilan ang mga malupit na pagtatangka sa mga endpoint sa pag-login (hal., 5 pagtatangka bawat 5 minuto bawat IP/user).
### Pamamahala ng Session
- Gumamit ng secure, HTTP-only, SameSite cookies para sa mga token ng session.
- Itakda ang naaangkop na mga oras ng pag-expire.
- I-invalidate ang mga session sa pag-logout at sa pagpapalit ng password.
- Iwasang ilantad ang mga session ID sa mga URL.
### OAuth2 / OIDC
- Gumamit ng mga mahusay na naitatag na aklatan (hal., Authlib, PyJWT, Passport.js, Spring Security).
- I-validate nang lubusan ang mga token ng ID (pirma, issuer, audience, expiration).
- Gumamit ng mga parameter ng estado upang maiwasan ang CSRF.
- Panatilihing kumpidensyal ang mga lihim ng kliyente.
### JWT (JSON Web Tokens)
- **Sign**: Gamitin ang RS256 o ES256 (asymmetric) para sa mas mahusay na seguridad; Ang HS256 (symmetric) ay katanggap-tanggap kung ang mga nakabahaging lihim ay maayos na pinamamahalaan.
- **Patunayan**: Palaging i-verify ang lagda, tagabigay (`iss`), audience (`aud`), at expiration (`exp`).
- **Panatilihin ang maikling expiration**: 15–60 minuto para sa mga token ng access; gumamit ng mga refresh token para sa mas mahabang session.
- **Mag-imbak nang ligtas**: Huwag kailanman mag-imbak ng mga JWT sa localStorage (mahina sa XSS); gumamit na lang ng HTTP-only na cookies.
---

## Seguridad ng API
### Pagpapatotoo
- Palaging i-authenticate ang mga tawag sa API (maliban sa mga pampublikong endpoint).
- Mas gusto ang mga API key o OAuth2 token kaysa sa pangunahing auth (na nagpapadala ng mga kredensyal sa bawat kahilingan).
### Paglilimita at Pag-thrott ng Rate
- Ilapat ang mga limitasyon sa bawat user at per-IP rate upang maiwasan ang pang-aabuso at DoS.
- Ibalik ang`429 Too Many Requests`na may`Retry-After`na header.
### CORS (Cross-Origin Resource Sharing)
- Pahintulutan lamang ang mga partikular na pinagmulan (hindi kailanman`*`sa produksyon).
- I-validate ang`Origin`header sa gilid ng server.
### Pagpapatunay ng Input
- I-validate ang lahat ng mga parameter ng kahilingan, kabilang ang mga header at body.
- Tanggihan ang mga hindi inaasahang field (`"strict": true`o`additionalProperties: false`sa JSON Schema).
### HTTPS / TLS
- Ipatupad ang HTTPS sa produksyon.
- Gumamit ng HSTS (HTTP Strict Transport Security) upang pilitin ang mga browser na gumamit ng HTTPS.
- Gumamit ng TLS 1.2 o 1.3 (huwag paganahin ang TLS 1.0/1.1).
---

## Pamamahala ng mga Lihim
### Huwag kailanman Hardcode Secrets
- Huwag gumawa ng mga lihim (API key, password, database URL) sa source control.
- Gumamit ng mga variable ng kapaligiran o mga tool sa lihim na pamamahala.
### Mga tool
| Tool | Paglalarawan |
|------|-------------|
| **HashiCorp Vault** | Enterprise-grade, dynamic na mga lihim |
| **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager** | Cloud-native |
| **SOPS** | I-encrypt ang mga lihim sa mga file at i-commit ang mga ito (sa KMS o GPG) |
| **Mga lihim ng Docker** | Para sa Swarm mode; Mga lihim ng Kubernetes (isaalang-alang ang panlabas na driver ng CSI ng Secrets Store) |
### Pag-ikot
- Regular na iikot ang mga lihim at account ng serbisyo.
- I-automate ang pag-ikot kung posible.
---

## Pamamahala ng Dependency
### Pag-scan ng Kahinaan
| Wika/Platform | Mga tool |
|-------------------|-------|
| **Python** | `safety`,`pip-audit`,`bandit`|
| **Node** | `npm audit`,`yarn audit`,`snyk`|
| **Kalawang** | `cargo audit`|
| **Pumunta** | `govulncheck`|
| **Pangkalahatan** | `Dependabot`(GitHub),`Renovate`,`Trivy`|
### Patching
- Panatilihing na-update ang mga dependency sa mga naka-patch na bersyon.
- I-set up ang mga automated na pull request para sa minor/patch update.
- Suriin ang mga changelog para sa paglabag sa mga pagbabago.
### Integridad ng Supply Chain
- Gumamit ng mga package lockfiles (`package-lock.json`,`Cargo.lock`,`go.sum`) upang matiyak na maaaring kopyahin ang mga build.
- I-verify ang mga checksum ng mga na-download na dependencies.
- Mas gusto ang mga opisyal na rehistro at magtiwala lamang sa mga na-verify na publisher.
---

## Seguridad sa Imprastraktura
### Mga Firewall
- I-block ang lahat ng papasok na port maliban sa mga tahasang kailangan (hal., 80, 443).
- Limitahan ang SSH access sa mga partikular na saklaw ng IP (o gumamit ng VPN/bastion host).
- Gumamit ng mga security group (AWS) o NSG (Azure) para sa pinong kontrol.
### Pagpapatigas ng OS
- Regular na ilapat ang mga update sa seguridad (`sudo apt upgrade`,`yum update`).
- Huwag paganahin ang mga hindi kinakailangang serbisyo at default na account.
- Gumamit ng fail2ban upang harangan ang mga pagtatangka ng brute-force sa SSH.
- Patigasin ang SSH: huwag paganahin ang root login, gumamit ng key-based na auth, baguhin ang default na port (opsyonal).
### Network Segmentation
- Maglagay ng mga database at cache sa mga pribadong subnet na walang internet access.
- Gumamit ng DMZ para sa mga serbisyong nakaharap sa publiko.
- Ilapat ang prinsipyo ng hindi bababa sa pribilehiyo sa pag-access sa network.
### Mga Lihim sa Imprastraktura
- Huwag kailanman mag-imbak ng mga lihim sa mga variable ng kapaligiran ng CI/CD maliban kung naka-encrypt.
- Gamitin ang mga tungkulin ng IAM ng cloud provider para sa mga EC2/VM instance sa halip na mga long-lived key.
---

## Pag-log at Pagsubaybay
### Ano ang I-log
- Mga kaganapan sa pagpapatunay (tagumpay/kabigo).
- Mga desisyon sa kontrol sa pag-access (mga pagkabigo sa pahintulot).
- Mga aksyon ng admin (paglikha ng user, pagtanggal, mga pagbabago sa pahintulot).
- Mga pagbabago sa schema ng database.
- Mga error sa system at mga pagbubukod.
- Mga kahilingan at tugon ng API (i-redact ang sensitibong data).
### Ano ang Hindi Dapat I-log
- Mga password, sikreto, token, PII (Personal Identifiable Information) maliban kung na-hash/na-redact.
- Buong mga numero ng credit card.
### Nag-aalerto
- Mag-set up ng mga alerto para sa:
  - Maramihang nabigong pag-login (potensyal na brute force).
  - Mga hindi pangkaraniwang pattern ng pag-access (hal., mula sa mga bagong lokasyon, sa mga kakaibang oras).
  - Nagawa ang mga bagong admin account.
  - Mataas na rate ng error o latency spike.
- Gumamit ng SIEM (Security Information and Event Management) para sa advanced na ugnayan.
### Pagpapanatili ng Log
- Panatilihin ang mga log nang hindi bababa sa 30–90 araw depende sa mga kinakailangan sa regulasyon.
- Mag-imbak ng mga log sa isang sentralisadong, tamper-evident system (hal., ELK Stack, Splunk, Datadog).
---

## Secure Development Lifecycle (SDL)
1. **Pagsasanay**: Tiyaking nauunawaan ng mga developer ang mga karaniwang kahinaan.
2. **Pagmomodelo ng pagbabanta**: Kilalanin ang mga potensyal na banta nang maaga sa disenyo.
3. **Secure coding standards**: Ipatupad sa pamamagitan ng mga linter at mga checklist sa pagsusuri ng code.
4. **SAST** (Static Application Security Testing): I-scan ang source code para sa mga kahinaan (SonarQube, CodeQL).
5. **DAST** (Dynamic Application Security Testing): I-scan ang mga tumatakbong application (OWASP ZAP, Burp Suite).
6. **SCA** (Software Composition Analysis): I-scan ang mga dependency.
7. **Pagsusuri sa pagtagos**: Mga regular na pagsasanay sa etikal na pag-hack.
8. **Bug bounty**: Hikayatin ang mga panlabas na mananaliksik na maghanap ng mga kahinaan nang responsable.
9. **Plano ng pagtugon sa insidente**: Magkaroon ng malinaw na plano kung may nakitang paglabag.
---

## Emergency Checklist (Kapag May Paghihinalaang Paglabag)
1. **Huwag mag-panic** — ngunit kumilos kaagad.
2. **Ihiwalay** ang mga apektadong system (idiskonekta sa network kung kinakailangan).
3. **Panatilihin ang ebidensya**: Kumuha ng mga log, memory dump, at mga imahe sa disk.
4. **Kilalanin** ang saklaw: aling mga system, aling data.
5. **I-rotate** lahat ng nakompromisong kredensyal at sikreto.
6. **Patch** ang kahinaan.
7. **Abisuhan** ang mga apektadong user at regulatory body kung kinakailangan (sa loob ng mga legal na timeframe).
8. **Magsagawa ng post-mortem** upang maunawaan ang ugat ng sanhi at mapabuti ang mga proseso.