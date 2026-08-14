---
# Metadata
title: "Thermodynamics and Statistical Mechanics"
description: "Laws of thermodynamics, entropy (thermodynamic and statistical), enthalpy, free energy, Carnot cycle, Boltzmann distribution, partition functions, and connections to information-theoretic entropy"
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
    changes: "Initial deep-dive into thermodynamics and statistical mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [thermodynamics, statistical-mechanics, entropy, enthalpy, free-energy, carnot-cycle, boltzmann, partition-function]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
  - "classical_mechanics.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Termodinâmica e Mecânica Estatística
A termodinâmica descreve o comportamento macroscópico dos sistemas em termos de temperatura, pressão e entropia – sem saber como são os átomos. A mecânica estatística explica a termodinâmica de baixo para cima: ela deriva propriedades macroscópicas do comportamento microscópico de um grande número de partículas. Juntos, eles fornecem a compreensão mais profunda de energia, entropia e equilíbrio — conceitos que migraram para a teoria da informação, aprendizado de máquina e muito mais.
---

## Variáveis ​​termodinâmicas e estado
### Variáveis ​​de Estado
| Variável | Tipo | Unidade | Descrição |
|----------|------|------|------------|
| Temperatura (T) | Intensivo | Kelvin (K) | Energia cinética média por partícula |
| Pressão (P) | Intensivo | Pascal (Pa) | Força por unidade de área |
| Volume (V) | Extenso | m³ | Espaço ocupado |
| Energia interna (U) | Extenso | Joule (J) | Energia microscópica total |
| Entropia (S) | Extenso | J/K | Medida de desordem/microestados |
| Número de partículas (N) | Extenso | moles ou contagem | Quantidade de substância |
**Variáveis ​​intensivas** não dependem do tamanho do sistema; **extensas** variáveis ​​sim.
### Equação de Estado
Para um gás ideal: PV = nRT = Nk_BT
| Constante | Valor |
|----------|-------|
| R (constante dos gases) | 8,314 J/(mol·K) |
| k_B (constante de Boltzmann) | 1,381 × 10⁻²³J/K |
| N_A (número de Avogadro) | 6,022 × 10²³ /mol |
---

## As Leis da Termodinâmica
### Lei Zero
Se A está em equilíbrio térmico com B e B com C, então A está em equilíbrio térmico com C.
**Significado:** A temperatura é bem definida e mensurável.
### Primeira Lei (Conservação de Energia)
ΔU = Q − W
| Símbolo | Significado |
|--------|---------|
| ΔU | Mudança na energia interna |
| P | Calor adicionado ao sistema |
| W | Trabalho realizado pelo sistema |
**Forma diferencial:** dU = δQ − δW = δQ − PdV
| Processo | Restrição | Consequência |
|--------|-----------|-------------|
| Isocórico | dV = 0 | W = 0, ΔU = Q |
| Isobárico | dP = 0 | W = PΔV |
| Isotérmico | dT = 0 | ΔU = 0 (gás ideal), Q = W |
| Adiabático | δQ = 0 | ΔU = −W |
### Segunda Lei (Entropia)
**Declaração de Clausius:** O calor não pode fluir espontaneamente do frio para o quente.
**Declaração Kelvin-Planck:** Nenhum motor pode converter todo o calor em trabalho.
**Declaração de entropia:** Para qualquer processo: ΔS_universe ≥ 0
| Tipo de processo | ΔS_universo |
|------------|------------|
| Reversível | = 0 |
| Irreversível (real) | > 0 |
**Alteração de entropia:** dS = δQ_rev / T
### Terceira Lei
À medida que T → 0 K, a entropia de um cristal perfeito se aproxima de zero: lim_{T→0} S = 0
**Significado:** O zero absoluto é inatingível em etapas finitas.
---

## Entropia em profundidade
### Entropia Termodinâmica
S é uma função de estado. Para um processo reversível entre os estados A e B:
ΔS = ∫_A^B δQ_rev / T
**Exemplo resolvido:** Mudança de entropia ao aquecer água de T₁ para T₂ a pressão constante.
ΔS = ∫_{T₁}^{T₂} (mc_p/T) dT = mc_p ln(T₂/T₁)
### Entropia Estatística (Boltzmann)
S = k_B ln Ω
onde Ω é o número de microestados consistente com o macroestado.
| Macroestado | Microestados (Ω) | Entropia |
|-------|-------|--------|
| Todo o gás na metade da caixa | Pequeno | Baixo |
| Gás distribuído uniformemente | Muito grande | Alto |
| Cristal perfeito a 0 K | 1 | 0 |
**Conexão:** A segunda lei torna-se estatística – os sistemas evoluem em direção a macroestados com mais microestados simplesmente porque são esmagadoramente mais prováveis.
---

