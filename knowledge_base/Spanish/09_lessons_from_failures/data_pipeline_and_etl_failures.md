---
# Metadatos
título: "Errores de canalización de datos y ETL"
descripción: "Derivación del esquema, datos duplicados, lagunas de validación, supervisión de canalización"
categoría: "Lecciones de los fracasos"
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
review_by: "Lecciones de las fallas del equipo de la base de conocimientos"
next_review: "2027-08-05"
# Clasificación
Etiquetas: [datos, canalización, etl, fracasos, lecciones de los fracasos]
nivel_dificultad: "avanzado"
requisitos previos: []
estimado_reading_time: "5 minutos"
# Guía de contribución
contribución:
  licencia: "MIT"
  feedback_channel: "Problemas de GitHub"
  how_to_contribute: "Enviar un PR con cambios y actualizar el registro de cambios"
  review_process: "Los mantenedores de categorías revisan los cambios antes de fusionarlos"
---
# Fallos de canalización de datos y ETL
Los canales de datos son la tubería de las organizaciones modernas: mueven datos desde los sistemas de origen a través de transformaciones a las bases de datos, almacenes y lagos donde se utilizan para análisis, aprendizaje automático y toma de decisiones. Cuando trabajan, nadie se da cuenta. Cuando fallan, las decisiones se toman sobre datos obsoletos, los modelos se entrenan con basura, los informes muestran números imposibles y la confianza en toda la plataforma de datos se erosiona. Las fallas en la canalización de datos se encuentran entre las fallas más comunes y costosas en las organizaciones tecnológicas.
---

## Modos de falla comunes
### Problemas de calidad de datos
| Fracaso | Descripción | Impacto | Dificultad de detección |
|---------|-------------|--------|---------------------|
| **Corrupción silenciosa de datos** | Los datos se modifican incorrectamente sin que se genere ningún error | Los sistemas posteriores confían en datos incorrectos; decisiones basadas en información falsa | Muy difícil: no hay señal de error |
| **Deriva del esquema** | El sistema fuente cambia el esquema (agrega, elimina, cambia el nombre de las columnas) | La canalización se rompe o deja caer datos silenciosamente | Medio: el proceso de tramitación puede fallar o producir resultados parciales |
| **El tipo de datos no coincide** | La fuente envía una cadena donde se esperaba un número entero; cambios de precisión del flotador | El oleoducto falla; datos truncados; errores de redondeo | Medio: puede provocar errores en la canalización o problemas sutiles con los datos |
| **Registros duplicados** | El mismo evento procesado varias veces | Recuentos inflados; agregaciones incorrectas | Difícil: cada registro parece válido individualmente |
| **Valores nulos/faltantes** | Los campos esperados están vacíos | Los cálculos fallan; modelos producen predicciones erróneas | Medio: depende del manejo nulo |
| **Valores fuera de rango** | Valores fuera de los límites esperados (edades negativas; fechas futuras) | Estadísticas sesgadas; lógica de negocios rota | Medio: requiere reglas de validación |
| **Datos que llegan tarde** | Los datos llegan después de que se haya cerrado la ventana de procesamiento | Resultados incompletos; registros perdidos | Difícil: los resultados parecen completos pero no lo son |
### Problemas de infraestructura de oleoductos
| Fracaso | Descripción | Impacto |
|---------|-------------|--------|
| **Falló la orquestación** | El programador (Airflow, Prefect) no activa la canalización | Los datos están obsoletos; no se produce ningún procesamiento |
| **Agotamiento de recursos** | Pipeline se queda sin memoria, CPU o disco | El oleoducto colapsa; resultados parciales |
| **Error de dependencia** | El sistema aguas arriba está inactivo o es lento | Tubería espera indefinidamente o falla |
| **Problemas de simultaneidad** | Múltiples canales modifican los mismos datos simultáneamente | Condiciones de carrera; corrupción de datos |
| **Deriva de configuración** | Los cambios de entorno (red, credenciales, puntos finales) no se reflejan en la canalización | Tubería falla inesperadamente |
| **Contrapresión** | Los datos llegan más rápido de lo que el canal puede procesar | Colas crecientes; latencia creciente |
---

## Estudios de caso
### Estudio de caso 1: Duplicación silenciosa de datos
| Aspecto | Descripción |
|--------|-------------|
| **Escenario** | El proceso de pedidos de una empresa de comercio electrónico procesa eventos de una cola de mensajes |
| **Qué salió mal** | Un reinicio del consumidor provocó que los mensajes se volvieran a consumir; no existía ninguna lógica de deduplicación |
| **Impacto** | Las cifras de ingresos se inflaron un 15% durante 3 semanas antes de que alguien se diera cuenta |
| **Causa raíz** | Sin claves de idempotencia; entrega al menos una vez sin deduplicación |
| **Reparar** | Se agregaron claves de idempotencia basadas en el ID del pedido; implementó la semántica exactamente una vez |
| **Lección** | La entrega al menos una vez requiere deduplicación; validar siempre los totales con respecto a los sistemas fuente |
### Estudio de caso 2: El cambio de esquema se interrumpe en sentido descendente
| Aspecto | Descripción |
|--------|-------------|
| **Escenario** | Un proveedor de pagos cambia el nombre de un campo en su respuesta API |
| **Qué salió mal** | La canalización ETL comenzó silenciosamente a escribir valores nulos; sin validación de esquema |
| **Impacto** | Los informes financieros mostraron cero ingresos por ese método de pago durante 2 meses |
| **Causa raíz** | Sin validación de esquema en el momento de la ingesta; valores nulos tratados como válidos |
| **Reparar** | Se agregó validación de esquema con alertas; campos obligatorios aplicados; cheques nulos |
| **Lección** | Nunca confíes en que los esquemas externos permanezcan estables; validar en el límite |
### Estudio de caso 3: Catástrofe en la zona horaria
| Aspecto | Descripción |
|--------|-------------|
| **Escenario** | Una empresa global agrega métricas diarias en todas las oficinas |
| **Qué salió mal** | Algunas fuentes utilizaron UTC, otras utilizaron la hora local; tubería no se normalizó |
| **Impacto** | Los totales diarios no coincidían; algunas transacciones se cuentan en el día equivocado; el cierre de fin de mes fue incorrecto |
| **Causa raíz** | Sin política de zona horaria estándar; marcas de tiempo almacenadas de manera inconsistente |
| **Reparar** | Todas las marcas de tiempo almacenadas como UTC; conversión a hora local sólo en la capa de presentación |
| **Lección** | Estandarizar el UTC en todas partes; sea ​​explícito sobre las zonas horarias en cada límite |
---

