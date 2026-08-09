---
# Metadatos
título: "Fundamentos de ciberseguridad"
descripción: "Cifrado, TLS, OWASP, codificación segura, SDL"
categoría: "Codificación y tecnología"
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
review_by: "Equipo de base de conocimientos de codificación y tecnología"
next_review: "2027-08-05"
# Clasificación
Etiquetas: [ciberseguridad, codificación y tecnología]
nivel_dificultad: "intermedio"
requisitos previos: []
estimado_reading_time: "9 minutos"
# Guía de contribución
contribución:
  licencia: "MIT"
  feedback_channel: "Problemas de GitHub"
  how_to_contribute: "Enviar un PR con cambios y actualizar el registro de cambios"
  review_process: "Los mantenedores de categorías revisan los cambios antes de fusionarlos"
---
# Fundamentos de ciberseguridad
La seguridad no es una característica que se incorpora al final; es una disciplina que debe integrarse en cada capa de un sistema desde el primer día. Ya sea que esté creando una aplicación web, administrando infraestructura o enviando una API, comprender el panorama de amenazas y los fundamentos de la defensa es esencial.
---

## Cifrado y criptografía
### Cifrado simétrico versus asimétrico
| Tipo | Cómo funciona | Velocidad | Distribución de claves | Ejemplos |
|------|-------------|-------|-----------|----------|
| **Simétrico** | Misma clave para cifrado y descifrado | Rápido | Desafío: ¿cómo compartir la clave? | AES-256, ChaCha20 |
| **Asimétrico** | La clave pública cifra, la clave privada descifra | Más lento | La clave pública se puede compartir abiertamente | RSA, ECC (curva elíptica) |
En la práctica, la mayoría de los sistemas utilizan **ambos**: cifrado asimétrico para intercambiar de forma segura una clave simétrica y luego cifrado simétrico para la mayor parte de los datos. Así es como funciona TLS/HTTPS.
### Hashing
El hashing es una función unidireccional: convierte la entrada en una cadena de tamaño fijo. No puedes revertirlo, pero la misma entrada siempre produce la misma salida.
| Caso de uso | Algoritmo recomendado | Evitar |
|----------|----------------------|-------|
| **Almacenamiento de contraseña** | Argon2id, bcrypt, scrypt | MD5, SHA-1, SHA-256 simple (demasiado rápido) |
| **Integridad de los datos** | SHA-256, SHA-3 | MD5 (roto), SHA-1 (roto) |
| **Firmas digitales** | Ed25519, RSA-2048+ | DSA |
### TLS/HTTPS
HTTPS es HTTP sobre TLS (Seguridad de la capa de transporte). Proporciona:
- **Cifrado**: los espías no pueden leer los datos en tránsito.
- **Autenticación**: El servidor acredita su identidad mediante un certificado.
- **Integridad**: los datos no se pueden modificar en tránsito sin detección.
Utilice TLS 1.2 o 1.3. Deshabilite TLS 1.0 y 1.1. Habilite HSTS (HTTP Strict Transport Security) para obligar a los navegadores a utilizar siempre HTTPS.
---

## Autenticación y autorización
### Autenticación: ¿Quién eres?
| Método | Nivel de seguridad | Caso de uso |
|--------|---------------|----------|
| **Contraseña** | Bajo-Medio | Cuentas básicas (aplicar más de 12 caracteres, verificar si hay infracciones) |
| **AMF (TOTP)** | Alto | Estándar para cuentas confidenciales (Google Authenticator, Authy) |
| **Clave de hardware (FIDO2/WebAuthn)** | Muy Alto | Cuentas de alta seguridad (YubiKey) |
| **Biométrico** | Medio-alto | Desbloqueo del dispositivo (huella digital, rostro): no es excelente como único factor |
| **OAuth2 / OIDC** | Alto | Inicio de sesión de terceros ("Iniciar sesión con Google") |
**Reglas de contraseña**: aplique una longitud mínima (12 a 16 caracteres), verifique las listas de contraseñas violadas, use Argon2id o bcrypt para hash con sales por usuario.
### Autorización: ¿Qué puedes hacer?
| Modelo | Descripción | Ejemplo |
|-------|-------------|---------|
| **RBAC** (Control de acceso basado en roles) | Permisos asignados a roles; los usuarios obtienen roles | Administrador, editor, visor |
| **ABAC** (Basado en atributos) | Reglas basadas en atributos de usuario, recursos, entorno | "Los directivos pueden aprobar las solicitudes de su equipo" |
| **ACL** (Lista de control de acceso) | Permisos explícitos por usuario/recurso | Permisos de archivos (lectura/escritura/ejecución) |
**Principio de privilegio mínimo**: brinde a cada usuario, servicio y proceso solo el acceso mínimo que necesita.
### JWT (tokens web JSON)
| Aspecto | Recomendación |
|--------|---------------|
| **Firma** | Se prefiere RS256 o ES256 (asimétrico); HS256 aceptable con secretos administrados |
| **Vencimiento** | 15 a 60 minutos para tokens de acceso; utilice tokens de actualización para sesiones más largas |
| **Almacenamiento** | Cookies solo HTTP (no localStorage, vulnerables a XSS) |
| **Validación** | Verifique siempre firma, emisor, audiencia y vencimiento |
---

