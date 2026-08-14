---
# Metadata
title: "Data Visualization"
description: "Chart selection, design principles, storytelling, tools"
category: "Data Science and Analytics"
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

# Data Visualization
Ang isang mahusay na disenyo na tsart ay maaaring magbunyag ng mga pattern na itinatago ng mga talahanayan ng mga numero. Ang isang hindi maganda ang disenyo ay maaaring iligaw, lituhin, o mainip. Ang data visualization ay ang craft ng paggawa ng data sa mga visual na kwento na nagbibigay-alam sa mga desisyon. Sinasaklaw ng file na ito ang pagpili ng tsart, mga prinsipyo ng disenyo, karaniwang pagkakamali, at ang mga tool na ginagawang posible ang lahat ng ito.
---

## Pagpili ng Tamang Chart
Ang pinakamahalagang desisyon sa anumang visualization ay ang pagpili ng tamang uri ng chart para sa iyong data at mensahe.
### Gabay sa Pagpili ng Tsart
| Iyong Layunin | Pinakamahusay na Mga Uri ng Tsart |
|-----------|-----------------|
| **Ihambing ang mga kategorya** | Bar chart, nakapangkat na bar chart |
| **Ipakita ang pagbabago sa paglipas ng panahon** | Line chart, area chart |
| **Ipakita ang pamamahagi** | Histogram, box plot, violin plot |
| **Ipakita ang relasyon** | Scatter plot, bubble chart |
| **Ipakita ang komposisyon** | Stacked bar, pie chart (limitadong hiwa), treemap |
| **Ipakita ang ugnayan** | Scatter plot, heatmap, pair plot |
| **Ipakita ang ranggo** | Pahalang na bar chart |
| **Ipakita ang mga geographic na pattern** | Choropleth na mapa, tuldok na mapa |
| **Ipakita ang part-to-whole sa paglipas ng panahon** | Stacked area chart |
### Kailan Gagamitin ang Bawat Chart
| Tsart | Mga Lakas | Iwasan Kapag |
|-------|-----------|-----------|
| **Bar** | I-clear ang mga paghahambing sa mga kategorya | Masyadong maraming kategorya (>15) |
| **Linya** | Mga uso sa paglipas ng panahon; tuloy-tuloy na data | Ang data ay hindi sequential |
| **Scatter** | Mga ugnayan sa pagitan ng dalawang variable | Masyadong maraming magkakapatong na puntos |
| **Histogram** | Pamamahagi ng hugis ng isang variable | Maliit na laki ng sample (<20) |
| **Box plot** | Summary statistics + outliers; compare distributions | Audience unfamiliar with them |
| **Heatmap** | Correlation matrices; patterns in 2D data | Too many variables |
| **Pie chart** | Simple composition (2–5 slices) | More than 5 slices; precise comparisons needed |
| **Violin plot** | Distribution density + quartiles | Small audiences unfamiliar with them |
| **Pair plot** | Quick overview of all variable relationships | Many variables (>8) |
---

## Mga Prinsipyo ng Disenyo
### Mga Pangunahing Ideya ni Tufte
Ang mga prinsipyo ni Edward Tufte ay nananatiling gintong pamantayan para sa visualization ng data:
| Prinsipyo | Paglalarawan |
|-----------|-------------|
| **I-maximize ang ratio ng data-ink** | Ang bawat patak ng tinta ay dapat maghatid ng data. Alisin ang lahat ng iba pa. |
| **Alisin ang chartjunk** | Walang 3D effect, gratuitous gradients, o decorative elements. |
| **Ipakita ang data** | Huwag papangitin, itago, o cherry-pick. Hayaang magsalita ang data. |
| **Maliliit na multiple** | Gumamit ng paulit-ulit na maliliit na chart para sa paghahambing sa mga kategorya. |
| **Sparklines** | Maliliit, kasing laki ng salita na mga chart para sa inline na data ng trend. |
### Mga Praktikal na Panuntunan sa Disenyo
| Panuntunan | Bakit |
|------|-----|
| **Simulan ang y-axis sa zero** (para sa mga bar chart) | Kung hindi, pinalalaki mo ang mga pagkakaiba |
| **Direktang lagyan ng label** | Maglagay ng mga label sa mga linya/bar sa halip na gumamit ng alamat kapag posible |
| **Gumamit ng kulay nang may layunin** | I-highlight kung ano ang mahalaga; gumamit ng kulay abo para sa konteksto |
| **Panatilihin itong simple** | Isang mensahe sa bawat tsart; huwag mag-overload |
| **Gumamit ng pare-parehong mga sukat** | Kapag naghahambing ng mga chart, panatilihing pareho ang mga axes |
| **Mag-order nang makahulugan** | Pagbukud-bukurin ang mga bar ayon sa halaga (hindi ayon sa alpabeto) maliban kung mayroong natural na pagkakasunud-sunod |
| **Magbigay ng konteksto** | Magdagdag ng mga benchmark, target, o makasaysayang average |
### Mga Alituntunin sa Kulay
| Use Case | Diskarte |
|----------|----------|
| **Kategorya** | Mga natatanging kulay (asul, orange, berde, pula) — max 7–8 na kategorya |
| **Sequential** | Maliwanag hanggang madilim ng isang kulay (mapusyaw na asul → madilim na asul) |
| **Pag-iiba** | Two-hue gradient para sa data na may makabuluhang midpoint (pula ← puti → asul) |
| **Accessibility** | Subukan gamit ang colorblind simulator; huwag umasa sa kulay lamang (magdagdag ng mga label o pattern) |
---

