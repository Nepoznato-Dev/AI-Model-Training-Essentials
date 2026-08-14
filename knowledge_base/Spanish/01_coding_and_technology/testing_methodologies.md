---
# Metadata
title: "Testing Methodologies"
description: "Unit, integration, E2E, TDD, BDD, test pyramids"
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
tags: [testing, methodologies, coding-and-technology]
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
# Metodologías de prueba
Las pruebas son la forma de ganar confianza en que su código funciona y, lo que es más importante, en que los cambios no rompan lo que ya funciona. Las buenas pruebas detectan errores antes que los usuarios, documentan el comportamiento esperado y permiten una refactorización valiente. Este archivo cubre el espectro completo de estrategias de prueba, desde pruebas unitarias hasta pruebas de un extremo a otro, y los principios que hacen que las pruebas sean efectivas.
---

## La pirámide de pruebas
La pirámide de pruebas describe la distribución ideal de las pruebas en un proyecto.
```
        /  E2E  \          ← Few; slow; expensive; test the whole system
       /─────────\
      / Integration\       ← Some; test how components work together
     /───────────────\
    /   Unit Tests    \    ← Many; fast; cheap; test individual functions
   /─────────────────────\
```

| Nivel | Contar | Velocidad | Costo | Qué prueba |
|-------|-------|-------|------|---------------|
| **Unidad** | Muchos | Rápido (ms) | Bajo | Funciones individuales, clases, métodos |
| **Integración** | Algunos | Medio (100 ms-s) | Medio | Cómo interactúan los componentes; consultas de bases de datos; Llamadas API |
| **E2E** | Pocos | Lento (segundos-minutos) | Alto | El usuario completo fluye a través del sistema real |
---

## Prueba unitaria
Probar unidades individuales de código de forma aislada.
### Principios
| Principio | Descripción |
|-----------|-------------|
| **Rápido** | Cada prueba debe ejecutarse en milisegundos |
| **Aislado** | Las pruebas no dependen unas de otras; sin estado compartido |
| **Determinista** | Misma entrada → misma salida cada vez (sin aleatoriedad, sin dependencia del tiempo) |
| **Autocomprobación** | La prueba pasa o falla automáticamente; sin inspección manual |
| **Oportuno** | Escrito al lado o antes del código (TDD) |
### Anatomía de una prueba
| Fase | Descripción |
|-------|-------------|
| **Organizar** | Configurar los datos de prueba y las dependencias |
| **Actuar** | Llame a la función o método que se está probando |
| **Afirmar** | Verifique que el resultado coincida con las expectativas |
### Qué probar
| Categoría | Ejemplos |
|----------|---------|
| **Feliz camino** | Los insumos normales producen los resultados esperados |
| **Casos extremos** | Entrada vacía, nula, cero, valores máximos, elemento único |
| **Casos de error** | Entrada no válida, datos faltantes, permiso denegado |
| **Condiciones de contorno** | Uno por uno; exactamente en los límites |
### Burlarse y aplastar
| Término | Descripción | Cuándo utilizar |
|------|-------------|-------------|
| **Simulacro** | Un objeto falso que registra cómo se llamaba | Verificación de interacciones (¿se llamó este método?) |
| **Talón** | Un objeto falso que devuelve valores predeterminados | Proporcionar datos de prueba (devolver a este usuario de la base de datos) |
| **Espía** | Un contenedor que registra llamadas a un objeto real | Verificación parcial |
| **Falso** | Una implementación simplificada pero funcional | Base de datos en memoria para pruebas |
| Biblioteca burlona | Idioma |
|----------------|--------|
| **prueba unitaria.mock** | Pitón |
| **Broma** | JavaScript/Mecanografiado |
| **Mockito** | Java |
| **Pedido mínimo** | C# |
| **testificar / burlarse** | Ir |
---

