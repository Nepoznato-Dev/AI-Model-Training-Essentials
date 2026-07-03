# Arquitetura de Nuvem

## Fundamentos da Computação em Nuvem

### O que é Computação em Nuvem?
Entrega sob demanda de recursos de computação (servidores, armazenamento, bancos de dados, rede e software) pela internet, com cobrança conforme o uso.

### Características Essenciais (Definição do NIST)
- **Autoatendimento sob Demanda**: Provisionamento de recursos sem interação humana
- **Amplo Acesso à Rede**: Disponível pela rede por meio de mecanismos padrão
- **Agrupamento de Recursos**: Modelo multitenant com alocação dinâmica
- **Elasticidade Rápida**: Escalabilidade para expandir e reduzir rapidamente
- **Serviço Mensurado**: Uso dos recursos monitorado e faturado

### Modelos de Implantação em Nuvem
- **Nuvem Pública**: Pertence aos provedores, infraestrutura compartilhada (AWS, Azure, GCP)
- **Nuvem Privada**: Dedicada a uma única organização (on-premises ou hospedada)
- **Nuvem Híbrida**: Combinação de nuvens públicas e privadas
- **Multi-Cloud**: Uso de vários provedores de nuvem pública
- **Nuvem Comunitária**: Compartilhada por organizações com interesses em comum

### Modelos de Serviço

#### Infraestrutura como Serviço (IaaS)
- **Fornece**: Máquinas virtuais, armazenamento, redes, sistemas operacionais
- **Exemplos**: AWS EC2, Google Compute Engine, Azure VMs
- **Casos de Uso**: Migrações lift-and-shift, ambientes de desenvolvimento, necessidades de alto controle

#### Plataforma como Serviço (PaaS)
- **Fornece**: Plataformas de desenvolvimento, bancos de dados, middleware
- **Exemplos**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **Casos de Uso**: Desenvolvimento de aplicações, implantação de APIs, microservices

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
- **Principais Serviços**:
  - Compute: EC2, Lambda, ECS, EKS
  - Storage: S3, EBS, Glacier
  - Database: RDS, DynamoDB, Aurora
  - Networking: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **Participação de Mercado**: ~23%
- **Pontos Fortes**: Integração corporativa, nuvem híbrida, ecossistema Microsoft
- **Principais Serviços**:
  - Compute: Virtual Machines, Azure Functions, AKS
  - Storage: Blob Storage, Disk Storage
  - Database: SQL Database, Cosmos DB
  - Networking: Virtual Network, Traffic Manager
  - AI/ML: Azure ML, Cognitive Services

### Google Cloud Platform (GCP)
- **Participação de Mercado**: ~10%
- **Pontos Fortes**: Análise de dados, AI/ML, Kubernetes
- **Principais Serviços**:
  - Compute: Compute Engine, Cloud Functions, GKE
  - Storage: Cloud Storage, Persistent Disk
  - Database: Cloud SQL, Firestore, Bigtable
  - Analytics: BigQuery, Dataflow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

### Outros Provedores
- **IBM Cloud**: Foco corporativo, Watson AI
- **Oracle Cloud**: Cargas de trabalho de banco de dados, aplicações corporativas
- **Alibaba Cloud**: Dominante na Ásia-Pacífico
- **DigitalOcean**: Amigável para desenvolvedores, ofertas simplificadas

## Padrões de Arquitetura de Nuvem

### Princípios do Well-Architected Framework

#### Excelência Operacional
- Automatizar operações
- Fazer mudanças frequentes e reversíveis
- Refinar procedimentos continuamente
- Antecipar falhas

#### Segurança
- Implementar uma base sólida de identidade
- Habilitar rastreabilidade
- Aplicar segurança em todas as camadas
- Automatizar boas práticas de segurança
- Proteger dados em trânsito e em repouso

#### Confiabilidade
- Testar procedimentos de recuperação
- Recuperar-se automaticamente de falhas
- Escalar horizontalmente para disponibilidade
- Parar de adivinhar capacidade
- Gerenciar mudanças por meio de automação

#### Eficiência de Desempenho
- Democratizar tecnologias avançadas
- Tornar-se global em minutos
- Usar arquiteturas serverless
- Experimentar com mais frequência
- Considerar a afinidade mecânica

