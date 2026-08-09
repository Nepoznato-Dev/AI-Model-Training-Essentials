---
# Metadatos
título: "Hoja de referencia de Docker y Kubernetes"
descripción: "Docker, Docker Compose, Kubernetes, hoja de referencia de Helm"
categoría: "Referencia rápida"
versión: "1.0.0"
estado: "activo"
# Contribución
autores:
  - nombre: "Equipo de formación del modelo de IA"
    correo electrónico: ""
    rol: "autor_original"
colaboradores: []
registro de cambios:
  - versión: "1.0.0"
    fecha: "2026-08-05"
    autor: "Equipo de formación del modelo de IA"
    cambios: "Se agregaron metadatos de temas frontales de YAML para el seguimiento de los contribuyentes"
# Revisión
creado: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
review_by: "Equipo de la base de conocimientos de referencia rápida"
next_review: "2027-08-05"
# Clasificación
Etiquetas: [acoplador, kubernetes, referencia rápida]
nivel_dificultad: "principiante"
requisitos previos: []
estimado_reading_time: "15 minutos"
# Guía de contribución
contribución:
  licencia: "MIT"
  feedback_channel: "Problemas de GitHub"
  how_to_contribute: "Enviar un PR con cambios y actualizar el registro de cambios"
  review_process: "Los mantenedores de categorías revisan los cambios antes de fusionarlos"
---
# Hoja de referencia de Docker y Kubernetes
Una referencia práctica para contener aplicaciones con Docker y orquestarlas con Kubernetes. Asume una familiaridad básica con la línea de comando.
---

## Fundamentos de Docker
| Concepto | Descripción |
|---------|-------------|
| **Imagen** | Plantilla de solo lectura con código de aplicación + dependencias + bibliotecas de sistema operativo |
| **Contenedor** | Instancia en ejecución de una imagen; proceso aislado |
| **Archivo Docker** | Receta para construir una imagen |
| **Registro** | Almacenamiento de imágenes (Docker Hub, ECR, GCR, GHCR) |
| **Volumen** | Almacenamiento persistente que sobrevive a los reinicios de contenedores |
| **Red** | Red virtual que conecta contenedores |
---

## Comandos esenciales de Docker
### Imágenes
| Comando | Descripción |
|---------|-------------|
| `docker build -t myapp:1.0 .`| Construya una imagen a partir de un Dockerfile |
| `docker images`| Listar imágenes locales |
| `docker pull nginx:latest`| Extraer una imagen de un registro |
| `docker push myrepo/myapp:1.0`| Enviar una imagen a un registro |
| `docker rmi myapp:1.0`| Eliminar una imagen local |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| Etiquetar una imagen para un registro |
| `docker image prune -a`| Eliminar todas las imágenes no utilizadas |
### Contenedores
| Comando | Descripción |
|---------|-------------|
| `docker run -d -p 8080:80 nginx`| Ejecute un contenedor en segundo plano, asigne el puerto 8080→80 |
| `docker run -it ubuntu bash`| Ejecutar interactivamente con un shell |
| `docker run --name web -e DB_HOST=db nginx`| Establecer el nombre del contenedor y la variable de entorno |
| `docker ps`| Listar contenedores en ejecución |
| `docker ps -a`| Listar todos los contenedores (incluidos los detenidos) |
| `docker stop web`| Detener un contenedor en ejecución |
| `docker start web`| Iniciar un contenedor detenido |
| `docker rm web`| Retirar un contenedor detenido |
| `docker exec -it web bash`| Abrir un shell dentro de un contenedor en ejecución |
| `docker logs -f web`| Siga los registros de contenedores |
| `docker inspect web`| Metadatos de contenedor detallados (JSON) |
| `docker stats`| Uso de recursos en vivo para todos los contenedores |
### Limpieza
| Comando | Descripción |
|---------|-------------|
| `docker system prune -a`| Eliminar todos los contenedores, imágenes, redes y caché de compilación no utilizados |
| `docker volume prune`| Eliminar todos los volúmenes no utilizados |
| `docker container prune`| Retire todos los contenedores detenidos |
---

