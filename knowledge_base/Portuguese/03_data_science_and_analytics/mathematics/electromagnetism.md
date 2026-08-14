<!--
---
# Metadata
title: "Electromagnetism"
description: "Electric and magnetic fields, Coulomb's law, Gauss's law, Faraday's law, Ampere's law, Maxwell's equations, electromagnetic waves, and RLC circuits"
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
    changes: "Initial deep-dive into electromagnetism"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [electromagnetism, maxwell-equations, electric-fields, magnetic-fields, electromagnetic-waves, circuits, gauss-law, faraday]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "classical_mechanics.md"
  - "real_analysis.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Eletromagnetismo
Eletromagnetismo é o estudo dos campos elétricos e magnéticos e suas interações. Unificado por Maxwell na década de 1860, o eletromagnetismo explica a luz, a eletricidade, o magnetismo, as ondas de rádio e a estrutura dos átomos. Foi a primeira força fundamental a ser totalmente compreendida matematicamente, e as suas equações inspiraram a relatividade especial de Einstein e a moderna teoria de campo.
---

## Campos Elétricos
### Lei de Coulomb
A força entre duas cargas pontuais q₁ e q₂ separadas pela distância r:
**F** = (1/4πε₀) · (q₁q₂/r²) · r̂
| Constante | Valor |
|----------|-------|
| ε₀ (permissividade do espaço livre) | 8,854 × 10⁻¹²F/m |
| 1/4πε₀ (constante k de Coulomb) | 8,988 × 10⁹ N·m²/C² |
### Definição de Campo Elétrico
**E** = **F**/q (força por unidade de carga)
Para uma carga pontual Q: **E** = (1/4πε₀) · (Q/r²) · r̂
### Linhas de Campo Elétrico
| Propriedade | Regra |
|----------|------|
| Direção | Aponte para longe das cargas positivas, em direção às negativas |
| Densidade | Linhas mais próximas = campo mais forte |
| Travessia | As linhas de campo nunca se cruzam |
| Condutores | As linhas encontram a superfície perpendicularmente |
### Potencial Elétrico (Tensão)
V = −∫ **E** · d**l** (a diferença de potencial é a integral de linha negativa de E)
**E** = −∇V (campo é o gradiente negativo de potencial)
Para uma carga pontual: V = (1/4πε₀) · Q/r
| Conceito | Fórmula | Unidade |
|--------|---------|------|
| Energia potencial | você = qV | Joules |
| Elétron-volt | 1eV = 1,602 × 10⁻¹⁹J | Unidade de energia |
| Superfície equipotencial | Superfície onde V é constante | E é perpendicular a ele |
---

## Lei de Gauss
### Declaração
O fluxo elétrico total através de qualquer superfície fechada é igual à carga fechada dividida por ε₀:
∮ **E** · d**A** = Q_enc / ε₀
Na forma diferencial: ∇ · **E** = ρ/ε₀
### Usando a Lei de Gauss
A lei de Gauss é mais útil quando a simetria permite que E seja retirado da integral.
| Simetria | Superfície Gaussiana | Resultado |
|----------|-----------------|--------|
| Esférico | Esfera | E = Q/(4πε₀r²) fora |
| Cilíndrico (carga de linha) | Cilindro | E = λ/(2πε₀r) |
| Planar (folha infinita) | Caixa de comprimidos | E = σ/(2ε₀) |
| Entre placas paralelas | Caixa de comprimidos | E = σ/ε₀ |
---

## Condutores e Capacitores
### Condutores em Equilíbrio Eletrostático
| Propriedade | Explicação |
|----------|------------|
| E = 0 dentro | Encargos reorganizados para cancelar campo interno |
| Todas as cargas na superfície | Sem carga líquida no interior |
| E perpendicular à superfície | Nenhuma componente tangencial (caso contrário, as cargas movem-se) |
| Equipotencial em todo | O mesmo V em todos os lugares dentro e na superfície |
### Capacitores
Um **capacitor** armazena energia em um campo elétrico entre dois condutores.
| Configuração | Capacitância |
|--------------|-------------|
| Placas paralelas | C = ε₀A/d |
| Cilíndrico | C = 2πε₀L / ln(b/a) |
| Esférico | C = 4πε₀ab / (b−a) |
| Fórmula | Expressão |
|--------|------------|
| Tensão de carga | Q = VC |
| Energia armazenada | U = ½CV² = ½Q²/C |
| Densidade energética | você = ½ε₀E² |
| Combinação de séries | 1/C_total = 1/C₁ + 1/C₂ + ... |
| Combinação paralela | C_total = C₁ + C₂ + ... |
### Dielétricos
A inserção de um dielétrico (material isolante) com κ constante aumenta a capacitância: C = κC₀.
---

