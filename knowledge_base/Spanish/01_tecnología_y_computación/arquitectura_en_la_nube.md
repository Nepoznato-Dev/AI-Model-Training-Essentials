<!-- 
This file was automatically translated from English to Spanish.
Source: cloud_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Arquitectura en la Nube

## Fundamentos de la Computación en la Nube

### ¿Qué es la Computación en la Nube?
Entrega bajo demanda de recursos informáticos (servidores, almacenamiento, bases de datos, redes, software) a través de Internet con precios de pago por uso.

### Características Esenciales (Definición NIST)
- **Autoservicio Bajo Demanda**: Aprovisionar recursos sin interacción humana
- **Acceso Amplio a la Red**: Disponible a través de la red mediante mecanismos estándar
- **Agrupación de Recursos**: Modelo multiinquilino con asignación dinámica
- **Elasticidad Rápida**: Escalar hacia afuera y hacia adentro rápidamente
- **Servicio Medido**: Uso de recursos monitoreado y facturado

### Modelos de Implementación en la Nube
- **Nube Pública**: Propiedad de proveedores, infraestructura compartida (AWS, Azure, GCP)
- **Nube Privada**: Dedicada a una sola organización (en las instalaciones o alojada)
- **Nube Híbrida**: Combinación de nubes públicas y privadas
- **Multi-Nube**: Uso de múltiples proveedores de nube pública
- **Nube Comunitaria**: Compartida por organizaciones con preocupaciones comunes

### Modelos de Servicio

#### Infrastructure as a Service (IaaS)
- **Proporciona**: Máquinas virtuales, almacenamiento, redes, sistemas operativos
- **Ejemplos**: AWS EC2, Google Compute Engine, Azure VMs
- **Casos de Uso**: Migraciones lift-and-shift, entornos de desarrollo, necesidades de alto control

#### Platform as a Service (PaaS)
- **Proporciona**: Plataformas de desarrollo, bases de datos, middleware
- **Ejemplos**: Heroku, Google App Engine, AWS Elastic Beanstalk
- **Casos de Uso**: Desarrollo de aplicaciones, implementación de API, microservicios

#### Software as a Service (SaaS)
- **Proporciona**: Aplicaciones completas a través de Internet
- **Ejemplos**: Salesforce, Google Workspace, Microsoft 365, Slack
- **Casos de Uso**: Correo electrónico, CRM, colaboración, aplicaciones empresariales

#### Function as a Service (FaaS) / Serverless
- **Proporciona**: Ejecución de funciones impulsada por eventos
- **Ejemplos**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Casos de Uso**: Procesamiento de eventos, API, tareas programadas, procesamiento en tiempo real

## Principales Proveedores de Nube

### Amazon Web Services (AWS)
- **Cuota de Mercado**: ~32% (proveedor más grande)
- **Servicios Clave**:
  - Cómputo: EC2, Lambda, ECS, EKS
  - Almacenamiento: S3, EBS, Glacier
  - Base de Datos: RDS, DynamoDB, Aurora
  - Redes: VPC, Route 53, CloudFront
  - AI/ML: SageMaker, Rekognition, Comprehend

### Microsoft Azure
- **Cuota de Mercado**: ~23%
- **Fortalezas**: Integración empresarial, nube híbrida, ecosistema Microsoft
- **Servicios Clave**:
  - Cómputo: Virtual Machines, Azure Functions, AKS
  - Almacenamiento: Blob Storage, Disk Storage
  - Base de Datos: SQL Database, Cosmos DB
  - Redes: Virtual Network, Traffic Manager
  - AI/ML: Azure ML, Cognitive Services

### Google Cloud Platform (GCP)
- **Cuota de Mercado**: ~10%
- **Fortalezas**: Análisis de datos, AI/ML, Kubernetes
- **Servicios Clave**:
  - Cómputo: Compute Engine, Cloud Functions, GKE
  - Almacenamiento: Cloud Storage, Persistent Disk
  - Base de Datos: Cloud SQL, Firestore, Bigtable
  - Analytics: BigQuery, Dataflow, Pub/Sub
  - AI/ML: Vertex AI, AutoML

