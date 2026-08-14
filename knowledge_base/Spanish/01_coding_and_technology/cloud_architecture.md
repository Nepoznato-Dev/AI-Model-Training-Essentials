---
# Metadata
title: "Cloud Architecture"
description: "Cloud providers, architecture patterns, security"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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
# Arquitectura de la nube
La computación en la nube ha cambiado fundamentalmente la forma en que las organizaciones crean, implementan y escalan software. En lugar de comprar y mantener servidores físicos, puede aprovisionar recursos informáticos según demanda, pagar por lo que utiliza y escalar globalmente en minutos. Este archivo cubre los conceptos básicos, patrones de arquitectura, servicios y mejores prácticas que necesita conocer.
---

## Fundamentos de la computación en la nube
### ¿Qué es la computación en la nube?
Entrega bajo demanda de recursos informáticos (servidores, almacenamiento, bases de datos, redes, software) a través de Internet con precios de pago por uso.
### Características esenciales del NIST
| Característica | Significado |
|---------------|---------|
| **Autoservicio bajo demanda** | Provisión de recursos sin interacción humana |
| **Amplio acceso a la red** | Disponible en la red mediante mecanismos estándar |
| **Agrupación de recursos** | Modelo multiinquilino; recursos asignados dinámicamente |
| **Elasticidad rápida** | Escale hacia afuera y hacia adentro rápidamente |
| **Servicio medido** | El uso es monitoreado y facturado |
### Modelos de implementación
| Modelo | Descripción | Cuándo utilizar |
|-------|-------------|-------------|
| **Nube pública** | Propiedad de proveedores; infraestructura compartida (AWS, Azure, GCP) | La mayoría de las cargas de trabajo; rentable |
| **Nube privada** | Dedicado a una sola organización | Requisitos reglamentarios, datos sensibles |
| **Nube híbrida** | Combinación de público y privado | Flexibilidad + cumplimiento |
| **Nube múltiple** | Uso de múltiples proveedores de nube pública | Evite la dependencia del proveedor, el mejor de su clase |
### Modelos de servicio
| Modelo | Proporciona | Ejemplos | Casos de uso |
|-------|----------|----------|-----------|
| **IaaS** | VM, almacenamiento, redes, SO | AWS EC2, máquinas virtuales de Azure, GCP Compute Engine | Migraciones de tipo lift-and-shift, control total |
| **PaaS** | Plataformas de desarrollo, bases de datos, middleware | Heroku, Google App Engine, AWS Elastic Beanstalk | Desarrollo de aplicaciones, implementación de API |
| **SaaS** | Solicitudes completas a través de Internet | Salesforce, Google Workspace, Microsoft 365 | Correo electrónico, CRM, colaboración |
| **FaaS/Sin servidor** | Ejecución de funciones controladas por eventos | AWS Lambda, Funciones de Azure, Funciones de nube de GCP | API, procesamiento de eventos, tareas programadas |
---

## Principales proveedores de nube
| Proveedor | Cuota de mercado | Fortalezas |
|----------|-------------|-----------|
| **AWS** | ~32% | Catálogo de servicios más amplio, ecosistema más grande |
| **Azul** | ~23% | Integración empresarial, nube híbrida, pila de Microsoft |
| **PCG** | ~10% | Análisis de datos, IA/ML, Kubernetes |
| **Nube de Alibaba** | ~4% | Dominante en Asia-Pacífico |
| **Nube de Oráculo** | ~2% | Cargas de trabajo de bases de datos, aplicaciones empresariales |
| **Nube de IBM** | ~2% | Enfoque empresarial, Watson AI |
| **Océano Digital** | Nicho | Ofertas simplificadas y fáciles de usar para desarrolladores |
### Comparación de servicios (3 proveedores principales)
| Categoría | AWS | Azul | PCG |
|----------|-----|-------|-----|
| **Calcular** | EC2, Lambda, ECS | VM, funciones, AKS | Compute Engine, Funciones en la nube, GKE |
| **Almacenamiento** | S3, EBS, Glaciar | Almacenamiento de blobs, almacenamiento en disco | Almacenamiento en la nube, disco persistente |
| **Base de datos** | RDS, DynamoDB, Aurora | Base de datos SQL, Cosmos DB | Nube SQL, Firestore, Bigtable |
| **Análisis** | Desplazamiento al rojo, EMR | Sinapsis, ladrillos de datos | BigQuery, flujo de datos |
| **IA/ML** | SageMaker, Reconocimiento | Azure ML, servicios cognitivos | Vértice AI, AutoML |
| **Redes** | VPC, Ruta 53, CloudFront | VNet, administrador de tráfico | VPC, DNS en la nube, CDN en la nube |
---

