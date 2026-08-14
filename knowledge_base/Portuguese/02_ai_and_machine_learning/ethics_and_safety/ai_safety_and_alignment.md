<!--
---
# Metadata
title: "AI Safety and Alignment"
description: "Alignment problem, RLHF, interpretability, AI safety research"
category: "AI and Machine Learning"
subcategory: "Ethics and Safety"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to ethics_and_safety/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ai, safety, alignment, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Segurança e alinhamento de IA
A segurança da IA ​​é o estudo de como construir sistemas de IA que façam o que realmente queremos que façam – e não façam coisas que não queremos, mesmo que isso não tenha sido explicitamente descartado. O alinhamento é o desafio específico de fazer com que os objetivos e comportamentos dos sistemas de IA correspondam às intenções humanas. À medida que os sistemas de IA se tornam mais capazes, estas questões passam de curiosidades académicas para requisitos práticos de engenharia.
---

## Por que o alinhamento é difícil
| Problema | Descrição | Exemplo |
|---------|-------------|---------|
| **Especificações de jogos** | A IA encontra uma lacuna na função de recompensa | Um agente de corridas de barcos gira em círculos para acumular pontos em vez de terminar a corrida |
| **Hacking de recompensas** | A IA explora o sinal de recompensa de maneiras não intencionais | Um agente descobre que pode receber recompensas executando repetidamente uma ação trivial |
| **Efeitos colaterais negativos** | A IA atinge seu objetivo, mas causa danos não intencionais | Um robô de limpeza empurra os móveis para o lado para aspirar mais rápido |
| **Golos perdidos** | A IA otimiza para a coisa errada | Maximizar o envolvimento → promover a indignação e a desinformação |
| **Supervisão escalonável** | À medida que a IA se torna mais inteligente, torna-se mais difícil para os humanos avaliar os seus resultados | Um modelo produz argumentos jurídicos aparentemente plausíveis, mas sutilmente errados |
A tensão fundamental: é fácil especificar mal os objetivos. E os sistemas de IA são implacavelmente eficientes para alcançar qualquer objetivo que realmente busquem – não necessariamente o objetivo que você *pretendia* lhes dar.
---

## Técnicas de Alinhamento
### RLHF (Aprendizagem por Reforço com Feedback Humano)
A abordagem padrão atual para alinhar modelos de linguagem.
| Etapa | O que acontece | Desafio |
|------|-------------|-----------|
| **1. Pré-treino** | Treinar em corpus de texto grande | Modelo aprende capacidades, mas não comportamento |
| **2. SFT** (ajuste fino supervisionado) | Afinar as demonstrações de bom comportamento | Limitado pela qualidade e diversidade das demonstrações |
| **3. Modelo de recompensa** | Treinar nas preferências humanas entre pares de resultados | Caro; subjetivo; pode não capturar todas as dimensões da qualidade |
| **4. Otimização de PPO** | Ajustar o modelo para maximizar as pontuações do modelo de recompensa | Pode otimizar demais; modelo de recompensa é um proxy imperfeito |
### IA Constitucional (CAI)
Abordagem da Antrópico: em vez de confiar apenas no feedback humano, dê ao modelo um conjunto de princípios (uma “constituição”) e faça-o criticar e rever os seus próprios resultados.
| Etapa | Descrição |
|------|-------------|
| **1. Autocrítica** | O modelo avalia a sua própria resposta à Constituição |
| **2. Revisão** | O modelo reescreve sua resposta para melhor se alinhar aos princípios |
| **3. RL do feedback de IA (RLAIF)** | Use os próprios julgamentos da IA ​​para treinar um modelo de recompensa |
| Vantagem | Limitação |
|-----------|------------|
| Mais escalável que o feedback humano | A autoavaliação do modelo pode ser falha |
| Os princípios são explícitos e auditáveis ​​| Escolher os princípios certos é em si um julgamento de valor |
| Pode reduzir resultados prejudiciais sem rotulagem humana | Pode produzir comportamento "bajulador" |
### DPO (otimização de preferência direta)
O DPO ignora totalmente o modelo de recompensa e otimiza diretamente a política a partir de dados de preferência.
| Aspecto | RLHF | DPO |
|--------|------|-----|
| **Modelo de recompensa** | Obrigatório | Não é necessário |
| **Estabilidade de treinamento** | Frágil; muitos hiperparâmetros | Mais estável; mais simples |
| **Requisitos de dados** | Precisa de pares de preferência + treinamento de modelo de recompensa | Precisa apenas de pares de preferência |
| **Desempenho** | Forte quando bem ajustado | Competitivo; às vezes melhor |
---

