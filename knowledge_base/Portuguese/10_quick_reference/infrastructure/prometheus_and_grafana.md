---
# Metadata
title: "Prometheus and Grafana"
description: "PromQL, exporters, dashboards, alerting, monitoring stack"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [prometheus, grafana, quick-reference]
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

# Prometeu e Grafana
Prometheus é um kit de ferramentas de monitoramento e alerta de código aberto projetado para oferecer confiabilidade e escalabilidade. Grafana é a plataforma de código aberto líder para visualização de dados de séries temporais. Juntos, eles formam a pilha de monitoramento mais popular para infraestrutura e aplicativos modernos. O Prometheus coleta e armazena métricas; Grafana os exibe em painéis.
---

## Arquitetura Prometheus
| Componente | Descrição |
|-----------|------------|
| **Servidor Prometheus** | Extrai métricas de metas; armazena dados de série temporal; avalia regras de alerta |
| **Exportador** | Expõe métricas de um sistema (Node Exporter, cAdvisor, etc.) |
| **Pushgateway** | Recebe métricas de trabalhos de curta duração (trabalhos em lote, CI) |
| **Gerenciador de alertas** | Lida com alertas: agrupamento, silenciamento, roteamento, inibição |
| **Descoberta de serviço** | Descobre alvos automaticamente (Kubernetes, Consul, EC2, etc.) |
---

## Conceitos-chave
| Conceito | Descrição |
|--------|-------------|
| **Métrica** | Uma medida nomeada com rótulos opcionais e um valor |
| **Série temporal** | Um fluxo de pontos de dados para uma combinação específica de métrica + rótulo |
| **Trabalho** | Uma coleção de alvos com o mesmo propósito |
| **Instância** | Um único alvo para raspar (geralmente um processo) |
| **Raspe** | Prometheus extraindo métricas de um alvo em intervalos regulares |
| **Etiqueta** | Um par de valores-chave que dimensiona uma métrica (por exemplo,`method="GET"`) |
| **Amostra** | Um valor em um determinado momento: (timestamp, valor) |
---

## Tipos de métricas
| Tipo | Descrição | Caso de uso |
|------|-------------|----------|
| **Contador** | Valor crescente monotonicamente (só sobe) | Contagem de solicitações; erros; tarefas concluídas |
| **Medidor** | Valor que pode subir ou descer | Temperatura; uso de memória; comprimento da fila |
| **Histograma** | Observações agrupadas por valor | Latência de solicitação; tamanho da resposta |
| **Resumo** | Semelhante ao histograma; calcula quantis do lado do cliente | Percentis de latência |
---

## PromQL (linguagem de consulta)
### Consultas básicas
| Consulta | Descrição |
|-------|------------|
| `http_requests_total`| Séries temporais brutas |
| `http_requests_total{method="GET"}`| Filtrar por rótulo |
| `http_requests_total{method="GET", status="200"}`| Vários filtros de rótulos |
| `rate(http_requests_total[5m])`| Taxa por segundo durante 5 minutos |
| `increase(http_requests_total[1h])`| Aumento total em 1 hora |
| `sum(rate(http_requests_total[5m])) by (status)`| Taxa agregada por status |
| `histogram_quantile(0.95, rate(http_duration_bucket[5m]))`| Latência do percentil 95 |
| `avg(node_cpu_seconds_total{mode="idle"})`| Média de CPU ociosa |
| `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))`| Utilização da CPU |
### Funções Comuns
| Função | Descrição | Exemplo |
|----------|------------|---------|
| `rate()`| Taxa média de aumento por segundo | `rate(requests_total[5m])`|
| `irate()`| Taxa por segundo baseada nos dois últimos pontos de dados | `irate(requests_total[1m])`|
| `increase()`| Aumento total ao longo do intervalo de tempo | `increase(errors_total[1h])`|
| `sum()`| Soma das séries | `sum(rate(requests_total[5m])) by (service)`|
| `avg()`| Média entre séries | `avg(node_memory_usage)`|
| `histogram_quantile()`| Calcular quantil a partir do histograma | `histogram_quantile(0.99, rate(duration_bucket[5m]))`|
| `topk()`| Principais séries K por valor | `topk(5, rate(requests_total[5m]))`|
| `predict_linear()`| Previsão linear | `predict_linear(disk_usage[1h], 4*3600)`|
| `absent()`| Verifique se a métrica está faltando | `absent(up{job="myapp"})`|
---

