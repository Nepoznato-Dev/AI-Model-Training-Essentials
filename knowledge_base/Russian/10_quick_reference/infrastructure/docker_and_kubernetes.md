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

# Шпаргалка по Docker и Kubernetes
Практическое руководство по контейнеризации приложений с помощью Docker и их оркестрации с помощью Kubernetes. Предполагается базовое знакомство с командной строкой.
---

## Основы Docker
| Концепция | Описание |
|---------|-------------|
| **Изображение** | Доступный только для чтения шаблон с кодом приложения + зависимостями + библиотеками ОС |
| **Контейнер** | Запуск экземпляра изображения; изолированный процесс |
| **Докерфайл** | Рецепт создания имиджа |
| **Реестр** | Хранилище для образов (Docker Hub, ECR, GCR, GHCR) |
| **Объем** | Постоянное хранилище, выдерживающее перезапуск контейнера |
| **Сеть** | Виртуальная сеть, соединяющая контейнеры |
---

## Основные команды Docker
### Изображения
| Команда | Описание |
|---------|-------------|
| `docker build -t myapp:1.0 .`| Создайте образ из Dockerfile |
| `docker images`| Список локальных изображений |
| `docker pull nginx:latest`| Вытащить образ из реестра |
| `docker push myrepo/myapp:1.0`| Отправить образ в реестр |
| `docker rmi myapp:1.0`| Удалить локальное изображение |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| Пометить изображение для реестра |
| `docker image prune -a`| Удалить все неиспользуемые изображения |
### Контейнеры
| Команда | Описание |
|---------|-------------|
| `docker run -d -p 8080:80 nginx`| Запустите контейнер в фоновом режиме, выберите порт 8080→80 |
| `docker run -it ubuntu bash`| Запуск в интерактивном режиме с помощью оболочки |
| `docker run --name web -e DB_HOST=db nginx`| Установить имя контейнера и переменную среды |
| `docker ps`| Список запущенных контейнеров |
| `docker ps -a`| Список всех контейнеров (включая остановленные) |
| `docker stop web`| Остановить работающий контейнер |
| `docker start web`| Запустить остановленный контейнер |
| `docker rm web`| Удалить остановленный контейнер |
| `docker exec -it web bash`| Открытие оболочки внутри работающего контейнера |
| `docker logs -f web`| Следите за журналами контейнеров |
| `docker inspect web`| Подробные метаданные контейнера (JSON) |
| `docker stats`| Использование ресурсов в реальном времени для всех контейнеров |
### Очистка
| Команда | Описание |
|---------|-------------|
| `docker system prune -a`| Удалите все неиспользуемые контейнеры, изображения, сети и создайте кеш |
| `docker volume prune`| Удалить все неиспользуемые тома |
| `docker container prune`| Удалить все остановленные контейнеры |
---

## Справочник по файлам Docker
### Общие инструкции
| Инструкция | Цель | Пример |
|-------------|---------|---------|
| `FROM`| Базовое изображение | `FROM python:3.12-slim`|
| `WORKDIR`| Установить рабочий каталог внутри изображения | `WORKDIR /app`|
| `COPY`| Копирование файлов с хоста в образ | `COPY requirements.txt .`|
| `ADD`| Как COPY, но также извлекает файлы tar и поддерживает URL-адреса | `ADD app.tar.gz /app/`|
| `RUN`| Выполнить команду во время сборки | `RUN pip install -r requirements.txt`|
| `CMD`| Команда по умолчанию при запуске контейнера | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| Фиксированная команда; CMD становится аргументом | `ENTRYPOINT ["python"]`|
| `ENV`| Установить переменную среды | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| Документ, какой порт прослушивает приложение | `EXPOSE 8000`|
| `ARG`| Переменная времени сборки | `ARG VERSION=1.0`|
| `USER`| Переключиться на пользователя без полномочий root | `USER appuser`|
| `HEALTHCHECK`| Определить команду проверки работоспособности | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| Создать точку монтирования | `VOLUME /data`|
### Лучшие практики
| Практика | Почему |
|----------|-----|
| Используйте тонкие/базовые изображения | Меньшие изображения = более быстрые запросы, меньшая поверхность атаки |
| Объедините команды RUN с`&&`| Уменьшает слои изображения |
| Сначала скопируйте файлы зависимостей, затем код | Использует кэш сборки Docker |
| Используйте`.dockerignore`| Исключить `node_modules`, `.git`,`__pycache__`|
| Запуск от имени пользователя без полномочий root | Лучшие практики безопасности |
| Используйте многоэтапные сборки | Отдельная среда сборки и выполнения; окончательное изображение меньшего размера |
| Версии базового изображения Pin | Воспроизводимые сборки (`python:3.12.1-slim`, а не`python:latest`) |
### Пример многоэтапной сборки
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

