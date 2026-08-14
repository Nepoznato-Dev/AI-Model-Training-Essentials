<!--
---
# Metadata
title: "Federated Learning and Privacy"
description: "Decentralised training, differential privacy, secure aggregation"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
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
    changes: "Moved to architectures/ subfolder; added subcategory field"
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
tags: [federated, learning, privacy, ai-and-machine-learning]
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
# Aprendizagem Federada e Privacidade
O aprendizado federado é uma técnica para treinar modelos de aprendizado de máquina em vários dispositivos ou organizações sem compartilhar os dados brutos. Em vez de enviar dados para um servidor central, cada dispositivo treina um modelo local e compartilha apenas as atualizações do modelo (gradientes ou pesos). O servidor central agrega essas atualizações para produzir um modelo global. Ele foi projetado pelo Google para treinar modelos de linguagem de teclado em telefones Android – e desde então se tornou uma técnica chave para IA que preserva a privacidade.
---

## Por que aprendizagem federada?
| Motivação | Descrição | Exemplo |
|------------|-------------|---------|
| **Privacidade de dados** | Os dados brutos nunca saem do dispositivo | Os registros médicos ficam no hospital; fotos ficam no celular |
| **Conformidade regulatória** | GDPR, HIPAA e outras regulamentações restringem o compartilhamento de dados | Os bancos podem colaborar sem compartilhar dados de clientes |
| **Volume de dados** | Mover dados é caro e lento | O treinamento em bilhões de telefones é impraticável se os dados precisarem ser carregados |
| **Sensibilidade dos dados** | Alguns dados são demasiado sensíveis para serem partilhados, mesmo com consentimento | Inteligência governamental; dados pessoais de saúde |
---

## Como funciona o aprendizado federado
### O Protocolo Básico (FedAvg)
| Etapa | O que acontece |
|------|-------------|
| **1. Inicializar** | Servidor central cria modelo global com pesos aleatórios |
| **2. Distribuir** | Servidor envia o modelo global atual para dispositivos selecionados |
| **3. Treinamento local** | Cada dispositivo treina o modelo em seus dados locais por várias épocas |
| **4. Carregar** | Os dispositivos enviam seus pesos de modelo atualizados (não dados) de volta ao servidor |
| **5. Agregado** | Servidor calcula a média dos pesos (Média Federada) para criar um novo modelo global |
| **6. Repetir** | Volte ao passo 2 até que o modelo convirja |
```
Server: global_model = average(local_model_1, local_model_2, ..., local_model_n)
```

### Principais Propriedades
| Propriedade | Descrição |
|----------|------------|
| **Dados não IID** | Cada dispositivo possui distribuições de dados diferentes (não independentes e distribuídas de forma idêntica) |
| **Dados não balanceados** | Alguns dispositivos possuem muitos dados, outros possuem muito poucos |
| **Participação parcial** | Nem todos os dispositivos estão disponíveis em todas as rodadas |
| **Eficiência de comunicação** | O gargalo é a comunicação, não a computação |
---

## Variantes de aprendizagem federada
| Variante | Descrição | Vantagem |
|--------|-------------|-----------|
| **MédiaFed** | Pesos médios do modelo entre dispositivos | Simples; funciona bem para dados IID |
| **FedProx** | Adiciona um termo proximal ao treinamento local | Melhor para dados não IID |
| **ANDAIME** | Usa variáveis ​​de controle para corrigir a heterogeneidade dos dados | Convergência mais rápida em dados não IID |
| **FedSGD** | Como o FedAvg, mas com uma etapa de gradiente por rodada | Menor custo de comunicação por rodada |
| **FL personalizado** | Cada dispositivo mantém um modelo personalizado ao lado do global | Melhor desempenho por dispositivo |
| **FL vertical** | Características diferentes (não amostras diferentes) entre as partes | Quando as partes detêm diferentes aspectos dos mesmos dados |
---

