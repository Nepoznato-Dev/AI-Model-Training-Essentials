<!--
---
# Metadata
title: "Optics and Waves"
description: "Wave equation, superposition, interference, diffraction, polarization, geometric optics, Fourier optics, and applications to signal processing and imaging"
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
    changes: "Initial deep-dive into optics and waves"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [optics, waves, wave-equation, interference, diffraction, polarization, geometric-optics, fourier-optics]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "electromagnetism.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Óptica e Ondas
As ondas estão por toda parte: som, luz, água, sinais de rádio, amplitudes de probabilidade quântica, flutuações do mercado de ações e vibrações de ativações de redes neurais. A óptica – o estudo da luz – é a ciência das ondas mais bem desenvolvida, e as suas ferramentas matemáticas (análise de Fourier, interferência, difração) aplicam-se a todos os fenómenos ondulatórios. Compreender as ondas é essencial para o processamento de sinais, análise de imagens, comunicações e a camada física de toda a tecnologia moderna.
---

## A equação da onda
### Equação Geral da Onda
A equação de onda unidimensional:
∂²u/∂t² = c² ∂²u/∂x²
onde u(x,t) é o deslocamento da onda e c é a velocidade da onda.
### Solução Geral (d'Alembert)
você(x,t) = f(x − ct) + g(x + ct)
onde f é uma onda que se propaga para a direita e g é uma onda que se propaga para a esquerda.
### Parâmetros principais da onda
| Parâmetro | Símbolo | Unidade | Descrição |
|-----------|--------|------|------------|
| Amplitude | Um | varia | Deslocamento máximo |
| Comprimento de onda | λ | metros | Distância entre cristas consecutivas |
| Frequência | f ou ν | Hertz (Hz) | Ciclos por segundo |
| Período | T = 1/f | segundos | Tempo para um ciclo completo |
| Número da onda | k = 2π/λ | rad/m | Frequência espacial |
| Frequência angular | ω = 2πf | radianos/s | Frequência temporal |
| Velocidade da onda | c = fλ = ω/k | m/s | Velocidade de propagação |
### Onda Senoidal
você(x,t) = A sin(kx − ωt + φ)
onde φ é a constante de fase.
### Velocidade da onda em diferentes mídias
| Tipo de onda | Médio | Fórmula de velocidade |
|-----------|--------|---------------|
| Corda | Tensão T, densidade linear μ | c = √(T/μ) |
| Som | Módulo aparente B, densidade ρ | c = √(B/ρ) |
| Som (gás ideal) | γ, R, T, M | c = √(γRT/M) |
| Onda EM | Permissividade ε, permeabilidade μ | c = 1/√(με) |
| Onda EM (vácuo) | ε₀, μ₀ | c = 3 × 10⁸ m/s |
---

## Superposição e interferência
### Princípio da Superposição
Quando duas ou mais ondas se sobrepõem, o deslocamento resultante é a soma dos deslocamentos individuais:
u_total = u₁ + u₂ + ... + uₙ
Isso vale para equações de ondas lineares.
### Interferência de Duas Ondas
Duas ondas com a mesma frequência e amplitude, diferença de fase Δφ:
u_total = 2A cos(Δφ/2) sin(kx − ωt + Δφ/2)
| Diferença de Fase | Resultado | Intensidade |
|-----------------|--------|-----------|
| Δφ = 0, 2π, 4π, ... | **Construtivo** (amplitude = 2A) | 4I₀ (máximo) |
| Δφ = π, 3π, 5π, ... | **Destrutivo** (amplitude = 0) | 0 (mínimo) |
| Δφ = π/2 | Parcial | 2I₀ |
### Condições para interferência
| Condição | Tipo | Diferença de caminho |
|-----------|------|------|
| Construtivo | Franja brilhante | ΔL = mλ (m = 0, 1, 2, ...) |
| Destrutivo | Franja escura | ΔL = (m + ½)λ |
---

## Experimento de fenda dupla de Young
A luz passa por duas fendas estreitas separadas pela distância d, criando um padrão de interferência em uma tela à distância L.
### Posições de franja
| Franja | Posição na tela |
|--------|-------------------|
| Brilhante (máximo) | y_m = mλL/d |
| Escuro (mínimos) | y_m = (m + ½)λL/d |
| Espaçamento de franjas | Δy = λL/d |
Este experimento provou a natureza ondulatória da luz (Thomas Young, 1801) e mais tarde tornou-se central para a mecânica quântica (dualidade onda-partícula).
---

