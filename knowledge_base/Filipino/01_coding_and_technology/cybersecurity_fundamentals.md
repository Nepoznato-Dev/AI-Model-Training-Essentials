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
# Cybersecurity Fundamentals
Ang seguridad ay isang disiplina na dapat isama sa bawat layer ng isang system mula sa simula, sa halip na idagdag bilang isang nahuling pag-iisip. Kung ang pagbuo ng isang web application, pamamahala ng imprastraktura, o pagpapadala ng isang API, ang pag-unawa sa landscape ng pagbabanta at ang mga pangunahing kaalaman sa pagtatanggol ay mahalaga.
---

## Encryption at Cryptography
### Symmetric vs Asymmetric Encryption
| Uri | Paano Ito Gumagana | Bilis | Pamamahagi ng Susing | Mga halimbawa |
|------|-------------|-------|----------------|----------|
| **Simetriko** | Parehong susi para sa pag-encrypt at pag-decryption | Mabilis | Hamon: paano ibahagi ang susi? | AES-256, ChaCha20 |
| **Asymmetric** | Public key encrypts, private key decrypts | Mas mabagal | Ang pampublikong susi ay maaaring ibahagi nang bukas | RSA, ECC (Elliptic Curve) |
Sa pagsasagawa, karamihan sa mga system ay gumagamit ng **parehong**: asymmetric encryption upang secure na makipagpalitan ng simetriko na key, pagkatapos ay simetriko na pag-encrypt para sa karamihan ng data. Ganito gumagana ang TLS/HTTPS.
### Hashing
Ang pag-hash ay isang one-way na function: kino-convert nito ang input sa isang fixed-size na string. Hindi mo ito maibabalik, ngunit ang parehong input ay palaging gumagawa ng parehong output.
| Use Case | Inirerekomendang Algorithm | Iwasan ang |
|----------|----------------------|-------|
| **Imbakan ng password** | Argon2id, bcrypt, scrypt | MD5, SHA-1, plain SHA-256 (masyadong mabilis) |
| **Integridad ng data** | SHA-256, SHA-3 | MD5 (sirang), SHA-1 (sirang) |
| **Mga digital na lagda** | Ed25519, RSA-2048+ | DSA |
### TLS/HTTPS
Ang HTTPS ay HTTP over TLS (Transport Layer Security). Nagbibigay ito ng:
- **Encryption**: Hindi mababasa ng mga eavesdropper ang data sa transit.
- **Authentication**: Pinatutunayan ng server ang pagkakakilanlan nito sa pamamagitan ng isang certificate.
- **Integridad**: Hindi mababago ang data sa pagpapadala nang walang detection.
Gumamit ng TLS 1.2 o 1.3. Huwag paganahin ang TLS 1.0 at 1.1. Paganahin ang HSTS (HTTP Strict Transport Security) upang pilitin ang mga browser na palaging gumamit ng HTTPS.
---

## Pagpapatunay at Awtorisasyon
### Pagpapatotoo: Sino Ka?
| Paraan | Antas ng Seguridad | Use Case |
|--------|--------------|----------|
| **Password** | Mababang–Katamtaman | Mga pangunahing account (ipatupad ang 12+ character, tingnan kung may mga paglabag) |
| **MFA (TOTP)** | Mataas | Karaniwan para sa mga sensitibong account (Google Authenticator, Authy) |
| **Susi ng hardware (FIDO2/WebAuthn)** | Napakataas | Mga account na may mataas na seguridad (YubiKey) |
| **Biometric** | Katamtaman–Mataas | Pag-unlock ng device (fingerprint, mukha) — hindi mahusay bilang nag-iisang kadahilanan |
| **OAuth2 / OIDC** | Mataas | Third-party na login ("Mag-sign in gamit ang Google") |
**Panuntunan ng password**: ipatupad ang pinakamababang haba (12–16 na character), suriin ang mga listahan ng nalabag na password, gamitin ang Argon2id o bcrypt para sa pag-hash gamit ang bawat user salt.
### Awtorisasyon: Ano ang Magagawa Mo?
| Modelo | Paglalarawan | Halimbawa |
|-------|-------------|---------|
| **RBAC** (Role-Based Access Control) | Mga pahintulot na itinalaga sa mga tungkulin; ang mga gumagamit ay nakakakuha ng mga tungkulin | Admin, Editor, Viewer |
| **ABAC** (Batay sa Katangian) | Mga panuntunan batay sa mga katangian ng user, mapagkukunan, kapaligiran | "Maaaring aprubahan ng mga manager ang mga kahilingan ng kanilang team" |
| **ACL** (Access Control List) | Mga tahasang pahintulot sa bawat user/resource | Mga pahintulot sa file (basahin/isulat/isagawa) |
**Principle of least privilege**: bigyan ang bawat user, serbisyo, at proseso ng minimum na access na kailangan nila.
### JWT (JSON Web Tokens)
| Aspeto | Rekomendasyon |
|--------|--------------|
| **Pagpirma** | Mas gusto ang RS256 o ES256 (asymmetric); HS256 katanggap-tanggap na may pinamamahalaang mga lihim |
| **Pag-expire** | 15–60 minuto para sa mga token ng pag-access; gumamit ng mga refresh token para sa mas mahabang session |
| **Imbakan** | HTTP-only na cookies (hindi localStorage — vulnerable sa XSS) |
| **Pagpapatunay** | Palaging i-verify ang lagda, tagapagbigay, madla, at pag-expire |
---

