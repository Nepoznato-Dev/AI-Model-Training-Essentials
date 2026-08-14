---
# Metadata
title: "Security Best Practices"
description: "OWASP Top 10, input validation, auth, secrets management"
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
tags: [security, best, practices, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Mejores prácticas de seguridad
Una guía práctica para proteger aplicaciones, infraestructura y datos, desde el desarrollo hasta la producción.
---

## OWASP Top 10 (2021): descripción general
1. **Control de acceso roto**: los usuarios pueden acceder a recursos que no deberían.
2. **Fallos criptográficos**: cifrado débil o faltante.
3. **Inyección**: SQL, NoSQL, comando del sistema operativo o inyección LDAP.
4. **Diseño inseguro**: Defectos arquitectónicos.
5. **Configuración incorrecta de seguridad**: contraseñas predeterminadas, puertos abiertos, errores detallados.
6. **Componentes vulnerables y obsoletos**: CVE conocidos en dependencias.
7. **Fallos de identificación y autenticación**: Contraseñas débiles, mala gestión de sesiones.
8. **Fallos de integridad de datos y software**: ataques a la cadena de suministro, actualizaciones no firmadas.
9. **Fallos de monitoreo y registro de seguridad**: No se detectan infracciones.
10. **Falsificación de solicitudes del lado del servidor (SSRF)**: Abuso del servidor para realizar solicitudes a sistemas internos.
---

## Validación de entrada y codificación de salida
### Reglas de validación
- **Lista blanca > Lista negra**: defina patrones permitidos (por ejemplo, expresiones regulares para correo electrónico) en lugar de bloquear patrones incorrectos conocidos.
- **Límites de longitud**: aplique longitudes máximas para evitar desbordamientos del búfer y DoS.
- **Comprobación de tipos**: asegúrese de que los números enteros sean números enteros y los valores booleanos sean booleanos.
- **Utilice bibliotecas bien probadas**: para la validación de correo electrónico, URL y fecha, utilice bibliotecas estándar (por ejemplo,`email-validator`en Python,`validator.js`en Node).
### Codificación de salida
- **Codificación HTML**: Codifique `<`, `>`, `&`, `"`,`'`para evitar XSS.
- **Parametrización SQL**: nunca concatene la entrada del usuario en consultas SQL. Utilice consultas parametrizadas (declaraciones preparadas) o un ORM.
- **Escapado de Shell**: evite crear comandos de Shell a partir de la entrada del usuario; si es inevitable, utilice`shlex.quote()`o similar.
---

## Autenticación y autorización
### Gestión de contraseñas
- **Hashing**: almacene contraseñas con un algoritmo de hashing lento y potente: **Argon2id** (preferido), **bcrypt**, **scrypt** o **PBKDF2**.
- **Salado**: agrega una sal única por usuario.
- **Longitud mínima**: aplique al menos 12 a 16 caracteres.
- **MFA (Autenticación multifactor)**: requiere un segundo factor (TOTP, SMS, clave de hardware) para operaciones confidenciales.
- **Limitación de velocidad**: evita intentos de fuerza bruta en puntos finales de inicio de sesión (por ejemplo, 5 intentos cada 5 minutos por IP/usuario).
### Gestión de sesiones
- Utilice cookies SameSite seguras, solo HTTP, para tokens de sesión.
- Establecer tiempos de vencimiento adecuados.
- Invalidar sesiones al cerrar sesión y al cambiar de contraseña.
- Evite exponer los ID de sesión en las URL.
### OAuth2 / OIDC
- Utilice bibliotecas bien establecidas (por ejemplo, Authlib, PyJWT, Passport.js, Spring Security).
- Validar minuciosamente los tokens de identificación (firma, emisor, audiencia, vencimiento).
- Utilice parámetros de estado para evitar CSRF.
- Mantener la confidencialidad de los secretos del cliente.
### JWT (tokens web JSON)
- **Señal**: utilice RS256 o ES256 (asimétrico) para mayor seguridad; HS256 (simétrico) es aceptable si los secretos compartidos se gestionan bien.
- **Validar**: Verifique siempre la firma, el emisor (`iss`), la audiencia (`aud`) y el vencimiento (`exp`).
- **Mantener una caducidad corta**: entre 15 y 60 minutos para los tokens de acceso; utilice tokens de actualización para sesiones más largas.
- **Almacenar de forma segura**: nunca almacene archivos JWT en localStorage (vulnerable a XSS); utilice cookies solo HTTP en su lugar.
---

## Seguridad API
### Autenticación
- Autenticar siempre las llamadas API (excepto los puntos finales públicos).
- Prefiera claves API o tokens OAuth2 a la autenticación básica (que envía credenciales en cada solicitud).
### Limitación y estrangulamiento de velocidad
- Aplique límites de velocidad por usuario y por IP para evitar abusos y DoS.
- Devuelve`429 Too Many Requests`con un encabezado `Retry-After`.
### CORS (intercambio de recursos entre orígenes)
- Permitir sólo orígenes específicos (nunca`*`en producción).
- Validar el encabezado`Origin`en el lado del servidor.
### Validación de entrada
- Validar todos los parámetros de la solicitud, incluidos los encabezados y el cuerpo.
- Rechazar campos inesperados (`"strict": true` o`additionalProperties: false`en esquema JSON).
### HTTPS/TLS
- Aplicar HTTPS en producción.
- Utilice HSTS (HTTP Strict Transport Security) para obligar a los navegadores a utilizar HTTPS.
- Utilice TLS 1.2 o 1.3 (deshabilite TLS 1.0/1.1).
---

## Gestión de secretos
### Nunca codifiques secretos
- No envíe secretos (claves API, contraseñas, URL de bases de datos) al control de fuente.
- Utilizar variables de entorno o herramientas de gestión de secretos.
### Herramientas
| Herramienta | Descripción |
|------|-------------|
| **Bóveda de HashiCorp** | Secretos dinámicos y de nivel empresarial |
| **AWS Secrets Manager/Azure Key Vault/GCP Secret Manager** | Nativo de la nube |
| **SOPS** | Cifrar secretos en archivos y confirmarlos (con KMS o GPG) |
| **Secretos de Docker** | Para el modo Enjambre; Secretos de Kubernetes (considere el controlador CSI externo de Secrets Store) |
### Rotación
- Rotar periódicamente secretos y cuentas de servicio.
- Automatizar la rotación cuando sea posible.
---

## Gestión de dependencias
### Escaneo de vulnerabilidades
| Idioma/Plataforma | Herramientas |
|-------------------|-------|
| **Python** |  `safety`, `pip-audit`,`bandit`|
| **Nodo** |  `npm audit`, `yarn audit`,`snyk`|
| **Óxido** | `cargo audit`|
| **Ir** | `govulncheck`|
| **Generalidades** | `Dependabot`(GitHub), `Renovate`,`Trivy`|
### Parcheo
- Mantener las dependencias actualizadas a versiones parcheadas.
- Configurar solicitudes de extracción automáticas para actualizaciones menores o de parches.
- Revisar los registros de cambios para detectar cambios importantes.
### Integridad de la cadena de suministro
- Utilice archivos de bloqueo de paquetes (`package-lock.json`, `Cargo.lock`, `go.sum`) para garantizar compilaciones reproducibles.
- Verificar sumas de verificación de las dependencias descargadas.
- Prefiere registros oficiales y confía únicamente en editores verificados.
---

## Seguridad de infraestructura
### Cortafuegos
- Bloquear todos los puertos de entrada excepto aquellos explícitamente necesarios (por ejemplo, 80, 443).
- Limite el acceso SSH a rangos de IP específicos (o use una VPN/host bastión).
- Utilice grupos de seguridad (AWS) o NSG (Azure) para un control detallado.
### Endurecimiento del sistema operativo
- Aplicar actualizaciones de seguridad periódicamente (`sudo apt upgrade`, `yum update`).
- Desactivar servicios innecesarios y cuentas predeterminadas.
- Utilice fail2ban para bloquear intentos de fuerza bruta en SSH.
- Reforzar SSH: deshabilitar el inicio de sesión de root, usar autenticación basada en claves, cambiar el puerto predeterminado (opcional).
### Segmentación de red
- Coloque bases de datos y cachés en subredes privadas sin acceso a Internet.
- Utilice una DMZ para servicios públicos.
- Aplicar el principio de privilegio mínimo al acceso a la red.
### Secretos en infraestructura
- Nunca almacene secretos en variables de entorno CI/CD a menos que estén cifrados.
- Utilice las funciones de IAM del proveedor de la nube para instancias EC2/VM en lugar de claves de larga duración.
---

## Registro y monitoreo
### Qué registrar
- Eventos de autenticación (éxito/fracaso).
- Decisiones de control de acceso (fallos de autorización).
- Acciones de administrador (creación de usuarios, eliminación, cambios de permisos).
- Cambios en el esquema de la base de datos.
- Errores y excepciones del sistema.
- Solicitudes y respuestas de API (redactar datos confidenciales).
### Qué no registrar
- Contraseñas, secretos, tokens, PII (información de identificación personal) a menos que estén codificados o redactados.
- Números completos de tarjetas de crédito.
### Alerta
- Configurar alertas para:
  - Múltiples inicios de sesión fallidos (potencial fuerza bruta).
  - Patrones de acceso inusuales (por ejemplo, desde nuevas ubicaciones, en horas impares).
  - Nuevas cuentas de administrador creadas.
  - Altas tasas de error o picos de latencia.
- Utilice un SIEM (Gestión de eventos e información de seguridad) para correlación avanzada.
### Retención de registros
- Conserve los registros durante al menos 30 a 90 días, según los requisitos reglamentarios.
- Almacenar registros en un sistema centralizado a prueba de manipulaciones (por ejemplo, ELK Stack, Splunk, Datadog).
---

## Ciclo de vida de desarrollo seguro (SDL)
1. **Capacitación**: asegúrese de que los desarrolladores comprendan las vulnerabilidades comunes.
2. **Modelado de amenazas**: identifique amenazas potenciales en las primeras etapas del diseño.
3. **Estándares de codificación segura**: Aplicar mediante linters y listas de verificación de revisión de código.
4. **SAST** (Prueba de seguridad de aplicaciones estáticas): escanea el código fuente en busca de vulnerabilidades (SonarQube, CodeQL).
5. **DAST** (Prueba dinámica de seguridad de aplicaciones): escanea aplicaciones en ejecución (OWASP ZAP, Burp Suite).
6. **SCA** (Análisis de composición de software): escanea dependencias.
7. **Pruebas de penetración**: ejercicios periódicos de piratería ética.
8. **Recompensa por errores**: anime a los investigadores externos a encontrar vulnerabilidades de manera responsable.
9. **Plan de respuesta a incidentes**: tenga un plan claro para cuando se detecte una infracción.
---

## Lista de verificación de emergencia (cuando se sospecha una infracción)
1. **No entre en pánico**, pero actúe rápidamente.
2. **Aislar** los sistemas afectados (desconectarlos de la red si es necesario).
3. **Conservar evidencia**: Capture registros, volcados de memoria e imágenes de disco.
4. **Identificar** el alcance: qué sistemas, qué datos.
5. **Rote** todas las credenciales y secretos comprometidos.
6. **Parchear** la vulnerabilidad.
7. **Notificar** a los usuarios y organismos reguladores afectados si es necesario (dentro de los plazos legales).
8. **Realice una autopsia** para comprender la causa raíz y mejorar los procesos.