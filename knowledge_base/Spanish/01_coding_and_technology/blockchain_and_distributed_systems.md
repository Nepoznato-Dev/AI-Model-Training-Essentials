---
# Metadatos
título: "Blockchain y Sistemas Distribuidos"
descripción: "Consenso, contratos inteligentes, DeFi, tolerancia a fallas bizantinas"
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
Etiquetas: [cadena de bloques, distribuida, sistemas, codificación y tecnología]
nivel_dificultad: "intermedio"
requisitos previos: []
estimado_reading_time: "7 minutos"
# Guía de contribución
contribución:
  licencia: "MIT"
  feedback_channel: "Problemas de GitHub"
  how_to_contribute: "Enviar un PR con cambios y actualizar el registro de cambios"
  review_process: "Los mantenedores de categorías revisan los cambios antes de fusionarlos"
---
# Blockchain y Sistemas Distribuidos
Blockchain es un tipo específico de sistema distribuido: un libro de contabilidad descentralizado que solo se adjunta donde los registros (bloques) están vinculados mediante hashes criptográficos. Los sistemas distribuidos son el campo más amplio de hacer que varias computadoras funcionen juntas como una sola. Ambos conceptos son importantes para comprender la infraestructura moderna, desde las criptomonedas hasta las bases de datos distribuidas y los algoritmos de consenso que impulsan los servicios globales.
---

## Fundamentos de los sistemas distribuidos
### ¿Por qué sistemas distribuidos?
| Motivación | Descripción |
|-----------|-------------|
| **Escalabilidad** | Agregue más máquinas para manejar más carga |
| **Tolerancia a fallos** | El sistema continúa funcionando incluso si algunas máquinas fallan |
| **Distribución geográfica** | Atender a usuarios desde centros de datos cercanos |
| **Especialización** | Diferentes máquinas realizan diferentes tareas |
### Conceptos clave
| Concepto | Descripción | Desafío |
|---------|-------------|-----------|
| **Consenso** | Conseguir que todos los nodos se pongan de acuerdo sobre un valor | Particiones de red; Fallas bizantinas |
| **Replicación** | Copiar datos en varios nodos | Coherencia vs disponibilidad |
| **Partición (fragmentación)** | Dividir datos entre nodos | Puntos calientes; consultas entre fragmentos |
| **Modelos de coherencia** | Garantías sobre lo que ven los diferentes lectores | La consistencia fuerte es lenta; eventual coherencia puede sorprender a los usuarios |
| **Teorema CAP** | Sólo puede tener 2 de: Coherencia, Disponibilidad, Tolerancia de partición | En la práctica, se requiere tolerancia de partición; elija C o A |
### El teorema de la PAC
| Elección | Lo que obtienes | A qué renuncias | Ejemplo |
|--------|-------------|-----------------|---------|
| **PC** | Consistente + tolerante a particiones | Es posible que algunos nodos no estén disponibles durante las particiones | HBase, MongoDB, Redis |
| **AP** | Disponible + tolerante a particiones | Las lecturas pueden devolver datos obsoletos | Casandra, DynamoDB, CouchDB |
| **CA** | Consistente + disponible | No puedo tolerar particiones de red | Bases de datos de un solo nodo (no realmente distribuidas) |
---

## Algoritmos de consenso
¿Cómo se ponen de acuerdo los nodos distribuidos sobre el estado del sistema?
| Algoritmo | Tipo | Tolerancia a fallos | Usado en |
|-----------|--------------|----------------|-----------------|
| **Paxos** | Tolerante a fallos de colisión | Hasta f fallos con 2f+1 nodos | Google gordito; teoría fundacional |
| **Balsa** | Tolerante a fallos de colisión | Hasta f fallos con 2f+1 nodos | etcd, Cónsul, TiKV |
| **PBFT** | Tolerante a fallas bizantinas | Hasta f fallos con 3f+1 nodos | Tela Hyperledger |
| **Prueba de trabajo** | Tolerante a fallas bizantinas | Depende del poder hash | Bitcoin |
| **Prueba de participación** | Tolerante a fallas bizantinas | Depende de lo que esté en juego | Etereum 2.0, Cardano |
### Balsa (simplificada)
| Rol | Responsabilidad |
|------|---------------|
| **Líder** | Maneja todas las solicitudes de los clientes; envía entradas de registro a seguidores |
| **Seguidor** | Responde a las solicitudes del líder; votos en las elecciones |
| **Candidato** | Pide votos para convertirse en líder |
1. Todos los nodos comienzan como seguidores.
2. Si un seguidor no recibe noticias del líder durante un tiempo muerto electoral, se convierte en candidato.
3. Los candidatos solicitan votos; el que tiene más votos se convierte en líder
4. El líder replica las entradas del registro a los seguidores.
5. Cuando la mayoría lo confirma, se compromete la entrada.
---

