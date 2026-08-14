---
# Metadata
title: "Technology and Computing"
description: "Computing basics, internet, databases, cloud, security"
category: "General Reference"
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
reviewed_by: "General Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, computing, general-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Teknolohiya at Computing
Ang pag-compute ay nasa lahat ng dako — sa iyong telepono, sa iyong sasakyan, sa iyong refrigerator, sa iyong mga medikal na device, at sa imprastraktura na nagpapatakbo ng modernong lipunan. Hindi mo kailangang maging isang programmer upang makinabang mula sa pag-unawa kung paano gumagana ang lahat. Sinasaklaw ng file na ito ang mga pangunahing kaalaman: kung ano ang isang computer, kung paano gumagana ang internet, kung paano binuo ang software, at ang mga konsepto na humuhubog sa digital na mundo.
> **Gustong lumalim pa?** Ang file na ito ay isang malawak na pangkalahatang-ideya. Para sa detalyadong saklaw ng anumang paksa, tingnan ang mga nakalaang file sa[`01_coding_and_technology/`](../01_coding_and_technology/)— kabilang ang[database systems](../01_coding_and_technology/database_systems.md),[cloud architecture](../01_coding_and_technology/cloud_architecture.md),[networking](../01_coding_and_technology/networking_basics.md), at.
---

## Ano ang Computer?
Sa kaibuturan nito, ang bawat computer — mula sa isang smartphone hanggang sa isang supercomputer — ay gumagawa ng parehong bagay: nangangailangan ito ng input, pinoproseso ito ayon sa mga tagubilin (isang programa), at gumagawa ng output. Ang magic ay nasa bilis at sukat.
### Ang Arkitekturang Von Neumann
Halos lahat ng modernong computer ay sumusunod sa pangunahing disenyong ito:
| Bahagi | Ano ang Ginagawa Nito | Pagkakatulad |
|-----------|-------------|---------|
| **CPU** (Central Processing Unit) | Nagsasagawa ng mga tagubilin; ang "utak" | Ang chef na sumusunod sa isang recipe |
| **RAM** (Memorya) | Nag-iimbak ng data na aktibong ginagamit ng CPU; nawala kapag patay ang kuryente | Ang countertop — mabilis na pag-access, limitadong espasyo |
| **Storage** (SSD/HDD) | Permanenteng iniimbak ang data | Ang pantry — mas mabagal na pag-access, mas maraming espasyo |
| **Input/Output** | Keyboard, mouse, screen, network | Paano tumatanggap ang chef ng mga order at naghahatid ng pagkain |
| **GPU** (Graphics Processing Unit) | Dalubhasang processor para sa magkatulad na mga gawain (graphics, AI) | Isang pangkat ng mga katulong na lahat ay gumagawa ng parehong gawain nang sabay-sabay |
**Pangunahing insight**: Ang RAM ay mabilis ngunit pansamantala. Ang imbakan ay mabagal ngunit permanente. Kapag ang iyong computer ay "mabagal," kadalasan ay dahil ito ay nauubusan ng RAM at kailangang gumamit ng storage bilang pansamantalang memorya (pagpapalit), na mas mabagal.
---

## Mga Wika sa Programming — Pakikipag-usap sa Mga Computer
Ang isang programming language ay isang set ng mga tagubilin na maaaring isagawa ng isang computer. Ang iba't ibang wika ay idinisenyo para sa iba't ibang layunin. Para sa detalyadong saklaw ng 34 na indibidwal na mga wika, tingnan ang folder na [`programming_languages/`](../01_coding_and_technology/programming_languages/).
| Wika | Pinakamahusay Para sa | Bakit Pinili Ito |
|----------|---------|--------------|
| **Python** | Data science, AI, automation, web backends | Simpleng syntax; malaking ekosistema; mahusay para sa mga nagsisimula |
| **JavaScript** | Mga frontend sa web, full-stack (Node.js) | Tumatakbo sa bawat browser; mahalaga para sa web development |
| **Java** | Enterprise software, Android app | Platform-independent (JVM); malaking ecosystem |
| **C/C++** | System programming, laro, naka-embed | Pinakamataas na pagganap; direktang kontrol ng hardware |
| **Kalawang** | System programming na may mga garantiya sa kaligtasan | Kaligtasan ng memorya nang walang koleksyon ng basura |
| **Pumunta** | Mga serbisyo sa cloud, microservice, CLI tool | Simple; mahusay na pagkakatugma; mabilis na compilation |
| **SQL** | Mga query sa database | Ang pangkalahatang wika para sa pagtatrabaho sa data |
| **TypeScript** | Malaking sukat na web application | JavaScript na may pagsuri ng uri; maagang nahuhuli ng mga bug |
---

