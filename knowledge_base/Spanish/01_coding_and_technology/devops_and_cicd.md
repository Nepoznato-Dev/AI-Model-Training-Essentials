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
# DevOps y CI/CD
DevOps es la combinación de filosofía cultural, prácticas y herramientas que permite a los equipos entregar software de manera más rápida y confiable. Derriba el muro entre los desarrolladores (que quieren implementar cambios) y las operaciones (que quieren estabilidad). CI/CD (integración continua y entrega continua) es la columna vertebral de la automatización que lo hace posible.
---

## Canalizaciones de CI/CD
### Qué significa realmente CI/CD
| Término | Qué hace |
|------|-------------|
| **Integración Continua (CI)** | Los desarrolladores fusionan código con frecuencia; cada fusión desencadena compilaciones y pruebas automatizadas |
| **Entrega continua (CD)** | El código siempre está en un estado desplegable; lanzar a producción es una decisión manual |
| **Implementación continua** | Cada cambio que pasa las pruebas pasa a producción automáticamente, sin puerta manual |
### Etapas típicas de la tubería
| Etapa | Qué pasa | Herramientas |
|-------|-------------|-------|
| **Fuente** | Desarrollador envía código a Git | GitHub, GitLab, Bitbucket |
| **Construir** | Compilar código, instalar dependencias | Maven, Gradle, npm, pip |
| **Prueba** | Unidad de ejecución, integración, comprobaciones de pelusa | Broma, pytest, JUnit |
| **Paquete** | Construir imagen o artefacto de Docker | Docker, paquetes de compilación |
| **Implementar (preparación)** | Implementar en el entorno de ensayo | Kubernetes, ECS, máquinas virtuales |
| **Prueba (puesta en escena)** | Pruebas de integración, pruebas de humo | Selenio, cartero |
| **Implementar (producción)** | Lanzamiento a producción | Azul verdoso, canario, rodante |
| **Monitorizar** | Observar el estado, los errores y el rendimiento | Prometeo, Grafana, Datadog |
### Herramientas CI/CD comparadas
| Herramienta | Tipo | Fuerza |
|------|------|----------|
| **Acciones de GitHub** | CI/CD en la nube | Profundamente integrado con GitHub; Flujos de trabajo YAML |
| **GitLab CI** | CI/CD integrado | Plataforma única para repo + pipeline |
| **Jenkins** | CI/CD autohospedado | Altamente configurable; ecosistema de complementos masivo |
| **CírculoCI** | CI/CD en la nube | Rápido; bueno para flujos de trabajo en contenedores |
| **ArgoCD** | GitOps para Kubernetes | Implementaciones declarativas impulsadas por Git |
---

## Docker y contenedores
### ¿Por qué contenedores?
Antes de los contenedores, el problema clásico era "funciona en mi máquina". Los contenedores resuelven esto empaquetando una aplicación con todas sus dependencias (bibliotecas, tiempo de ejecución, configuración) en una única unidad portátil que se ejecuta de manera idéntica en cualquier lugar.
### Elementos esenciales de Docker
| Concepto | Descripción |
|---------|-------------|
| **Imagen** | Plantilla de solo lectura con aplicación + dependencias |
| **Contenedor** | Instancia en ejecución de una imagen |
| **Archivo Docker** | Receta para construir una imagen |
| **Registro** | Almacenamiento de imágenes (Docker Hub, ECR, GCR) |
| **Volumen** | Almacenamiento persistente que sobrevive a los reinicios de contenedores |
| **Red** | Capa de red aislada para contenedores |
### Mejores prácticas de Dockerfile
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

Prácticas clave: usar imágenes base delgadas/alpinas, ejecutar como no raíz, aprovechar el almacenamiento en caché de capas, usar `.dockerignore`, escanear imágenes en busca de vulnerabilidades (`trivy`, `docker scan`) y establecer límites de recursos.
### Componente acoplable
Para ejecutar varios contenedores juntos (aplicación + base de datos + caché):
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

## Kubernetes (K8)
Kubernetes es el orquestador de contenedores estándar de la industria. Gestiona la implementación, el escalado y el funcionamiento de aplicaciones en contenedores.
### Arquitectura central
| Componente | Rol |
|-----------|--------------|
| **Plano de control** | Gestiona el cluster (servidor API, planificador, etcd, administrador de controladores) |
| **Nodo** | Máquina de trabajo (VM o física) que ejecuta contenedores |
| **Pod** | Unidad desplegable más pequeña; uno o más contenedores que comparten redes |
| **Servicio** | Punto final de red estable que dirige el tráfico a pods |
| **Implementación** | Definición declarativa del estado deseado del pod (réplicas, imagen, etc.) |
| **Ingreso** | Reglas de enrutamiento HTTP para tráfico externo |
| **Mapa de configuración / Secreto** | Configuración y datos confidenciales inyectados en pods |
### Comandos esenciales de kubectl
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

### Timón
Helm es el administrador de paquetes de Kubernetes. Un **gráfico** es un conjunto de recursos de Kubernetes preconfigurados. Piense en ello como`apt`o`brew`para K8.
```bash
helm install my-release bitnami/postgresql   # Install a chart
helm upgrade my-release bitnami/postgresql   # Upgrade
helm rollback my-release 1                   # Rollback to revision 1
helm list                                    # List releases
```