## cadena de bloques
### Cómo funciona una cadena de bloques
| Componente | Descripción |
|-----------|-------------|
| **Bloquear** | Un lote de transacciones + metadatos + hash del bloque anterior |
| **picadillo** | Huella criptográfica del contenido del bloque |
| **Cadena** | Cada bloque hace referencia al hash del bloque anterior, creando una cadena inmutable |
| **Consenso** | Los participantes de la red acuerdan qué bloques agregar |
| **Árbol Merkle** | Árbol de hashes que resume todas las transacciones en un bloque |
### Por qué es difícil manipular Blockchain
1. Cada bloque contiene el hash del bloque anterior.
2. Cambiar cualquier transacción cambia el hash del bloque.
3. El hash modificado rompe la cadena: todos los bloques posteriores dejan de ser válidos
4. Un atacante necesitaría volver a extraer todos los bloques posteriores Y controlar >50% de la red.
### Tipos de cadenas de bloques
| Tipo | Acceso | Validador | Ejemplo |
|------|--------|-----------|---------|
| **Público (sin permiso)** | Cualquiera puede leer y escribir | Consenso abierto (PoW, PoS) | Bitcoin, Etereum |
| **Privado (permitido)** | Acceso restringido | Validadores conocidos | Hiperledger, Corda |
| **Consorcio** | Gobernado por un grupo de organizaciones | Validadores seleccionados | R3 Corda para la banca |
### Contratos inteligentes
Código autoejecutable almacenado en la cadena de bloques que se ejecuta cuando se cumplen condiciones predeterminadas.
| Plataforma | Idioma | Característica notable |
|----------|----------|-----------------|
| **Etereum** | Solidez, Vyper | El ecosistema de contratos inteligentes más grande |
| **Solana** | Óxido, C | Alto rendimiento; tarifas bajas |
| **Cardano** | Haskell (Pluto) | Revisado por pares; verificación formal |
| **Hiperlibro** | Ir, Java, JavaScript | Empresa; autorizado |
---

## Criptomoneda
| Moneda | Consenso | Suministro | Uso primario |
|----------|-----------|--------|-------------|
| **Bitcoin** | Prueba de trabajo | 21 millones (tope) | Reserva de valor; oro digital |
| **Etereum** | Prueba de participación | Sin límite rígido | Contratos inteligentes; DeFi; NFT |
| **Solana** | Prueba de participación + Prueba de historial | Sin límite rígido | Transacciones de alta velocidad |
| **Cardano** | Prueba de participación (Ouroboros) | 45 mil millones (limitado) | Enfoque académico; sostenibilidad |
---

## Bases de datos distribuidas
| Base de datos | Arquitectura | Consistencia | Mejor para |
|----------|-------------|-------------|----------|
| **Casandra** | Columna ancha; punto a punto | Sintonizable (eventualmente hasta el quórum) | Alto rendimiento de escritura; series de tiempo |
| **MongoDB** | Documento; conjuntos de réplicas | Eventual (con opción de coherencia causal) | Esquema flexible; rápido desarrollo |
| **CucarachaDB** | SQL distribuido; Consenso de balsa | Fuerte | SQL distribuido; despliegue global |
| **TiDB** | SQL distribuido; Balsa (a través de TiKV) | Fuerte | Compatible con MySQL; escalado horizontal |
| **DynamoDB** | Valor-clave; gestionado | Eventual (o fuerte con lecturas consistentes) | Sin servidor; Integrado con AWS |
| **Llave inglesa** | SQL distribuido; Paxos | Fuerte | Nube de Google; coherencia global |
---

## Patrones de sistemas distribuidos
| Patrón | Descripción | Caso de uso |
|---------|-------------|----------|
| **Elección de líder** | Elija un nodo para coordinar | Líder de balsa; Guardián del zoológico |
| **Replicación** | Copiar datos para redundancia y escalar de lectura | Réplicas de bases de datos; CDN |
| **Fragmentación** | Partición de datos por rango de claves o hash | Bases de datos a gran escala |
| **MapaReducir** | Dividir el cálculo entre nodos; resultados agregados | Procesamiento de grandes datos |
| **Protocolo de chismes** | Los nodos comparten periódicamente el estado con pares aleatorios | Membresía del grupo; detección de fallos |
| **Compromiso en dos fases** | Coordinar transacciones en múltiples nodos | Bases de datos distribuidas |
| **Patrón de saga** | Serie de transacciones locales con acciones compensatorias | Transacciones de microservicios |
| **Disyuntor** | Deje de llamar a un servicio defectuoso; fallar rápido | Resiliencia; evitar fallos en cascada |
---

## Desafíos en los sistemas distribuidos
| Desafío | Descripción | Mitigación |
|-----------|-------------|------------|
| **Particiones de red** | Los nodos no pueden comunicarse | Compensación de la PAC; reintentar con retroceso |
| **Desviación del reloj** | Diferentes nodos tienen diferentes relojes | Utilice relojes lógicos; NTP; evite depender del tiempo del reloj de pared |
| **Fallas bizantinas** | Nodos que mienten o se comportan arbitrariamente | Consenso BFT; cadena de bloques |
| **Cerebro dividido** | Dos nodos creen que son el líder | Esgrima; decisiones basadas en quórum |
| **Fallos en cascada** | Un fracaso desencadena otros | Disyuntores; mamparos; degradación elegante |
| **Coherencia de los datos** | Mantener réplicas sincronizadas | Modelos de consistencia; resolución de conflictos |
---

## Resumen
Los sistemas distribuidos son la forma en que el software moderno escala, sobrevive a fallas y sirve a los usuarios a nivel mundial. Los algoritmos de consenso (Raft, Paxos) garantizan que los nodos estén de acuerdo. Las cadenas de bloques añaden verificación criptográfica y descentralización para crear libros de contabilidad sin confianza. Las bases de datos distribuidas (Cassandra, CockroachDB, DynamoDB) manejan datos a escala. El equilibrio fundamental, captado por el teorema CAP, es entre coherencia y disponibilidad cuando la red no es confiable. Comprender estos conceptos es esencial para construir sistemas que funcionen a escala de Internet.