<!--
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
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-10"
    author: "Nepoznato-Dev"
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

-->
# Teoryang Graph
Ang **graph** ay isang mathematical structure na binubuo ng mga vertices (node) na konektado ng mga gilid (links). Mga relasyon sa modelo ng mga graph: mga social network, mga mapa ng kalsada, mga neural network, mga dependency, mga channel ng komunikasyon. Graph theory — ang pag-aaral ng mga istrukturang ito — ay nagbibigay ng mga algorithm at theorems na sentro ng computer science, operations research, at data science.
---

## Mga Pangunahing Konsepto
### Mga Kahulugan
| Termino | Kahulugan | Notasyon |
|------|------------|----------|
| **Graph** | Isang pares G = (V, E) ng mga vertex at mga gilid | G |
| **Vertex (node)** | Isang elemento ng V | v, ikaw, w |
| **Gilid** | Isang koneksyon sa pagitan ng dalawang vertex | e = (u, v) o {u, v} |
| **Utos** | Bilang ng mga vertex | \|V\| = n |
| **Laki** | Bilang ng mga gilid | \|E\| = m |
| **Degree** | Bilang ng mga gilid na insidente sa isang vertex | deg(v) |
| **Path** | Pagkakasunud-sunod ng mga natatanging vertice na konektado sa pamamagitan ng mga gilid | v₁, v₂, ..., vₖ |
| **Ikot** | Isang landas na nagsisimula at nagtatapos sa parehong vertex | v₁ → v₂ → ... → vₖ → v₁ |
| **Nakakonekta** | May path sa pagitan ng bawat pares ng vertices | — |
| **Component** | Isang pinakamataas na konektadong subgraph | — |
| **Subgraph** | Isang graph na nabuo mula sa isang subset ng V at E | H ⊆ G |
### Mga Uri ng Graph
| Uri | Paglalarawan | Halimbawa |
|------|-------------|---------|
| **Hindi nakadirekta** | Ang mga gilid ay walang direksyon | Network ng pagkakaibigan |
| **Itinuro (digraph)** | Ang mga gilid ay may direksyon (mga arko) | Mga link sa web page |
| **Tinimbang** | Ang mga gilid ay may mga numerical na halaga | Mga distansya sa kalsada |
| **Walang timbang** | Ang lahat ng mga gilid ay katumbas | Mga social na koneksyon |
| **Simple** | Walang mga loop, walang maraming gilid | Karamihan sa mga graph ng aklat-aralin |
| **Multigraph** | Maramihang mga gilid sa pagitan ng parehong vertices pinapayagan | Mga ruta ng flight (maraming flight sa pagitan ng mga lungsod) |
| **Kumpleto** | Ang bawat pares ng vertices ay konektado | Ang Kₙ ay may n(n−1)/2 gilid |
| **Bipartite** | Nahati ang mga vertex sa dalawang grupo; mga gilid lang cross group | Mga matrice ng rekomendasyon ng user-item |
| **Planar** | Maaaring iguhit nang walang mga tawiran sa gilid | Mga layout ng circuit board |
| **Puno** | Nakakonekta, acyclic graph | Mga puno ng desisyon, mga file system |
| **DAG** | Nakadirekta, walang nakadirekta na mga cycle | Pag-iiskedyul ng gawain, mga graph ng dependency |
### The Handshaking Lemma
Ang kabuuan ng lahat ng vertex degrees ay katumbas ng dalawang beses sa bilang ng mga gilid:
Σᵥ deg(v) = 2|E|
**Corollary:** Ang bawat graph ay may even number ng odd-degree vertices.
**Halimbawa:** Sa isang party ng 10 tao kung saan ang lahat ay nakikipagkamay sa eksaktong 3 iba pa: Σ deg = 30, kaya |E| = 15 pagkakamay sa kabuuan.
---