## Referencia del archivo Docker
### Instrucciones comunes
| Instrucción | Propósito | Ejemplo |
|------------|---------|---------|
| `FROM`| Imagen básica | `FROM python:3.12-slim`|
| `WORKDIR`| Establecer directorio de trabajo dentro de la imagen | `WORKDIR /app`|
| `COPY`| Copie archivos del host a la imagen | `COPY requirements.txt .`|
| `ADD`| Como COPY, pero también extrae archivos tar y admite URL | `ADD app.tar.gz /app/`|
| `RUN`| Ejecutar un comando durante la compilación | `RUN pip install -r requirements.txt`|
| `CMD`| Comando predeterminado cuando se inicia el contenedor | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| Comando fijo; CMD se convierte en argumentos | `ENTRYPOINT ["python"]`|
| `ENV`| Establecer variable de entorno | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| Documente en qué puerto escucha la aplicación | `EXPOSE 8000`|
| `ARG`| Variable de tiempo de construcción | `ARG VERSION=1.0`|
| `USER`| Cambiar a usuario no root | `USER appuser`|
| `HEALTHCHECK`| Definir un comando de verificación de estado | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| Crear un punto de montaje | `VOLUME /data`|
### Mejores prácticas
| Práctica | Por qué |
|----------|-----|
| Utilice imágenes delgadas/base | Imágenes más pequeñas = tirones más rápidos, superficie de ataque más pequeña |
| Combine comandos RUN con`&&`| Reduce las capas de la imagen |
| Copie los archivos de dependencia primero, luego codifique | Aprovecha la caché de compilación de Docker |
| Utilice`.dockerignore`| Excluir `node_modules`, `.git`,`__pycache__`|
| Ejecutar como usuario no root | Mejores prácticas de seguridad |
| Utilice compilaciones de varias etapas | Construcción y tiempo de ejecución separados; imagen final más pequeña |
| Versiones de la imagen base de pines | Construcciones reproducibles (`python:3.12.1-slim`, no `python:latest`) |
### Ejemplo de compilación de varias etapas
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

## Componente acoplable
Docker Compose define aplicaciones de múltiples contenedores en un único archivo YAML.
### Comandos clave
| Comando | Descripción |
|---------|-------------|
| `docker compose up -d`| Iniciar todos los servicios en segundo plano |
| `docker compose down`| Detener y retirar contenedores, redes |
| `docker compose down -v`| Eliminar también volúmenes |
| `docker compose logs -f`| Seguir registros de todos los servicios |
| `docker compose ps`| Lista de servicios en ejecución |
| `docker compose build`| Reconstruir imágenes |
| `docker compose exec web bash`| Ejecutar comando en un servicio en ejecución |
| `docker compose pull`| Extraiga las últimas imágenes |
### Ejemplo de archivo de redacción
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

## Arquitectura de Kubernetes
| Componente | Rol |
|-----------|--------------|
| **Clúster** | Un conjunto de nodos (máquinas) que ejecutan aplicaciones en contenedores |
| **Plano de control** | Servidor API, programador, administrador de controladores, etc. (estado del clúster) |
| **Nodo** | Una máquina de trabajo (VM o física) que ejecuta pods |
| **Pod** | Unidad más pequeña; uno o más contenedores estrechamente acoplados |
| **Implementación** | Gestiona réplicas de un pod; maneja actualizaciones continuas |
| **Servicio** | Punto final de red estable para un conjunto de pods |
| **Ingreso** | Enrutamiento HTTP desde fuera del clúster a servicios |
| **Mapa de configuración** | Datos de configuración no secretos |
| **Secreto** | Datos confidenciales (codificados en base64) |
| **Espacio de nombres** | Aislamiento lógico dentro de un clúster |
| **Volumen persistente (PV)** | Recurso de almacenamiento a nivel de clúster |
| **Reclamación de volumen persistente (PVC)** | Solicitud de almacenamiento por pod |
---