## Campos Magnéticos
### Força Magnética
**F** = q(**v** × **B**) (força de Lorentz, componente magnético)
| Propriedade | Declaração |
|----------|-----------|
| Direção | Perpendicular a v e a B (regra da mão direita) |
| Trabalho realizado | Zero (a força é perpendicular à velocidade) |
| Movimento circular | Raio r = mv/(qB) em campo B uniforme |
### Lei Biot-Savart
O campo magnético devido a um pequeno elemento de corrente:
d**B** = (μ₀/4π) · I(d**l** × r̂) / r²
| Constante | Valor |
|----------|-------|
| μ₀ (permeabilidade do espaço livre) | 4π × 10⁻⁷ T·m/A |
### Lei de Ampère
∮ **B** · d**l** = μ₀I_enc
Na forma diferencial: ∇ × **B** = μ₀**J**
**Aplicativos:**
| Configuração | Campo B |
|-------------|---------|
| Fio longo e reto | B = μ₀I/(2πr) |
| Solenóide (interno) | B = μ₀nI |
| Toroide (dentro) | B = μ₀NI/(2πr) |
---

## Indução Eletromagnética
### Lei de Faraday
Um fluxo magnético variável induz uma força eletromotriz (EMF):
EMF = −dΦ_B/dt
onde Φ_B = ∫ **B** · d**A** é o fluxo magnético.
Na forma diferencial: ∇ × **E** = −∂**B**/∂t
**Lei de Lenz:** O EMF induzido se opõe à mudança no fluxo (o sinal negativo).
### Aplicações de Indução
| Aplicação | Princípio |
|------------|-----------|
| Gerador | Bobina giratória no campo B → EMF alternado |
| Transformador | Alteração da corrente no primário → EMF no secundário |
| Indutor | Opõe-se a mudanças na corrente: EMF = −L(dI/dt) |
| Correntes parasitas | Correntes induzidas em condutores granéis (travagem, aquecimento) |
### Indutores
| Fórmula | Expressão |
|--------|------------|
| Ligação de fluxo | Φ = LI |
| Energia armazenada | você = ½LI² |
| Combinação de séries | L_total = L₁ + L₂ + ... |
| Combinação paralela | 1/L_total = 1/L₁ + 1/L₂ + ... |
---

## Equações de Maxwell
As equações de Maxwell unificam a eletricidade e o magnetismo em uma única teoria.
### Na forma integral
| Equação | Nome | Declaração |
|----------|------|-----------|
| ∮ **E** · d**A** = Q/ε₀ | Lei de Gauss (elétrica) | Fluxo elétrico = carga encerrada |
| ∮ **B** · d**A** = 0 | Lei de Gauss (magnética) | Não há monopolos magnéticos |
| ∮ **E** · d**l** = −dΦ_B/dt | Lei de Faraday | Mudar B induz E |
| ∮ **B** · d**l** = μ₀I + μ₀ε₀ dΦ_E/dt | Lei de Ampère-Maxwell | E atual e mutável produz B |
### Em forma diferencial
| Equação | Nome | Expressão |
|----------|------|-----------|
| Gauss (elétrico) | ∇ · **E** = ρ/ε₀ |
| Gauss (magnético) | ∇ · **B** = 0 |
| Faraday | ∇ × **E** = −∂**B**/∂t |
| Ampère-Maxwell | ∇ × **B** = μ₀**J** + μ₀ε₀ ∂**E**/∂t |
### A Corrente de Deslocamento
Adição principal de Maxwell: o termo μ₀ε₀ ∂**E**/∂t (corrente de deslocamento). Isso garante a conservação da carga e prevê ondas eletromagnéticas.
---

