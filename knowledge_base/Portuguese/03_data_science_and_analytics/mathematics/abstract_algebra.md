---
# Metadata
title: "Abstract Algebra"
description: "Groups, subgroups, homomorphisms, rings, fields, vector spaces, linear maps, eigen theory, and applications in coding theory and quantum computing"
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
    changes: "Initial deep-dive into abstract algebra"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [abstract-algebra, groups, rings, fields, vector-spaces, linear-maps, eigen-theory, coding-theory, quantum-computing]
difficulty_level: "advanced"
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
# Álgebra Abstrata
A álgebra abstrata estuda estruturas algébricas – conjuntos equipados com operações que seguem regras específicas. Em vez de trabalhar com números, a álgebra abstrata funciona com quaisquer objetos que satisfaçam os axiomas. Esta generalidade é poderosa: um teorema provado para “grupos” aplica-se simultaneamente a números inteiros, simetrias, matrizes, permutações e estados quânticos. A álgebra abstrata sustenta a criptografia, os códigos de correção de erros, a computação quântica e a análise de simetria usada em toda a física.
---

## Grupos
Um **grupo** é a estrutura algébrica mais fundamental. Ele captura a essência da simetria.
### Definição
Um **grupo** (G, ∗) é um conjunto G com uma operação binária ∗ satisfatória:
| Axioma | Declaração | Exemplo (ℤ, +) |
|-------|-----------|-----------------|
| **Encerramento** | ∀a,b ∈ G: a ∗ b ∈ G | a + b é um número inteiro |
| **Associatividade** | (a ∗ b) ∗ c = a ∗ (b ∗ c) | (a + b) + c = a + (b + c) |
| **Identidade** | ∃e ∈ G: e ∗ a = a ∗ e = a | 0 + uma = uma + 0 = uma |
| **Inverso** | ∀a ∈ G, ∃a⁻¹: a ∗ a⁻¹ = a⁻¹ ∗ a = e | uma + (−a) = 0 |
Se a operação também for **comutativa** (a ∗ b = b ∗ a), o grupo é denominado **abeliano**.
### Exemplos de grupos
| Grupo | Definir | Operação | Identidade | Inverso | Abeliano? |
|-------|-----|-----------|----------|---------|----------|
| (ℤ, +) | Inteiros | Adição | 0 | −a | Sim |
| (ℚ*, ×) | Racionais diferentes de zero | Multiplicação | 1 | 1/um | Sim |
| (ℤ/nℤ, +) | Resíduos mod n | Adição mod n | [0] | [n−a] | Sim |
| Sₙ | Permutações de {1,...,n} | Composição | identificação | Permutação inversa | Não (n ≥ 3) |
| GL(n, ℝ) | Matrizes n×n invertíveis | Multiplicação de matrizes | Euₙ | A⁻¹ | Não (n ≥ 2) |
| (ℝⁿ, +) | vetores n-dimensionais | Adição de vetores | 0 | −v | Sim |
### Ordem de um grupo e elementos
| Prazo | Definição | Exemplo |
|------|------------|--------|
| **Ordem de G** (\|G\|) | Número de elementos em G | \|ℤ/5ℤ\| = 5 |
| **Ordem do elemento a** (ord(a)) | Menor k positivo com aᵏ = e | ord(2) em (ℤ/7ℤ)* = 3 (já que 2³ = 8 ≡ 1) |
| **Grupo finito** | \|G\| é finito | S₃ tem pedido 6 |
| **Grupo infinito** | \|G\| é infinito | (ℤ, +) |
### Subgrupos
Um **subgrupo** H de G é um subconjunto H ⊆ G que é ele próprio um grupo sob a mesma operação.
**Teste de subgrupo:** H é um subgrupo de G se:
1. H não é vazio
2. Para todo a, b ∈ H: a ∗ b⁻¹ ∈ H
**Exemplos:**
- (ℤ, +) tem subgrupos nℤ = {..., −2n, −n, 0, n, 2n, ...} para cada n ≥ 0
- O **subgrupo trivial** {e} e o próprio grupo G são sempre subgrupos
- Em S₃, o conjunto {id, (12)} é um subgrupo de ordem 2
### Cosets e Teorema de Lagrange
Para um subgrupo H de G e elemento a ∈ G:
- **Coset esquerdo:** aH = {ah : h ∈ H}
- **Coset certo:** Ha = {ha : h ∈ H}
**Teorema de Lagrange:** Para um grupo finito G e subgrupo H:
|H| divide |G|
**Corolários:**
- A ordem de cada elemento divide |G|
- Se |G| = p (primo), então G é cíclico (não tem subgrupos não triviais)
- uma^|G| = e para todo a ∈ G (generaliza o Pequeno Teorema de Fermat)
### Grupos Cíclicos
Um grupo G é **cíclico** se existe g ∈ G tal que todo elemento de G é uma potência de g. Escrevemos G = ⟨g⟩.
| Propriedade | Declaração |
|----------|-----------|
| Todo grupo cíclico é abeliano | — |
| ℤ/nℤ adicionado é cíclico | Gerado por [1] |
| (ℤ/pℤ)* é cíclico para primo p | Gerador é chamado de raiz primitiva |
| Classificação | Todo grupo cíclico finito é isomórfico a ℤ/nℤ para algum n |
---

