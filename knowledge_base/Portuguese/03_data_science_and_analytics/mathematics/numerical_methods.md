---
# Metadata
title: "Numerical Methods"
description: "Floating-point arithmetic, root finding, numerical integration, ODE solvers, interpolation, numerical stability, and conditioning"
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
    changes: "Initial deep-dive into numerical methods"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [numerical-methods, floating-point, root-finding, numerical-integration, ode-solvers, interpolation, stability]
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

# Métodos Numéricos
Os métodos numéricos são a ponte entre a teoria matemática e a computação prática. Embora a matemática pura prove que existem soluções, os métodos numéricos na verdade calculam respostas aproximadas com precisão finita. Cada modelo de aprendizado de máquina, simulação física e pipeline de análise de dados depende, em última análise, de computação numérica. Compreender esses métodos — sua precisão, estabilidade e limitações — é essencial para construir software confiável.
---

## Aritmética de ponto flutuante
Os computadores representam números reais com precisão finita. O **padrão IEEE 754** define como os números de ponto flutuante são armazenados e manipulados.
### Formatos IEEE 754
| Formato | Pedaços | Expoente | Mantissa | Dígitos Decimais Aproximados | Alcance |
|----|------|----------|----------|---------------------------|-------|
| Metade (fp16) | 16 | 5 | 10 | 3.3 | ±6,5 × 10⁴ |
| Único (fp32) | 32 | 8 | 23 | 7.2 | ±3,4 × 10³⁸ |
| Duplo (fp64) | 64 | 11 | 52 | 15,9 | ±1,8 × 10³⁰⁸ |
### Máquina Épsilon
**Épsilon da máquina** (ε_mach) é o menor número tal que 1 + ε_mach > 1 em ponto flutuante.
| Formato | ε_mach |
|--------|--------|
| fp16 | 2⁻¹⁰ ≈ 9.8 × 10⁻⁴ |
| fp32 | 2⁻²³ ≈ 1.2 × 10⁻⁷ |
| fp64 | 2⁻⁵² ≈ 2.2 × 10⁻¹⁶ |
### Armadilhas Comuns
| Armadilha | Exemplo | Consequência |
|---------|---------|------------|
| **Cancelamento catastrófico** | Computando (1 + x) − 1 para x pequeno | Perda de dígitos significativos |
| **Absorção** | 10⁸ + 1 = 10⁸ em fp32 | Pequenos valores perdidos em grandes somas |
| **Não associatividade** | (a + b) + c ≠ a + (b + c) | A ordem da soma é importante |
| **Divisão por quase zero** | 1/10⁻³⁰⁰ → estouro | Infinito ou NaN |
### Estratégias de Mitigação
| Estratégia | Descrição |
|----------|------------|
| **Somatório de Kahan** | Soma compensada para reduzir o erro de absorção |
| **Kahan-Babuska-Neumaier** | Versão melhorada do somatório de Kahan |
| **Somatório classificado** | Some primeiro os números pequenos para evitar a absorção |
| **Aritmética duplo-duplo** | Use pares de duplos para maior precisão |
| **Análise de condicionamento** | Entenda se o problema em si amplifica os erros |
---