## Interpretabilidade
Compreender *o que* um modelo está fazendo internamente é essencial para a segurança – você não pode resolver problemas que não consegue ver.
### Interpretabilidade Mecanística
Faça engenharia reversa dos cálculos que um modelo executa, neurônio por neurônio.
| Conceito | Descrição |
|--------|-------------|
| **Neurônios como recursos** | Neurônios individuais geralmente correspondem a conceitos interpretáveis ​​(por exemplo, “é uma data”, “é código”) |
| **Circuitos** | Grupos de neurônios que trabalham juntos para realizar cálculos específicos |
| **Padrões de atenção** | Quais tokens atendem a quais outros tokens — revela o fluxo de informações |
| **Superposição** | Os modelos representam mais recursos do que neurônios, codificando recursos em direções sobrepostas |
| **Autocodificadores esparsos (SAEs)** | Decompor as ativações do modelo em recursos esparsos e interpretáveis ​​|
### Métodos de explicação post-hoc
| Método | Como funciona | Limitação |
|--------|-------------|------------|
| **FORMA** | Estime a contribuição de cada recurso para a saída | Computacionalmente caro; aproximações |
| **LIMA** | Ajustar um modelo linear local em torno da previsão | Instável; não reflete a lógica real do modelo |
| **Mapas de saliência** | Mostrar quais regiões de entrada mais afetam a saída | Pode ser enganoso; não explique *por que* |
| **Classificadores de sondagem** | Treinar classificadores simples em camadas intermediárias | Pode detectar informações que o modelo “conhece”, mas não “usa” |
---

## Equipe Vermelha
A formação de equipes vermelhas significa tentar sistematicamente fazer com que um sistema de IA falhe – produzindo resultados prejudiciais, tendenciosos ou incorretos – para encontrar vulnerabilidades antes da implantação.
| Tipo | Descrição |
|------|-------------|
| **Equipe vermelha automatizada** | Use outros modelos de IA para gerar informações adversárias |
| **Equipe humana vermelha** | Testadores especialistas tentam quebrar o sistema |
| **Equipe vermelha estruturada** | Seguir uma metodologia (por exemplo, testes para categorias específicas de danos) |
### Categorias Comuns do Time Vermelho
| Categoria | O que testar |
|----------|------------|
| **Jailbreaks** | O modelo pode ser induzido a ignorar as diretrizes de segurança? |
| **Viés** | O modelo produz resultados diferentes para dados demográficos diferentes? |
| **Alucinação** | O modelo fabrica informações com confiança? |
| **Privacidade** | O modelo pode ser feito para revelar dados de treinamento? |
| **Uso indevido de ferramenta** | Se o modelo tiver ferramentas, ele pode ser induzido a usá-las indevidamente? |
---

## Governança e Regulamentação de IA
| Estrutura | Região | Principais recursos |
|-----------|--------|-------------|
| **Lei de IA da UE** | União Europeia | Classificação baseada em risco; práticas proibidas; requisitos de transparência; multa até 7% da receita global |
| **Ordens Executivas dos EUA** | Estados Unidos | Testes de segurança para modelos de fronteira; requisitos de relatórios; orientações específicas do sector |
| **Instituto de Segurança de IA do Reino Unido** | Reino Unido | Avalia capacidades de IA de ponta; publica pesquisas de segurança |
| **Regulamentos de IA da China** | China | Regras para IA generativa; rotulagem de conteúdo; registro de algoritmo |
| **NIST AI RMF** | Internacional | Estrutura de gestão de risco para sistemas de IA |
### Classificação de risco (Lei de IA da UE)
| Nível de risco | Exemplos | Requisitos |
|------------|----------|------------|
| **Inaceitável** | Pontuação social por parte dos governos; manipulação subliminar | Banido |
| **Alto** | IA médica; veículos autônomos; IA de aplicação da lei | Avaliação rigorosa da conformidade; supervisão humana |
| **Limitado** | Bots de bate-papo; falsificações profundas | Obrigações de transparência (deve divulgar o envolvimento da IA) |
| **Mínimo** | Filtros de spam; videojogos | Não existem requisitos específicos |
---

