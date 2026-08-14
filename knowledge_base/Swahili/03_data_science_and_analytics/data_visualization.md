<!--
---
# Metadata
title: "Data Visualization"
description: "Chart selection, design principles, storytelling, tools"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, visualization, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Taswira ya data
Chati iliyoundwa vizuri inaweza kufichua ruwaza ambazo majedwali ya nambari huficha. Mtu aliyeundwa vibaya anaweza kupotosha, kuchanganya, au kuchoka. Taswira ya data ni ufundi wa kubadilisha data kuwa hadithi za taswira zinazotoa maamuzi. Faili hii inashughulikia uteuzi wa chati, kanuni za muundo, makosa ya kawaida, na zana zinazowezesha yote.
---

## Kuchagua Chati Sahihi
Uamuzi muhimu zaidi katika taswira yoyote ni kuchagua aina sahihi ya chati kwa data na ujumbe wako.
### Mwongozo wa Uchaguzi wa Chati
| Lengo lako | Aina Bora za Chati |
|-----------|-----------------|
| **Linganisha kategoria** | Chati ya pau, chati ya pau iliyopangwa |
| **Onyesha mabadiliko baada ya muda** | Chati ya mstari, chati ya eneo |
| **Onyesha usambazaji** | Histogram, njama ya sanduku, njama ya violin |
| **Onyesha uhusiano** | Kiwanja cha kutawanya, chati ya viputo |
| **Onyesha muundo** | Upau uliopangwa kwa rafu, chati ya pai (vipande vichache), ramani ya miti |
| **Onyesha uwiano** | Njama ya kutawanya, ramani ya joto, njama ya jozi |
| **Onyesha cheo** | Chati ya upau mlalo |
| **Onyesha ruwaza za kijiografia** | Ramani ya Choropleth, ramani ya nukta |
| **Onyesha sehemu-kwa-zima baada ya muda** | Chati ya eneo lililopangwa kwa rafu |
### Wakati wa Kutumia Kila Chati
| Chati | Nguvu | Epuka Wakati |
|-------|-----------|------------|
| **Bar** | Futa ulinganishaji katika kategoria zote | Aina nyingi sana (>15) |
| **Mstari** | Mitindo ya muda; data endelevu | Data si mfuatano |
| **Tawanya** | Uhusiano kati ya vigezo viwili | Pointi nyingi sana zinazopishana |
| **Histogram** | Umbo la usambazaji wa kigeu kimoja | Saizi ndogo za sampuli (<20) |
| **Box plot** | Summary statistics + outliers; compare distributions | Audience unfamiliar with them |
| **Heatmap** | Correlation matrices; patterns in 2D data | Too many variables |
| **Pie chart** | Simple composition (2–5 slices) | More than 5 slices; precise comparisons needed |
| **Violin plot** | Distribution density + quartiles | Small audiences unfamiliar with them |
| **Pair plot** | Quick overview of all variable relationships | Many variables (>8) |
---

## Kanuni za Kubuni
### Mawazo ya Msingi ya Tufte
Kanuni za Edward Tufte zinasalia kuwa kiwango cha dhahabu cha taswira ya data:
| Kanuni | Maelezo |
|-----------|-------------|
| **Ongeza uwiano wa wino wa data** | Kila tone la wino linapaswa kuwasilisha data. Ondoa kila kitu kingine. |
| **Kuondoa chartjunk** | Hakuna madoido ya 3D, gradient bila malipo, au vipengee vya mapambo. |
| **Onyesha data** | Usipotoshe, usifiche, au uchague cherry. Acha data izungumze. |
| **Vizidishi vidogo** | Tumia chati ndogo zinazorudiwa kwa kulinganisha katika kategoria. |
| **Cheche** | Chati ndogo, za ukubwa wa maneno kwa data ya mienendo ya ndani. |
### Kanuni za Usanifu kwa Vitendo
| Kanuni | Kwa nini |
|------|-----|
| **Anzisha mhimili y kwa sufuri** (kwa chati za miraba) | Vinginevyo unazidisha tofauti |
| **Weka lebo moja kwa moja** | Weka lebo kwenye mistari/paa badala ya kutumia ngano inapowezekana |
| **Tumia rangi kwa makusudi** | Angazia mambo muhimu; tumia kijivu kwa muktadha |
| **Weka rahisi** | Ujumbe mmoja kwa kila chati; usipakie |
| **Tumia mizani thabiti** | Unapolinganisha chati, weka shoka sawa |
| **Agiza kwa maana** | Panga pau kwa thamani (sio kialfabeti) isipokuwa kama kuna mpangilio asilia |
| **Toa muktadha** | Ongeza alama, shabaha, au wastani wa kihistoria |
### Miongozo ya Rangi
| Tumia Kesi | Mbinu |
|----------|----------|
| **Kategoria** | Rangi tofauti (bluu, machungwa, kijani kibichi, nyekundu) - upeo wa aina 7-8 |
| **Mfuatano** | Mwanga hadi giza wa hue moja (bluu isiyokolea → bluu iliyokolea) |
| **Kuachana** | gradient ya rangi mbili kwa data yenye alama ya katikati yenye maana (nyekundu ← nyeupe → bluu) |
| **Ufikivu** | Jaribu na viigaji visivyo na rangi; usitegemee rangi pekee (ongeza lebo au ruwaza) |
---

