<!--
---
# Metadata
title: "DevOps and CI/CD"
description: "CI/CD pipelines, Docker, Kubernetes, Terraform, GitOps"
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
tags: [devops, cicd, coding-and-technology]
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
# DevOps e CI/CD
DevOps é a combinação de filosofia cultural, práticas e ferramentas que permite às equipes entregar software de forma mais rápida e confiável. Ele quebra a barreira entre os desenvolvedores (que desejam implementar mudanças) e as operações (que desejam estabilidade). CI/CD — Integração Contínua e Entrega Contínua — é a espinha dorsal da automação que torna isso possível.
---

## Pipelines de CI/CD
### O que CI/CD realmente significa
| Prazo | O que faz |
|------|-------------|
| **Integração Contínua (CI)** | Os desenvolvedores mesclam códigos com frequência; cada mesclagem aciona compilações e testes automatizados |
| **Entrega Contínua (CD)** | O código está sempre em estado implantável; liberar para produção é uma decisão manual |
| **Implantação contínua** | Cada mudança que passa nos testes vai para produção automaticamente – sem controle manual |
### Estágios típicos do pipeline
| Palco | O que acontece | Ferramentas |
|-------|-------------|-------|
| **Fonte** | Desenvolvedor envia código para Git | GitHub, GitLab, Bitbucket |
| **Construir** | Compilar código, instalar dependências | Maven, Gradle, npm, pip |
| **Teste** | Executar verificações de unidade, integração e lint | Brincadeira, pytest, JUnit |
| **Pacote** | Construir imagem ou artefato Docker | Docker, pacotes de construção |
| **Implantar (preparação)** | Implantar no ambiente de teste | Kubernetes, ECS, VM |
| **Teste (preparação)** | Testes de integração, testes de fumaça | Selênio, carteiro |
| **Implantar (produção)** | Liberação para produção | Azul esverdeado, canário, rolante |
| **Monitoramento** | Observe saúde, erros, desempenho | Prometeu, Grafana, Datadog |
### Ferramentas CI/CD comparadas
| Ferramenta | Tipo | Força |
|------|------|----------|
| **Ações do GitHub** | CI/CD na nuvem | Profundamente integrado com GitHub; Fluxos de trabalho YAML |
| **GitLabCI** | CI/CD integrado | Plataforma única para repo + pipeline |
| **Jenkins** | CI/CD auto-hospedado | Altamente configurável; enorme ecossistema de plugins |
| **CírculoCI** | CI/CD na nuvem | Rápido; bom para fluxos de trabalho em contêineres |
| **ArgoCD** | GitOps para Kubernetes | Implantações declarativas orientadas por Git |
---

## Docker e contêineres
### Por que contêineres?
Antes dos contêineres, o problema clássico era “funciona na minha máquina”. Os contêineres resolvem isso empacotando um aplicativo com todas as suas dependências (bibliotecas, tempo de execução, configuração) em uma unidade única e portátil que é executada de forma idêntica em qualquer lugar.
### Fundamentos do Docker
| Conceito | Descrição |
|--------|-------------|
| **Imagem** | Modelo somente leitura com app + dependências |
| **Contêiner** | Executando instância de uma imagem |
| **Dockerfile** | Receita para construir uma imagem |
| **Registro** | Armazenamento de imagens (Docker Hub, ECR, GCR) |
| **Volume** | Armazenamento persistente que sobrevive a reinicializações de contêineres |
| **Rede** | Camada de rede isolada para contêineres |
### Melhores práticas do Dockerfile
```dockerfile
# Use specific base image tags, not 'latest'
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (leverage Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run as non-root user
USER appuser

# Expose port and define entrypoint
EXPOSE 8000
CMD ["python", "main.py"]
```

Práticas principais: usar imagens base slim/alpine, executar como não raiz, aproveitar o cache da camada, usar`.dockerignore`, verificar imagens em busca de vulnerabilidades (`trivy`,`docker scan`) e definir limites de recursos.
### Docker Compor
Para executar vários contêineres juntos (aplicativo + banco de dados + cache):
```yaml
services:
  app:
    build: .
    ports: ["8000:8000"]
    depends_on: [db, redis]
    environment:
      DATABASE_URL: postgresql://user:pass@db:5432/mydb
  db:
    image: postgres:16
    volumes: [pgdata:/var/lib/postgresql/data]
  redis:
    image: redis:7-alpine
volumes:
  pgdata:
```

---

##Kubernetes (K8s)
Kubernetes é o orquestrador de contêineres padrão do setor. Ele gerencia a implantação, o dimensionamento e a operação de aplicativos em contêineres.
### Arquitetura Central
| Componente | Função |
|-----------|------|
| **Plano de Controle** | Gerencia o cluster (servidor API, agendador, etcd, gerenciador de controlador) |
| **Nó** | Máquina trabalhadora (VM ou física) que executa contêineres |
| **Vagem** | Menor unidade implantável; um ou mais contêineres que compartilham redes |
| **Serviço** | Endpoint de rede estável que roteia o tráfego para pods |
| **Implantação** | Definição declarativa do estado desejado do pod (réplicas, imagem, etc.) |
| **Entrada** | Regras de roteamento HTTP para tráfego externo |
| **ConfigMap / Segredo** | Configuração e dados confidenciais injetados em pods |
### Comandos essenciais do kubectl
```bash
kubectl get pods                    # List pods
kubectl get services                # List services
kubectl describe pod <name>         # Detailed pod info
kubectl logs <pod-name>             # View pod logs
kubectl exec -it <pod> -- /bin/sh   # Shell into a pod
kubectl apply -f deployment.yaml    # Apply a manifest
kubectl rollout status deploy/myapp # Check rollout progress
kubectl scale deploy/myapp --replicas=5  # Scale to 5 replicas
```

