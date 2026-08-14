---
# Metadata
title: "API Design and Integration Failures"
description: "API anti-patterns, breaking changes, versioning failures, cascading failures"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [api, design, integration, failures, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Fallos de integración y diseño de API
Las API (interfaces de programación de aplicaciones) son el tejido conectivo del software moderno: permiten que los servicios se comuniquen, que terceros se integren y que los equipos trabajen de forma independiente. Cuando el diseño de API sale mal, las consecuencias se extienden a todos los sistemas que dependen de él: integraciones rotas, vulnerabilidades de seguridad, frustración de los desarrolladores y reescrituras costosas. Las fallas de integración (donde los sistemas no pueden comunicarse de manera confiable) se encuentran entre las fuentes más comunes de incidentes de producción.
---

## Fallos comunes en el diseño de API
### Errores de diseño
| Error | Descripción | Consecuencia |
|---------|-------------|-------------|
| **Nombres inconsistentes** | `/getUsers`frente a`/list_users`frente a`/fetch-users`| Confusión; errores; lento desarrollo |
| **Puntos finales sobrecargados** | Un punto final que hace 10 cosas diferentes según los parámetros | Difícil de entender; difícil de probar; difícil de cambiar |
| **Infravalorado** | El cliente necesita realizar 5 llamadas API para obtener datos relacionados | Lento; antieconómico; código de cliente complejo |
| **Exceso de recuperación** | API devuelve todos los campos cuando el cliente solo necesita 2 | Ancho de banda desperdiciado; lento en el móvil; riesgo de seguridad (exponiendo datos innecesarios) |
| **Sin versiones** | Cambios importantes implementados sin previo aviso | Los clientes rompen; desarrolladores enojados |
| **Mensajes de error vagos** | "Error 500: Error interno del servidor" sin detalles | Imposible de depurar; resolución lenta |
| **Falta paginación** | Endpoint devuelve todos los registros (podrían ser millones) | Tiempos de espera; agotamiento de la memoria; clientes estrellados |
| **Códigos de estado inconsistentes** | 200 OK por errores; 500 por errores del cliente | Los clientes no pueden distinguir el éxito del fracaso |
### Antipatrones de API REST
| Antipatrón | Descripción | Mejor enfoque |
|-------------|-------------|-----------------|
| **Usando GET para mutaciones** | `GET /delete-user?id=5`| Utilice el método BORRAR |
| **Usando POST para todo** |  `POST /get-users`; `POST /update-user`| Utilice métodos HTTP apropiados (GET, POST, PUT, PATCH, DELETE) |
| **Devolviendo HTML desde API** | API devuelve fragmentos HTML | Devuelve JSON; dejar que el cliente renderice |
| **Lógica empresarial en URL** | `/users/active/premium/from-2023`| Utilice parámetros de consulta o cuerpo de solicitud para filtros complejos |
| **Exponer el esquema de la base de datos** | `/api/table_name/column`| Diseñe API en torno a recursos y conceptos de dominio, no a tablas |
| **Sin HATEOAS / enlaces** | El cliente codifica todas las URL | Incluir enlaces a recursos relacionados en las respuestas |
---

## Fallos de seguridad
### Vulnerabilidades comunes de la API
| Vulnerabilidad | Descripción | Ejemplo |
|--------------|-------------|---------|
| **Autenticación rota** | API no verifica correctamente la identidad | Falta validación de token; se aceptan tokens caducados |
| **Exposición excesiva de datos** | API devuelve más datos de los que el cliente necesita | El punto final del usuario devuelve hash de contraseña e ID internos |
| **Asignación masiva** | El cliente puede configurar campos que no debería | `PATCH /user`permite configurar`role: "admin"`|
| **Inyección** | Entrada del usuario interpretada como código | inyección SQL; Inyección NoSQL; inyección de comando |
| **IDOR** (Referencia de objeto directa insegura) | Accediendo a recursos cambiando el ID en la URL | `/api/users/5`→ cambiar a`/api/users/6`para ver los datos de otra persona |
| **Falta el límite de velocidad** | Sin límite de llamadas API | Fuerza bruta; denegación de servicio; raspado |
| **Configuración incorrecta de CORS** | Acceso entre orígenes demasiado permisivo | `Access-Control-Allow-Origin: *`en puntos finales autenticados |
### Fallos de autenticación y autorización
| Fracaso | Descripción | Impacto |
|---------|-------------|--------|
| **Credenciales codificadas** | Claves API o contraseñas en el código fuente | Filtrado a través del control de versiones; accesible a todos los desarrolladores |
| **Sin vencimiento del token** | Los tokens nunca caducan | El token robado da acceso permanente |
| **Claves secretas débiles** | Claves de firma breves o predecibles | Las fichas se pueden falsificar |
| **Sin alcance/permisos** | Todos los tokens tienen acceso completo | Token comprometido = acceso completo al sistema |
| **Registro de datos confidenciales** | Tokens o contraseñas en registros | Accesible para cualquier persona con acceso de registro |
| **Autorización inconsistente** | Algunos puntos finales verifican los permisos; otros no | Acceso no autorizado a través de puntos finales no vigilados |
---

## Fallos de integración
### Problemas de integración del sistema distribuido
| Fracaso | Descripción | Ejemplo |
|---------|-------------|---------|
| **Acoplamiento apretado** | Los servicios dependen de los detalles de implementación interna de cada uno | Cambiar la base de datos de un servicio daña otros tres |
| **Cadenas sincrónicas** | El servicio A llama a B llama a C llama a D; se acumula latencia | 200 ms + 300 ms + 500 ms = 1 segundo de tiempo de respuesta |
| **Sin disyuntor** | Un servicio fallido provoca fallos en cascada | El servicio D es lento; todos los servicios upstream agotan sus hilos de espera |
| **Sin lógica de reintento** | Las fallas transitorias se vuelven permanentes | Blip de red = transacción fallida; el usuario tiene que volver a intentarlo manualmente |
| **Reintentos excesivos** | Los reintentos sin retroceso abruman los servicios de recuperación | Problema de rebaño atronador |
| **Sin idempotencia** | Reintentar una operación no idempotente crea duplicados | Pago cobrado dos veces; pedido creado dos veces |
| **Eventuales sorpresas de consistencia** | El cliente lee datos obsoletos después de una escritura | Perfil de actualizaciones de usuario; actualiza la página; datos antiguos todavía se muestran |
### Fallos de integración de terceros
| Fracaso | Descripción | Mitigación |
|---------|-------------|------------|
| **Cambios en la API del proveedor** | Un tercero cambia su API sin previo aviso | Fijación de versión; capa de abstracción; seguimiento de registros de cambios de proveedores |
| **Limitación de tasa** | Un tercero acelera sus solicitudes | Almacenamiento en caché; cola de solicitudes; negociando límites más altos |
| **Tiempo de inactividad del proveedor** | El servicio de terceros no está disponible | Disyuntores; comportamiento de respaldo; estrategia de múltiples proveedores |
| **Cambios de formato de datos** | Un tercero cambia el formato de respuesta | Validación de esquemas; capa de transformación; alertas sobre cambios de formato |
| **Desuso sin ruta de migración** | El proveedor desaprueba el punto final sin equivalente | Manténgase informado; mantener la abstracción; planificar las migraciones con antelación |
---

## Estudios de caso
### Estudio de caso 1: La API que devolvió todo
| Aspecto | Descripción |
|--------|-------------|
| **Escenario** | La API de usuario de una empresa SaaS devolvió todos los campos de usuario, incluidos los metadatos internos |
| **Qué salió mal** | Sin filtrado de campos; respuesta incluyó hashes de contraseña, notas internas e indicadores de administrador |
| **Impacto** | Los investigadores de seguridad descubrieron la exposición; divulgación pública; Investigación RGPD |
| **Causa raíz** | API serializó todo el modelo de base de datos sin filtrar |
| **Reparar** | Modelos de respuesta explícita; control de acceso a nivel de campo; revisión de seguridad de todos los puntos finales |
| **Lección** | Nunca exponga su modelo de base de datos directamente a través de una API; utilizar DTO (objetos de transferencia de datos) |
### Estudio de caso 2: El fracaso en cascada
| Aspecto | Descripción |
|--------|-------------|
| **Escenario** | Una arquitectura de microservicios con comunicación síncrona entre servicios |
| **Qué salió mal** | Un servicio experimentó una desaceleración de la base de datos; los servicios upstream esperaban respuestas; grupos de hilos agotados |
| **Impacto** | Corte total del sistema durante 45 minutos; todos los servicios afectados |
| **Causa raíz** | Sin disyuntores; sin tiempos de espera; cadena de dependencia sincrónica |
| **Reparar** | Disyuntores; tiempos de espera; comunicación asíncrona cuando sea posible; mamparos |
| **Lección** | Las llamadas sincrónicas entre servicios crean cadenas frágiles; diseño para el fracaso |
---

## Mejores prácticas
### Lista de verificación de diseño de API
| Área | Práctica |
|------|----------|
| **Denominación** | Utilice sustantivos para recursos; Métodos HTTP para acciones; convención de nomenclatura coherente |
| **Versionamiento** | Versión desde el primer día; utilizar control de versiones de URL (`/v1/`) o control de versiones de encabezado |
| **Paginación** | Paginar siempre los puntos finales de la lista; utilizar paginación basada en cursor para conjuntos de datos grandes |
| **Manejo de errores** | Formato de error consistente; incluir códigos de error; proporcionar mensajes procesables |
| **Limitación de tasa** | Implementar límites de tarifas; devuelve 429 con encabezado de reintento posterior |
| **Idempotencia** | Admite claves de idempotencia para puntos finales de mutación |
| **Documentación** | Especificaciones OpenAPI/Swagger; mantenlo actualizado; proporcionar ejemplos |
| **Pruebas** | Pruebas de contrato; pruebas de integración; pruebas de contratos impulsadas por el consumidor |
| **Monitoreo** | Seguimiento de latencia; tasas de error; rendimiento; salud dependencia |
| **Desuso** | Anunciar las desusos con mucha antelación; proporcionar guías de migración |
---

## Resumen
Los fallos en el diseño de API van desde cosméticos (nombramientos inconsistentes) hasta catastróficos (vulnerabilidades de seguridad, fallos en cascada). Los errores de diseño más comunes (puntos finales sobrecargados, recuperación excesiva, falta de paginación, errores vagos) hacen que las API sean difíciles de usar y mantener. Los fallos de seguridad (autenticación rota, IDOR, asignación masiva, exposición excesiva de datos) exponen los sistemas a ataques. Las fallas de integración (acoplamiento estrecho, cadenas síncronas, disyuntores faltantes, falta de idempotencia) crean sistemas frágiles donde una falla se propaga en cascada a través de los servicios. Las integraciones de terceros añaden riesgos externos: cambios de API, limitación de tasas y tiempo de inactividad de los proveedores. Las estrategias de prevención están bien establecidas: utilizar modelos de respuesta explícitos; versión desde el primer día; implementar disyuntores y tiempos de espera; diseño para la idempotencia; validar y desinfectar todos los insumos; monitorear todo; y tratar los contratos de API como acuerdos vinculantes que requieren coordinación para cambiar. Las mejores API son aburridas: predecibles, consistentes, bien documentadas y resistentes a fallas.