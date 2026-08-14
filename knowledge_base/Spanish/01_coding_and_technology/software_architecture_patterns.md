<!--
---
# Metadata
title: "Software Architecture Patterns"
description: "Monolith, microservices, event-driven, DDD, caching, SOLID"
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
tags: [software, architecture, patterns, coding-and-technology]
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

-->
# Patrones de arquitectura de software
La arquitectura es el conjunto de decisiones estructurales sobre cómo se organiza un sistema: qué componentes tiene, cómo se comunican y dónde recaen las responsabilidades. Una buena arquitectura hace que un sistema sea fácil de entender, modificar y escalar. La mala arquitectura hace que cada cambio sea una lucha. Este archivo cubre los patrones principales, cuándo usar cada uno y las compensaciones involucradas.
---

## Monolito vs Microservicios
Esta es la decisión arquitectónica más fundamental y vale la pena hacerlo bien.
| Aspecto | Monolito | Microservicios |
|--------|----------|---------------|
| **Estructura** | Unidad desplegable única | Muchos servicios pequeños que se pueden implementar de forma independiente |
| **Datos** | Base de datos compartida | Cada servicio es dueño de sus datos |
| **Comunicación** | Llamadas a funciones en proceso | Llamadas de red (HTTP, gRPC, mensajería) |
| **Escalado** | Escalar toda la aplicación | Escalar servicios individuales |
| **Implementación** | Ciclo de lanzamiento único | Despliegues independientes |
| **Complejidad** | Más sencillo de desarrollar inicialmente | Complejidad operativa (conexión en red, seguimiento) |
| **Mejor para** | Equipos pequeños, productos en etapa inicial | Grandes equipos, dominios complejos, gran escala |
### Cuándo empezar con un monolito
La mayoría de las aplicaciones deberían comenzar como un monolito. Es más sencillo de construir, probar, implementar y depurar. Siempre podrás extraer servicios más adelante, cuando tengas una idea más clara de los límites de tu dominio. A esto a veces se le llama "monolito modular", un monolito con límites internos limpios que facilitan la extracción posterior.
### Cuándo optar por los microservicios
Considere los microservicios cuando:
- Los equipos son lo suficientemente grandes como para que la coordinación se convierta en un cuello de botella.
- Las diferentes partes del sistema tienen requisitos de escala muy diferentes.
- Necesita una implementación independiente de componentes.
- Su dominio tiene contextos delimitados claros (consulte DDD a continuación).
---

## Arquitectura en capas (N-Nivel)
El patrón arquitectónico más común. El código está organizado en capas, cada una con una responsabilidad específica.
```
â”Œ─────────────────────────┐
│   Presentation Layer    │  ← UI, controllers, API endpoints
├─────────────────────────┤
│   Application Layer     │  ← Use cases, orchestration
├─────────────────────────┤
│   Domain Layer          │  ← Business logic, entities
├─────────────────────────┤
│   Infrastructure Layer  │  ← Database, external services, file I/O
└─────────────────────────┘
```

| Capa | Responsabilidad | Regla |
|-------|---------------|------|
| **Presentación** | Manejar solicitudes de usuario/HTTP | Solo puede llamar a la capa de aplicación |
| **Solicitud** | Orquestar casos de uso | Puede llamar a la capa de dominio |
| **Dominio** | Lógica empresarial central | No debería depender de otras capas |
| **Infraestructura** | Preocupaciones técnicas | Implementa interfaces definidas en Dominio |
**Regla clave**: las dependencias apuntan hacia adentro. La capa de dominio no conoce la base de datos ni el marco web.
---

