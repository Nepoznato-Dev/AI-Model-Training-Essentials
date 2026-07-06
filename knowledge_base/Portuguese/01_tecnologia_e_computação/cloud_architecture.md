# Arquitetura de Nuvem

## Fundamentos de Computação em Nuvem

### O que é Computação em Nuvem?
Entrega sob demanda de recursos de computação (servidores, armazenamento, bancos de dados, redes, software) pela internet com cobrança conforme o uso (pay-as-you-go).

### Características Essenciais (Definição do NIST)
- **Autoatendimento sob Demanda**: Provisione recursos sem interação humana
- **Amplo Acesso à Rede**: Disponível pela rede por meio de mecanismos padrão
- **Agrupamento de Recursos**: Modelo multi-tenant com atribuição dinâmica
- **Elasticidade Rápida**: Escale para mais e para menos rapidamente
- **Serviço Medido**: Uso de recursos monitorado e cobrado

### Modelos de Implantação em Nuvem
- **Nuvem Pública**: De propriedade dos provedores, infraestrutura compartilhada (AWS, Azure, GCP)
- **Nuvem Privada**: Dedicada a uma única organização (on-premises ou hospedada)
- **Nuvem Híbrida**: Combinação de nuvens públicas e privadas
- **Multi-Cloud**: Uso de múltiplos provedores de nuvem pública
- **Nuvem Comunitária**: Compartilhada por organizações com preocupações em comum

### Modelos de Serviço

#### Infraestrutura como Serviço (IaaS)
- **Fornece**: Máquinas virtuais, armazenamento, redes, sistemas operacionais
- **Exemplos**: AWS EC2, Google Compute Engine, Azure VMs
- **Casos de Uso**: Migrações lift-and-shift, ambientes de desenvolvimento, necessidades de alto controle

#### Plataforma como Serviço (PaaS)
- **Fornece**: Plataformas de desenvolvimento, bancos de dados, middleware
- **Exemplos**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **Casos de Uso**: Desenvolvimento de aplicações, implantação de APIs, microsserviços

#### Software como Serviço (SaaS)
- **Fornece**: Aplicações completas pela internet
- **Exemplos**: Salesforce, Google Workspace, Microsoft 365, Slack
- **Casos de Uso**: E-mail, CRM, colaboração, aplicações de negócios

#### Função como Serviço (FaaS) / Serverless
- **Fornece**: Execução de funções orientada a eventos
- **Exemplos**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Casos de Uso**: Processamento de eventos, APIs, tarefas agendadas, processamento em tempo real

## Principais Provedores de Nuvem

### Amazon Web Services (AWS)
- **Participação de Mercado**: ~32% (maior provedor)
- **Serviços Principais**:
  - Computação: EC2, Lambda, ECS, EKS
  - Armazenamento: S3, EBS, Glacier
  - Banco de Dados: RDS, DynamoDB, Aurora
  - Redes: VPC, Route 53, CloudFront
  - IA/ML: SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **Participação de Mercado**: ~23%
- **Pontos Fortes**: Integração corporativa, nuvem híbrida, ecossistema Microsoft
- **Serviços Principais**:
  - Computação: Virtual Machines, Azure Functions, AKS
  - Armazenamento: Blob Storage, Disk Storage
  - Banco de Dados: SQL Database, Cosmos DB
  - Redes: Virtual Network, Traffic Manager
  - IA/ML: Azure ML, Cognitive Services

### Google Cloud Platform (GCP)
- **Participação de Mercado**: ~10%
- **Pontos Fortes**: Análise de dados, IA/ML, Kubernetes
- **Serviços Principais**:
  - Computação: Compute Engine, Cloud Functions, GKE
  - Armazenamento: Cloud Storage, Persistent Disk
  - Banco de Dados: Cloud SQL, Firestore, Bigtable
  - Analytics: BigQuery, Dataflow, Pub/Sub
  - IA/ML: Vertex AI, AutoML

### Outros Provedores
- **IBM Cloud**: Foco corporativo, Watson AI
- **Oracle Cloud**: Cargas de trabalho de banco de dados, aplicações corporativas
- **Alibaba Cloud**: Dominante na Ásia-Pacífico
- **DigitalOcean**: Amigável para desenvolvedores, ofertas simplificadas

## Padrões de Arquitetura de Nuvem

### Princípios do Well-Architected Framework

#### Excelência Operacional
- Automatize operações
- Faça mudanças frequentes e reversíveis
- Refine os procedimentos continuamente
- Antecipe falhas