## Paano Gumagana ang Internet
Ang internet ay hindi katulad ng web. Ang internet ay ang pisikal na network — mga cable, router, server, at protocol na kumokonekta sa bilyun-bilyong device. Ang World Wide Web ay isang serbisyo na tumatakbo sa internet (kasama ang email, file transfer, streaming, gaming, atbp.).
### Ang Paglalakbay ng isang Kahilingan sa Web
Kapag nag-type ka ng`https://www.example.com`sa iyong browser:
1. **DNS lookup**: Ang iyong browser ay humihiling sa isang DNS server na isalin ang "www.example.com" sa isang IP address (tulad ng 93.184.216.34).
2. **Koneksyon ng TCP**: Ang iyong device ay nagtatatag ng koneksyon sa IP address na iyon gamit ang TCP (isang protocol na ginagarantiyahan ang maaasahang paghahatid).
3. **TLS handshake**: Kung gumagamit ng HTTPS, ang iyong browser at ang server ay nakikipag-ayos sa isang naka-encrypt na koneksyon.
4. **HTTP request**: Nagpapadala ang iyong browser ng kahilingan: "Ibigay sa akin ang pahina sa /index.html."
5. **Pagproseso ng server**: Hinahanap ng web server ang page, posibleng mag-query ng database, at naghahanda ng tugon.
6. **Tugon sa HTTP**: Ang server ay nagpapadala ng HTML, CSS, at JavaScript.
7. **Rendering**: Pina-parse ng iyong browser ang HTML, inilalapat ang mga istilo ng CSS, at pinapagana ang JavaScript upang ipakita ang pahina.
Ang buong prosesong ito ay karaniwang tumatagal ng mas mababa sa isang segundo.
### Mga Pangunahing Protokol
| Protocol | Ano ang Ginagawa Nito | Layer |
|----------|-------------|-------|
| **IP** (Internet Protocol) | Mga ruta ng packet sa pagitan ng mga network | Network |
| **TCP** | Maaasahan, iniutos na paghahatid (muling ipinapadala ang mga nawawalang packet) | Transportasyon |
| **UDP** | Mabilis, hindi maaasahang paghahatid (walang muling pagpapadala) | Transportasyon |
| **HTTP/HTTPS** | Paglipat ng web page (nagdaragdag ng encryption ang HTTPS) | Application |
| **DNS** | Nagsasalin ng mga domain name sa mga IP address | Application |
| **SSH** | Secure remote access sa mga computer | Application |
| **SMTP/IMAP** | Pagpapadala at pagtanggap ng email | Application |
---

## Software Development — Paano Nabubuo ang Mga Programa
### Ang Proseso ng Pag-unlad
1. **Write code**: Nagsusulat ang mga developer ng mga tagubilin sa isang programming language.
2. **Test code**: Patakbuhin ang code para ma-verify na gumagana ito nang tama.
3. **Version control**: Subaybayan ang mga pagbabago gamit ang Git — ang pangkalahatang pamantayan.
4. **Review**: Sinusuri ng ibang mga developer ang code para sa mga error at kalidad.
5. **Build**: I-convert ang source code sa isang runnable program (compilation).
6. **Deploy**: I-release ang program sa mga user (server, app store, atbp.).
7. **Monitor**: Panoorin ang mga error at mga isyu sa pagganap sa produksyon.
### Mga Pangunahing Konsepto
| Konsepto | Ano ang Ibig Sabihin Nito | Bakit Mahalaga |
|---------|----------------|----------------|
| **Control ng bersyon (Git)** | Subaybayan ang bawat pagbabago sa code sa paglipas ng panahon | Pakikipagtulungan; kakayahang i-undo ang mga pagkakamali |
| **API** (Application Programming Interface) | Isang tinukoy na paraan para sa mga bahagi ng software upang makipag-usap | Nagbibigay-daan sa iba't ibang mga system na gumana nang magkasama |
| **Database** | Organisadong storage para sa data | Ang bawat application ay kailangang mag-imbak at kumuha ng data |
| **Pagsubok** | Automated check na gumagana nang tama ang code | Pinipigilan ang mga bug na maabot ang mga user |
| **CI/CD** (Patuloy na Pagsasama/Paghahatid) | Automated pipeline mula sa code commit to production | Mas mabilis, mas ligtas na mga release |
| **Containerization (Docker)** | I-package ang isang application kasama ang lahat ng dependencies nito | Ang "Works on my machine" ay nagiging "works everywhere" |
---