## Homomorfismos e Isomorfismos
Um **homomorfismo** é um mapa que preserva a estrutura entre grupos.
### Definições
| Prazo | Definição | Exemplo |
|------|------------|--------|
| **Homomorfismo** | φ: G → H onde φ(ab) = φ(a)φ(b) | det: GL(n,ℝ) → ℝ* |
| **Isomorfismo** | Um homomorfismo bijetivo (os grupos são "iguais") | (ℤ/6ℤ) ≅ (ℤ/2ℤ) × (ℤ/3ℤ) |
| **Núcleo** | ker(φ) = {g ∈ G : φ(g) = e_H} | ker(det) = SL(n, ℝ) |
| **Imagem** | im(φ) = {φ(g) : g ∈ G} | eu(det) = ℝ* |
### Primeiro Teorema do Isomorfismo
Se φ: G → H é um homomorfismo, então:
G / ker(φ) ≅ im(φ)
Este é um dos teoremas mais importantes da álgebra – diz que todo homomorfismo se decompõe em um quociente seguido por um isomorfismo.
---

## Anéis
Um **anel** adiciona uma segunda operação a um grupo, modelando aritmética com adição e multiplicação.
### Definição
Um **anel** (R, +, ×) é um conjunto R com duas operações que satisfazem:
| Axioma | Declaração |
|-------|-----------|
| (R, +) é um grupo abeliano | A adição é comutativa, associativa, possui identidade 0, todo elemento possui inverso aditivo |
| A multiplicação é associativa | (a × b) × c = a × (b × c) |
| Leis distributivas | a(b + c) = ab + ac e (a + b)c = ac + bc |
Se a multiplicação também for comutativa e tiver identidade (1), R é um **anel comutativo com unidade**.
### Exemplos de anéis
| Anel | Descrição | Comutativo? | Tem 1? |
|------|---------|-------------|--------|
| (ℤ, +, ×) | Inteiros | Sim | Sim |
| (ℚ, +, ×) | Racionais | Sim | Sim |
| (ℝ, +, ×) | Números reais | Sim | Sim |
| (ℤ/nℤ, +, ×) | Mod inteiro n | Sim | Sim |
| Mₙ(ℝ) | n×n matrizes reais | Não (n ≥ 2) | Sim |
| ℝ[x] | Polinômios com coeficientes reais | Sim | Sim |
### Ideais e anéis de quociente
Um **ideal** I de um anel R é um subconjunto que:
1. É um subgrupo em adição
2. Absorve multiplicação: para todo r ∈ R e a ∈ I, ambos ra ∈ I e ar ∈ I
**Anel de quociente** R/I: os elementos são coconjuntos de I, com operações herdadas de R.
**Exemplo:** ℤ/nℤ = ℤ/nℤ é o quociente de ℤ pelo nℤ ideal.
### Domínios e Campos Integrais
| Estrutura | Definição | Exemplos |
|-----------|------------|----------|
| **Domínio integral** | Anel comutativo com 1, sem divisores de zero (ab = 0 → a = 0 ou b = 0) | ℤ, ℚ[x], ℝ[x] |
| **Campo** | Anel comutativo onde todo elemento diferente de zero possui um inverso multiplicativo | ℚ, ℝ, ℂ, ℤ/pℤ (p linha) |
---