## Arquitectura basada en eventos
Los componentes se comunican emitiendo y reaccionando a **eventos**: cosas que han sucedido.
| Patrón | Descripción |
|---------|-------------|
| **Notificación de evento** | El servicio A emite "Pedido realizado"; servicios B, C, D reaccionan |
| **Abastecimiento de eventos** | Almacene todos los cambios de estado como una secuencia de eventos (no solo el estado actual) |
| **CQR** | Separe el modelo de lectura (consultas) del modelo de escritura (comandos) |
### Búsqueda de eventos
En lugar de almacenar el "estado actual" en una base de datos, almacene cada cambio de estado como un evento:
```
OrderCreated(order_id=123, total=$50)
OrderPaid(order_id=123, payment_id=456)
OrderShipped(order_id=123, tracking=ABC)
```

Beneficios: pista de auditoría completa, capacidad de reconstruir cualquier estado anterior, consumidores desacoplados. Desafíos: evolución del esquema de eventos, consistencia eventual, complejidad de depuración.
### CQRS (Segregación de responsabilidad de consulta de comando)
| Lado | Propósito | Base de datos |
|------|---------|----------|
| **Comando (Escribir)** | Manejar mutaciones; hacer cumplir las reglas comerciales | Optimizado para escrituras (normalizado) |
| **Consulta (Leer)** | Servir solicitudes de lectura | Optimizado para lecturas (desnormalizado) |
CQRS se combina naturalmente con Event Sourcing: los eventos del lado de escritura se proyectan en vistas optimizadas para lectura.
---

## Colas de mensajes y agentes de eventos
Cuando los servicios necesitan comunicarse de forma asincrónica, las colas de mensajes son la columna vertebral.
| Herramienta | Tipo | Mejor para |
|------|------|----------|
| **Apache Kafka** | Registro de eventos distribuido | Transmisión de eventos de alto rendimiento, abastecimiento de eventos |
| **ConejoMQ** | Agente de mensajes con enrutamiento | Colas de tareas, patrones de enrutamiento complejos |
| **AWS SQS** | Cola gestionada | Cola simple y nativa de AWS |
| **AWS SNS** | Notificación de publicación/suscripción | Distribución en abanico para múltiples suscriptores |
| **Google Pub/Sub** | Publicación/suscripción gestionada | Transmisión de eventos nativos de GCP |
| **Transmisiones de Redis** | Corriente ligera | Registro de eventos simple y casos de uso de almacenamiento en caché |
### Patrones de mensajería
| Patrón | Descripción |
|---------|-------------|
| **Punto a punto** | Un productor, un consumidor por mensaje |
| **Publicar/Suscribirse** | Un productor, múltiples suscriptores |
| **Solicitar/Responder** | Estilo síncrono sobre transporte asíncrono |
| **Cola de mensajes no entregados** | Los mensajes que no se procesan pasan a una cola separada para su inspección |
---

## Diseño basado en dominio (DDD)
DDD es un enfoque estratégico para el diseño de software que centra el código en conceptos comerciales en lugar de preocupaciones técnicas.
### Conceptos clave
| Concepto | Descripción |
|---------|-------------|
| **Contexto limitado** | Un límite dentro del cual un modelo de dominio es consistente (por ejemplo, "Pedidos", "Envío", "Facturación") |
| **Lenguaje ubicuo** | Vocabulario compartido entre desarrolladores y expertos en el dominio |
| **Agregados** | Grupos de entidades relacionadas tratadas como una sola unidad para cambios de datos |
| **Entidades** | Objetos con identidad (por ejemplo, un usuario con un user_id) |
| **Objetos de valor** | Objetos sin identidad; definido por sus atributos (por ejemplo, dinero, dirección) |
| **Eventos de dominio** | Algo que sucedió en el dominio (por ejemplo, OrderPlaced) |
| **Capa Anticorrupción** | Capa de traducción entre tu dominio y sistemas externos |
### Cuando DDD ayuda
DDD es más valioso cuando el ámbito empresarial es complejo: piense en el comercio electrónico, la logística, los servicios financieros y la atención sanitaria. Si su dominio es simple (un blog, una aplicación de tareas pendientes), DDD es excesivo.
---