## Mga Database — Kung Saan Nakatira ang Data
Ang bawat application ay kailangang mag-imbak ng data. Ang mga database ay ang mga system na gumagawa nito nang mahusay at mapagkakatiwalaan.
| Uri | Paano Iniimbak ang Data | Pinakamahusay Para sa | Mga halimbawa |
|------|--------------------|----------|---------|
| **Relational (SQL)** | Mga talahanayan na may mga hilera at haligi; mahigpit na schema | Nakabalangkas na data; kumplikadong mga katanungan; mga transaksyon | PostgreSQL, MySQL, SQLite |
| **Dokumento (NoSQL)** | Mga dokumentong tulad ng JSON; nababaluktot na schema | Semi-structured na data; mabilis na pag-ulit | MongoDB, CouchDB |
| **Susi-halaga** | Simpleng key → mga pares ng halaga | Pag-cache; imbakan ng session; mabilis na paghahanap | Redis, DynamoDB |
| **Graph** | Mga node at gilid (mga relasyon) | Mga social network; mga engine ng rekomendasyon | Neo4j, JanusGraph |
| **Time-serye** | Na-optimize para sa time-stamped data | Pagsubaybay; pagsusuri; IoT | InfluxDB, TimescaleDB |
**SQL** (Structured Query Language) ay ang karaniwang wika para sa mga relational database. Ito ay isa sa pinakamahalagang teknikal na kasanayan na maaari mong matutunan — halos lahat ng organisasyon ay gumagamit ng mga database, at ang SQL ay kung paano ka nakikipag-usap sa kanila.
---

## Mga Operating System
Ang operating system (OS) ay ang software layer sa pagitan mo (at ng iyong mga program) at ng hardware. Pinamamahalaan nito ang memorya, mga proseso, mga file, at mga device.
| OS | Kung Saan Ito Nangibabaw | Pangunahing Tampok |
|----|--------------------|-------------|
| **Windows** | Mga desktop/laptop PC (~72% market share) | Pinakamalawak na software/hardware compatibility |
| **macOS** | Mga malikhaing propesyonal, mga developer | Nakabatay sa Unix; pinakintab na UI; Apple ecosystem |
| **Linux** | Mga server (~96%), supercomputer (100%), naka-embed, mga developer | Open source; libre; lubhang napapasadyang |
| **Android** | Mobile (~72% global market share) | Batay sa Linux kernel; open source |
| **iOS** | Mobile (~27% global, ngunit mas mataas na kita) | Saradong ecosystem; pinakintab; nakatuon sa privacy |
Nararapat sa Linux ang espesyal na pagbanggit: pinapagana nito ang karamihan sa internet, bawat top-500 supercomputer, karamihan sa imprastraktura ng cloud, at lahat ng Android phone. Ito ay libre, open source, at pinananatili ng isang pandaigdigang komunidad.
---

## Cloud Computing
Ang ibig sabihin ng cloud computing ay pagrenta ng mga mapagkukunan ng computing (server, storage, database, atbp.) sa internet sa halip na bumili at magpanatili ng iyong sariling hardware. Para sa isang komprehensibong gabay sa cloud architecture, mga modelo ng serbisyo, at paghahambing ng provider, tingnan ang[cloud architecture](../01_coding_and_technology/cloud_architecture.md).
| Modelo ng Serbisyo | Ano ang Makukuha Mo | Pagkakatulad | Mga halimbawa |
|--------------|-------------|---------|---------|
| **IaaS** (Imprastraktura) | Mga virtual na server, imbakan, networking | Pag-upa ng kapirasong lupa at pagtatayo ng gusto mo | AWS EC2, Google Compute Engine |
| **PaaS** (Platform) | kapaligiran ng runtime; magdala ka ng code | Pag-upa ng apartment na inayos | Heroku, Google App Engine |
| **SaaS** (Software) | Kumpletuhin ang aplikasyon; gamitin mo lang | Pananatili sa isang hotel | Gmail, Slack, Salesforce |
Ang tatlong pangunahing cloud provider ay **AWS** (Amazon, ~32% market share), **Azure** (Microsoft, ~23%), at **GCP** (Google, ~10%). Nag-aalok sila ng daan-daang serbisyo na sumasaklaw sa compute, storage, database, AI, networking, at higit pa.
---

