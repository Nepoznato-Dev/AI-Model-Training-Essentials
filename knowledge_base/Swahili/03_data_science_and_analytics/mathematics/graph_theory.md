---
# Metadata
title: "Graph Theory"
description: "Graph representations, trees, traversals, shortest paths, minimum spanning trees, network flows, and spectral graph theory"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial deep-dive into graph theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [graph-theory, trees, traversals, shortest-paths, spanning-trees, network-flows, spectral-graph-theory]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Nadharia ya Grafu
**grafu** ni muundo wa hisabati unaojumuisha vipeo (nodi) zilizounganishwa na kingo (viungo). Mahusiano ya kielelezo cha grafu: mitandao ya kijamii, ramani za barabara, mitandao ya neva, tegemezi, njia za mawasiliano. Nadharia ya grafu - utafiti wa miundo hii - hutoa algoriti na nadharia ambazo ni muhimu kwa sayansi ya kompyuta, utafiti wa uendeshaji na sayansi ya data.
---

## Dhana za Msingi
### Ufafanuzi
| Muda | Ufafanuzi | Nukuu |
|------|------------|----------|
| **Grafu** | Jozi G = (V, E) ya wima na kingo | G |
| **Kipeo (nodi)** | Sehemu ya V | v, wewe, w |
| **Makali** | Uunganisho kati ya wima mbili | e = (u, v) au {u, v} |
| **Agizo** | Idadi ya wima | \|V\| = n |
| **Ukubwa** | Idadi ya kingo | \|E\| = m |
| **Shahada** | Idadi ya tukio la kingo kwa vertex | deg(v) |
| **Njia** | Mlolongo wa wima tofauti zilizounganishwa na kingo | v₁, v₂, ..., vₖ |
| **Mzunguko** | Njia inayoanza na kuishia kwenye kipeo sawa | v₁ → v₂ → ... → vₖ → v₁ |
| **Imeunganishwa** | Kuna njia kati ya kila jozi ya wima | - |
| **Sehemu** | Upeo mdogo uliounganishwa | - |
| **Njia ndogo** | Grafu iliyoundwa kutoka kwa kikundi kidogo cha V na E | H ⊆ G |
### Aina za Grafu
| Aina | Maelezo | Mfano |
|------|-------------|----------|
| **Isiyoelekezwa** | Kingo hazina mwelekeo | Mtandao wa urafiki |
| **Imeelekezwa (digrafu)** | Kingo zina mwelekeo (arcs) | Viungo vya ukurasa wa wavuti |
| **Uzito** | Kingo hubeba maadili ya nambari | Umbali wa barabara |
| **Bila uzito** | Kingo zote ni sawa | Miunganisho ya kijamii |
| **Rahisi** | Hakuna vitanzi, hakuna kingo nyingi | Grafu nyingi za kiada |
| **Multigraph** | Kingo nyingi kati ya wima sawa zinaruhusiwa | Njia za ndege (safari nyingi za ndege kati ya miji) |
| **Kamili** | Kila jozi ya wima imeunganishwa | Kₙ ina kingo n(n−1)/2 |
| **Wawili** | Vipeo vimegawanywa katika vikundi viwili; kingo tu vikundi vya msalaba | Mapendekezo ya kipengee cha mtumiaji matrices |
| **Mpango** | Inaweza kuchorwa bila vivuko vya makali | Mipangilio ya bodi ya mzunguko |
| **Mti** | Imeunganishwa, grafu ya acyclic | Miti ya maamuzi, mifumo ya faili |
| **DAG** | Imeelekezwa, hakuna mizunguko iliyoelekezwa | Kupanga kazi, grafu za utegemezi |
### Lema wa Kupeana Mikono
Jumla ya digrii zote za kipeo ni sawa na mara mbili ya idadi ya kingo:
Σᵥ deg(v) = 2|E|
**Muhimu:** Kila grafu ina idadi sawa ya vipeo vya digrii isiyo ya kawaida.
**Mfano:** Katika karamu ya watu 10 ambapo kila mtu anapeana mikono na watu wengine 3 haswa: Σ deg = 30, hivyo |E| = kupeana mikono 15 kwa jumla.
---