### Otros Proveedores
- **IBM Cloud**: Enfoque empresarial, Watson AI
- **Oracle Cloud**: Cargas de trabajo de bases de datos, aplicaciones empresariales
- **Alibaba Cloud**: Dominante en Asia-Pacífico
- **DigitalOcean**: Amigable para desarrolladores, ofertas simplificadas

## Patrones de Arquitectura en la Nube

### Principios del Marco Well-Architected

#### Excelencia Operativa
- Automatizar operaciones
- Realizar cambios frecuentes y reversibles
- Refinar procedimientos continuamente
- Anticipar fallos

#### Seguridad
- Implementar una base de identidad sólida
- Habilitar la trazabilidad
- Aplicar seguridad en todas las capas
- Automatizar las mejores prácticas de seguridad
- Proteger los datos en tránsito y en reposo

#### Confiabilidad
- Probar procedimientos de recuperación
- Recuperarse automáticamente de fallos
- Escalar horizontalmente para disponibilidad
- Dejar de adivinar la capacidad
- Gestionar el cambio en la automatización

#### Eficiencia de Rendimiento
- Democratizar tecnologías avanzadas
- Ir global en minutos
- Usar arquitecturas serverless
- Experimentar más a menudo
- Considerar la simpatía mecánica

#### Optimización de Costos
- Adoptar modelo de consumo
- Medir la eficiencia general
- Dejar de gastar dinero en trabajo indiferenciado
- Analizar y atribuir el gasto
- Usar servicios gestionados

### Patrones de Arquitectura Comunes

#### Arquitectura de Microservicios
- Descomponer aplicaciones en servicios pequeños e independientes
- Cada servicio posee sus datos y lógica
- Comunicarse vía APIs (REST, gRPC, mensajería)
- Implementar independientemente
- **Beneficios**: Escalabilidad, aislamiento de fallos, diversidad tecnológica
- **Desafíos**: Complejidad distribuida, consistencia de datos, monitoreo

#### Arquitectura Dirigida por Eventos
- Los componentes se comunican a través de eventos
- Los productores emiten eventos, los consumidores reaccionan
- **Patrones**: Event sourcing, CQRS, pub/sub
- **Tecnologías**: Kafka, SNS/SQS, EventBridge, Pub/Sub
- **Beneficios**: Acoplamiento flexible, escalabilidad, procesamiento en tiempo real

#### Arquitectura Serverless
- No se requiere gestión de servidores
- Pago por ejecución
- Escalado automático
- **Componentes**: Funciones, API Gateway, servicios gestionados
- **Beneficios**: Eficiencia de costos, operaciones reducidas, implementación rápida
- **Consideraciones**: Arranques en frío, bloqueo del proveedor, límites de ejecución

#### Arquitectura en Capas (N-Tier)
- Capa de presentación (UI)
- Capa de lógica de aplicación/negocio
- Capa de acceso a datos
- Capa de base de datos
- **Beneficios**: Separación de responsabilidades, mantenibilidad
- **Común**: Aplicaciones web de 3 niveles

#### Arquitectura Basada en Espacio
- Manejar alta concurrencia con datos distribuidos
- Memoria virtualizada a través de servidores
- Nodos de procesamiento escalan independientemente
- **Casos de Uso**: Aplicaciones de alto volumen y baja latencia

## Servicios de Cómputo

### Máquinas Virtuales
- **Tipos**: Propósito general, optimizadas para cómputo, optimizadas para memoria, GPU
- **Precios**: Bajo demanda, instancias reservadas, instancias spot
- **Gestión**: Grupos de autoescalado, balanceadores de carga
- **Mejores Prácticas**: Dimensionamiento correcto, etiquetado, monitoreo, parcheo

