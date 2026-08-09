---
# Metadatos
título: "Desarrollo móvil"
descripción: "iOS, Android, React Native, Flutter, arquitectura móvil"
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
Etiquetas: [móvil, desarrollo, codificación y tecnología]
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
# Desarrollo móvil
El desarrollo móvil es la práctica de crear aplicaciones para teléfonos inteligentes y tabletas, principalmente para iOS (Apple) y Android (Google). Abarca todo, desde el diseño de la interfaz de usuario para pantallas pequeñas hasta la gestión de la duración de la batería, el manejo de la inestabilidad de la red y la distribución de aplicaciones a través de las tiendas. El campo ha madurado significativamente y los marcos multiplataforma ahora compiten con el desarrollo nativo en la mayoría de los casos de uso.
---

## El panorama móvil
| Plataforma | Desarrollador | Idioma(s) | Tienda | Cuota de mercado (global) |
|----------|-----------|-------------|-------|----------------------|
| **Android** | Google | Kotlin, Java | Google Play | ~72% |
| **iOS** | manzana | Rápido, Objective-C | Tienda de aplicaciones | ~27% |
---

## Desarrollo Nativo
### androide
| Aspecto | Detalles |
|--------|---------|
| **Idioma** | Kotlin (primario), Java (heredado) |
| **Marco de interfaz de usuario** | Jetpack Compose (moderno), diseños XML (heredados) |
| **Construir sistema** | Gradle |
| **IDE** | Estudio de Android |
| **SDK mínimo** | El desarrollador elige; API 24+ más objetivo (Android 7.0, 2016) |
| **Distribución** | Tienda Google Play; tiendas alternativas en algunos mercados |
### iOS
| Aspecto | Detalles |
|--------|---------|
| **Idioma** | Swift (primario), Objective-C (heredado) |
| **Marco de interfaz de usuario** | SwiftUI (moderno), UIKit (maduro) |
| **Construir sistema** | Sistema de compilación Xcode |
| **IDE** | Xcode (solo macOS) |
| **Versión mínima** | El desarrollador elige; la mayoría apunta a iOS 16+ |
| **Distribución** | Apple App Store (única opción para la mayoría de las aplicaciones) |
---

## Marcos multiplataforma
Compile una vez e implemente tanto en iOS como en Android.
| Marco | Idioma | Representación | Rendimiento | Mejor para |
|-----------|----------|-----------|-------------|----------|
| **Aleteo** | Dardo | Motor personalizado (Skia/Impeller) | Casi nativo | Ricas interfaces de usuario personalizadas; mirada consistente en todas las plataformas |
| **Reaccionar nativo** | JavaScript/Mecanografiado | Componentes nativos vía puente | Bueno (la nueva arquitectura mejora esto) | Equipos con experiencia web/JS |
| **Kotlin multiplataforma** | Kotlin | UI nativa por plataforma | Nativo | Compartir lógica empresarial; interfaz de usuario nativa |
| **MAUI** (.NET) | C# | Controles nativos | Bueno | equipos .NET; aplicaciones empresariales |
| **Iónico / Condensador** | HTML/CSS/JS | Vista web | Inferior | Aplicaciones sencillas; equipos web |
### Flutter vs Reaccionar nativo
| Aspecto | Aleteo | Reaccionar nativo |
|--------|---------|-------------|
| **Idioma** | Dardo | JavaScript/Mecanografiado |
| **Representación de interfaz de usuario** | Dibuja todo por sí mismo (consistente en todas las plataformas) | Utiliza componentes nativos (aspecto específico de la plataforma) |
| **Recarga en caliente** | Excelente | Bueno |
| **Ecosistema** | Creciendo rápidamente; basado en widgets | Grande; ecosistema npm |
| **Curva de aprendizaje** | Necesito aprender Dart | Más fácil para desarrolladores web |
| **Integración de plataforma** | Canales de plataforma para código nativo | Módulos nativos vía puente |
| **Rendimiento** | Excelente; casi nativo | Bien; puente elevado (reducido con nueva arquitectura) |
---

## Patrones de arquitectura móvil
| Patrón | Descripción | Cuándo utilizar |
|---------|-------------|-------------|
| **MVC** | Modelo-Vista-Controlador | Aplicaciones sencillas; familiar para los desarrolladores web |
| **MVVM** | Modelo-Vista-VerModelo; enlace de datos | Aplicaciones móviles más modernas |
| **MVI** | Modelo-Vista-Intento; flujo de datos unidireccional | Gestión estatal compleja; Aleteo (con BLoC/Riverpod) |
| **Arquitectura limpia** | Capas con inversión de dependencia | Equipos grandes; lógica empresarial compleja |
---

