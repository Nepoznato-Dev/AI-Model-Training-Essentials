---
# Metadata
title: "Classical Mechanics"
description: "Newton's laws, free-body diagrams, work-energy theorem, conservation laws, Lagrangian mechanics, Hamiltonian mechanics, rigid body dynamics, and orbital mechanics"
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
    changes: "Initial deep-dive into classical mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [classical-mechanics, newton, lagrangian, hamiltonian, conservation-laws, orbital-mechanics, rigid-body]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Mecânica Clássica
A mecânica clássica descreve o movimento de objetos sob a influência de forças. Desde maçãs caindo até planetas em órbita, desde cordas vibrantes até partículas em colisão, seus princípios governam o mundo macroscópico. Além de suas aplicações físicas, a mecânica clássica deu origem ao cálculo de variações, à geometria simplética e à estrutura hamiltoniana que sustenta a mecânica quântica e a otimização moderna.
---

## Mecânica Newtoniana
### Três Leis de Newton
| Direito | Declaração | Forma Matemática |
|-----|-----------|-------------------|
| **Primeiro (Inércia)** | Um objeto permanece em repouso ou em movimento uniforme, a menos que seja influenciado por uma força | Se F_net = 0, então v = constante |
| **Segundo (F = ma)** | Força é igual a massa vezes aceleração | **F** = m**a** = m(d²**x**/dt²) |
| **Terceiro (Ação-Reação)** | Toda ação tem uma reação igual e oposta | **F**₁₂ = −**F**₂₁ |
### Diagramas de corpo livre
Um **diagrama de corpo livre** isola um objeto e mostra todas as forças que atuam sobre ele.
**Forças comuns:**
| Força | Fórmula | Direção |
|-------|------------|-----------|
| Gravidade (perto da Terra) | F = mg | Para baixo |
| Força normal | N | Perpendicular à superfície |
| Fricção (estática) | f_s ≤ μ_s N | Opõe-se ao movimento iminente |
| Fricção (cinética) | f_k = μ_k N | Opõe-se ao movimento |
| Primavera (lei de Hooke) | F = −kx | Restaurando (em direção ao equilíbrio) |
| Tensão | T | Ao longo do barbante/corda |
| Arraste | F_d = ½C_d ρAv² | Opõe-se à velocidade |
### Exemplo resolvido: Bloqueio na inclinação
Um bloco de massa m em um plano inclinado sem atrito com ângulo θ.
- Forças: gravidade (mg para baixo), força normal (N perpendicular à superfície)
- Decompor a gravidade: mg sin θ (ao longo da inclinação), mg cos θ (na superfície)
- N = mg cos θ (nenhum movimento perpendicular à superfície)
- Aceleração ao longo da inclinação: a = g sin θ
---

## Métodos Energéticos
### Trabalho e Energia Cinética
**Trabalho** realizado por uma força: W = ∫ **F** · d**r**
**Teorema da Energia de Trabalho:** W_net = ΔKE = ½mv₂² − ½mv₁²
### Energia Potencial
| Força | Energia Potencial | Notas |
|-------|-----------------|-------|
| Gravidade (perto da superfície) | você = mgh | h = altura acima da referência |
| Gravidade (geral) | você = −GMm/r | Zero no infinito |
| Primavera | você = ½kx² | x = deslocamento do equilíbrio |
| Eletrostático | você = kq₁q₂/r | Cargas semelhantes: U positivo |
### Conservação de Energia
Se apenas forças conservativas atuarem: E = KE + PE = constante
½mv₁² + U₁ = ½mv₂² + U₂
**Exemplo resolvido:** Uma bola caiu da altura h.
- Inicial: KE = 0, PE = mgh
- Pouco antes de atingir o solo: KE = ½mv², PE = 0
- Conservação: mgh = ½mv² → v = √(2gh)
### Poder
P = dW/dt = **F** · **v** (taxa de realização de trabalho)
---

