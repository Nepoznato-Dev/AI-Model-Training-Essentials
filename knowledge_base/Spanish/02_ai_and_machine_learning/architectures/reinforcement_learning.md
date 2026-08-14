---
# Metadata
title: "Reinforcement Learning"
description: "MDPs, Q-learning, policy gradients, RLHF, multi-agent systems"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to architectures/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [reinforcement, learning, ai-and-machine-learning]
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

# Aprendizaje por refuerzo
El aprendizaje por refuerzo (RL) es la forma en que las máquinas aprenden a tomar secuencias de decisiones mediante prueba y error. A diferencia del aprendizaje supervisado, donde se proporciona la respuesta correcta para cada ejemplo, RL le da al agente solo una señal de recompensa, y el agente debe descubrir qué acciones conducen a los mejores resultados con el tiempo. Es el enfoque detrás de AlphaGo, el control robótico, la IA para juegos y, fundamentalmente, RLHF, la técnica utilizada para alinear grandes modelos de lenguaje modernos con las preferencias humanas.
---

## Conceptos básicos
RL enmarca la toma de decisiones como un bucle entre un **agente** y un **entorno**.
| Componente | Rol | Ejemplo |
|-----------|------|---------|
| **Agente** | El tomador de decisiones | Un programa de ajedrez, un robot, un modelo de lenguaje |
| **Medio ambiente** | El mundo con el que interactúa el agente | El tablero de ajedrez, un almacén, una conversación |
| **Estado** | La situación actual | Posición del tablero, lecturas de sensores del robot, historial de chat |
| **Acción** | Qué puede hacer el agente | Mueve una pieza, gira a la izquierda, genera una ficha |
| **Recompensa** | Señal de retroalimentación (número escalar) | +1 por ganar, -1 por estrellarse, puntuación de preferencia humana |
| **Política** | Estrategia que asigna estados a acciones | "Si el rey está amenazado, muévelo" |
| **Función de valor** | Recompensa acumulativa esperada de un estado | "Esta posición en el tablero vale alrededor de +3 puntos" |
### El bucle RL
```
Agent observes State → chooses Action → Environment returns new State + Reward
        ↑                                                                         |
        └─────────────────────────────────────────────────────────────────────────┘
```

El objetivo del agente es maximizar la **recompensa acumulativa** a lo largo del tiempo, no solo la recompensa inmediata. Esto es lo que diferencia fundamentalmente la RL del aprendizaje supervisado.
---

## Diferencias clave con otros paradigmas de aprendizaje
| Aspecto | Aprendizaje supervisado | Aprendizaje no supervisado | Aprendizaje por refuerzo |
|--------|-------------------|---------------------|----------------------|
| **Señal** | Etiquetas correctas para cada ejemplo | Sin etiquetas; encontrar estructura | Recompensa escalar, a menudo retrasada |
| **Comentarios** | Inmediato | Ninguno | Retrasado y escaso |
| **Secuencia** | Cada ejemplo es independiente | Cada ejemplo es independiente | Acciones afectan estados futuros |
| **Objetivo** | Minimizar el error de predicción | Descubre patrones | Maximizar la recompensa acumulada |
---