## Cybersecurity — Pagprotekta sa Digital System
Ang cybersecurity ay ang kasanayan ng pagtatanggol sa mga computer, network, at data mula sa pag-atake. Mahalaga ito dahil ang lahat ay konektado, at ang halaga ng mga paglabag ay napakalaki. Para sa buong gabay na sumasaklaw sa OWASP Top 10, secure na development lifecycle, at pamamahala ng mga lihim, tingnan.
### Mga Karaniwang Banta
| Banta | Ano Ito | Pag-iwas |
|--------|-----------|------------|
| **Malware** | Nakakahamak na software (mga virus, worm, trojan) | Antivirus; panatilihing na-update ang software |
| **Phishing** | Mga pekeng email/mensahe na nanlilinlang sa iyo sa pagbubunyag ng impormasyon | Pagsasanay; pag-filter ng email; pag-aalinlangan |
| **Ransomware** | Ine-encrypt ang iyong data; humihingi ng bayad para sa susi | Mga backup; mga sistema ng patch; huwag magbayad |
| **DDoS** | Nilulusob ang isang serbisyo sa trapiko | Pag-filter ng trapiko; Proteksyon ng CDN |
| **SQL injection** | Ang pagpasok ng malisyosong SQL sa mga input field | Mga naka-parameter na query; pagpapatunay ng input |
| **Man-in-the-middle** | Pagharang sa komunikasyon sa pagitan ng dalawang partido | Pag-encrypt ng HTTPS/TLS |
### Mga Pangunahing Pangseguridad
- **Encryption**: Scramble data para ang mga awtorisadong partido lang ang makakabasa nito. Gumagamit ang HTTPS ng TLS para i-encrypt ang trapiko sa web.
- **Authentication**: I-verify ang pagkakakilanlan. Gumamit ng multi-factor authentication (MFA) — password + iba pa (code, biometric).
- **Awtorisasyon**: I-verify ang mga pahintulot. Dahil lamang na naka-log in ka ay hindi nangangahulugan na dapat mong i-access ang lahat.
- **Principle of least privilege**: Bigyan ang mga user at system ng access lang na kailangan nila, wala nang iba pa.
- **Patch management**: Panatilihing na-update ang software. Karamihan sa mga paglabag ay nagsasamantala sa mga kilalang kahinaan na mayroon nang mga patch.
---

## Mga Format ng Data
Ang mga programa ay nagpapalitan ng data sa mga partikular na format. Ang pinakakaraniwan:
| Format | Istraktura | Ginamit Para sa |
|--------|-----------|----------|
| **JSON** | Key-value pairs; nababasa ng tao | Mga API; pagsasaayos; pagpapalitan ng data |
| **XML** | Nakabatay sa tag; verbose ngunit nababaluktot | Mga legacy system; mga dokumento; Mga SOAP API |
| **YAML** | Nakabatay sa indentation; napaka nababasa | Configuration (Docker, Kubernetes, CI/CD) |
| **CSV** | Mga row at column ng plain text | Pag-import/pag-export ng data; mga spreadsheet |
---

## Buod
Ang computing ay engineering, hindi magic. Ang mga computer ay sumusunod sa mga tagubilin sa mataas na bilis. Ang internet ay nag-uugnay sa bilyun-bilyon sa kanila gamit ang mga standardized na protocol. Ang software ay binuo ng mga pangkat ng mga taong sumusulat, sumusubok, at nagde-deploy ng code sa mga umuulit na cycle. Ang mga database ay nag-iimbak at kumukuha ng data. Hinahayaan ng cloud computing ang sinuman na ma-access ang malakihang mapagkukunan ng computing kapag hinihiling. At ang cybersecurity ay ang patuloy na pagsisikap na protektahan ang mga sistemang ito mula sa pagsasamantala. Ang pag-unawa sa mga pangunahing kaalaman na ito ay nakakatulong na magbigay ng kaalaman sa mga desisyon sa digital world — bilang user man, developer, o tagamasid ng modernong teknolohiya.