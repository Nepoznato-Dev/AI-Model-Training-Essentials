---
# Metadata
title: "Technology and Computing"
description: "Computing basics, internet, databases, cloud, security"
category: "General Reference"
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
#Teknolojia na Kompyuta
Kompyuta iko kila mahali - katika simu yako, gari lako, jokofu lako, vifaa vyako vya matibabu na miundombinu inayoendesha jamii ya kisasa. Huhitaji kuwa mtayarishaji programu ili kufaidika kutokana na kuelewa jinsi yote yanavyofanya kazi. Faili hii inashughulikia mambo ya msingi: kompyuta ni nini, jinsi mtandao unavyofanya kazi, jinsi programu inavyoundwa, na dhana zinazounda ulimwengu wa kidijitali.
> **Je, ungependa kuingia ndani zaidi?** Faili hili ni muhtasari mpana. Kwa maelezo ya kina ya mada yoyote, angalia faili maalum katika[`01_coding_and_technology/`](../01_coding_and_technology/)— ikijumuisha[database systems](../01_coding_and_technology/database_systems.md),[cloud architecture](../01_coding_and_technology/cloud_architecture.md),[networking](../01_coding_and_technology/networking_basics.md), na.
---

## Kompyuta ni nini?
Katika msingi wake, kila kompyuta - kutoka kwa smartphone hadi kompyuta kubwa - hufanya jambo lile lile: inachukua pembejeo, inasindika kulingana na maagizo (mpango), na hutoa pato. Uchawi uko kwenye kasi na kiwango.
### Usanifu wa Von Neumann
Takriban kompyuta zote za kisasa hufuata muundo huu wa kimsingi:
| Sehemu | Inafanya Nini | Analojia |
|-----------|-------------|---------|
| **CPU** (Kitengo cha Usindikaji Kati) | Inatekeleza maagizo; "ubongo" | Mpishi akifuata mapishi |
| **RAM** (Kumbukumbu) | Huhifadhi data ambayo CPU inatumia kikamilifu; kupotea wakati umeme umezimwa | Kaunta — ufikiaji wa haraka, nafasi ndogo |
| **Hifadhi** (SSD/HDD) | Huhifadhi data kabisa | Pantry - ufikiaji polepole, nafasi zaidi |
| **Ingizo/Pato** | Kibodi, kipanya, skrini, mtandao | Jinsi mpishi anavyopokea oda na kutoa chakula |
| **GPU** (Kitengo cha Kuchakata Graphics) | Kichakataji maalum cha kazi zinazofanana (graphics, AI) | Timu ya wasaidizi wote wanafanya kazi sawa kwa wakati mmoja |
**Maarifa muhimu**: RAM ni haraka lakini ni ya muda. Hifadhi ni polepole lakini ni ya kudumu. Wakati kompyuta yako "inahisi polepole," mara nyingi ni kwa sababu inaishiwa na RAM na lazima itumie uhifadhi kama kumbukumbu ya muda (kubadilishana), ambayo ni polepole zaidi.
---

## Lugha za Kupanga — Kuzungumza na Kompyuta
Lugha ya programu ni seti ya maagizo ambayo kompyuta inaweza kutekeleza. Lugha tofauti zimeundwa kwa madhumuni tofauti. Kwa ushughulikiaji wa kina wa lugha 34 za kibinafsi, angalia folda ya [`programming_languages/`](../01_coding_and_technology/programming_languages/).
| Lugha | Bora Kwa | Kwa nini Uichague |
|----------|---------|---------------|
| **Chatu** | Sayansi ya data, AI, otomatiki, viambajengo vya wavuti | Sintaksia rahisi; mfumo mkubwa wa ikolojia; nzuri kwa Kompyuta |
| **JavaScript** | Sehemu za mbele za wavuti, safu kamili (Node.js) | Inaendesha katika kila kivinjari; muhimu kwa ukuzaji wa wavuti |
| **Java** | Programu za biashara, programu za Android | Jukwaa-huru (JVM); mfumo mkubwa wa ikolojia |
| **C/C++** | Upangaji wa mifumo, michezo, iliyopachikwa | Utendaji wa juu; udhibiti wa maunzi ya moja kwa moja |
| **Kutu** | Kupanga mifumo na dhamana za usalama | Usalama wa kumbukumbu bila ukusanyaji wa takataka |
| **Nenda** | Huduma za wingu, huduma ndogo, zana za CLI | Rahisi; mwingiliano bora; mkusanyiko wa haraka |
| **SQL** | Maswali ya hifadhidata | Lugha ya kimataifa ya kufanya kazi na data |
| **TypeScript** | Programu za wavuti kwa kiwango kikubwa | JavaScript na kuangalia aina; hupata mende mapema |
---

