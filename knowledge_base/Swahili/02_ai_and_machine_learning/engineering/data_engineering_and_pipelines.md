---
# Metadata
title: "Data Engineering and Pipelines"
description: "ETL/ELT, data lakes, orchestration, Kafka, feature stores"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to engineering/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, engineering, pipelines, ai-and-machine-learning]
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

# Uhandisi wa Data na Mabomba
Uhandisi wa data ni taaluma ya kujenga mifumo inayosonga, kubadilisha na kuhifadhi data kwa kiwango. Bila mabomba ya data ya kuaminika, miundo ya kujifunza kwa mashine haiwezi kufunzwa, dashibodi zinaonyesha nambari za zamani, na maamuzi ya biashara yanatokana na kubahatisha. Faili hii inashughulikia usanifu, zana, na mbinu za kujenga miundombinu ya data inayofanya kazi.
---

## ETL dhidi ya ELT
| Mbinu | Jinsi Inavyofanya Kazi | Bora Kwa | Zana |
|----------|-----------------------|--------|
| **ETL** (Dondoo → Badilisha → Mzigo) | Badilisha data *kabla* ya kupakia kwenye ghala | Ghala za kitamaduni zilizo na kompyuta ndogo | Informatica, Talend, Apache NiFi |
| **ELT** (Dondoo → Pakia → Badilisha) | Pakia data mbichi kwanza; badilisha *ndani* ya ghala | Maghala ya kisasa ya wingu na compute elastic | dbt, Fivetran, Airbyte + BigQuery/Snowflake |
Kuhama kutoka ETL hadi ELT kumeendeshwa na ghala za data za wingu (BigQuery, Snowflake, Redshift) ambazo zinaweza kukokotoa bila hifadhi. Hakuna tena haja ya kuchakata kila kitu mapema kabla ya kupakia.
---

## Maziwa ya Data dhidi ya Maghala ya Data
| Kipengele | Ziwa la Data | Ghala la Data |
|---------|-----------|---------------|
| **Muundo wa Data** | Mbichi, umbizo asili (schema-on-read) | Imeundwa, imechakatwa (schema-on-write) |
| **Schema** | Imefafanuliwa kwa wakati wa hoja | Imefafanuliwa kabla ya kupakia |
| **Aina za Data** | Imeundwa, nusu-muundo, isiyo na muundo | Iliyoundwa kimsingi |
| **Watumiaji** | Wanasayansi wa data, wahandisi | Wachambuzi wa biashara, zana za BI |
| **Gharama** | Uhifadhi wa bei nafuu (uhifadhi wa kitu) | Ghali zaidi (imeboreshwa kwa maswali) |
| **Mifano** | AWS S3, Azure Data Lake, GCS | Snowflake, BigQuery, Redshift |
Mbinu ya kisasa ni **nyumba ya ziwa**: changanya uhifadhi wa bei nafuu, unaonyumbulika wa ziwa na sifa za usimamizi na utendaji wa ghala. Delta Lake, Apache Iceberg, na Apache Hudi ndizo teknolojia kuu hapa.
---

## Usanifu wa Bomba
### Kundi dhidi ya Kutiririsha
| Hali | Maelezo | Kuchelewa | Tumia Kesi |
|------|-------------|---------|----------|
| **Bechi** | Mchakato wa data katika vipande vikubwa kwa vipindi vilivyoratibiwa | Dakika hadi saa | Ripoti za kila siku, kazi za ETL, uboreshaji wa data |
| **Inatiririsha** | Mchakato wa data kwa kuendelea inapofika | Milisekunde kwa sekunde | Dashibodi za wakati halisi, utambuzi wa ulaghai, arifa |
| **Bechi ndogo** | Vikundi vidogo kwa vipindi vifupi sana | Sekunde | Karibu na muda halisi na unyenyekevu wa kundi |
### Vipengele vya Bomba
Bomba la kawaida la data lina hatua hizi:
| Jukwaa | Maelezo | Zana |
|-------|-------------|--------|
| **Kumeza** | Kusanya data kutoka kwa vyanzo | Kafka, Airbyte, Fivetran, Debezium |
| **Mabadiliko** | Safi, boresha, kusanya | dbt, Spark, Panda |
| **Hifadhi** | Endelea data iliyochakatwa | BigQuery, Snowflake, S3, Delta Lake |
| **Inahudumia** | Fanya data ipatikane kwa watumiaji | API, dashibodi, maduka ya vipengele vya ML |
| **Ochestration** | Ratibu na udhibiti vitegemezi | Mtiririko wa hewa, Prefect, Dagster |
| **Ufuatiliaji** | Fuatilia afya ya bomba na ubora wa data | Matarajio Mazuri, Monte Carlo, arifa maalum |
---