## Procesos de decisión de Markov (MDP)
Los MDP son el marco matemático para RL. Asumen que el futuro depende sólo del estado actual, no de la historia de cómo se llegó allí (la **propiedad de Markov**).
| Componente | Notación | Significado |
|-----------|----------|---------|
| **Estados** | S | Todas las situaciones posibles en las que se puede encontrar el agente |
| **Acciones** | Un | Todo lo que el agente puede hacer |
| **Función de transición** | P(s' \| s, a) | Probabilidad de llegar a los estados s' después de realizar la acción a en los estados s |
| **Función de recompensa** | R(s, a, s') | Recompensa recibida por la transición |
| **Factor de descuento** | γ (gamma) | Cuánto valorar las recompensas futuras vs las inmediatas (0 a 1) |
El **reembolso** (recompensa total con descuento) es:
```
G = R₁ + γR₂ + γ²R₃ + ...
```

Un factor de descuento alto (γ cercano a 1) significa que el agente tiene visión de futuro. Un nivel bajo significa que es miope.
---

## Algoritmos RL clásicos
### Métodos basados ​​en valores
Estos aprenden qué tan bueno es cada estado (o par estado-acción).
| Algoritmo | Idea clave | Limitación |
|-----------|----------|------------|
| **Q-Aprendizaje** | Aprenda una tabla de valores Q: Q(estado, acción) = recompensa esperada | No se adapta a grandes espacios estatales |
| **Red Q profunda (DQN)** | Utilice una red neuronal para aproximar los valores Q | Sólo maneja acciones discretas; puede ser inestable |
| **Doble DQN** | Arreglar el sesgo de sobreestimación de Q-learning | Todavía limitado a acciones discretas |
Regla de actualización de Q-learning:
```
Q(s, a) ← Q(s, a) + α [r + γ max Q(s', a') - Q(s, a)]
```

### Métodos basados ​​en políticas
Estos aprenden directamente la política (estrategia) sin estimar valores.
| Algoritmo | Idea clave | Ventaja |
|-----------|----------|-----------|
| **REFUERZAR** | gradiente de la política de Montecarlo; actualizar la política en dirección a buenos resultados | Simple; trabaja con acciones continuas |
| **PPO** (Optimización de política próxima) | Recortar las actualizaciones de políticas para evitar cambios grandes y desestabilizadores | Estable; ampliamente utilizado; buen valor predeterminado |
| **TRPO** | Método de región de confianza para actualizaciones de políticas | Más principios que PPO; más difícil de implementar |
### Métodos actor-crítico
Combine lo mejor de ambos: un **actor** (política) y un **crítico** (función de valor).
| Algoritmo | Idea clave |
|-----------|----------|
| **A2C/A3C** | Ventaja Actor-Crítico; utiliza estimación de ventajas para reducir la varianza |
| **SAC** (Actor-crítico suave) | Maximizar la recompensa manteniendo la exploración (regularización de entropía) |
| **TD3** (DDPG gemelo retardado) | Abordar la sobreestimación en espacios de acción continua |
---

## RLHF: Aprendizaje reforzado a partir de la retroalimentación humana
RLHF es la técnica que hizo posible ChatGPT. Cierra la brecha entre un modelo que puede predecir texto y uno que produce resultados que los humanos realmente encuentran útiles.
### Los tres pasos
| Paso | Qué pasa | Salida |
|------|-------------|--------|
| **1. Ajuste Supervisado (SFT)** | Afinar un modelo previamente entrenado con ejemplos escritos por humanos de alta calidad | Un modelo que sigue razonablemente bien las instrucciones |
| **2. Entrenamiento del modelo de recompensa** | Los humanos comparan pares de resultados del modelo; entrenar un modelo para predecir las preferencias humanas | Un modelo de recompensa que puntúa la calidad de los resultados |
| **3. Optimización de RL** | Utilice PPO para ajustar el modelo SFT y maximizar las puntuaciones del modelo de recompensa | Un modelo alineado con las preferencias humanas |
### Por qué es importante RLHF
Sin RLHF, un modelo de lenguaje es como un estudiante que ha leído todos los libros pero no sabe cómo comportarse en una conversación. Puede generar texto, pero el texto puede ser inútil, tóxico o perder el sentido por completo. RLHF le enseña al modelo *lo que quieren los humanos*, no solo cómo se ve el texto.
### Variantes y alternativas
| Método | Descripción | Ventaja |
|--------|-------------|-----------|
| **DPO** (Optimización de preferencias directas) | Omita el modelo de recompensa; optimizar directamente la política a partir de las preferencias humanas | Más sencillo; no hay un modelo de recompensa separado para entrenar |
| **RLAIF** | Utilice IA (en lugar de humanos) para generar etiquetas de preferencias | Más barato que el etiquetado humano |
| **IA constitucional** | Utilice un conjunto de principios para guiar el comportamiento del modelo sin etiquetas humanas | Más escalable; El enfoque de Anthropic |
| **GRPO** (Optimización de políticas relativas al grupo) | Comparar resultados dentro de un grupo en lugar de hacerlo con un modelo separado | Utilizado en DeepSeek-R1; reduce la necesidad de una red de valor |
---

## Exploración vs Explotación
Ésta es la tensión central en RL. **Explotación** significa elegir acciones que sabes que funcionan bien. **Exploración** significa probar cosas nuevas para descubrir estrategias potencialmente mejores.
| Estrategia | Cómo funciona | Compensación |
|----------|-------------|-----------|
| **ε-codicioso** | Elige la mejor acción la mayor parte del tiempo; acción aleatoria con probabilidad ε | Simple pero ineficiente |
| **Exploración Boltzmann** | Elija acciones probabilísticamente en función de sus valores estimados | Más suave que ε-codicioso |
| **UCB** (Límite superior de confianza) | Prefiere acciones con alta incertidumbre (optimismo ante la incertidumbre) | Buenas garantías teóricas |
| **Regularización de entropía** | Agregue un bono por visitar diversos estados (usado en SAC, PPO) | Fomenta la exploración natural |
---

## Aprendizaje por refuerzo multiagente
Cuando varios agentes aprenden simultáneamente, la dinámica se vuelve mucho más compleja.
| Escenario | Desafío | Ejemplo |
|----------|-----------|---------|
| **Cooperativa** | Los agentes deben coordinar; la asignación de crédito es difícil | Equipos de fútbol de robots; redes distribuidas de sensores |
| **Competitivo** | Los oponentes se adaptan; el medio ambiente no es estacionario | Juego de IA (póquer, StarCraft); ciberseguridad |
| **Mixto** | Algunos agentes cooperan, otros compiten | Mercados de subastas; sistemas de tráfico |
| Algoritmo | Descripción |
|-----------|-------------|
| **MADDPG** | Versión multiagente de DDPG; crítico centralizado, actores descentralizados |
| **MAPPO** | PPO de agentes múltiples; ampliamente utilizado en la práctica |
| **Autojuego** | Agentes entrenan contra copias de sí mismos (AlphaGo, AlphaStar) |
---

## Transferencia de Sim a Real
Entrenar robots en el mundo real es lento y peligroso. En cambio, los agentes se entrenan en simulación y transferencia a la realidad.
| Desafío | Solución |
|-----------|----------|
| **Brecha de realidad** (simulación ≠ mundo real) | Aleatorización de dominios: variar los parámetros físicos durante el entrenamiento |
| **Ineficiencia de la muestra** | Utilice RL basado en modelos o entrene en grandes simulaciones paralelas |
| **Seguridad** | RL restringido: penalizar acciones inseguras durante el entrenamiento |
| **Observabilidad parcial** | Tren con sensores ruidosos y observaciones retrasadas |
Empresas como Boston Dynamics y Tesla utilizan ampliamente la simulación, pero la brecha entre el rendimiento físico y el simulado sigue siendo uno de los mayores desafíos del campo.
---

## Herramientas y marcos
| Herramienta | Propósito | Mejor para |
|------|---------|----------|
| **Líneas de base estables3** | Implementaciones limpias de Python de PPO, SAC, TD3, DQN | Aprendizaje y creación de prototipos |
| **RLlib** | Biblioteca RL escalable construida sobre Ray | Formación distribuida a gran escala |
| **LimpioRL** | Implementaciones de archivo único para investigación | Comprender profundamente los algoritmos |
| **Gimnasio (OpenAI)** | Interfaz de entorno estandarizado | Definición de problemas de RL |
| **Gimnasio Isaac / Laboratorio Isaac** | Simulación de física acelerada por GPU | Robótica, sim-real |
| **TRL** (Biblioteca RL de transformadores) | RLHF, DPO, PPO para modelos lingüísticos | Alineación de LLM |
| **AbiertoRLHF** | Marco distribuido RLHF | Entrenamiento de modelos grandes con RLHF |
---

## Consejos prácticos
- **Comience con PPO.** Es el algoritmo de propósito general más confiable. Si no está seguro de qué usar, PPO es la opción predeterminada.
- **Normaliza tus recompensas.** La escala de recompensas afecta drásticamente la estabilidad del entrenamiento.
- **Utilice entornos vectorizados.** La ejecución de muchos entornos en paralelo (por ejemplo, 8–64) estabiliza las estimaciones de gradiente y acelera enormemente el entrenamiento.
- **Supervise tanto la recompensa como la entropía.** Si la entropía cae a cero, su agente ha dejado de explorar y puede estar atrapado en un óptimo local.
- **La configuración de recompensas es un arte.** Diseñar la función de recompensa adecuada suele ser la parte más difícil. Las escasas recompensas (solo al final) hacen que el aprendizaje sea extremadamente lento. Las recompensas densas y bien definidas guían al agente, pero pueden introducir un comportamiento no deseado.
- **RLHF es frágil.** Pequeños cambios en el modelo de recompensa o en los hiperparámetros de PPO pueden provocar grandes caídas en la calidad. DPO es una alternativa más estable si no necesita el canal RLHF completo.
---

## Resumen
El aprendizaje por refuerzo es el estudio de cómo los agentes aprenden a tomar decisiones a través de la interacción. Abarca desde algoritmos clásicos como Q-learning hasta métodos modernos de RL profundo como PPO y SAC, y sustenta algunos de los avances recientes más importantes en IA, desde los juegos hasta la alineación de modelos de lenguaje. El desafío principal sigue siendo el mismo: ¿cómo se aprende un comportamiento óptimo cuando la retroalimentación es tardía, escasa y ruidosa? La respuesta (ensayo y error, guiado por matemáticas inteligentes) resulta ser una de las ideas más poderosas de toda la inteligencia artificial.