## Jinsi Mtandao Hufanya Kazi
Mtandao sio kitu sawa na wavuti. Mtandao ni mtandao halisi - kebo, vipanga njia, seva na itifaki zinazounganisha mabilioni ya vifaa. Mtandao Wote wa Ulimwenguni ni huduma moja inayoendesha kwenye mtandao (pamoja na barua pepe, uhamisho wa faili, utiririshaji, michezo ya kubahatisha, nk).
### Safari ya Ombi la Wavuti
Unapoandika`https://www.example.com`kwenye kivinjari chako:
1. **Utafutaji wa DNS**: Kivinjari chako kinauliza seva ya DNS kutafsiri "www.example.com" katika anwani ya IP (kama 93.184.216.34).
2. **Muunganisho wa TCP**: Kifaa chako huanzisha muunganisho kwa anwani hiyo ya IP kwa kutumia TCP (itifaki inayohakikisha uwasilishaji unaotegemewa).
3. ** TLS kupeana mkono**: Ikiwa unatumia HTTPS, kivinjari chako na seva hujadili muunganisho uliosimbwa kwa njia fiche.
4. **Ombi la HTTP**: Kivinjari chako kinatuma ombi: "Nipe ukurasa katika /index.html."
5. **Uchakataji wa seva**: Seva ya wavuti hupata ukurasa, ikiwezekana huuliza hifadhidata, na hutayarisha jibu.
6. **Jibu la HTTP**: Seva hutuma tena HTML, CSS, na JavaScript.
7. **Utoaji**: Kivinjari chako huchanganua HTML, hutumia mitindo ya CSS, na kutekeleza JavaScript ili kuonyesha ukurasa.
Mchakato huu wote kwa kawaida huchukua chini ya sekunde.
### Itifaki Muhimu
| Itifaki | Inafanya Nini | Tabaka |
|----------|---------------------|
| **IP** (Itifaki ya Mtandao) | Pakiti za njia kati ya mitandao | Mtandao |
| **TCP** | Uwasilishaji wa kuaminika, ulioamuru (hutuma tena pakiti zilizopotea) | Usafiri |
| **UDP** | Uwasilishaji wa haraka, usioaminika (hakuna uhamishaji tena) | Usafiri |
| **HTTP/HTTPS** | Uhamisho wa ukurasa wa wavuti (HTTPS inaongeza usimbaji fiche) | Maombi |
| **DNS** | Inatafsiri majina ya vikoa hadi anwani za IP | Maombi |
| **SSH** | Salama ufikiaji wa mbali kwa kompyuta | Maombi |
| **SMTP/IMAP** | Kutuma na kupokea barua pepe | Maombi |
---

## Ukuzaji wa Programu - Jinsi Mipango Hujengwa
### Mchakato wa Maendeleo
1. **Andika msimbo**: Wasanidi huandika maagizo katika lugha ya programu.
2. **Msimbo wa majaribio**: Tekeleza msimbo ili uthibitishe kuwa inafanya kazi ipasavyo.
3. **Udhibiti wa toleo**: Fuatilia mabadiliko kwa kutumia Git — kiwango cha wote.
4. **Kagua**: Wasanidi programu wengine huangalia msimbo kwa hitilafu na ubora.
5. **Jenga**: Badilisha msimbo wa chanzo kuwa programu inayoendeshwa (mkusanyiko).
6. **Weka**: Toa programu kwa watumiaji (seva, maduka ya programu, n.k.).
7. **Fuatilia**: Tazama hitilafu na masuala ya utendaji katika uzalishaji.
### Dhana Muhimu
| Dhana | Nini Maana Yake | Kwa Nini Ni Muhimu |
|---------|--------------------------------|
| **Udhibiti wa toleo (Git)** | Fuatilia kila mabadiliko kwenye msimbo baada ya muda | Ushirikiano; uwezo wa kutengua makosa |
| **API** (Kiolesura cha Kuandaa Programu) | Njia iliyobainishwa ya vijenzi vya programu kuwasiliana | Huruhusu mifumo tofauti kufanya kazi pamoja |
| ** Hifadhidata** | Hifadhi iliyopangwa ya data | Kila programu inahitaji kuhifadhi na kurejesha data |
| **Majaribio** | Hukagua kiotomatiki kwamba msimbo unafanya kazi ipasavyo | Huzuia hitilafu kufikia watumiaji |
| **CI/CD** (Ushirikiano Unaoendelea/Uwasilishaji) | Bomba otomatiki kutoka ahadi ya kanuni hadi uzalishaji | Matoleo ya haraka na salama zaidi |
| **Uwekaji vyombo (Docker)** | Pakia programu na vitegemezi vyake vyote | "Hufanya kazi kwenye mashine yangu" inakuwa "inafanya kazi kila mahali" |
---