## Momentum e colisões
### Momento Linear
**p** = m**v**
Segunda lei de Newton (forma alternativa): **F** = d**p**/dt
### Conservação do Momentum
Se não houver forças externas: o momento total é conservado.
| Tipo de colisão | KE conservado? | Momento conservado? |
|---------------|---------------|----------|
| **Elástico** | Sim | Sim |
| **Inelástico** | Não | Sim |
| **Perfeitamente inelástico** | Não (perda máxima) | Sim (objetos ficam juntos) |
**Colisão elástica 1D:** Duas massas m₁, m₂ com velocidades iniciais u₁, u₂:
- v₁ = ((m₁−m₂)u₁ + 2m₂u₂) / (m₁+m₂)
- v₂ = ((m₂−m₁)u₂ + 2m₁u₁) / (m₁+m₂)
### Momento Angular
**L** = **r** × **p** = m(**r** × **v**)
Torque: **τ** = d**L**/dt = **r** × **F**
**Conservação:** Se não houver torque externo, o momento angular é conservado.
---

## Mecânica Lagrangiana
A formulação **Lagrangiana** substitui forças por energia, proporcionando uma estrutura mais elegante e geral.
### O Lagrangiano
L = T − V (energia cinética menos energia potencial)
### Princípio da Mínima Ação (Princípio de Hamilton)
O caminho real percorrido por um sistema entre os tempos t₁ e t₂ minimiza (mais precisamente, torna estacionário) a **ação**:
S = ∫_{t₁}^{t₂} L(q, q̇, t) dt
### Equações de Euler-Lagrange
A condição δS = 0 produz:
d/dt(∂L/∂q̇) − ∂L/∂q = 0
para cada coordenada generalizada q.
**Exemplo resolvido:** Pêndulo simples (comprimento l, massa m, ângulo θ da vertical).
- T = ½ml²θ̇²
- V = −mgl cos θ
- L = ½ml²θ̇² + mgl cos θ
- ∂L/∂θ = −mgl sen θ
- ∂L/∂θ̇ = ml²θ̇ → d/dt(∂L/∂θ̇) = ml²θ̈
- Euler-Lagrange: ml²θ̈ + mgl sen θ = 0 → θ̈ + (g/l) sen θ = 0
### Vantagens da Mecânica Lagrangiana
| Vantagem | Explicação |
|-----------|------------|
| Independente de coordenadas | Funciona em qualquer sistema de coordenadas |
| Lida com restrições naturalmente | Não há necessidade de calcular forças de restrição |
| Simetria → conservação | O teorema de Noether conecta simetrias a quantidades conservadas |
| Generaliza facilmente | Para campos, relatividade, mecânica quântica |
---

## Mecânica Hamiltoniana
A formulação **Hamiltoniana** é uma reformulação da mecânica Lagrangiana que usa posições e momentos (em vez de posições e velocidades).
### O hamiltoniano
H = Σᵢ pᵢq̇ᵢ − L = T + V (para a maioria dos sistemas mecânicos)
onde pᵢ = ∂L/∂q̇ᵢ são os **momentos generalizados**.
### Equações de Hamilton
q̇ᵢ = ∂H/∂pᵢ
ṗᵢ = −∂H/∂qᵢ
Estas são 2n EDOs de primeira ordem (vs n equações de Euler-Lagrange de segunda ordem).
**Exemplo resolvido:** Oscilador harmônico (massa m, constante de mola k).
- H = p²/(2m) + ½kx²
- ẋ = ∂H/∂p = p/m → p = mẋ (como esperado)
- ṗ = −∂H/∂x = −kx → mẍ = −kx (Lei de Hooke)
### Colchetes Poisson
Para funções f(q, p) e g(q, p):
{f, g} = Σᵢ (∂f/∂qᵢ · ∂g/∂pᵢ − ∂f/∂pᵢ · ∂g/∂qᵢ)
| Propriedade | Declaração |
|----------|-----------|
| Evolução temporal | df/dt = {f, H} + ∂f/∂t |
| Conservação | f é conservado se {f, H} = 0 (e ∂f/∂t = 0) |
| Colchetes fundamentais | {qᵢ, pⱼ} = δᵢⱼ, {qᵢ, qⱼ} = 0, {pᵢ, pⱼ} = 0 |
**Conexão com a mecânica quântica:** Colchetes de Poisson tornam-se comutadores: {f, g} → (1/iℏ)[f̂, ĝ]
---

## Leis de Conservação e Teorema de Noether
### Teorema de Noether
Cada simetria contínua do Lagrangiano corresponde a uma quantidade conservada.
| Simetria | Quantidade conservada |
|----------|-------------------|
| Invariância de tradução de tempo | Energia |
| Invariância de tradução espacial | Momento linear |
| Invariância rotacional | Momento angular |
| Invariância do medidor | Carga elétrica |
Este é um dos resultados mais profundos de toda a física – liga a geometria do espaço-tempo às leis fundamentais de conservação.
---