## Privacidade Diferencial
A privacidade diferencial (DP) fornece uma garantia matemática de que a saída de um algoritmo não revela se os dados de algum indivíduo foram incluídos.
### Definição Central
Um mecanismo M satisfaz a privacidade diferencial (ε, δ) se para quaisquer dois conjuntos de dados D e D' que diferem em um registro:
```
P(M(D) ∈ S) ≤ e^ε × P(M(D') ∈ S) + Î´
```

| Parâmetro | Significado |
|-----------|---------|
| **ε (épsilon)** | Orçamento de privacidade. Menor = mais privado. Valores típicos: 0,1–10. |
| **δ (delta)** | Probabilidade de falha na garantia de privacidade. Normalmente definido como 1/N (inverso do tamanho do conjunto de dados). |
### Mecanismos para adicionar privacidade
| Mecanismo | Como funciona | Caso de uso |
|-----------|-------------|----------|
| **Mecanismo gaussiano** | Adicione ruído gaussiano calibrado para a sensibilidade da consulta | Valores contínuos (pesos do modelo) |
| **Mecanismo Laplace** | Adicionar ruído de Laplace | Contando consultas |
| **Mecanismo exponencial** | Selecionar resultados com probabilidade proporcional à sua utilidade | Escolhas discretas |
### DP-SGD (Descida Gradiente Estocástica Diferencialmente Privada)
| Etapa | Descrição |
|------|-------------|
| 1. Calcular gradientes por amostra | Em vez de gradientes em lote |
| 2. Gradientes de clipe | Limita a norma máxima de cada gradiente (limita a influência de qualquer amostra única) |
| 3. Adicione ruído | Adicione ruído gaussiano calibrado ao gradiente agregado |
| 4. Atualizar parâmetros | Degrau de descida gradiente padrão |
| Compensação | Descrição |
|-----------|------------|
| **Privacidade versus precisão** | Maior privacidade (ε inferior) requer mais ruído, o que reduz a precisão do modelo |
| **Privacidade versus tempo de treinamento** | Mais ruído significa convergência mais lenta |
| **Acompanhamento do orçamento de privacidade** | Cada etapa do treinamento consome parte do orçamento de privacidade; uma vez gasto, não pode ser recuperado |
---

## Combinando aprendizagem federada com privacidade diferencial
| Camada | Proteção |
|-------|-----------|
| **Aprendizagem federada** | Os dados brutos permanecem nos dispositivos |
| **Privacidade diferencial** | Até as atualizações do modelo são barulhentas, protegendo as contribuições individuais |
| **Agregação segura** | O servidor vê apenas o agregado de todas as atualizações, não as individuais |
Esta combinação proporciona fortes garantias de privacidade: mesmo que o servidor esteja comprometido, não é possível determinar se os dados de algum indivíduo específico foram utilizados no treinamento.
---

## Outras técnicas de preservação de privacidade
### Computação Multipartidária Segura (SMPC)
Múltiplas partes calculam uma função sobre seus dados combinados sem revelar suas entradas individuais.
| Recurso | Descrição |
|--------|-------------|
| **Como funciona** | Os dados são divididos em compartilhamentos distribuídos entre as partes; cálculo acontece em ações |
| **Garantia** | Nenhuma parte aprende nada sobre as contribuições dos outros |
| **Despesas gerais** | Custos significativos de comunicação e computação |
| **Caso de uso** | Bancos calculam modelos de risco conjuntos sem compartilhar dados de clientes |
### Criptografia Homomórfica (HE)
Execute cálculos diretamente em dados criptografados.
| Tipo | O que ele suporta | Despesas gerais |
|------|-----------------|----------|
| **Parcialmente ELE** | Uma operação (adição OU multiplicação) | Baixo |
| **Um pouco ELE** | Número limitado de ambas as operações | Médio |
| **Totalmente ELE** | Cálculos arbitrários | Muito alto (desaceleração de 100-1000x) |
| Aplicação | Descrição |
|------------|------------|
| **Inferência privada** | Execute modelos de ML em dados criptografados; retornar previsões criptografadas |
| **Treinamento criptografado** | Treinar em dados criptografados (ainda principalmente teóricos para aprendizado profundo) |
| **Consultas privadas** | Consultar um banco de dados sem revelar a consulta ou os dados |
### Ambientes de Execução Confiáveis ​​(TEEs)
Isolamento baseado em hardware (Intel SGX, ARM Trustzone) que protege os dados até mesmo do sistema operacional.
| Vantagem | Limitação |
|-----------|------------|
| Desempenho quase nativo | Requer hardware específico |
| Fortes garantias de segurança | Memória limitada (tamanho do enclave) |
| Sem sobrecarga criptográfica | Possíveis ataques de canal lateral |
---