## Patrones de arquitectura
### Marco bien diseñado
Los tres proveedores principales publican marcos bien diseñados construidos en torno a cinco pilares:
| Pilar | Principios clave |
|--------|---------------|
| **Excelencia operativa** | Automatizar operaciones; realizar cambios frecuentes y reversibles; anticipar el fracaso |
| **Seguridad** | Base de identidad sólida; aplicar seguridad en cada capa; proteger los datos en tránsito y en reposo |
| **Confiabilidad** | Procedimientos de recuperación de pruebas; recuperación automática de fallas; escalar horizontalmente |
| **Eficiencia de rendimiento** | Utilice sin servidor; globalícese en minutos; experimentar a menudo |
| **Optimización de costos** | Adoptar modelo de consumo; utilizar servicios gestionados; dejar de gastar en trabajo indiferenciado |
### Patrones comunes
| Patrón | Descripción | Beneficios | Desafíos |
|---------|-------------|----------|------------|
| **Microservicios** | Descomponer la aplicación en servicios pequeños e independientes | Escalabilidad, aislamiento de fallas, implementación independiente | Complejidad distribuida, coherencia de datos |
| **Basado en eventos** | Los componentes se comunican a través de eventos | Acoplamiento flexible, procesamiento en tiempo real | Complejidad de depuración, coherencia eventual |
| **Sin servidor** | Sin gestión de servidores; pago por ejecución | Rentabilidad, despliegue rápido | Arranques en frío, dependencia de proveedores, límites de ejecución |
| **En capas (N-Nivel)** | Presentación → Lógica de negocios → Acceso a datos → Base de datos | Separación de preocupaciones, mantenibilidad | Puede volverse monolítico |
| **Basado en el espacio** | Datos distribuidos entre nodos de memoria virtualizados | Maneja alta concurrencia, baja latencia | Complejo de diseñar y gestionar |
---

## Servicios principales
### Calcular
| Tipo de servicio | Detalles |
|-------------|---------|
| **Máquinas virtuales** | GPU de uso general, optimizada para computación y para memoria. Precios: bajo demanda, reservado, al contado. |
| **Contenedores** | Tiempo de ejecución de Docker; Orquestación a través de Kubernetes (EKS, AKS, GKE). Registros: ECR, GCR, ACR. |
| **Funciones sin servidor** | Activado por evento, sin estado. Límites de tiempo de ejecución, memoria, concurrencia. |
### Almacenamiento
| Tipo | Características | Ejemplos | Mejor para |
|------|----------------|----------|----------|
| **Objeto** | Estructura plana, acceso HTTP, rico en metadatos | S3, almacenamiento en la nube, Azure Blob | Activos estáticos, copias de seguridad, lagos de datos |
| **Bloquear** | Volúmenes sin procesar adjuntos a máquinas virtuales | EBS, disco persistente, discos Azure | Bases de datos, volúmenes de arranque |
| **Archivo** | Sistemas de archivos compartidos (NFS/SMB) | EFS, almacén de archivos, archivos de Azure | Gestión de contenidos, configuraciones compartidas |
| **Archivo** | Menor costo, demoras en la recuperación | Glaciar S3, Archivo Azul | Cumplimiento, copias de seguridad a largo plazo |
### Bases de datos
| Categoría | Servicios | Caso de uso |
|----------|----------|----------|
| **Relacional gestionado** | RDS, Nube SQL, Azure SQL | Aplicaciones tradicionales, transacciones ACID |
| **NoSQL — Documento** | DocumentDB, Firestore, Cosmos DB | Esquemas flexibles, datos JSON |
| **NoSQL — Valor-clave** | DynamoDB, caché de Redis | Almacenamiento en caché, sesiones, búsquedas simples |
| **NoSQL: columna ancha** | Mesa grande, Cassandra | Serie temporal con mucha escritura |
| **NoSQL — Gráfico** | Neptuno, Cosmos DB (API de gráficos) | Relaciones, redes sociales |
| **Almacenamiento de datos** | Copo de nieve, desplazamiento al rojo, BigQuery, Synapse | Análisis, BI |
| **Almacenamiento en caché** | ElastiCache, almacén de memoria en la nube | Almacenamiento de sesiones, almacenamiento en caché de consultas |
---