## Entalpia e Energia Livre
### Entalpia
H = U + PV
Útil para processos a pressão constante (principalmente química e biologia).
ΔH = Q_p (calor a pressão constante)
### Helmholtz Energia Livre
F = você − TS
| Propriedade | Declaração |
|----------|-----------|
| Significado | Trabalho máximo extraível a T, V constantes |
| Equilíbrio | Sistema minimiza F em constante T, V |
| Relação com a função de partição | F = −k_BT ln Z |
### Energia Livre de Gibbs
G = H − TS = U + PV − TS
| Propriedade | Declaração |
|----------|-----------|
| Significado | Trabalho máximo de não expansão a constante T, P |
| Equilíbrio | Sistema minimiza G em constante T, P |
| Espontaneidade | ΔG < 0 → espontâneo; ΔG = 0 → equilíbrio |
| Reações químicas | ΔG = ΔH − TΔS determina a direção |
### Resumo dos Potenciais Termodinâmicos
| Potencial | Variáveis ​​Naturais | Diferencial | Minimizado Quando |
|-----------|-------------------|-------------|----------------|
| U (energia interna) | S, V | dU = TdS − PdV | Sistema isolado |
| H (entalpia) | S, P | dH = TdS + VdP | Constante P, adiabática |
| F (Helmholtz) | T, V | dF = −SdT − PdV | Constante T, V |
| G (Gibbs) | T, P | dG = −SdT + VdP | Constante T, P |
---

## O Ciclo de Carnot
O **ciclo de Carnot** é a máquina térmica mais eficiente possível, operando entre temperaturas T_H (quente) e T_C (frio).
### Quatro etapas
| Palco | Processo | O que acontece |
|-------|------------|-------------|
| 1 → 2 | Expansão isotérmica | Absorver calor Q_H do reservatório quente em T_H |
| 2 → 3 | Expansão adiabática | O gás esfria de T_H para T_C |
| 3 → 4 | Compressão isotérmica | Rejeitar o calor Q_C para o reservatório frio em T_C |
| 4 → 1 | Compressão adiabática | O gás aquece de T_C a T_H |
### Eficiência de Carnot
η_Carnot = 1 − T_C/T_H
| T_H | T_C | η_Carnot |
|-----|-----|----------|
| 500 mil | 300 mil | 40% |
| 1000K | 300 mil | 70% |
| 300 mil | 299 mil | 0,33% |
**Nenhum motor real pode exceder a eficiência de Carnot.** Os motores reais são sempre irreversíveis (atrito, turbulência, diferenças finitas de temperatura).
---

## Mecânica Estatística
### A Distribuição Boltzmann
Para um sistema em equilíbrio térmico à temperatura T, a probabilidade de estar em um microestado com energia E_i:
P(E_i) = (1/Z) e^{−E_i / k_BT}
onde Z é a **função de partição**:
Z = Σᵢ e^{−E_i / k_BT}
### A função de partição
Z codifica todas as informações termodinâmicas sobre o sistema.
| Quantidade | Fórmula |
|----------|---------|
| Energia livre de Helmholtz | F = −k_BT ln Z |
| Energia média | ⟨E⟩ = −∂(ln Z)/∂β onde β = 1/(k_BT) |
| Entropia | S = k_B(ln Z + β⟨E⟩) |
| Capacidade térmica | C_V = ∂⟨E⟩/∂T = k_Bβ²(⟨E²⟩ − ⟨E⟩²) |
| Pressão | P = (1/β) ∂(ln Z)/∂V |
### Exemplo resolvido: sistema de dois estados
Uma partícula pode estar no estado 0 (energia 0) ou no estado 1 (energia ε).
Z = 1 + e^{−βε}
| Quantidade | Resultado |
|----------|--------|
| P(estado 0) | 1/(1 + e^{−βε}) |
| P(estado 1) | e^{−βε}/(1 + e^{−βε}) |
| ⟨E⟩ | ε/(1 + e^{βε}) |
| Limite T superior (β→0) | ⟨E⟩ → ε/2 (probabilidade igual) |
| Limite T inferior (β→∞) | ⟨E⟩ → 0 (estado fundamental) |
### Teorema da Equipartição
Cada grau de liberdade quadrático contribui com ½k_BT para a energia média.
| Sistema | Graus de liberdade | ⟨E⟩ |
|--------|-------------------|------|
| Gás monoatômico (He) | 3 tradução | (3/2)k_BT |
| Gás diatômico (N₂) na sala T | 3 trans + 2 podridão | (5/2)k_BT |
| Gás diatômico em alta T | 3 trans + 2 podridão + 1 vibração | (7/2)k_BT |
| Sólido (modelo Einstein) | 3 vibracionais (por átomo) | 3k_BT |
---