---

## Infraestructura como código (IaC)
IaC trata la configuración de la infraestructura de la misma manera que trata el código de la aplicación: controlada por versión, probada e implementada a través de canalizaciones.
### Terraform frente a Ansible
| Herramienta | Tipo | Enfoque | Mejor para |
|------|------|----------|----------|
| **Terraforma** | Aprovisionamiento | Declarativo (HCL); basado en el estado | Creación de recursos en la nube (VPC, VM, bases de datos) |
| **Ansible** | Configuración | Declarativo (YAML); sin agente | Configuración de servidores, instalación de software |
| **Pulumi** | Aprovisionamiento | Imperativo (Python, Go, TS) | Equipos que prefieren lenguajes de programación reales |
| **Formación de la nube** | Aprovisionamiento | Declarativo (YAML/JSON); Nativo de AWS | Infraestructura exclusiva de AWS |
### Ejemplo de Terraformación
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

Mejores prácticas: use módulos para la reutilización, almacene el estado de forma remota (S3 + DynamoDB para bloquear), nunca codifique secretos y controle las versiones de todo.
---

## Monitoreo y observabilidad
### Los tres pilares
| Pilar | Lo que te dice | Herramientas |
|--------|------------------|-------|
| **Métricas** | Mediciones numéricas a lo largo del tiempo (CPU, tasa de solicitudes, tasa de errores) | Prometeo, CloudWatch, Datadog |
| **Registros** | Eventos discretos con contexto (errores, solicitudes, cambios de estado) | ELK Stack, Loki, Registros de CloudWatch |
| **Rastros** | Viaje de solicitud de un extremo a otro a través de servicios | Jaeger, rayos X, Zipkin |
### Prometeo + Pila de Grafana
La pila de monitoreo estándar de código abierto:
| Componente | Rol |
|-----------|--------------|
| **Prometeo** | Base de datos de series temporales; extrae métricas de los servicios |
| **Gráfana** | Visualización y paneles de control |
| **Administrador de alertas** | Envía alertas a Slack, PagerDuty y correo electrónico |
| **Exportador de nodos** | Expone métricas a nivel del sistema (CPU, RAM, disco) |
| **Exportador de Blackbox** | Puntos finales de sondas (HTTP, TCP, ICMP) |
### Métricas clave para realizar un seguimiento
| Categoría | Métricas |
|----------|---------|
| **Infraestructura** | CPU, RAM, uso de disco, E/S de red |
| **Solicitud** | Tasa de solicitudes, latencia (p50, p95, p99), tasa de errores |
| **Base de datos** | Recuento de consultas, consultas lentas, uso del grupo de conexiones |
| **Negocios** | Registros, conversiones, ingresos |
---

## Estrategias de implementación
| Estrategia | Cómo funciona | Riesgo | Revertir |
|----------|-------------|------|----------|
| **Actualización continua** | Reemplace las instancias antiguas por otras nuevas gradualmente | Algunos usuarios de la versión anterior, otros de la nueva | Volver a la imagen anterior |
| **Azul-Verde** | Ejecute dos entornos idénticos; cambiar el tráfico | Duplicar el costo de la infraestructura durante la transición | Retroceso instantáneo |
| **Canarias** | Dirija un pequeño porcentaje del tráfico a la nueva versión; aumentar gradualmente | Gestión compleja del tráfico | Enrutar el tráfico de regreso al estado estable |
| **Banderas de funciones** | Implementar código pero ocultar funciones detrás de los botones | Complejidad del código a partir de la lógica condicional | Desactivar |
---

## GitOps
GitOps lleva IaC a su conclusión lógica: el repositorio Git es la única fuente de verdad para el estado deseado de su infraestructura y aplicaciones.
| Principio | Descripción |
|-----------|-------------|
| **Declarativo** | Todo lo descrito como código (YAML, HCL) |
| **Versionado** | Git es la fuente de la verdad |
| **Automatizado** | Las herramientas concilian continuamente el estado deseado con el estado real |
| **Auditable** | Cada cambio es un compromiso de Git |
**ArgoCD** y **Flux** son las herramientas GitOps líderes para Kubernetes. Inserta un cambio en su repositorio de Git y la herramienta lo implementa automáticamente en el clúster.
---

## Respuesta a incidentes
Cuando algo se rompe a las 3 a. m.:
1. **Reconocer** la alerta.
2. **Evaluar el alcance**: ¿qué servicios, usuarios y datos se ven afectados?
3. **Identifique** la causa raíz: verifique registros, métricas e implementaciones recientes.
4. **Contener** si es posible: disyuntores, banderas destacadas, cambios de tráfico.
5. **Solución**: revertir o avanzar parches.
6. **Comunicar**: actualice las partes interesadas y los usuarios (página de estado).
7. **Autopsia**: dentro de 24 a 48 horas, documente la causa raíz y las medidas a tomar.
El objetivo no es sólo resolver el incidente sino garantizar que el mismo incidente no se repita.