## Preocupaciones clave sobre dispositivos móviles
### Diseño sin conexión
Las aplicaciones móviles deben funcionar sin una conexión a Internet confiable.
| Estrategia | Descripción |
|----------|-------------|
| **Base de datos local** | Almacenar datos en el dispositivo (SQLite, Room, CoreData, Realm) |
| **Estrategia de sincronización** | Sincronizar con el servidor cuando esté en línea; resolver conflictos |
| **IU optimista** | Actualice la interfaz de usuario inmediatamente; conciliar cuando el servidor responde |
| **Caché** | Caché de respuestas de API; servir desde caché cuando no hay conexión |
### Actuación
| Preocupación | Solución |
|---------|----------|
| **Hora de inicio de la aplicación** | Carga diferida; minimizar el trabajo de inicialización |
| **Uso de memoria** | Compresión de imágenes; evitar pérdidas de memoria; utilizar herramientas de creación de perfiles |
| **Drenaje de la batería** | Reducir el trabajo en segundo plano; solicitudes de red por lotes; utilizar servicios de localización eficientes |
| **Eficiencia de la red** | Comprimir cargas útiles; utilizar paginación; caché agresivamente |
| **Desplazamiento de lista** | Reciclar vistas; utilizar carga diferida para imágenes |
### Seguridad
| Preocupación | Solución |
|---------|----------|
| **Datos en reposo** | Cifre datos confidenciales (llavero en iOS, EncryptedSharedPreferences en Android) |
| **Red** | Siempre HTTPS; fijación de certificados para aplicaciones sensibles |
| **Autenticación** | Biometría (Face ID, huella digital); OAuth; almacenamiento de fichas |
| **Ofuscación de código** | ProGuard/R8 para Android; código de bits para iOS |
| **Jailbreak/detección de raíz** | Detectar dispositivos comprometidos; limitar la funcionalidad |
---

## Ciclo de vida de la aplicación
| Estado | Descripción | Qué hacer |
|-------|-------------|------------|
| **Primer plano (activo)** | El usuario interactúa con la aplicación | Funcionamiento normal |
| **Fondo** | La aplicación no es visible pero aún está en la memoria | Pausar animaciones; guardar estado |
| **Suspendido** | OS ha congelado la aplicación para ahorrar recursos | Nada; aplicación está congelada |
| **Terminado** | OS eliminó la aplicación para liberar memoria | Restaurar el estado en el próximo lanzamiento |
---

## Notificaciones automáticas
| Plataforma | Servicio | Protocolo |
|----------|---------|----------|
| **iOS** | APN (servicio de notificaciones push de Apple) | HTTP/2 |
| **Android** | FCM (mensajería en la nube de Firebase) | HTTP/v1 |
| Tipo de notificación | Descripción |
|-------------------|-------------|
| **Notificación de datos** | Silencioso; aplicación procesa la carga útil | Actualizaciones de antecedentes |
| **Mostrar notificación** | Muestra en la bandeja de notificaciones | Alertas de usuario |
| **Notificación enriquecida** | Incluye imágenes, acciones o interfaz de usuario personalizada | Participación mejorada del usuario |
---

## Distribución de aplicaciones
| Plataforma | Tienda | Tiempo de revisión | Recorte de ingresos |
|----------|-------|-------------|-------------|
| **iOS** | Tienda de aplicaciones | 24-48 horas | 30% (15% para pequeñas empresas) |
| **Android** | Google Play | Horas a días | 30% (15% por el primer millón de dólares) |
| **Android (alternativa)** | Tienda Samsung Galaxy, Tienda de aplicaciones de Amazon, F-Droid | Varía | Varía |
### CI/CD para dispositivos móviles
| Herramienta | Propósito |
|------|---------|
| **Carril rápido** | Automatizar compilaciones, capturas de pantalla, firmas e implementación |
| **Acciones de GitHub** | CI/CD con ejecutores macOS para compilaciones de iOS |
| **Bitrise** | CI/CD centrado en dispositivos móviles |
| **Centro de aplicaciones** (Microsoft) | Construir, probar, distribuir (a punto de desaparecer; surgen alternativas) |
| **EAS** (Servicios de aplicaciones de exposición) | Construcciones en la nube para React Native/Expo |
---

## Pruebas
| Tipo | Herramientas | Propósito |
|------|-------|---------|
| **Pruebas unitarias** | Unidad JU, XCTest | Probar la lógica empresarial |
| **Pruebas de widgets** | Prueba de widget de aleteo, Robolectric | Pruebe los componentes de la interfaz de usuario de forma aislada |
| **Pruebas de integración** | Espresso (Android), XCUITest (iOS), Integración de Flutter | Interacciones de los componentes de prueba |
| **Pruebas E2E** | Desintoxicación, Appium, Maestro | Pruebe flujos de usuarios completos en dispositivos reales/simulados |
| **Pruebas de rendimiento** | Perfilador de Android, Instrumentos (iOS) | Medir la velocidad de fotogramas, la memoria y la CPU |
---

## Resumen
El desarrollo móvil ofrece la posibilidad de elegir entre nativo (mejor rendimiento, específico de la plataforma) y multiplataforma (código base compartido, iteración más rápida). Flutter y React Native han madurado hasta el punto en que la multiplataforma es la opción correcta para la mayoría de las aplicaciones. Los desafíos principales siguen siendo los mismos independientemente del marco: diseño fuera de línea, rendimiento en hardware limitado, eficiencia de la batería, seguridad en dispositivos que no son de confianza y navegación en los procesos de revisión de la tienda de aplicaciones. Este campo recompensa a los desarrolladores que piensan primero en la experiencia del usuario: inicio rápido, desplazamiento fluido y manejo elegante de una conectividad deficiente.