#### Segurança
- Implemente uma base sólida de identidade
- Habilite a rastreabilidade
- Aplique segurança em todas as camadas
- Automatize as melhores práticas de segurança
- Proteja os dados em trânsito e em repouso

#### Confiabilidade
- Teste os procedimentos de recuperação
- Recupere-se automaticamente de falhas
- Escale horizontalmente para disponibilidade
- Pare de estimar capacidade por suposição
- Gerencie mudanças com automação

#### Eficiência de Desempenho
- Democratize tecnologias avançadas
- Torne-se global em minutos
- Use arquiteturas serverless
- Experimente com mais frequência
- Considere a afinidade mecânica (mechanical sympathy)

#### Otimização de Custos
- Adote o modelo de consumo
- Meça a eficiência geral
- Pare de gastar dinheiro com trabalho sem diferenciação
- Analise e atribua os gastos
- Use serviços gerenciados

### Padrões Comuns de Arquitetura

#### Arquitetura de Microsserviços
- Decomponha as aplicações em serviços pequenos e independentes
- Cada serviço é dono de seus dados e de sua lógica
- Comunicam-se via APIs (REST, gRPC, mensageria)
- Implante de forma independente
- **Benefícios**: Escalabilidade, isolamento de falhas, diversidade tecnológica
- **Desafios**: Complexidade distribuída, consistência de dados, monitoramento

#### Arquitetura Orientada a Eventos
- Componentes se comunicam por meio de eventos
- Produtores emitem eventos, consumidores reagem
- **Padrões**: Event sourcing, CQRS, pub/sub
- **Tecnologias**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Benefícios**: Baixo acoplamento, escalabilidade, processamento em tempo real

#### Arquitetura Serverless
- Nenhum gerenciamento de servidor necessário
- Pague por execução
- Escalonamento automático
- **Componentes**: Funções, API Gateway, serviços gerenciados
- **Benefícios**: Eficiência de custos, menos operações, implantação rápida
- **Considerações**: Cold starts, vendor lock-in, limites de execução

#### Arquitetura em Camadas (N-Tier)
- Camada de apresentação (UI)
- Camada de lógica de aplicação/negócios
- Camada de acesso a dados
- Camada de banco de dados
- **Benefícios**: Separação de responsabilidades, manutenibilidade
- **Comum**: Aplicações web de 3 camadas

#### Arquitetura Baseada em Espaço (Space-Based)
- Lide com alta concorrência com dados distribuídos
- Memória virtualizada entre servidores
- Nós de processamento escalam de forma independente
- **Casos de Uso**: Aplicações de alto volume e baixa latência

## Serviços de Computação

### Máquinas Virtuais
- **Tipos**: Propósito geral, otimizada para computação, otimizada para memória, GPU
- **Preços**: On-demand, instâncias reservadas, instâncias spot
- **Gerenciamento**: Grupos de auto scaling, balanceadores de carga
- **Melhores Práticas**: Right-sizing, tagging, monitoramento, aplicação de patches

### Contêineres
- **Docker**: Padrão de runtime de contêineres
- **Orquestração**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Benefícios**: Portabilidade, eficiência, consistência
- **Registry**: ECR, GCR, ACR, Docker Hub

### Funções Serverless
- **Modelo de Execução**: Acionadas por eventos, sem estado (stateless)
- **Limites**: Tempo de execução, memória, execuções concorrentes
- **Casos de Uso**: APIs, processamento de arquivos, jobs agendados, backends de IoT
- **Monitoramento**: Contagem de invocações, erros, duração, cold starts

## Soluções de Armazenamento

### Armazenamento de Objetos
- **Características**: Estrutura plana, metadados, acesso via HTTP
- **Exemplos**: AWS S3, Google Cloud Storage, Azure Blob
- **Casos de Uso**: Ativos estáticos, backups, data lakes, arquivos
- **Classes de Armazenamento**: Hot, cool, cold, archive (custo/acesso variáveis)

### Armazenamento de Blocos
- **Características**: Volumes brutos, anexados a VMs
- **Exemplos**: AWS EBS, Google Persistent Disk, Azure Disks
- **Casos de Uso**: Bancos de dados, volumes de boot, necessidades de alto desempenho
- **Tipos**: SSD, HDD, IOPS provisionadas

### Armazenamento de Arquivos
- **Características**: Sistemas de arquivos compartilhados, protocolos NFS/SMB
- **Exemplos**: AWS EFS, Google Filestore, Azure Files
- **Casos de Uso**: Gestão de conteúdo, configurações compartilhadas, lift-and-shift

### Armazenamento de Arquivamento (Archive)
- **Características**: Custo mais baixo, atrasos na recuperação
- **Exemplos**: S3 Glacier, Azure Archive Storage
- **Casos de Uso**: Conformidade, backups de longo prazo, dados históricos

