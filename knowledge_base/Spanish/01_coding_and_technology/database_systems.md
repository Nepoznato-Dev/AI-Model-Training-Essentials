---
# Metadatos
título: "Sistemas de bases de datos"
descripción: "SQL, NoSQL, patrones de diseño, optimización"
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
Etiquetas: [base de datos, sistemas, codificación y tecnología]
nivel_dificultad: "intermedio"
requisitos previos: []
estimado_reading_time: "13 minutos"
# Guía de contribución
contribución:
  licencia: "MIT"
  feedback_channel: "Problemas de GitHub"
  how_to_contribute: "Enviar un PR con cambios y actualizar el registro de cambios"
  review_process: "Los mantenedores de categorías revisan los cambios antes de fusionarlos"
---
# Sistemas de bases de datos
## Fundamentos de bases de datos
### ¿Qué es una base de datos?
Una base de datos es una colección organizada de información estructurada almacenada electrónicamente, diseñada para la recuperación, inserción, actualización y eliminación eficiente de datos.
### Sistemas de gestión de bases de datos (DBMS)
Software que interactúa con los usuarios finales, las aplicaciones y la propia base de datos para capturar y analizar datos. Ejemplos: MySQL, PostgreSQL, Oracle, MongoDB.
### Conceptos clave
- **Esquema**: Estructura/organización de la base de datos (tablas, campos, relaciones)
- **Instancia**: datos reales almacenados en un momento particular
- **Propiedades del ÁCIDO**: Atomicidad, Consistencia, Aislamiento, Durabilidad
- **Teorema CAP**: Coherencia, Disponibilidad, Tolerancia de Partición (elija 2)
- **Normalización**: organización de datos para reducir la redundancia
- **Desnormalización**: agregar redundancia para mejorar el rendimiento de lectura
## Bases de datos relacionales (SQL)
### Conceptos básicos
- **Tablas**: Filas (registros) y columnas (campos)
- **Clave principal**: identificador único para cada fila
- **Clave externa**: referencia a la clave principal en otra tabla
- **Índices**: estructuras de datos que mejoran la velocidad de consulta
- **Vistas**: tablas virtuales basadas en resultados de consultas
- **Procedimientos almacenados**: bloques de código SQL precompilados
- **Disparadores**: acciones automáticas ante cambios de datos
### Operaciones SQL (CRUD)```sql
-- Create
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Read
SELECT * FROM users WHERE id = 1;
SELECT name, email FROM users ORDER BY name LIMIT 10;

-- Update
UPDATE users SET email = 'new@example.com' WHERE id = 1;