## Mga Representasyon ng Graph
Kung paano mo iniimbak ang isang graph sa memorya ay tumutukoy sa kahusayan ng bawat algorithm na pinapatakbo mo dito.
| Kinatawan | Space | Edge Lookup | Ulitin ang mga Kapitbahay | Pinakamahusay Para sa |
|----------------|-------|------------|--------------------|----------|
| **Adjacency Matrix** | O(n²) | O(1) | O(n) | Mga siksik na graph, mabilis na mga pagsubok sa gilid |
| **Listahan ng Adjacency** | O(n + m) | O(deg(v)) | O(deg(v)) | Kalat-kalat na mga graph, karamihan sa mga real-world na network |
| **Edge List** | O(m) | O(m) | O(m) | Mga simpleng algorithm, Kruskal's MST |
| **Incidence Matrix** | O(n · m) | O(m) | O(m) | Mga dalubhasang algorithm |
### Adjacency Matrix
Isang n × n matrix A kung saan A[i][j] = 1 kung umiiral ang gilid (i,j), 0 kung hindi. Para sa mga weighted graph, A[i][j] = weight.
**Mga Katangian:**
- Symmetric para sa hindi nakadirekta na mga graph
- Aᵏ[i][j] = bilang ng mga lakaran sa haba k mula i hanggang j
- Ang Eigenvalues ng A ay nagpapakita ng mga katangian ng istruktura (tingnan ang Spectral Graph Theory)
### Listahan ng Adjacency
Isang array (o hash map) kung saan ang bawat vertex v ay nag-iimbak ng listahan ng mga kapitbahay nito.
```
Vertex 0: [1, 3]
Vertex 1: [0, 2, 3]
Vertex 2: [1, 3]
Vertex 3: [0, 1, 2]
```

Ito ang pinakakaraniwang representasyon para sa mga real-world na graph, na karaniwang kalat-kalat (m ≪ n²).
---

## Mga puno
Ang **puno** ay isang konektado, acyclic na hindi nakadirekta na graph. Ang **kagubatan** ay isang magkahiwalay na pagsasama ng mga puno.
### Mga Katangian ng Puno
Para sa isang punong may n vertex:
- Mayroon itong eksaktong n − 1 na mga gilid
- May eksaktong isang landas sa pagitan ng alinmang dalawang vertice
- Ang pag-alis ng anumang gilid ay madidiskonekta ito
- Ang pagdaragdag ng anumang gilid ay lumilikha ng eksaktong isang cycle
### Mga Uri ng Puno
| Uri | Paglalarawan | Application |
|------|-------------|-------------|
| **Nakaugat na puno** | Isang vertex na itinalaga bilang ugat | Mga sistema ng file, mga chart ng organisasyon |
| **Binary tree** | Ang bawat node ay may hindi hihigit sa 2 anak | Mga BST, expression parsing, decision tree |
| **Balanseng puno** | Ang taas ay O(log n) | AVL trees, red-black trees (mga database) |
| **Spanning tree** | Subgraph na kinabibilangan ng lahat ng vertex at isang puno | Disenyo ng network, mga algorithm ng approximation |
| **Minimum na spanning tree** | Spanning tree na may pinakamababang kabuuang bigat ng gilid | Disenyo ng network, clustering |
| **Star graph** | Isang gitnang node na konektado sa lahat ng iba pa | Hub-and-spoke network |
### Binary Tree Properties
| Ari-arian | Formula |
|----------|---------|
| Max node sa lalim d | 2ᵈ |
| Max node sa tree of height h | 2ʰ⁺¹ − 1 |
| Min na taas para sa n node | ⌊log₂(n)⌋ |
| Mga node ng dahon sa buong binary tree | Mga panloob na node + 1 |
### Mga Paglalakbay sa Puno
| Paglalakbay | Order | Use Case |
|-----------|-------|----------|
| **Pre-order** | Root → Kaliwa → Kanan | Pagkopya ng puno, prefix expression |
| **In-order** | Kaliwa → Root → Kanan | Pinagsunod-sunod na output mula sa BST |
| **Post-order** | Kaliwa → Kanan → Root | Pagtanggal ng puno, postfix expression |
| **Level-order (BFS)** | Antas ayon sa antas, kaliwa pakanan | Pinakamaikling landas sa walang timbang na puno |
---