## Serviços de Banco de Dados

### Bancos de Dados Relacionais Gerenciados
- **Serviços**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL Database
- **Recursos**: Backups automatizados, patching, escalonamento, replicação
- **Engines**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### Bancos de Dados NoSQL
- **Documento**: DocumentDB, Firestore, Cosmos DB
- **Chave-Valor**: DynamoDB, Redis Cache
- **Wide-Column**: Bigtable, Cassandra (gerenciado)
- **Grafo**: Neptune, Cosmos DB (API de grafo)

### Data Warehousing
- **Serviços**: Snowflake, Redshift, BigQuery, Synapse
- **Características**: Armazenamento colunar, arquitetura MPP
- **Casos de Uso**: Analytics, BI, análise de dados em larga escala

### Serviços de Cache
- **Em Memória**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **Cache de CDN**: CloudFront, Cloud CDN, Azure CDN
- **Casos de Uso**: Armazenamento de sessão, cache de consultas, entrega de conteúdo

## Redes

### Redes Virtuais
- **VPC/VNet**: Ambientes de rede isolados
- **Sub-redes**: Públicas (voltadas para a internet), privadas (apenas internas)
- **Endereçamento IP**: Blocos CIDR, IPv4/IPv6
- **Tabelas de Rotas**: Controlam o fluxo de tráfego

### Balanceamento de Carga
- **Tipos**: Application (L7), Network (L4), Gateway
- **Recursos**: Health checks, terminação SSL, sticky sessions
- **Serviços**: ELB/ALB/NLB, Cloud Load Balancing, Azure Load Balancer

### Redes de Distribuição de Conteúdo (CDN)
- **Objetivo**: Armazenar conteúdo em cache em edge locations
- **Benefícios**: Menor latência, menor carga na origem, distribuição global
- **Serviços**: CloudFront, Cloud CDN, Azure CDN, Akamai

### Serviços de DNS
- **Funções**: Registro de domínios, roteamento, health checks
- **Serviços**: Route 53, Cloud DNS, Azure DNS
- **Políticas de Roteamento**: Simples, ponderado, baseado em latência, geolocalização, failover

### Opções de Conectividade
- **Internet Gateway**: Acesso à internet pública
- **NAT Gateway**: Acesso de saída de sub-redes privadas
- **VPN**: Túneis criptografados para o ambiente on-premises
- **Direct Connect/ExpressRoute**: Conexões privadas dedicadas
- **VPC Peering**: Conecte VPCs dentro de/entre contas

## Segurança na Nuvem

### Modelo de Responsabilidade Compartilhada
- **Responsabilidade do Provedor**: Segurança DA nuvem (infraestrutura)
- **Responsabilidade do Cliente**: Segurança NA nuvem (dados, aplicações, acesso)
- **Varia por Serviço**: Mais gerenciado = mais responsabilidade do provedor

### Gerenciamento de Identidade e Acesso (IAM)
- **Usuários**: Identidades individuais
- **Grupos**: Coleções de usuários
- **Funções (Roles)**: Credenciais temporárias para serviços/usuários
- **Políticas**: Documentos JSON que definem permissões
- **Princípios**: Menor privilégio, segregação de funções

### Segurança de Rede
- **Security Groups**: Firewalls com estado (stateful) para instâncias
- **Network ACLs**: Firewalls sem estado (stateless) para sub-redes
- **Web Application Firewall (WAF)**: Proteção contra exploits web
- **Proteção contra DDoS**: Shield, Cloud Armor, DDoS Protection

### Proteção de Dados
- **Criptografia em Repouso**: KMS, chaves gerenciadas pelo cliente
- **Criptografia em Trânsito**: TLS/SSL, HTTPS
- **Gerenciamento de Chaves**: HSM, rotação de chaves, trilhas de auditoria
- **Gerenciamento de Segredos**: Secrets Manager, Key Vault

### Conformidade e Governança
- **Certificações**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Ferramentas**: Aplicação de políticas, relatórios de conformidade, logs de auditoria
- **Frameworks**: Cloud Security Alliance, NIST CSF

## DevOps na Nuvem

### Serviços de CI/CD
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Terceiros**: Jenkins, CircleCI, GitLab CI

### Infraestrutura como Código (IaC)
- **Terraform**: Multi-cloud, declarativo, gerenciamento de estado
- **CloudFormation**: Nativo da AWS, templates YAML/JSON
- **ARM Templates**: Nativo do Azure
- **Deployment Manager**: Nativo do GCP
- **Pulumi**: Infraestrutura usando linguagens de programação
- **Benefícios**: Controle de versão, repetibilidade, documentação