## Nangungunang 10 ng OWASP (2021)
Ang OWASP Top 10 ay ang karaniwang dokumento ng kamalayan para sa seguridad ng web application. Kinakatawan nito ang pinakamahalagang panganib:
| # | Panganib | Ano ang Ibig Sabihin Nito |
|---|------|--------------|
| 1 | **Sirang Access Control** | Maaaring ma-access ng mga user ang mga mapagkukunang hindi nila dapat |
| 2 | **Cryptographic Failures** | Mahina o nawawalang pag-encrypt para sa sensitibong data |
| 3 | **Iksyon** | SQL, NoSQL, OS command, o LDAP injection |
| 4 | **Hindi Secure na Disenyo** | Architectural flaws na hindi maaaring ayusin sa pagpapatupad |
| 5 | **Misconfiguration ng Seguridad** | Mga default na password, bukas na port, verbose error messages |
| 6 | **Mga Masasamang Bahagi** | Mga kilalang CVE sa mga dependency |
| 7 | **Mga Pagkabigo sa Auth** | Mga mahihinang password, maling pamamahala sa session |
| 8 | **Mga Pagkabigo sa Integridad** | Mga pag-atake sa kadena ng suplay, mga hindi napirmahang update |
| 9 | **Mga Pagkabigo sa Pag-log/Pagsubaybay** | Walang pagtuklas ng mga paglabag |
| 10 | **SSRF** | Nalinlang ang server sa paggawa ng mga kahilingan sa mga panloob na system |
---

## Mga Secure Coding Practice
### Pagpapatunay ng Input
| Panuntunan | Bakit |
|------|-----|
| **Whitelist > Blacklist** | Tukuyin kung ano ang pinapayagan, hindi kung ano ang naka-block |
| **Mga naka-parameter na query** | Huwag kailanman pagsamahin ang input ng user sa SQL — gumamit ng mga inihandang pahayag o ORM |
| **HTML encoding** | I-encode ang`<`,`>`,`&`,`"`,`'`upang maiwasan ang XSS |
| **Shell escaping** | Iwasan ang pagbuo ng mga shell command mula sa input ng user; gamitin ang`shlex.quote()`|
| **Mga limitasyon sa haba** | Ipatupad ang maximum na haba upang maiwasan ang mga buffer overflow at DoS |
| **Type checking** | Tiyaking integer ang mga integer, ang mga boolean ay mga boolean |
### Mga Karaniwang Kahinaan
| Kahinaan | Pag-atake | Depensa |
|--------------|--------|---------|
| **SQL Injection** | `' OR 1=1 --`sa login form | Mga naka-parameter na query |
| **XSS** | `<script>alert('hacked')</script>`sa field ng komento | Output encoding, Patakaran sa Seguridad ng Nilalaman |
| **CSRF** | Dayain ang browser ng user sa paggawa ng hindi awtorisadong kahilingan | Mga token ng CSRF, cookies ng SameSite |
| **Path Traversal** | `../../etc/passwd`sa parameter ng file | I-validate at i-sanitize ang mga path ng file |
| **IDOR** | Baguhin ang`/user/123`sa`/user/124`upang makita ang data ng ibang tao | Pagsusuri ng pahintulot sa bawat kahilingan |
---

## Network Security
### Mga Firewall
| Uri | Paglalarawan |
|------|-------------|
| **Packet-filter** | Mga panuntunan batay sa IP, port, protocol |
| **Mahayag** | Sinusubaybayan ang mga estado ng koneksyon; mas matalinong pag-filter |
| **Antas ng aplikasyon (WAF)** | Sinusuri ang trapiko ng HTTP; hinaharangan ang SQL injection, XSS, atbp. |
| **Mga pangkat ng seguridad sa Cloud** | Mga virtual na firewall para sa cloud instance (AWS SGs, Azure NSGs) |
**Rule of thumb**: harangan ang lahat ng papasok na trapiko bilang default; buksan lamang kung ano ang tahasang kailangan (80, 443 para sa web).
### Network Segmentation
Maglagay ng mga database at cache sa mga pribadong subnet na walang direktang internet access. Gumamit ng DMZ para sa mga serbisyong nakaharap sa publiko (mga web server, load balancer). Ilapat ang prinsipyo ng hindi bababa sa pribilehiyo sa pag-access sa network.
---