## Mga Paglalakbay sa Graph
Binibisita ng mga traversal algorithm ang bawat maaabot na vertex nang sistematikong.
### Breadth-First Search (BFS)
I-explore ang mga vertices layer by layer, gamit ang **queue**.
| Ari-arian | Halaga |
|----------|-------|
| Istraktura ng data | Pila (FIFO) |
| Pagiging kumplikado ng oras | O(V + E) |
| Pagiging kumplikado ng espasyo | O(V) |
| Naghahanap ng pinakamaikling landas? | Oo (walang timbang na mga graph) |
| Kumpleto? | Oo (ginagalugad ang lahat ng naaabot na vertex) |
**Algorithm:**
1. Magsimula sa source vertex s. Bumisita si Mark. Enqueue s.
2. Habang ang pila ay walang laman: dequeue vertex u. Para sa bawat hindi nabisitang kapitbahay v ng u: mark v binisita, enqueue v.
**Aplikasyon:** pinakamaikling landas sa mga hindi natimbang na graph, konektadong mga bahagi, pagsubok ng bipartiteness, pag-crawl sa web.
### Depth-First Search (DFS)
Mag-explore nang mas malalim hangga't maaari bago mag-backtrack, gamit ang isang **stack** (o recursion).
| Ari-arian | Halaga |
|----------|-------|
| Istraktura ng data | Stack (LIFO) / recursion |
| Pagiging kumplikado ng oras | O(V + E) |
| Pagiging kumplikado ng espasyo | O(V) |
| Naghahanap ng pinakamaikling landas? | Hindi |
| Kumpleto? | Oo (para sa mga may hangganang graph) |
**Algorithm:**
1. Magsimula sa vertex s. Bumisita si Mark.
2. Para sa bawat hindi nabisitang kapitbahay v ng s: recursively DFS mula sa v.
**Inuuri ng DFS ang mga gilid sa:**
- **Mga gilid ng puno:** bahagi ng puno ng DFS
- **Mga gilid sa likod:** ikonekta ang isang vertex sa ninuno nito (ipahiwatig ang mga cycle)
- **Mga pasulong na gilid:** ikonekta ang isang vertex sa descendant nito
- **Cross edges:** ikonekta ang mga vertex sa iba't ibang sangay
**Aplikasyon:** topological sorting, cycle detection, malakas na konektadong mga bahagi, paglutas ng mga maze.
### Paghahambing ng BFS vs DFS
| Pamantayan | BFS | DFS |
|-----------|-----|-----|
| Diskarte | Malapad pagkatapos malalim | Malalim tapos malapad |
| Memorya | Mas mataas (mga tindahan ng hangganan) | Ibaba (nag-iimbak ng landas) |
| Pinakamaikling landas (walang timbang) | Garantisado | Hindi garantisadong |
| Gamitin kapag malapit nang magsimula ang solusyon | Mas mabuti | Mas masahol pa |
| Gamitin kapag ang graph ay napakalalim | Mas masahol pa | Mas mabuti |
| Topological na pag-uuri | Ang variant ng algorithm ng Kahn | Karaniwang diskarte |
---