## Top 10 de OWASP (2021)
OWASP Top 10 es el documento de concientización estándar para la seguridad de aplicaciones web. Representa los riesgos más críticos:
| # | Riesgo | Lo que significa |
|---|------|--------------|
| 1 | **Control de acceso roto** | Los usuarios pueden acceder a recursos que no deberían |
| 2 | **Fallos criptográficos** | Cifrado débil o faltante para datos confidenciales |
| 3 | **Inyección** | SQL, NoSQL, comando OS o inyección LDAP |
| 4 | **Diseño inseguro** | Defectos arquitectónicos que no se pueden solucionar con la implementación |
| 5 | **Mal configuración de seguridad** | Contraseñas predeterminadas, puertos abiertos, mensajes de error detallados |
| 6 | **Componentes vulnerables** | CVE conocidos en dependencias |
| 7 | **Errores de autenticación** | Contraseñas débiles, mala gestión de sesiones |
| 8 | **Fallos de integridad** | Ataques a la cadena de suministro, actualizaciones sin firmar |
| 9 | **Errores de registro/monitoreo** | No se detectan infracciones |
| 10 | **SSRF** | Servidor engañado para realizar solicitudes a sistemas internos |
---

## Prácticas de codificación segura
### Validación de entrada
| Regla | Por qué |
|------|-----|
| **Lista blanca > Lista negra** | Defina lo que está permitido, no lo que está bloqueado |
| **Consultas parametrizadas** | Nunca concatene la entrada del usuario en SQL: use declaraciones preparadas u ORM |
| **Codificación HTML** | Codifique `<`, `>`, `&`, `"`,`'`para evitar XSS |
| **Caparazón escapando** | Evite crear comandos de shell a partir de la entrada del usuario; utilizar`shlex.quote()`|
| **Límites de longitud** | Aplicar longitudes máximas para evitar desbordamientos de búfer y DoS |
| **Comprobación de tipos** | Asegúrese de que los números enteros sean números enteros y los booleanos sean booleanos |
### Vulnerabilidades comunes
| Vulnerabilidad | Ataque | Defensa |
|--------------|--------|---------|
| **Inyección SQL** | `' OR 1=1 --`en formulario de inicio de sesión | Consultas parametrizadas |
| **XSS** | `<script>alert('hacked')</script>`en el campo de comentarios | Codificación de salida, Política de seguridad de contenido |
| **CSRF** | Engañar al navegador del usuario para que realice una solicitud no autorizada | Fichas CSRF, cookies SameSite |
| **Recorrido de ruta** | `../../etc/passwd`en el parámetro de archivo | Validar y desinfectar rutas de archivos |
| **IDOR** | Cambie`/user/123`a`/user/124`para ver los datos de otra persona | Verificaciones de autorización en cada solicitud |
---