## Ondas Eletromagnéticas
No vácuo (sem cargas, sem correntes), as equações de Maxwell produzem equações de onda:
∇²**E** = μ₀ε₀ ∂²**E**/∂t²
∇²**B** = μ₀ε₀ ∂²**B**/∂t²
**Velocidade da luz:** c = 1/√(μ₀ε₀) ≈ 3 × 10⁸ m/s
### Propriedades das ondas EM
| Propriedade | Descrição |
|----------|------------|
| Transversal | E e B são perpendiculares entre si e à direção de propagação |
| Em fase | E e B atingem máximos simultaneamente |
| Razão de magnitude | E = cB |
| Fluxo de energia | S = (1/μ₀)**E** × **B** (vetor de pontuação) |
| Intensidade | I = ⟨S⟩ = E₀²/(2μ₀c) |
### O Espectro Eletromagnético
| Tipo | Comprimento de onda | Frequência | Fonte |
|------|-----------|-----------|--------|
| Rádio | > 1m | < 300 MHz | Antennas |
| Microwave | 1 mm − 1 m | 300 MHz − 300 GHz | Magnetrons, klystrons |
| Infrared | 700 nm − 1 mm | 300 GHz − 430 THz | Thermal radiation |
| Visible | 400 − 700 nm | 430 − 750 THz | Atomic transitions |
| Ultraviolet | 10 − 400 nm | 750 THz − 30 PHz | Hot objects, stars |
| X-ray | 0.01 − 10 nm | 30 PHz − 30 EHz | Electron deceleration |
| Gamma ray | < 0.01 nm | >30 EHz | Processos nucleares |
---

## Circuitos CA
### Componentes do Circuito RLC
| Componente | Relação Tensão-Corrente | Impedância |
|-----------|-------------|-----------|
| Resistor (R) | V = IR | Z_R = R |
| Indutor (L) | V = L(dI/dt) | Z_L = jωL |
| Capacitor (C) | Eu = C(dV/dt) | Z_C = 1/(jωC) |
### Impedância e Ressonância
Impedância total (série RLC): Z = R + j(ωL − 1/ωC)
|ω| = √(R² + (ωL − 1/ωC)²)
**Ressonância:** Quando ωL = 1/ωC → ω₀ = 1/√(LC)
- Na ressonância: a impedância é mínima (= R), a corrente é máxima
- **Fator de qualidade:** Q = ω₀L/R (nitidez da ressonância)
### Potência em circuitos CA
| Quantidade | Fórmula |
|----------|---------|
| Potência média | P_méd = V_rms · I_rms · cos φ |
| Fator de potência | porque φ = R/\|Z\| |
| Tensão eficaz | V_rms = V₀/√2 |
---

## Relevância para aprendizado de máquina e ciência de dados
| Conceito EM | Aplicação |
|-----------|------------|
| Equações de Maxwell | Redes neurais informadas pela física, eletromagnetismo computacional |
| Equação de onda | Fundação de processamento de sinal, motivação de análise de Fourier |
| Espectro eletromagnético | Dados de sensores (câmaras infravermelhas, radar, imagens de satélite) |
| Circuitos AC / impedância | Noções básicas sobre hardware que executa ML (fontes de alimentação, integridade de sinal) |
| Vetor de Poynting | Fluxo de energia na comunicação sem fio (relevante para IoT/Edge ML) |
| Lei de Gauss | Análogo à divergência no cálculo vetorial, usado em simulações de dinâmica de fluidos |
| Capacitores/indutores | Computação analógica para redes neurais, hardware neuromórfico |
| Ressonância | Projeto de filtros, análise no domínio da frequência, métodos espectrais |
| Problemas de valor limite | Métodos de elementos finitos, simulações baseadas em malhas |
| Cálculo vetorial (∇·, ∇×) | Ferramentas matemáticas essenciais usadas em toda a teoria de ML |
---

## Resumo
| Direito | O que diz | Forma Diferencial |
|-----|-------------|-------------------|
| Gauss (elétrico) | Cargas criam divergência no campo elétrico | ∇ · E = ρ/ε₀ |
| Gauss (magnético) | Não há monopolos magnéticos | ∇ · B = 0 |
| Faraday | Alterar B cria ondulação E | ∇ × E = −∂B/∂t |
| Ampère-Maxwell | Atual e mutável E cria ondulação B | ∇ × B = μ₀J + μ₀ε₀∂E/∂t |
O eletromagnetismo é a teoria física mais completa e bem testada já construída. Suas equações – apenas quatro – descrevem tudo, desde a eletricidade estática até a luz e o comportamento de todos os dispositivos eletrônicos já construídos. Para os cientistas de dados, a compreensão do eletromagnetismo fornece uma intuição profunda para fenômenos ondulatórios, cálculo vetorial e a física subjacente a todo hardware de computação moderno.