## Pinakamaikling Path Algorithms
Ang paghahanap ng pinakamaikling landas sa pagitan ng mga vertice ay isa sa pinakamahalagang problema sa graph.
### Algorithm ni Dijkstra
Naghahanap ng pinakamaikling path mula sa iisang source hanggang sa lahat ng iba pang vertices sa isang graph na may **non-negative** edge weights.
| Ari-arian | Halaga |
|----------|-------|
| Mga timbang sa gilid | Dapat ay ≥ 0 |
| Oras (binary heap) | O((V + E) log V) |
| Oras (Fibonacci heap) | O(E + V log V) |
| Matakaw? | Oo |
| Hinahawakan ang mga negatibong timbang? | Hindi |
**Algorithm:**
1. Simulan ang dist[s] = 0, dist[v] = ∞ para sa lahat ng v ≠ s. Priority queue Q kasama ang lahat ng vertices.
2. Habang walang laman ang Q: i-extract ang vertex u na may pinakamababang dist. Para sa bawat kapitbahay v ng u na may gilid na timbang w: kung dist[u] + w < dist[v], i-update ang dist[v] = dist[u] + w.
**Nagtrabaho Halimbawa:**```
Graph: A --1-- B --2-- C --1-- D
       A --4-- C
       B --1-- D

Shortest paths from A:
A → B: 1 (direct)
A → D: 2 (A→B→D)
A → C: 3 (A→B→C, NOT A→C=4)
```

### Bellman-Ford Algorithm
Pinangangasiwaan ang **negatibong** mga timbang sa gilid at nakakakita ng mga negatibong cycle.
| Ari-arian | Halaga |
|----------|-------|
| Mga timbang sa gilid | Anuman (nakakakita ng mga negatibong cycle) |
| Pagiging kumplikado ng oras | O(V · E) |
| Pagiging kumplikado ng espasyo | O(V) |
| Pinangangasiwaan ang mga negatibong cycle? | Oo (nakita at iniulat) |
**Algorithm:**
1. Simulan ang dist[s] = 0, dist[v] = ∞ para sa lahat ng v ≠ s.
2. Ulitin ang V − 1 beses: para sa bawat gilid (u, v) na may timbang w: kung dist[u] + w < dist[v], i-update ang dist[v].
3. Suriin kung may mga negatibong cycle: kung ang anumang gilid ay maaari pa ring i-relax, mayroong negatibong cycle.
### Floyd-Warshall Algorithm
Naghahanap ng pinakamaikling landas sa pagitan ng **lahat ng mga pares** ng mga vertex.
| Ari-arian | Halaga |
|----------|-------|
| Pagiging kumplikado ng oras | O(V³) |
| Pagiging kumplikado ng espasyo | O(V²) |
| Hinahawakan ang mga negatibong timbang? | Oo (ngunit hindi mga negatibong cycle) |
| Diskarte | Dynamic na programming |
**Pag-ulit:** dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) para sa bawat intermediate vertex k.
### Gabay sa Pagpili ng Algorithm
| Sitwasyon | Algorithm |
|----------|-----------|
| Nag-iisang pinagmulan, hindi negatibong mga timbang | Dijkstra |
| Nag-iisang pinagmulan, posibleng mga negatibong timbang | Bellman-Ford |
| Lahat ng pares, siksik na graph | Floyd-Warshall |
| Lahat ng pares, kalat-kalat na graph | Patakbuhin ang Dijkstra mula sa bawat vertex |
| Walang timbang na graph | BFS |
| DAG (walang cycle) | Topological sort + relaxation |
| A* (heuristic-guided) | Isang* paghahanap (para sa paghahanap ng landas na may magandang heuristic) |
---

