<!--
---
# Metadata
title: "Causal Inference"
description: "DAGs, confounders, difference-in-differences, instrumental variables"
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
tags: [causal, inference, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Maoni ya Sababu
Uelekezaji wa sababu ni sayansi ya kuamua ikiwa jambo moja husababisha lingine - sio tu ikiwa zinahusiana. Uunganisho unakuambia kuwa vijiti viwili vinasogea pamoja. Sababu inakuambia kuwa kubadilisha moja kutabadilisha nyingine. Tofauti hii ni muhimu sana katika dawa (je, dawa hii inafanya kazi?), sera (je, hatua hii inapunguza umaskini?), biashara (je, kampeni hii ya tangazo huongeza mauzo?), na sayansi (je, utaratibu huu unafafanua jambo hili?).
---

## Uhusiano dhidi ya Sababu
| Dhana | Maelezo | Mfano |
|---------|-------------|---------|
| **Uhusiano** | Vigezo viwili vinasogea pamoja | Mauzo ya aiskrimu na vifo vya kuzama vyote huongezeka wakati wa kiangazi |
| **Sababu** | Tofauti moja huathiri moja kwa moja nyingine | Uvutaji sigara husababisha saratani ya mapafu |
| **Inachanganya** | Tofauti ya tatu husababisha zote mbili | Hali ya hewa ya joto husababisha mauzo ya ice cream na kuogelea (na kuzama) |
| **Kisababishi cha nyuma** | Athari husababisha sababu inayodhaniwa | Watu hununua virutubisho vya afya kwa sababu ni wagonjwa, si vinginevyo |
| **Uhusiano wa uongo** | Uhusiano wa bahati mbaya | Utumiaji wa jibini kwa kila mtu unahusiana na vifo vinavyotokana na kubana kwa shuka |
---

## Mfumo wa Matokeo Yanayowezekana
### Rubin Causal Model
| Dhana | Maelezo |
|---------|-------------|
| **Matokeo yanayowezekana** | Kwa kila kitengo, kuna matokeo ikiwa itatibiwa Y(1) na matokeo ikiwa haijatibiwa Y(0) |
| **Madhara ya matibabu** | Tofauti: Y(1) - Y(0) kwa kitengo fulani |
| **Tatizo la msingi** | Hatuwezi kamwe kuona Y(1) na Y(0) kwa kitengo kimoja - tunaweza tu kuona moja |
| **Athari ya Wastani ya Matibabu (ATE)** | Wastani wa athari za matibabu ya mtu binafsi katika idadi ya watu |
| **Hakika** | Matokeo yasiyozingatiwa - nini kingetokea chini ya hali nyingine |
### Mawazo Muhimu
| Dhana | Maana | Jinsi ya Kutosheleza |
|-----------|--------|----------------|
| **Kutokujua (kutokuwa na mashaka)** | Mgawo wa matibabu hautegemei matokeo yanayoweza kutokea, ikizingatiwa washirika wanaozingatiwa | Kubahatisha; pima visumbufu vyote |
| **Chanya (muingiliano)** | Kila kitengo kina uwezekano usio sifuri wa kupokea matibabu yoyote | Angalia mwingiliano wa covariate kati ya vikundi |
| **SUTVA** (Dhana Imara ya Thamani ya Tiba) | Matibabu ya kitengo kimoja haiathiri matokeo ya mwingine; matibabu ni thabiti | Hakuna kuingiliwa; hakuna matoleo yaliyofichwa ya matibabu |
| **Uthabiti** | Matokeo yaliyozingatiwa ni sawa na matokeo yanayowezekana chini ya matibabu yaliyopokelewa | Matibabu iliyofafanuliwa vizuri |
---

## Mbinu za Uingizaji wa Sababu
### Mbinu za Majaribio
| Mbinu | Maelezo | Nguvu | Kizuizi |
|--------|------------------------|------------|
| **Jaribio lililodhibitiwa bila mpangilio (RCT)** | Nasibu gawa vitengo vya matibabu au udhibiti | Kiwango cha dhahabu; huondoa utata | Ghali; wakati mwingine usio na maadili; haiwezi kujumlisha |
| **Upimaji wa A/B** | RCT katika muktadha wa biashara/teknolojia | Rahisi; kali | Vipimo vya muda mfupi; athari mpya; kuingiliwa |
| **Majaribio ya kubadili nyuma** | Matibabu mbadala kwa muda | Hushughulikia mwingiliano katika soko | Inahitaji mazingira thabiti |
### Mbinu za Majaribio ya Nusu
| Mbinu | Maelezo | Dhana Muhimu |
|--------|-------------|----------------|
| **Tofauti-katika-tofauti (DiD)** | Linganisha mabadiliko ya matokeo kati ya vikundi vilivyotibiwa na kudhibiti kwa wakati | Mitindo sambamba: vikundi vingefuata mkondo huo huo bila matibabu |
| **Kukomesha urejeshi (RD)** | Linganisha vitengo vilivyo juu na chini kidogo ya sehemu ya matibabu | Vizio vilivyo karibu na sehemu ya kukatwa vinaweza kulinganishwa (kama-kama nasibu) |
| **Vigezo vya ala (IV)** | Tumia kigezo kinachoathiri matibabu lakini si matokeo isipokuwa kwa matibabu | Chombo kinahusiana na matibabu; huathiri matokeo tu kwa matibabu |
| **Udhibiti wa sintetiki** | Unda mchanganyiko ulio na uzani wa vitengo vya udhibiti ili ulingane na kitengo kilichotibiwa | Udhibiti wa syntetisk unawakilisha kwa usahihi sehemu iliyotibiwa |
| **Alama za tabia zinazolingana** | Linganisha vitengo vilivyotibiwa na kudhibiti vilivyo na uwezekano sawa wa matibabu | Vichanganyiko vyote hupimwa na kujumuishwa katika modeli ya mwelekeo |
### Tofauti-katika-Tofauti (Inayoonekana)
| Kipindi | Kikundi Kilichotibiwa | Kikundi cha Kudhibiti | Tofauti |
|--------|------------------------------------------|
| **Matibabu ya awali** | Y_t_pre | Y_c_pre | Y_t_pre - Y_c_pre |
| **Matibabu ya baada** | Y_t_chapisho | Y_c_chapisho | Chapisho_la_chapisho - Y_c_chapisho |
| **DiD makadirio** | | | (Y_t_post - Y_t_pre) - (Y_c_post - Y_c_pre) |
---

## Directed Acyclic Grafu (DAGs)
DAG ni zana zinazoonekana za kusimba mawazo ya visababishi na kutambua vikanganyiko.
### Miundo Msingi
| Muundo | Muundo | Maana |
|-----------|---------|-------------|
| **Msururu** | A → B → C | A na C zinahusishwa kupitia B; kudhibiti kwa B huzuia njia |
| **Uma** | A ← B → C | A na C wamechanganyikiwa na B; kudhibiti kwa B huzuia njia |
| **Mgongano** | A → B ← C | A na C ni huru; kudhibiti kwa B hufungua njia (huunda ushirika wa uwongo) |
### Kanuni za DAG
| Kanuni | Maelezo |
|------|-------------|
| **Kigezo cha mlango wa nyuma** | Ili kukadiria athari ya sababu ya X kwenye Y, zuia njia zote za mlango wa nyuma (njia zilizo na mshale ndani ya X) kwa kuweka vigezo vinavyofaa |
| **Kigezo cha mlango wa mbele** | Ikiwa njia za mlango wa nyuma haziwezi kuzuiwa, tumia vipatanishi: kadiria X → M → Y katika hatua mbili |
| **Usiweke masharti ya kugongana** | Kudhibiti kwa athari ya kawaida hufungua njia ya uwongo |
| **Usiweke masharti ya vizazi vya wagongana** | Shida sawa na hali kwenye kigonga chenyewe |
---

## Mitego ya Kawaida
| Shimo | Maelezo | Mfano |
|---------|-------------|---------|
| **Upendeleo tofauti ulioachwa** | Imeshindwa kudhibiti kwa mkanganyiko | Kukadiria elimu → mapato bila kudhibiti uwezo |
| **Kudhibiti kupita kiasi** | Kuweka kwenye mpatanishi au mgongano | Kudhibiti cheo cha kazi wakati wa kukadiria elimu → mapato |
| **Upendeleo wa uteuzi** | Kuweka juu ya kutofautiana kuathiriwa na matibabu | Kuchambua tu watu walioajiriwa wakati wa kusoma mafunzo → mshahara |
| **Upendeleo wa wakati usioweza kufa** | Kuweka vibaya wakati wa mtu katika masomo ya kikundi | Wagonjwa lazima waishi kwa muda wa kutosha ili kupokea matibabu |
| **Rejea kwa maana** | Thamani za juu zaidi zinaelekea kuelekea wastani | Wagonjwa wagonjwa huboresha baada ya matibabu bila kujali |
| **Upendeleo baada ya matibabu** | Uwekaji juu ya vigeuzo vinavyotokea baada ya matibabu | Kudhibiti kwa matukio mabaya wakati wa kukadiria ufanisi wa dawa |
---

## Zana na Maktaba
| Zana | Lugha | Maelezo |
|------|-------------------------|
| **Kwanini** | Chatu | maktaba ya Microsoft; Maelekezo ya sababu ya DAG |
| **CausalML** | Chatu | Maktaba ya Uber ya uundaji wa hali ya juu na sababu ML |
| **EconML** | Chatu | Double ML, misitu causal, ala vigezo |
| **mifano ya mstari** | Chatu | IV, miundo ya data ya paneli, DiD |
| **MatchIt** | R | Ulinganifu wa alama za propensity |
| **kitu** | R / mtandao | uchambuzi wa DAG; tambua seti za marekebisho |
| **Athari Sababu** | R / Chatu | Mfululizo wa saa wa muundo wa Bayesian kwa uelekezaji wa sababu |
---

## Muhtasari
Uelekezaji wa sababu ni juu ya kusonga zaidi ya "kilichotokea" hadi "kile kingetokea ikiwa mambo yangekuwa tofauti." Changamoto kuu ni kwamba hatuwezi kamwe kuona matokeo yaliyotibiwa na ambayo hayajatibiwa kwa kitengo kimoja - ukweli haupo kila wakati. Majaribio ya nasibu hutatua hili kwa kufanya vikundi vya matibabu na udhibiti vilinganishwe. Wakati ugeuzaji nasibu hauwezekani, mbinu za majaribio - DiD, kutoendelea kurudi nyuma, vigeu vya ala, udhibiti wa sintetiki - jaribu kuunda upya uwongo kutoka kwa data ya uchunguzi. DAG husaidia kufanya dhana kuwa wazi na kutambua vigeu sahihi vya kudhibiti. Ujuzi muhimu ni kufikiria kwa uangalifu juu ya mchakato wa kutengeneza data: ni nini husababisha nini, ni nini kichanganya, nini kigongana, na nini kingetokea chini ya njia mbadala.