## Regulamentos de privacidade e ML
| Regulamento | Região | Impacto no ML |
|------------|--------|-------------|
| **RGPD** | UE | Direito à explicação; minimização de dados; consentimento para processamento; direito ao apagamento |
| **CCPA** | Califórnia | Direito de saber, excluir e cancelar a venda de dados |
| **HIPAA** | EUA (saúde) | Controles rigorosos sobre dados de saúde; requisitos de desidentificação |
| **PIPL** | China | Localização de dados; requisitos de consentimento; regras de transferência transfronteiriça |
| **Lei de IA** | UE | Requisitos de transparência; classificação de risco; práticas proibidas |
### Impacto nos fluxos de trabalho de ML
| Princípio GDPR | Implicação de ML |
|----------------|---------------|
| **Minimização de dados** | Colete apenas o necessário; aprendizagem federada ajuda |
| **Limitação de finalidade** | Não é possível redirecionar dados sem novo consentimento |
| **Direito ao apagamento** | Deve ser capaz de remover os dados de uma pessoa de um modelo treinado (desaprendizado de máquina) |
| **Direito à explicação** | Os modelos devem ser suficientemente interpretáveis ​​para explicar as previsões individuais |
| **Privacidade desde a concepção** | A privacidade deve ser incorporada aos sistemas desde o início |
---

## Desafios
| Desafio | Descrição |
|-----------|------------|
| **Custo de comunicação** | Enviar atualizações de modelos para milhões de dispositivos é caro |
| **Dados não IID** | Os dispositivos têm distribuições de dados muito diferentes, prejudicando a convergência |
| **Retardatários** | Dispositivos lentos atrasam a rodada inteira |
| **Compensação entre privacidade e utilidade** | Privacidade mais forte significa pior desempenho do modelo |
| **Ataques de envenenamento** | Participantes maliciosos podem corromper o modelo global |
| **Extração de modelo** | Até mesmo atualizações de modelos compartilhados podem vazar informações sobre dados de treinamento |
| **Heterogeneidade de hardware** | Dispositivos diferentes têm capacidades computacionais diferentes |
---

## Ferramentas e Estruturas
| Ferramenta | Finalidade |
|------|---------|
| **Flor** | Estrutura de aprendizagem federada de código aberto; independente de estrutura |
| **TensorFlow Federado** | Estrutura FL do Google para modelos TensorFlow |
| **PySyft** (OpenMined) | ML que preserva a privacidade no PyTorch |
| **DESTINO** (Webank) | Plataforma de aprendizagem federada de nível industrial |
| **FOLHA** | Conjunto de referência para pesquisa de aprendizagem federada |
| **Opaco** (Meta) | Privacidade diferencial para PyTorch |
| **Privacidade TF do Google** | Privacidade diferencial para TensorFlow |
---

## Resumo
As técnicas de aprendizagem federada e de preservação da privacidade abordam uma tensão fundamental: como construir modelos de IA poderosos quando os dados são distribuídos, confidenciais ou regulamentados? O aprendizado federado mantém dados em dispositivos e compartilha apenas atualizações de modelo. A privacidade diferencial acrescenta garantias matemáticas de que as contribuições individuais não podem ser detectadas. A computação segura e a criptografia homomórfica vão além, permitindo a computação em dados criptografados. Cada técnica tem custos – sobrecarga de comunicação, precisão reduzida, despesas computacionais – mas juntas formam um kit de ferramentas para construir uma IA que respeite a privacidade e ao mesmo tempo aprenda com os dados do mundo.