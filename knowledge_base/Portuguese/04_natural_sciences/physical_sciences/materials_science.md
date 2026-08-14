<!--
---
# Metadata
title: "Materials Science"
description: "Crystal structures, polymers, alloys, semiconductors, nanomaterials"
category: "Natural Sciences"
subcategory: "Physical Sciences"
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
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to physical_sciences/ subfolder; added subcategory field"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Natural Sciences Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [materials, science, natural-sciences]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Ciência dos Materiais
A ciência dos materiais é o estudo de como a estrutura de um material (em escalas atômica, microscópica e macroscópica) determina suas propriedades e como os métodos de processamento podem ser usados ​​para controlar essa estrutura para alcançar o desempenho desejado. É a área que responde a perguntas como: por que o aço é forte, mas pesado? Por que o vidro é transparente, mas quebradiço? Como podemos fabricar baterias que carreguem mais rápido? Que materiais sobreviverão às condições de Marte? Cada peça de tecnologia que você já usou é feita de materiais, e os avanços na tecnologia quase sempre exigem avanços nos materiais.
---

## O Tetraedro da Ciência dos Materiais
Os quatro elementos interligados que definem o campo:
| Elemento | Descrição |
|--------|-------------|
| **Estrutura** | Como os átomos e as moléculas estão dispostos (estrutura cristalina; contornos de grão; defeitos) |
| **Propriedades** | Como o material se comporta (mecânico; elétrico; térmico; óptico; magnético) |
| **Processamento** | Como o material é fabricado e moldado (fundição; sinterização; dopagem; recozimento) |
| **Desempenho** | Como o material funciona em uma aplicação real |
O insight principal: mudar o processamento muda a estrutura, o que muda as propriedades, o que muda o desempenho.
---

## Classes de Materiais
### Visão geral
| Classe | Colagem | Propriedades Chave | Exemplos |
|-------|--------|---------------|---------|
| **Metais** | Metálico (elétrons deslocalizados) | Forte; dúctil; condutor; opaco | Aço; alumínio; cobre; titânio |
| **Cerâmica** | Iônico/covalente | Duro; frágil; resistente ao calor; isolante | Alumina; carboneto de silício; vidro; porcelana |
| **Polímeros** | Covalente (cadeias) + van der Waals | Leve; flexível; isolante; baixo ponto de fusão | Polietileno; nylon; borracha; epóxi |
| **Compostos** | Combinação de duas ou mais classes | Propriedades sob medida; alta resistência ao peso | Fibra de carbono; fibra de vidro; concreto |
| **Semicondutores** | Covalente (com impurezas controladas) | Condutividade ajustável; base da eletrônica | Silício; germânio; arseneto de gálio |
| **Biomateriais** | Vários; biocompatível necessário | Interaja com sistemas biológicos | Implantes de titânio; colágeno; hidroxiapatita |
---

## Estruturas Cristalinas
### Estruturas Cristalinas Metálicas Comuns
| Estrutura | Átomos por célula unitária | Fração de Embalagem | Exemplos |
|-----------|-------------------|-----------------|---------|
| **FCC** (Cúbico Centrado na Face) | 4 | 0,74 (embalado mais próximo) | Alumínio; cobre; ouro; níquel; austenita (ferro γ) |
| **BCC** (Cúbico Centrado no Corpo) | 2 | 0,68 | Ferro (ferro alfa); cromo; tungstênio; molibdênio |
| **HCP** (Hexagonal Fechado) | 6 | 0,74 (embalado mais próximo) | Titânio; zinco; magnésio; cobalto |
### Por que a estrutura cristalina é importante
| Propriedade | Influência da Estrutura Cristalina |
|----------|-------------------------------|
| **Força** | Os sistemas de deslizamento (planos ao longo dos quais os átomos deslizam) diferem em estrutura; Os metais FCC são mais dúcteis que os HCP |
| **Densidade** | A fração de empacotamento determina o quão firmemente os átomos são empacotados |
| **Transformações de fase** | O ferro transforma-se de BCC em FCC a 912°C — esta é a base do tratamento térmico do aço |
| **Anisotropia** | As propriedades podem variar com a direção em cristais não cúbicos |
---

## Propriedades Mecânicas
### Principais métricas
| Propriedade | Definição | Unidades | Valores típicos |
|----------|-----------|-------|----------------|
| **Módulo de Young (E)** | Rigidez; tensão/deformação na região elástica | GPa | Aço: 200; Alumínio: 70; Borracha: 0,01–0,1 |
| **Força de rendimento** | Tensão na qual começa a deformação permanente (plástica) | MPa | Aço: 250–1000; Alumínio: 40–500 |
| **Resistência à tração (UTS)** | Tensão máxima antes da falha | MPa | Aço: 400–2000; Alumínio: 90–600 |
| **Ductilidade (% alongamento)** | Quanto um material estica antes de quebrar | % | Aço: 10–50; Vidro: <1 |
| **Resistência** | Energia absorvida antes da fractura (área sob a curva tensão-deformação) | MJ/m³ | Aço: alto; cerâmica: baixa |
| **Dureza** | Resistência à indentação superficial | Várias escalas | Diamante: mais difícil; talco: mais macio |
### Mecanismos de Fortalecimento
| Mecanismo | Como funciona | Exemplo |
|-----------|-------------|---------|
| **Refinamento de grãos** | Grãos menores = mais limites de grão = mais difícil para os deslocamentos se moverem | Relação Hall-Petch |
| **Fortalecimento de solução sólida** | Átomos estranhos distorcem a rede; impedir o movimento de deslocamento | Adicionando zinco ao cobre → latão |
| **Endurecimento por precipitação** | Partículas pequenas bloqueiam o movimento de deslocamento | Ligas de alumínio envelhecidas |
| **Endurecimento por trabalho (endurecimento por deformação)** | A deformação plástica aumenta a densidade das discordâncias; eles se enredam e se impedem | Aço laminado a frio |
| **Reforço de compósito** | Fibras fortes em uma matriz mais macia suportam a carga | Polímero reforçado com fibra de carbono |
---