## Uwakilishi wa Grafu
Jinsi unavyohifadhi grafu kwenye kumbukumbu huamua ufanisi wa kila algoriti unayoendesha juu yake.
| Uwakilishi | Nafasi | Utafutaji wa makali | Iterate Majirani | Bora Kwa |
|----------------|----------------------------------------|-----------|
| **Matrix ya Ukaribu** | O(n²) | O(1) | O(n) | Grafu mnene, majaribio ya makali ya haraka |
| **Orodha ya Ukaribu** | O(n + m) | O(deg(v)) | O(deg(v)) | Grafu chache, mitandao mingi ya ulimwengu halisi |
| **Orodha ya Kingo** | O(m) | O(m) | O(m) | Algorithms rahisi, MST ya Kruskal |
| **Matrix ya Matukio** | O(n · m) | O(m) | O(m) | Algorithms maalum |
### Matrix ya Ukaribu
N × n tumbo A ambapo A[i][j] = 1 ikiwa kingo (i,j) kipo, 0 vinginevyo. Kwa grafu zilizopimwa, A[i][j] = uzito.
**Sifa:**
- Symmetric kwa grafu zisizoelekezwa
- Aᵏ[i][j] = idadi ya matembezi ya urefu k kutoka i hadi j
- Thamani za A hufichua sifa za kimuundo (tazama Nadharia ya Grafu ya Spectral)
### Orodha ya Kukaribiana
Mkusanyiko (au ramani ya hashi) ambapo kila vertex v huhifadhi orodha ya majirani zake.
```
Vertex 0: [1, 3]
Vertex 1: [0, 2, 3]
Vertex 2: [1, 3]
Vertex 3: [0, 1, 2]
```

Huu ndio uwakilishi unaojulikana zaidi kwa grafu za ulimwengu halisi, ambazo kwa kawaida ni chache (m ≪ n²).
---

#Miti #
**mti** ni grafu iliyounganishwa, isiyoelekezwa ya acyclic. **Msitu** ni muunganiko usio wa pamoja wa miti.
### Sifa za Miti
Kwa mti ulio na wima n:
- Ina n - 1 kingo
- Kuna njia moja kabisa kati ya wima zozote mbili
- Kuondoa makali yoyote huitenganisha
- Kuongeza makali yoyote hutengeneza mzunguko mmoja
### Aina za Miti
| Aina | Maelezo | Maombi |
|------|-------------|-------------|
| **Mti wenye mizizi** | Kipeo kimoja kilichoteuliwa kama mzizi | Mifumo ya faili, chati za shirika |
| **Mti wa binary** | Kila nodi ina angalau watoto 2 | BSTs, uchanganuzi wa kujieleza, miti ya maamuzi |
| **Mti uliosawazishwa** | Urefu ni O(logi n) | Miti ya AVL, miti nyekundu-nyeusi (database) |
| **Mti unaozunguka** | Subgraph ambayo inajumuisha wima zote na ni mti | Muundo wa mtandao, kanuni za ukadiriaji |
| **Kiwango cha chini kabisa cha mti unaozunguka** | Mti unaozunguka na uzito wa chini kabisa wa makali | Ubunifu wa mtandao, nguzo |
| **Mchoro wa nyota** | Nodi moja ya kati iliyounganishwa na zingine zote | Mitandao ya kitovu-na-kuzungumza |
### Sifa za Mti wa Binary
| Mali | Mfumo |
|----------|---------|
| Vifundo vya juu kwa kina d | 2 |
| Vifundo vya juu katika mti wa urefu h | 2ʰ⁺¹ − 1 |
| Urefu mdogo kwa nodi n | ⌊logi₂(n)⌋ |
| Vifundo vya majani katika mti kamili wa binary | Nodi za ndani + 1 |
### Mitembezi ya Miti
| Kusafiri | Agizo | Tumia Kesi |
|-----------|-------------------|
| **Agiza mapema** | Mzizi → Kushoto → Kulia | Kunakili mti, usemi wa kiambishi awali |
| **Kwa mpangilio** | Kushoto → Mzizi → Kulia | Matokeo yaliyopangwa kutoka BST |
| **Agizo la baada** | Kushoto → Kulia → Mzizi | Inafuta mti, usemi wa kurekebisha |
| **Mpangilio wa kiwango (BFS)** | Kiwango kwa ngazi, kushoto kwenda kulia | Njia fupi zaidi kwenye mti usio na uzito |
---