### Contenedores
- **Docker**: Estándar de tiempo de ejecución de contenedores
- **Orquestación**: Kubernetes (EKS, AKS, GKE), ECS, Fargate
- **Beneficios**: Portabilidad, eficiencia, consistencia
- **Registro**: ECR, GCR, ACR, Docker Hub

### Funciones Serverless
- **Modelo de Ejecución**: Activado por eventos, sin estado
- **Límites**: Tiempo de ejecución, memoria, ejecuciones simultáneas
- **Casos de Uso**: APIs, procesamiento de archivos, trabajos programados, backends IoT
- **Monitoreo**: Recuentos de invocaciones, errores, duración, arranques en frío

## Soluciones de Almacenamiento

### Almacenamiento de Objetos
- **Características**: Estructura plana, metadatos, acceso HTTP
- **Ejemplos**: AWS S3, Google Cloud Storage, Azure Blob
- **Casos de Uso**: Activos estáticos, copias de seguridad, lagos de datos, archivos
- **Clases de Almacenamiento**: Caliente, frío, muy frío, archivo (costo/acceso variable)

### Almacenamiento en Bloque
- **Características**: Volúmenes brutos, adjuntos a VMs
- **Ejemplos**: AWS EBS, Google Persistent Disk, Azure Disks
- **Casos de Uso**: Bases de datos, volúmenes de arranque, necesidades de alto rendimiento
- **Tipos**: SSD, HDD, IOPS aprovisionados

### Almacenamiento de Archivos
- **Características**: Sistemas de archivos compartidos, protocolos NFS/SMB
- **Ejemplos**: AWS EFS, Google Filestore, Azure Files
- **Casos de Uso**: Gestión de contenido, configuraciones compartidas, migraciones lift-and-shift

### Almacenamiento de Archivo
- **Características**: Costo más bajo, retrasos de recuperación
- **Ejemplos**: S3 Glacier, Azure Archive Storage
- **Casos de Uso**: Cumplimiento normativo, copias de seguridad a largo plazo, datos históricos

## Servicios de Base de Datos

### Bases de Datos Relacionales Gestionadas
- **Servicios**: AWS RDS/Aurora, Google Cloud SQL, Azure SQL Database
- **Características**: Copias de seguridad automatizadas, parcheo, escalado, replicación
- **Motores**: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server

### Bases de Datos NoSQL
- **Documento**: DocumentDB, Firestore, Cosmos DB
- **Clave-Valor**: DynamoDB, Redis Cache
- **Columna Ancha**: Bigtable, Cassandra (gestionada)
- **Grafo**: Neptune, Cosmos DB (API de grafo)

### Almacenes de Datos
- **Servicios**: Snowflake, Redshift, BigQuery, Synapse
- **Características**: Almacenamiento columnar, arquitectura MPP
- **Casos de Uso**: Análisis, BI, análisis de datos a gran escala

### Servicios de Caché
- **En Memoria**: ElastiCache (Redis/Memcached), Cloud Memorystore
- **Caché CDN**: CloudFront, Cloud CDN, Azure CDN
- **Casos de Uso**: Almacenamiento de sesiones, caché de consultas, entrega de contenido

## Redes

### Redes Virtuales
- **VPC/VNet**: Entornos de red aislados
- **Subredes**: Públicas (orientadas a Internet), privadas (solo internas)
- **Direccionamiento IP**: Bloques CIDR, IPv4/IPv6
- **Tablas de Rutas**: Controlar el flujo de tráfico

### Balanceo de Carga
- **Tipos**: Aplicación (L7), Red (L4), Gateway
- **Características**: Comprobaciones de estado, terminación SSL, sesiones persistentes
- **Servicios**: ELB/ALB/NLB, Cloud Load Balancing, Azure Load Balancer

### Redes de Entrega de Contenido (CDN)
- **Propósito**: Almacenar contenido en caché en ubicaciones periféricas
- **Beneficios**: Latencia reducida, menor carga de origen, distribución global
- **Servicios**: CloudFront, Cloud CDN, Azure CDN, Akamai

