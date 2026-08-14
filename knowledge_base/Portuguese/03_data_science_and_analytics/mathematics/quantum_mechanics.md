---
# Metadata
title: "Quantum Mechanics"
description: "Wave-particle duality, Schrodinger equation, operators and observables, uncertainty principle, quantum states and superposition, entanglement, qubits, quantum gates, and relevance to quantum computing"
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
    changes: "Initial deep-dive into quantum mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [quantum-mechanics, schrodinger-equation, uncertainty-principle, superposition, entanglement, qubits, quantum-gates, quantum-computing]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "abstract_algebra.md"
  - "classical_mechanics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Mecânica Quântica
A mecânica quântica é a teoria da física nas menores escalas – átomos, elétrons, fótons e as partículas fundamentais da natureza. Substitui o mundo determinístico da mecânica clássica por probabilidades, superposições e emaranhados. Apesar de sua natureza contra-intuitiva, a mecânica quântica é a teoria testada com mais precisão em toda a ciência. Hoje, seus princípios estão se tornando diretamente relevantes para a computação por meio de computadores quânticos, que prometem resolver determinados problemas de forma exponencialmente mais rápida do que as máquinas clássicas.
---

## Motivação Histórica
### Falhas da Física Clássica
| Problema | Previsão Clássica | Observação | Resolução |
|---------|----------|-------------|------------|
| Radiação de corpo negro | Catástrofe ultravioleta (energia infinita em curto λ) | Comprimento de onda de pico finito | Planck: a energia é quantizada (E = nhν) |
| Efeito fotoelétrico | KE depende da intensidade, não da frequência | KE depende da frequência | Einstein: a luz é quantizada (fótons, E = hν) |
| Espectros atômicos | Espectro de emissão contínua | Linhas espectrais discretas | Bohr: elétrons ocupam órbitas quantizadas |
| Difracção de electrões | Partículas não difratam | Elétrons produzem padrões de interferência | de Broglie: partículas têm comprimento de onda λ = h/p |
### Constantes Chave
| Constante | Símbolo | Valor |
|----------|--------|-------|
| Constante de Planck | h | 6,626 × 10⁻³⁴J·s |
| Constante de Planck reduzida | ℏ = h/2π | 1,055 × 10⁻³⁴J·s |
| Velocidade da luz | c | 3,0 × 10⁸m/s |
| Massa do elétron | m_e | 9,109 × 10⁻³¹kg |
| Carga elementar | e | 1,602 × 10⁻¹⁹ C |
| Raio de Bohr | uma₀ | 5,292 × 10⁻¹¹m |
---

## Dualidade onda-partícula
### de comprimento de onda de Broglie
Cada partícula com momento p tem um comprimento de onda associado:
λ = h/p = h/(mv)
| Partícula | λ típico | Comportamento de onda observável? |
|----------|-----------|--------------------------|
| Elétron (100 eV) | 0,12nm | Sim (difracção de cristal) |
| Próton | 0,003nm | Sim (espalhamento de nêutrons) |
| Beisebol (40 m/s) | 10⁻³⁴m | Não (muito pequeno para ser detectado) |
### Experimento de fenda dupla
O experimento quântico por excelência:
1. Partículas de fogo (elétrons, fótons), uma de cada vez, em duas fendas
2. Cada partícula pousa em um único ponto do detector
3. Com o tempo, surge um padrão de interferência – como se cada partícula passasse pelas duas fendas simultaneamente
4. Se você medir por qual fenda a partícula passa, o padrão de interferência desaparece
**Conclusão:** Objetos quânticos não são puramente partículas nem puramente ondas. Eles exibem comportamento semelhante a uma onda quando não observados e comportamento semelhante a uma partícula quando medido.
---

## A função de onda
### Definição
A **função de onda** ψ(x, t) descreve completamente um sistema quântico. É uma função de valor complexo cujo módulo quadrático fornece a densidade de probabilidade:
P(x) = |ψ(x)|² = ψ*(x)ψ(x)
### Normalização
A probabilidade total deve ser igual a 1:
∫ |ψ(x)|² dx = 1 (em todo o espaço)
### Regra Nascida
A probabilidade de encontrar a partícula entre x e x + dx:
P(x para x+dx) = |ψ(x)|² dx
Para um observável geral com estados próprios φₙ:
P (medição do autovalor aₙ) = |⟨φₙ|ψ⟩|²
---

