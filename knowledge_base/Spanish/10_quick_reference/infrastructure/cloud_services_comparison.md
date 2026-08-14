<!--
---
# Metadata
title: "Cloud Services Comparison"
description: "AWS vs Azure vs GCP side-by-side comparison"
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
tags: [cloud, services, comparison, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Comparación de servicios en la nube
Una comparación lado a lado de los tres principales proveedores de nube (AWS, Azure y Google Cloud) en computación, almacenamiento, bases de datos, IA/ML, redes, monitoreo e infraestructura como código. Útil para arquitectos que deciden qué plataforma usar o mapean servicios de una nube a otra.
---

## Descripción general del proveedor
| | AWS | Azul | Nube de Google (GCP) |
|---|-----|-------|---------------------|
| **Cuota de mercado** | ~31% (más grande) | ~25% (segundo) | ~11% (tercero, de mayor crecimiento) |
| **Fortalezas** | Amplitud de servicios; madurez; ecosistema | Integración empresarial; nube híbrida; Pila de Microsoft | Datos/IA; Kubernetes; red mundial |
| **Mejor para** | Desde startups hasta empresas; catálogo de servicios más amplio | Empresas con Microsoft/Active Directory; híbrido | Cargas de trabajo intensivas en datos; Nativo de Kubernetes; IA/ML |
| ** Regiones ** | 33 regiones, 105 AZ | Más de 60 regiones | Más de 40 regiones, más de 100 zonas |
| **Nivel gratuito** | 12 meses de nivel gratuito + siempre gratis | 12 meses gratis + $200 de crédito | Crédito de $300 por 90 días + siempre gratis |
---

## Calcular
| Categoría de servicio | AWS | Azul | PCG |
|-----------------|-----|-------|-----|
| **Máquinas virtuales** | EC2 (Nube de Computación Elástica) | Máquinas virtuales | Motor de Computación |
| **Escalado automático** | Grupos de Auto Scaling | Conjuntos de escalado de máquinas virtuales | Grupos de instancias |
| **Funciones sin servidor** | lambda | Funciones de Azure | Funciones de la nube |
| **Registro de contenedores** | ECR (Registro de Contenedores Elásticos) | Registro de contenedores de Azure | Registro de artefactos |
| **Orquestación de contenedores** | ECS/EKS | ACS/AKS | GKE/ejecución en la nube |
| **Contenedores sin servidor** | Fargate | Aplicaciones de contenedores | Ejecución en la nube |
| **Plataforma de aplicaciones (PaaS)** | Elastic Beanstalk, corredor de aplicaciones | Servicio de aplicaciones | Motor de aplicaciones |
| **Procesamiento por lotes** | Lote de AWS | Lote azul | Lote en la nube |
| **GPU / Computación AI** | EC2 (instancias P4d, P5) | Máquinas virtuales de la serie NC/ND | máquinas virtuales A2/A3; TPU |
### Modelos de precios de VM
| Modelo | AWS | Azul | PCG |
|-------|-----|-------|-----|
| **Bajo demanda** | Instancias bajo demanda | Pago por uso | Bajo demanda |
| **Reservado / Comprometido** | Instancias reservadas (1 a 3 años) | Máquinas virtuales reservadas (1 a 3 años) | Descuentos por uso comprometido (1 a 3 años) |
| **Puntual / Interrumpible** | Instancias puntuales | Detectar máquinas virtuales | Máquinas virtuales interrumpibles/puntuales |
| **Planes de ahorro** | Planes de Ahorro | Planes de ahorro | Descuentos por uso comprometido |
---

## Almacenamiento
| Categoría de servicio | AWS | Azul | PCG |
|-----------------|-----|-------|-----|
| **Almacenamiento de objetos** | T3 | Almacenamiento de blobs | Almacenamiento en la nube |
| **Almacenamiento en bloque** | EBS | Discos administrados | Disco persistente |
| **Almacenamiento de archivos** | EFS, FSx | Archivos de Azure | Almacén de archivos |
| **Archivo / Frío** | Glaciar S3, Archivo Profundo | Niveles de Blob Cool/Archivo | Línea fría/Archivo de almacenamiento en la nube |
| **Transferencia de datos** | Bola de nieve, sincronización de datos | Cuadro de datos | Dispositivo de transferencia |
### Comparación de clases de almacenamiento
| Caso de uso | AWS S3 | Mancha azur | Almacenamiento en la nube de GCP |
|----------|--------|------------|-------------------|
| **Acceso frecuente** | Estándar S3 | Caliente | Estándar |
| **Acceso poco frecuente** | S3 Estándar-IA | Genial | Cerca de la línea |
| **Acceso poco frecuente** | S3 Una Zona-IA | — | Línea fría |
| **Archivo** | Glaciar S3 / Archivo Profundo | Archivo | Archivo |
---

## Bases de datos
| Categoría de servicio | AWS | Azul | PCG |
|-----------------|-----|-------|-----|
| **Relacional (gestionado)** | RDS (MySQL, PostgreSQL, Oracle, Servidor SQL) | Base de datos Azure (MySQL, PostgreSQL); Azure SQL | Nube SQL (MySQL, PostgreSQL) |
| **Relacional (nativo de la nube)** | Aurora (compatible con MySQL/PostgreSQL) | Base de datos SQL de Azure (grupos elásticos) | Cloud Spanner (distribuido globalmente) |
| **NoSQL (documento)** | DinamoDB | Cosmos DB (API de MongoDB, API de SQL) | almacén de bomberos; Almacén de datos |
| **NoSQL (columna ancha)** | DynamoDB (también) | Cosmos DB (API de Cassandra) | Mesa grande |
| **NoSQL (clave-valor)** | DynamoDB, ElastiCache | Caché de Azure para Redis | Almacén de memoria (Redis) |
| **Gráfico** | Neptuno | Cosmos DB (API Gremlin) | — |
| **Series temporales** | Corriente temporal | Explorador de datos de Azure | — |
| **Libro mayor** | QLDB | Libro mayor confidencial de Azure | — |
| **Caché en memoria** | ElastiCache (Redis, Memcached) | Caché de Azure para Redis | Almacén de memorias |
| **Buscar** | Servicio OpenSearch | Búsqueda de IA en Azure | Búsqueda en la nube; Búsqueda de IA de vértice |
| **Almacén de datos** | Desplazamiento al rojo | Análisis de sinapsis | Gran consulta |
---

## IA y aprendizaje automático
| Categoría de servicio | AWS | Azul | PCG |
|-----------------|-----|-------|-----|
| **Plataforma de aprendizaje automático** | Creador de salvia | Aprendizaje automático de Azure | IA de vértice |
| **API previamente entrenadas** | Reconocimiento (visión), Polly (TTS), Comprender (PNL), Transcribir | Servicios Cognitivos (Visión, Habla, Lenguaje, Decisión) | Vision AI, voz a texto, API de lenguaje natural |
| **LLM / IA generativa** | Bedrock (Claude, Llama, Titán) | Servicio Azure OpenAI (GPT-4, DALL-E) | Vértice AI (Géminis); Jardín modelo |
| **Vectores / Incrustaciones** | OpenSearch (k-NN), bases de conocimiento de Bedrock | Búsqueda de IA en Azure (vector) | Búsqueda de vectores Vertex AI, AlloyDB |
| **MLOps** | Pipelines de SageMaker, registro de modelos | Canalizaciones de Azure ML, registro de modelos | Canalizaciones de Vertex AI, registro de modelos |
| **Etiquetado de datos** | Verdad fundamental de SageMaker | Etiquetado de datos de Azure ML | Etiquetado de datos Vertex AI |
| **IA conversacional** | Alex | Servicio de bots de Azure | Flujo de diálogo CX/ES |
| **Traducción** | Traducir | Traductor | API de traducción |
---

## Redes
| Categoría de servicio | AWS | Azul | PCG |
|-----------------|-----|-------|-----|
| **Red virtual** | VPC | Red virtual (VNet) | VPC |
| **Equilibrio de carga** | ELB/ALB/NLB/CLB | Equilibrador de carga (aplicación, red, puerta de enlace) | Equilibrio de carga en la nube |
| **DNS** | Ruta 53 | DNS de Azure | DNS en la nube |
| **CDN** | Frente a la nube | Puerta de entrada azul | CDN en la nube |
| **Puerta de enlace API** | Puerta de enlace API | Gestión de API | Puerta de enlace API |
| **VPN** | VPN de sitio a sitio, VPN de cliente | Puerta de enlace VPN | VPN en la nube |
| **Conexión directa/ExpressRoute** | Conexión directa | Ruta Express | Interconexión en la nube |
| **Enlace privado** | PrivateLink, puntos finales de la VPC | Enlace privado, puntos finales privados | Conexión de servicio privado |
| **Cortafuegos** | WAF, cortafuegos de red | Cortafuegos de Azure, WAF | Armadura de nube, cortafuegos |
| **Protección DDoS** | Escudo Estándar / Avanzado | Protección DDoS | Armadura de nube |
---

## Monitoreo y registro
| Categoría de servicio | AWS | Azul | PCG |
|-----------------|-----|-------|-----|
| **Métricas/Monitoreo** | Vigilancia de la nube | Monitor de Azure | Monitoreo de la nube (Stackdriver) |
| **Registro** | Registros de CloudWatch | Análisis de registros (registros de Azure Monitor) | Registro en la nube |
| **Rastreo** | Rayos X | Información sobre la aplicación | Seguimiento de la nube |
| **Alerta** | Alarmas de CloudWatch | Alertas de Azure Monitor | Alertas de monitoreo en la nube |
| **Paneles** | Paneles de control de CloudWatch | Libros de trabajo/paneles de Azure | Paneles de control de la nube |
| **Seguimiento de errores** | Sintéticos CloudWatch | Información sobre la aplicación | Informe de errores en la nube |
| **Tercero** | Datadog, Nueva Reliquia, PagerDuty | Datadog, Nueva Reliquia, PagerDuty | Datadog, Nueva Reliquia, PagerDuty |
---

## Infraestructura como código y DevOps
| Categoría de servicio | AWS | Azul | PCG |
|-----------------|-----|-------|-----|
| **IaC (nativo)** | Formación de nubes | Plantillas ARM / Bíceps | Gerente de Implementación / Pulumi |
| **IaC (entre nubes)** | Terraform, Pulumi, CDK | Terraform, Pulumi, Bíceps | Terraform, Pulumi |
| **CI/CD** | CodePipeline, CodeBuild | Azure DevOps, acciones de GitHub | Construcción de nube; Implementación en la nube |
| **Registro de contenedores** | ECR | Registro de contenedores de Azure | Registro de artefactos |
| **GitOps** | Aplicación Mesh + Flux/ArgoCD | Flux/ArgoCD en AKS | Sincronización de configuración (Anthos) |
| **Gestión de secretos** | Administrador de secretos, almacén de parámetros SSM | Bóveda de claves | Gerente Secreto |
---

## Consideraciones de precios
| factor | AWS | Azul | PCG |
|--------|-----|-------|-----|
| **Granularidad de facturación** | Por segundo (después de la primera hora para algunos) | Por segundo | Por segundo |
| **Descuentos por uso sostenido** | Instancias Reservadas / Planes de Ahorro | Máquinas virtuales reservadas | Descuentos por uso comprometido |
| **Instancias puntuales** | Hasta 90% de descuento | Hasta 90% de descuento | Hasta 91% de descuento |
| **Salida de datos** | Cobrado (caro) | Cargado | Mismo precio independientemente del destino (a menudo más barato) |
| **Nivel gratuito** | 12 meses + siempre gratis | 12 meses + $200 de crédito | $300 por 90 días + siempre gratis |
| **Descuentos para empresas** | Programa de descuento empresarial (EDP) | MACC (Contrato de Compromiso Monetario) | Uso comprometido + CUDs |
---

## Cuándo usar cuál
| Escenario | Recomendado | Por qué |
|----------|-------------|-----|
| **La más amplia selección de servicios; ecosistema maduro** | AWS | Catálogo más grande; la mayoría de las integraciones de terceros |
| **Empresa de Microsoft; Directorio Activo; híbrido** | Azul | Integración nativa de AD; potentes herramientas híbridas |
| **Almacenamiento de datos; Gran consulta; análisis intensivo** | PCG | BigQuery es el mejor de su clase; integración perfecta de datos |
| **Desarrollo nativo de Kubernetes** | PCG | GKE es el Kubernetes administrado más pulido |
| **Aplicaciones de IA generativa/LLM** | Azure o GCP | Azure OpenAI para modelos GPT; Vertex AI para Géminis |
| **Aplicaciones de baja latencia y escala global** | PCG | La red global de Google es una verdadera ventaja |
| **Cargas de trabajo de gobierno/cumplimiento pesado** | AWS o Azure | La mayoría de las certificaciones de cumplimiento; Regiones de GovCloud |
| **Startups sensibles a los costos** | GCP o AWS | El nivel gratuito de GCP es generoso; AWS tiene créditos iniciales |
| **Pila existente de Microsoft/.NET** | Azul | Estrecha integración con Visual Studio, .NET, Office 365 |
| **Estrategia multinube** | Terraform + los tres | Utilice Terraform para gestionar recursos en las nubes |
---

## Resumen
Las tres nubes son capaces, confiables y en constante expansión. La elección generalmente se reduce a: lo que su equipo ya sabe, cómo son sus contratos existentes y qué servicios específicos son importantes para su carga de trabajo. La multinube es cada vez más común: utilice Terraform o Pulumi para evitar la dependencia de un proveedor en la capa de infraestructura y elija cada nube según lo que mejor hace.