## Upitishaji wa Grafu
Algorithms ya kupita hutembelea kila kipeo kinachoweza kufikiwa kwa utaratibu.
### Utafutaji wa Upana-Kwanza (BFS)
Huchunguza safu ya wima kwa safu, kwa kutumia **foleni**.
| Mali | Thamani |
|----------|-------|
| Muundo wa data | Foleni (FIFO) |
| Utata wa wakati | O(V + E) |
| Utata wa nafasi | O(V) |
| Je, ungependa kupata njia fupi zaidi? | Ndiyo (grafu zisizo na uzito) |
| Je, umekamilisha? | Ndiyo (huchunguza wima zote zinazoweza kufikiwa) |
**Algorithm:**
1. Anzia kwenye kipeo cha chanzo s. Mark alitembelewa. Msururu wa s.
2. Wakati foleni si tupu: dequeue vertex u. Kwa kila jirani ambaye hajatembelewa v wa u: mark v alitembelea, enqueue v.
**Programu:** njia fupi zaidi katika grafu zisizo na uzito, vipengee vilivyounganishwa, majaribio ya sehemu mbili, kutambaa kwenye wavuti.
### Utafutaji wa Kina wa Kwanza (DFS)
Huchunguza kwa kina iwezekanavyo kabla ya kurudi nyuma, kwa kutumia **bunda** (au kujirudia).
| Mali | Thamani |
|----------|-------|
| Muundo wa data | Rafu (LIFO) / recursion |
| Utata wa wakati | O(V + E) |
| Utata wa nafasi | O(V) |
| Je, ungependa kupata njia fupi zaidi? | Hapana |
| Je, umekamilisha? | Ndiyo (kwa grafu zenye ukomo) |
**Algorithm:**
1. Anza kwenye vertex s. Mark alitembelewa.
2. Kwa kila jirani ambaye hajatembelewa v ya s: kwa kujirudia DFS kutoka v.
**DFS inaainisha kingo kuwa:**
- **Kingo za miti:** sehemu ya mti wa DFS
- **Kingo za nyuma:** unganisha vertex kwa babu yake (onyesha mizunguko)
- **Kingo za mbele:** unganisha kipeo kwa kizazi chake
- **Kingo za kupita:** unganisha wima katika matawi tofauti
**Programu:** upangaji wa kitopolojia, utambuzi wa mzunguko, vipengee vilivyounganishwa kwa nguvu, kutatua misururu.
### BFS dhidi ya Ulinganisho wa DFS
| Kigezo | BFS | DFS |
|-----------|-----|-----|
| Mkakati | Pana kisha kina | Kina kisha pana |
| Kumbukumbu | Juu (mpaka wa maduka) | Chini (njia ya maduka) |
| Njia fupi zaidi (isiyo na uzito) | Imehakikishwa | Haina uhakika |
| Tumia wakati suluhisho linakaribia kuanza | Bora | Mbaya zaidi |
| Tumia wakati grafu ni ya kina sana | Mbaya zaidi | Bora |
| Upangaji wa kitopolojia | Lahaja ya algoriti ya Kahn | Mbinu ya kawaida |
---

