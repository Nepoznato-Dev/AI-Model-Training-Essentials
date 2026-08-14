<!--
---
# Metadata
title: "API Design and Architecture"
description: "REST, GraphQL, gRPC, versioning, auth, API gateways"
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
tags: [api, design, architecture, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Diseño y arquitectura de API
Una API (interfaz de programación de aplicaciones) es la forma en que los componentes de software se comunican entre sí. Una API bien diseñada es intuitiva, consistente y es un placer trabajar con ella. Uno mal diseñado provoca confusión, errores y frustración. Este archivo cubre los principios, patrones y prácticas para crear API que los desarrolladores realmente desean utilizar.
---

## Principios de la API REST
REST (Transferencia de estado representacional) es el estilo arquitectónico dominante para las API web. Trata los datos como **recursos** identificados por URL y utiliza métodos HTTP para operar con ellos.
### Principios básicos
| Principio | Descripción |
|-----------|-------------|
| **Recursos** | Todo es un recurso con un URI (`/users/123`, `/orders/456`) |
| **Métodos HTTP** | GET (leer), POST (crear), PUT (reemplazar), PATCH (actualización parcial), DELETE (eliminar) |
| **Apatridia** | Cada solicitud contiene toda la información necesaria; sin estado de sesión del lado del servidor |
| **Interfaz uniforme** | Denominación coherente de recursos, métodos estándar, códigos de estado estándar |
| **Representación** | Los recursos se pueden representar en múltiples formatos (JSON, XML) |
### Convenciones de nomenclatura de recursos
| Hacer | No |
|----|-------|
| `/users`(sustantivo plural) | `/user`(singular) |
| `/users/123/orders`(anidado) | `/getOrdersForUser?id=123`|
| `/products?category=electronics`(parámetros de consulta para filtrado) | `/productsByCategory/electronics`|
| Utilice guiones:`/user-profiles`| Utilice guiones bajos:`/user_profiles`|
### Métodos HTTP e idempotencia
| Método | Propósito | ¿Idempotente? | ¿Seguro? |
|--------|---------|-------------|-------|
| **OBTENER** | Leer un recurso | ✅ Sí | ✅ Sí |
| **ENVÍO** | Crear un recurso | ❌ No | ❌ No |
| **PONER** | Reemplazar un recurso por completo | ✅ Sí | ❌ No |
| **PARCHE** | Actualizar parcialmente un recurso | ❌ No* | ❌ No |
| **ELIMINAR** | Eliminar un recurso | ✅ Sí | ❌ No |
*PATCH se puede hacer idempotente con un diseño cuidadoso.
### Códigos de estado HTTP
| Código | Significado | Cuándo utilizar |
|------|---------|-------------|
| **200** | Aceptar | OBTENER, PONER, PATCH, BORRAR con éxito |
| **201** | Creado | POST exitoso (recurso creado) |
| **204** | Sin contenido | BORRAR exitoso (nada que devolver) |
| **400** | Solicitud incorrecta | Entrada no válida o solicitud con formato incorrecto |
| **401** | No autorizado | Autenticación faltante o no válida |
| **403** | Prohibido | Autenticado pero no autorizado |
| **404** | No encontrado | El recurso no existe |
| **409** | Conflicto | Recurso duplicado o conflicto estatal |
| **422** | Entidad no procesable | JSON válido pero errores semánticos |
| **429** | Demasiadas solicitudes | Límite de tarifa excedido |
| **500** | Error interno del servidor | Error inesperado del servidor |
| **502** | Mala puerta de enlace | Fallo del servicio ascendente |
| **503** | Servicio no disponible | Sobrecarga temporal o mantenimiento |
---

## Versiones de API
Las API evolucionan. Cuando necesita realizar cambios importantes, el control de versiones permite que los clientes existentes sigan trabajando.
| Estrategia | Ejemplo | Ventajas | Contras |
|----------|---------|------|------|
| **Ruta URL** | `/v1/users`,`/v2/users`| Sencillo, explícito | Cambios de URL por versión |
| **Parámetro de consulta** | `/users?version=2`| Flexibles | Fácil de olvidar |
| **Encabezado** | `Accept: application/vnd.myapi.v2+json`| Limpiar URL | Menos reconocible |
| **Sin versiones** | Sólo evolución del esquema | Más simple | Los cambios importantes afectan a todos |
**Práctica recomendada**: utilice el control de versiones de la ruta URL (`/v1/`) para mayor claridad. Admite al menos una versión anterior. Desaprobar las versiones antiguas con cronogramas claros.
---

## Métodos de autenticación
| Método | Cómo funciona | Mejor para |
|--------|-------------|----------|
| **Claves API** | Clave secreta en el encabezado (`X-API-Key: abc123`) | Integraciones simples de servidor a servidor |
| **OAuth2** | Delegación basada en tokens con alcances | Acceso de terceros, aplicaciones autorizadas por el usuario |
| **JWT** | Token autónomo con reclamos | Autenticación sin estado entre servicios |
| **Autenticación básica** | Nombre de usuario codificado en Base64:contraseña | Solo desarrollo, nunca producción sin TLS |
| **Cookies de sesión** | ID de sesión del lado del servidor en cookie solo HTTP | Aplicaciones web tradicionales |
### Flujo de OAuth2 (simplificado)
1. El cliente redirige al usuario al servidor de autorización.
2. El usuario inicia sesión y otorga permiso.
3. El servidor de autorización devuelve un código de autorización.
4. El cliente intercambia el código por un token de acceso (y, opcionalmente, un token de actualización).
5. El cliente utiliza un token de acceso para llamar a la API.
6. Cuando el token de acceso caduque, utilice el token de actualización para obtener uno nuevo.
---

## Estilos de API: REST frente a GraphQL frente a gRPC
| Característica | DESCANSO | GráficoQL | gRPC |
|---------|------|---------|------|
| **Formato de datos** | JSON (normalmente) | JSON | Protobuf (binario) |
| **Puntos finales** | Múltiples (uno por recurso) | Punto final único | Definido por el archivo .proto |
| **Exceso de recuperación** | Común (obtenga más de lo necesario) | Ninguno (el cliente especifica campos) | Ninguno (definido por esquema) |
| **Infravalorado** | Requiere múltiples llamadas | Ninguno (obtenga exactamente lo que necesita) | Ninguno |
| **En tiempo real** | WebSockets necesarios | Suscripciones integradas | Transmisión incorporada |
| **Almacenamiento en caché** | El almacenamiento en caché HTTP funciona de forma natural | Más difícil de almacenar en caché | Limitado |
| **Curva de aprendizaje** | Bajo | Medio | Medio-alto |
| **Mejor para** | API públicas, aplicaciones CRUD | UI complejas, aplicaciones móviles | Microservicios internos de alto rendimiento |
---

## Paginación, filtrado y clasificación
Para puntos finales que devuelven listas:
| Técnica | Ejemplo | Cuándo utilizar |
|-----------|---------|-------------|
| **Compensación/Límite** | `?offset=20&limit=10`| Simple; funciona para pequeños conjuntos de datos |
| **Basado en cursor** | `?cursor=abc123&limit=10`| Grandes conjuntos de datos; resultados consistentes |
| **Conjunto de claves** | `?created_after=2024-01-01&limit=10`| Muy eficiente; requiere clave única |
```json
// Cursor-based response
{
  "data": [...],
  "pagination": {
    "next_cursor": "abc123",
    "has_more": true
  }
}
```

---

## Limitación de velocidad
Proteja su API del abuso y garantice un uso justo.
| Estrategia | Cómo funciona |
|----------|-------------|
| **Ventana fija** | N solicitudes por ventana de tiempo (por ejemplo, 100/hora) |
| **Ventana corredera** | Más granular; cuenta las solicitudes en una ventana móvil |
| **Cubo de fichas** | Tokens agregados a tasa fija; cada solicitud consume un token |
Devuelve`429 Too Many Requests`con encabezados:```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1625097600
Retry-After: 60
```

---

## Manejo de errores
Las respuestas de error consistentes hacen que sea mucho más fácil trabajar con las API:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "issue": "Invalid email format"
      }
    ]
  }
}
```

**Principios**: utilice una estructura de error coherente, incluya mensajes procesables, utilice códigos de estado HTTP estándar, registre los errores en el lado del servidor con ID de correlación y nunca exponga seguimientos de pila ni detalles internos.
---

## Documentación API
| Herramienta | Descripción |
|------|-------------|
| **OpenAPI (arrogancia)** | Estándar de la industria para la documentación de API REST |
| **Interfaz de usuario arrogante** | Documentación API interactiva de la especificación OpenAPI |
| **Cartero** | Pruebas de API, documentación y uso compartido de colecciones |
| **Redoc** | Hermosos documentos de referencia de API de la especificación OpenAPI |
| **Área de juegos GraphQL / GraphiQL** | Exploración interactiva de GraphQL |
**Mejores prácticas**: escriba primero la especificación OpenAPI (desarrollo basado en especificaciones) y luego genere la documentación y los SDK del cliente a partir de ella.
---

## Patrones de puerta de enlace API
Una puerta de enlace API se encuentra entre los clientes y los servicios backend, proporcionando un único punto de entrada.
| Responsabilidad | Descripción |
|---------------|-------------|
| **Enrutamiento** | Solicitudes directas a los servicios backend apropiados |
| **Autenticación** | Validar tokens a nivel de puerta de enlace |
| **Límite de tasa** | Aplicar límites globales o por cliente |
| **Transformación** | Convertir entre protocolos (REST ↔ gRPC) |
| **Almacenamiento en caché** | Caché de respuestas comunes |
| **Monitoreo** | Registro y métricas centralizados |
| **Equilibrio de carga** | Distribuir el tráfico entre instancias de servicio |
| Herramienta | Tipo |
|------|------|
| **Kong** | Puerta de enlace API de código abierto (basada en Nginx) |
| **Puerta de enlace API de AWS** | Totalmente administrado, integrado con AWS |
| **Administración de API de Azure** | Puerta de enlace administrada con portal para desarrolladores |
| **Enviado / Istio** | Malla de servicios con capacidades de puerta de enlace API |
| **Traefik** | Descubrimiento automático, integración de Let's Encrypt |
---

## Webhooks
Los webhooks permiten que su API envíe eventos a los clientes en tiempo real, en lugar de hacer que los clientes realicen encuestas para detectar cambios.
| Aspecto | Mejores prácticas |
|--------|--------------|
| **Entrega** | Solicitud POST con carga útil JSON a la URL del cliente |
| **Seguridad** | Firmar cargas útiles con HMAC; cliente verifica firma |
| **Confiabilidad** | Reintentar entregas fallidas con retroceso exponencial |
| **Idempotencia** | Incluya una identificación de evento única; cliente maneja duplicados |
| **Versionamiento** | Incluir la versión API en la carga útil del webhook |
---

## Lista de verificación de diseño
- [ ] Los recursos son sustantivos en plural (`/users`, no`/getUser`)
- [] Métodos HTTP utilizados correctamente (GET para lecturas, POST para creaciones, etc.)
- [] Formato de respuesta de error consistente
- [] Paginación para todos los puntos finales de la lista
- [] Limitación de tarifas con encabezados claros
- [ ] Estrategia de control de versiones de API definida
- [] Autenticación y autorización implementadas
- [] Validación de entrada en todos los puntos finales
- [] Se mantiene la documentación de OpenAPI/Swagger.
- [] CORS configurado correctamente
- [] HTTPS aplicado en producción
- [] Claves de idempotencia para operaciones POST cuando sea necesario