## Redes
### Redes virtuales
Cada implementación de nube se encuentra dentro de una nube privada virtual (VPC/VNet): una red aislada que usted define con bloques CIDR, subredes (públicas o privadas), tablas de rutas y puertas de enlace.
### Equilibrio de carga y CDN
| Servicio | Propósito |
|---------|---------|
| **Equilibradores de carga** | Distribuir el tráfico entre instancias (red L4, aplicación L7) |
| **CDN** | Almacenar en caché el contenido en ubicaciones perimetrales para reducir la latencia (CloudFront, Cloud CDN, Azure CDN) |
| **DNS** | Registro de dominio, políticas de enrutamiento, comprobaciones de estado (Route 53, Cloud DNS, Azure DNS) |
### Opciones de conectividad
| Opción | Descripción |
|--------|-------------|
| **Puerta de enlace a Internet** | Acceso público a Internet para VPC |
| **Puerta de enlace NAT** | Acceso saliente a subred privada |
| **VPN** | Túneles cifrados hacia las instalaciones |
| **Conexión directa/ExpressRoute** | Conexiones privadas dedicadas |
| **Emparejamiento de VPC** | Conecte VPC dentro o entre cuentas |
---

## Seguridad
### Modelo de responsabilidad compartida
| Capa | Proveedor | Cliente |
|-------|----------|----------|
| **Infraestructura** (hardware, instalaciones) | ✅ | |
| **Informática, almacenamiento, redes** | ✅ (gestionado) | ✅ (autogestionado) |
| **Datos, Aplicaciones, Identidad** | | ✅ |
Cuanto más gestionado es el servicio, más maneja el proveedor. Con IaaS gestionas casi todo; con SaaS, el proveedor se encarga de casi todo.
### Gestión de identidad y acceso (IAM)
| Concepto | Descripción |
|---------|-------------|
| **Usuarios** | Identidades individuales |
| **Grupos** | Colecciones de usuarios |
| **Funciones** | Credenciales temporales para servicios o usuarios |
| **Políticas** | Documentos que definen permisos |
| **Principio** | Mínimo privilegio, separación de funciones |
### Protección de datos
- **Cifrado en reposo**: KMS, claves administradas por el cliente, HSM.
- **Cifrado en tránsito**: TLS/SSL, HTTPS.
- **Gestión de secretos**: Secrets Manager, Key Vault: nunca codifique secretos.
---

