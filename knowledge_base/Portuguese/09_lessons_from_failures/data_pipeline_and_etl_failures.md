<!--
---
# Metadata
title: "Data Pipeline and ETL Failures"
description: "Schema drift, duplicate data, validation gaps, pipeline monitoring"
category: "Lessons from Failures"
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

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, pipeline, etl, failures, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Pipeline de dados e falhas de ETL
Os pipelines de dados são o encanamento das organizações modernas: eles movem dados dos sistemas de origem por meio de transformações para bancos de dados, armazéns e lagos, onde são usados ​​para análises, aprendizado de máquina e tomada de decisões. Quando eles trabalham, ninguém percebe. Quando falham, as decisões são tomadas com base em dados obsoletos, os modelos são treinados com base no lixo, os relatórios mostram números impossíveis e a confiança em toda a plataforma de dados diminui. As falhas no pipeline de dados estão entre as falhas mais comuns e mais caras nas organizações de tecnologia.
---

## Modos de falha comuns
### Problemas de qualidade de dados
| Falha | Descrição | Impacto | Dificuldade de detecção |
|---------|-------------|--------|---------------------|
| **Corrupção silenciosa de dados** | Os dados são modificados incorretamente sem que nenhum erro seja gerado | Os sistemas downstream confiam em dados incorretos; decisões baseadas em informações falsas | Muito difícil — sem sinal de erro |
| **Desvio de esquema** | O sistema de origem altera o esquema (adiciona, remove, renomeia colunas) | Pipeline quebra ou descarta dados silenciosamente | Médio — o pipeline pode falhar ou produzir resultados parciais |
| **Incompatibilidade de tipo de dados** | Fonte envia string onde o inteiro é esperado; mudanças de precisão flutuante | O pipeline falha; dados truncados; erros de arredondamento | Médio — pode causar erros no pipeline ou problemas sutis de dados |
| **Registros duplicados** | O mesmo evento foi processado diversas vezes | Contagens inflacionadas; agregações incorretas | Difícil — cada registro parece válido individualmente |
| **Valores nulos/ausentes** | Os campos esperados estão vazios | Os cálculos falham; modelos produzem previsões erradas | Médio — depende do tratamento nulo |
| **Valores fora do intervalo** | Valores fora dos limites esperados (idades negativas; datas futuras) | Estatísticas distorcidas; lógica de negócios quebrada | Médio — requer regras de validação |
| **Dados atrasados** | Os dados chegam após o fechamento da janela de processamento | Resultados incompletos; registros perdidos | Difícil — os resultados parecem completos, mas não são |
### Problemas de infraestrutura de pipeline
| Falha | Descrição | Impacto |
|--------|-------------|--------|
| **Falha na orquestração** | Agendador (Airflow, Prefect) não aciona o pipeline | Os dados estão obsoletos; nenhum processamento ocorre |
| **Esgotamento de recursos** | Pipeline fica sem memória, CPU ou disco | Falhas no pipeline; resultados parciais |
| **Falha de dependência** | O sistema upstream está inoperante ou lento | Pipeline espera indefinidamente ou falha |
| **Problemas de simultaneidade** | Vários pipelines modificam os mesmos dados simultaneamente | Condições de corrida; corrupção de dados |
| **Desvio de configuração** | Mudanças no ambiente (rede, credenciais, endpoints) não refletidas no pipeline | Pipeline falha inesperadamente |
| **Contrapressão** | Os dados chegam mais rápido do que o pipeline pode processar | Filas crescentes; aumentando a latência |
---

## Estudos de caso
### Estudo de caso 1: Duplicação silenciosa de dados
| Aspecto | Descrição |
|--------|------------|
| **Cenário** | O pipeline de pedidos de uma empresa de comércio eletrônico processa eventos de uma fila de mensagens |
| **O que deu errado** | A reinicialização do consumidor fez com que as mensagens fossem consumidas novamente; não existia lógica de desduplicação |
| **Impacto** | Os números da receita foram inflacionados em 15% durante 3 semanas antes que alguém percebesse |
| **Causa raiz** | Sem chaves de idempotência; entrega pelo menos uma vez sem desduplicação |
| **Corrigir** | Adicionadas chaves de idempotência com base no ID do pedido; implementou semântica exatamente uma vez |
| **Lição** | A entrega pelo menos uma vez requer desduplicação; sempre valide os totais em relação aos sistemas de origem |
### Estudo de caso 2: Mudança de esquema quebra downstream
| Aspecto | Descrição |
|--------|------------|
| **Cenário** | Um provedor de pagamento altera o nome de um campo em sua resposta da API |
| **O que deu errado** | O pipeline ETL começou silenciosamente a gravar valores nulos; nenhuma validação de esquema |
| **Impacto** | Os relatórios financeiros mostraram receita zero desse método de pagamento por 2 meses |
| **Causa raiz** | Nenhuma validação de esquema na ingestão; valores nulos tratados como válidos |
| **Corrigir** | Adicionada validação de esquema com alertas; campos obrigatórios aplicados; verificações nulas |
| **Lição** | Nunca confie em esquemas externos para permanecerem estáveis; validar na fronteira |
### Estudo de caso 3: Catástrofe de fuso horário
| Aspecto | Descrição |
|--------|------------|
| **Cenário** | Uma empresa global agrega métricas diárias em todos os escritórios |
| **O que deu errado** | Algumas fontes usaram UTC, outras usaram a hora local; pipeline não normalizou |
| **Impacto** | Os totais diários não correspondiam; algumas transações foram contabilizadas em dia errado; o fechamento do mês estava errado |
| **Causa raiz** | Nenhuma política padrão de fuso horário; carimbos de data e hora armazenados de forma inconsistente |
| **Corrigir** | Todos os carimbos de data/hora armazenados como UTC; conversão para hora local apenas na camada de apresentação |
| **Lição** | Padronize o UTC em todos os lugares; seja explícito sobre fusos horários em todas as fronteiras |
---