## Seguridad de la red
### Cortafuegos
| Tipo | Descripción |
|------|-------------|
| **Filtrado de paquetes** | Reglas basadas en IP, puerto, protocolo |
| **Con estado** | Realiza un seguimiento de los estados de conexión; filtrado más inteligente |
| **Nivel de aplicación (WAF)** | Inspecciona el tráfico HTTP; bloquea la inyección SQL, XSS, etc. |
| **Grupos de seguridad en la nube** | Firewalls virtuales para instancias en la nube (AWS SG, Azure NSG) |
**Regla general**: bloquear todo el tráfico entrante de forma predeterminada; abra solo lo que se necesita explícitamente (80, 443 para web).
### Segmentación de red
Coloque bases de datos y cachés en subredes privadas sin acceso directo a Internet. Utilice una DMZ para servicios públicos (servidores web, equilibradores de carga). Aplicar el principio de privilegio mínimo al acceso a la red.
---

## Gestión de secretos
### La regla de oro
**Nunca codifique secretos.** No hay claves API, contraseñas ni URL de bases de datos en el código fuente. No hay secretos en las variables de entorno comprometidas con Git. No hay secretos en las imágenes de Docker.
### Herramientas
| Herramienta | Tipo | Mejor para |
|------|------|----------|
| **Bóveda de HashiCorp** | Gerente de secretos empresariales | Secretos dinámicos, cifrado como servicio |
| **Administrador de secretos de AWS** | Nativo de la nube | Entornos AWS |
| **Bóveda de claves de Azure** | Nativo de la nube | Entornos Azure |
| **SOPS** | Archivos cifrados | Cifrar secretos en Git (con KMS o GPG) |
| **Secretos de Docker** | Nativo del contenedor | Docker Swarm (para K8, considere Secrets Store CSI) |
| **dotenv (.env)** | Desarrollo local | Sólo desarrollo, nunca en producción ni comprometido |
### Rotación
Rota los secretos de forma regular y automática. Si se filtra un secreto (por ejemplo, si se envía a un repositorio público), rótelo inmediatamente, incluso si cree que nadie lo vio.
---

## Seguridad de dependencia
Su aplicación es tan segura como su dependencia más débil.
### Herramientas de escaneo
| Idioma | Herramientas |
|----------|-------|
| **Python** |  `safety`, `pip-audit`,`bandit`|
| **Nodo.js** |  `npm audit`, `yarn audit`,`snyk`|
| **Óxido** | `cargo audit`|
| **Ir** | `govulncheck`|
| **Generalidades** | `Dependabot`(GitHub), `Renovate`,`Trivy`|
### Integridad de la cadena de suministro
- Utilice archivos de bloqueo (`package-lock.json`, `Cargo.lock`, `go.sum`) para compilaciones reproducibles.
- Verificar sumas de verificación de las dependencias descargadas.
- Preferir registros oficiales y editores verificados.
- Automatizar actualizaciones menores/parches a través de Dependabot o Renovate.
---

## Ciclo de vida de desarrollo de seguridad (SDL)
| Fase | Actividad |
|-------|----------|
| **Entrenamiento** | Asegúrese de que los desarrolladores comprendan las vulnerabilidades comunes |
| **Modelado de amenazas** | Identificar amenazas potenciales durante el diseño |
| **Estándares de codificación segura** | Aplicar mediante linters y listas de verificación de revisión de código |
| **SAST** | Análisis estático de código fuente (SonarQube, CodeQL) |
| **DAST** | Análisis dinámico de la aplicación en ejecución (OWASP ZAP, Burp Suite) |
| **SCA** | Análisis de composición de software: dependencias de escaneo |
| **Pruebas de penetración** | Ejercicios periódicos de piratería ética |
| **Recompensa por errores** | Alentar a investigadores externos a encontrar vulnerabilidades |
| **Plan de respuesta a incidentes** | Tener un plan claro para cuando se detecte una infracción |
---

## Lista de verificación de emergencia
Cuando sospecha de una infracción:
1. **No entre en pánico**, pero actúe rápidamente.
2. **Aislar** los sistemas afectados (desconectarlos de la red si es necesario).
3. **Conservar evidencia**: capturar registros, volcados de memoria, imágenes de disco.
4. **Identificar el alcance**: ¿qué sistemas, qué datos?
5. **Rote** todas las credenciales y secretos comprometidos.
6. **Parchear** la vulnerabilidad.
7. **Notificar** a los usuarios y reguladores afectados si es necesario (dentro de los plazos legales).
8. **Autopsia**: documente la causa raíz y las medidas a tomar en un plazo de 24 a 48 horas.