## Pruebas de integración
Probar cómo funcionan varios componentes juntos.
| Qué probar | Ejemplo |
|-------------|---------|
| **Consultas a bases de datos** | ¿El ORM produce SQL correcto? ¿Se utilizan índices? |
| **Puntos finales API** | ¿Funciona el ciclo completo de solicitud-respuesta? |
| **Interacciones de servicio** | ¿El servicio A llama correctamente al servicio B? |
| **Dependencias externas** | ¿Funciona la integración de la pasarela de pago? |
### Estrategias
| Estrategia | Descripción | Compensación |
|----------|-------------|-----------|
| **Dependencias reales** | Utilice una base de datos real, cola de mensajes real | Más realista; Más lento; más difícil de configurar |
| **Contenedores de prueba** | Haga girar los contenedores Docker para cada ejecución de prueba | Buen equilibrio; reproducible |
| **Alternativas en memoria** | H2 en lugar de PostgreSQL; bus de mensajes en memoria | Rápido; puede pasar por alto cuestiones del mundo real |
| **Pruebas por contrato** | Verificar que los servicios cumplan con sus contratos API | Capta cambios en la interfaz |
---

## Pruebas de extremo a extremo (E2E)
Probando el sistema completo desde la perspectiva del usuario.
| Herramienta | Tipo | Mejor para |
|------|------|----------|
| **Dramaturgo** | Automatización del navegador | Aplicaciones web; navegador cruzado |
| **Ciprés** | Automatización del navegador | Aplicaciones web; experiencia de desarrollador |
| **Selenio** | Automatización del navegador | Legado; amplio soporte de idiomas |
| **Desintoxicación** | Móvil E2E | Reaccionar aplicaciones nativas |
| **Apio** | Móvil E2E | Aplicaciones móviles nativas e híbridas |
| **Maestro** | Móvil E2E | Aplicaciones móviles; sintaxis YAML simple |
| **k6 / Langosta** | Pruebas de carga | Rendimiento bajo carga |
### Mejores prácticas de E2E
| Práctica | Por qué |
|----------|-----|
| **Prueba solo rutas críticas** | Las pruebas E2E son lentas; céntrate en lo que más importa |
| **Usar fábricas de datos de prueba** | Cree datos de prueba mediante programación; no confíe en los datos de semillas |
| **Limpieza después de las pruebas** | Cada prueba debe dejar el sistema en un estado conocido |
| **Evite probar los detalles de la interfaz de usuario** | Comportamiento de prueba, no clases CSS o posiciones de elementos |
| **Ejecutar en CI** | Las pruebas E2E deben ejecutarse automáticamente en cada cambio |
---

## Desarrollo basado en pruebas (TDD)
Primero escriba la prueba y luego escriba el código para aprobarla.
| Paso | Descripción |
|------|-------------|
| **1. Rojo** | Escriba una prueba fallida que describa el comportamiento deseado |
| **2. Verde** | Escribe el código mínimo para pasar la prueba |
| **3. Refactorizar** | Limpiar el código manteniendo las pruebas en verde |
| Beneficio | Descripción |
|---------|-------------|
| **Comentarios de diseño** | Las pruebas te obligan a pensar en las interfaces antes de la implementación |
| **Seguridad de regresión** | Cada error se prueba; el error nunca podrá regresar |
| **Documentación** | Las pruebas sirven como documentación viva del comportamiento esperado |
| **Confianza** | La alta cobertura de pruebas permite una refactorización valiente |
---

## Desarrollo impulsado por el comportamiento (BDD)
BDD extiende TDD escribiendo pruebas en lenguaje natural que describen el comportamiento desde la perspectiva del usuario.
### Formato dado-cuándo-entonces
```
Given a user with an empty shopping cart
When they add a "Python Book" priced at $29.99
Then the cart total should be $29.99
And the cart should contain 1 item
```

| Herramienta | Idioma |
|------|----------|
| **Pepino** | Java, JavaScript, Ruby y otros |
| **Compórtate** | Pitón |
| **Flujo de especificaciones** | C# |
| **Broma** (con describir/it) | JavaScript |
---

## Otros tipos de pruebas
| Tipo | Qué prueba | Herramientas |
|------|--------------|-------|
| **Rendimiento/Carga** | Comportamiento del sistema bajo carga | k6, JMeter, langosta, Gatling |
| **Seguridad** | Vulnerabilidades y vectores de ataque | OWASP ZAP, Suite Burp, Snyk |
| **Accesibilidad** | Cumplimiento de las WCAG | hacha, faro, pa11y |
| **Contrato** | Compatibilidad API entre servicios | Pacto, contrato Spring Cloud |
| **Mutación** | Calidad del propio conjunto de pruebas | Stryker, mumut, PIT |
| **Regresión visual** | La interfaz de usuario cambia entre versiones | Percy, Cromático, BackstopJS |
| **Caos** | Resiliencia del sistema ante fallos | Mono del Caos, Tornasol, Gremlin |
| **Humo** | Funcionalidad básica después de la implementación | Guiones personalizados; controles de salud |
| **Remojar** | Comportamiento del sistema durante un tiempo prolongado | Pruebas de carga de larga duración |
---

