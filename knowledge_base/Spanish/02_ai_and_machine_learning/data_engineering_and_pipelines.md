---
# Metadatos
título: "Ingeniería de Datos y Pipelines"
descripción: "ETL/ELT, lagos de datos, orquestación, Kafka, almacenes de características"
categoría: "IA y aprendizaje automático"
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
review_by: "Equipo de base de conocimientos de inteligencia artificial y aprendizaje automático"
next_review: "2027-08-05"
# Clasificación
Etiquetas: [datos, ingeniería, oleoductos, inteligencia artificial y aprendizaje automático]
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
# Ingeniería de datos y oleoductos
La ingeniería de datos es la disciplina de construir sistemas que mueven, transforman y almacenan datos a escala. Sin canales de datos confiables, los modelos de aprendizaje automático no se pueden entrenar, los paneles muestran números obsoletos y las decisiones comerciales se basan en conjeturas. Este archivo cubre la arquitectura, las herramientas y las prácticas para construir una infraestructura de datos que funcione.
---

## ETL frente a ELT
| Enfoque | Cómo funciona | Mejor para | Herramientas |
|----------|-------------|----------|-------|
| **ETL** (Extraer → Transformar → Cargar) | Transformar datos *antes* de cargarlos en el almacén | Almacenes tradicionales con computación limitada | Informática, Talend, Apache NiFi |
| **ELT** (Extraer → Cargar → Transformar) | Cargue los datos sin procesar primero; transformar *dentro* del almacén | Almacenes en la nube modernos con computación elástica | dbt, Fivetran, Airbyte + BigQuery/Copo de nieve |
El cambio de ETL a ELT ha sido impulsado por los almacenes de datos en la nube (BigQuery, Snowflake, Redshift) que pueden escalar la computación independientemente del almacenamiento. Ya no es necesario preprocesar todo antes de cargarlo.
---

## Lagos de datos frente a almacenes de datos
| Característica | Lago de datos | Almacén de datos |
|---------|-----------|---------------|
| **Formato de datos** | Formato nativo sin formato (esquema en lectura) | Estructurado, procesado (esquema en escritura) |
| **Esquema** | Definido en el momento de la consulta | Definido antes de cargar |
| **Tipos de datos** | Estructurados, semiestructurados, no estructurados | Principalmente estructurado |
| **Usuarios** | Científicos de datos, ingenieros | Analistas de negocio, herramientas de BI |
| **Costo** | Almacenamiento más económico (almacenamiento de objetos) | Más caro (optimizado para consultas) |
| **Ejemplos** | AWS S3, Lago de datos Azure, GCS | Copo de nieve, BigQuery, Desplazamiento al rojo |
El enfoque moderno es la **casa del lago**: combinar el almacenamiento flexible y económico de un lago con las características de gestión y rendimiento de un almacén. Delta Lake, Apache Iceberg y Apache Hudi son las tecnologías clave aquí.
---

## Arquitectura de tuberías
### Lote frente a transmisión
| Modo | Descripción | Latencia | Caso de uso |
|------|-------------|---------|----------|
| **Lote** | Procesar datos en grandes porciones a intervalos programados | Minutos a horas | Informes diarios, trabajos ETL, enriquecimiento de datos |
| **Transmisión** | Procesar datos continuamente a medida que llegan | Milisegundos a segundos | Paneles de control en tiempo real, detección de fraude, alertas |
| **Microlote** | Pequeños lotes a intervalos muy cortos | Segundos | Casi en tiempo real con simplicidad por lotes |
### Componentes de tubería
Una canalización de datos típica tiene estas etapas:
| Etapa | Descripción | Herramientas |
|-------|-------------|-------|
| **Ingestión** | Recopilar datos de fuentes | Kafka, Airbyte, Fivetran, Debezium |
| **Transformación** | Limpiar, enriquecer, agregar | dbt, Spark, Pandas |
| **Almacenamiento** | Persistir datos procesados ​​| BigQuery, Copo de nieve, T3, Lago Delta |
| **Servicio** | Poner los datos a disposición de los consumidores | API, paneles de control, tiendas de funciones de aprendizaje automático |
| **Orquestación** | Programar y gestionar dependencias | Flujo de aire, Prefecto, Dagster |
| **Monitoreo** | Seguimiento del estado de la tubería y la calidad de los datos | Grandes Esperanzas, Montecarlo, alertas personalizadas |
---

## Herramientas de orquestación
| Herramienta | Enfoque | Fuerza |
|------|----------|----------|
| **Flujo de aire Apache** | DAG basados ​​en Python; estándar de la industria | Ecosistema enorme, maduro, flexible |
| **Prefecto** | Nativo de Python; API más limpia que Airflow | Diseño moderno, excelente manejo de errores |
| **Dagster** | Centrado en activos; enfoque de ingeniería de software | Sistema de tipos, pruebas, observabilidad |
| **Luigi** | La herramienta de canalización original de Spotify | Simple, pero desarrollado menos activamente |
### Ejemplo de flujo de aire
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    # Pull data from source
    pass

def transform():
    # Clean and process
    pass

def load():
    # Write to warehouse
    pass

with DAG("etl_pipeline", start_date=datetime(2024, 1, 1),
         schedule="@daily", catchup=False) as dag:
    e = PythonOperator(task_id="extract", python_callable=extract)
    t = PythonOperator(task_id="transform", python_callable=transform)
    l = PythonOperator(task_id="load", python_callable=load)
    
    e >> t >> l  # Define dependencies