## Algorithms za Njia fupi zaidi
Kupata njia fupi kati ya wima ni moja wapo ya shida muhimu za grafu.
### Kanuni za Dijkstra
Hupata njia fupi zaidi kutoka chanzo kimoja hadi wima nyingine zote kwenye grafu yenye uzani wa ukingo **usio hasi**.
| Mali | Thamani |
|----------|-------|
| Uzito wa makali | Lazima iwe ≥ 0 |
| Wakati (lundo la binary) | O((V + E) logi V) |
| Muda (Lundo la Fibonacci) | O(E + V logi V) |
| Mwenye pupa? | Ndiyo |
| Hushughulikia uzani hasi? | Hapana |
**Algorithm:**
1. Anzisha dist[s] = 0, dist[v] = ∞ kwa v ≠ s zote. Foleni ya kipaumbele Q yenye wima zote.
2. Wakati Q si tupu: toa kipeo u na dist ya chini zaidi. Kwa kila jirani v wa u mwenye uzani wa kingo w: ikiwa dist[u] + w < dist[v], sasisha dist[v] = dist[u] + w.
**Mfano Uliofanya Kazi:**```
Graph: A --1-- B --2-- C --1-- D
       A --4-- C
       B --1-- D

Shortest paths from A:
A → B: 1 (direct)
A → D: 2 (A→B→D)
A → C: 3 (A→B→C, NOT A→C=4)
```

### Algorithm ya Bellman-Ford
Hushughulikia uzani wa kingo **hasi** na kutambua mizunguko hasi.
| Mali | Thamani |
|----------|-------|
| Uzito wa makali | Yoyote (hutambua mizunguko hasi) |
| Utata wa wakati | O(V · E) |
| Utata wa nafasi | O(V) |
| Hushughulikia mizunguko hasi? | Ndiyo (inatambua na kuripoti) |
**Algorithm:**
1. Anzisha dist[s] = 0, dist[v] = ∞ kwa v ≠ s zote.
2. Rudia V - mara 1: kwa kila ukingo (u, v) yenye uzito w: ikiwa dist[u] + w < dist[v], sasisha dist[v].
3. Angalia mizunguko hasi: ikiwa makali yoyote bado yanaweza kupunguzwa, mzunguko mbaya upo.
### Algorithm ya Floyd-Warshall
Hupata njia fupi zaidi kati ya **jozi zote** za wima.
| Mali | Thamani |
|----------|-------|
| Utata wa wakati | O(V³) |
| Utata wa nafasi | O(V²) |
| Hushughulikia uzani hasi? | Ndiyo (lakini sio mizunguko hasi) |
| Mbinu | Utayarishaji wa nguvu |
**Urudiaji:** dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) kwa kila kipeo cha kati k.
### Mwongozo wa Uchaguzi wa Algorithm
| Hali | Algorithm |
|----------|-----------|
| Chanzo kimoja, uzani usio hasi | Dijkstra |
| Chanzo kimoja, uzani hasi unawezekana | Bellman-Ford |
| Jozi zote, grafu mnene | Floyd-Warshall |
| Jozi zote, grafu chache | Endesha Dijkstra kutoka kwa kila kipeo |
| Grafu isiyo na uzito | BFS |
| DAG (hakuna mizunguko) | Aina ya kitopolojia + utulivu |
| A* (kuongozwa na heuristic) | Utafutaji wa * (wa kutafuta njia kwa heuristic nzuri) |
---