## Docker Compose
Docker Compose определяет многоконтейнерные приложения в одном файле YAML.
### Ключевые команды
| Команда | Описание |
|---------|-------------|
| `docker compose up -d`| Запустить все службы в фоновом режиме |
| `docker compose down`| Остановить и удалить контейнеры, сети |
| `docker compose down -v`| Также удалите тома |
| `docker compose logs -f`| Следите за логами всех сервисов |
| `docker compose ps`| Список запущенных сервисов |
| `docker compose build`| Восстановить изображения |
| `docker compose exec web bash`| Запустить команду в работающей службе |
| `docker compose pull`| Вытащить последние изображения |
### Пример создания файла
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

## Архитектура Кубернетеса
| Компонент | Роль |
|-----------|------|
| **Кластер** | Набор узлов (машин), на которых выполняются контейнерные приложения |
| **Плоскость управления** | API-сервер, планировщик, диспетчер контроллеров и т. д. (состояние кластера) |
| **Узел** | Рабочая машина (виртуальная или физическая), на которой работают модули |
| **Капсула** | Самая маленькая единица; один или несколько плотно связанных контейнеров |
| **Развертывание** | Управляет репликами модуля; обрабатывает постоянные обновления |
| **Сервис** | Стабильная конечная точка сети для набора модулей |
| **Вход** | HTTP-маршрутизация из-за пределов кластера к службам |
| **Карта конфигурации** | Несекретные данные конфигурации |
| **Секрет** | Конфиденциальные данные (в кодировке Base64) |
| **Пространство имен** | Логическая изоляция внутри кластера |
| **Постоянный объем (PV)** | Ресурс хранения на уровне кластера |
| **PersistentVolumeClaim (PVC)** | Запрос на хранение по капсуле |
---

## команды kubectl
### Информация о кластере
| Команда | Описание |
|---------|-------------|
| `kubectl cluster-info`| Сведения о конечной точке кластера |
| `kubectl get nodes`| Список всех узлов |
| `kubectl get namespaces`| Список пространств имен |
| `kubectl config current-context`| Показать текущий контекст кластера |
| `kubectl config use-context prod`| Переключить контекст |
### Рабочие нагрузки
| Команда | Описание |
|---------|-------------|
| `kubectl get pods`| Список модулей в текущем пространстве имен |
| `kubectl get pods -A`| Получение списка модулей во всех пространствах имен |
| `kubectl get deployments`| Получение списка развертываний |
| `kubectl get services`| Список услуг |
| `kubectl get ingress`| Список входящих ресурсов |
| `kubectl describe pod <name>`| Подробная информация о модуле (события, статус, характеристики) |
| `kubectl logs <pod>`| Просмотр журналов модулей |
| `kubectl logs -f <pod>`| Следите за журналами модулей |
| `kubectl logs <pod> -c <container>`| Журналы из определенного контейнера в многоконтейнерном модуле |
| `kubectl exec -it <pod> -- bash`| Оболочка в капсулу |
| `kubectl delete pod <name>`| Удалить под (он будет воссоздан его контроллером) |
| `kubectl rollout status deployment/<name>`| Проверьте ход внедрения |
| `kubectl rollout undo deployment/<name>`| Откат к предыдущей версии |
### Применение конфигурации
| Команда | Описание |
|---------|-------------|
| `kubectl apply -f deployment.yaml`| Применить манифест YAML |
| `kubectl apply -f ./dir/`| Применить все файлы YAML в каталоге |
| `kubectl delete -f deployment.yaml`| Удаление ресурсов, определенных в файле YAML |
| `kubectl scale deployment/web --replicas=5`| Масштабирование развертывания |
| `kubectl set image deployment/web web=myapp:2.0`| Обновить образ контейнера |
---

## Общие манифесты Kubernetes
### Развертывание
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

### Услуга
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

### Вход
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

## Основы управления шлемом
Helm — менеджер пакетов Kubernetes. Он упаковывает ресурсы Kubernetes в многоразовые диаграммы.
| Команда | Описание |
|---------|-------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| Добавить репозиторий диаграмм |
| `helm repo update`| Обновить индекс локального графика |
| `helm search repo nginx`| Поиск диаграммы |
| `helm install my-release bitnami/nginx`| Установить график |
| `helm install my-release bitnami/nginx --set replicaCount=3`| Установить с пользовательскими значениями |
| `helm install my-release bitnami/nginx -f values.yaml`| Установить с помощью файла значений |
| `helm list`| Список установленных выпусков |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| Обновить выпуск |
| `helm rollback my-release 1`| Откат к предыдущей версии |
| `helm uninstall my-release`| Удалить выпуск |
| `helm status my-release`| Показать статус выпуска |
---

## Краткое руководство по устранению неполадок
| Проблема | Команды, которые стоит попробовать |
|---------|----------------|
| Pod не запускается | `kubectl describe pod <name>`→ проверить События |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ узнайте, почему произошел сбой |
| Ошибка получения изображения | Проверьте имя образа, тег и учетные данные реестра |
| Сервис недоступен | `kubectl get endpoints <service>`→ выбраны ли модули? |
| ООМУбит | Увеличьте лимиты памяти или оптимизируйте использование памяти приложениями |
| Ожидающие модули | `kubectl describe pod`→ проверить ресурсы узла, помехи, сходство |
| Проблемы с DNS | `kubectl exec <pod> -- nslookup kubernetes.default`|