## Pinakamababang Spanning Tree
Isang **minimum spanning tree (MST)** ang nag-uugnay sa lahat ng vertices na may pinakamababang kabuuang bigat ng gilid.
### Mga Katangian
- Ang isang MST ay may eksaktong n − 1 gilid (para sa n vertices)
- May MST kung konektado ang graph
- Ang isang graph na may natatanging mga timbang sa gilid ay may natatanging MST
- Natutugunan ng MST ang **cut property**: ang pinakamababang timbang na gilid na tumatawid sa anumang hiwa ay kabilang sa MST
- Natutugunan ng MST ang **cycle property**: ang maximum-weight edge sa anumang cycle ay hindi kabilang sa MST
### Kruskal's Algorithm
| Ari-arian | Halaga |
|----------|-------|
| Diskarte | Matakaw — magdagdag ng mga gilid sa pagkakasunud-sunod ng timbang |
| Istraktura ng data | Disjoint-set (union-find) |
| Pagiging kumplikado ng oras | O(E log E) |
| Pinakamahusay para sa | Kalat-kalat na mga graph |
**Algorithm:**
1. Pagbukud-bukurin ang lahat ng mga gilid ayon sa timbang.
2. Para sa bawat gilid (sa pagkakasunud-sunod): kung ang pagdaragdag nito ay hindi lumikha ng isang cycle (suriin gamit ang union-find), idagdag ito sa MST.
3. Huminto kapag napili ang n − 1 mga gilid.
### Prim's Algorithm
| Ari-arian | Halaga |
|----------|-------|
| Diskarte | Matakaw — lumaki ang puno mula sa isang panimulang taluktok |
| Istraktura ng data | Priyoridad na pila (min-heap) |
| Pagiging kumplikado ng oras | O(E log V) na may binary heap |
| Pinakamahusay para sa | Mga siksik na graph |
**Algorithm:**
1. Magsimula sa anumang vertex. Markahan ito bilang bahagi ng MST.
2. Paulit-ulit na idagdag ang gilid na may pinakamababang timbang na kumukonekta sa isang vertex sa MST sa isang vertex sa labas nito.
3. Huminto kapag kasama na ang lahat ng vertices.
### MST Application
| Application | Paano Nakakatulong ang MST |
|-------------|----------------|
| Disenyo ng network | Maglagay ng pinakamababang cable/pipe para ikonekta ang lahat ng lokasyon |
| Pag-cluster | Alisin ang k − 1 pinakamahabang mga gilid ng MST upang makakuha ng mga k cluster |
| Mga algorithm ng pagtatantya | 2-approximation para sa metric TSP |
| Pag-segment ng larawan | Ipangkat ang mga pixel ayon sa MST ng pagkakatulad ng kulay |
| Pag-aalis ng tampok | Alisin ang mga redundant na feature gamit ang MST ng correlation graph |
---

## Daloy ng Network
Ang mga problema sa daloy ng network ay modelo ng paggalaw ng mga mapagkukunan sa pamamagitan ng isang system.
### Depinisyon ng Daloy ng Network
Ang **flow network** ay isang nakadirekta na graph na may:
- Isang **source** vertex s (gumagawa ng daloy)
- Isang **sink** vertex t (kumokonsumo ng daloy)
- **Mga Kapasidad** c(u,v) ≥ 0 sa bawat gilid
- **Daloy** f(u,v) kasiya-siya:
  - **Pagpigil sa kapasidad:** 0 ≤ f(u,v) ≤ c(u,v)
  - **Pag-iingat ng daloy:** daloy papasok = daloy palabas sa bawat taluktok maliban sa s at t
### Problema sa Pinakamataas na Daloy
Hanapin ang maximum na kabuuang daloy mula s hanggang t.
**Paraan ng Ford-Fulkerson:**
1. Habang mayroong isang nagpapalaki na landas mula s hanggang t sa natitirang graph:
2. Hanapin ang bottleneck capacity sa daan
3. Palakihin ang daloy sa daanan ng halaga ng bottleneck
4. I-update ang mga natitirang kapasidad
| Algorithm | Pagiging Kumplikado ng Oras | Mga Tala |
|-----------|----------------|-------|
| Ford-Fulkerson (DFS) | O(m · f*) kung saan ang f* ay max flow | Maaaring hindi magwakas nang may hindi makatwirang mga kapasidad |
| Edmonds-Karp (BFS) | O(V · E²) | Palaging nagtatapos, pinipili ang pinakamaikling landas ng pagpapalaki |
| Algorithm ni Dinic | O(V² · E) | Gumagamit ng pagharang sa mga daloy; O(V^(1/2) · E) para sa mga kapasidad ng unit |
### Max-Flow Min-Cut Theorem
Ang **maximum flow** mula s hanggang t ay katumbas ng **minimum cut** capacity na naghihiwalay sa s mula sa t.
A **cut** (S, T) partition vertices sa S (naglalaman ng s) at T (naglalaman ng t). Ang kapasidad ng hiwa ay ang kabuuan ng mga kapasidad ng mga gilid mula S hanggang T.
**Mga application ng max flow:**
- Bipartite matching (magtalaga ng mga manggagawa sa mga trabaho)
- Pagse-segment ng imahe (paghiwalayin ang foreground mula sa background)
- Pag-aalis ng Baseball (panalo pa kaya ang team X?)
- Pagiging maaasahan ng network (maximum na data throughput)
### Pagtutugma ng Bipartite sa pamamagitan ng Max Flow
Dahil sa bipartite graph G = (L ∪ R, E):
1. Magdagdag ng source s na may mga gilid sa lahat ng vertices sa L (kapasidad 1)
2. Magdagdag ng sink t na may mga gilid mula sa lahat ng vertices sa R (kapasidad 1)
3. Itakda ang lahat ng orihinal na kapasidad sa gilid sa 1
4. Pinakamataas na daloy = maximum na pagtutugma
---

