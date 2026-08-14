<!--
---
# Metadata
title: "Docker and Kubernetes Cheat Sheet"
description: "Docker, Docker Compose, Kubernetes, Helm cheat sheet"
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
tags: [docker, kubernetes, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "15 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Folha de dicas do Docker e Kubernetes
Uma referência prática para conteinerizar aplicações com Docker e orquestrá-las com Kubernetes. Pressupõe familiaridade básica com a linha de comando.
---

## Fundamentos do Docker
| Conceito | Descrição |
|--------|-------------|
| **Imagem** | Modelo somente leitura com código do aplicativo + dependências + bibliotecas de sistema operacional |
| **Contêiner** | Executando instância de uma imagem; processo isolado |
| **Dockerfile** | Receita para construir uma imagem |
| **Registro** | Armazenamento para imagens (Docker Hub, ECR, GCR, GHCR) |
| **Volume** | Armazenamento persistente que sobrevive a reinicializações de contêineres |
| **Rede** | Rede virtual conectando contêineres |
---

## Comandos essenciais do Docker
### Imagens
| Comando | Descrição |
|--------|-------------|
| `docker build -t myapp:1.0 .`| Construir uma imagem a partir de um Dockerfile |
| `docker images`| Listar imagens locais |
| `docker pull nginx:latest`| Extrair uma imagem de um registro |
| `docker push myrepo/myapp:1.0`| Enviar uma imagem para um registro |
| `docker rmi myapp:1.0`| Remover uma imagem local |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| Marcar uma imagem para um registro |
| `docker image prune -a`| Remova todas as imagens não utilizadas |
### Contêineres
| Comando | Descrição |
|--------|-------------|
| `docker run -d -p 8080:80 nginx`| Execute um contêiner em segundo plano, mapeie a porta 8080→80 |
| `docker run -it ubuntu bash`| Execute interativamente com um shell |
| `docker run --name web -e DB_HOST=db nginx`| Defina o nome do contêiner e a variável de ambiente |
| `docker ps`| Listar contêineres em execução |
| `docker ps -a`| Listar todos os contentores (incluindo os parados) |
| `docker stop web`| Pare um contêiner em execução |
| `docker start web`| Iniciar um contêiner parado |
| `docker rm web`| Remover um contêiner parado |
| `docker exec -it web bash`| Abra um shell dentro de um contêiner em execução |
| `docker logs -f web`| Siga os registros do contêiner |
| `docker inspect web`| Metadados detalhados do contêiner (JSON) |
| `docker stats`| Uso de recursos ativos para todos os contêineres |
### Limpar
| Comando | Descrição |
|--------|-------------|
| `docker system prune -a`| Remova todos os contêineres, imagens, redes não utilizados e crie cache |
| `docker volume prune`| Remova todos os volumes não utilizados |
| `docker container prune`| Remover todos os contêineres parados |
---

## Referência do Dockerfile
### Instruções Comuns
| Instrução | Finalidade | Exemplo |
|---------|---------|---------|
| `FROM`| Imagem base | `FROM python:3.12-slim`|
| `WORKDIR`| Defina o diretório de trabalho dentro da imagem | `WORKDIR /app`|
| `COPY`| Copie arquivos do host para a imagem | `COPY requirements.txt .`|
| `ADD`| Gosta de COPY, mas também extrai tars e suporta URLs | `ADD app.tar.gz /app/`|
| `RUN`| Execute um comando durante a construção | `RUN pip install -r requirements.txt`|
| `CMD`| Comando padrão quando o contêiner é iniciado | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| Comando fixo; CMD vira argumento | `ENTRYPOINT ["python"]`|
| `ENV`| Definir variável de ambiente | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| Documente em qual porta o aplicativo escuta | `EXPOSE 8000`|
| `ARG`| Variável de tempo de construção | `ARG VERSION=1.0`|
| `USER`| Mudar para usuário não root | `USER appuser`|
| `HEALTHCHECK`| Definir um comando de verificação de integridade | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| Crie um ponto de montagem | `VOLUME /data`|
### Melhores Práticas
| Prática | Por que |
|----------|-----|
| Use imagens finas/base | Imagens menores = pulls mais rápidos, superfície de ataque menor |
| Combine comandos RUN com`&&`| Reduz camadas de imagem |
| Copie os arquivos de dependência primeiro e depois codifique | Aproveita o cache de compilação do Docker |
| Usar`.dockerignore`| Excluir`node_modules`,`.git`,`__pycache__`|
| Executar como usuário não root | Melhores práticas de segurança |
| Use compilações de vários estágios | Construção e tempo de execução separados; imagem final menor |
| Fixar versões da imagem base | Construções reproduzíveis (`python:3.12.1-slim`, não`python:latest`) |
### Exemplo de construção em vários estágios
```dockerfile
# Build stage
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# Production stage
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/main.js"]
```

---

## Docker Compor
Docker Compose define aplicativos de vários contêineres em um único arquivo YAML.
### Comandos de teclas
| Comando | Descrição |
|--------|-------------|
| `docker compose up -d`| Inicie todos os serviços em segundo plano |
| `docker compose down`| Parar e remover contêineres, redes |
| `docker compose down -v`| Remova também volumes |
| `docker compose logs -f`| Acompanhe os logs de todos os serviços |
| `docker compose ps`| Listar serviços em execução |
| `docker compose build`| Reconstruir imagens |
| `docker compose exec web bash`| Executar comando em um serviço em execução |
| `docker compose pull`| Puxe as imagens mais recentes |
### Exemplo de arquivo de composição
```yaml
services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://user:pass@db:5432/mydb
      - REDIS_URL=redis://cache:6379
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_started
    restart: unless-stopped

  db:
    image: postgres:16-alpine
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 5s
      timeout: 5s
      retries: 5

  cache:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  pgdata:
```

---

## Arquitetura Kubernetes
| Componente | Função |
|-----------|------|
| **Aglomerado** | Um conjunto de nós (máquinas) executando aplicativos em contêineres |
| **Plano de Controle** | Servidor API, agendador, gerenciador de controlador, etcd (estado do cluster) |
| **Nó** | Uma máquina de trabalho (VM ou física) que executa pods |
| **Vagem** | Unidade menor; um ou mais contentores fortemente acoplados |
| **Implantação** | Gerencia réplicas de um pod; lida com atualizações contínuas |
| **Serviço** | Endpoint de rede estável para um conjunto de pods |
| **Entrada** | Roteamento HTTP de fora do cluster para serviços |
| **ConfigMap** | Dados de configuração não secretos |
| **Segredo** | Dados confidenciais (codificados em base64) |
| **Espaço para nome** | Isolamento lógico dentro de um cluster |
| **Volume Persistente (PV)** | Recurso de armazenamento em nível de cluster |
| **PersistentVolumeClaim (PVC)** | Solicitação de armazenamento por pod |
---

## Comandos kubectl
### Informações do cluster
| Comando | Descrição |
|--------|-------------|
| `kubectl cluster-info`| Detalhes do endpoint do cluster |
| `kubectl get nodes`| Listar todos os nós |
| `kubectl get namespaces`| Listar namespaces |
| `kubectl config current-context`| Mostrar contexto atual do cluster |
| `kubectl config use-context prod`| Mudar contexto |
### Cargas de trabalho
| Comando | Descrição |
|--------|-------------|
| `kubectl get pods`| Listar pods no namespace atual |
| `kubectl get pods -A`| Listar pods em todos os namespaces |
| `kubectl get deployments`| Listar implantações |
| `kubectl get services`| Listar serviços |
| `kubectl get ingress`| Listar recursos de entrada |
| `kubectl describe pod <name>`| Informações detalhadas do pod (eventos, status, especificações) |
| `kubectl logs <pod>`| Ver registros de pod |
| `kubectl logs -f <pod>`| Siga os registros do pod |
| `kubectl logs <pod> -c <container>`| Logs de um contêiner específico em um pod de vários contêineres |
| `kubectl exec -it <pod> -- bash`| Shell em um pod |
| `kubectl delete pod <name>`| Exclua um pod (ele será recriado por seu controlador) |
| `kubectl rollout status deployment/<name>`| Verifique o progresso da implementação |
| `kubectl rollout undo deployment/<name>`| Reverter para a versão anterior |
### Aplicando configuração
| Comando | Descrição |
|--------|-------------|
| `kubectl apply -f deployment.yaml`| Aplicar um manifesto YAML |
| `kubectl apply -f ./dir/`| Aplicar todos os arquivos YAML em um diretório |
| `kubectl delete -f deployment.yaml`| Excluir recursos definidos em um arquivo YAML |
| `kubectl scale deployment/web --replicas=5`| Dimensionar uma implantação |
| `kubectl set image deployment/web web=myapp:2.0`| Atualizar imagem do contêiner |
---

## Manifestos comuns do Kubernetes
### Implantação
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
  labels:
    app: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: myapp:1.0
        ports:
        - containerPort: 8080
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 15
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
```

### Serviço
```yaml
apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 8080
  type: ClusterIP    # Internal only
  # type: LoadBalancer  # External (cloud provider)
  # type: NodePort      # External via node IP + port
```

### Entrada
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web
            port:
              number: 80
```

---

## Noções básicas do leme
Helm é o gerenciador de pacotes do Kubernetes. Ele empacota recursos do Kubernetes em gráficos reutilizáveis.
| Comando | Descrição |
|--------|-------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| Adicionar um repositório de gráficos |
| `helm repo update`| Atualizar índice gráfico local |
| `helm search repo nginx`| Procure um gráfico |
| `helm install my-release bitnami/nginx`| Instale um gráfico |
| `helm install my-release bitnami/nginx --set replicaCount=3`| Instalar com valores personalizados |
| `helm install my-release bitnami/nginx -f values.yaml`| Instale com um arquivo de valores |
| `helm list`| Listar versões instaladas |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| Atualizar uma versão |
| `helm rollback my-release 1`| Reverter para uma revisão anterior |
| `helm uninstall my-release`| Desinstalar uma versão |
| `helm status my-release`| Mostrar status de lançamento |
---

## Referência rápida para solução de problemas
| Problema | Comandos para experimentar |
|--------|----------------|
| O pod não inicia | `kubectl describe pod <name>`→ verificar eventos |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ veja porque travou |
| Erro de extração de imagem | Verifique o nome da imagem, tag e credenciais de registro |
| Serviço não acessível | `kubectl get endpoints <service>`→ os pods estão selecionados? |
| OOMmorto | Aumente os limites de memória ou otimize o uso de memória do aplicativo |
| Pods pendentes | `kubectl describe pod`→ verificar recursos do nó, taints, afinidade |
| Problemas de DNS | `kubectl exec <pod> -- nslookup kubernetes.default`|