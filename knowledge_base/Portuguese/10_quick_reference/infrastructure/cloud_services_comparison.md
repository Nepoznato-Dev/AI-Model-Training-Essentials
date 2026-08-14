<!--
---
# Metadata
title: "Cloud Services Comparison"
description: "AWS vs Azure vs GCP side-by-side comparison"
category: "Quick Reference"
subcategory: "Infrastructure"
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
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cloud, services, comparison, quick-reference]
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
# Comparação de serviços em nuvem
Uma comparação lado a lado dos três principais provedores de nuvem — AWS, Azure e Google Cloud — em computação, armazenamento, bancos de dados, IA/ML, rede, monitoramento e infraestrutura como código. Útil para arquitetos que decidem qual plataforma usar ou mapeiam serviços de uma nuvem para outra.
---

## Visão geral do provedor
| | AWS | Azul | Google Cloud (GCP) |
|---|-----|-------|---------------------|
| **Participação de mercado** | ~31% (maior) | ~25% (segundo) | ~11% (terceiro, com crescimento mais rápido) |
| **Fortes** | Amplitude de serviços; maturidade; ecossistema | Integração empresarial; nuvem híbrida; Pilha da Microsoft | Dados/IA; Kubernetes; rede global |
| **Melhor para** | Startups para empresas; o mais amplo catálogo de serviços | Empresas com Microsoft/Active Directory; híbrido | Cargas de trabalho com uso intensivo de dados; Nativo do Kubernetes; IA/ML |
| **Regiões** | 33 regiões, 105 AZs | Mais de 60 regiões | Mais de 40 regiões, mais de 100 zonas |
| **Nível gratuito** | 12 meses de nível gratuito + sempre gratuito | 12 meses grátis + crédito de $ 200 | Crédito de $ 300 por 90 dias + sempre grátis |
---

## Computação
| Categoria de serviço | AWS | Azul | GCP |
|-----------------|-----|-------|-----|
| **Máquinas Virtuais** | EC2 (Elastic Compute Cloud) | Máquinas Virtuais | Motor de computação |
| **Escalonamento automático** | Grupos de escalonamento automático | Conjuntos de dimensionamento de máquinas virtuais | Grupos de instâncias |
| **Funções sem servidor** | Lambda | Funções do Azure | Funções de nuvem |
| **Registro de contêiner** | ECR (Registro de Contêineres Elásticos) | Registro de contêiner do Azure | Registro de artefato |
| **Orquestração de contêineres** | ECS / EKS | ACS/AKS | GKE/Cloud Run |
| **Contêineres sem servidor** | Fargate | Aplicativos de contêiner | Corrida na nuvem |
| **Plataforma de aplicativos (PaaS)** | Pé de feijão elástico, App Runner | Serviço de aplicativo | Motor de aplicativos |
| **Processamento em lote** | Lote AWS | Lote do Azure | Lote de nuvem |
| **Computação GPU/IA** | EC2 (instâncias P4d, P5) | VMs da série NC/ND | VMs A2/A3; TPU |
### Modelos de preços de VM
| Modelo | AWS | Azul | GCP |
|-------|-----|-------|-----|
| **Sob demanda** | Instâncias sob demanda | Pagamento conforme o uso | Sob demanda |
| **Reservado/Comprometido** | Instâncias reservadas (1–3 anos) | VMs reservadas (1–3 anos) | Descontos por uso contínuo (1–3 anos) |
| **Ponto / Interrompível** | Instâncias spot | VMs spot | VMs preemptivas/spot |
| **Planos de poupança** | Planos de Poupança | Planos de poupança | Descontos por uso contínuo |
---

## Armazenar
| Categoria de serviço | AWS | Azul | GCP |
|-----------------|-----|-------|-----|
| **Armazenamento de objetos** | S3 | Armazenamento de Blobs | Armazenamento em nuvem |
| **Armazenamento em bloco** | EBS | Discos gerenciados | Disco Permanente |
| **Armazenamento de arquivos** | EFS, FSx | Arquivos do Azure | Armazenamento de arquivos |
| **Arquivo/Frio** | Geleira S3, arquivo profundo | Camadas Blob Cool/Arquivo | Coldline/Arquivo de armazenamento em nuvem |
| **Transferência de dados** | Bola de neve, DataSync | Caixa de dados | Dispositivo de transferência |
### Comparação de classes de armazenamento
| Caso de uso | AWS S3 | Blob Azure | Armazenamento em nuvem GCP |
|----------|--------|------------|--------|
| **Acesso frequente** | Padrão S3 | Quente | Padrão |
| **Acesso pouco frequente** | Padrão S3-IA | Legal | Linha próxima |
| **Acesso raro** | S3 Uma Zona-IA | — | Linha fria |
| **Arquivo** | Geleira S3 / Arquivo Profundo | Arquivo | Arquivo |
---

