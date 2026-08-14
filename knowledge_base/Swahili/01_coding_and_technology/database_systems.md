<!--
---
# Metadata
title: "Database Systems"
description: "SQL, NoSQL, design patterns, optimization"
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
tags: [database, systems, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Mifumo ya Hifadhidata
## Misingi ya Hifadhidata
### Hifadhidata ni nini?
Hifadhidata ni mkusanyiko uliopangwa wa maelezo yaliyopangwa yaliyohifadhiwa kwa njia ya kielektroniki, iliyoundwa kwa ajili ya kurejesha, kuingizwa, kusasisha na kufuta data kwa ufanisi.
### Mifumo ya Usimamizi wa Hifadhidata (DBMS)
Programu inayoingiliana na watumiaji wa mwisho, programu, na hifadhidata yenyewe ili kunasa na kuchanganua data. Mifano: MySQL, PostgreSQL, Oracle, MongoDB.
### Dhana Muhimu
- **Schema**: Muundo/mpangilio wa hifadhidata (meza, nyanja, mahusiano)
- **Mfano**: Data halisi iliyohifadhiwa kwa wakati fulani
- **Sifa za ACID**: Atomiki, Uthabiti, Kutengwa, Kudumu
- **Nadharia ya CAP**: Uthabiti, Upatikanaji, Uvumilivu wa Sehemu (chagua 2)
- **Kusawazisha**: Kupanga data ili kupunguza upungufu
- **Kupunguza hali ya kawaida**: Kuongeza upungufu ili kuboresha utendaji wa usomaji
## Hifadhidata za Uhusiano (SQL)
### Dhana za Msingi
- **Majedwali**: Safu mlalo (rekodi) na safu wima (sehemu)
- **Ufunguo Msingi**: Kitambulishi cha kipekee kwa kila safu mlalo
- **Ufunguo wa Kigeni**: Rejelea ufunguo msingi katika jedwali lingine
- **Fahasi**: Miundo ya data kuboresha kasi ya hoja
- **Maoni**: Majedwali pepe kulingana na matokeo ya hoja
- **Taratibu Zilizohifadhiwa**: Vizuizi vya msimbo wa SQL vilivyokusanywa mapema
- **Vichochezi**: Vitendo otomatiki kwenye mabadiliko ya data
### Uendeshaji wa SQL (CRUD)```sql
-- Create
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Read
SELECT * FROM users WHERE id = 1;
SELECT name, email FROM users ORDER BY name LIMIT 10;

-- Update
UPDATE users SET email = 'new@example.com' WHERE id = 1;

-- Delete
DELETE FROM users WHERE id = 1;
```

### Inajiunga
- **INER JOIN**: Hurejesha safu mlalo zinazolingana kutoka kwa majedwali yote mawili
- **KUSHOTO JIUNGE**: Safu mlalo zote kutoka kwa jedwali la kushoto, zinalingana kutoka kulia
- **KUJIUNGA KWA HAKI**: Safu mlalo zote kutoka kwa jedwali la kulia, zinazolingana kutoka kushoto
- **KUJIUNGA KAMILI KWA NJE**: Safu mlalo zote kutoka kwa jedwali zote mbili
- **KUJIUNGA NA KUPANDA**: Bidhaa ya Cartesian ya meza zote mbili
- **JIUNGE NAFSI**: Jedwali limeunganishwa lenyewe
### Fomu za Kurekebisha
- **1NF**: Thamani za atomiki, hakuna vikundi vinavyojirudia
- **2NF**: 1NF + hakuna utegemezi wa sehemu (sifa zote zisizo muhimu hutegemea ufunguo mzima wa msingi)
- **3NF**: 2NF + hakuna utegemezi wa mpito (sifa zisizo muhimu hazitegemei sifa zingine zisizo muhimu)
- **BCNF**: 3NF Imara zaidi, kila kibainishi ni ufunguo wa mgombea
- **4NF**: Hakuna tegemezi zenye thamani nyingi
- **5NF**: Hakuna utegemezi wa kujiunga
### RDBMS Maarufu
- **PostgreSQL**: Vipengee vya hali ya juu, vinavyoweza kupanuka, vinavyoendana na ACID
- **MySQL**: Inatumika sana, inasomwa haraka, programu za wavuti
- ** Oracle **: Makala ya biashara, scalability, ghali
- **Seva ya SQL**: Mfumo wa ikolojia wa Microsoft, zana zilizojumuishwa
- **SQLite**: Iliyopachikwa, isiyo na seva, nyepesi
- **MariaDB**: Uma wa MySQL, chanzo-wazi
## Hifadhidata za NoSQL
### Aina za Hifadhidata za NoSQL
#### Duka za Hati
- **Muundo**: Hati zinazofanana na JSON (BSON)
- **Kesi za Matumizi**: Usimamizi wa maudhui, katalogi, wasifu wa mtumiaji
- **Mifano**: MongoDB, CouchDB, DocumentDB
- **Mfano wa Swali** (MongoDB):```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Maduka ya Thamani Muhimu
- **Muundo**: Jozi rahisi za ufunguo-thamani
- **Tumia Kesi**: Uhifadhi, vipindi, mikokoteni ya ununuzi
- **Mifano**: Redis, DynamoDB, Riak
- **Sifa**: Uulizaji wa haraka, rahisi na mdogo
#### Maduka ya Safu-ya Familia
- **Muundo**: Safu zilizopangwa katika familia
- **Tumia Kesi**: Data kubwa, uchanganuzi, mfululizo wa saa
- **Mifano**: Cassandra, HBase, ScyllaDB
- **Sifa**: Imeboreshwa kwa uandishi, inasambazwa, inaweza kupanuka
#### Hifadhidata za Grafu
- ** Muundo **: Nodi, kingo, mali
- **Tumia Kesi**: Mitandao ya kijamii, utambuzi wa ulaghai, mapendekezo
- **Mifano**: Neo4j, Amazon Neptune, ArangoDB
- **Lugha ya Maswali**: Cypher (Neo4j), Gremlin
### Wakati wa Kutumia NoSQL
- Ratiba inayobadilika/kubadilika
- Mahitaji ya kuongeza usawa
- Kiwango cha juu cha maandishi
- Data ya daraja/kiota
- Mifumo iliyosambazwa
- Maombi ya muda halisi
## Muundo wa Hifadhidata
### Muundo wa Uhusiano wa Taasisi
- **Vyombo**: Vitu/dhana (Mteja, Bidhaa, Agizo)
- **Sifa**: Sifa za vyombo (jina, bei, tarehe)
- **Mahusiano**: Miunganisho kati ya huluki (moja-kwa-moja, moja-kwa-nyingi, nyingi-kwa-nyingi)
- **Kadinali**: Idadi ya matukio katika uhusiano
### Miundo ya Usanifu wa Schema
- **Urithi wa Jedwali Moja**: Aina zote kwenye jedwali moja na kibaguzi wa aina
- **Urithi wa Jedwali la Hatari**: Tenganisha majedwali kwa msingi na madaraja
- **Urithi wa Jedwali la Zege**: Jedwali tofauti kwa kila darasa la zege
- **Jedwali la Makutano**: Suluhisha mahusiano kati ya mengi hadi mengi
- **Majedwali ya Ukaguzi**: Fuatilia mabadiliko (yaliyoundwa_yamesasishwa, yalifutwa_sasi)
### Mikakati ya Kuorodhesha
- **B-Tree**: Chaguomsingi, maswali mbalimbali, kupanga
- **Hashi**: Utafutaji halisi wa mechi
- **Ramani ndogo**: Safu wima zenye viwango vya chini (jinsia, hali)
- **Nakala Kamili**: Uwezo wa kutafuta maandishi
- **Spatial**: Data ya kijiografia (GIS)
- **Muundo**: Safu wima nyingi zimeunganishwa
- **Inashughulikia**: Inajumuisha safu wima zote zinazohitajika kwa hoja
## Uboreshaji wa Hoja
### Mipango ya Utekelezaji
- Kuelewa jinsi hifadhidata inavyotekeleza maswali
- Kutambua vikwazo (sketi kamili za jedwali, faharisi zilizokosekana)
- Zana: ELEZA, ELEZA CHAMBUA
### Mbinu za Kuboresha
- **Matumizi ya Faharasa**: Hakikisha kuwa hoja zinatumia faharasa zinazofaa
- **Kuandika upya Hoja**: Rahisisha maswali changamano
- ** Jiunge na Uboreshaji **: Chagua aina sahihi za kujiunga na utaratibu
- ** Kugawanya **: Gawanya meza kubwa (anuwai, hashi, orodha)
- **Mionekano ya Nyenzo**: Matokeo ya hoja yaliyokokotwa mapema
- ** Uhifadhi wa Maswali **: Hifadhi matokeo ya hoja ya mara kwa mara
### Masuala ya Utendaji ya Kawaida
- **N+1 Tatizo la Hoja**: Kuleta data inayohusiana bila ufanisi
- **Fahirisi zinazokosekana**: Uchanganuzi wa jedwali kamili kwenye jedwali kubwa
- **Kuweka faharasa kupita kiasi**: Huandika polepole kwa sababu ya faharasa nyingi sana
- **Fuli Mabishano**: Shughuli zinazosubiri kufuli
- **Maswali yasiyofaa**: CHAGUA *, viungio visivyo vya lazima
## Miamala na Concurrency
### Viwango vya Kutengwa kwa Muamala
- **SOMA BILA KUJITOA**: Kutengwa kwa chini kabisa, usomaji mchafu iwezekanavyo
- **SOMA UMEJITUMA**: Data iliyojitolea pekee ndiyo inayoonekana (chaguo-msingi katika DB nyingi)
- **INAYORUDIWA KUSOMA**: Hoja sawa hurejesha matokeo yale yale ndani ya muamala
- **SERIALIZABLE**: Kutengwa kwa hali ya juu zaidi, miamala hutekelezwa kwa kufuatana
### Udhibiti wa Sarafu
- **Kufungia kwa Kukata tamaa**: Funga rasilimali kabla ya ufikiaji
- ** Kufunga kwa Matumaini **: Angalia toleo kabla ya kujitolea
- **MVCC (Udhibiti wa Ubadilishanaji wa Toleo nyingi)**: Dumisha matoleo mengi ya safu mlalo
- **Kufunga kwa Kiwango cha Safu**: Funga safu mlalo mahususi
- **Kufunga kwa Kiwango cha Jedwali**: Funga jedwali zima
### Mifuko ya mwisho
- Utegemezi wa mduara ambapo miamala hungoja kila mmoja
- Kinga: Kuagiza kwa kufuli thabiti, kuisha kwa muda, ugunduzi wa kufuli
- Azimio: Acha muamala mmoja
## Kurudia na Kuongeza
### Aina za Kurudufu
- **Bwana-Mtumwa**: Nakala moja ya msingi, iliyosomwa nyingi
- **Mwalimu-Mwalimu**: Michujo mingi, urudufishaji wa pande mbili
- **Multi-Master**: N mchujo, utatuzi wa migogoro unahitajika
- ** Urudiaji wa Mnyororo **: Urudufu wa mfuatano kupitia nodi
### Mbinu za Kuongeza
- **Kuongeza Wima**: Ongeza rasilimali za seva (CPU, RAM, uhifadhi)
- **Kuongeza Mlalo**: Ongeza seva zaidi (kugawanya, kugawanya)
- **Soma Nakala**: Pakia trafiki iliyosomwa
- **Kushiriki**: Gawanya data kwenye seva kwa ufunguo/safa/heshi
- **Shirikisho**: Imegawanywa kwa kazi/huduma
### Miundo ya Uthabiti
- **Uthabiti Wenye Nguvu**: Nodi zote huona data sawa kwa wakati mmoja
- **Uthabiti wa Hatimaye**: Nodi huungana baada ya muda
- **Uwiano wa Sababu**: Mahusiano ya sababu-athari yamehifadhiwa
- **Soma-Maandishi-Yako**: Mtumiaji huona sasisho zake mara moja
## Hifadhi nakala na Urejeshaji
### Mikakati ya Hifadhi Nakala
- **Hifadhi Kamili**: Kamilisha nakala ya hifadhidata
- ** Hifadhi Nakala ya Kuongezeka **: Mabadiliko tangu nakala rudufu ya mwisho
- **Hifadhi Nakala Tofauti**: Mabadiliko tangu hifadhi kamili ya mwisho
- ** Urejeshaji wa Pointi-in-Time **: Rejesha kwa wakati maalum
- ** Hifadhi Nakala inayoendelea **: Rudufu ya wakati halisi kwa chelezo
### Taratibu za Urejeshaji
- **RTO (Lengo la Muda wa Kuokoa)**: Muda wa juu unaokubalika wa kupumzika
- **RPO (Lengo la Urejeshaji)**: Upotevu wa juu zaidi unaokubalika wa data
- **Mpango wa Kuokoa Maafa**: Taratibu zilizoandikwa za kushindwa
- **Upimaji**: Mazoezi ya urejeshaji mara kwa mara
##Usalama
### Udhibiti wa Ufikiaji
- **Uthibitishaji**: Thibitisha utambulisho wa mtumiaji
- **Uidhinishaji**: Ruhusa za Ruzuku (RUHUSU, TITISHA)
- **Majukumu**: Ruhusa za kikundi kwa usimamizi rahisi
- **Kanuni ya Haki Angalau **: Ufikiaji wa chini unaohitajika
### Ulinzi wa Data
- **Usimbaji fiche Wakati wa Kupumzika**: Simba data iliyohifadhiwa kwa njia fiche
- **Usimbaji fiche katika Usafiri**: TLS/SSL kwa miunganisho
- **Kuficha**: Ficha data nyeti katika isiyo ya utayarishaji
- **Kuweka alama**: Badilisha data nyeti na tokeni
### Athari za Kawaida
- **Sindano ya SQL**: SQL hasidi katika ingizo la mtumiaji
- **Kuongezeka kwa Haki**: Kupata ufikiaji ambao haujaidhinishwa
- **Ukataji wa Magogo**: Fuatilia shughuli zote za hifadhidata
- **Utiifu**: Mahitaji ya GDPR, HIPAA, PCI-DSS
## Teknolojia za Hifadhidata za Kisasa
### Hifadhidata za Wingu
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: Hifadhidata ya SQL, Cosmos DB, Synapse
- **Manufaa**: Huduma inayosimamiwa, kuongeza kiotomatiki, chelezo zimejumuishwa
### Hifadhidata za NewSQL
- Kuchanganya uthabiti wa SQL na uboreshaji wa NoSQL
- **Mifano**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Sifa**: Imesambazwa, shughuli za ACID, kuongeza mlalo
### Hifadhidata za Mfululizo wa Wakati
- Imeboreshwa kwa data iliyowekwa muhuri
- **Mifano**: InfluxDB, TimescaleDB, Prometheus
- **Tumia Kesi**: IoT, ufuatiliaji, data ya kifedha
### Hifadhidata za Vekta
- Hifadhi na uulize viboreshaji vya kupachika
- **Mifano**: Pinekoni, Milvus, Weaviate, Qdrant
- **Tumia Kesi**: Utafutaji wa kimantiki, mifumo ya mapendekezo, programu za AI
### Hifadhidata za Miundo Mingi
- Kusaidia mifano nyingi za data katika mfumo mmoja
- **Mifano**: ArangoDB, OrientDB, Azure Cosmos DB
- **Faida**: Kubadilika bila hifadhidata nyingi
## ORMs na Ufikiaji wa Data
### Ramani ya Mahusiano ya Kitu
- **Kusudi**: Majedwali ya hifadhidata ya ramani kwa vitu vya programu
- **ORM Maarufu**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Mfumo wa Huluki
### Faida
- Uondoaji kutoka kwa SQL
- Aina ya usalama
- Usimamizi wa uhamiaji
- API za kujenga hoja
### Mapungufu
- Utendaji wa juu
- Maswali magumu ni magumu kuandika
- Matatizo ya hoja ya N+1
- Curve ya kujifunza
## Usimamizi wa Hifadhidata
### Majukumu ya DBA
- Ufungaji na usanidi
- Marekebisho ya utendaji
- Backup na ahueni
- Usimamizi wa usalama
- Upangaji wa uwezo
- Ufuatiliaji na tahadhari
- Usimamizi wa kiraka
### Vipimo vya Ufuatiliaji
- Muda wa kujibu swali
- Upitishaji (shughuli kwa sekunde)
- Idadi ya uunganisho
- Cache hit uwiano
- Diski I/O
- Lock kusubiri wakati
- Kuchelewa kurudia
### Kazi za Matengenezo
- **Ombwe/Changanua**: Sasisha takwimu, rudisha nafasi
- **Uundaji upya wa Faharasa**: Faharisi za utengano
- **Masasisho ya Takwimu**: Endelea kufahamisha kiboresha hoja
- **Mzunguko wa Kumbukumbu**: Dhibiti ukubwa wa faili za kumbukumbu
- **Upangaji wa Uwezo**: Tabiri ukuaji, panga uboreshaji