## Localização de raiz
Encontrar x tal que f(x) = 0.
### Método de bissecção
| Propriedade | Valor |
|----------|-------|
| Requer | f contínua, f(a) e f(b) têm sinais opostos |
| Convergência | Linear (o erro divide cada etapa pela metade) |
| Garantido? | Sim — sempre converge |
| Iterações para d dígitos | ≈ d / log₁₀(2) ≈ 3,32d |
**Algoritmo:**
1. Comece com intervalo [a, b] onde f(a) · f(b) <0
2. Calcule o ponto médio c = (a + b) / 2
3. Se f(c) = 0 ou |b − a| <tolerância, pare
4. Se f(a) · f(c) < 0, defina b = c; senão defina a = c
5. Repita
### Método Newton-Raphson
| Propriedade | Valor |
|----------|-------|
| Requer | f diferenciável, f'(x) ≠ 0 na raiz |
| Convergência | Quadrático (perto da raiz) |
| Garantido? | Não — pode divergir ou circular |
| Regra de atualização | x_{n+1} = x_n − f(x_n) / f'(x_n) |
**Exemplo resolvido:** Encontre √2 resolvendo f(x) = x² − 2 = 0.
-f'(x) = 2x
- x₀ = 1,5
- x₁ = 1,5 − (2,25 − 2) / 3 = 1,5 − 0,0833 = 1,4167
- x₂ = 1,4167 − (2,0069 − 2) / 2,8333 = 1,4142
- x₃ = 1,41421356... (correto com 8 casas decimais)
### Método Secante
Como o método de Newton, mas aproxima a derivada:
x_{n+1} = x_n − f(x_n) · (x_n − x_{n-1}) / (f(x_n) − f(x_{n-1}))
| Propriedade | Valor |
|----------|-------|
| Convergência | Superlinear (ordem ≈ 1,618, a proporção áurea) |
| Requer | Duas estimativas iniciais (sem necessidade de derivada) |
### Comparação de métodos de localização de raízes
| Método | Convergência | Derivada necessária? | Garantido? | Custo por etapa |
|--------|------------|-------------------|-------------|---------------|
| Bisecção | Linear (1) | Não | Sim | 1 função de avaliação |
| Newton-Raphson | Quadrático (2) | Sim | Não | 2 avaliações de função |
| Secante | Superlinear (1.618) | Não | Não | 1 função de avaliação |
| Método de Brent | Superlinear | Não | Sim | Varia |
**Método de Brent** combina bissecção (convergência garantida) com interpolação quadrática secante/inversa (convergência rápida). É o localizador de raiz padrão na maioria das bibliotecas numéricas.
---

## Integração Numérica (Quadratura)
Calculando ∫ₐᵇ f(x) dx aproximadamente.
### Métodos
| Método | Fórmula | Erro | Encomendar |
|----|---------|-------|-------|
| **Retângulo (ponto médio)** | (b−a) · f((a+b)/2) | O(h²) | 1 |
| **Trapezoidal** | (b−a)/2 · [f(a) + f(b)] | O(h²) | 2 |
| **1/3 dos Simpsons** | (b−a)/6 · [f(a) + 4f(m) + f(b)] | O(h⁴) | 3 |
| **Simpsons 3/8** | Usa 4 pontos igualmente espaçados | O(h⁴) | 4 |
| **Quadratura gaussiana** | Posicionamento ideal dos nós | O(h²ⁿ) | n pontos |
### Regras Compostas
Para n subintervalos de largura h = (b−a)/n:
| Regra | Fórmula Composta | Erro |
|------|-------------------|-------|
| Composto Trapezoidal | h[f(a)/2 + Σf(xᵢ) + f(b)/2] | O(h²) |
| Simpson composto | h/3[f(a) + 4Σf(ímpar) + 2Σf(par) + f(b)] | O(h⁴) |
**Exemplo resolvido:** Aproxime ∫₀¹ e^(−x²) dx usando trapezoidal composto com n = 4.
- h = 0,25, pontos: 0, 0,25, 0,5, 0,75, 1
- f(0) = 1, f(0,25) = 0,9394, f(0,5) = 0,7788, f(0,75) = 0,5698, f(1) = 0,3679
- T = 0,25[1/2 + 0,9394 + 0,7788 + 0,5698 + 0,3679/2] = 0,25[1/2 + 2,2880 + 0,1840] = 0,7430
- Valor verdadeiro: ≈ 0,7468 (erro ≈ 0,5%)
### Quadratura Adaptativa
Subdivide automaticamente os intervalos onde a função varia rapidamente, usando menos pontos onde ela é suave. Isto é o que`scipy.integrate.quad`usa (baseado em QUADPACK).
---