### Elmo
Helm é o gerenciador de pacotes do Kubernetes. Um **gráfico** é um pacote de recursos pré-configurados do Kubernetes. Pense nisso como`apt`ou`brew`para K8s.
```bash
helm install my-release bitnami/postgresql   # Install a chart
helm upgrade my-release bitnami/postgresql   # Upgrade
helm rollback my-release 1                   # Rollback to revision 1
helm list                                    # List releases
```

---

## Infraestrutura como código (IaC)
A IaC trata a configuração da infraestrutura da mesma forma que você trata o código do aplicativo: controlado por versão, testado e implantado por meio de pipelines.
###Terraform vs Ansible
| Ferramenta | Tipo | Abordagem | Melhor para |
|------|------|----------|----------|
| **Terraforma** | Provisionamento | Declarativo (HCL); baseado no estado | Criação de recursos em nuvem (VPCs, VMs, bancos de dados) |
| **Ansible** | Configuração | Declarativo (YAML); sem agente | Configurando servidores, instalando software |
| **Pulumi** | Provisionamento | Imperativo (Python, Go, TS) | Equipes que preferem linguagens de programação reais |
| **CloudFormation** | Provisionamento | Declarativo (YAML/JSON); Nativo da AWS | Infraestrutura somente AWS |
### Exemplo de Terraform
```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  tags = {
    Name = "web-server"
  }
}
```

Práticas recomendadas: use módulos para reutilização, armazene o estado remotamente (S3 + DynamoDB para bloqueio), nunca codifique segredos e controle de versão tudo.
---

## Monitoramento e Observabilidade
### Os Três Pilares
| Pilar | O que isso lhe diz | Ferramentas |
|----|------------------|-------|
| **Métricas** | Medições numéricas ao longo do tempo (CPU, taxa de pedidos, taxa de erros) | Prometheus, CloudWatch, Datadog |
| **Registros** | Eventos discretos com contexto (erros, solicitações, mudanças de estado) | Pilha ELK, Loki, CloudWatch Logs |
| **Traços** | Jornada de solicitação ponta a ponta entre serviços | Jaeger, Raio X, Zipkin |
### Prometheus + Pilha Grafana
A pilha de monitoramento de código aberto padrão:
| Componente | Função |
|-----------|------|
| **Prometeu** | Banco de dados de séries temporais; extrai métricas de serviços |
| **Grafana** | Visualização e dashboards |
| **Gerenciador de alertas** | Encaminha alertas para Slack, PagerDuty, email |
| **Exportador de nós** | Expõe métricas em nível de sistema (CPU, RAM, disco) |
| **Exportador de caixa preta** | Testa endpoints (HTTP, TCP, ICMP) |
### Principais métricas a serem rastreadas
| Categoria | Métricas |
|----------|---------|
| **Infraestrutura** | CPU, RAM, uso de disco, E/S de rede |
| **Inscrição** | Taxa de solicitação, latência (p50, p95, p99), taxa de erro |
| **Banco de dados** | Contagem de consultas, consultas lentas, uso do pool de conexões |
| **Negócios** | Inscrições, conversões, receitas |
---

## Estratégias de implantação
| Estratégia | Como funciona | Risco | Reversão |
|----------|------------|------|----------|
| **Atualização contínua** | Substitua gradualmente as instâncias antigas por novas | Alguns usuários na versão antiga, alguns na nova versão | Reverter para imagem anterior |
| **Azul-Verde** | Execute dois ambientes idênticos; mudar o tráfego | Custo duplo da infraestrutura durante a transição | Retorno instantâneo |
| **Canário** | Direcione pequena % de tráfego para nova versão; aumentar gradualmente | Gestão de tráfego complexo | Direcione o tráfego de volta para estável |
| **Sinalizadores de recursos** | Implantar código, mas ocultar recursos atrás de botões | Complexidade de código a partir de lógica condicional | Desativar |
---

## GitOps
O GitOps leva o IaC à sua conclusão lógica: o repositório Git é a única fonte de verdade para o estado desejado de sua infraestrutura e aplicativos.
| Princípio | Descrição |
|-----------|------------|
| **Declarativo** | Tudo descrito como código (YAML, HCL) |
| **Versionado** | Git é a fonte da verdade |
| **Automatizado** | As ferramentas reconciliam continuamente o estado desejado com o estado real |
| **Auditável** | Cada mudança é um commit do Git |
**ArgoCD** e **Flux** são as principais ferramentas GitOps para Kubernetes. Você envia uma alteração para seu repositório Git e a ferramenta a implanta automaticamente no cluster.
---

## Resposta a Incidentes
Quando algo quebra às 3 da manhã:
1. **Reconhecer** o alerta.
2. **Avaliar o escopo**: quais serviços, usuários e dados são afetados?
3. **Identifique** a causa raiz — verifique logs, métricas e implantações recentes.
4. **Contenha** se possível — disjuntores, sinalizadores de recursos, mudança de tráfego.
5. **Correção** — reversão ou avanço de patch.
6. **Comunicar** — atualizar as partes interessadas e os usuários (página de status).
7. **Post-mortem** — dentro de 24 a 48 horas, documente a causa raiz e os itens de ação.
O objetivo não é apenas resolver o incidente, mas garantir que o mesmo incidente não se repita.