```

---

## Apache Kafka
Kafka es la columna vertebral de muchos sistemas de datos en tiempo real. Es un registro de eventos distribuido que proporciona mensajería de alto rendimiento y tolerante a fallas.
### Conceptos básicos
| Concepto | Descripción |
|---------|-------------|
| **Tema** | Una categoría de mensajes (por ejemplo, `orders`, `user-events`) |
| **Partición** | Los temas se dividen en particiones para lograr paralelismo |
| **Productor** | Aplicación que escribe mensajes a temas |
| **Consumidor** | Aplicación que lee mensajes de temas |
| **Grupo de consumidores** | Grupo de consumidores que comparten la carga de leer un tema |
| **Compensación** | Posición de un consumidor dentro de una partición |
| **Corredor** | Un nodo de servidor Kafka |
### Cuándo utilizar Kafka
- **Transmisión de eventos**: procesamiento de eventos en tiempo real a escala.
- **Servicios de desacoplamiento**: Los productores y consumidores no necesitan conocerse unos a otros.
- **Repetición**: los mensajes se conservan; los consumidores pueden volver a leer desde cualquier compensación.
- **Contrapresión**: Kafka maneja naturalmente las diferencias de velocidad entre productores y consumidores.
---

## Modelado de datos
### Esquema de estrella versus esquema de copo de nieve
| Esquema | Estructura | Ventajas | Contras |
|--------|-----------|------|------|
| **Estrella** | Mesa de hechos central rodeada de tablas de dimensiones desnormalizadas | Consultas sencillas, lecturas rápidas | Redundancia de datos |
| **Copo de nieve** | Las tablas de dimensiones están normalizadas (divididas en subtablas) | Menos redundancia | Más uniones, consultas más lentas |
### Tablas de hechos y dimensiones
| Tipo de mesa | Contiene | Ejemplo |
|-----------|----------|---------|
| **Hecho** | Eventos medibles (métricas) | `orders`(id_pedido, id_producto, id_cliente, importe, fecha) |
| **Dimensión** | Atributos descriptivos | `products`(id_producto, nombre, categoría, precio),`customers`(id_cliente, nombre, ciudad) |
---

## Tiendas de funciones
Un almacén de características es un depósito centralizado de características de ML: los valores derivados utilizados como entrada para los modelos (por ejemplo, "valor de pedido promedio del usuario en los últimos 30 días").
| Capacidad | Descripción |
|-----------|-------------|
| **Registro de funciones** | Catálogo de funcionalidades disponibles con metadatos |
| **Tienda sin conexión** | Características históricas para el entrenamiento de modelos (por lotes) |
| **Tienda en línea** | Función de baja latencia que sirve para inferencia en tiempo real |
| **Monitoreo de funciones** | Detectar deriva, valores perdidos, cambios de distribución |
| Herramienta | Descripción |
|------|-------------|
| **Fiesta** | Código abierto; funciona con cualquier marco de ML |
| **Tectón** | Comercial; plataforma de funciones en tiempo real |
| **Trabajos de lúpulo** | Código abierto; plataforma ML completa con tienda de funciones |
| **Tienda de funciones de Databricks** | Integrado con Databricks/Spark |
---

## Calidad de los datos
La calidad de los datos es el asesino silencioso de los proyectos de ML. Basura entra, basura sale.
### Dimensiones de calidad
| Dimensión | Pregunta |
|-----------|----------|
| **Precisión** | ¿Los datos reflejan la realidad? |
| **Integridad** | ¿Están completos los campos obligatorios? |
| **Consistencia** | ¿Los valores coinciden entre las fuentes? |
| **Puntualidad** | ¿Los datos están actualizados? |
| **Validez** | ¿Los valores se ajustan a reglas definidas? |
| **Singularidad** | ¿Hay registros duplicados? |
### Herramientas de calidad de datos
| Herramienta | Enfoque |
|------|----------|
| **Grandes expectativas** | Basado en Python; definir "expectativas" sobre los datos |
| **Montecarlo** | Plataforma de observabilidad de datos impulsada por ML |
| **pruebas dbt** | Pruebas integradas para datos de almacén (relaciones únicas, not_null) |
| **Refresco** | Escaneo de calidad de datos de código abierto |
---

## Gobernanza de datos
La gobernanza de datos garantiza que los datos se gestionen de forma responsable en toda la organización.
| Área | Descripción |
|------|-------------|
| **Catálogo de datos** | Inventario de búsqueda de conjuntos de datos con metadatos (Amundsen, DataHub, Atlan) |
| **Linaje de datos** | Seguimiento de dónde provienen los datos y cómo se transforman |
| **Control de acceso** | Permisos basados ​​en roles; quién sabe leer/escribir qué |
| **Cumplimiento** | Cumplimiento de GDPR, CCPA, HIPAA |
| **Propiedad de los datos** | Propiedad clara de cada conjunto de datos (custodia) |
| **Políticas de retención** | Definir cuánto tiempo se conservan los datos y cuándo se eliminan |
---

## La pila de datos moderna
La "pila de datos moderna" se refiere a la combinación típica de herramientas que utilizan los equipos de datos en la actualidad:
| Capa | Herramientas típicas |
|-------|--------------|
| **Ingestión** | Fivetran, Airbyte |
| **Almacén** | Copo de nieve, BigQuery, Desplazamiento al rojo |
| **Transformación** | dbt |
| **Orquestación** | Flujo de aire, Prefecto, Dagster |
| **BI / Visualización** | Looker, Metabase, Tableau |
| **ETL inverso** | Censo, Hightouch (sincronizar los datos del almacén con las herramientas) |
| **Calidad de los datos** | Grandes esperanzas, Montecarlo |
La tendencia es hacia las mejores herramientas modulares conectadas por estándares abiertos (SQL, modelos dbt, Airflow DAG) en lugar de plataformas monolíticas.