## DevOps en la nube
### Infraestructura como código (IaC)
| Herramienta | Descripción |
|------|-------------|
| **Terraforma** | Multinube, HCL declarativa, gestión estatal |
| **Formación de la nube** | Plantillas YAML/JSON nativas de AWS |
| **Plantillas ARM / Bíceps** | Nativo de Azure |
| **Pulumi** | Infraestructura utilizando lenguajes de programación (Python, Go, etc.) |
### Servicios de CI/CD
| Proveedor | Herramientas |
|----------|-------|
| **AWS** | CodePipeline, CodeBuild, CodeDeploy |
| **Azul** | Azure DevOps, acciones de GitHub |
| **PCG** | Creación de nube, implementación de nube |
| **Tercero** | Jenkins, CircleCI, GitLabCI |
### Monitoreo y observabilidad
| Capacidad | AWS | Azul | PCG |
|-----------|-----|-------|-----|
| **Métricas** | Vigilancia de la nube | Monitor de Azure | Monitoreo de la nube |
| **Registro** | Registros de CloudWatch | Análisis de registros | Registro en la nube |
| **Rastreo** | Rayos X | Información sobre la aplicación | Seguimiento de la nube |
---

## Gestión de costes
### Modelos de precios
| Modelo | Descripción | Mejor para |
|-------|-------------|----------|
| **Bajo demanda** | Paga por lo que usas, por segundo/hora | Cargas de trabajo variables y de corta duración |
| **Instancias reservadas** | Compromiso de 1 a 3 años, descuento importante | Cargas de trabajo en estado estacionario |
| **Instancias puntuales** | Oferta por capacidad no utilizada; puede ser interrumpido | Trabajos flexibles y tolerantes a fallos |
| **Planes de ahorro** | Precios de compromiso flexibles | Patrones de uso mixto |
| **Nivel gratuito** | Uso gratuito limitado para cuentas nuevas | Aprendizaje, creación de prototipos |
### Estrategias de optimización
Instancias del tamaño adecuado para adaptarse a las cargas de trabajo. Utilice el escalado automático para manejar los picos de demanda. Capacidad de reserva para cargas predecibles. Utilice instancias puntuales para trabajos por lotes. Mueva los datos a los que se accede con poca frecuencia a niveles de almacenamiento más económicos. Elimine los recursos no utilizados (instantáneas huérfanas, equilibradores de carga inactivos, IP no conectadas).
---

## Alta disponibilidad y recuperación ante desastres
### Conceptos de disponibilidad
| Concepto | Descripción |
|---------|-------------|
| **Zona de disponibilidad (AZ)** | Centros de datos físicamente separados dentro de una región |
| **Región** | Área geográfica con múltiples AZ |
| **Ubicación del borde** | Ubicación de caché CDN para entrega de contenido |
### Estrategias de recuperación ante desastres
| Estrategia | Costo | RTO | RPO | Descripción |
|----------|------|-----|-----|-------------|
| **Copia de seguridad y restauración** | Más bajo | Horas | Horas-días | Copias de seguridad periódicas, restaurar cuando sea necesario |
| **Luz piloto** | Bajo | Minutos–horas | Minutos | Los elementos centrales siempre están en funcionamiento y se amplían en caso de desastre |
| **Espera cálida** | Medio | Minutos | Segundos-minutos | Versión reducida siempre en ejecución |
| **Multisitio activo/activo** | Más alto | Cerca de cero | Cero | Producción plena en múltiples regiones |
**RTO** (Objetivo de tiempo de recuperación) = tiempo de inactividad máximo aceptable. **RPO** (Objetivo de punto de recuperación) = pérdida de datos máxima aceptable.
---

## Tendencias emergentes
| Tendencia | ¿Qué está pasando?
|-------|-----------------|
| **Computación de vanguardia** | Procesamiento de datos más cerca de la fuente (AWS Outposts, Wavelength, Azure Edge) |
| **Nube múltiple** | Evitar la dependencia del proveedor; aprovechando lo mejor de su clase entre proveedores |
| **Servicios de IA/ML** | Modelos previamente entrenados (visión, habla, lenguaje) + entrenamiento personalizado (SageMaker, Vertex AI) |
| **Computación cuántica** | Servicios experimentales en etapa inicial (AWS Braket, Azure Quantum) |
| **Nube Sostenible** | Seguimiento de la huella de carbono, compromisos en materia de energías renovables, arquitectura verde |