### Gerenciamento de Configuração
- **Ansible**: Sem agente, playbooks em YAML
- **Chef**: Baseado em Ruby, ecossistema maduro
- **Puppet**: Declarativo, relatórios robustos
- **SaltStack**: Rápido, baseado em Python

### Monitoramento e Observabilidade
- **Métricas**: CloudWatch, Cloud Monitoring, Azure Monitor
- **Logging**: CloudWatch Logs, Cloud Logging, Log Analytics
- **Tracing**: X-Ray, Cloud Trace, Application Insights
- **Dashboards**: CloudWatch Dashboards, Cloud Console
- **Alertas**: SNS, alertas do Cloud Monitoring, Action Groups

### Orquestração de Contêineres
- **Kubernetes**: Padrão de orquestração da indústria
- **Serviços Gerenciados**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (gerenciamento de tráfego, segurança)
- **GitOps**: ArgoCD, Flux (implantações declarativas)

## Gerenciamento de Custos

### Modelos de Preço
- **Pay-as-you-go**: Pague pelo que usar
- **Instâncias Reservadas**: Compromissos de 1 a 3 anos, descontos significativos
- **Instâncias Spot**: Lance por capacidade ociosa, podem ser interrompidas
- **Savings Plans**: Preços por compromisso flexível
- **Free Tier**: Uso gratuito limitado para novas contas

### Estratégias de Otimização de Custos
- **Right-sizing**: Ajuste os tipos de instância às necessidades da carga de trabalho
- **Auto-scaling**: Escale conforme a demanda
- **Capacidade Reservada**: Comprometa-se com cargas de trabalho de estado estável
- **Uso de Spot**: Use para cargas de trabalho tolerantes a falhas e flexíveis
- **Camadas de Armazenamento**: Mova dados de acesso pouco frequente para camadas mais baratas
- **Limpeza**: Exclua recursos não utilizados, snapshots e AMIs

### Ferramentas de Gerenciamento de Custos
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost Management, Advisor
- **GCP**: Relatórios de faturamento, Recommender
- **Terceiros**: CloudHealth, CloudCheckr, Datadog

## Alta Disponibilidade e Recuperação de Desastres

### Conceitos de Disponibilidade
- **Zonas de Disponibilidade**: Data centers fisicamente separados dentro de uma região
- **Regiões**: Áreas geográficas com múltiplas AZs
- **Edge Locations**: Locais de cache de CDN globalmente

### Estratégias de Alta Disponibilidade
- **Multi-AZ**: Implante entre zonas de disponibilidade
- **Auto-healing**: Substitua automaticamente instâncias com falha
- **Balanceamento de Carga**: Distribua o tráfego entre instâncias saudáveis
- **Replicação de Banco de Dados**: Implantações Multi-AZ, réplicas de leitura

### Estratégias de Recuperação de Desastres
- **Backup e Restauração**: Backups periódicos, restauração quando necessário (custo mais baixo)
- **Pilot Light**: Elementos centrais em execução, escale durante o desastre
- **Warm Standby**: Versão reduzida sempre em execução
- **Multi-Site Ativo/Ativo**: Produção completa em múltiplas regiões (custo mais alto)

### RTO e RPO
- **Objetivo de Tempo de Recuperação (RTO)**: Tempo máximo de indisponibilidade aceitável
- **Objetivo de Ponto de Recuperação (RPO)**: Perda máxima de dados aceitável
- **Seleção de Estratégia**: Com base nos requisitos de negócio e no orçamento

## Tendências Emergentes

### Edge Computing
- Processe dados mais perto da origem
- **Serviços**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Casos de Uso**: IoT, análise em tempo real, aplicações de baixa latência

### Multi-Cloud e Nuvem Híbrida
- Evite vendor lock-in
- Aproveite serviços best-of-breed
- **Ferramentas**: Terraform, Anthos, Arc, CloudHealth

### Serviços de IA/ML
- Modelos pré-treinados: Visão, fala, linguagem
- Treinamento de modelos personalizados: SageMaker, Vertex AI, Azure ML
- MLOps: Implantação, monitoramento e governança de modelos

### Computação Quântica
- **Serviços**: AWS Braket, Azure Quantum
- **Status**: Estágio inicial, experimental
- **Potencial**: Criptografia, otimização, descoberta de medicamentos

### Nuvem Sustentável
- Rastreamento da pegada de carbono
- Compromissos com energia renovável
- Utilização eficiente de recursos
- Padrões de arquitetura verde (green architecture)
