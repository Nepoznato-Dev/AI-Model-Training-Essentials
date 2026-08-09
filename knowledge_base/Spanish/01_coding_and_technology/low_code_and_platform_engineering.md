---
# Metadatos
título: "Ingeniería de plataformas y código bajo"
descripción: "Plataformas de código bajo, plataformas de desarrollo interno, caminos dorados"
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
Etiquetas: [bajo, código, plataforma, ingeniería, codificación y tecnología]
nivel_dificultad: "intermedio"
requisitos previos: []
estimado_reading_time: "5 minutos"
# Guía de contribución
contribución:
  licencia: "MIT"
  feedback_channel: "Problemas de GitHub"
  how_to_contribute: "Enviar un PR con cambios y actualizar el registro de cambios"
  review_process: "Los mantenedores de categorías revisan los cambios antes de fusionarlos"
---
# Ingeniería de plataforma y código bajo
Las plataformas de código bajo permiten a las personas crear aplicaciones con un mínimo de código escrito a mano, generalmente a través de interfaces de arrastrar y soltar, flujos de trabajo visuales y conectores prediseñados. La ingeniería de plataformas es la disciplina de crear plataformas de desarrollo internas (IDP) que faciliten a los equipos de productos el autoservicio de infraestructura, CI/CD y herramientas operativas. Ambas tendencias son respuestas al mismo problema: la brecha entre la demanda de software y la oferta de desarrolladores que pueden construirlo.
---

## Plataformas de código bajo
### Lo que realmente significa Low-Code
| Aspecto | Descripción |
|--------|-------------|
| **Desarrollo visual** | Constructores de UI de arrastrar y soltar; editores visuales de flujo de trabajo; diseñadores de formularios |
| **Componentes prediseñados** | Widgets, conectores, plantillas e integraciones listos para usar |
| **Lógica declarativa** | Configurar el comportamiento mediante reglas y condiciones en lugar de escribir código |
| **Extensibilidad** | Posibilidad de agregar código personalizado cuando las capacidades integradas de la plataforma no son suficientes |
| **Infraestructura gestionada** | La plataforma se encarga del alojamiento, el escalado y los parches de seguridad |
### Plataformas populares de código bajo
| Plataforma | Fuerza | Caso de uso típico |
|----------|----------|-----------------|
| **Plataforma de energía de Microsoft** | Integración profunda de Microsoft 365/Azure; Power Apps, Power Automate, Power BI | Flujos de trabajo empresariales; herramientas internas |
| **Plataforma Salesforce** | Nativo de CRM; Ápice para extensiones; Generador de flujo | Aplicaciones orientadas al cliente; flujos de trabajo de ventas |
| **Servicio Ahora** | gestión de servicios de TI; automatización del flujo de trabajo | operaciones de TI; HORA; instalaciones |
| **Apia** | Minería de procesos; gestión de casos | Procesos comerciales complejos; cumplimiento |
| **OutSystems** | Web y móvil de pila completa; nivel empresarial | Portales de clientes; aplicaciones móviles |
| **Reequipar** | Constructor de herramientas interno; se conecta a bases de datos y API | Paneles de administración; tableros de instrumentos; herramientas de operaciones |
| **Mesa de aire** | Híbrido hoja de cálculo-base de datos; automatizaciones | Seguimiento de proyectos; CRM ligero |
### Cuando el código bajo funciona bien
| Escenario | Por qué encaja el código bajo |
|----------|-------------------|
| **Herramientas internas** | Rápido de construir; los usuarios son internos, por lo que la flexibilidad de la interfaz de usuario importa menos |
| **Formularios y aprobaciones** | Los creadores de flujos de trabajo visuales se destacan en esto |
| **Aplicaciones CRUD** | La mayoría de las plataformas de código bajo están optimizadas para patrones de creación, lectura, actualización y eliminación.
| **Creación de prototipos** | Validar una idea en horas en lugar de semanas |
| **Desarrollo ciudadano** | Los analistas de negocios pueden crear sus propias soluciones con gobierno de TI |
### Cuando el código bajo se queda corto
| Limitación | Impacto |
|------------|--------|
| **Fijación de proveedor** | Las aplicaciones no se pueden migrar fácilmente fuera de la plataforma |
| **Límites máximos de rendimiento** | No apto para aplicaciones de alto rendimiento o sensibles a la latencia |
| **Restricciones de la interfaz de usuario** | Los diseños personalizados son difíciles; estás limitado a lo que admite la plataforma |
| **Complejidad de la integración** | La conexión a API inusuales o sistemas heredados puede requerir código personalizado de todos modos |
| **Costo a escala** | Los precios por usuario o por aplicación pueden volverse costosos a medida que aumenta el uso |
| **Dificultad de depuración** | Las abstracciones visuales dificultan el diagnóstico de problemas complejos |
---

