---
# Metadata
title: "Prometheus and Grafana"
description: "PromQL, exporters, dashboards, alerting, monitoring stack"
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
tags: [prometheus, grafana, quick-reference]
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
# Prometeo y Grafana
Prometheus es un conjunto de herramientas de monitoreo y alertas de código abierto diseñado para brindar confiabilidad y escalabilidad. Grafana es la plataforma líder de código abierto para visualizar datos de series temporales. Juntos, forman la pila de monitoreo más popular para infraestructuras y aplicaciones modernas. Prometheus recopila y almacena métricas; Grafana los muestra en paneles.
---

## Arquitectura Prometeo
| Componente | Descripción |
|-----------|-------------|
| **Servidor Prometeo** | Elimina métricas de los objetivos; almacena datos de series de tiempo; evalúa reglas de alerta |
| **Exportador** | Expone métricas de un sistema (Node Exporter, cAdvisor, etc.) |
| **Puerta de empuje** | Recibe métricas de trabajos de corta duración (trabajos por lotes, CI) |
| **Administrador de alertas** | Maneja alertas: agrupación, silenciamiento, enrutamiento, inhibición |
| **Descubrimiento de servicios** | Descubre objetivos automáticamente (Kubernetes, Consul, EC2, etc.) |
---

## Conceptos clave
| Concepto | Descripción |
|---------|-------------|
| **Métrico** | Una medida con nombre con etiquetas opcionales y un valor |
| **Serie temporal** | Un flujo de puntos de datos para una combinación específica de métrica + etiqueta |
| **Trabajo** | Una colección de objetivos con el mismo propósito |
| **Instancia** | Un único objetivo para eliminar (normalmente un proceso) |
| **Raspar** | Prometheus extrae métricas de un objetivo a intervalos regulares |
| **Etiqueta** | Un par clave-valor que dimensiona una métrica (por ejemplo,`method="GET"`) |
| **Muestra** | Un valor en un momento dado: (marca de tiempo, valor) |
---

## Tipos de métricas
| Tipo | Descripción | Caso de uso |
|------|-------------|----------|
| **Contador** | Valor creciente monótonamente (solo sube) | Recuento de solicitudes; errores; tareas completadas |
| **Medidor** | Valor que puede subir o bajar | Temperatura; uso de memoria; longitud de la cola |
| **Histograma** | Observaciones agrupadas por valor | Solicitar latencia; tamaño de respuesta |
| **Resumen** | Similar al histograma; calcula cuantiles del lado del cliente | Percentiles de latencia |
---

## PromQL (lenguaje de consulta)
### Consultas básicas
| Consulta | Descripción |
|-------|-------------|
| `http_requests_total`| Serie temporal sin procesar |
| `http_requests_total{method="GET"}`| Filtrar por etiqueta |
| `http_requests_total{method="GET", status="200"}`| Múltiples filtros de etiquetas |
| `rate(http_requests_total[5m])`| Tarifa por segundo durante 5 minutos |
| `increase(http_requests_total[1h])`| Incremento total en 1 hora |
| `sum(rate(http_requests_total[5m])) by (status)`| Tasa agregada por estatus |
| `histogram_quantile(0.95, rate(http_duration_bucket[5m]))`| Latencia percentil 95 |
| `avg(node_cpu_seconds_total{mode="idle"})`| Promedio de inactividad de CPU |
| `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))`| Utilización de CPU |
### Funciones comunes
| Función | Descripción | Ejemplo |
|----------|-------------|---------|
| `rate()`| Tasa media de aumento por segundo | `rate(requests_total[5m])`|
| `irate()`| Tasa por segundo basada en los dos últimos puntos de datos | `irate(requests_total[1m])`|
| `increase()`| Incremento total en el intervalo de tiempo | `increase(errors_total[1h])`|
| `sum()`| Suma entre series | `sum(rate(requests_total[5m])) by (service)`|
| `avg()`| Promedio entre series | `avg(node_memory_usage)`|
| `histogram_quantile()`| Calcular cuantiles a partir del histograma | `histogram_quantile(0.99, rate(duration_bucket[5m]))`|
| `topk()`| Principales series K por valor | `topk(5, rate(requests_total[5m]))`|
| `predict_linear()`| Predicción lineal | `predict_linear(disk_usage[1h], 4*3600)`|
| `absent()`| Compruebe si falta la métrica | `absent(up{job="myapp"})`|
---