## Kima cha chini cha Miti ya Kuruka
**Mti wa chini unaozunguka (MST)** huunganisha wima zote na uzito wa chini kabisa wa ukingo.
### Mali
- MST ina kingo n - 1 haswa (kwa wima n)
- MST inapatikana ikiwa grafu imeunganishwa
- Grafu yenye uzani tofauti wa makali ina MST ya kipekee
- MST inakidhi **mali iliyokatwa**: makali ya uzani wa chini zaidi ya kuvuka kata yoyote ni ya MST
- MST inakidhi **mali ya mzunguko**: makali ya uzani wa juu katika mzunguko wowote si ya MST
### Algorithm ya Kruskal
| Mali | Thamani |
|----------|-------|
| Mkakati | Tamaa - ongeza kingo kwa mpangilio wa uzito |
| Muundo wa data | Seti-tofauti (pata-muungano) |
| Utata wa wakati | O( logi E) |
| Bora kwa | Grafu chache |
**Algorithm:**
1. Panga kingo zote kwa uzito.
2. Kwa kila makali (kwa mpangilio): ikiwa kuiongeza hakufanyi mzunguko (angalia na union-find), ongeza kwenye MST.
3. Acha wakati n - 1 kingo zimechaguliwa.
### Algorithm ya Prim
| Mali | Thamani |
|----------|-------|
| Mkakati | Tamaa - panda mti kutoka kwenye kipeo cha kuanzia |
| Muundo wa data | Foleni ya kipaumbele (min-rundo) |
| Utata wa wakati | O(E logi V) na lundo la jozi |
| Bora kwa | Grafu mnene |
**Algorithm:**
1. Anza kutoka kwa vertex yoyote. Weka alama kama sehemu ya MST.
2. Ongeza ukingo wa uzani wa chini zaidi unaounganisha kipeo katika MST na kipeo nje yake.
3. Acha wakati wima zote zimejumuishwa.
### Maombi ya MST
| Maombi | Jinsi MST Inasaidia |
|-----------------------------|
| Muundo wa mtandao | Weka kebo/bomba la chini ili kuunganisha maeneo yote |
| Kuunganisha | Ondoa k − kingo 1 ndefu zaidi za MST ili kupata k nguzo |
| Kanuni za makadirio | 2-makadirio ya kipimo cha TSP |
| Sehemu ya picha | Panga saizi kwa MST za kufanana kwa rangi |
| Kuondoa kipengele | Ondoa vipengele visivyohitajika kwa kutumia MST ya grafu ya uunganisho |
---

## Mtiririko wa Mtandao
Matatizo ya mtiririko wa mtandao ni mfano wa uhamishaji wa rasilimali kupitia mfumo.
### Ufafanuzi wa Mtandao wa Mtiririko
**Mtandao wa mtiririko** ni grafu iliyoelekezwa na:
- **chanzo** vertex s (hutoa mtiririko)
- Kipeo cha **kuzama** (hutumia mtiririko)
- **Uwezo** c(u,v) ≥0 kwa kila ukingo
- **Mtiririko** f(u,v) ya kuridhisha:
  - **Kizuizi cha uwezo:** 0 ≤ f(u,v) ≤ c(u,v)
  - **Uhifadhi wa mtiririko:** mtiririko ndani = mtiririko nje katika kila kipeo isipokuwa s na t
### Upeo wa Tatizo la Mtiririko
Pata mtiririko wa juu kabisa kutoka s hadi t.
**Njia ya Ford-Fulkerson:**
1. Ingawa kuna njia ya kuongeza kutoka s hadi t kwenye mabaki ya grafu:
2. Tafuta uwezo wa kizuizi kwenye njia
3. Ongeza mtiririko kando ya njia kwa kiasi cha kizuizi
4. Sasisha uwezo wa mabaki
| Algorithm | Utata wa Wakati | Vidokezo |
|-----------|----------------|-------|
| Ford-Fulkerson (DFS) | O(m · f*) ambapo f* ni mtiririko wa juu zaidi | Huenda isisitishwe kwa uwezo usio na mantiki |
| Edmonds-Karp (BFS) | O(V · E²) | Hukomesha kila wakati, chagua njia fupi zaidi ya kuongeza |
| Algorithm ya Dinic | O(V² · E) | Inatumia kuzuia mtiririko; O(V^(1/2) · E) kwa uwezo wa kitengo |
### Nadharia ya Kupunguza Kiwango cha Juu-Mtiririko wa Juu
**Kiwango cha juu cha mtiririko** kutoka s hadi t ni sawa na **kiwango cha chini kabisa cha kukata** kinachotenganisha s kutoka t.
A **kata** (S, T) inagawanya wima kuwa S (iliyo na s) na T (iliyo na t). Uwezo wa kukata ni jumla ya uwezo wa kingo kutoka S hadi T.
**Matumizi ya mtiririko wa juu zaidi:**
- Ulinganishaji wa pande mbili (wape wafanyikazi kazi)
- Mgawanyiko wa picha (tenganisha uso wa mbele na mandharinyuma)
- Kuondolewa kwa baseball (je timu X bado inaweza kushinda?)
- Kuegemea kwa mtandao (kiwango cha juu cha upitishaji wa data)
### Ulinganishaji wa Sehemu Mbili kupitia Mtiririko wa Juu
Kwa kuzingatia grafu ya sehemu mbili G = (L ∪ R, E):
1. Ongeza chanzo s na kingo kwa wima zote katika L (uwezo wa 1)
2. Ongeza sink t yenye kingo kutoka kwa wima zote katika R (uwezo wa 1)
3. Weka uwezo wote wa makali asili kuwa 1
4. Upeo wa mtiririko = upeo unaofanana
---