## Interpolação
Estimando valores entre pontos de dados conhecidos.
### Métodos
| Método | Descrição | Suavidade | Oscilação |
|--------|-------------|------------|-------------|
| **Vizinho mais próximo** | Use o ponto de dados mais próximo | Descontínuo | Nenhum |
| **Linear** | Conecte pontos com linhas retas | C⁰ (contínuo) | Nenhum |
| **Polinômio (Lagrange)** | Polinômio único em todos os pontos | C^∞ | Grave em muitos pontos (fenômeno de Runge) |
| **Spline cúbica** | Cúbico por partes, liso nas juntas | C² | Mínimo |
| **Função de base radial** | Soma ponderada dos núcleos radiais | Depende do kernel | Baixo |
### Interpolação de Lagrange
Dados n+1 pontos (x₀, y₀), ..., (xₙ, yₙ), o polinômio único de grau ≤ n passando por todos os pontos:
P(x) = Σᵢ₌₀ⁿ yᵢ · Πⱼ≠ᵢ (x − xⱼ) / (xᵢ − xⱼ)
**Fenômeno de Runge:** A interpolação polinomial de alto grau em pontos igualmente espaçados pode oscilar muito perto das bordas. Mitigado usando nós ou splines Chebyshev.
### Splines Cúbicas
Polinômios cúbicos por partes que são C² contínuos (segundas derivadas contínuas).
| Tipo | Condição limite |
|------|-------------------|
| Estria natural | S''(x₀) = S''(xₙ) = 0 |
| Estria fixada | S'(x₀) e S'(xₙ) especificados |
| Não é um nó | Terceira derivada contínua em x₁ e xₙ₋₁ |
---

## Solucionadores de EDO
Resolvendo equações diferenciais ordinárias dy/dt = f(t, y) numericamente.
### Método de Euler
O solucionador de EDO mais simples.
**Atualização:** y_{n+1} = y_n + h · f(t_n, y_n)
| Propriedade | Valor |
|----------|-------|
| Encomendar | 1 (erro por etapa: O(h²), global: O(h)) |
| Estabilidade | Condicionalmente estável (h necessário pequeno) |
| Custo | 1 avaliação de função por etapa |
### Métodos Runge-Kutta
| Método | Encomendar | Etapas | Notas |
|--------|-------|--------|-------|
| **Euler** | 1 | 1 | Mais simples |
| **Ponto médio** | 2 | 2 | Melhor precisão |
| **Heun (RK2)** | 2 | 2 | Preditor-corretor |
| **RK4 clássico** | 4 | 4 | Cavalo de batalha padrão |
| **Dormand-Prince (RK45)** | 4(5) | 6 | Tamanho do passo adaptativo (usado em ode45) |
### Clássico RK4 (Runge-Kutta de 4ª ordem)
k₁ = f(t_n, y_n)
k₂ = f(t_n + h/2, y_n + hk₁/2)
k₃ = f(t_n + h/2, y_n + hk₂/2)
k₄ = f(t_n + h, y_n + hk₃)
y_{n+1} = y_n + h(k₁ + 2k₂ + 2k₃ + k₄) / 6
| Propriedade | Valor |
|----------|-------|
| Encomendar | 4 (erro global: O(h⁴)) |
| Custo | 4 avaliações de funções por etapa |
| Estabilidade | Muito melhor que Euler |
| Uso | Padrão para EDOs não rígidas |
### EDOs rígidas
Uma EDO **rígida** tem componentes que variam em escalas de tempo muito diferentes. Métodos explícitos (Euler, RK4) requerem tamanhos de passo impraticavelmente pequenos.
| Método | Tipo | Estabilidade |
|--------|------|-----------|
| Euler implícito | Implícito | A-estável (incondicionalmente estável) |
| Fórmula de diferenciação retroativa (BDF) | Implícito | A-estável (até ordem 5) |
| Runge-Kutta implícito | Implícito | Existem variantes L-estáveis ​​|
| LSODA | Automático | Alterna entre rígido/não rígido |
---

