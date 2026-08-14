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

# Terraform e infraestructura como código
Terraform es la herramienta de infraestructura como código (IaC) más utilizada: le permite definir la infraestructura de la nube (servidores, bases de datos, redes, permisos) en archivos de configuración declarativos que se pueden versionar, revisar, probar y automatizar. En lugar de hacer clic en una consola en la nube, escribe un código que describe el estado deseado de su infraestructura y Terraform determina qué cambios realizar.
---

## Conceptos básicos
| Concepto | Descripción |
|---------|-------------|
| **Proveedor** | Complemento que gestiona una plataforma en la nube específica (AWS, Azure, GCP, etc.) |
| **Recurso** | Un objeto de infraestructura (servidor, base de datos, red) |
| **Estado** | El registro de Terraform sobre qué infraestructura existe; almacenado en un archivo de estado |
| **Planificar** | Vista previa de los cambios que hará Terraform |
| **Aplicar** | Ejecutar el plan; crear/actualizar/destruir infraestructura |
| **Módulo** | Colección reutilizable de recursos |
| **Variables** | Parámetro de entrada para configuraciones |
| **Salida** | Valor exportado desde un módulo o configuración |
| **Fuente de datos** | Leer información de la infraestructura existente |
---

## Flujo de trabajo básico
| Paso | Comando | Descripción |
|------|---------|-------------|
| **1. Configuración de escritura** | Crear archivos`.tf`| Definir proveedores, recursos, variables |
| **2. Inicializar** | `terraform init`| Proveedores de descargas; configurar el servidor |
| **3. Formato** | `terraform fmt`| Estandarizar el formato |
| **4. Validar** | `terraform validate`| Verificar sintaxis y configuración |
| **5. Plano** | `terraform plan`| Vista previa de cambios (ejecución en seco) |
| **6. Aplicar** | `terraform apply`| Crear o actualizar infraestructura |
| **7. Destruir** | `terraform destroy`| Derribar toda la infraestructura gestionada |
---

## Comandos comunes
| Comando | Descripción |
|---------|-------------|
| `terraform init`| Inicializar el directorio de trabajo; proveedores y módulos de descarga |
| `terraform plan`| Mostrar qué cambios se realizarán |
| `terraform apply`| Aplicar cambios; agregue`-auto-approve`para omitir la confirmación |
| `terraform destroy`| Destruir todos los recursos administrados |
| `terraform fmt`| Formatear archivos de configuración al estilo estándar |
| `terraform validate`| Validar la sintaxis de configuración |
| `terraform output`| Mostrar valores de salida |
| `terraform state list`| Enumere todos los recursos en el estado |
| `terraform state show <resource>`| Mostrar detalles de un recurso específico |
| `terraform import <resource> <id>`| Importar infraestructura existente al estado |
| `terraform taint <resource>`| Marcar un recurso para recreación en la próxima solicitud |
| `terraform refresh`| Actualizar el estado para que coincida con la infraestructura real |
| `terraform graph`| Generar un gráfico de dependencia visual (formato DOT) |
| `terraform console`| Consola interactiva para probar expresiones |
---

## Gestión del Estado
| Mejores prácticas | Descripción |
|--------------|-------------|
| **Estado remoto** | Almacenar el estado en S3, GCS, Azure Blob o Terraform Cloud, nunca localmente |
| **Bloqueo de estado** | Utilice DynamoDB (backend de S3) o bloqueo nativo para evitar modificaciones simultáneas |
| **Cifrado de estado** | Habilite el cifrado en reposo para archivos de estado (contienen datos confidenciales) |
| **Separación de estados** | Utilice archivos de estado separados para diferentes entornos o equipos |
| **Copia de seguridad del estado** | Los backends remotos versionan automáticamente el estado; mantenga esto habilitado |
| **Nunca edite el estado manualmente** | Utilice `terraform state mv`, `rm`,`import`en su lugar |
---

## Estructura del módulo
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

## Tipos de variables
| Tipo | Ejemplo | Caso de uso |
|------|---------|----------|
| **cadena** | `variable "region" { type = string }`| Valor de texto único |
| **número** | `variable "count" { type = number }`| Valor numérico |
| **bool** | `variable "enable" { type = bool }`| Bandera de verdadero/falso |
| **lista** | `variable "zones" { type = list(string) }`| Colección ordenada |
| **mapa** | `variable "tags" { type = map(string) }`| Pares clave-valor |
| **objeto** | `variable "config" { type = object({...}) }`| Configuración estructurada |
---

## Patrones comunes
| Patrón | Descripción |
|---------|-------------|
| **Contar** | `count = 3`crea múltiples instancias de un recurso |
| **Para cada** | `for_each = var.items`itera sobre un mapa o conjunto |
| **Bloques dinámicos** | Generar bloques anidados repetidos (por ejemplo, reglas de ingreso) |
| **Valores locales** | `locals { ... }`para valores calculados y reducción de repeticiones |
| **Fuentes de datos** | Leer la infraestructura existente (por ejemplo, buscar una VPC existente) |
| **Aprovisionadores** | Ejecute scripts en recursos después de la creación (úselos con moderación) |
| **Espacios de trabajo** | Estado separado para diferentes entornos dentro de la misma configuración |
---

## Solución de problemas
| Problema | Solución |
|---------|----------|
| **Deriva del estado** | Ejecute`terraform plan`para ver las diferencias; `terraform apply`para conciliar |
| **Estado bloqueado** | Comprueba quién tiene el candado; utilice`terraform force-unlock`si es seguro |
| **Errores del proveedor** | Verificar credenciales; actualizar la versión del proveedor; comprobar los límites de API |
| **Conflictos de importación** | Recurso ya en estado; utilice`terraform state rm`primero |
| **Dependencias circulares** | Reestructurar recursos; utilice`depends_on`con cuidado |
| **Estado grande** | Dividir en módulos; utilice`-target`para operaciones parciales |
---

## Resumen
Terraform gestiona la infraestructura a través de archivos de configuración declarativos. El flujo de trabajo es: escribir configuración → inicio → plan → aplicar. El estado rastrea lo que existe y debe almacenarse de forma remota con bloqueo. Los módulos permiten la reutilización. Las variables parametrizan las configuraciones. Los principios clave son: tratar la infraestructura como código (control de versiones; revisión; prueba); nunca edite el estado manualmente; planificar antes de aplicar; utilizar estado remoto con bloqueo; y configuraciones de estructura con módulos para mantenibilidad.