#### Otimização de Custos
- Adotar o modelo de consumo
- Medir a eficiência geral
- Parar de gastar dinheiro com trabalho não diferenciado
- Analisar e atribuir gastos
- Usar serviços gerenciados

### Padrões Comuns de Arquitetura

#### Arquitetura de Microservices
- Decompor aplicações em serviços pequenos e independentes
- Cada serviço é dono de seus dados e de sua lógica
- Comunicar-se por APIs (REST, gRPC, mensageria)
- Fazer deploy de forma independente
- **Benefícios**: Escalabilidade, isolamento de falhas, diversidade tecnológica
- **Desafios**: Complexidade distribuída, consistência de dados, monitoramento

#### Arquitetura Orientada a Eventos
- Os componentes se comunicam por meio de eventos
- Produtores emitem eventos, consumidores reagem
- **Padrões**: Event sourcing, CQRS, pub/sub
- **Tecnologias**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Benefícios**: Baixo acoplamento, escalabilidade, processamento em tempo real

#### Arquitetura Serverless
- Não exige gerenciamento de servidores
- Pagamento por execução
- Escalabilidade automática
- **Componentes**: Functions, API Gateway, serviços gerenciados
- **Benefícios**: Eficiência de custos, menos operações, implantação rápida
- **Considerações**: Cold starts, vendor lock-in, limites de execução

#### Arquitetura em Camadas (N-Tier)
- Camada de apresentação (UI)
- Camada de aplicação/lógica de negócios
- Camada de acesso a dados
- Camada de banco de dados
- **Benefícios**: Separação de responsabilidades, manutenibilidade
- **Comum**: Aplicações web em 3 camadas

#### Arquitetura Baseada em Espaço
- Lida com alta concorrência usando dados distribuídos
- Memória virtualizada entre servidores
- Nós de processamento escalam de forma independente
- **Casos de Uso**: Aplicações de alto volume e baixa latência

## Serviços de Compute

### Máquinas Virtuais
- **Tipos**: Uso geral, otimizadas para computação, otimizadas para memória, GPU
- **Preços**: On-demand, reserved instances, spot instances
- **Gerenciamento**: Grupos de auto-scaling, load balancers
- **Boas Práticas**: Right-sizing, tagging, monitoramento, patching

### Containers
- **Docker**: Padrão de runtime para containers
- **Orquestração**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Benefícios**: Portabilidade, eficiência, consistência
- **Registry**: ECR, GCR, ACR, Docker Hub

### Funções Serverless
- **Modelo de Execução**: Acionado por eventos, stateless
- **Limites**: Tempo de execução, memória, execuções simultâneas
- **Casos de Uso**: APIs, processamento de arquivos, jobs agendados, backends de IoT
- **Monitoramento**: Número de invocações, erros, duração, cold starts

## Soluções de Armazenamento

### Armazenamento de Objetos
- **Características**: Estrutura plana, metadados, acesso via HTTP
- **Exemplos**: AWS S3, Google Cloud Storage, Azure Blob
- **Casos de Uso**: Ativos estáticos, backups, data lakes, arquivos
- **Classes de Armazenamento**: Hot, cool, cold, archive (custos/acesso variáveis)

### Armazenamento em Blocos
- **Características**: Volumes brutos, anexados a VMs
- **Exemplos**: AWS EBS, Google Persistent Disk, Azure Disks
- **Casos de Uso**: Bancos de dados, volumes de boot, necessidades de alto desempenho
- **Tipos**: SSD, HDD, IOPS provisionado

### Armazenamento de Arquivos
- **Características**: Sistemas de arquivos compartilhados, protocolos NFS/SMB
- **Exemplos**: AWS EFS, Google Filestore, Azure Files
- **Casos de Uso**: Gestão de conteúdo, configurações compartilhadas, lift-and-shift

### Armazenamento de Arquivo Morto
- **Características**: Menor custo, atraso na recuperação
- **Exemplos**: S3 Glacier, Azure Archive Storage
- **Casos de Uso**: Compliance, backups de longo prazo, dados históricos

## Serviços de Banco de Dados