## Bancos de dados
| Categoria de serviço | AWS | Azul | GCP |
|-----------------|-----|-------|-----|
| **Relacional (gerenciado)** | RDS (MySQL, PostgreSQL, Oracle, SQL Server) | Banco de Dados Azure (MySQL, PostgreSQL); SQL do Azure | Cloud SQL (MySQL, PostgreSQL) |
| **Relacional (nativo da nuvem)** | Aurora (compatível com MySQL/PostgreSQL) | Banco de Dados SQL do Azure (pools elásticos) | Cloud Spanner (distribuído globalmente) |
| **NoSQL (documento)** | DynamoDB | Cosmos DB (API MongoDB, API SQL) | Bombeiro; Armazenamento de dados |
| **NoSQL (coluna larga)** | DynamoDB (também) | Cosmos DB (API Cassandra) | Grande mesa |
| **NoSQL (valor-chave)** | DynamoDB, ElastiCache | Cache do Azure para Redis | Armazenamento de memória (Redis) |
| **Gráfico** | Netuno | Cosmos DB (API Gremlin) | — |
| **Série temporal** | Fluxo de tempo | Explorador de dados do Azure | — |
| **Registro** | QLDB | Razão Confidencial do Azure | — |
| **Cache na memória** | ElastiCache (Redis, Memcached) | Cache do Azure para Redis | Armazenamento de memória |
| **Pesquisar** | Serviço OpenSearch | Pesquisa de IA do Azure | Pesquisa na nuvem; Pesquisa Vertex AI |
| **Armazenamento de dados** | Desvio para o vermelho | Análise de sinapse | BigQuery |
---

## IA e aprendizado de máquina
| Categoria de serviço | AWS | Azul | GCP |
|-----------------|-----|-------|-----|
| **Plataforma de ML** | SageMaker | Aprendizado de Máquina Azure | Vértice AI |
| **APIs pré-treinadas** | Reconhecimento (visão), Polly (TTS), Compreender (PNL), Transcrever | Serviços Cognitivos (Visão, Fala, Linguagem, Decisão) | Vision AI, conversão de fala em texto, API de linguagem natural |
| **LLM / IA generativa** | Bedrock (Claude, Lhama, Titã) | Serviço OpenAI do Azure (GPT-4, DALL-E) | Vertex AI (Gêmeos); Jardim Modelo |
| **Vetor / Embeddings** | OpenSearch (k-NN), Bases de Conhecimento Bedrock | Pesquisa de IA do Azure (vetor) | Pesquisa vetorial Vertex AI, AlloyDB |
| **MLOps** | Pipelines SageMaker, registro de modelo | Pipelines do Azure ML, registro de modelo | Pipelines da Vertex AI, registro de modelo |
| **Rotulagem de dados** | Verdade fundamental do SageMaker | Rotulagem de dados do Azure ML | Rotulagem de dados da Vertex AI |
| **IA conversacional** | Lex | Serviço de bot do Azure | Fluxo de diálogo CX/ES |
| **Tradução** | Traduzir | Tradutor | API de tradução |
---

## Rede
| Categoria de serviço | AWS | Azul | GCP |
|-----------------|-----|-------|-----|
| **Rede Virtual** | VPC | Rede Virtual (VNet) | VPC |
| **Balanceamento de carga** | ELB/ALB/NLB/CLB | Balanceador de carga (aplicativo, rede, gateway) | Balanceamento de carga em nuvem |
| **DNS** | Rota 53 | DNS do Azure | DNS em nuvem |
| **CDN** | CloudFront | Porta frontal Azure | CDN em nuvem |
| **Gateway de API** | Gateway de API | Gerenciamento de APIs | Gateway de API |
| **VPN** | VPN site a site, VPN cliente | Gateway VPN | VPN na nuvem |
| **Conexão direta/ExpressRoute** | Conexão direta | Rota Expressa | Interconexão em nuvem |
| **Link privado** | PrivateLink, endpoints VPC | Link privado, endpoints privados | Conexão de serviço privado |
| **Firewall** | WAF, firewall de rede | Firewall do Azure, WAF | Armadura de nuvem, firewall |
| **Proteção DDoS** | Escudo Padrão/Avançado | Proteção DDoS | Armadura de Nuvem |
---