## A Equação de Schrodinger
### Equação de Schrodinger Dependente do Tempo
iℏ ∂ψ/∂t = Ĥψ
onde Ĥ é o **operador hamiltoniano** (operador de energia total).
### Equação de Schrodinger Independente do Tempo
Para estados estacionários (estados próprios de energia):
Ĥψ = Eψ
Esta é uma equação de autovalor: as energias permitidas E são os autovalores de Ĥ.
### Partícula em uma caixa (poço quadrado infinito)
O sistema quântico mais simples: partícula confinada em 0 < x < L.
| Quantidade | Resultado |
|----------|--------|
| Funções de onda | ψₙ(x) = √(2/L) sin(nπx/L) |
| Níveis de energia | Eₙ = n²π²ℏ²/(2mL²) = n²h²/(8mL²) |
| Estado fundamental | n = 1, E₁ = h²/(8mL²) |
| Energia do ponto zero | E₁ > 0 (a partícula não pode ficar perfeitamente imóvel) |
| Número quântico | n = 1, 2, 3, ... (apenas números inteiros positivos) |
### Oscilador Harmônico Quântico
V(x) = ½mω²x²
| Quantidade | Resultado |
|----------|--------|
| Níveis de energia | Eₙ = (n + ½)ℏω |
| Energia do ponto zero | E₀ = ½ℏω |
| Espaçamento | ΔE = ℏω (uniforme) |
| Funções de onda | Polinômios de Hermite × Gaussianos |
---

## Operadores e Observáveis
Na mecânica quântica, todo observável físico corresponde a um **operador Hermitiano**.
### Operadores Chave
| Observável | Operador (espaço de posição) | Autovalores |
|-----------|--------------------------|------------|
| Posição | x̂ = x | Tudo real x |
| Momento | p̂ = −iℏ ∂/∂x | Tudo real p |
| Energia (Hamiltoniana) | Ĥ = −(ℏ²/2m)∂²/∂x² + V(x) | Eₙ (discreto para estados vinculados) |
| Momento angular | L̂ = r × p̂ | ℏ√(eu(eu+1)) |
| Girar | Ŝ = (ℏ/2)σ (matrizes de Pauli) | ±ℏ/2 (para centrifugação-½) |
### Valores de expectativa
O resultado médio da medição de A observável no estado ψ:
⟨A⟩ = ⟨ψ|Â|ψ⟩ = ∫ ψ*(x) Â ψ(x) dx
### Relações de comutação
[Â, B̂] = ÂB̂ − B̂Â
| Comutador | Resultado | Significância |
|-----------|--------|-------------|
| [x̂, p̂] | euℏ | Posição e impulso são incompatíveis |
| [L̂ₓ, L̂ᵧ] | iℏL̂_z | Os componentes do momento angular são incompatíveis |
| [σ̂ₓ, σ̂ᵧ] | 2iσ̂_z | Matrizes de Pauli (componentes de spin) |
Se [Â, B̂] = 0, os observáveis ​​podem ser medidos simultaneamente (compartilhar estados próprios).
---

## Princípio da Incerteza
### Princípio da Incerteza de Heisenberg
Δx · Δp ≥ ℏ/2
Mais geralmente, para quaisquer dois observáveis ​​A e B:
ΔA · ΔB ≥ (1/2)|⟨[Â, B̂]⟩|
### Relações de incerteza
| Par | Relação | Interpretação |
|------|----------|----------------|
| Momento de posição | ΔxΔp ≥ ℏ/2 | Não é possível conhecer ambos com precisão |
| Tempo de energia | ΔEΔt ≥ ℏ/2 | Estados de vida curta têm energia incerta |
| Momento angular | ΔLₓΔLᵧ ≥ (ℏ/2)\|⟨L_z⟩\| | Não é possível conhecer todos os componentes simultaneamente |
**Importante:** A incerteza não tem a ver com distúrbios de medição — é uma propriedade fundamental dos estados quânticos. Uma partícula não tem posição e momento definidos simultaneamente.
---