### Bancos de Dados Relacionais Gerenciados
- **Serviços**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL Database
- **Recursos**: Backups automáticos, patching, escalabilidade, replicação
- **Engines**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### Bancos de Dados NoSQL
- **Document**: DocumentDB, Firestore, Cosmos DB
- **Key-Value**: DynamoDB, Redis Cache
- **Wide-Column**: Bigtable, Cassandra (gerenciado)
- **Graph**: Neptune, Cosmos DB (graph API)

### Data Warehousing
- **Serviços**: Snowflake, Redshift, BigQuery, Synapse
- **Características**: Armazenamento colunar, arquitetura MPP
- **Casos de Uso**: Analytics, BI, análise de dados em grande escala

### Serviços de Cache
- **In-Memory**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **CDN Caching**: CloudFront, Cloud CDN, Azure CDN
- **Casos de Uso**: Armazenamento de sessão, cache de consultas, entrega de conteúdo

## Rede

### Redes Virtuais
- **VPC/VNet**: Ambientes de rede isolados
- **Sub-redes**: Públicas (voltadas para a internet), privadas (somente internas)
- **Endereçamento IP**: Blocos CIDR, IPv4/IPv6
- **Tabelas de Rotas**: Controlam o fluxo do tráfego

### Balanceamento de Carga
- **Tipos**: Application (L7), Network (L4), Gateway
- **Recursos**: Health checks, terminação SSL, sticky sessions
- **Serviços**: ELB/ALB/NLB, Cloud Load Balancing, Azure Load Balancer

### Redes de Entrega de Conteúdo (CDN)
- **Objetivo**: Armazenar conteúdo em cache nos edge locations
- **Benefícios**: Menor latência, menor carga na origem, distribuição global
- **Serviços**: CloudFront, Cloud CDN, Azure CDN, Akamai

### Serviços de DNS
- **Funções**: Registro de domínio, roteamento, health checks
- **Serviços**: Route 53, Cloud DNS, Azure DNS
- **Políticas de Roteamento**: Simples, ponderado, baseado em latência, geolocalização, failover

### Opções de Conectividade
- **Internet Gateway**: Acesso à internet pública
- **NAT Gateway**: Acesso de saída para sub-redes privadas
- **VPN**: Túneis criptografados para ambientes on-premises
- **Direct Connect/ExpressRoute**: Conexões privadas dedicadas
- **VPC Peering**: Conecta VPCs dentro/entre contas

## Segurança na Nuvem

### Modelo de Responsabilidade Compartilhada
- **Responsabilidade do Provedor**: Segurança DA nuvem (infraestrutura)
- **Responsabilidade do Cliente**: Segurança NA nuvem (dados, aplicações, acesso)
- **Varia por Serviço**: Quanto mais gerenciado, maior a responsabilidade do provedor

### Identity and Access Management (IAM)
- **Users**: Identidades individuais
- **Groups**: Coleções de usuários
- **Roles**: Credenciais temporárias para serviços/usuários
- **Policies**: Documentos JSON que definem permissões
- **Princípios**: Menor privilégio, separação de funções

### Segurança de Rede
- **Security Groups**: Firewalls stateful para instâncias
- **Network ACLs**: Firewalls stateless para sub-redes
- **Web Application Firewall (WAF)**: Proteção contra explorações web
- **Proteção contra DDoS**: Shield, Cloud Armor, DDoS Protection

### Proteção de Dados
- **Criptografia em Repouso**: KMS, chaves gerenciadas pelo cliente
- **Criptografia em Trânsito**: TLS/SSL, HTTPS
- **Gerenciamento de Chaves**: HSM, rotação de chaves, trilhas de auditoria
- **Gerenciamento de Segredos**: Secrets Manager, Key Vault

### Compliance e Governança
- **Certificações**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Ferramentas**: Aplicação de políticas, relatórios de conformidade, logs de auditoria
- **Frameworks**: Cloud Security Alliance, NIST CSF

## DevOps na Nuvem

### Serviços de CI/CD
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Terceiros**: Jenkins, CircleCI, GitLab CI

### Infrastructure as Code (IaC)
- **Terraform**: Multi-cloud, declarativo, gerenciamento de estado
- **CloudFormation**: Nativo da AWS, templates YAML/JSON
- **ARM Templates**: Nativo do Azure
- **Deployment Manager**: Nativo do GCP
- **Pulumi**: Infraestrutura usando linguagens de programação
- **Benefícios**: Controle de versão, repetibilidade, documentação