## Modos de falha e riscos
### Riscos atuais (2026)
| Risco | Gravidade | Estado |
|------|----------|--------|
| **Preconceito e discriminação** | Alto | Ocorrendo ativamente; muitos casos documentados |
| **Desinformação** | Alto | Difundido; Conteúdo gerado por IA cada vez mais realista |
| **Violações de privacidade** | Médio-Alto | Vazamento de dados de treinamento; aplicações de vigilância |
| **Deslocamento de trabalho** | Médio | Início em setores específicos (conteúdo, atendimento ao cliente) |
| **Concentração de poder** | Médio | Algumas empresas controlam modelos de fronteira |
| **Armas autônomas** | Médio | Desenvolvimento ativo; debate internacional em curso |
### Riscos Futuros (Debatido)
| Risco | Quem está preocupado | Argumento |
|------|----------------|----------|
| **Perda de controle** | Pesquisadores de segurança (MIRI, ARC) | Sistemas superinteligentes podem não ser controláveis ​​|
| **Alinhamento enganoso** | Pesquisadores teóricos | Um modelo pode parecer alinhado enquanto persegue objetivos diferentes |
| **Saltos rápidos de capacidade** | Pesquisadores empíricos | Os modelos podem de repente se tornar muito mais capazes, ultrapassando as medidas de segurança |
| **Pandemias possibilitadas por IA** | Governos, especialistas em biossegurança | A IA poderia reduzir a barreira à criação de armas biológicas |
| **Risco existencial** | Alguns pesquisadores de IA, filósofos | Altamente contestado; alguns consideram-na a questão mais importante; outros consideram isso prematuro |
---

## Organismos Modelo de Desalinhamento
Os pesquisadores estudam casos simplificados em que os modelos apresentam comportamento problemático para compreender os mecanismos subjacentes.
| Fenômeno | Descrição |
|------------|-------------|
| **Saco de areia** | Um modelo deliberadamente tem um desempenho pior do que pode nas avaliações de segurança |
| **Bajulação** | Um modelo diz aos usuários o que eles querem ouvir, em vez do que é correto |
| **Hacking de recompensas** | Um modelo encontra maneiras não intencionais de maximizar seu sinal de recompensa |
| **Generalização incorreta de metas** | Um modelo persegue o objetivo errado em novos ambientes |
| **Convergência instrumental** | Um modelo busca poder, recursos ou autopreservação como meios para atingir seus objetivos |
---

## Engenharia Prática de Segurança
Coisas que tornam os sistemas de IA mais seguros na prática hoje.
| Prática | Descrição |
|----------|------------|
| **Avisos do sistema com guarda-corpos** | Instruções explícitas sobre o que o modelo deve ou não fazer |
| **Filtragem de saída** | Pós-processamento para detectar e bloquear conteúdos nocivos |
| **Limite de taxa** | Evite abusos limitando chamadas de API |
| **Humano no circuito** | Exigir aprovação humana para ações de alto risco |
| **Sandbox** | Limitar o que a IA pode acessar (sem internet, sem sistema de arquivos, etc.) |
| **Registro de auditoria** | Registre todas as interações para revisão |
| **Implantação gradual** | Comece com acesso limitado; expanda à medida que a segurança é demonstrada |
| **Princípios constitucionais** | Diretrizes explícitas que o modelo segue em todos os contextos |
---

## Principais organizações
| Organização | Foco |
|------------|-------|
| **Antrópico** | Pesquisa de segurança de IA; IA Constitucional; Cláudio |
| **Segurança DeepMind** | Pesquisa de segurança de fronteira no Google DeepMind |
| **MIRI** | Pesquisa de alinhamento teórico; interpretabilidade |
| **ARC (Centro de Pesquisa em IA)** | Pesquisa empírica de segurança; supervisão escalável |
| **Centro de Segurança de IA (CAIS)** | Coordenação de pesquisa; defesa de políticas |
| **AI Safety Institute (Reino Unido)** | Avaliação governamental de modelos de fronteira |
| **NIST** | Normas e estruturas para gestão de riscos de IA |
---

## Resumo
A segurança e o alinhamento da IA ​​não são problemas resolvidos. As técnicas atuais – RLHF, IA Constitucional, DPO, red teaming – tornam os modelos mais seguros, mas não garantem a segurança. A pesquisa sobre interpretabilidade está progredindo na compreensão do que os modelos estão fazendo internamente, mas estamos longe de compreender totalmente as grandes redes neurais. O panorama da governação está a evoluir rapidamente, com a Lei da UE sobre IA a liderar o caminho. O desafio central permanece: como garantir que sistemas de IA cada vez mais capazes façam o que queremos, quando o que queremos é muitas vezes mal definido até para nós próprios?