## Estrategias de almacenamiento en caché
El almacenamiento en caché es una de las formas más efectivas de mejorar el rendimiento, pero introduce complejidad en torno a la coherencia.
| Estrategia | Descripción | Compensación |
|----------|-------------|-----------|
| **Caché aparte** | La aplicación comprueba primero el caché; cargas desde DB en caso de fallo | Simple; coherencia final |
| **Escritura simultánea** | Escribir en caché y base de datos simultáneamente | Coherente; escrituras más lentas |
| **Escritura retrasada** | Escribir en caché; escritura asíncrona en DB | Escrituras rápidas; riesgo de pérdida de datos |
| **Lectura completa** | La caché se carga desde la base de datos en caso de error de forma transparente | Más simple que guardar caché |
### Qué almacenar en caché
| Capa | Qué | Herramientas |
|-------|------|-------|
| **CDN** | Activos estáticos, respuestas API | CloudFront, Cloudflare |
| **Solicitud** | Resultados calculados, datos de sesión | Redis, Memcached |
| **Base de datos** | Resultados de la consulta, filas a las que se accede con frecuencia | Caché de consultas, vistas materializadas |
**La invalidación de la caché** es muy difícil. Estrategias comunes: TTL (tiempo de vida), invalidación basada en eventos (borrar caché al cambiar los datos) y desalojo LRU (uso menos reciente).
---

## Patrones de diseño
### Principios SÓLIDOS
| Principio | Lo que significa |
|-----------|--------------|
| **S** — Responsabilidad única | Una clase debería tener una razón para cambiar |
| **O** — Abierto/Cerrado | Abierto para prórroga, cerrado para modificación |
| **L** — Sustitución de Liskov | Los subtipos deben ser sustituibles por sus tipos base |
| **I** — Segregación de interfaz | Muchas interfaces específicas > una interfaz de propósito general |
| **D** — Inversión de dependencia | Depende de abstracciones, no de concreciones |
### Patrones comunes
| Patrón | Intención | Ejemplo |
|---------|--------|---------|
| **Único** | Asegúrese de que una clase tenga solo una instancia | Grupo de conexiones de base de datos |
| **Fábrica** | Crear objetos sin especificar clase exacta | `UserFactory.create(type="admin")`|
| **Observador** | Notificar a los dependientes cuando cambie el estado | Oyentes de eventos, pub/sub |
| **Estrategia** | Intercambiar algoritmos en tiempo de ejecución | Estrategia de pago: Tarjeta de crédito, PayPal, Cripto |
| **Repositorio** | Acceso a datos abstractos detrás de una interfaz limpia | `UserRepository.find_by_id(123)`|
| **Decorador** | Agregar comportamiento dinámicamente | Decorador de registro en torno a un servicio |
| **Adaptador** | Hacer que las interfaces incompatibles funcionen juntas | Adaptador API heredado |
---

## Elegir la arquitectura adecuada
No existe una arquitectura universalmente "mejor". La elección correcta depende de:
| factor | Favorezca el monolito cuando... | Favorecer los microservicios cuando... |
|--------|------------------------|------------------------------|
| **Tamaño del equipo** | < 10 developers | >20 desarrolladores, múltiples equipos |
| **Complejidad del dominio** | Simple o bien entendido | Contextos complejos y muchos acotados |
| **Requisitos de escala** | Necesidades de escala uniforme | Diferentes componentes necesitan diferente escala |
| **Cadencia de implementación** | Ciclo de lanzamiento único | Se necesitan implementaciones independientes |
| **Diversidad tecnológica** | Una pila está bien | Diferentes servicios necesitan diferentes tecnologías |
**Consejos prácticos**: empieza con un monolito modular. Extraiga servicios solo cuando tenga una necesidad clara y límites de dominio claros. Los microservicios prematuros son uno de los errores arquitectónicos más comunes en la industria.