## Teorya ng Spectral Graph
Ang teorya ng spectral graph ay nag-aaral ng mga graph sa pamamagitan ng eigenvalues ​​at eigenvectors ng mga matrice na nauugnay sa graph.
### Mga Pangunahing Matrice
| Matrix | Kahulugan | Ano ang Kinukuha Nito |
|--------|------------|------------------|
| **Adjacency matrix** A | A[i][j] = 1 kung may gilid (i,j) | Pattern ng pagkakakonekta |
| **Degree matrix** D | dayagonal; D[i][i] = deg(i) | Kahalagahan ng Vertex ayon sa antas |
| **Laplacian** L = D − A | L[i][j] = −1 kung gilid, deg(i) sa dayagonal | Smoothness ng mga function sa graph |
| **Normalized Laplacian** L_norm = D^(−1/2) L D^(−1/2) | Scale-invariant na bersyon | Istraktura ng komunidad |
### Mga Eigenvalues ​​ng Laplacian
Ang Laplacian L ay positibong semi-definite, kaya lahat ng eigenvalues ​​ay ≥ 0.
| Eigenvalue | Ibig sabihin |
|------------|---------|
| λ₁ = 0 | Laging zero; Ang eigenvector ay ang pare-parehong vector |
| λ₂ (algebraic na pagkakakonekta) | > 0 iff graph ay konektado; mas malaki = mas mahusay na konektado |
| Bilang ng mga zero eigenvalues ​​| Katumbas ng bilang ng mga konektadong bahagi |
| λₙ | Nauugnay sa maximum na antas at pagpapalawak ng graph |
### Mga Application ng Spectral Methods
| Application | Paraan |
|-------------|--------|
| **Paghahati ng graph** | Gumamit ng eigenvectors ng L upang hatiin ang graph sa mga balanseng bahagi |
| **Deteksyon ng komunidad** | Spectral clustering: mag-embed ng mga vertices gamit ang lower eigenvectors, pagkatapos ay cluster |
| **PageRank** | Eigenvector ng adjacency matrix (o transition matrix) ng web graph |
| **Pagguhit ng graph** | Iposisyon ang mga vertices gamit ang eigenvectors ng Laplacian |
| **Semi-supervised learning** | I-propagate ang mga label gamit ang graph na Laplacian (label propagation) |
| **Graph neural network** | Spectral convolutions: mga signal ng filter sa mga graph gamit ang eigenvectors ng L |
### Hindi Pagkakapantay-pantay ni Cheeger
Iniuugnay ang pangalawang eigenvalue λ₂ sa **pagpapalawak** ng graph (kung gaano ito kahusay):
λ₂ / 2 ≤ h(G) ≤ √(2λ₂)
kung saan ang h(G) ay ang Cheeger constant (isoperimetric number). Nangangahulugan ito na tinatayang sinusukat ng λ₂ kung gaano kahirap i-cut ang graph sa dalawang piraso — isang mahalagang insight para sa clustering.
---