## Estratégias de Prevenção
### Validação de dados
| Estratégia | Descrição | Exemplos de ferramentas |
|----------|-------------|---------------|
| **Validação de esquema** | Verifique se os dados correspondem ao esquema esperado em cada estágio | Grandes Expectativas; Deequ; Refrigerante |
| **Verificações de alcance** | Os valores ficam dentro dos limites esperados | Asserções personalizadas; testes dbt |
| **Verificações de frescor** | Os dados são suficientemente recentes para serem úteis | Monitoramento de carimbos de data/hora; Alertas de SLA |
| **Verificações de volume** | A contagem de linhas está dentro do intervalo esperado | Detecção de anomalias em contagens de linhas |
| **Integridade referencial** | Correspondência de chaves estrangeiras; nenhum registro órfão | Restrições SQL; ferramentas de qualidade de dados |
| **Reconciliação entre fontes** | Correspondência de totais entre origem e destino | Trabalhos de reconciliação automatizados |
### Padrões de projeto de pipeline
| Padrão | Descrição | Benefício |
|---------|-------------|---------|
| **Idempotência** | Executar o pipeline várias vezes produz o mesmo resultado | É seguro tentar novamente; sem duplicatas |
| **Atomicidade** | O pipeline é totalmente bem-sucedido ou falha totalmente (sem estado parcial) | Não há dados parcialmente processados ​​|
| **Ponto de verificação** | Salve o progresso em cada etapa; retomar do último ponto de verificação | Tolerância a falhas; sem reprocessamento |
| **Filas de mensagens mortas** | Registros com falha vão para uma fila separada para investigação | Sem perda de dados; pode investigar e reproduzir |
| **Disjuntores** | Interromper o processamento quando o downstream estiver falhando | Evitar falhas em cascata |
| **Contratos de dados** | Acordo entre produtores e consumidores sobre formato de dados | As alterações de esquema são coordenadas |
### Monitoramento e alertas
| O que monitorar | Por que | Como |
|-----------------|-----|-----|
| **Duração do pipeline** | Aumento da duração sinaliza problemas | Análise de tendências; Acompanhamento de SLA |
| **Contagem de linhas** | Mudanças repentinas indicam problemas | Compare com médias históricas |
| **Taxas nulas** | Aumentando o esquema do sinal nulo ou problemas de origem | Rastreamento nulo em nível de coluna |
| **Atualidade dos dados** | Dados desatualizados significam que o pipeline não está em execução | Carimbo de data/hora do último registro |
| **Impacto a jusante** | Os relatórios e modelos estão usando dados corretos? | Linhagem de dados ponta a ponta |
| **Uso de recursos** | CPU; memória; disco; rede | Monitorização de infraestruturas |
---

## Estratégias de recuperação
| Situação | Estratégia |
|-----------|----------|
| **Dados inválidos já no armazém** | Identifique o intervalo de tempo afetado; reprocessar da fonte; notificar os consumidores a jusante |
| **Falha no pipeline no meio da execução** | O design idempotente permite uma nova execução segura; checkpointing permite currículo |
| **A mudança de esquema quebrou o pipeline** | Corrigir transformação; preencher os dados afetados; adicionar manipulação de evolução de esquema |
| **Corrupção silenciosa descoberta tardiamente** | Análise de causa raiz; determinar o raio da explosão; reprocessar; adiciona monitoramento para detectar recorrência |
| **Perda de dados** | Restaurar do backup; reproduzir da fonte; avaliar se a perda é recuperável |
---

## Resumo
As falhas no pipeline de dados são onipresentes e muitas vezes mais caras do que as interrupções de aplicativos porque produzem respostas erradas em vez de erros óbvios. Corrupção silenciosa de dados, desvio de esquema, duplicatas, erros de fuso horário e valores ausentes são os culpados mais comuns. As principais estratégias de prevenção são: validar dados em todos os limites (esquema, intervalo, volume, atualização); projetar pipelines para serem idempotentes e atômicos; monitorar tudo (duração, contagem de linhas, taxas nulas, atualização); use filas de mensagens mortas para registros com falha; e estabelecer contratos de dados entre produtores e consumidores. Quando ocorrem falhas, a resposta deve incluir a análise da causa raiz, o reprocessamento dos dados afetados, a notificação dos consumidores a jusante e, de forma crítica, a adição de monitoramento para detectar a mesma classe de falha no futuro. As organizações que acertam tratam os pipelines de dados com o mesmo rigor que o software de produção: testes, monitoramento, alertas, resposta a incidentes e post-mortems.