## Comandos kubectl
### Información del clúster
| Comando | Descripción |
|---------|-------------|
| `kubectl cluster-info`| Detalles del punto final del clúster |
| `kubectl get nodes`| Listar todos los nodos |
| `kubectl get namespaces`| Listar espacios de nombres |
| `kubectl config current-context`| Mostrar el contexto actual del clúster |
| `kubectl config use-context prod`| Cambiar contexto |
### Cargas de trabajo
| Comando | Descripción |
|---------|-------------|
| `kubectl get pods`| Listar pods en el espacio de nombres actual |
| `kubectl get pods -A`| Listar pods en todos los espacios de nombres |
| `kubectl get deployments`| Listar implementaciones |
| `kubectl get services`| Listar servicios |
| `kubectl get ingress`| Listar recursos de ingreso |
| `kubectl describe pod <name>`| Información detallada del pod (eventos, estado, especificaciones) |
| `kubectl logs <pod>`| Ver registros de pods |
| `kubectl logs -f <pod>`| Seguir los registros del pod |
| `kubectl logs <pod> -c <container>`| Registros de un contenedor específico en un pod de múltiples contenedores |
| `kubectl exec -it <pod> -- bash`| Cáscara en una vaina |
| `kubectl delete pod <name>`| Eliminar un pod (su controlador lo recreará) |
| `kubectl rollout status deployment/<name>`| Verifique el progreso de la implementación |
| `kubectl rollout undo deployment/<name>`| Volver a la versión anterior |
### Aplicando configuración
| Comando | Descripción |
|---------|-------------|
| `kubectl apply -f deployment.yaml`| Aplicar un manifiesto YAML |
| `kubectl apply -f ./dir/`| Aplicar todos los archivos YAML en un directorio |
| `kubectl delete -f deployment.yaml`| Eliminar recursos definidos en un archivo YAML |
| `kubectl scale deployment/web --replicas=5`| Escalar una implementación |
| `kubectl set image deployment/web web=myapp:2.0`| Actualizar imagen del contenedor |
---

## Manifiestos comunes de Kubernetes
### Implementación
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

### Servicio
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

### Ingreso
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

## Conceptos básicos del timón
Helm es el administrador de paquetes de Kubernetes. Empaqueta los recursos de Kubernetes en gráficos reutilizables.
| Comando | Descripción |
|---------|-------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| Agregar un repositorio de gráficos |
| `helm repo update`| Actualizar el índice del gráfico local |
| `helm search repo nginx`| Buscar un gráfico |
| `helm install my-release bitnami/nginx`| Instalar un gráfico |
| `helm install my-release bitnami/nginx --set replicaCount=3`| Instalar con valores personalizados |
| `helm install my-release bitnami/nginx -f values.yaml`| Instalar con un archivo de valores |
| `helm list`| Listar versiones instaladas |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| Actualizar una versión |
| `helm rollback my-release 1`| Retroceder a una revisión anterior |
| `helm uninstall my-release`| Desinstalar una versión |
| `helm status my-release`| Mostrar estado de lanzamiento |
---

## Referencia rápida para solucionar problemas
| Problema | Comandos para probar |
|---------|----------------|
| El módulo no arranca | `kubectl describe pod <name>`→ comprobar Eventos |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ vea por qué falló |
| Error al extraer la imagen | Verifique el nombre de la imagen, la etiqueta y las credenciales de registro |
| Servicio no accesible | `kubectl get endpoints <service>`→ ¿se han seleccionado los pods? |
| OOM asesinado | Aumente los límites de memoria u optimice el uso de memoria de la aplicación |
| Grupos pendientes | `kubectl describe pod`→ verificar recursos de nodo, contaminación, afinidad |
| Problemas de DNS | `kubectl exec <pod> -- nslookup kubernetes.default`|