## Campos
Os campos são os objetos algébricos mais estruturados de uso comum. Todo elemento diferente de zero pode ser adicionado, subtraído, multiplicado e dividido.
### Principais Propriedades
| Propriedade | Declaração |
|----------|-----------|
| Todo campo é um domínio integral | — |
| Todo domínio integral finito é um corpo | — |
| Característica | Menor n com n·1 = 0, ou 0 se tal n não existir |
| char(ℚ) = char(ℝ) = char(ℂ) | = 0 |
| char(ℤ/pℤ) | = p (para p primo) |
### Campos Finitos (Campos de Galois)
Para cada potência primária pᵏ, existe um campo finito único (até o isomorfismo) de ordem pᵏ, denotado GF(pᵏ) ou 𝔽_{pᵏ}.
| Campo | Tamanho | Construção | Aplicação |
|-------|------|-------------|-------------|
| FG(2) | 2 | {0, 1} módulo 2 | Aritmética binária, XOR |
| GF(2ᵏ) | 2ᵏ | Polinômios mod poli irredutível sobre GF(2) | Criptografia AES, códigos CRC |
| FG(p) | p | ℤ/pℤ para primo p | Aritmética modular, teoria da codificação |
| GF(pᵏ) | pᵏ | Campos de extensão | Códigos Reed-Solomon, curvas elípticas |
**Construção de GF(2⁸)** (usado em AES):
- Comece com GF(2) = {0, 1}
- Escolha o polinômio irredutível p(x) = x⁸ + x⁴ + x³ + x + 1 sobre GF(2)
- Os elementos são polinômios de grau <8 com coeficientes em GF(2)
- Aritmética: adição polinomial (XOR) e multiplicação mod p(x)
---

## Espaços vetoriais
Um **espaço vetorial** é um conjunto de vetores que podem ser adicionados e escalonados, formando a base da álgebra linear.
### Definição
Um **espaço vetorial** V sobre um corpo F é um conjunto com:
- Adição de vetores: V × V → V (tornando V um grupo abeliano)
- Multiplicação escalar: F × V → V
Satisfatório: associatividade, comutatividade da adição, distributividade da multiplicação escalar e 1·v = v.
### Conceitos-chave
| Conceito | Definição | Exemplo |
|--------|------------|---------|
| **Base** | Conjunto gerador linearmente independente | {e₁, e₂, ..., eₙ} para Fⁿ |
| **Dimensão** | Número de vetores em qualquer base | dim(ℝ³) = 3 |
| **Subespaço** | Subconjunto fechado sob adição e multiplicação escalar | Um plano que passa pela origem em ℝ³ |
| **Combinação linear** | Σ cᵢvᵢ onde cᵢ ∈ F | 3v₁ + 2v₂ − v₃ |
| **Período** | Conjunto de todas as combinações lineares | Span({v₁, v₂}) = plano se v₁, v₂ independente |
| **Independência linear** | Nenhum vetor é uma combinação linear de outros | e₁, e₂, e₃ em ℝ³ |
### Espaços vetoriais importantes
| Espaço | Descrição | Dimensão |
|-------|------------|-----------|
| Fⁿ | n-tuplas no campo F | n |
| Pₙ(F) | Polinômios de grau ≤ n | n+1 |
| Mₘₓₙ(F) | Matrizes m × n sobre F | homem |
| C[a,b] | Funções contínuas em [a,b] | Infinito |
| L²(ℝ) | Funções quadradas integráveis ​​| Infinito (espaço de Hilbert) |
---

## Mapas Lineares e Teoria Eigen
### Mapas Lineares
Um **mapa linear** (transformação linear) T: V → W satisfaz:
- T(u + v) = T(u) + T(v)
- T(cv) = cT(v) para todos os escalares c
| Conceito | Definição | Exemplo |
|--------|------------|---------|
| **Núcleo** | {v ∈ V : T(v) = 0} | Espaço nulo de uma matriz |
| **Imagem** | {T(v) : v ∈ V} | Espaço de coluna de uma matriz |
| **Teorema da Nulidade de Classificação** | dim(ker T) + dim(im T) = dim(V) | Restrição fundamental |
| **Representação matricial** | T(v) = Av para alguma matriz A | Todo mapa linear entre espaços de dimensão finita |
### Valores próprios e vetores próprios
Para um mapa linear T: V → V (ou matriz A):
**Equação de autovalor:** Av = λv, onde v ≠ 0
| Prazo | Definição |
|------|------------|
| **Autovalor** λ | Escalar tal que Av = λv para algum v ≠ 0 |
| **Vetor próprio** v | Vetor diferente de zero satisfazendo Av = λv |
| **Polinômio característico** | det(A − λI) = 0 |
| **Espaço próprio** | {v : Av = λv} — o conjunto de todos os autovetores para λ (mais 0) |
| **Espectro** | Conjunto de todos os autovalores |
### Calculando valores próprios
Para uma matriz 2×2 A = [[a, b], [c, d]]:
- Polinômio característico: λ² − (a+d)λ + (ad−bc) = 0
- λ = ((a+d) ± √((a+d)² − 4(ad−bc))) / 2
**Principais propriedades:**
- Soma dos autovalores = traço (A) = soma dos elementos diagonais
- Produto de autovalores = det(A)
### Diagonalização
Uma matriz A é **diagonalizável** se tiver n autovetores linearmente independentes (onde A é n×n).
Se A = PDP⁻¹ onde D é diagonal:
- Aᵏ = PDᵏP⁻¹ (exponencialização rápida da matriz)
- D contém autovalores na diagonal
- P contém autovetores como colunas
**Teorema Espectral:** Toda matriz simétrica real é diagonalizável por uma matriz ortogonal. Seus autovalores são reais.
---