## Estados Quânticos e Superposição
### Notação Dirac (Bra-Ket)
| Símbolo | Nome | Significado |
|--------|------|--------|
| \|ψ⟩ | Ket | Vetor de estado (vetor coluna) |
| ⟨ψ\| | Sutiã | Transposição conjugada (vetor linha) |
| ⟨φ\|ψ⟩ | Produto interno | Amplitude para ψ encontrada no estado φ |
| \|ψ\|² | Norma ao quadrado | Probabilidade |
### Princípio da Superposição
Se \|ψ₁⟩ e \|ψ₂⟩ são estados quânticos válidos, então qualquer combinação linear também é válida:
\|ψ⟩ = α\|ψ₁⟩ + β\|ψ₂⟩

onde |α|² + |β|² = 1 (normalização).
**Medição:** Quando medido, o sistema "colapsa" para \|ψ₁⟩ com probabilidade |α|² ou \|ψ₂⟩ com probabilidade |β|².
### Qubits
Um **qubit** é um bit quântico: um sistema quântico de dois níveis.
\|ψ⟩ = α\|0⟩ + β\|1⟩, onde |α|² + |β|² = 1
| Representação | \|0⟩ | \|1⟩ |
|---------------|------|------|
| Girar | Acelere ↑ | Girar para baixo ↓ |
| Polarização de fótons | Horizontais | Verticais |
| Nível de energia | Estado fundamental | Estado animado |
| Circuito | \|0⟩ = [1, 0]ᵀ | \|1⟩ = [0, 1]ᵀ |
**Esfera de Bloch:** Qualquer estado de qubit pode ser escrito como:
\|ψ⟩ = cos(θ/2)\|0⟩ + e^{iφ} sin(θ/2)\|1⟩
onde θ ∈ [0, π] e φ ∈ [0, 2π). O espaço de estado é uma esfera.
---

## Emaranhamento
Dois qubits estão **emaranhados** quando seu estado conjunto não pode ser escrito como um produto de estados individuais.
### Estados de Bell (Maximamente Emaranhados)
| Estado | Expressão | Nome |
|-------|-----------|------|
| \|Φ⁺⟩ | (1/√2)(\|00⟩ + \|11⟩) | Estado de sino |
| \|Φ⁻⟩ | (1/√2)(\|00⟩ − \|11⟩) | Estado de sino |
| \|Ψ⁺⟩ | (1/√2)(\|01⟩ + \|10⟩) | Estado de sino |
| \|Ψ⁻⟩ | (1/√2)(\|01⟩ − \|10⟩) | Estado singleto |
### Propriedades de emaranhamento
| Propriedade | Descrição |
|----------|------------|
| Correlação | Medir um qubit determina instantaneamente o outro, independentemente da distância |
| Sem comunicação | Não é possível usar apenas o emaranhamento para enviar informações mais rápido que a luz |
| Monogamia | Se A está maximamente emaranhado com B, não pode ser emaranhado com C |
| Fragilidade | A interação com o ambiente destrói o emaranhamento (decoerência) |
### Paradoxo EPR e Teorema de Bell
Einstein, Podolsky e Rosen argumentaram que a mecânica quântica deve ser incompleta (variáveis ​​ocultas). Bell mostrou que qualquer teoria de variáveis ​​ocultas locais satisfaz certas desigualdades. Os experimentos violam as desigualdades de Bell – confirmando a mecânica quântica e descartando variáveis ​​ocultas locais.
---