### Servicios DNS
- **Funciones**: Registro de dominios, enrutamiento, comprobaciones de estado
- **Servicios**: Route 53, Cloud DNS, Azure DNS
- **Políticas de Enrutamiento**: Simple, ponderado, basado en latencia, geolocalización, conmutación por error

### Opciones de Conectividad
- **Gateway de Internet**: Acceso público a Internet
- **Gateway NAT**: Acceso saliente de subred privada
- **VPN**: Túneles cifrados a instalaciones locales
- **Direct Connect/ExpressRoute**: Conexiones privadas dedicadas
- **VPC Peering**: Conectar VPC dentro/entre cuentas

## Seguridad en la Nube

### Modelo de Responsabilidad Compartida
- **Responsabilidad del Proveedor**: Seguridad DE la nube (infraestructura)
- **Responsabilidad del Cliente**: Seguridad EN la nube (datos, aplicaciones, acceso)
- **Varía por Servicio**: Más gestionado = más responsabilidad del proveedor

### Gestión de Identidad y Acceso (IAM)
- **Usuarios**: Identidades individuales
- **Grupos**: Colecciones de usuarios
- **Roles**: Credenciales temporales para servicios/usuarios
- **Políticas**: Documentos JSON que definen permisos
- **Principios**: Mínimo privilegio, separación de deberes

### Seguridad de Red
- **Grupos de Seguridad**: Firewalls con estado para instancias
- **ACLs de Red**: Firewalls sin estado para subredes
- **Web Application Firewall (WAF)**: Proteger contra exploits web
- **Protección DDoS**: Shield, Cloud Armor, DDoS Protection

### Protección de Datos
- **Cifrado en Reposo**: KMS, claves gestionadas por el cliente
- **Cifrado en Tránsito**: TLS/SSL, HTTPS
- **Gestión de Claves**: HSM, rotación de claves, registros de auditoría
- **Gestión de Secretos**: Secrets Manager, Key Vault

### Cumplimiento y Gobernanza
- **Certificaciones**: SOC 2, ISO 27001, HIPAA, PCI-DSS, GDPR
- **Herramientas**: Aplicación de políticas, informes de cumplimiento, registros de auditoría
- **Marcos**: Cloud Security Alliance, NIST CSF

## DevOps en la Nube

### Servicios CI/CD
- **AWS**: CodePipeline, CodeBuild, CodeDeploy
- **Azure**: Azure DevOps, GitHub Actions
- **GCP**: Cloud Build, Cloud Deploy
- **Terceros**: Jenkins, CircleCI, GitLab CI

### Infraestructura como Código (IaC)
- **Terraform**: Multi-nube, declarativo, gestión de estado
- **CloudFormation**: Nativo de AWS, plantillas YAML/JSON
- **Plantillas ARM**: Nativo de Azure
- **Deployment Manager**: Nativo de GCP
- **Pulumi**: Infraestructura usando lenguajes de programación
- **Beneficios**: Control de versiones, repetibilidad, documentación

### Gestión de Configuración
- **Ansible**: Sin agente, playbooks YAML
- **Chef**: Basado en Ruby, ecosistema maduro
- **Puppet**: Declarativo, informes sólidos
- **SaltStack**: Rápido, basado en Python

### Monitoreo y Observabilidad
- **Métricas**: CloudWatch, Cloud Monitoring, Azure Monitor
- **Registro**: CloudWatch Logs, Cloud Logging, Log Analytics
- **Trazabilidad**: X-Ray, Cloud Trace, Application Insights
- **Paneles**: CloudWatch Dashboards, Cloud Console
- **Alertas**: SNS, alertas de Cloud Monitoring, Action Groups

### Orquestación de Contenedores
- **Kubernetes**: Orquestación estándar de la industria
- **Servicios Gestionados**: EKS, AKS, GKE
- **Service Mesh**: Istio, Linkerd (gestión de tráfico, seguridad)
- **GitOps**: ArgoCD, Flux (implementaciones declarativas)

