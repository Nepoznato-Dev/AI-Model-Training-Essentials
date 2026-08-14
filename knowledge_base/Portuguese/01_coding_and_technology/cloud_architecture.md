<!--
---
# Metadata
title: "Cloud Architecture"
description: "Cloud providers, architecture patterns, security"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cloud, architecture, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "11 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Arquitetura em nuvem
A computação em nuvem mudou fundamentalmente a forma como as organizações criam, implantam e dimensionam software. Em vez de comprar e manter servidores físicos, você pode provisionar recursos de computação sob demanda, pagar pelo que usa e dimensionar globalmente em minutos. Este arquivo cobre os principais conceitos, padrões de arquitetura, serviços e práticas recomendadas que você precisa conhecer.
---

## Fundamentos da computação em nuvem
### O que é computação em nuvem?
Entrega sob demanda de recursos de computação — servidores, armazenamento, bancos de dados, redes, software — pela Internet com preços pré-pagos.
### Características essenciais do NIST
| Característica | Significado |
|---------------|---------|
| **Autoatendimento sob demanda** | Provisão de recursos sem interação humana |
| **Amplo acesso à rede** | Disponível na rede através de mecanismos padrão |
| **Agregação de recursos** | Modelo multilocatário; recursos atribuídos dinamicamente |
| **Elasticidade Rápida** | Expanda para fora e para dentro rapidamente |
| **Serviço medido** | O uso é monitorado e cobrado |
### Modelos de implantação
| Modelo | Descrição | Quando usar |
|-------|------------|-------------|
| **Nuvem pública** | Propriedade de fornecedores; infraestrutura compartilhada (AWS, Azure, GCP) | A maioria das cargas de trabalho; rentável |
| **Nuvem privada** | Dedicado a uma única organização | Requisitos regulamentares, dados sensíveis |
| **Nuvem Híbrida** | Combinação de público e privado | Flexibilidade + conformidade |
| **Multinuvem** | Usando vários provedores de nuvem pública | Evite o aprisionamento do fornecedor, o melhor da categoria |
### Modelos de serviço
| Modelo | Fornece | Exemplos | Casos de uso |
|-------|----------|----------|----------|
| **IaaS** | VMs, armazenamento, redes, SO | AWS EC2, VMs do Azure, GCP Compute Engine | Migrações lift-and-shift, controle total |
| **PaaS** | Plataformas de desenvolvimento, bancos de dados, middleware | Heroku, Google App Engine, AWS Elastic Beanstalk | Desenvolvimento de aplicativos, implantação de API |
| **SaaS** | Preencher inscrições pela internet | Salesforce, Google Workspace, Microsoft 365 | E-mail, CRM, colaboração |
| **FaaS/sem servidor** | Execução de função orientada a eventos | AWS Lambda, Azure Functions, GCP Cloud Functions | APIs, processamento de eventos, tarefas agendadas |
---

## Principais provedores de nuvem
| Provedor | Participação de mercado | Pontos fortes |
|----------|-------------|-----------|
| **AWS** | ~32% | Catálogo de serviços mais amplo, maior ecossistema |
| **Azul** | ~23% | Integração empresarial, nuvem híbrida, pilha Microsoft |
| **GCP** | ~10% | Análise de dados, IA/ML, Kubernetes |
| **Nuvem Alibaba** | ~4% | Dominante na Ásia-Pacífico |
| **Oracle Cloud** | ~2% | Cargas de trabalho de banco de dados, aplicativos corporativos |
| **Nuvem IBM** | ~2% | Foco empresarial, Watson AI |
| **Oceano Digital** | Nicho | Ofertas simplificadas e amigáveis ​​ao desenvolvedor |
### Comparação de serviços (3 principais provedores)
| Categoria | AWS | Azul | GCP |
|----------|-----|-------|-----|
| **Cálculo** | EC2, Lambda, ECS | VMs, funções, AKS | Compute Engine, Cloud Functions, GKE |
| **Armazenamento** | S3, EBS, Geleira | Armazenamento de blob, armazenamento em disco | Armazenamento em nuvem, disco permanente |
| **Banco de dados** | RDS, DynamoDB, Aurora | Banco de dados SQL, Cosmos DB | Cloud SQL, Firestore, Bigtable |
| **Análise** | Desvio para o vermelho, EMR | Sinapse, blocos de dados | BigQuery, fluxo de dados |
| **IA/ML** | SageMaker, Reconhecimento | Azure ML, serviços cognitivos | Vertex AI, AutoML |
| **Rede** | VPC, Rota 53, CloudFront | VNet, Gerenciador de Tráfego | VPC, Cloud DNS, Cloud CDN |
---