## Difração
**Difração** é a curvatura e propagação de ondas em torno de obstáculos e através de aberturas.
### Difração de fenda única
A luz através de uma fenda de largura a produz um padrão de franjas claras e escuras.
| Recurso | Condição |
|--------|-----------|
| Máximo central | Mais amplo e mais brilhante; largura = 2λL/a |
| Mínimos (franjas escuras) | um sen θ = mλ (m = ±1, ±2, ...) |
| Máximos secundários | Aproximadamente entre mínimos; muito mais escuro |
### Grade de difração
N fendas igualmente espaçadas (espaçamento d) produzem máximos muito nítidos:
d sen θ = mλ (m = 0, 1, 2, ...)
| Propriedade | Efeito |
|----------|--------|
| Mais fendas (N maior) | Máximos mais nítidos e brilhantes |
| Poder de resolução | R = mN (pode distinguir comprimentos de onda próximos) |
| Aplicações | Espectroscopia, medição de comprimento de onda |
### Critério Rayleigh (limite de resolução)
Duas fontes pontuais só podem ser resolvidas quando o máximo central de uma cai sobre o primeiro mínimo da outra:
θ_min = 1,22 λ/D
onde D é o diâmetro da abertura.
| Sistema | λ | D | θ_min |
|----|---|---|-------|
| Olho humano | 550 nm | 5mm | 1,3 × 10⁻⁴rad (~0,01°) |
| Telescópio Espacial Hubble | 550 nm | 2,4m | 2,8 × 10⁻⁷ rad |
| Radiotelescópio (Arecibo) | 21cm | 305m | 8,4 × 10⁻⁴ rad |
---

## Polarização
**Polarização** descreve a orientação da oscilação do campo elétrico em uma onda transversal.
### Tipos de polarização
| Tipo | Descrição |
|------|-------------|
| **Linear** | E oscila em um plano fixo |
| **Circular** | E gira em círculo (destro ou canhoto) |
| **Elíptico** | E traça uma elipse (mais geral) |
| **Não polarizado** | Mistura aleatória de todas as polarizações (maioria da luz natural) |
### Lei de Malus
Quando a luz polarizada passa através de um polarizador em um ângulo θ com a direção de polarização:
I = I₀ cos²θ
| Ânguloθ | Intensidade transmitida |
|--------|----------------------|
| 0° | 100% (I₀) |
| 30° | 75% |
| 45° | 50% |
| 60° | 25% |
| 90° | 0% (completamente bloqueado) |
### Polarização por Reflexão (Ângulo de Brewster)
A luz refletida no ângulo de Brewster é completamente polarizada:
tan θ_B = n₂/n₁
| Interface | n₁ | n₂ | θ_B |
|-----------|----|----|-----|
| Ar → vidro | 1,0 | 1,5 | 56,3° |
| Ar → água | 1,0 | 1,33 | 53,1° |
| Vidro → diamante | 1,5 | 2,42 | 58,1° |
---

## Óptica Geométrica
A óptica geométrica (de raios) trata a luz como raios que viajam em linhas retas, curvando-se nas interfaces.
### Lei de Snell (Refração)
n₁ sen θ₁ = n₂ sen θ₂
| Materiais | Índice de refração n |
|----------|-------------------|
| Vácuo | 1.000 |
| Ar | 1.0003 |
| Água | 1,33 |
| Vidro (coroa) | 1,52 |
| Vidro (pederneira) | 1,62 |
| Diamante | 2,42 |
### Reflexão Interna Total
Quando a luz viaja de um meio mais denso para um meio menos denso, além do **ângulo crítico**:
θ_c = arco seno (n₂/n₁)
Toda a luz é refletida – é assim que funcionam as fibras ópticas.
### Equação de lentes finas
1/f = 1/d_o + 1/d_i
| Quantidade | Significado |
|----------|---------|
| f | Distância focal |
| d_o | Distância do objeto |
| d_i | Distância da imagem |
| M = −d_i/d_o | Ampliação |
| Tipo de lente | f | Imagem |
|-----------|---|-------|
| Convergente (convexo) | Positivo | Real (se d_o > f) ou virtual |
| Divergente (côncavo) | Negativo | Sempre virtual, vertical, reduzido |
### Equação do espelho
Mesma forma da equação da lente: 1/f = 1/d_o + 1/d_i, onde f = R/2 para espelhos esféricos.
---

## Óptica de Fourier
A óptica de Fourier trata a imagem e a difração como operações de transformada de Fourier.
### Princípio-chave
O padrão de difração de campo distante de uma abertura é a **transformada de Fourier** da função de abertura.
| Abertura | Padrão de difração (transformada de Fourier) |
|----------|----------------------------------------|
| Fenda única | função sinc |
| Abertura circular | Disco arejado (J₁(r)/r) |
| Abertura retangular | Sincronização 2D |
| Grade | Funções delta discretas |
### Transformada Óptica de Fourier
Uma lente realiza uma transformada de Fourier 2D: colocar um objeto no plano focal frontal produz sua transformada de Fourier no plano focal posterior.
### Aplicativos
| Aplicação | Como a Óptica Fourier ajuda |
|------------|--------------|
| Filtragem de imagens | Coloque máscaras no plano de Fourier para bloquear/passar frequências espaciais |
| Detecção de bordas | Filtragem passa-alta no plano de Fourier |
| Reconhecimento de padrões | Correlação via transformadas de Fourier |
| Holografia | Gravação e reconstrução de frentes de onda |
| Computação óptica | Realizando transformadas de Fourier na velocidade da luz |
---

