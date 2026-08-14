<!--
---
# Metadata
title: "Terraform and Infrastructure as Code"
description: "IaC concepts, Terraform commands, state management, modules"
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
tags: [terraform, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Terraform e infraestrutura como código
Terraform é a ferramenta de infraestrutura como código (IaC) mais amplamente usada – permite definir infraestrutura em nuvem (servidores, bancos de dados, redes, permissões) em arquivos de configuração declarativos que podem ser versionados, revisados, testados e automatizados. Em vez de clicar em um console de nuvem, você escreve um código que descreve o estado desejado de sua infraestrutura e o Terraform descobre quais mudanças fazer.
---

## Conceitos Básicos
| Conceito | Descrição |
|--------|-------------|
| **Provedor** | Plugin que gerencia uma plataforma de nuvem específica (AWS, Azure, GCP, etc.) |
| **Recurso** | Um objeto de infraestrutura (servidor, banco de dados, rede) |
| **Estado** | Registro do Terraform sobre qual infraestrutura existe; armazenado em um arquivo de estado |
| **Plano** | Prévia das mudanças que o Terraform fará |
| **Inscreva-se** | Executar o plano; criar/atualizar/destruir infraestrutura |
| **Módulo** | Coleta reutilizável de recursos |
| **Variável** | Parâmetro de entrada para configurações |
| **Saída** | Valor exportado de um módulo ou configuração |
| **Fonte de dados** | Ler informações da infraestrutura existente |
---

## Fluxo de trabalho básico
| Etapa | Comando | Descrição |
|------|---------|-------------|
| **1. Configuração de gravação** | Criar arquivos`.tf`| Definir provedores, recursos, variáveis ​​|
| **2. Inicializar** | `terraform init`| Provedores de download; configurar back-end |
| **3. Formato** | `terraform fmt`| Padronizar a formatação |
| **4. Validar** | `terraform validate`| Verifique sintaxe e configuração |
| **5. Plano** | `terraform plan`| Visualizar alterações (ensaio) |
| **6. Aplicar** | `terraform apply`| Criar ou atualizar infraestrutura |
| **7. Destruir** | `terraform destroy`| Destruir toda a infraestrutura gerenciada |
---

## Comandos Comuns
| Comando | Descrição |
|--------|-------------|
| `terraform init`| Inicialize o diretório de trabalho; provedores e módulos de download |
| `terraform plan`| Mostrar quais mudanças serão feitas |
| `terraform apply`| Aplicar alterações; adicione`-auto-approve`para pular a confirmação |
| `terraform destroy`| Destrua todos os recursos gerenciados |
| `terraform fmt`| Formate os arquivos de configuração no estilo padrão |
| `terraform validate`| Validar sintaxe de configuração |
| `terraform output`| Mostrar valores de saída |
| `terraform state list`| Liste todos os recursos no estado |
| `terraform state show <resource>`| Mostrar detalhes de um recurso específico |
| `terraform import <resource> <id>`| Importar infraestrutura existente para o estado |
| `terraform taint <resource>`| Marcar um recurso para recreação na próxima aplicação |
| `terraform refresh`| Atualizar estado para corresponder à infraestrutura real |
| `terraform graph`| Gere um gráfico de dependência visual (formato DOT) |
| `terraform console`| Console interativo para testar expressões |
---

## Gestão de Estado
| Melhores Práticas | Descrição |
|--------------|-------------|
| **Estado remoto** | Armazene o estado em S3, GCS, Azure Blob ou Terraform Cloud — nunca localmente |
| **Bloqueio de estado** | Use DynamoDB (backend S3) ou bloqueio nativo para evitar modificações simultâneas |
| **Criptografia de estado** | Habilite a criptografia em repouso para arquivos de estado (eles contêm dados confidenciais) |
| **Separação de Estados** | Use arquivos de estado separados para diferentes ambientes ou equipes |
| **Backup de estado** | Back-ends remotos atualizam automaticamente o estado da versão; mantenha isso ativado |
| **Nunca edite o estado manualmente** | Use`terraform state mv`,`rm`,`import`|
---

## Estrutura do Módulo
```
module/
├── main.tf          # Primary resources
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider and Terraform version constraints
├── README.md        # Documentation
└── examples/        # Example usage
    └── basic/
        └── main.tf
```

---

## Tipos de variáveis
| Tipo | Exemplo | Caso de uso |
|------|---------|----------|
| **sequência** | `variable "region" { type = string }`| Valor de texto único |
| **número** | `variable "count" { type = number }`| Valor numérico |
| **bool** | `variable "enable" { type = bool }`| Sinalizador verdadeiro/falso |
| **lista** | `variable "zones" { type = list(string) }`| Coleta ordenada |
| **mapa** | `variable "tags" { type = map(string) }`| Pares de valores-chave |
| **objeto** | `variable "config" { type = object({...}) }`| Configuração estruturada |
---

## Padrões Comuns
| Padrão | Descrição |
|--------|-------------|
| **Contagem** | `count = 3`cria múltiplas instâncias de um recurso |
| **Para cada** | `for_each = var.items`itera sobre um mapa ou conjunto |
| **Blocos dinâmicos** | Gerar blocos aninhados repetidos (por exemplo, regras de entrada) |
| **Valores locais** | `locals { ... }`para valores computados e redução de repetição |
| **Fontes de dados** | Leia a infraestrutura existente (por exemplo, encontre uma VPC existente) |
| **Provisionadores** | Execute scripts em recursos após a criação (use com moderação) |
| **Espaços de trabalho** | Estado separado para ambientes diferentes na mesma configuração |
---

## Solução de problemas
| Problema | Solução |
|--------|----------|
| **Desvio de estado** | Execute`terraform plan`para ver as diferenças; `terraform apply`para reconciliar |
| **Estado bloqueado** | Verifique quem está com o bloqueio; use`terraform force-unlock`se for seguro |
| **Erros do provedor** | Verifique as credenciais; atualizar a versão do provedor; verifique os limites da API |
| **Conflitos de importação** | Recurso já em estado; use`terraform state rm`primeiro |
| **Dependências circulares** | Reestruturar recursos; use`depends_on`com cuidado |
| **Grande estado** | Dividido em módulos; use`-target`para operações parciais |
---

## Resumo
O Terraform gerencia a infraestrutura por meio de arquivos de configuração declarativos. O fluxo de trabalho é: escrever configuração → init → planejar → aplicar. O estado rastreia o que existe e deve ser armazenado remotamente com bloqueio. Os módulos permitem a reutilização. Variáveis ​​parametrizam configurações. Os princípios-chave são: tratar a infraestrutura como código (controle de versão; revisão; teste); nunca edite o estado manualmente; planeje antes de aplicar; use estado remoto com bloqueio; e configurações de estrutura com módulos para manutenção.