## Gestión de Costos

### Modelos de Precios
- **Pago por uso**: Paga por lo que usas
- **Instancias Reservadas**: Compromisos de 1-3 años, descuentos significativos
- **Instancias Spot**: Ofertar por capacidad no utilizada, puede ser interrumpido
- **Planes de Ahorro**: Precios de compromiso flexible
- **Nivel Gratuito**: Uso gratuito limitado para cuentas nuevas

### Estrategias de Optimización de Costos
- **Dimensionamiento correcto**: Coincidir tipos de instancia con necesidades de carga de trabajo
- **Autoescalado**: Escalar según la demanda
- **Capacidad Reservada**: Comprometerse con cargas de trabajo de estado estable
- **Uso de Spot**: Usar para cargas de trabajo tolerantes a fallos y flexibles
- **Niveles de Almacenamiento**: Mover datos infrecuentes a niveles más baratos
- **Limpieza**: Eliminar recursos no utilizados, instantáneas, AMIs

### Herramientas de Gestión de Costos
- **AWS**: Cost Explorer, Budgets, Trusted Advisor
- **Azure**: Cost Management, Advisor
- **GCP**: Informes de facturación, Recommender
- **Terceros**: CloudHealth, CloudCheckr, Datadog

## Alta Disponibilidad y Recuperación ante Desastres

### Conceptos de Disponibilidad
- **Zonas de Disponibilidad**: Centros de datos físicamente separados dentro de una región
- **Regiones**: Áreas geográficas con múltiples AZs
- **Ubicaciones Periféricas**: Ubicaciones de caché CDN globalmente

### Estrategias de Alta Disponibilidad
- **Multi-AZ**: Implementar en zonas de disponibilidad
- **Auto-curación**: Reemplazar automáticamente instancias fallidas
- **Balanceo de Carga**: Distribuir tráfico entre instancias saludables
- **Replicación de Base de Datos**: Implementaciones Multi-AZ, réplicas de lectura

### Estrategias de Recuperación ante Desastres
- **Copia de Seguridad y Restauración**: Copias de seguridad periódicas, restaurar cuando sea necesario (costo más bajo)
- **Pilot Light**: Elementos centrales ejecutándose, escalar durante desastre
- **Standby Caliente**: Versión reducida siempre ejecutándose
- **Multi-Sitio Activo/Activo**: Producción completa en múltiples regiones (costo más alto)

### RTO y RPO
- **Objetivo de Tiempo de Recuperación (RTO)**: Tiempo de inactividad máximo aceptable
- **Objetivo de Punto de Recuperación (RPO)**: Pérdida de datos máxima aceptable
- **Selección de Estrategia**: Basado en requisitos empresariales y presupuesto

## Tendencias Emergentes

### Computación en el Borde
- Procesar datos más cerca de la fuente
- **Servicios**: AWS Outposts, Wavelength, Azure Edge, Cloud CDN
- **Casos de Uso**: IoT, análisis en tiempo real, aplicaciones de baja latencia

### Multi-Nube y Nube Híbrida
- Evitar el bloqueo del proveedor
- Aprovechar servicios best-of-breed
- **Herramientas**: Terraform, Anthos, Arc, CloudHealth

### Servicios AI/ML
- Modelos preentrenados: Visión, voz, lenguaje
- Entrenamiento de modelos personalizados: SageMaker, Vertex AI, Azure ML
- MLOps: Implementación de modelos, monitoreo, gobernanza

### Computación Cuántica
- **Servicios**: AWS Braket, Azure Quantum
- **Estado**: Etapa temprana, experimental
- **Potencial**: Criptografía, optimización, descubrimiento de fármacos

### Nube Sostenible
- Seguimiento de huella de carbono
- Compromisos de energía renovable
- Utilización eficiente de recursos
- Patrones de arquitectura verde