## Hadithi zenye Data
Chati bila simulizi ni picha tu. Usimulizi wa hadithi hugeuza data kuwa utambuzi.
### Mfumo wa Kusimulia Hadithi
1. **Muktadha**: Je, hali ikoje? Je, watazamaji tayari wanajua nini?
2. **Migogoro**: Nini tatizo, mshangao, au mvutano katika data?
3. **Azimio**: Hadhira inapaswa kufanya nini na umaizi huu?
### Vidokezo Vitendo
| Kidokezo | Maelezo |
|-----|--------------|
| **Ongoza kwa ufahamu** | Jina la chati iliyo na vitu vya kuchukua, sio data ("Mapato yalikua 30%" sio "Mapato kwa Robo") |
| **Fafanua mambo muhimu** | Ongeza miito ya maandishi kwa matukio muhimu au sehemu za mabadiliko |
| **Tumia ufichuzi unaoendelea** | Onyesha chati moja kwa wakati mmoja; tengeneza hadithi hatua kwa hatua |
| **Angazia mambo muhimu** | Tumia rangi au saizi kuteka umakini kwenye sehemu kuu ya data |
| **Toa "ili nini?"** | Kila chati inapaswa kujibu swali au kuuliza kitendo |
---

## Makosa ya Kawaida
| Kosa | Kwanini Ni Mbaya | Rekebisha |
|---------|-------------|-----|
| **Mhimili wa y uliokatwa** | Hutia chumvi tofauti ndogo | Anzia sifuri kwa chati za miraba |
| **Kipindi cha kuchuma Cherry** | Upotoshaji kuhusu mitindo | Onyesha safu kamili inayopatikana |
| **Rangi nyingi mno** | Hulemea mtazamaji | Kikomo hadi 5-7; tumia kijivu kwa muktadha |
| **Axes y mbili** | Inamaanisha uwiano ambao unaweza kuwa haupo | Tumia chati mbili tofauti |
| **Chati za 3D** | Hupotosha uwiano | Tumia 2D | kila wakati
| **Chati pai zilizo na vipande 10+** | Haiwezekani kulinganisha | Tumia chati ya pau badala yake |
| **Lebo zinazokosekana** | Mtazamaji hawezi kuelewa chati | Kila wakati weka lebo kwenye shoka, mada na vitengo |
| **Chati za maeneo yanayopotosha** | Maeneo yaliyopangwa kwa rafu yanapotosha mtazamo wa mfululizo mahususi | Tumia chati za mistari au vizidishi vidogo |
---

##Zana
### Chatu
| Maktaba | Nguvu |
|---------|----------|
| **matplotlib** | Msingi wa njama ya Python; inayoweza kubinafsishwa kikamilifu |
| **mzaliwa wa baharini** | Taswira ya takwimu; chaguo-msingi nzuri; imejengwa kwenye matplotlib |
| **njama** | Chati zinazoingiliana, msingi wa wavuti; dashibodi |
| **madhabahu** | Sarufi ya kutangaza ya michoro (Vega-Lite) |
| **bokeh** | Taswira shirikishi kwa vivinjari |
### JavaScript / Wavuti
| Maktaba | Nguvu |
|---------|----------|
| **D3.js** | Upeo wa kubadilika; mkondo wa kujifunza mwinuko |
| **Chati.js** | Chati rahisi na sikivu |
| **Chati upya** | Uwekaji chati wa kirafiki |
| **Njama Inayoonekana** | Sarufi nyepesi, inayoelezea ya michoro |
### Zana za Hakuna Msimbo / BI
| Zana | Aina |
|------|------|
| **Jedwali** | Uchanganuzi wa kawaida wa tasnia |
| **Nguvu BI** | Mfumo wa ikolojia wa Microsoft; biashara BI |
| **Mtazamaji** | Wingu la Google; uchunguzi wa data |
| **Metabase** | Chanzo-wazi; usanidi rahisi |
| **Apache Superset** | Chanzo-wazi; Asili ya SQL |
---

## Muundo wa Dashibodi
Dashibodi ni mkusanyiko wa taswira ambazo kwa pamoja zinasimulia hadithi kamili kuhusu mchakato, mfumo au biashara.
### Aina za Dashibodi
| Aina | Hadhira | Kusudi |
|------|---------------------|
| **Mkakati** | Watendaji | KPI za kiwango cha juu; mitindo ya muda mrefu |
| **Uendeshaji** | Wasimamizi | Ufuatiliaji wa wakati halisi; shughuli za kila siku |
| **Uchambuzi** | Wachambuzi | Uchunguzi wa kina; kuchuja, kuchimba chini |
### Orodha ya Usanifu
- **Fahamu hadhira yako**: Watafanya maamuzi gani kutoka kwenye dashibodi hii?
- **Sheria ya sekunde 5**: Je, bidhaa kuu ya kuchukua inaweza kueleweka katika sekunde 5?
- **Mpangilio**: Vipimo muhimu zaidi juu-kushoto (ambapo macho hutangulia).
- **Punguza aina za chati**: Aina 3–4 za juu kwa kila dashibodi kwa uthabiti.
- **Inaingiliana kwa chaguomsingi**: Vichujio, viteuzi vya masafa ya tarehe, miteremko.
- **Utendaji**: Dashibodi zinazochukua >sekunde 5 kupakia hazitumiki.
- **Simu ya Mkononi**: Zingatia muundo sikivu ikiwa watumiaji wanauhitaji popote pale.
---

## Muhtasari
Taswira nzuri ya data inahusu uwazi, uaminifu na athari. Chagua chati inayofaa kwa data yako. Ondoa kila kitu ambacho hakitumii ujumbe. Tumia rangi na ufafanuzi ili kuelekeza mtazamaji. Na kila wakati, acha data isimulie hadithi - sio kinyume chake.