## Zana za Ochestration
| Zana | Mbinu | Nguvu |
|------|----------------------|
| **Apache Airflow** | Python-based DAGs; kiwango cha sekta | Mfumo mkubwa wa ikolojia, uliokomaa, unaonyumbulika |
| **Mkuu** | Python-asili; API safi kuliko Airflow | Muundo wa kisasa, ushughulikiaji wa makosa makubwa |
| **Dagster** | Asset-centric; mbinu ya uhandisi wa programu | Aina ya mfumo, upimaji, uangalizi |
| **Luigi** | Zana halisi ya bomba la Spotify | Rahisi, lakini haijaendelezwa kikamilifu |
### Mfano wa mtiririko wa hewa
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    # Pull data from source
    pass

def transform():
    # Clean and process
    pass

def load():
    # Write to warehouse
    pass

with DAG("etl_pipeline", start_date=datetime(2024, 1, 1),
         schedule="@daily", catchup=False) as dag:
    e = PythonOperator(task_id="extract", python_callable=extract)
    t = PythonOperator(task_id="transform", python_callable=transform)
    l = PythonOperator(task_id="load", python_callable=load)
    
    e >> t >> l  # Define dependencies
```

---

## Apache Kafka
Kafka ndio uti wa mgongo wa mifumo mingi ya data ya wakati halisi. Ni kumbukumbu ya matukio iliyosambazwa ambayo hutoa ujumbe wa hali ya juu, unaostahimili makosa.
### Dhana za Msingi
| Dhana | Maelezo |
|---------|-------------|
| **Mada** | Aina ya ujumbe (k.m.,`orders`,`user-events`) |
| **Sehemu** | Mada zimegawanywa katika sehemu za usawa |
| **Mtayarishaji** | Programu inayoandika ujumbe kwa mada |
| **Mtumiaji** | Programu inayosoma ujumbe kutoka kwa mada |
| **Kikundi cha Watumiaji** | Kundi la watumiaji wanaoshiriki mzigo wa kusoma mada |
| **Kukabiliana** | Nafasi ya mtumiaji ndani ya kizigeu |
| **Dalali** | Nodi ya seva ya Kafka |
### Wakati wa Kutumia Kafka
- **Utiririshaji wa tukio**: Uchakataji wa tukio la wakati halisi kwa kiwango kikubwa.
- **Huduma za utengano**: Watayarishaji na watumiaji hawahitaji kujuana.
- **Cheza tena**: Ujumbe huhifadhiwa; watumiaji wanaweza kusoma tena kutoka kwa kukabiliana yoyote.
- **Shinikizo la Nyuma**: Kafka hushughulikia kwa kawaida tofauti za kasi kati ya wazalishaji na watumiaji.
---

## Kuunda Data
### Star Schema vs Snowflake Schema
| Mpango | Muundo | Faida | Hasara |
|--------|-----------|------|------|
| **Nyota** | Jedwali kuu la ukweli lililozungukwa na majedwali ya vipimo visivyo na kawaida | Maswali rahisi, yanasomwa haraka | Upungufu wa data |
| **Mwenye theluji** | Majedwali ya vipimo yanarekebishwa (yamegawanywa katika majedwali madogo) | Upungufu wa uhitaji | Zaidi hujiunga, maswali ya polepole |
### Majedwali ya Ukweli na Vipimo
| Aina ya Jedwali | Ina | Mfano |
|-----------|----------|----------|
| **Ukweli** | Matukio yanayoweza kupimika (metriki) | `orders`(kitambulisho_cha_agizo, kitambulisho_cha_bidhaa, kitambulisho_cha_mteja, kiasi, tarehe) |
| **Kipimo** | Sifa za maelezo | `products`(kitambulisho_cha_bidhaa, jina, kategoria, bei),`customers`(kitambulisho_cha_mteja, jina, jiji) |
---

## Duka za Kipengele
Duka la vipengele ni hazina ya kati ya vipengele vya ML - thamani zinazotolewa zinazotumiwa kama ingizo kwa miundo (k.m., "wastani wa thamani ya agizo la mtumiaji katika siku 30 zilizopita").
| Uwezo | Maelezo |
|-----------|-------------|
| **Usajili wa Kipengele** | Katalogi ya vipengele vinavyopatikana vilivyo na metadata |
| **Duka la Nje ya Mtandao** | Vipengele vya kihistoria vya mafunzo ya mfano (bechi) |
| **Duka la Mtandaoni** | Kipengele cha kusubiri kidogo kinachohudumia kwa makisio ya wakati halisi |
| **Ufuatiliaji wa Kipengele** | Tambua mteremko, thamani zinazokosekana, mabadiliko ya usambazaji |
| Zana | Maelezo |
|------|-------------|
| **Sikukuu** | Chanzo-wazi; inafanya kazi na mfumo wowote wa ML |
| **Tektoni** | Kibiashara; jukwaa la kipengele cha wakati halisi |
| **Hopsworks** | Chanzo-wazi; jukwaa kamili la ML na duka la huduma |
| **Duka la Kipengele cha Matofali ya Data** | Imeunganishwa na Databricks/Spark |
---

## Ubora wa Data
Ubora wa data ndio muuaji kimya wa miradi ya ML. Taka ndani, takataka nje.
### Vipimo vya Ubora
| Vipimo | Swali |
|-----------|----------|
| **Usahihi** | Je, data inaonyesha ukweli? |
| **Ukamilifu** | Je, sehemu zinazohitajika zina watu? |
| **Uthabiti** | Je, maadili yanakubaliana katika vyanzo vyote? |
| **Wakati** | Je, data ni ya sasa? |
| **Uhalali** | Je, maadili yanaambatana na sheria zilizobainishwa? |
| **Upekee** | Je, kuna nakala za rekodi? |
### Zana za Ubora wa Data
| Zana | Mbinu |
|------|-----------|
| **Matarajio Makubwa** | Python-msingi; fafanua "matarajio" kuhusu data |
| **Monte Carlo** | Mfumo wa uangalizi wa data unaoendeshwa na ML |
| **dbt vipimo** | Majaribio yaliyojumuishwa ndani ya data ya ghala (ya kipekee, si_null, mahusiano) |
| **Soda** | Uchanganuzi wa ubora wa data kwenye chanzo huria |
---

## Utawala wa Takwimu
Udhibiti wa data huhakikisha kuwa data inadhibitiwa kwa uwajibikaji kote katika shirika.
| Eneo | Maelezo |
|------|-------------|
| **Katalojia ya Data** | Orodha inayoweza kutafutwa ya seti za data zilizo na metadata (Amundsen, DataHub, Atlan) |
| **Ukoo wa Data** | Fuatilia wapi data inatoka na jinsi inavyobadilika |
| **Udhibiti wa Ufikiaji** | Ruhusa za msingi; nani anaweza kusoma/kuandika nini |
| **Kuzingatia** | Ufuasi wa GDPR, CCPA, HIPAA |
| **Umiliki wa Data** | Futa umiliki kwa kila seti ya data (usimamizi) |
| **Sera za Uhifadhi** | Bainisha muda ambao data inatunzwa na inafutwa lini |
---

## Rafu ya Data ya Kisasa
"Rundo la kisasa la data" linarejelea mchanganyiko wa kawaida wa zana zinazotumiwa na timu za data leo:
| Tabaka | Zana za Kawaida |
|-------|--------------|
| **Kumeza** | Fivetran, Airbyte |
| **Ghala** | Snowflake, BigQuery, Redshift |
| **Mabadiliko** | dbt |
| **Ochestration** | Mtiririko wa hewa, Prefect, Dagster |
| **BI / Visualization** | Mtazamaji, Metabase, Jedwali |
| **Reverse ETL** | Sensa, Hightouch (sawazisha data ya ghala kwenye zana) |
| **Ubora wa Data** | Matarajio Mazuri, Monte Carlo |
Mwelekeo unaelekea kwenye zana za msimu, bora zaidi za kuzaliana zilizounganishwa na viwango vya wazi (SQL, miundo ya dbt, Airflow DAGs) badala ya mifumo ya monolithic.