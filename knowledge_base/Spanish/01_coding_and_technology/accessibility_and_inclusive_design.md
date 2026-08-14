<!--
---
# Metadata
title: "Accessibility and Inclusive Design"
description: "WCAG, inclusive UX, assistive technology, accessible coding"
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
tags: [accessibility, inclusive, design, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Accesibilidad y Diseño Inclusivo
La accesibilidad (a menudo abreviada como a11y) es la práctica de hacer que el software sea utilizable por todos, incluidas las personas con discapacidades visuales, auditivas, motoras, cognitivas y neurológicas. Es un requisito legal en muchas jurisdicciones y una práctica de ingeniería estándar. El software accesible es mejor software para todos, porque las decisiones de diseño que apoyan a los usuarios discapacitados (estructura clara, navegación por teclado, contraste suficiente, texto legible) mejoran la experiencia para todos los usuarios.
---

## ¿Quién se beneficia de la accesibilidad?
| Tipo de discapacidad | Ejemplos | Tecnología de asistencia |
|----------------|---------|---------------------|
| **Visual** | Ceguera, baja visión, daltonismo | Lectores de pantalla (JAWS, NVDA, VoiceOver); lupas; modos de alto contraste |
| **Auditivo** | Sordera, problemas de audición | Subtítulos; transcripciones; alertas visuales |
| **Motor** | Destreza limitada, parálisis, temblor | Navegación sólo con teclado; control de voz; dispositivos de conmutación; seguimiento ocular |
| **Cognitivo** | Dislexia, TDAH, autismo, problemas de memoria | Lenguaje claro; navegación consistente; distracciones reducidas |
| **Temporal** | Brazo roto, luz solar brillante, ambiente ruidoso | Mismas adaptaciones que las discapacidades permanentes |
| **Situacional** | Sostener a un bebé, conducir, con una mano ocupada | Interfaces de voz; objetivos táctiles grandes |
**Información clave**: las funciones de accesibilidad diseñadas para usuarios discapacitados ayudan a todos. Los cortes en las aceras (rampas en las aceras) fueron diseñados para sillas de ruedas, pero los utilizan padres con cochecitos, repartidores con carritos y viajeros con equipaje.
---

## Accesibilidad web (WCAG)
Las Pautas de Accesibilidad al Contenido Web (WCAG) son el estándar internacional para la accesibilidad web.
### Principios WCAG (POUR)
| Principio | Requisito |
|-----------|-------------|
| **Perceptible** | La información debe estar presentable de manera que los usuarios puedan percibirla (alternativas de texto, subtítulos, diseño adaptable) |
| **Operable** | La interfaz debe ser navegable y utilizable (accesible mediante teclado, tiempo suficiente, sin contenido que provoque convulsiones) |
| **Comprensible** | La información y el funcionamiento deben ser comprensibles (legibles, predecibles, asistencia de entrada) |
| **Robusto** | El contenido debe funcionar con las tecnologías de asistencia actuales y futuras |
### Niveles de conformidad WCAG
| Nivel | Requisitos | Objetivo típico |
|-------|-------------|---------------|
| **A** | Nivel mínimo; 30 criterios de éxito | Mínimo legal en algunas jurisdicciones |
| **AA** | Aborda las barreras más comunes | Objetivo estándar para la mayoría de las organizaciones |
| **AAA** | Nivel más alto; no todos los contenidos pueden lograrlo | Contenido especializado; sitios educativos |
### Criterios clave de éxito (nivel AA)
| Criterio | Requisito | Cómo lograrlo |
|-----------|-------------|---------------|
| **1.1.1 Contenido no textual** | Todas las imágenes tienen alternativas de texto |  Atributos `alt`; `aria-label`para iconos |
| **1.3.1 Información y relaciones** | Estructura transmitida programáticamente | HTML semántico; encabezados; liza; puntos de referencia |
| **1.4.3 Contraste (mínimo)** | El texto tiene una relación de contraste de al menos 4,5:1 | Pruebe con fichas de contraste; elija paletas de colores accesibles |
| **1.4.4 Cambiar el tamaño del texto** | El texto se puede cambiar de tamaño al 200% sin pérdida | Utilice unidades relativas (rem, em); diseño responsivo |
| **2.1.1 Teclado** | Todas las funciones disponibles a través del teclado | Sin trampas de teclado; indicadores de enfoque visibles |
| **2.4.3 Orden de enfoque** | El orden de enfoque preserva el significado y la operatividad | Orden de tabulación lógico; El orden DOM coincide con el orden visual |
| **2.4.7 Enfoque visible** | El foco del teclado se indica visualmente | Estilos CSS `:focus-visible`; nunca`outline: none`sin reemplazo |
| **3.3.2 Etiquetas o instrucciones** | Las entradas tienen etiquetas |  Elementos `<label>`; `aria-label`|
| **4.1.2 Nombre, rol, valor** | Los componentes de la interfaz de usuario tienen nombres y funciones accesibles | atributos ARIA; HTML semántico |
---

## ARIA (Aplicaciones de Internet enriquecidas accesibles)
ARIA agrega información de accesibilidad a elementos HTML que no tienen semántica incorporada.
### Roles de ARIA
| Rol | Propósito | Ejemplo |
|------|---------|---------|
| `button`| Identifica un elemento como un botón | Un`<div>`con el estilo de un botón |
| `dialog`| Diálogo modal o no modal | Componentes modales personalizados |
| `tablist`/`tab`/`tabpanel`| Interfaz de pestañas | Componentes de pestañas personalizados |
| `alert`| Mensaje importante que aparece dinámicamente | Notificaciones de errores |
| `progressbar`| Indicador de progreso | Cargando estados |
| `menu`/`menuitem`| Navegación del menú | Menús desplegables |
### Atributos ARIA
| Atributo | Propósito | Ejemplo |
|-----------|---------|---------|
| `aria-label`| Nombre accesible cuando no hay texto visible | Botón de solo ícono:`aria-label="Search"`|
| `aria-describedby`| Vincula el elemento a su descripción | Campo de formulario con texto de ayuda |
| `aria-expanded`| Indica si una sección está expandida | Acordeón; menú desplegable |
| `aria-hidden`| Oculta elemento de la tecnología de asistencia | Iconos decorativos |
| `aria-live`| Anuncia cambios de contenido dinámico | Actualizaciones en vivo; notificaciones |
| `aria-disabled`| Indica que el elemento está deshabilitado | Botones atenuados |
### La primera regla de ARIA
> **No utilice ARIA si puede utilizar HTML nativo en su lugar.** Ya se puede acceder a un `<button>`. Un`<div role="button">`requiere que agregue manualmente el manejo del teclado, la administración del enfoque y la compatibilidad con el lector de pantalla. Utilice HTML semántico primero; ARIA solo cuando los elementos nativos no pueden hacer el trabajo.
---

## Navegación por teclado
| Clave | Comportamiento esperado |
|-----|-------------------|
| **Pestaña** | Mover el foco al siguiente elemento interactivo |
| **Mayús + Tabulador** | Mover el foco al elemento interactivo anterior |
| **Entrar / Espacio** | Activar el elemento enfocado (botón, enlace) |
| **Teclas de flecha** | Navegar dentro de los componentes (menús, pestañas, grupos de radio) |
| **Escapar** | Cerrar un cuadro de diálogo, menú o ventana emergente |
| **Inicio / Fin** | Saltar al primer/último elemento de una lista |
### Trampas comunes del teclado
| Problema | Arreglar |
|---------|-----|
| El foco ingresa a un componente pero no puede salir | Asegúrese de que Tab mueva el foco hacia afuera; manejar Escape |
| Modal no atrapa el foco | El enfoque debe circular dentro del modal; volver al gatillo al cerrar |
| Los componentes personalizados no responden al teclado | Agregue controladores de pulsación de teclas para Intro, Espacio, flechas |
---

## Color y diseño visual
| Directriz | Requisito |
|-----------|-------------|
| **Relación de contraste** | 4,5:1 para texto normal; 3:1 para texto grande (18 puntos+ o 14 puntos+ negrita) |
| **No confíes sólo en el color** | Utilice iconos, texto o patrones además del color |
| **Indicadores de enfoque** | Siempre visible; alto contraste; nunca eliminado sin reemplazo |
| **Cambiar el tamaño del texto** | El diseño debe funcionar con un zoom del 200% |
| **Responsivo** | El contenido debe redistribuirse con un ancho de 320 px (móvil) |
### Consideraciones sobre el daltonismo
| Tipo | Colores afectados | Consejo de diseño |
|------|-----------------|------------|
| **Deuteranopía** | Rojo-verde (más común) | No utilice rojo/verde para transmitir estatus; utilizar iconos + color |
| **Protanopia** | Rojo-verde | Igual que arriba |
| **Tritanopia** | Azul-amarillo | No utilices azul/amarillo como único diferenciador |
---

## Prueba de accesibilidad
| Método | Herramienta | Lo que atrapa |
|--------|------|----------------|
| **Escaneo automatizado** | hacha, faro, OLA | Falta texto alternativo; cuestiones de contraste; Errores ARIA |
| **Prueba de teclado** | Manual: desconecte el mouse, use solo el teclado | Orden de enfoque; trampas de teclado; controladores faltantes |
| **Prueba de lector de pantalla** | NVDA (gratis), VoiceOver (macOS), JAWS | Etiquetas faltantes; mala estructura; cambios no anunciados |
| **Prueba de zoom** | Zoom del navegador al 200%, 400% | Rotura de diseño; texto recortado; problemas de desbordamiento |
| **Contraste de color** | Comprobador de contraste WebAIM, complemento Stark | Relaciones de contraste insuficientes |
| **Prueba de usuario** | Prueba con usuarios discapacitados | Barreras del mundo real que las herramientas automatizadas pasan por alto |
---

## Requisitos legales
| Ley | Región | Requisitos |
|-----|--------|-------------|
| **ADA** (Ley de Estadounidenses con Discapacidades) | Estados Unidos | Los sitios web de alojamientos públicos deben ser accesibles |
| **Sección 508** | Estados Unidos (federal) | Las TIC de las agencias federales deben ser accesibles |
| **EAA** (Ley Europea de Accesibilidad) | UE (2025+) | Los productos y servicios deben cumplir requisitos de accesibilidad |
| **EN 301 549** | UE | Norma técnica de accesibilidad a las TIC |
| **ACA** (Ley de Accesibilidad de Canadá) | Canadá | Gobierno e industrias reguladas |
| **Ley de Igualdad de 2010** | Reino Unido | Los proveedores de servicios deben hacer ajustes razonables |
---

## Accesibilidad móvil
| Plataforma | Directrices | Herramientas clave |
|----------|-----------|-----------|
| **iOS** | Directrices de la interfaz humana de Apple (sección Accesibilidad) | Voz en off; Tipo dinámico; Control de interruptor |
| **Android** | Pautas de accesibilidad de Android | Respuesta de conversación; Acceso por interruptor; Seleccione para hablar |
| Preocupación móvil | Solución |
|---------------|----------|
| **Objetivos táctiles** | Mínimo 44×44 puntos (iOS) / 48×48 dp (Android) |
| **Compatibilidad con lectores de pantalla** | Descripciones de contenido; etiquetas de accesibilidad |
| **Sensibilidad al movimiento** | Respeto `prefers-reduced-motion`; evitar animaciones de reproducción automática |
| **Tamaño de texto dinámico** | Tamaños de fuente del sistema de soporte; utilizar unidades de texto escalables |
---

## Resumen
La accesibilidad es un principio de diseño que debe informar cada decisión desde el principio, no una característica agregada al final. Utilice HTML semántico. Asegúrese de que la navegación con el teclado funcione. Mantenga un contraste de color suficiente. Proporcione alternativas de texto para contenido que no sea de texto. Pruebe con lectores de pantalla y usuarios discapacitados. El resultado es un software que funciona mejor para todos, incluidos aquellos con discapacidades temporales, limitaciones situacionales, dispositivos más antiguos, conexiones lentas y las muchas formas en que el uso en el mundo real difiere de un entorno de desarrollo controlado.