## Propriedades Elétricas e Térmicas
### Condutividade Elétrica
| Tipo de material | Condutividade (S/m) | Mecanismo |
|--------------|--------------------|-----------|
| **Condutores** (cobre, prata) | 10^7 – 10^8 | Elétrons livres em ligações metálicas |
| **Semicondutores** (silício, GaAs) | 10^-6 – 10^4 | Ajustável por doping; engenharia de banda gap |
| **Isoladores** (vidro, borracha) | 10^-12 – 10^-20 | Grande lacuna de banda; elétrons ligados |
| **Supercondutores** | Infinito (abaixo da temperatura crítica) | Resistência elétrica zero; Efeito Meissner |
### Propriedades Térmicas
| Propriedade | Descrição | Importante para |
|----------|-------------|---------------|
| **Condutividade térmica** | Quão bem o calor flui através do material | Dissipadores de calor; isolamento |
| **Expansão térmica** | Quanto um material se expande quando aquecido | Combinação de materiais em compósitos; pontes; trilhos |
| **Capacidade térmica específica** | Energia necessária para aumentar a temperatura em 1°C | Armazenamento de energia térmica |
| **Ponto de fusão** | Temperatura à qual o sólido se torna líquido | Aplicações de alta temperatura |
---

## Polímeros
### Tipos de Polímeros
| Tipo | Estrutura | Propriedades | Exemplos |
|------|-----------|-----------|---------|
| **Termoplásticos** | Cadeias lineares ou ramificadas; forças intermoleculares fracas | Derreta quando aquecido; reciclável | Polietileno; poliestireno; náilon |
| **Termofixos** | Rede interligada; ligações covalentes entre cadeias | Não derreta; decompor-se a alta temperatura | Epóxi; borracha vulcanizada; Baquelite |
| **Elastômeros** | Levemente reticulado; correntes enroladas | Alongar e voltar à forma | Borracha natural; silicone; neoprene |
### Propriedades do Polímero
| Propriedade | Descrição |
|----------|------------|
| **Temperatura de transição vítrea (Tg)** | Abaixo de Tg: duro e quebradiço. Acima de Tg: macio e flexível |
| **Cristalinidade** | Os polímeros semicristalinos são mais fortes e opacos; amorfos são transparentes |
| **Peso molecular** | Maior CM = mais forte; mais difícil de processar |
| **Grau de polimerização** | Número de unidades monoméricas; afeta propriedades |
---

## Diagramas de fases
### Diagrama de Fases Ferro-Carbono (Simplificado)
| Fase | Conteúdo de carbono | Estrutura | Propriedades |
|-------|---------------|-----------|-----------|
| **Ferrita (α)** | Até 0,022% | Ferro BCC | Macio; dúctil; magnético |
| **Austenita (γ)** | Até 2,14% | Ferro FCC | Não magnético; moldável |
| **Cementita (Fe₃C)** | 6,67% | Ortorrômbico | Duro; quebradiço |
| **Perlita** | 0,76% (eutetóide) | Camadas alternadas de ferrita e cementita | Forte; difícil |
| **Martensita** | Qualquer (formado por têmpera rápida) | BCT (tetragonal centrado no corpo) | Muito difícil; quebradiço |
---

## Materiais Modernos e Emergentes
| Materiais | Descrição | Aplicação |
|----------|-------------|-------------|
| **Grafeno** | Camada única de átomos de carbono; material mais forte conhecido; excelente condutor | Eletrônica; compósitos; sensores |
| **Nanotubos de carbono** | Cilindros de grafeno enrolados; relação resistência-peso extrema | Compósitos; eletrônica; armazenamento de energia |
| **Perovskitas** | Estrutura cristalina ABX₃; intervalo de banda ajustável | Células solares; LEDs; detectores |
| **Estruturas metal-orgânicas (MOFs)** | Materiais cristalinos porosos; enorme área de superfície | Armazenamento de gás; catálise; distribuição de medicamentos |
| **Ligas com memória de forma** | Retorna à forma original quando aquecido | Stents; atuadores; estruturas auto-reparáveis ​​|
| **Metamateriais** | Microestrutura projetada fornece propriedades não encontradas na natureza | Índice de refração negativo; camuflagem |
| **Ligas de alta entropia** | Múltiplos elementos principais; combinações incomuns de propriedades | Ambientes extremos; aeroespacial |
---

## Resumo
A ciência dos materiais conecta a estrutura atômica de um material às suas propriedades macroscópicas e desempenho no mundo real. Os metais são fortes e condutores, mas pesados. A cerâmica é dura e resistente ao calor, mas quebradiça. Os polímeros são leves e flexíveis, mas limitados pela temperatura. Os compósitos combinam o melhor de diferentes classes. A estrutura cristalina determina o comportamento mecânico. O processamento – tratamento térmico, formação de ligas, endurecimento por trabalho – controla a microestrutura e, portanto, as propriedades. Materiais modernos como grafeno, perovskitas e MOFs ultrapassam os limites do que é possível. O campo é fundamentalmente interdisciplinar: a física explica as ligações, a química explica as reações, a engenharia explica o desempenho, e tudo isso é importante para todas as tecnologias, desde smartphones até naves espaciais.