## Padrões de Arquitetura
### Estrutura bem arquitetada
Todos os três principais fornecedores publicam estruturas bem arquitetadas, construídas em torno de cinco pilares:
| Pilar | Princípios Chave |
|--------|---------------|
| **Excelência Operacional** | Automatizar operações; fazer alterações frequentes e reversíveis; antecipar o fracasso |
| **Segurança** | Forte base de identidade; aplique segurança em todas as camadas; proteger dados em trânsito e em repouso |
| **Confiabilidade** | Procedimentos de recuperação de testes; recuperação automática de falhas; dimensionar horizontalmente |
| **Eficiência de desempenho** | Use sem servidor; torne-se global em minutos; experimente frequentemente |
| **Otimização de custos** | Adotar modelo de consumo; usar serviços gerenciados; parar de gastar com trabalho indiferenciado |
### Padrões Comuns
| Padrão | Descrição | Benefícios | Desafios |
|---------|-------------|----------|------------|
| **Microsserviços** | Decompor o aplicativo em serviços pequenos e independentes | Escalabilidade, isolamento de falhas, implantação independente | Complexidade distribuída, consistência de dados |
| **Orientado por eventos** | Componentes se comunicam através de eventos | Acoplamento frouxo, processamento em tempo real | Complexidade de depuração, consistência eventual |
| **Sem servidor** | Sem gerenciamento de servidor; pagamento por execução | Eficiência de custos, implantação rápida | Arranques a frio, dependência de fornecedor, limites de execução |
| **Em camadas (n camadas)** | Apresentação → Lógica de negócios → Acesso a dados → Banco de dados | Separação de preocupações, manutenibilidade | Pode tornar-se monolítico |
| **Baseado no espaço** | Dados distribuídos entre nós de memória virtualizados | Lida com alta simultaneidade e baixa latência | Complexo para projetar e gerenciar |
---

## Serviços principais
### Computação
| Tipo de serviço | Detalhes |
|------------|---------|
| **Máquinas Virtuais** | GPU de uso geral, otimizada para computação e memória. Preços: sob demanda, reservado, spot. |
| **Contêineres** | Tempo de execução do Docker; orquestração via Kubernetes (EKS, AKS, GKE). Registros: ECR, GCR, ACR. |
| **Funções sem servidor** | Acionado por evento, sem estado. Limites de tempo de execução, memória, simultaneidade. |
### Armazenar
| Tipo | Características | Exemplos | Melhor para |
|------|----------------|----------|----------|
| **Objeto** | Estrutura plana, acesso HTTP, rico em metadados | S3, armazenamento em nuvem, Blob do Azure | Ativos estáticos, backups, data lakes |
| **Bloquear** | Volumes brutos anexados a VMs | EBS, Disco Permanente, Discos Azure | Bancos de dados, volumes de inicialização |
| **Arquivo** | Sistemas de arquivos compartilhados (NFS/SMB) | EFS, Filestore, Arquivos do Azure | Gerenciamento de conteúdo, configurações compartilhadas |
| **Arquivo** | Menor custo, atrasos na recuperação | Geleira S3, Arquivo do Azure | Conformidade, backups de longo prazo |
### Bancos de dados
| Categoria | Serviços | Caso de uso |
|----------|----------|----------|
| **Relacional Gerenciado** | RDS, Cloud SQL, Azure SQL | Aplicativos tradicionais, transações ACID |
| **NoSQL — Documento** | DocumentDB, Firestore, Cosmos DB | Esquemas flexíveis, dados JSON |
| **NoSQL — Valor-chave** | DynamoDB, Cache Redis | Cache, sessões, pesquisas simples |
| **NoSQL — Coluna Larga** | Bigtable, Cassandra | Séries temporais com muitas gravações |
| **NoSQL — Gráfico** | Netuno, Cosmos DB (API gráfica) | Relacionamentos, redes sociais |
| **Armazenamento de Dados** | Floco de neve, Redshift, BigQuery, Synapse | Análise, BI |
| **Cache** | ElastiCache, armazenamento de memória em nuvem | Armazenamento de sessão, cache de consulta |
---

## Rede
### Redes Virtuais
Cada implantação de nuvem reside dentro de uma nuvem privada virtual (VPC/VNet) — uma rede isolada que você define com blocos CIDR, sub-redes (públicas ou privadas), tabelas de rotas e gateways.
### Balanceamento de carga e CDN
| Serviço | Finalidade |
|--------|---------|
| **Balanceadores de carga** | Distribuir o tráfego entre instâncias (rede L4, aplicação L7) |
| **CDN** | Conteúdo em cache em pontos de presença para menor latência (CloudFront, Cloud CDN, Azure CDN) |
| **DNS** | Registro de domínio, políticas de roteamento, verificações de integridade (Route 53, Cloud DNS, Azure DNS) |
### Opções de conectividade
| Opção | Descrição |
|--------|------------|
| **Gateway de Internet** | Acesso público à Internet para VPC |
| **Gateway NAT** | Acesso de saída à sub-rede privada |
| **VPN** | Túneis criptografados para o local |
| **Conexão direta/ExpressRoute** | Conexões privadas dedicadas |
| **Peering de VPC** | Conectar VPCs dentro ou entre contas |
---