## Aplicativos
### Teoria da codificação (códigos de correção de erros)
Os campos finitos são a base dos códigos modernos de correção de erros.
| Código | Campo | Corrige | Aplicação |
|------|-------|----------|------------|
| Código de Hamming | FG(2) | 1 erro por bloco | RAM ECC, rede inicial |
| Reed-Salomão | GF(2ᵏ) | Vários erros | CDs, DVDs, códigos QR, comunicação via satélite |
| Códigos BCH | GF(2ᵏ) | Vários erros | Memória flash, satélite |
| Códigos LDPC | FG(2) | Vários erros | Wi-Fi (802.11n), DVB-S2, 5G |
**Codificação Reed-Solomon:** Trate os dados como um polinômio sobre GF(2ᵏ), avalie em vários pontos. Mesmo que algumas avaliações estejam corrompidas, o polinômio original pode ser recuperado.
### Computação Quântica
Os estados quânticos vivem em espaços vetoriais complexos (espaços de Hilbert). Portas quânticas são matrizes unitárias.
| Conceito Quântico | Estrutura Algébrica |
|----------------|-------------------|
| Qubit | Vetor unitário em ℂ² (espaço vetorial 2D complexo) |
| Portão quântico | Matriz unitária U ∈ U(2ⁿ) |
| Medição | Operador de projeção |
| Emaranhamento | Estado do produto tensorial não separável |
| Teorema da não clonagem | Nenhum mapa linear pode copiar um estado quântico desconhecido |
**Portas de qubit único:**
| Portão | Matriz | Efeito |
|------|--------|--------|
| Pauli-X (NÃO) | [[0,1],[1,0]] | Inversão de bits |
| Pauli-Z | [[1,0],[0,−1]] | Inversão de fase |
| Hadamard | (1/√2)[[1,1],[1,−1]] | Cria superposição |
| NÃO | Portão controlado 4×4 | Enreda dois qubits |
### Criptografia
| Aplicação | Álgebra Usada |
|------------|------------|
| RSA | Grupo multiplicativo (ℤ/nℤ)* |
| Criptografia de curva elíptica | Grupo de pontos em curva elíptica sobre campo finito |
| AES | Aritmética em GF(2⁸) |
| Diffie-Hellman | Subgrupo cíclico de (ℤ/pℤ)* ou grupo de curva elíptica |
---

## Relevância para aprendizado de máquina e ciência de dados
| Conceito de Álgebra | Aplicação |
|----------------|------------|
| Espaços vetoriais | Espaços de recursos, espaços de incorporação, aprendizagem de representação |
| Mapas lineares | Camadas de rede neural (y = Wx + b), redução de dimensionalidade |
| Valores próprios/vetores | PCA, agrupamento espectral, PageRank, análise de estabilidade |
| Decomposição matricial | SVD, autocomposição para compactação de modelo |
| Campos finitos | Códigos de correção de erros para armazenamento/transmissão confiável de dados |
| Teoria dos grupos | Simetria em física (leis de conservação), aumento de dados (rotações, reflexões) |
| Produtos tensores | Aprendizagem multimodal, computação quântica, mecanismos de atenção |
| Anéis e polinômios | Métodos de kernel, mapas de características polinomiais |
---

## Resumo
| Estrutura | Operações | Propriedade chave | Exemplo |
|-----------|-----------|-------------|---------|
| Grupo | Um (∗) | Fechamento, associatividade, identidade, inverso | (ℤ, +), Sₙ |
| Anel | Dois (+, ×) | Grupo abeliano em +, monóide em ×, distributivo | ℤ, ℤ/nℤ, Mₙ(ℝ) |
| Campo | Dois (+, ×) | Anel onde elementos diferentes de zero formam um grupo sob × | ℚ, ℝ, ℂ, GF(p) |
| Espaço vetorial | Mult escalar + adição | Módulo sobre um campo | ℝⁿ, Pₙ(F), espaços funcionais |
A álgebra abstrata fornece a linguagem para a própria estrutura. Os grupos capturam a simetria, os anéis capturam a aritmética, os campos capturam a divisão e os espaços vetoriais capturam a linearidade. Essas estruturas não são abstratas por si só – elas aparecem em todos os códigos de correção de erros que protegem seus dados, em todos os protocolos criptográficos que protegem suas comunicações, em todos os algoritmos quânticos que podem um dia transformar a computação e em todas as transformações lineares que passam por uma rede neural.