## Organización de pruebas
| Patrón | Descripción | Cuándo utilizar |
|---------|-------------|-------------|
| **Co-ubicado** | Pruebas junto al código que prueban (`src/utils.test.ts`) | La mayoría de los proyectos; fácil de encontrar |
| **Directorio separado** | Pruebas en una carpeta`tests/`o`__tests__/`| Grandes proyectos; separación clara |
| **Accesorios de prueba** | Datos de prueba compartidos en un directorio`fixtures/`| Cuando varias pruebas necesitan los mismos datos |
| **Utilidades de prueba** | Ayudantes compartidos en un directorio`test-utils/`| Cuando la lógica de configuración es compleja |
---

## Cobertura de código
| Métrica | Qué mide | Limitación |
|--------|-----------------|------------|
| **Cobertura de línea** | Porcentaje de líneas de código ejecutadas por pruebas | No mide la calidad de las afirmaciones |
| **Cobertura de sucursales** | Porcentaje de sucursales (si/si no) tomadas | Mejor que la cobertura de línea; todavía no detecta todos los errores |
| **Cobertura de camino** | Porcentaje de vías de ejecución tomadas | Más completo; exponencial en código complejo |
| **Puntuación de mutación** | Porcentaje de mutaciones detectadas por las pruebas | La mejor medida de la calidad de las pruebas |
**Objetivo**: una cobertura de línea del 80 % es un valor predeterminado razonable. Pero la cobertura es una guía, no un objetivo: una cobertura del 100% con afirmaciones débiles es peor que una cobertura del 70% con pruebas exhaustivas.
---

## Integración y pruebas continuas
| Práctica | Descripción |
|----------|-------------|
| **Ejecute todas las pruebas unitarias en cada confirmación** | Comentarios rápidos; detecta regresiones inmediatamente |
| **Ejecutar pruebas de integración en PR** | Detecta problemas que las pruebas unitarias pasan por alto |
| **Ejecute pruebas E2E todas las noches o al fusionarse con principal** | Lento pero minucioso |
| **Falla rápido** | Detener el oleoducto ante el primer fallo para ahorrar tiempo |
| **Política de prueba inestable** | Poner en cuarentena o eliminar las pruebas inestables inmediatamente; nunca ignores |
| **Prueba de paralelización** | Ejecute pruebas en paralelo para reducir el tiempo de CI |
---

## Consejos prácticos
- **Nombra las pruebas claramente.**`test_calculates_tax_for_high_earner`te dice qué se rompió. `test_1`no te dice nada.
- **Una afirmación por prueba (cuando sea práctico).** Facilita el diagnóstico de fallas.
- **No probar los detalles de implementación.** Comportamiento de la prueba. Si refactoriza los componentes internos, las pruebas no deberían fallar.
- **Evita probar código de terceros.** Simulacros de bibliotecas externas; Pruebe la interacción de su código con ellos.
- **Haga pruebas rápidamente.** Si su conjunto de pruebas tarda 10 minutos, los desarrolladores dejarán de ejecutarlo. Optimice sin descanso.
- **Eliminar pruebas inactivas.** Las pruebas que siempre pasan o prueban el código eliminado son ruido.
- **Trate el código de prueba como código de producción.** Debe ser legible, mantenible y bien estructurado.
---

## Resumen
Las pruebas no son opcionales: es la forma de crear software que no se rompa. La pirámide de pruebas lo guía hacia muchas pruebas unitarias rápidas, algunas pruebas de integración y algunas pruebas E2E. TDD y BDD proporcionan enfoques estructurados. La burla aísla las unidades para realizar pruebas. La cobertura del código mide amplitud pero no profundidad. El principio más importante es este: si no se prueba, está roto; simplemente no lo sabes todavía.