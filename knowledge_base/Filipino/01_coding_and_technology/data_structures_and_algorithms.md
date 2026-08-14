---
# Metadata
title: "Data Structures and Algorithms"
description: "Arrays, trees, graphs, sorting, searching, complexity"
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
tags: [data, structures, algorithms, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Mga Istraktura ng Data at Algorithm
Ang mga istruktura ng data ay ang mga paraan ng pag-aayos ng data sa memorya upang ang mga operasyon dito ay mahusay. Ang mga algorithm ay ang mga hakbang-hakbang na pamamaraan para sa paglutas ng mga problema. Magkasama, sila ang bumubuo sa pundasyon ng computer science — lahat ng program na ginamit mo ay umaasa sa kanila. Ang pagpili ng tamang istraktura ng data ay maaaring gawing mabilis ang isang napakabagal na programa, at ang pag-alam sa tamang algorithm ay maaaring gawing isang maliit na problema ang isang hindi malulutas na problema.
---

## Mga Pangunahing Istruktura ng Data
### Mga Linear na Istraktura
| Istraktura | Access | Maghanap | Ipasok | Tanggalin | Use Case |
|-----------|--------|--------|--------|--------|----------|
| **Array** | O(1) ayon sa index | O(n) | O(n) | O(n) | Fixed-size na mga koleksyon; random na pag-access |
| **Listahan ng Naka-link** | O(n) | O(n) | O(1) sa ulo | O(1) sa ulo | Dynamic na laki; mga pagpapasok/pagtanggal |
| **Stack** | O(n) | O(n) | O(1) push/pop | O(1) pop | Mga function na tawag; i-undo; pag-parse |
| **Pila** | O(n) | O(n) | O(1) enqueue | O(1) dequeue | Pag-iiskedyul ng gawain; BFS; mga pila ng mensahe |
| **Deque** | O(1) sa magkabilang dulo | O(n) | O(1) sa magkabilang dulo | O(1) sa magkabilang dulo | Sliding window; pagnanakaw ng trabaho |
### Mga Istraktura na Nakabatay sa Hash
| Istraktura | Maghanap | Ipasok | Tanggalin | Use Case |
|-----------|--------|--------|--------|----------|
| **Hash Table** | O(1) average | O(1) average | O(1) average | Key-value lookups; mga cache; set |
| **Hash Set** | O(1) | O(1) | O(1) | Pagsubok sa pagiging miyembro; deduplikasyon |
**Mga banggaan ng hash**: kapag nagha-hash ang dalawang key sa iisang slot, iniimbak ang mga ito sa isang naka-link na listahan (chaining) o sa susunod na available na slot (open addressing). Ang mga magagandang hash function ay nagpapaliit ng mga banggaan.
### Mga Istraktura ng Puno
| Istraktura | Maghanap | Ipasok | Tanggalin | Use Case |
|-----------|--------|--------|--------|----------|
| **Binary Search Tree** | O(log n) average | O(log n) | O(log n) | Pinagsunod-sunod na data; hanay ng mga query |
| **AVL / Pula-Itim na Puno** | O(log n) garantisadong | O(log n) | O(log n) | Pagbalanse sa sarili; ginamit sa mga mapa/set |
| **B-Tree / B+ Tree** | O(log n) | O(log n) | O(log n) | Mga index ng database; file system |
| **Subukan** | O(k) kung saan k = haba ng key | O(k) | O(k) | Autocomplete; pagtutugma ng prefix |
| **Bunton (Binary)** | O(n) | O(log n) | O(log n) | Mga priyoridad na pila; pag-iiskedyul |
### Mga Representasyon ng Graph
| Kinatawan | Space | Edge Lookup | Magdagdag ng Edge | Ulitin ang mga Kapitbahay |
|--------------|-------|------------|----------|-------------------|
| **Adjacency matrix** | O(V²) | O(1) | O(1) | O(V) |
| **Listahan ng adjacency** | O(V + E) | O(degree) | O(1) | O(degree) |
| **Listahan ng gilid** | O(E) | O(E) | O(1) | O(E) |
---

## Pagiging Kumplikado ng Algorithm (Big-O)
Inilalarawan ng Big-O notation kung paano lumalaki ang mga kinakailangan sa oras o espasyo ng algorithm habang tumataas ang laki ng input.
| Pagiging kumplikado | Pangalan | Halimbawa |
|-----------|------|---------|
| **O(1)** | pare-pareho | Hash table lookup; array access sa pamamagitan ng index |
| **O(log n)** | Logarithmic | Binary na paghahanap; balanseng pagpapatakbo ng puno |
| **O(n)** | Linear | Linear na paghahanap; inuulit ang isang array |
| **O(n log n)** | Linearithmic | Pagsamahin ang pag-uuri; uri ng bunton; pinaka mahusay na pangkalahatang layunin na mga uri |
| **O(n²)** | Quadratic | Bubble sort; nested na mga loop sa parehong data |
| **O(2^n)** | Exponential | Brute-force subset generation; walang muwang recursive Fibonacci |
| **O(n!)** | Factorial | Naglalakbay na tindero (brute force); mga permutasyon |
### Mga Karaniwang Maling Palagay
| Maling akala | Realidad |
|--------------|---------|
| "Ang O(n) ay palaging mas mabilis kaysa sa O(n²)" | Para sa maliit na n, mas mahalaga ang pare-parehong kadahilanan |
| "Ang Lower Big-O ay palaging mas mahusay" | May mga space-time trade-off; Ang O(1) lookup ay gumagamit ng O(n) memory |
| "Sinasabi sa iyo ng Big-O ang eksaktong bilis" | Inilalarawan nito ang rate ng paglago, hindi ganap na oras |
---

## Pag-uuri ng Algorithm
| Algorithm | Pinakamahusay | Karaniwan | Pinakamasama | Space | Matatag | In-Place |
|-----------|------|---------|-------|-------|--------|----------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Oo | Oo |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Oo | Oo |
| **Pag-uuri-uriin ng Pinili** | O(n²) | O(n²) | O(n²) | O(1) | Hindi | Oo |
| **Pagsamahin ang Pag-uuri** | O(n log n) | O(n log n) | O(n log n) | O(n) | Oo | Hindi |
| **Mabilis na Pag-uuri** | O(n log n) | O(n log n) | O(n²) | O(log n) | Hindi | Oo |
| **Pagbukud-bukurin** | O(n log n) | O(n log n) | O(n log n) | O(1) | Hindi | Oo |
| **Tim Sort** | O(n) | O(n log n) | O(n log n) | O(n) | Oo | Hindi |
**Praktikal na payo**: gamitin ang built-in na uri ng iyong wika (Python's`sorted()`, JavaScript's`Array.sort()`). Gumagamit sila ng lubos na na-optimize na mga algorithm (Tim Sort, Introsort) na humahawak sa lahat ng edge case.
---

## Paghahanap ng Algorithm
| Algorithm | Istruktura ng Data | Pagiging kumplikado | Kinakailangan |
|-----------|----------------|-----------|-------------|
| **Linear na paghahanap** | Anumang | O(n) | Wala |
| **Binary na paghahanap** | Pinagsunod-sunod na array | O(log n) | Dapat ayusin ang data |
| **Hash table lookup** | Hash table | O(1) average | Magandang hash function |
| **BFS** (Breadth-First Search) | Graph / puno | O(V + E) | Hindi natimbang na pinakamaikling landas |
| **DFS** (Depth-First Search) | Graph / puno | O(V + E) | Paghahanap ng landas; cycle detection |
| **Ni Dijkstra** | Natimbang na graph | O((V + E) log V) | Mga di-negatibong timbang; pinakamaikling landas |
| **A* Search** | Natimbang na graph | O((V + E) log V) | Heuristic-guided; pinakamainam na may tinatanggap na heuristic |
---

## Mga Key Algorithm Pattern
| Pattern | Paglalarawan | Mga Halimbawang Problema |
|---------|-------------|----------------|
| **Hatiin at lupigin** | Hatiin ang problema sa mga sub-problema; malutas ang recursively; pagsamahin | Pagsamahin ang pag-uuri; quicksort; binary na paghahanap |
| **Dynamic na programming** | Hatiin ang magkakapatong na mga sub-problema; mga resulta ng cache | Fibonacci; knapsack; pinakamahabang karaniwang kasunod |
| **Sakim** | Gawin ang lokal na pinakamainam na pagpipilian sa bawat hakbang | ni Dijkstra; Huffman coding; pagpili ng aktibidad |
| **Backtracking** | Subukan ang mga posibilidad; i-undo ang masasamang pagpili; subukan ang mga alternatibo | Sudoku solver; N-reyna; mga permutasyon |
| **Sliding window** | Panatilihin ang isang window ng mga elemento; i-slide ito sa buong data | Maximum sum subarray ng laki K; pinakamahabang substring na walang inuulit |
| **Dalawang pointer** | Gumamit ng dalawang pointer na gumagalaw patungo sa isa't isa o sa parehong direksyon | Ipares ang kabuuan sa pinagsunod-sunod na array; alisin ang mga duplicate |
| **Binary na paghahanap sa sagot** | Binary search ang answer space | Maglaan ng pinakamababang pahina; agresibong baka |
---

## Kailan Gamitin ang Ano
| Problema | Istruktura ng Data | Algorithm |
|---------|----------------|-----------|
| Mabilis na key-value lookup | Hash table / diksyunaryo | Hashing |
| Panatilihin ang pinagsunod-sunod na order | Balanseng BST (TreeMap, std::set) | Mga pagpapatakbo ng puno |
| Pagproseso na nakabatay sa priyoridad | Heap / priority queue | Mga pagpapatakbo ng heap |
| Pinakamaikling landas (walang timbang) | Graph (listahan ng katabi) | BFS |
| Pinakamaikling landas (timbang) | Graph (listahan ng katabi) | Dijkstra's / A* |
| Pagsubok sa membership | Hash set / Bloom filter | Hashing |
| Pagtutugma ng prefix | Subukan | Subukan ang paglalakbay |
| Mga query sa hanay | Puno ng segment / puno ng Fenwick | Mga pagpapatakbo ng puno |
| LRU cache | Hash map + dobleng naka-link na listahan | Pinagsamang mga operasyon |
| Mga konektadong bahagi | Disjoint Set Union (Union-Find) | Union at Hanapin |
---

## Buod
Ang mga istruktura at algorithm ng data ay hindi lamang mga paksa sa pakikipanayam — ang mga ito ay ang mga bloke ng pagbuo ng mahusay na software. Pinangangasiwaan ng mga array at hash table ang karamihan sa pang-araw-araw na pangangailangan. Pinangangasiwaan ng mga puno at graph ang hierarchical at relational na data. Ang pag-uuri at paghahanap ay malulutas ang mga problema sa karaniwang mga aklatan. Ang mga algorithmic pattern — hatiin at lupigin, dynamic na programming, matakaw, backtracking — ay magagamit muli na mga diskarte para sa pagharap sa mga bagong problema. Ang pangunahing kasanayan ay hindi pagsasaulo ng mga algorithm; ito ay pagkilala kung aling pattern ang akma sa isang partikular na problema at pagpili ng tamang istraktura ng data para sa trabaho.