## Ingeniería de plataforma
### El problema que resuelve la ingeniería de plataformas
| Sin Ingeniería de Plataforma | Con Ingeniería de Plataforma |
|------------------------------|---------------------|
| Cada equipo gestiona su propia infraestructura | Infraestructura de resúmenes de plataforma de autoservicio |
| Herramientas inconsistentes entre equipos | Cadena de herramientas estandarizada; caminos dorados |
| Los desarrolladores esperan que las operaciones aprovisionen recursos | Los desarrolladores suministran recursos bajo demanda |
| Silos de conocimiento; conocimiento tribal | Documentado; automatizado; descubrible |
| Incorporación lenta para nuevos ingenieros | Los nuevos ingenieros pueden implementarse desde el primer día |
### Componentes principales de una plataforma de desarrollo interna
| Componente | Propósito | Herramientas de ejemplo |
|-----------|---------|---------------|
| **Catálogo de servicios** | Registro central de todos los servicios y sus propietarios | Entre bastidores; Puerto; Corteza |
| **Andamios con plantilla** | Generar nuevos servicios a partir de plantillas aprobadas | Plantillas de software entre bastidores; Cortador de galletas |
| **Infraestructura de autoservicio** | Los desarrolladores aprovisionan recursos en la nube sin presentar tickets | Módulos Terraform; Pulumi; Plano cruzado |
| **Canalizaciones de CI/CD** | Tuberías estandarizadas de construcción, prueba e implementación | Acciones de GitHub; GitLab CI; CD Argó |
| **Gestión medioambiental** | Entornos efímeros de desarrollo y puesta en escena bajo demanda | Vclúster; Espacio de nombres; Gitpod |
| **Observabilidad** | Registro, métricas y seguimiento integrados en cada servicio | Prometeo; Grafana; OpenTelemetría; Perro de datos |
| **Gestión secreta** | Almacenamiento seguro y rotación de credenciales | Bóveda; Administrador de secretos de AWS; SOPS |
| **Identidad y acceso** | SSO; acceso basado en roles; autenticación de servicio a servicio | Okta; capa de llaves; ESPIFE |
### Caminos Dorados
Un camino dorado es la forma apoyada y obstinada de hacer algo. Es el camino de menor resistencia: si lo sigues, todo funciona. Puedes desviarte del camino, pero estás solo.
| Camino Dorado | Qué proporciona |
|-------------|-----------------|
| **Nuevo servicio** | Repositorio de plantillas; CI/CD; escucha; explotación florestal; configuración de implementación |
| **Nueva base de datos** | Instancia aprovisionada; cadenas de conexión en secretos; copia de seguridad configurada |
| **Nueva interfaz** | Construir oleoductos; CDN; entornos de vista previa; controles de faro |
| **Canalización de datos** | Orquestación; validación de esquemas; escucha; alertando |
### Decisiones de construcción versus compra
| factor | Crear personalizado | Utilice la herramienta existente |
|--------|-------------|-------------------|
| **Competencia básica** | Único para su negocio; ventaja competitiva | Producto; toda empresa lo necesita |
| **Carga de mantenimiento** | Tienes capacidad para mantenerlo | La herramienta está bien mantenida por el proveedor/comunidad |
| **Necesidades de integración** | Se requiere una integración profunda con los sistemas internos | Las API y los conectores estándar son suficientes |
| **Costo** | Más barato de construir que de licencia | Más barato licenciar que construir |
---

## La relación entre Low-Code y la ingeniería de plataformas
| Dimensión | Código bajo | Ingeniería de Plataformas |
|-----------|----------|---------------------|
| **Usuario objetivo** | Usuarios empresariales; desarrolladores ciudadanos | Ingenieros de software profesionales |
| **Objetivo** | Reducir el código; aumentar la velocidad | Reducir la carga cognitiva; aumentar la autonomía |
| **Nivel de abstracción** | Muy alto; visuales | Medio; basado en código pero simplificado |
| **Flexibilidad** | Limitado por las capacidades de la plataforma | Flexibilidad total; puedes escribir cualquier código |
| **Gobernanza** | Plataforma hace cumplir las reglas | Plataforma ofrece caminos dorados |
Son complementarios: la ingeniería de plataformas hace que los desarrolladores profesionales sean más rápidos, mientras que el código bajo permite a los no desarrolladores crear aplicaciones simples. Juntos, abordan la brecha en la entrega de software desde diferentes ángulos.
---

## Resumen
Tanto las plataformas de código bajo como las plataformas de desarrollo interno tienen como objetivo aumentar la cantidad de personas que pueden entregar software. Low-code hace esto abstrayendo el código por completo: constructores visuales, conectores prediseñados, lógica declarativa. La ingeniería de plataformas hace esto para los desarrolladores profesionales al brindarles infraestructura de autoservicio, caminos dorados y herramientas estandarizadas para que dediquen menos tiempo al trabajo operativo y más tiempo a las características del producto. Ninguna de las dos es una solución milagrosa: el código bajo tiene limitaciones de rendimiento y dependencia del proveedor, y la ingeniería de la plataforma requiere una inversión continua para su mantenimiento. Pero cuando se aplican a los problemas correctos (herramientas internas, aplicaciones CRUD, prestación de servicios estandarizados), ambos pueden reducir drásticamente el tiempo desde la idea hasta la producción.