## Hifadhidata — Mahali Data Inaishi
Kila programu inahitaji kuhifadhi data. Hifadhidata ni mifumo inayofanya hivi kwa ufanisi na kwa uhakika.
| Aina | Jinsi Data Inavyohifadhiwa | Bora Kwa | Mifano |
|------|-----------------------------|---------|
| **Mahusiano (SQL)** | Majedwali yenye safu na nguzo; schema kali | Data iliyopangwa; maswali magumu; shughuli | PostgreSQL, MySQL, SQLite |
| **Hati (NoSQL)** | Hati zinazofanana na JSON; schema inayoweza kubadilika | Data ya muundo wa nusu; kurudia haraka | MongoDB, CouchDB |
| **Thamani-muhimu** | Kitufe rahisi → jozi za thamani | Kuhifadhi akiba; uhifadhi wa kikao; utafutaji wa haraka | Redis, DynamoDB |
| **Grafu** | Nodi na kingo (mahusiano) | Mitandao ya kijamii; injini za mapendekezo | Neo4j, JanusGraph |
| **Mfululizo wa saa** | Imeboreshwa kwa data iliyopigwa muhuri wa wakati | Ufuatiliaji; uchanganuzi; IoT | InfluxDB, TimescaleDB |
**SQL** (Lugha ya Maswali Iliyoundwa) ndiyo lugha sanifu ya hifadhidata za uhusiano. Ni mojawapo ya ujuzi muhimu sana wa kiufundi unaoweza kujifunza - karibu kila shirika hutumia hifadhidata, na SQL ni jinsi unavyozungumza nao.
---

## Mifumo ya Uendeshaji
Mfumo wa uendeshaji (OS) ni safu ya programu kati yako (na programu zako) na maunzi. Inasimamia kumbukumbu, michakato, faili na vifaa.
| OS | Ambapo Inatawala | Kipengele Muhimu |
|----|---------------------------------|
| **Windows** | Kompyuta za mezani/laptop (~ hisa 72% ya soko) | Utangamano mpana wa programu/vifaa |
| **macOS** | Wataalamu wa ubunifu, watengenezaji | Unix-msingi; UI iliyosafishwa; Mfumo wa ikolojia wa Apple |
| **Linux** | Seva (~96%), kompyuta kuu (100%), zilizopachikwa, wasanidi | Chanzo wazi; bure; inayoweza kubinafsishwa sana |
| **Android** | Simu ya rununu (~72% ya hisa ya soko la kimataifa) | Kulingana na Linux kernel; chanzo wazi |
| **iOS** | Simu ya mkononi (~27% kimataifa, lakini mapato ya juu) | Mfumo wa ikolojia uliofungwa; iliyosafishwa; faragha-inazingatia |
Linux inastahili kutajwa maalum: inawezesha mtandao mwingi, kila kompyuta kuu 500, miundombinu mingi ya wingu na simu zote za Android. Ni bure, chanzo wazi, na hudumishwa na jumuiya ya kimataifa.
---

## Cloud Computing
Kompyuta ya wingu inamaanisha kukodisha rasilimali za kompyuta (seva, hifadhi, hifadhidata, n.k.) kwenye mtandao badala ya kununua na kudumisha maunzi yako mwenyewe. Kwa mwongozo wa kina wa usanifu wa wingu, miundo ya huduma, na ulinganisho wa watoa huduma, angalia[cloud architecture](../01_coding_and_technology/cloud_architecture.md).
| Mfano wa Huduma | Unachopata | Analojia | Mifano |
|----------------------------|--------------------|
| **IaaS** (Miundombinu) | Seva pepe, hifadhi, mitandao | Kukodisha kiwanja na kujenga unachotaka | AWS EC2, Google Compute Engine |
| **PaaS** (Jukwaa) | Mazingira ya wakati wa kukimbia; unaleta nambari | Kukodisha nyumba iliyo na samani | Heroku, Google App Engine |
| **SaaS** (Programu) | Kukamilisha maombi; unaitumia tu | Kukaa katika hoteli | Gmail, Slack, Salesforce |
Watoa huduma wakuu watatu wa mtandao ni **AWS** (Amazon, ~32% ya hisa ya soko), **Azure** (Microsoft, ~23%), na **GCP** (Google, ~10%). Wanatoa mamia ya huduma zinazofunika hesabu, uhifadhi, hifadhidata, AI, mitandao, na zaidi.
---