## Exportadores Comuns
| Exportador | O que monitora |
|----------|-----------------|
| **Exportador de nós** | Métricas de host Linux/Unix (CPU, memória, disco, rede) |
| **cConselheiro** | Métricas de contêiner (CPU, memória, rede, sistema de arquivos) |
| **Exportador MySQL** | Métricas de banco de dados MySQL |
| **Exportador PostgreSQL** | Métricas do banco de dados PostgreSQL |
| **Exportador Redis** | Métricas Redis |
| **Exportador de caixa preta** | Sondar endpoints sobre HTTP, HTTPS, DNS, TCP, ICMP |
| **Exportador SNMP** | Métricas de dispositivos de rede via SNMP |
| **Exportador JSON** | Métricas personalizadas de APIs JSON |
---

##Grafana
### Conceitos-chave
| Conceito | Descrição |
|--------|-------------|
| **Fonte de dados** | Conexão com Prometheus (ou outros backends) |
| **Painel** | Coleção de painéis dispostos em layout |
| **Painel** | Visualização única (gráfico, medidor, tabela, mapa de calor) |
| **Variável** | Filtro dinâmico para dashboards (por exemplo, selecionar instância) |
| **Anotação** | Marcar eventos em gráficos (implantações, incidentes) |
| **Regra de alerta** | Alertas baseados em limites no Grafana |
| **Modelagem** | Padrões de painel reutilizáveis ​​com variáveis ​​|
### Padrões úteis de painel
| Padrão | Descrição |
|--------|-------------|
| **Linha de visão geral** | Visão geral das principais métricas: taxa de erro, latência, taxa de transferência |
| **Detalhamento** | Clique do resumo para a visualização detalhada usando variáveis ​​|
| **Método VERMELHO** | Taxa, Erros, Duração — as três principais métricas de serviço |
| **USE método** | Utilização, Saturação, Erros — para infra-estruturas |
| **Sinais dourados** | Latência, tráfego, erros, saturação (livro SRE do Google) |
---

## Alerta
### Estrutura de regras de alerta
```yaml
groups:
  - name: example
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate on {{ $labels.instance }}"
          description: "Error rate is {{ $value | humanizePercentage }}"
```

### Roteamento do Alertmanager
| Conceito | Descrição |
|--------|-------------|
| **Grupo** | Combine alertas semelhantes em uma notificação |
| **Rota** | Árvore de matchers que determina para onde vão os alertas |
| **Receptor** | Para onde enviar alertas (e-mail, Slack, PagerDuty, webhook) |
| **Inibir** | Suprimir alertas quando outro alerta for disparado |
| **Silêncio** | Silenciar temporariamente alertas por marcador de correspondência |
---

## Solução de problemas
| Problema | Solução |
|--------|----------|
| **Meta reduzida** | Verifique se o exportador está em execução; verifique rede/firewall; verifique a configuração do scrape |
| **Sem dados** | Verifique a ortografia do nome da métrica; verifique filtros de rótulos; verificar intervalo de tempo |
| **Alta cardinalidade** | Muitas combinações de rótulos; reduzir os valores dos rótulos; usar regras de gravação |
| **Consultas lentas** | Utilize regras de gravação para consultas complexas; aumentar o intervalo de raspagem |
| **Fadiga de alerta** | Ajustar limites; adicione duração `for`; alertas relacionados ao grupo |
| **Métricas ausentes após reinicialização** | O Prometheus armazena dados localmente; verifique as configurações de retenção |
---

## Resumo
O Prometheus monitora os sistemas coletando métricas dos exportadores em intervalos regulares. As métricas vêm em quatro tipos: contadores (somente para cima), medidores (para cima e para baixo), histogramas (observações agrupadas) e resumos (quantis). PromQL é a linguagem de consulta –`rate()`,`increase()`,`histogram_quantile()`e funções de agregação (`sum`,`avg`) são as operações mais comuns. Grafana visualiza dados do Prometheus em painéis com painéis, variáveis ​​e anotações. O Alerting usa o Alertmanager para agrupar, rotear, silenciar e inibir alertas. Os principais padrões de monitoramento são os sinais dourados do Google (latência, tráfego, erros, saturação) e o método RED (taxa, erros, duração) para serviços e o método USE (utilização, saturação, erros) para infraestrutura.