## Som e Acústica
### Propriedades das ondas sonoras
| Propriedade | Faixa típica | Unidade |
|----------|-------------|------|
| Frequência | 20 − 20.000 (audição humana) | Hz |
| Velocidade (ar, 20°C) | 343 | m/s |
| Velocidade (água) | 1.480 | m/s |
| Velocidade (aço) | 5.960 | m/s |
| Limiar de intensidade | 10⁻¹² | L/m² |
### Escala de decibéis
β = 10 log₁₀(I/I₀) dB, onde I₀ = 10⁻¹² W/m²
| Som | Intensidade (W/m²) | Nível (dB) |
|-------|-------------------|--------|
| Limiar de audição | 10⁻¹² | 0 |
| Folhas farfalhantes | 10⁻¹¹ | 10 |
| Conversa normal | 10⁻⁶ | 60 |
| Concerto de rock | 1 | 120 |
| Limiar de dor | 10 | 130 |
| Motor a jato | 100 | 140 |
### Efeito Doppler
Frequência observada quando a fonte e o observador se movem um em relação ao outro:
f' = f(v ± v_o)/(v ∓ v_s)
| Cenário | Efeito |
|----------|--------|
| Fonte se aproximando | Frequência mais elevada (deslocamento para o azul da luz) |
| Fonte recuando | Frequência mais baixa (desvio para o vermelho da luz) |
| Aplicações | Radar, ultrassom médico, astronomia (desvio para o vermelho das galáxias) |
---

## Relevância para aprendizado de máquina e ciência de dados
| Conceito de Onda/Óptica | Aplicação |
|----------|-------------|
| Equação de onda | Redes neurais informadas pela física, análise de dados sísmicos, processamento de áudio |
| Análise de Fourier | Fundação de processamento de sinais, análise espectral, extração de características |
| Transformada de Fourier | As CNNs realizam implicitamente análises de Fourier locais; FFT usado no pré-processamento de dados |
| Interferência | Computação analógica, redes neurais ópticas |
| Difração | Modelos de formação de imagens, algoritmos de desfoque, fotografia computacional |
| Polarização | Sensoriamento remoto, classificação de materiais, análise de imagens de satélite |
| Óptica geométrica | Modelos de câmeras em visão computacional, traçado de raios para geração de dados sintéticos |
| Equação da lente | Calibração de câmera, estimativa de profundidade, reconstrução 3D |
| Óptica de Fourier | Computação óptica, redes neurais profundas difrativas (D²NN) |
| Efeito Doppler | Processamento de sinais de radar, imagens médicas (ultrassom Doppler), estimativa de velocidade |
| Escala de decibéis | Engenharia de recursos de áudio, pré-processamento de reconhecimento de fala |
| Teoria da amostragem | Teorema de Nyquist-Shannon conecta a teoria das ondas ao processamento digital de sinais |
---

## Resumo
| Tópico | Ideia Central | Equação Chave |
|-------|-----------|------------|
| Equação de onda | As ondas se propagam com velocidade c | ∂²u/∂t² = c²∂²u/∂x² |
| Superposição | As ondas se somam linearmente | você = você₁ + você₂ |
| Interferência | Fase determina reforço | Δφ = 2πΔL/λ |
| Difração | Ondas contornam obstáculos | um sen θ = mλ (fenda única) |
| Polarização | Orientação da oscilação | Lei de Malus: I = I₀cos²θ |
| Óptica geométrica | Luz como raios | Lei de Snell: n₁sinθ₁ = n₂sinθ₂ |
| Óptica de Fourier | Imagem como transformada de Fourier | Campo distante = FT de abertura |
| Efeito Doppler | Mudança de frequência do movimento | f' = f(v ± v_o)/(v ∓ v_s) |
As ondas são a linguagem universal dos sistemas oscilantes. Esteja você processando sinais de áudio, analisando séries temporais, projetando sistemas de reconhecimento de imagem ou construindo simulações físicas, a matemática das ondas – superposição, análise de Fourier, interferência, difração – fornece o kit de ferramentas essencial. A óptica, como a ciência das ondas mais madura, oferece tanto a base teórica quanto as técnicas práticas que permeiam a moderna ciência de dados.