## Estrategias de Prevención
### Validación de datos
| Estrategia | Descripción | Ejemplos de herramientas |
|----------|-------------|---------------|
| **Validación de esquema** | Verificar que los datos coincidan con el esquema esperado en cada etapa | Grandes expectativas; Deequ; refresco |
| **Comprobaciones de alcance** | Los valores caen dentro de los límites esperados | Afirmaciones personalizadas; pruebas dbt |
| **Controles de frescura** | Los datos son lo suficientemente recientes como para ser útiles | Monitoreo de marcas de tiempo; Alertas de SLA |
| **Comprobaciones de volumen** | Los recuentos de filas están dentro del rango esperado | Detección de anomalías en el recuento de filas |
| **Integridad referencial** | Coincidencia de claves externas; sin registros huérfanos | restricciones SQL; herramientas de calidad de datos |
| **Conciliación entre fuentes** | Coincidencia de totales entre origen y destino | Trabajos de conciliación automatizados |
### Patrones de diseño de tuberías
| Patrón | Descripción | Beneficio |
|---------|-------------|---------|
| **Idempotencia** | Ejecutar la canalización varias veces produce el mismo resultado | Es seguro volver a intentarlo; sin duplicados |
| **Atomicidad** | La tubería tiene éxito o fracasa por completo (sin estado parcial) | Sin datos a medio procesar |
| **Puntos de control** | Guarde el progreso en cada etapa; reanudar desde el último punto de control | Tolerancia a fallos; sin reprocesamiento |
| **Colas de mensajes no entregados** | Los registros fallidos pasan a una cola separada para su investigación | Sin pérdida de datos; puede investigar y reproducir |
| **Disyuntores** | Detener el procesamiento cuando falla el flujo descendente | Evite fallos en cascada |
| **Contratos de datos** | Acuerdo entre productores y consumidores sobre formato de datos | Los cambios de esquema están coordinados |
### Monitoreo y alertas
| Qué monitorear | Por qué | Cómo |
|-----------------|-----|-----|
| **Duración del proceso de tramitación** | El aumento de la duración indica problemas | Análisis de tendencias; Seguimiento de SLA |
| **Recuento de filas** | Los cambios repentinos indican problemas | Comparar con promedios históricos |
| **Tarifas nulas** | Los nulos en aumento señalan problemas de esquema o fuente | Seguimiento nulo a nivel de columna |
| **Actualidad de los datos** | Los datos obsoletos significan que el proceso no se está ejecutando | Marca de tiempo del último registro |
| **Impacto aguas abajo** | ¿Los informes y modelos utilizan datos correctos? | Linaje de datos de extremo a extremo |
| **Uso de recursos** | UPC; memoria; disco; red | Monitoreo de infraestructura |
---

## Estrategias de recuperación
| Situación | Estrategia |
|-----------|----------|
| **Datos incorrectos ya en el almacén** | Identificar el rango de tiempo afectado; reprocesar desde la fuente; notificar a los consumidores intermedios |
| **Falla en el oleoducto a mitad de camino** | El diseño idempotente permite una repetición segura; puntos de control permite reanudar |
| **El cambio de esquema interrumpió el proceso** | Arreglar la transformación; reponer los datos afectados; agregar manejo de evolución de esquema |
| **Corrupción silenciosa descubierta tarde** | Análisis de causa raíz; determinar el radio de la explosión; reprocesar; agregar monitoreo para detectar recurrencia |
| **Pérdida de datos** | Restaurar desde copia de seguridad; reproducir desde la fuente; evaluar si la pérdida es recuperable |
---

## Resumen
Las fallas en la canalización de datos son omnipresentes y, a menudo, más costosas que las interrupciones de las aplicaciones porque producen respuestas incorrectas en lugar de errores obvios. La corrupción silenciosa de los datos, la desviación del esquema, los duplicados, los errores de zona horaria y los valores faltantes son los culpables más comunes. Las estrategias clave de prevención son: validar los datos en cada límite (esquema, rango, volumen, actualidad); diseñar tuberías para que sean idempotentes y atómicas; monitorear todo (duración, recuento de filas, tasas nulas, frescura); utilizar colas de mensajes fallidos para registros fallidos; y establecer contratos de datos entre productores y consumidores. Cuando ocurren fallas, la respuesta debe incluir un análisis de la causa raíz, el reprocesamiento de los datos afectados, la notificación a los consumidores intermedios y, fundamentalmente, agregar monitoreo para detectar la misma clase de falla en el futuro. Las organizaciones que hacen esto bien tratan los canales de datos con el mismo rigor que el software de producción: pruebas, monitoreo, alertas, respuesta a incidentes y autopsias.