## Exportadores comunes
| Exportador | Qué monitorea |
|----------|-----------------|
| **Exportador de nodos** | Métricas de host Linux/Unix (CPU, memoria, disco, red) |
| **cAsesor** | Métricas de contenedor (CPU, memoria, red, sistema de archivos) |
| **Exportador de MySQL** | Métricas de la base de datos MySQL |
| **Exportador PostgreSQL** | Métricas de la base de datos PostgreSQL |
| **Exportador de Redis** | Métricas de Redis |
| **Exportador de Blackbox** | Sondear puntos finales a través de HTTP, HTTPS, DNS, TCP, ICMP |
| **Exportador SNMP** | Métricas de dispositivos de red a través de SNMP |
| **Exportador JSON** | Métricas personalizadas de las API JSON |
---

## Grafana
### Conceptos clave
| Concepto | Descripción |
|---------|-------------|
| **Fuente de datos** | Conexión a Prometheus (u otros backends) |
| **Panel** | Colección de paneles dispuestos en un diseño |
| **Panel** | Visualización única (gráfico, indicador, tabla, mapa de calor) |
| **Variables** | Filtro dinámico para paneles (por ejemplo, seleccionar instancia) |
| **Anotación** | Marcar eventos en gráficos (implementaciones, incidentes) |
| **Regla de alerta** | Alertas basadas en umbrales dentro de Grafana |
| **Plantillas** | Patrones de tablero reutilizables con variables |
### Patrones de tablero útiles
| Patrón | Descripción |
|---------|-------------|
| **Fila de descripción general** | Métricas clave de un vistazo: tasa de error, latencia, rendimiento |
| **Profundización** | Haga clic desde el resumen hasta la vista detallada usando variables |
| **Método ROJO** | Tasa, errores y duración: las tres métricas clave del servicio |
| **Método USAR** | Utilización, saturación y errores: para infraestructuras |
| **Señales doradas** | Latencia, tráfico, errores, saturación (libro SRE de Google) |
---

## Alerta
### Estructura de reglas de alerta
```yaml
groups:
  - name: example
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate on {{ $labels.instance }}"
          description: "Error rate is {{ $value | humanizePercentage }}"
```

### Enrutamiento del administrador de alertas
| Concepto | Descripción |
|---------|-------------|
| **Grupo** | Combine alertas similares en una sola notificación |
| **Ruta** | Árbol de comparadores que determina dónde van las alertas |
| **Receptor** | Dónde enviar alertas (correo electrónico, Slack, PagerDuty, webhook) |
| **Inhibir** | Suprimir alertas cuando se activa otra alerta |
| **Silencio** | Silenciar temporalmente las alertas del comparador de etiquetas |
---

## Solución de problemas
| Problema | Solución |
|---------|----------|
| **Objetivo hacia abajo** | Compruebe si el exportador está en ejecución; comprobar la red/firewall; verificar la configuración de raspado |
| **Sin datos** | Verifique la ortografía del nombre de la métrica; comprobar los filtros de las etiquetas; verificar rango de tiempo |
| **Alta cardinalidad** | Demasiadas combinaciones de etiquetas; reducir los valores de las etiquetas; utilizar reglas de grabación |
| **Consultas lentas** | Utilice reglas de grabación para consultas complejas; aumentar el intervalo de raspado |
| **Fatiga de alerta** | Sintonizar umbrales; agregue la duración `for`; alertas relacionadas con el grupo |
| **Faltan métricas después del reinicio** | Prometheus almacena datos localmente; comprobar la configuración de retención |
---

## Resumen
Prometheus monitorea los sistemas extrayendo métricas de los exportadores a intervalos regulares. Las métricas son de cuatro tipos: contadores (solo aumentan), indicadores (arriba y abajo), histogramas (observaciones agrupadas) y resúmenes (cuantiles). PromQL es el lenguaje de consulta: `rate()`, `increase()`,`histogram_quantile()`y las funciones de agregación (`sum`, `avg`) son las operaciones más comunes. Grafana visualiza los datos de Prometheus en paneles con paneles, variables y anotaciones. Las alertas utilizan Alertmanager para agrupar, enrutar, silenciar e inhibir alertas. Los patrones de seguimiento clave son las señales doradas de Google (latencia, tráfico, errores, saturación) y el método RED (tasa, errores, duración) para servicios y el método USE (utilización, saturación, errores) para infraestructura.