## Estabilidade Numérica e Condicionamento
### Número da condição
O **número da condição** mede o quanto a saída de um problema muda em relação a pequenas mudanças na entrada.
Para um sistema linear Ax = b: κ(A) = ||A|| · ||A⁻¹||
| κ(A) | Interpretação |
|-------|---------------|
| ≈ 1 | Bem condicionado |
| 10³ | Ligeiramente sensível |
| 10⁸ | Mal condicionado (perde aproximadamente 8 dígitos de precisão) |
| → ∞ | Singular (sem solução única) |
### Estabilidade de Algoritmos
Um algoritmo é **numericamente estável** se pequenas perturbações na entrada levarem a pequenas perturbações na saída (em relação ao número de condição do problema).
| Algoritmo | Estável? | Notas |
|-----------|---------|-------|
| Eliminação gaussiana com pivotamento parcial | Sim | Abordagem padrão |
| Calculando autovalores via QR | Sim | Estável para trás |
| Somatório ingênuo (grande + pequeno primeiro) | Não | Use o somatório de Kahan |
| Calculando a variância como E[X²] − (E[X])² | Potencialmente não | Use o algoritmo online de Welford |
### Algoritmo Online de Welford
Cálculo numericamente estável da média e variância corrente:
```
mean_new = mean_old + (x − mean_old) / n
M2_new = M2_old + (x − mean_old)(x − mean_new)
variance = M2 / (n − 1)
```

Isso evita o cancelamento catastrófico que ocorre na fórmula ingênua de duas passagens.
---

## Relevância para aprendizado de máquina e ciência de dados
| Método Numérico | Aplicação |
|-----------------|-------------|
| Ponto flutuante (fp16/fp32/bf16) | Treinamento de precisão mista, quantização de modelos, eficiência de memória |
| Localização de raiz | Estimativa de máxima verossimilhança (descobrir onde gradiente = 0) |
| Integração numérica | Inferência bayesiana (cálculo de probabilidades marginais), valores esperados |
| Interpolação | Suavização, imputação, modelos substitutos, funções de ativação |
| Solucionadores de EDO | EDOs neurais, RNNs de tempo contínuo, dinâmica populacional, ML informado pela física |
| Número da condição | Compreendendo questões numéricas em regressão linear, equações normais |
| Soma estável | Computação de funções de perda, estatísticas de normalização de lote |
| RK4 / solucionadores adaptativos | Simulação de sistemas dinâmicos, treinamento de redes de profundidade contínua |
---

## Resumo
| Tópico | Ideia Central | Método Chave |
|-------|-----------|-----------|
| Ponto flutuante | Representação de precisão finita | IEEE 754, somatório de Kahan |
| Localização de raiz | Resolva f(x) = 0 | Bissecção, Newton-Raphson, Brent's |
| Integração numérica | Aproximado ∫f(x)dx | Quadratura trapezoidal, Simpson, Gaussiana |
| Interpolação | Estimativa entre pontos de dados | Splines cúbicas, Lagrange, RBF |
| Solucionadores de EDO | Resolva dy/dt = f(t,y) | Euler, RK4, métodos adaptativos |
| Estabilidade | Sensibilidade a erros de arredondamento | Número de condição, algoritmos estáveis ​​|
Os métodos numéricos são onde a matemática encontra a realidade. Nenhum computador pode representar exatamente a maioria dos números reais, nenhuma derivada é calculada simbolicamente na prática e nenhuma integral é avaliada de forma fechada para problemas do mundo real. Compreender os métodos numéricos permite escolher o algoritmo certo, prever sua precisão e evitar os erros sutis que surgem da aritmética de precisão finita.