## Monitoramento e registro
| Categoria de serviço | AWS | Azul | GCP |
|-----------------|-----|-------|-----|
| **Métricas/Monitoramento** | CloudWatch | Monitor Azure | Monitoramento de nuvem (Stackdriver) |
| **Registro** | Registros do CloudWatch | Log Analytics (registros do Monitor do Azure) | Registro em nuvem |
| **Rastreamento** | Raio X | Informações sobre aplicativos | Rastreamento de nuvem |
| **Alerta** | Alarmes CloudWatch | Alertas do Monitor Azure | Alertas de monitoramento de nuvem |
| **Painéis** | Painéis CloudWatch | Pastas de trabalho/painéis do Azure | Painéis de monitoramento de nuvem |
| **Rastreamento de erros** | Sintéticos CloudWatch | Informações sobre aplicativos | Relatório de erros na nuvem |
| **Terceiros** | Datadog, Nova Relíquia, PagerDuty | Datadog, Nova Relíquia, PagerDuty | Datadog, Nova Relíquia, PagerDuty |
---

## Infraestrutura como código e DevOps
| Categoria de serviço | AWS | Azul | GCP |
|-----------------|-----|-------|-----|
| **IaC (nativo)** | Formação em nuvem | Modelos ARM / Bíceps | Gerente de Implantação / Pulumi |
| **IaC (entre nuvens)** | Terraform, Pulumi, CDK | Terraform, Pulumi, Bíceps | Terraform, Pulumi |
| **CI/CD** | CodePipeline, CodeBuild | Azure DevOps, ações do GitHub | Construção em nuvem; Implantação na nuvem |
| **Registro de contêiner** | ECR | Registro de contêiner do Azure | Registro de artefato |
| **GitOps** | App Mesh + Flux/ArgoCD | Flux/ArgoCD no AKS | Sincronização de configuração (Anthos) |
| **Gerenciamento de segredos** | Gerenciador de segredos, armazenamento de parâmetros SSM | Cofre de chaves | Gerenciador de segredos |
---

## Considerações sobre preços
| Fator | AWS | Azul | GCP |
|--------|-----|-------|-----|
| **Granularidade de faturamento** | Por segundo (após a primeira hora para alguns) | Por segundo | Por segundo |
| **Descontos por uso prolongado** | Instâncias Reservadas / Planos Poupança | VMs reservadas | Descontos por uso contínuo |
| **Instâncias pontuais** | Até 90% de desconto | Até 90% de desconto | Até 91% de desconto |
| **Saída de dados** | Cobrado (caro) | Cobrado | Mesmo preço independentemente do destino (muitas vezes mais barato) |
| **Nível gratuito** | 12 meses + sempre grátis | 12 meses + crédito de $ 200 | $ 300 por 90 dias + sempre grátis |
| **Descontos empresariais** | Programa de Desconto Empresarial (EDP) | MACC (Contrato de Compromisso Monetário) | Utilização comprometida + CUDs |
---

## Quando usar qual
| Cenário | Recomendado | Por que |
|----------|-------------|-----|
| **Mais ampla seleção de serviços; ecossistema maduro** | AWS | Maior catálogo; a maioria das integrações de terceiros |
| **Empresa Microsoft; Diretório Ativo; híbrido** | Azul | Integração nativa do AD; ferramentas híbridas fortes |
| **Armazenamento de dados; BigQuery; análise pesada** | GCP | O BigQuery é o melhor da categoria; integração perfeita de dados |
| **Desenvolvimento nativo do Kubernetes** | GCP | GKE é o Kubernetes gerenciado mais sofisticado |
| **Aplicações generativas de IA/LLM** | Azure ou GCP | Azure OpenAI para modelos GPT; Vertex AI para Gêmeos |
| **Aplicativos em escala global e baixa latência** | GCP | A rede global do Google é uma vantagem genuína |
| **Cargas de trabalho com alto nível de conformidade/governamental** | AWS ou Azure | A maioria das certificações de conformidade; Regiões GovCloud |
| **Startups sensíveis ao custo** | GCP ou AWS | O nível gratuito do GCP é generoso; AWS tem créditos iniciais |
| **Pilha Microsoft/.NET existente** | Azul | Forte integração com Visual Studio, .NET, Office 365 |
| **Estratégia multinuvem** | Terraform + todos os três | Use o Terraform para gerenciar recursos em nuvens |
---

## Resumo
Todas as três nuvens são capazes, confiáveis ​​e estão em constante expansão. A escolha geralmente se resume a: o que sua equipe já sabe, como são os contratos existentes e quais serviços específicos são importantes para sua carga de trabalho. A multinuvem é cada vez mais comum – use Terraform ou Pulumi para evitar o aprisionamento do fornecedor na camada de infraestrutura e escolha cada nuvem pelo que ela faz de melhor.