## Dinâmica Corporal Rígida
Um **corpo rígido** é um objeto onde todas as distâncias internas permanecem fixas.
### Conceitos-chave
| Conceito | Fórmula | Descrição |
|---------|---------|------------|
| **Momento de inércia** | I = Σmᵢrᵢ² ou I = ∫r² dm | Resistência à aceleração rotacional |
| **KE rotacional** | KE = ½Iω² | Energia de rotação |
| **Momento angular** | eu = euω | Análogo rotacional de p = mv |
| **Torque** | τ = Iα | Análogo rotacional de F = ma |
### Momentos de Inércia (Formas Comuns)
| Forma | Eixo | eu |
|-------|------|---|
| Esfera sólida | Através do centro | (2/5)MR² |
| Esfera oca | Através do centro | (2/3)MR² |
| Cilindro sólido | Ao longo do eixo | (1/2)MR² |
| Haste fina | Pelo centro, perpendicular | (1/12)ML² |
| Haste fina | Através da extremidade, perpendicular | (1/3)ML² |
| Disco | Pelo centro, perpendicular | (1/2)MR² |
---

## Mecânica Orbital
### Leis de Kepler
| Direito | Declaração |
|-----|-----------|
| **Primeiro (reticências)** | Os planetas se movem em elipses com o Sol em um dos focos |
| **Segundo (Áreas iguais)** | Uma linha que vai do Sol ao planeta percorre áreas iguais em tempos iguais |
| **Terceiro (Harmônico)** | T² ∝ a³ (período ao quadrado proporcional ao semieixo maior ao cubo) |
### Energia Orbital
E = ½mv² − GMm/r
| E | Tipo de órbita |
|---|-----------|
| E< 0 | Elliptical (bound) |
| E = 0 | Parabolic (escape trajectory) |
| E >0 | Hiperbólico (não consolidado) |
### Velocidade de escape
v_escape = √(2GM/R)
Para a Terra: v_escape ≈ 11,2 km/s
---

## Relevância para aprendizado de máquina e ciência de dados
| Conceito de Mecânica | Aplicação |
|------------------|------------|
| Leis de Newton | Motores de física em simulações, IA de jogos, robótica |
| Métodos energéticos | Modelos baseados em energia, redes Hopfield, máquinas Boltzmann |
| Mecânica Lagrangiana | Redes neurais informadas pela física, controle ideal, otimização de trajetória |
| Mecânica hamiltoniana | Redes neurais hamiltonianas (HNNs), integradores simpléticos para simulação |
| Leis de conservação | Vieses indutivos em modelos de ML, redes neurais equivariantes |
| Teorema de Noether | Aprendizado de máquina com reconhecimento de simetria, aprendizado profundo geométrico |
| Dinâmica corporal rígida | Simulação robótica, dinâmica molecular, animação 3D |
| Mecânica orbital | Posicionamento por satélite (GPS para ML baseado em localização), projeto de missão espacial |
| Espaço de fase (Hamiltoniano) | Compreendendo sistemas dinâmicos, redes atrativas |
| Cálculo de variações | Transporte ideal, modelagem generativa (correspondência de fluxo) |
---

## Resumo
| Estrutura | Equação Central | Força |
|-----------|--------------|----------|
| Newtoniano | **F** = m**a** | Análise de força direta e intuitiva |
| Lagrangiano | d/dt(∂L/∂q̇) − ∂L/∂q = 0 | Livre de coordenadas, lida com restrições |
| Hamiltoniano | q̇ = ∂H/∂p, ṗ = −∂H/∂q | Estrutura simplética, conecta-se ao QM |
| Leis de conservação | Teorema de Noether | Conexão profunda de simetria-conservação |
A mecânica clássica não envolve apenas bolas caindo e pêndulos balançando. Suas estruturas matemáticas – mecânica Lagrangiana e Hamiltoniana – estão entre as ideias mais influentes em toda a ciência. Eles generalizam para a mecânica quântica, a teoria de campo e até mesmo o aprendizado de máquina moderno, onde modelos baseados em energia e redes neurais informadas pela física se baseiam diretamente nessas formulações centenárias.