## Pamamahala ng mga Lihim
### Ang Gintong Panuntunan
**Huwag kailanman maglihim ng hardcode.** Walang mga API key, password, o database URL sa source code. Walang mga lihim sa mga variable ng kapaligiran na nakatuon sa Git. Walang mga lihim sa mga larawan ng Docker.
### Mga tool
| Tool | Uri | Pinakamahusay Para sa |
|------|------|----------|
| **HashiCorp Vault** | Tagapamahala ng mga lihim ng negosyo | Mga dinamikong lihim, pag-encrypt bilang isang serbisyo |
| **AWS Secrets Manager** | Cloud-native | AWS environment |
| **Azure Key Vault** | Cloud-native | Azure na kapaligiran |
| **SOPS** | Mga naka-encrypt na file | I-encrypt ang mga lihim sa Git (na may KMS o GPG) |
| **Mga Lihim ng Docker** | Lalagyan-katutubong | Docker Swarm (para sa mga K8, isaalang-alang ang Secrets Store CSI) |
| **dotenv (.env)** | Lokal na pag-unlad | Pag-unlad lamang — hindi kailanman sa produksyon o nakatuon |
### Pag-ikot
Paikutin ang mga lihim nang regular at awtomatiko. Kung may na-leak na lihim (hal., nakatuon sa isang pampublikong repo), i-rotate ito kaagad — kahit na sa tingin mo ay walang nakakita nito.
---

## Dependency Security
Ang iyong aplikasyon ay kasing-secure lamang ng pinakamahina nitong dependency.
### Mga Tool sa Pag-scan
| Wika | Mga tool |
|----------|-------|
| **Python** | `safety`,`pip-audit`,`bandit`|
| **Node.js** | `npm audit`,`yarn audit`,`snyk`|
| **Kalawang** | `cargo audit`|
| **Pumunta** | `govulncheck`|
| **Pangkalahatan** | `Dependabot`(GitHub),`Renovate`,`Trivy`|
### Integridad ng Supply Chain
- Gumamit ng mga lockfile (`package-lock.json`,`Cargo.lock`,`go.sum`) para sa mga reproducible build.
- I-verify ang mga checksum ng mga na-download na dependencies.
- Mas gusto ang mga opisyal na rehistro at na-verify na publisher.
- I-automate ang mga menor de edad/patch update sa pamamagitan ng Dependabot o Renovate.
---

## Security Development Lifecycle (SDL)
| Yugto | Aktibidad |
|-------|----------|
| **Pagsasanay** | Tiyaking nauunawaan ng mga developer ang mga karaniwang kahinaan |
| **Pagmomodelo ng Banta** | Tukuyin ang mga potensyal na banta sa panahon ng disenyo |
| **Mga Secure Coding Standards** | Ipatupad sa pamamagitan ng mga linter at mga checklist sa pagsusuri ng code |
| **SAST** | Static na pagsusuri ng source code (SonarQube, CodeQL) |
| **DAST** | Dynamic na pagsusuri ng tumatakbong application (OWASP ZAP, Burp Suite) |
| **SCA** | Pagsusuri ng komposisyon ng software — mga dependency sa pag-scan |
| **Pagsubok sa Pagpasok** | Mga regular na pagsasanay sa etikal na pag-hack |
| **Bug Bounty** | Hikayatin ang mga panlabas na mananaliksik na maghanap ng mga kahinaan |
| **Plano ng Pagtugon sa Insidente** | Magkaroon ng malinaw na plano para sa kapag may nakitang paglabag |
---

## Emergency Checklist
Kapag pinaghihinalaan mo ang isang paglabag:
1. **Huwag mag-panic** — ngunit kumilos kaagad.
2. **Ihiwalay** ang mga apektadong sistema (idiskonekta sa network kung kinakailangan).
3. **Panatilihin ang ebidensya**: capture logs, memory dumps, disk images.
4. **Kilalanin ang saklaw**: aling mga system, aling data?
5. **I-rotate** lahat ng nakompromisong kredensyal at sikreto.
6. **Patch** ang kahinaan.
7. **Abisuhan** ang mga apektadong user at regulator kung kinakailangan (sa loob ng mga legal na timeframe).
8. **Post-mortem**: idokumento ang ugat ng sanhi at mga item ng aksyon sa loob ng 24–48 oras.