-- Delete
DELETE FROM users WHERE id = 1;
```

### Se une
- **UNIÓN INTERNA**: Devuelve filas coincidentes de ambas tablas
- **UNIÓN IZQUIERDA**: todas las filas de la tabla izquierda, coincidencias de la derecha
- **UNIÓN DERECHA**: Todas las filas de la tabla derecha, coincidencias de la izquierda
- **UNIÓN EXTERIOR COMPLETA**: Todas las filas de ambas tablas
- **UNIÓN CRUZADA**: Producto cartesiano de ambas tablas
- **SELF JOIN**: Tabla unida consigo misma
### Formularios de normalización
- **1NF**: Valores atómicos, sin grupos repetidos
- **2NF**: 1NF + sin dependencias parciales (todos los atributos que no son clave dependen de la clave primaria completa)
- **3NF**: 2NF + sin dependencias transitivas (los atributos no clave no dependen de otros atributos no clave)
- **BCNF**: 3NF más fuerte, cada determinante es una clave candidata
- **4NF**: Sin dependencias multivalor
- **5NF**: Sin dependencias de unión
### RDBMS populares
- **PostgreSQL**: funciones avanzadas, extensible, compatible con ACID
- **MySQL**: aplicaciones web ampliamente utilizadas y de lectura rápida.
- **Oracle**: características empresariales, escalabilidad, costosas
- **SQL Server**: ecosistema de Microsoft, herramientas integradas
- **SQLite**: integrado, sin servidor, ligero
- **MariaDB**: bifurcación MySQL, código abierto
## Bases de datos NoSQL
### Tipos de bases de datos NoSQL
#### Almacenes de documentos
- **Estructura**: documentos tipo JSON (BSON)
- **Casos de uso**: gestión de contenidos, catálogos, perfiles de usuario
- **Ejemplos**: MongoDB, CouchDB, DocumentDB
- **Ejemplo de consulta** (MongoDB):```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Tiendas de valor clave
- **Estructura**: pares clave-valor simples
- **Casos de uso**: almacenamiento en caché, sesiones, carritos de compras
- **Ejemplos**: Redis, DynamoDB, Riak
- **Características**: Consultas rápidas, sencillas y limitadas
#### Tiendas familiares de columnas
- **Estructura**: Columnas agrupadas en familias
- **Casos de uso**: Big data, análisis, series temporales
- **Ejemplos**: Cassandra, HBase, ScyllaDB
- **Características**: optimizado para escritura, distribuido, escalable
#### Bases de datos de gráficos
- **Estructura**: Nodos, aristas, propiedades
- **Casos de uso**: Redes sociales, detección de fraude, recomendaciones
- **Ejemplos**: Neo4j, Amazon Neptune, ArangoDB
- **Lenguaje de consulta**: Cypher (Neo4j), Gremlin
### Cuándo utilizar NoSQL
- Esquema flexible/evolutivo
- Requisitos de escala horizontal
- Alto rendimiento de escritura
- Datos jerárquicos/anidados
- Sistemas distribuidos
- Aplicaciones en tiempo real
## Diseño de base de datos
### Modelado entidad-relación
- **Entidades**: Objetos/conceptos (Cliente, Producto, Pedido)
- **Atributos**: Propiedades de las entidades (nombre, precio, fecha)
- **Relaciones**: Conexiones entre entidades (uno a uno, uno a muchos, muchos a muchos)
- **Cardinalidad**: Número de instancias en relación
### Patrones de diseño de esquemas
- **Herencia de tabla única**: todos los tipos en una tabla con discriminador de tipos
- **Herencia de tablas de clases**: tablas separadas para clases base y subclases
- **Herencia de la tabla de concreto**: tabla separada para cada clase de concreto
- **Tablas de unión**: resuelve relaciones de muchos a muchos
- **Tablas de auditoría**: seguimiento de cambios (creado_at, actualizado_at, eliminado_at)
### Estrategias de indexación
- **B-Tree**: Predeterminado, consultas de rango, clasificación
- **Hash**: búsquedas de coincidencias exactas
- **Mapa de bits**: columnas de baja cardinalidad (género, estado)
- **Texto completo**: capacidades de búsqueda de texto
- **Espacial**: Datos geográficos (GIS)
- **Compuesto**: varias columnas combinadas
- **Cobertura**: incluye todas las columnas necesarias para la consulta
## Optimización de consultas
### Planes de ejecución
- Comprender cómo la base de datos ejecuta consultas.
- Identificación de cuellos de botella (escaneos completos de tablas, índices faltantes)
- Herramientas: EXPLICAR, EXPLICAR ANALIZAR
### Técnicas de optimización
- **Uso de índice**: asegúrese de que las consultas utilicen índices adecuados
- **Reescritura de consultas**: simplifique consultas complejas
- **Optimización de unión**: elija los tipos de unión y el orden correctos
- **Particionamiento**: dividir tablas grandes (rango, hash, lista)
- **Vistas materializadas**: resultados de consultas precalculados
- **Almacenamiento en caché de consultas**: almacena resultados de consultas frecuentes
### Problemas comunes de rendimiento
- **Problema de consulta N+1**: Obtener datos relacionados de manera ineficiente
- **Índices faltantes**: escaneos completos de tablas en tablas grandes
- **Sobreindexación**: escrituras lentas debido a demasiados índices
- **Contención de bloqueo**: transacciones en espera de bloqueos
- **Consultas ineficientes**: SELECT *, uniones innecesarias
## Transacciones y Simultaneidad
### Niveles de aislamiento de transacciones
- **LECTURA NO COMPROMETIDA**: aislamiento mínimo, lecturas sucias posibles
- **LEER COMPROMETIDO**: Solo son visibles los datos confirmados (predeterminado en la mayoría de las bases de datos)
- **LECTURA REPETIBLE**: La misma consulta devuelve los mismos resultados dentro de la transacción
- **SERIALIZABLE**: Máximo aislamiento, las transacciones se ejecutan secuencialmente
### Control de concurrencia
- **Bloqueo pesimista**: bloquea los recursos antes del acceso
- **Bloqueo optimista**: comprobar la versión antes de confirmar
- **MVCC (Control de simultaneidad de versiones múltiples)**: mantiene múltiples versiones de filas
- **Bloqueo a nivel de fila**: bloquea filas específicas
- **Bloqueo a nivel de tabla**: bloquea toda la tabla
### Puntos muertos
- Dependencia circular donde las transacciones se esperan unas a otras.
- Prevención: orden de bloqueo consistente, tiempos de espera, detección de interbloqueos
- Resolución: cancelar una transacción
## Replicación y escalamiento
### Tipos de replicación
- **Maestro-Esclavo**: una principal, múltiples réplicas de lectura
- **Master-Master**: múltiples primarios, replicación bidireccional
- **Multi-Master**: N primarios, se necesita resolución de conflictos
- **Replicación en cadena**: Replicación secuencial a través de nodos
### Enfoques de escala
- **Escalado vertical**: aumenta los recursos del servidor (CPU, RAM, almacenamiento)
- **Escalado horizontal**: agregue más servidores (fragmentación, particionamiento)
- **Réplicas de lectura**: descargar tráfico de lectura
- **Sharding**: divide los datos entre servidores por clave/rango/hash
- **Federación**: Dividido por función/servicio
### Modelos de consistencia
- **Fuerte consistencia**: todos los nodos ven los mismos datos al mismo tiempo
- **Consistencia final**: los nodos convergen con el tiempo
- **Consistencia causal**: Se preservan las relaciones causa-efecto
- **Read-Your-Writes**: el usuario ve sus propias actualizaciones inmediatamente
## Copia de seguridad y recuperación
### Estrategias de respaldo
- **Copia de seguridad completa**: copia completa de la base de datos
- **Copia de seguridad incremental**: cambios desde la última copia de seguridad
- **Copia de seguridad diferencial**: cambios desde la última copia de seguridad completa
- **Recuperación de un punto en el tiempo**: restaurar a un momento específico
- **Copia de seguridad continua**: replicación en tiempo real para realizar copias de seguridad
### Procedimientos de recuperación
- **RTO (objetivo de tiempo de recuperación)**: tiempo de inactividad máximo aceptable
- **RPO (Objetivo de punto de recuperación)**: Pérdida de datos máxima aceptable
- **Plan de Recuperación ante Desastres**: Procedimientos documentados para fallas
- **Pruebas**: ejercicios de recuperación periódicos
## Seguridad
### Control de acceso
- **Autenticación**: verificar la identidad del usuario
- **Autorización**: Otorgar permisos (CONCEDER, REVOCAR)
- **Roles**: permisos de grupo para una gestión más sencilla
- **Principio de Mínimo Privilegio**: Acceso mínimo necesario
### Protección de datos
- **Cifrado en reposo**: cifra los datos almacenados
- **Cifrado en tránsito**: TLS/SSL para conexiones
- **Enmascaramiento**: oculta datos confidenciales en situaciones que no son de producción
- **Tokenización**: reemplazar datos confidenciales con tokens
### Vulnerabilidades comunes
- **Inyección SQL**: SQL malicioso en la entrada del usuario
- **Escalada de privilegios**: obtener acceso no autorizado
- **Registro de auditoría**: seguimiento de todas las actividades de la base de datos
- **Cumplimiento**: requisitos de GDPR, HIPAA y PCI-DSS
## Tecnologías modernas de bases de datos
### Bases de datos en la nube
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: base de datos SQL, Cosmos DB, Synapse
- **Beneficios**: Servicio administrado, escalado automático, copias de seguridad incluidas
### Nuevas bases de datos SQL
- Combine la coherencia de SQL con la escalabilidad de NoSQL
- **Ejemplos**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Características**: Distribuidas, transacciones ACID, escalamiento horizontal
### Bases de datos de series temporales
- Optimizado para datos con marca de tiempo
- **Ejemplos**: InfluxDB, TimescaleDB, Prometheus
- **Casos de uso**: IoT, monitoreo, datos financieros
### Bases de datos vectoriales
- Almacenar y consultar vectores de incrustación.
- **Ejemplos**: Piña, Milvus, Weaviate, Qdrant
- **Casos de uso**: búsqueda semántica, sistemas de recomendación, aplicaciones de IA
### Bases de datos multimodelo
- Admite múltiples modelos de datos en un solo sistema
- **Ejemplos**: ArangoDB, OrientDB, Azure Cosmos DB
- **Beneficio**: Flexibilidad sin múltiples bases de datos
## ORM y acceso a datos
### Mapeo relacional de objetos
- **Propósito**: Asignar tablas de bases de datos a objetos de programación
- **ORM populares**:
  -Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernar, JPA
  - Rubí: ActiveRecord
  - .NET: Marco de entidad
### Beneficios
- Abstracción de SQL
- Tipo de seguridad
- Gestión de la migración
- API de creación de consultas
### Desventajas
- Gastos generales de rendimiento
- Consultas complejas más difíciles de escribir.
- N+1 problemas de consulta
- Curva de aprendizaje
## Administración de base de datos
### Responsabilidades del DBA
- Instalación y configuración
- Ajuste del rendimiento
- Copia de seguridad y recuperación
- Gestión de seguridad
- Planificación de capacidad
- Monitoreo y alerta
- Gestión de parches
### Métricas de seguimiento
- Tiempo de respuesta a consultas
- Rendimiento (transacciones por segundo)
- Recuento de conexiones
- Proporción de aciertos de caché
- E/S de disco
- Bloquear el tiempo de espera
- Retraso de replicación
### Tareas de mantenimiento
- **Vacuum/Analyze**: actualiza estadísticas, recupera espacio
- **Reconstrucción de índices**: desfragmentar índices
- **Actualizaciones de estadísticas**: mantenga informado al optimizador de consultas
- **Rotación de registros**: administra el tamaño de los archivos de registro
- **Planificación de capacidad**: predecir el crecimiento, planificar actualizaciones