## Segurança
### Modelo de Responsabilidade Compartilhada
| Camada | Provedor | Cliente |
|-------|----------|----------|
| **Infraestrutura** (hardware, instalações) | ✅ | |
| **Computação, armazenamento, rede** | ✅ (gerenciado) | ✅ (autogerenciado) |
| **Dados, aplicativos, identidade** | | ✅ |
Quanto mais gerenciado o serviço, mais o provedor gerencia. Com IaaS você gerencia quase tudo; com o SaaS, o provedor cuida de quase tudo.
### Gerenciamento de identidade e acesso (IAM)
| Conceito | Descrição |
|--------|-------------|
| **Usuários** | Identidades individuais |
| **Grupos** | Coleções de usuários |
| **Funções** | Credenciais temporárias para serviços ou usuários |
| **Políticas** | Documentos que definem permissões |
| **Princípio** | Privilégio mínimo, separação de funções |
### Proteção de Dados
- **Criptografia em repouso**: KMS, chaves gerenciadas pelo cliente, HSM.
- **Criptografia em trânsito**: TLS/SSL, HTTPS.
- **Gerenciamento de segredos**: Secrets Manager, Key Vault — nunca codifique segredos.
---

## DevOps na nuvem
### Infraestrutura como Código (IaC)
| Ferramenta | Descrição |
|------|-------------|
| **Terraforma** | HCL declarativa, multinuvem, gerenciamento de estado |
| **CloudFormation** | Modelos YAML/JSON nativos da AWS |
| **Modelos ARM/Bíceps** | Nativo do Azure |
| **Pulumi** | Infraestrutura utilizando linguagens de programação (Python, Go, etc.) |
### Serviços CI/CD
| Provedor | Ferramentas |
|----------|-------|
| **AWS** | CodePipeline, CodeBuild, CodeDeploy |
| **Azul** | Azure DevOps, ações do GitHub |
| **GCP** | Construção em nuvem, implantação em nuvem |
| **Terceiros** | Jenkins, CircleCI, GitLab CI |
### Monitoramento e Observabilidade
| Capacidade | AWS | Azul | GCP |
|-----------|-----|-------|-----|
| **Métricas** | CloudWatch | Monitor Azure | Monitoramento de nuvem |
| **Registro** | Registros do CloudWatch | Análise de registros | Registro em nuvem |
| **Rastreamento** | Raio X | Informações sobre aplicativos | Rastreamento de nuvem |
---

## Gerenciamento de Custos
### Modelos de preços
| Modelo | Descrição | Melhor para |
|-------|------------|----------|
| **Sob demanda** | Pague pelo que usar, por segundo/hora | Cargas de trabalho variáveis ​​e de curto prazo |
| **Instâncias reservadas** | Compromisso de 1–3 anos, desconto significativo | Cargas de trabalho em estado estacionário |
| **Instâncias spot** | Licitar capacidade não utilizada; pode ser interrompido | Trabalhos flexíveis e tolerantes a falhas |
| **Planos de Poupança** | Preços de compromisso flexíveis | Padrões de uso mistos |
| **Nível gratuito** | Uso gratuito limitado para novas contas | Aprendizagem, prototipagem |
### Estratégias de otimização
Instâncias do tamanho certo para corresponder às cargas de trabalho. Use o escalonamento automático para lidar com picos de demanda. Capacidade de reserva para cargas previsíveis. Use instâncias spot para trabalhos em lote. Mova dados acessados ​​com pouca frequência para níveis de armazenamento mais baratos. Exclua recursos não utilizados (snapshots órfãos, balanceadores de carga ociosos, IPs não anexados).
---

## Alta disponibilidade e recuperação de desastres
### Conceitos de Disponibilidade
| Conceito | Descrição |
|--------|-------------|
| **Zona de disponibilidade (AZ)** | Data centers separados fisicamente em uma região |
| **Região** | Área geográfica com múltiplas AZs |
| **Localização da borda** | Localização do cache CDN para entrega de conteúdo |
### Estratégias de recuperação de desastres
| Estratégia | Custo | RTO | RPO | Descrição |
|----------|------|-----|-----|------------|
| **Backup e restauração** | Mais baixo | Horas | Horas–dias | Backups periódicos, restaure quando necessário |
| **Luz piloto** | Baixo | Minutos–horas | Minutos | Elementos centrais sempre em execução, ampliados em caso de desastre |
| **Espera quente** | Médio | Minutos | Segundos–minutos | Versão reduzida sempre em execução |
| **Vários sites ativos/ativos** | Mais alto | Perto de zero | Zero | Produção total em múltiplas regiões |
**RTO** (Recovery Time Objective) = tempo de inatividade máximo aceitável. **RPO** (Recovery Point Objective) = perda de dados máxima aceitável.
---

## Tendências emergentes
| Tendência | O que está acontecendo |
|-------|-----------------|
| **Computação de borda** | Processamento de dados mais próximo da origem (AWS Outposts, Wavelength, Azure Edge) |
| **Multinuvem** | Evitar o aprisionamento do fornecedor; aproveitando o que há de melhor entre fornecedores |
| **Serviços de IA/ML** | Modelos pré-treinados (visão, fala, linguagem) + treinamento personalizado (SageMaker, Vertex AI) |
| **Computação Quântica** | Serviços experimentais em estágio inicial (AWS Braket, Azure Quantum) |
| **Nuvem sustentável** | Rastreamento da pegada de carbono, compromissos com energias renováveis, arquitetura verde |