## Mga Espesyal na Istruktura ng Graph
| Graph | Vertices | Mga gilid | Mga Katangian |
|-------|----------|-------|------------|
| Kumpletuhin ang Kₙ | n | n(n−1)/2 | Ang bawat pares ay konektado; diameter 1 |
| Ikot Cₙ | n | n | 2-regular; konektado |
| Landas Pₙ | n | n−1 | Puno; diameter n−1 |
| Hypercube Qₖ | 2ᵏ | k·2ᵏ⁻¹ | k-regular; diameter k; dalawang partido |
| Kumpletuhin ang bipartite K_{m,n} | m+n | m·n | Ang bawat vertex sa isang bahagi ay kumokonekta sa lahat sa iba pang |
| Petersen graph | 10 | 15 | 3-regular; diameter 2; hindi planar; walang Hamiltonian cycle |
---

## Kaugnayan sa Machine Learning at Data Science
| Konsepto ng Graph | Application |
|--------------|-------------|
| BFS / DFS | Pag-crawl sa web, pagsusuri sa social network, pag-label ng konektadong bahagi |
| Dijkstra / A* | Pagpaplano ng ruta, laro AI pathfinding, robotics navigation |
| Pinakamababang spanning tree | Clustering (single-linkage), pagpili ng tampok, disenyo ng network |
| Max na daloy / min cut | Pagse-segment ng larawan, pagtutugma ng bipartite, pagtatalaga ng rekomendasyon |
| Mga pamamaraan ng parang multo | Spectral clustering, graph neural network, pagbawas ng dimensionality (Laplacian eigenmaps) |
| PageRank | Pagraranggo ng search engine, pagsusuri ng impluwensya sa mga social network |
| Mga DAG | Bayesian network, causal inference, task scheduling, computation graphs sa deep learning |
| Mga bipartite na graph | Mga matrice ng user-item sa mga recommender system, dalawang panig na market |
| Mga istruktura ng puno | Decision tree, random na kagubatan, hierarchical clustering, file system navigation |
| Mga representasyon ng graph | Mga graph ng kaalaman (Wikidata, DBpedia), mga molecular graph (pagtuklas ng droga), mga network ng pagsipi |
---

## Buod
| Paksa | Pangunahing Ideya | Key Algorithm / Resulta |
|-------|-----------|----------------------|
| Mga Pangunahing Kaalaman | Vertices, gilid, degree, path | Pagkamay lemma |
| Mga Kinatawan | Paano mag-imbak ng mga graph | Adjacency matrix vs adjacency list |
| Puno | Mga konektadong acyclic graph | n vertices → n−1 gilid |
| Mga Paglalakbay | Systematic vertex exploration | BFS (pinakamaikling landas), DFS (deep exploration) |
| Pinakamaikling Landas | Mga rutang may pinakamababang timbang | Dijkstra, Bellman-Ford, Floyd-Warshall |
| Pinakamababang Spanning Tree | Pinakamurang paraan upang ikonekta ang lahat ng vertices | Kruskal's, Prim's |
| Daloy ng Network | Pinakamataas na throughput | Ford-Fulkerson, max-flow min-cut theorem |
| Spectral Theory | Ang Eigenvalues ​​ay nagpapakita ng istraktura | Laplacian eigenvalues, spectral clustering |
Ang teorya ng graph ay arguably ang pinaka direktang naaangkop na sangay ng matematika sa modernong data science. Ang mga social network, mga graph ng kaalaman, mga istrukturang molekular, mga graph ng pagkalkula sa mga framework ng malalim na pag-aaral, paglutas ng dependency, mga sistema ng rekomendasyon — lahat ay pangunahing mga problema sa graph. Ang mga algorithm na sakop dito ay hindi lamang teoretikal; tumatakbo sila sa sukat sa mga sistema ng produksyon araw-araw.