## Usalama Mtandaoni - Kulinda Mifumo ya Kidijitali
Cybersecurity ni desturi ya kulinda kompyuta, mitandao na data dhidi ya mashambulizi. Ni muhimu kwa sababu kila kitu kimeunganishwa, na gharama ya uvunjaji ni kubwa sana. Kwa mwongozo kamili unaohusu 10 Bora za OWASP, mzunguko wa maisha salama wa maendeleo, na usimamizi wa siri, ona.
### Vitisho vya Kawaida
| Tishio | Ni Nini | Kinga |
|--------|-----------|------------|
| **Programu hasidi** | Programu hasidi (virusi, minyoo, trojans) | Antivirus; weka programu kusasishwa |
| **Hadaa** | Barua pepe/ujumbe ghushi unaokulaghai ili ufichue maelezo | Mafunzo; kuchuja barua pepe; mashaka |
| **Ransomware** | Husimba data yako kwa njia fiche; inadai malipo ya ufunguo | Hifadhi rudufu; mifumo ya kiraka; usilipe |
| **DDoS** | Hulemea huduma na trafiki | Uchujaji wa trafiki; Ulinzi wa CDN |
| **Sindano ya SQL** | Kuingiza SQL hasidi kwenye sehemu za ingizo | maswali ya parameterized; uthibitishaji wa pembejeo |
| **Mtu-katikati** | Kukatiza mawasiliano kati ya pande mbili | Usimbaji fiche wa HTTPS/TLS |
### Misingi ya Usalama
- **Usimbaji fiche**: Vunja data ili watu walioidhinishwa pekee waweze kuisoma. HTTPS hutumia TLS kusimba trafiki ya wavuti kwa njia fiche.
- **Uthibitishaji**: Thibitisha utambulisho. Tumia uthibitishaji wa vipengele vingi (MFA) - nenosiri + kitu kingine (msimbo, biometriska).
- **Uidhinishaji**: Thibitisha ruhusa. Kwa sababu tu umeingia haimaanishi unapaswa kufikia kila kitu.
- **Kanuni ya upendeleo mdogo zaidi**: Wape watumiaji na mifumo ufikiaji wanaohitaji tu, hakuna zaidi.
- **Udhibiti wa kiraka**: Weka programu kusasishwa. Ukiukaji mwingi hutumia udhaifu unaojulikana ambao tayari una viraka.
---

## Miundo ya Data
Programu hubadilishana data katika miundo maalum. Ya kawaida zaidi:
| Umbizo | Muundo | Inatumika Kwa |
|--------|-----------|-----------|
| **JSON** | Jozi za thamani-muhimu; inayoweza kusomeka na binadamu | API; usanidi; kubadilishana data |
| **XML** | Kulingana na lebo; kitenzi lakini kinachonyumbulika | Mifumo ya urithi; nyaraka; API za SABUNI |
| **YAML** | Uingizaji-msingi; inasomeka sana | Usanidi (Docker, Kubernetes, CI/CD) |
| **CSV** | Safu mlalo na safu wima za maandishi wazi | Kuagiza / kuuza nje data; lahajedwali |
---

## Muhtasari
Kompyuta ni uhandisi, sio uchawi. Kompyuta hufuata maagizo kwa kasi ya juu. Mtandao huunganisha mabilioni yao kwa kutumia itifaki sanifu. Programu hutengenezwa na timu za watu wanaoandika, kujaribu, na kupeleka msimbo katika mizunguko ya kurudia. Hifadhidata huhifadhi na kupata data. Kompyuta ya wingu huruhusu mtu yeyote kufikia rasilimali za kompyuta kwa mahitaji. Na usalama wa mtandao ni juhudi zinazoendelea za kulinda mifumo hii dhidi ya unyonyaji. Kuelewa mambo haya ya msingi husaidia kufahamisha maamuzi katika ulimwengu wa kidijitali - iwe kama mtumiaji, msanidi programu, au mwangalizi wa teknolojia ya kisasa.