## Nadharia ya Grafu ya Spectral
Nadharia ya girafu huchunguza grafu kupitia thamani za eigen na vienezaji vya hesabu vinavyohusishwa na grafu.
### Matrices Muhimu
| Matrix | Ufafanuzi | Kinachonasa |
|--------|------------|------------------|
| **Matrix ya ukaribu** A | A[i][j] = 1 ikiwa kingo (i,j) kipo | Muundo wa muunganisho |
| **Matrix ya shahada** D | Ulalo; D[i][i] = deg(i) | Umuhimu wa kipeo kwa shahada |
| **Laplacian** L = D - A | L[i][j] = −1 ikiwa kingo, deg(i) kwenye mshazari | Ulaini wa utendaji kwenye grafu |
| **Laplacian ya Kawaida** L_norm = D^(−1/2) L D^(-1/2) | Toleo lisilobadilika kwa kipimo | Muundo wa Jumuiya |
### Thamani Eigen za Laplacian
Laplacian L ni chanya nusu-dhahiri, kwa hivyo thamani zote eigen ni ≥ 0.
| Thamani ya Eigen | Maana |
|------------|---------|
| λ₁ = 0 | Daima sifuri; eigenvector ndio vekta ya mara kwa mara |
| λ₂ (muunganisho wa aljebra) | > grafu 0 ikiwa imeunganishwa; kubwa = iliyounganishwa vyema |
| Idadi ya sifuri eigenvalues ​​| Sawa na idadi ya vipengele vilivyounganishwa |
| λₙ | Kuhusiana na kiwango cha juu cha digrii na upanuzi wa grafu |
### Matumizi ya Mbinu za Spectral
| Maombi | Mbinu |
|----------------------|
| **Kugawanya grafu** | Tumia eigenveekta za L kugawanya grafu katika sehemu zilizosawazishwa |
| **Ugunduzi wa jumuiya** | Mkusanyiko wa Spectral: wima iliyopachikwa kwa kutumia eigenveekta za chini, kisha nguzo |
| **Kiwango cha Ukurasa** | Eigenvector ya tumbo la karibu (au tumbo la mpito) la grafu ya wavuti |
| **Mchoro wa grafu** | Weka wima kwa kutumia eigenvekta za Laplacian |
| **Mafunzo yanayosimamiwa nusu** | Tangaza lebo kwa kutumia grafu Laplacian (uenezi wa lebo) |
| **Mitandao ya neva ya grafu** | Ubadilishaji wa Spectral: mawimbi ya vichujio kwenye grafu kwa kutumia eigenveekta za L |
### Kutokuwa na Usawa kwa Cheeger
Inahusisha eigenvalue ya pili λ₂ na **upanuzi** wa grafu (jinsi imeunganishwa vizuri):
λ₂ / 2 ≤ h(G) ≤ √(2λ₂)
ambapo h(G) ni nambari ya Cheeger (nambari ya isoperimetric). Hii inamaanisha λ₂ takriban hupima jinsi ilivyo ngumu kukata grafu katika vipande viwili - ufahamu muhimu wa kuunganisha.
---