## Conexão com a Teoria da Informação
### Entropia de Shannon vs Entropia Termodinâmica
| Aspecto | Entropia de Shannon H(X) | Entropia Termodinâmica S |
|--------|---------------------|-----------------------|
| Definição | −Σ pᵢ log pᵢ | k_B ln Ω (ou −k_B Σ pᵢ ln pᵢ) |
| Máximo quando | Distribuição uniforme | Equilíbrio térmico |
| Medidas | Incerteza/conteúdo informativo | Número de microestados acessíveis |
| Unidades | Bits ou limpos | J/K |
**Fórmula de entropia de Gibbs:** S = −k_B Σᵢ pᵢ ln pᵢ (idêntica em forma à entropia de Shannon)
### Princípio da Entropia Máxima
Ambos os campos utilizam o mesmo princípio: a distribuição que melhor representa o nosso estado de conhecimento é aquela que maximiza a entropia sujeita a restrições conhecidas.
| Restrição | Distribuição resultante |
|-----------|-----------|
| Média conhecida | Distribuição exponencial |
| Média e variância conhecidas | Distribuição gaussiana |
| Energia conhecida ⟨E⟩ | Distribuição Boltzmann |
| Sem restrições | Distribuição uniforme |
### Princípio de Landauer
Apagar um bit de informação dissipa pelo menos k_BT ln 2 de energia na forma de calor. Isso conecta o processamento de informações diretamente à termodinâmica – a computação tem um custo energético fundamental.
---

## Relevância para aprendizado de máquina e ciência de dados
| Conceito Thermo/StatMech | Aplicação |
|------------------------|-------------|
| Distribuição Boltzmann | Função Softmax, modelos baseados em energia, recozimento simulado |
| Função de partição | Constante de normalização em modelos probabilísticos, intratáveis ​​em geral |
| Energia grátis | Inferência variacional (minimizando a energia livre variacional = minimizando a divergência KL) |
| Entropia | Regularização, exploração em RL (RL de entropia máxima), árvores de decisão |
| Princípio da entropia máxima | Classificadores MaxEnt, seleção prévia, estimativa de distribuição |
| Recozimento simulado | Otimização global através da redução gradual da “temperatura” |
| Mecânica estatística | Compreender as transições de fase na aprendizagem (grokking, descida dupla) |
| Equipartição | Compreendendo a distribuição de energia em simulações físicas |
| Princípio de Landauer | Limites fundamentais da computação, computação reversível |
| Amostragem de Gibbs | Método MCMC inspirado diretamente na mecânica estatística |
| Temperatura (em softmax) | Controla a aleatoriedade das previsões: P(i) ∝ exp(z_i/T) |
---

## Resumo
| Direito/Conceito | Ideia Central | Fórmula |
|------------|-----------|--------|
| Lei zero | A temperatura está bem definida | Transitividade do equilíbrio térmico |
| Primeira lei | A energia é conservada | ΔU = Q − W |
| Segunda lei | A entropia do universo aumenta | ΔS ≥ 0 |
| Terceira lei | O zero absoluto é inatingível | S → 0 como T → 0 |
| Entropia de Boltzmann | A entropia conta microestados | S = k_B ln Ω |
| Distribuição Boltzmann | Probabilidade de estados de energia | P ∝ e^{−E/k_BT} |
| Função de partição | Codifica todas as informações termodinâmicas | Z = Σ e^{−E_i/k_BT} |
| Energia grátis | Trabalho útil disponível | F = U − TS, G = H − TS |
| Eficiência de Carnot | Eficiência máxima do motor térmico | η = 1 − T_C/T_H |
A termodinâmica e a mecânica estatística são onde a física encontra a teoria da informação. A mesma entropia que governa os motores térmicos governa a compressão de dados. A mesma distribuição de Boltzmann que descreve as moléculas de gás alimenta a camada softmax em cada classificador. A compreensão dessas conexões oferece uma visão unificada da física, da probabilidade e do aprendizado de máquina.