### Gerenciamento de Configuração
- **Ansible**: Sem agente, playbooks YAML
- **Chef**: Baseado em Ruby, ecossistema maduro
- **Puppet**: Declarativo, relatórios robustos
- **SaltStack**: Rápido, baseado em Python

### Monitoramento e Observabilidade
- **Métricas**: CloudWatch, Cloud Monitoring, Azure Monitor
- **Logging**: CloudWatch Logs, Cloud Logging, Log Analytics
- **Tracing**: X-Ray, Cloud Trace, Application Insights
- **Dashboards**: CloudWatch Dashboards, Cloud Console
- **Alertas**: SNS, alertas do Cloud Monitoring, Action Groups

### Orquestração de Containers
- **Kubernetes**: Padrão da indústria para orquestração
- **Serviços Gerenciados**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (gerenciamento de tráfego, segurança)
- **GitOps**: ArgoCD, Flux (implantações declarativas)

## Gestão de Custos

### Modelos de Preço
- **Pay-as-you-go**: Pague pelo que usar
- **Reserved Instances**: Compromissos de 1 a 3 anos, descontos significativos
- **Spot Instances**: Oferta por capacidade ociosa, podem ser interrompidas
- **Savings Plans**: Preços flexíveis por compromisso
- **Free Tier**: Uso gratuito limitado para novas contas

### Estratégias de Otimização de Custos
- **Right-sizing**: Adequar tipos de instância às necessidades da carga de trabalho
- **Auto-scaling**: Escalar com base na demanda
- **Capacidade Reservada**: Comprometer-se com cargas de trabalho estáveis
- **Uso de Spot**: Usar para cargas flexíveis e tolerantes a falhas
- **Camadas de Armazenamento**: Mover dados pouco acessados para camadas mais baratas
- **Limpeza**: Excluir recursos não usados, snapshots e AMIs

### Ferramentas de Gestão de Custos
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost Management, Advisor
- **GCP**: Relatórios de billing, Recommender
- **Terceiros**: CloudHealth, CloudCheckr, Datadog

## Alta Disponibilidade e Recuperação de Desastres

### Conceitos de Disponibilidade
- **Availability Zones**: Data centers fisicamente separados dentro de uma região
- **Regions**: Áreas geográficas com múltiplas AZs
- **Edge Locations**: Locais globais de cache da CDN

### Estratégias de HA
- **Multi-AZ**: Implantar em várias zonas de disponibilidade
- **Auto-healing**: Substituição automática de instâncias com falha
- **Load Balancing**: Distribuir tráfego entre instâncias saudáveis
- **Replicação de Banco de Dados**: Implantações Multi-AZ, réplicas de leitura

### Estratégias de Recuperação de Desastres
- **Backup and Restore**: Backups periódicos, restauração quando necessário (menor custo)
- **Pilot Light**: Elementos essenciais em execução, com escalonamento durante o desastre
- **Warm Standby**: Versão reduzida sempre em execução
- **Multi-Site Active/Active**: Produção completa em várias regiões (maior custo)

### RTO e RPO
- **Recovery Time Objective (RTO)**: Tempo máximo aceitável de indisponibilidade
- **Recovery Point Objective (RPO)**: Perda máxima aceitável de dados
- **Seleção da Estratégia**: Baseada em requisitos de negócio e orçamento

## Tendências Emergentes

### Edge Computing
- Processar dados mais perto da origem
- **Serviços**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Casos de Uso**: IoT, analytics em tempo real, aplicações de baixa latência

### Multi-Cloud e Nuvem Híbrida
- Evitar vendor lock-in
- Aproveitar serviços best-of-breed
- **Ferramentas**: Terraform, Anthos, Arc, CloudHealth

### Serviços de AI/ML
- Modelos pré-treinados: visão, fala, linguagem
- Treinamento de modelos customizados: SageMaker, Vertex AI, Azure ML
- MLOps: implantação de modelos, monitoramento, governança

### Computação Quântica
- **Serviços**: AWS Braket, Azure Quantum
- **Status**: Estágio inicial, experimental
- **Potencial**: Criptografia, otimização, descoberta de medicamentos

### Nuvem Sustentável
- Rastreamento da pegada de carbono
- Compromissos com energia renovável
- Utilização eficiente de recursos
- Padrões de arquitetura verde