## Pagkukuwento gamit ang Data
Ang tsart na walang salaysay ay isang larawan lamang. Ginagawang insight ng pagkukuwento ang data.
### Ang Storytelling Framework
1. **Konteksto**: Ano ang sitwasyon? Ano ang alam na ng madla?
2. **Conflict**: Ano ang problema, sorpresa, o tensyon sa data?
3. **Resolution**: Ano ang dapat gawin ng audience sa insight na ito?
### Mga Praktikal na Tip
| Tip | Paglalarawan |
|-----|-------------|
| **Lead with the insight** | Pamagat ng chart ang takeaway, hindi ang data ("Tumago ng 30% ang kita" hindi "Kita ayon sa Quarter") |
| **I-annotate ang mga pangunahing punto** | Magdagdag ng mga text callout para sa mahahalagang kaganapan o turning point |
| **Gumamit ng progresibong pagsisiwalat** | Ipakita ang isang tsart sa isang pagkakataon; buuin ang kwento nang hakbang-hakbang |
| **I-highlight kung ano ang mahalaga** | Gumamit ng kulay o laki upang maakit ang pansin sa pangunahing punto ng data |
| **Magbigay ng "so ano?"** | Dapat sagutin ng bawat tsart ang isang tanong o mag-prompt ng isang aksyon |
---

## Mga Karaniwang Pagkakamali
| Pagkakamali | Bakit Masama | Ayusin |
|---------|-------------|-----|
| **Truncated y-axis** | Pinalalaki ang maliliit na pagkakaiba | Magsimula sa zero para sa mga bar chart |
| ** Saklaw ng oras ng pagpili ng cherry** | Mga panlilinlang tungkol sa mga uso | Ipakita ang buong magagamit na hanay |
| **Masyadong maraming kulay** | Nakaka-overwhelm ang manonood | Limitahan sa 5–7; gumamit ng kulay abo para sa konteksto |
| **Dual y-axes** | Nagpapahiwatig ng ugnayan na maaaring wala | Gumamit ng dalawang magkahiwalay na chart |
| **3D chart** | Binabaluktot ang mga proporsyon | Palaging gumamit ng 2D |
| **Mga pie chart na may 10+ slice** | Imposibleng ihambing | Gumamit na lang ng bar chart |
| **Nawawalang mga label** | Hindi maintindihan ng viewer ang chart | Palaging lagyan ng label ang mga axes, pamagat, at mga unit |
| **Mga chart ng mapanlinlang na lugar** | Ang mga nakasalansan na lugar ay sumisira sa pananaw ng indibidwal na serye | Gumamit ng mga line chart o maliliit na multiple |
---

## Mga tool
### Sawa
| Aklatan | Lakas |
|---------|----------|
| **matplotlib** | Foundation ng Python plotting; ganap na nako-customize |
| **seaborn** | Paggunita sa istatistika; magagandang default; binuo sa matplotlib |
| **plotly** | Interactive, web-based na mga chart; mga dashboard |
| **altair** | Declarative grammar ng graphics (Vega-Lite) |
| **bokeh** | Interactive visualization para sa mga browser |
### JavaScript / Web
| Aklatan | Lakas |
|---------|----------|
| **D3.js** | Pinakamataas na kakayahang umangkop; matarik na kurba ng pagkatuto |
| **Chart.js** | Simple, tumutugon na mga chart |
| **Recharts** | React-friendly na charting |
| **Namamasid na Plot** | Magaan, nagpapahayag ng grammar ng mga graphics |
### Mga Tool na Walang Code / BI
| Tool | Uri |
|------|------|
| **Tableau** | Pang-industriyang visual analytics |
| **Power BI** | Microsoft ecosystem; enterprise BI |
| **Looker** | Google Cloud; paggalugad ng data |
| **Metabase** | Open-source; simpleng setup |
| **Apache Superset** | Open-source; Katutubong SQL |
---

## Disenyo ng Dashboard
Ang dashboard ay isang koleksyon ng mga visualization na magkasamang nagsasabi ng kumpletong kuwento tungkol sa isang proseso, system, o negosyo.
### Mga Uri ng Dashboard
| Uri | Madla | Layunin |
|------|----------|---------|
| **Madiskarte** | Mga Executive | Mga mataas na antas ng KPI; pangmatagalang uso |
| **Pagpapatakbo** | Mga Tagapamahala | Real-time na pagsubaybay; araw-araw na operasyon |
| **Analytical** | Mga Analyst | Malalim na paggalugad; pagsala, drill-down |
### Checklist ng Disenyo
- **Kilalanin ang iyong audience**: Anong mga desisyon ang gagawin nila mula sa dashboard na ito?
- **5-segundong panuntunan**: Maiintindihan ba ang pangunahing takeaway sa loob ng 5 segundo?
- **Layout**: Mga pinakamahalagang sukatan sa kaliwang itaas (kung saan nauuna ang mga mata).
- **Limitahan ang mga uri ng chart**: 3–4 na uri ng max bawat dashboard para sa pagkakapare-pareho.
- **Interactive bilang default**: Mga filter, tagapili ng hanay ng petsa, drill-down.
- **Pagganap**: Ang mga dashboard na tumatagal ng >5 segundo bago mag-load ay hindi nasanay.
- **Mobile**: Isaalang-alang ang tumutugon na disenyo kung kailangan ito ng mga user on the go.
---

## Buod
Ang magandang visualization ng data ay tungkol sa kalinawan, katapatan, at epekto. Piliin ang tamang chart para sa iyong data. Alisin ang lahat ng hindi nagsisilbi sa mensahe. Gumamit ng kulay at anotasyon upang gabayan ang manonood. At palagi, laging hayaan ang data na magkuwento — hindi ang kabaligtaran.