## Portões Quânticos
Portas quânticas são operações unitárias em qubits.
### Portas de Qubit Único
| Portão | Matriz | Efeito |
|------|--------|--------|
| **Pauli-X** (NÃO) | [[0,1],[1,0]] | Inversão de bits: \|0⟩ ↔ \|1⟩ |
| **Pauli-Y** | [[0,−i],[i,0]] | Bit + inversão de fase |
| **Pauli-Z** | [[1,0],[0,−1]] | Inversão de fase: \|1⟩ → −\|1⟩ |
| **Hadamard** (H) | (1/√2)[[1,1],[1,−1]] | Cria superposição: \|0⟩ → (\|0⟩+\|1⟩)/√2 |
| **Fase** (S) | [[1,0],[0,i]] | Rotação π/2 em torno de Z |
| **Portão T** | [[1,0],[0,e^{iπ/4}]] | Rotação π/4 em torno de Z |
| **Rotação** Rₓ(θ) | cos(θ/2)I − i sin(θ/2)σₓ | Rotação em θ em torno do eixo X |
### Portões de Dois Qubits
| Portão | Descrição | Efeito |
|------|------------|--------|
| **NÃO** | Controlado-NÃO | Inverte o alvo se o controle for \|1⟩ |
| **CZ** | Controlado-Z | Aplica Z ao alvo se o controle for \|1⟩ |
| **TROCA** | Trocar qubits | \|ab⟩ → \|ba⟩ |
### Criando Emaranhamento
Aplique H ao qubit 1 e, em seguida, CNOT com o qubit 1 como controle:
\|00⟩ → (H⊗I)\|00⟩ → CNOT → (1/√2)(\|00⟩ + \|11⟩) = \|Φ⁺⟩
---

## Algoritmos Quânticos
| Algoritmo | Aceleração | Aplicação |
|-----------|---------|------------|
| **Shor** | Exponencial (fatoração) | Quebra a criptografia RSA |
| **Grover's** | Quadrático (pesquisa) | Pesquisa não estruturada em O(√N) |
| **VQE** | Heurística | Encontrando energias do estado fundamental (química, materiais) |
| **QAOA** | Heurística | Otimização combinatória |
| **HHL** | Exponencial (sob condições) | Resolvendo sistemas lineares |
| **Simulação quântica** | Exponencial | Simulação de sistemas quânticos (motivação original de Feynman) |
---

## Relevância para aprendizado de máquina e ciência de dados
| Conceito Quântico | Aplicação |
|----------------|------------|
| Qubits e superposição | Aprendizado de máquina quântica, amostragem aprimorada quântica |
| Emaranhamento | Comunicação quântica, distribuição quântica de chaves (QKD) |
| Portões quânticos | Projeto de circuito quântico para sub-rotinas de ML |
| Algoritmo de Grover | Aceleração quadrática para otimização baseada em pesquisa |
| Algoritmo de Shor | Ameaça à criptografia atual; motiva criptografia pós-quântica |
| Simulação quântica | Descoberta de medicamentos, ciência de materiais, simulação química |
| Algoritmos variacionais (VQE, QAOA) | ML quântico de curto prazo em dispositivos NISQ |
| Regra nascida | Resultados probabilísticos análogos à amostragem de distribuições |
| Produtos tensores | Sistemas multiqubit (espaço de estado exponencial - mesma matemática da álgebra multilinear em ML) |
| Matrizes unitárias | Análogos quânticos de transformações ortogonais |
---

## Resumo
| Conceito | Ideia Central | Equação Chave |
|--------|-----------|-------------|
| Dualidade onda-partícula | A matéria tem propriedades ondulatórias | λ = h/p |
| Função de onda | Descrição completa do estado quântico | P(x) = \|ψ(x)\|² |
| Equação de Schrödinger | Como os estados quânticos evoluem | iℏ ∂ψ/∂t = Ĥψ |
| Operadores | Observáveis ​​são operadores hermitianos | ⟨A⟩ = ⟨ψ\|Â\|ψ⟩ |
| Incerteza | Limites fundamentais do conhecimento simultâneo | ΔxΔp ≥ ℏ/2 |
| Superposição | Estados podem ser adicionados | \|ψ⟩ = α\|0⟩ + β\|1⟩ |
| Emaranhamento | Estados conjuntos indissociáveis ​​| \|Φ⁺⟩ = (\|00⟩ + \|11⟩)/√2 |
| Portões quânticos | Operações unitárias em qubits | Conjuntos de portões H, CNOT e universais |
A mecânica quântica desafia as nossas intuições mais profundas sobre a realidade – partículas que são ondas, objetos em dois lugares ao mesmo tempo, correlações que desafiam a explicação clássica. No entanto, a sua matemática é precisa e as suas previsões são incomparáveis ​​em termos de precisão. Para os cientistas de dados, a mecânica quântica está a tornar-se diretamente relevante através da computação quântica, que promete transformar a otimização, a criptografia, a simulação e, potencialmente, a própria aprendizagem automática.