## Miundo Maalum ya Grafu
| Grafu | Viwango | Mipaka | Mali |
|-------|--------------------------------|
| Kamilisha Kₙ | n | n(n−1)/2 | Kila jozi iliyounganishwa; kipenyo 1 |
| Mzunguko Cₙ | n | n | 2-mara kwa mara; imeunganishwa |
| Njia Pₙ | n | n−1 | Mti; kipenyo n−1 |
| Hypercube Qₖ | 2 | k·2ᵏ⁻¹ | k-kawaida; kipenyo k; pande mbili |
| Kamili sehemu mbili K_{m,n} | m+n | m·n | Kila kipeo katika sehemu moja huungana na zote katika nyingine |
| Petersen grafu | 10 | 15 | 3-mara kwa mara; kipenyo 2; sio mpango; hakuna mzunguko wa Hamiltonia |
---

## Umuhimu kwa Kujifunza kwa Mashine na Sayansi ya Data
| Dhana ya Grafu | Maombi |
|-----------------------------|
| BFS / DFS | Utambazaji wa wavuti, uchanganuzi wa mitandao ya kijamii, uwekaji lebo za sehemu |
| Dijkstra / A* | Upangaji wa njia, utaftaji wa njia wa AI, urambazaji wa roboti |
| Kiwango cha chini cha mti unaozunguka | Kuunganisha (kiunganishi kimoja), uteuzi wa kipengele, muundo wa mtandao |
| Mtiririko wa juu / dakika iliyokatwa | Mgawanyiko wa picha, kulinganisha pande mbili, mgawo wa mapendekezo |
| Mbinu za Spectral | Mkusanyiko wa Spectral, mitandao ya neva ya grafu, upunguzaji wa mwelekeo (Laplacian eigenmaps) |
| Kiwango cha Ukurasa | Nafasi ya injini ya utafutaji, uchanganuzi wa ushawishi katika mitandao ya kijamii |
| DAG | Mitandao ya Bayesian, uelekezaji wa sababu, upangaji wa kazi, grafu za kukokotoa katika ujifunzaji wa kina |
| Grafu za pande mbili | Matrices ya bidhaa za mtumiaji katika mifumo ya pendekezo, masoko ya pande mbili |
| Miundo ya miti | Miti ya maamuzi, misitu nasibu, nguzo za daraja, urambazaji wa mfumo wa faili |
| Uwakilishi wa grafu | Grafu za maarifa (Wikidata, DBpedia), grafu za molekuli (ugunduzi wa dawa), mitandao ya manukuu |
---

## Muhtasari
| Mada | Wazo la Msingi | Algorithm muhimu / Matokeo |
|-------|----------------------------------|
| Misingi | Wima, kingo, digrii, njia | Lema ya kupeana mikono |
| Uwakilishi | Jinsi ya kuhifadhi grafu | Matrix ya ukaribu dhidi ya orodha ya karibu |
| Miti | Grafu za acyclic zilizounganishwa | n wima → kingo n−1 |
| Wasafiri | Uchunguzi wa kipeo wa utaratibu | BFS (njia fupi), DFS (uchunguzi wa kina) |
| Njia fupi zaidi | Njia za uzani wa chini | Dijkstra, Bellman-Ford, Floyd-Warshall |
| Kiwango cha Chini cha Mti Unaoruka | Njia ya bei nafuu zaidi ya kuunganisha wima zote | Kruskal's, Prim |
| Mtiririko wa Mtandao | Upeo wa upitishaji | Ford-Fulkerson, nadharia ya max-flow min-cut |
| Nadharia ya Spectral | Thamani za Eigen zinaonyesha muundo | Eigenvalues ​​za Laplacian, nguzo za spectral |
Nadharia ya grafu bila shaka ndiyo tawi linalotumika moja kwa moja la hisabati kwa sayansi ya kisasa ya data. Mitandao ya kijamii, grafu za maarifa, miundo ya molekuli, grafu za ukokotoaji katika mifumo ya kina ya kujifunza, utatuzi wa utegemezi, mifumo ya mapendekezo - yote kimsingi ni matatizo ya grafu. Algorithms iliyofunikwa hapa sio ya kinadharia tu; zinaendeshwa kwa kiwango kikubwa katika mifumo ya uzalishaji kila siku.