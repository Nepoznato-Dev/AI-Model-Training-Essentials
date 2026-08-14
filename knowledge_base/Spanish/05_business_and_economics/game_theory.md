---
# Metadata
title: "Game Theory and Strategic Thinking"
description: "Nash equilibrium, prisoner's dilemma, mechanism design, auctions"
category: "Business and Economics"
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
reviewed_by: "Business & Economics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [game, theory, business-and-economics]
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
# Teoría de juegos y pensamiento estratégico
La teoría de juegos es el estudio matemático de las interacciones estratégicas: situaciones en las que el resultado depende no sólo de lo que usted hace, sino de lo que hacen los demás. Se aplica en todas partes: competencia empresarial, relaciones internacionales, subastas, negociaciones, biología evolutiva y decisiones cotidianas como elegir una ruta a través del tráfico. La idea central es que los actores racionales en situaciones estratégicas no sólo optimizan su propia estrategia: anticipan lo que otros harán y otros están haciendo lo mismo.
---

## Conceptos fundamentales
### Terminología clave
| Término | Definición |
|------|-----------|
| **Juego** | Cualquier situación en la que dos o más tomadores de decisiones (jugadores) cuyas elecciones afectan los resultados de cada uno |
| **Jugador** | Un tomador de decisiones en el juego |
| **Estrategia** | Un plan de acción completo para cada situación que pueda surgir |
| **Recompensa** | El resultado que recibe un jugador de una combinación particular de estrategias |
| **Equilibrio de Nash** | Un conjunto de estrategias donde ningún jugador puede mejorar su rentabilidad cambiando unilateralmente su estrategia |
| **Estrategia dominante** | Una estrategia que es mejor independientemente de lo que hagan otros jugadores |
| **Juego de suma cero** | La ganancia de un jugador es exactamente la pérdida de otro |
| **Juego de suma distinta de cero** | Potencialmente, todos los jugadores pueden ganar o perder |
| **Juego cooperativo** | Los jugadores pueden llegar a acuerdos vinculantes |
| **Juego no cooperativo** | Sin acuerdos vinculantes; cada jugador actúa por interés propio |
---

## Juegos clásicos
### El dilema del prisionero
Dos sospechosos son arrestados. Cada uno puede cooperar (permanecer en silencio) o desertar (confesar).
| | B Coopera | B Defectos |
|---|-------------|-----------|
| **A Coopera** | A: 1 año, B: 1 año | A: 10 años, B: gratis |
| **A Defectos** | A: gratis, B: 10 años | A: 5 años, B: 5 años |
| Perspectiva | Descripción |
|---------|-------------|
| **Estrategia dominante** | El defecto es dominante para ambos jugadores |
| **Equilibrio de Nash** | Ambos defectuosos (5 años cada uno) |
| **Óptimo de Pareto** | Ambos cooperan (1 año cada uno) |
| **Lección** | Las decisiones individuales racionales pueden conducir a peores resultados colectivos |
### Otros juegos clásicos
| Juego | Descripción | Equilibrio de Nash | Lección |
|------|-------------|-----------------|--------|
| **Pollo (halcón-paloma)** | Dos conductores se dirigen el uno hacia el otro; desviarse o seguir recto | Uno se desvía, el otro sigue recto | Política arriesgada; credibilidad del compromiso |
| **Caza del ciervo** | Cazar un ciervo juntos (beneficio alto) o cazar una liebre solo (beneficio bajo) | Ambos ciervos o ambos liebres | Coordinación; confianza |
| **Batalla de los Sexos** | Dos jugadores prefieren resultados diferentes pero quieren coordinarse | Ambos van al mismo evento | Equilibrios múltiples; quien se mueve primero tiene ventaja |
| **Juego de ultimátum** | El proponente divide el dinero; el respondedor acepta o rechaza (ambos no obtienen nada) | El proponente ofrece un mínimo; respondedor acepta | La gente rechaza ofertas injustas (irracionales pero comunes) |
| **Juego de bienes públicos** | Contribuya a un grupo compartido o viaje gratis | Todos viajan gratis | Tragedia de los comunes; necesidad de hacer cumplir la ley |
---

## Tipos de juegos
### Por tiempo
| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Simultáneo** | Los jugadores se mueven al mismo tiempo (o sin conocer los movimientos de los demás) | Piedra, papel o tijera; subastas sobre sobre cerrado |
| **Secuencial** | Los jugadores se mueven uno tras otro; los jugadores posteriores observan los movimientos anteriores | Ajedrez; decisiones de entrada al mercado |
| **Repetido** | El mismo juego jugado varias veces | El repetido dilema del prisionero; competencia empresarial en curso |
### Por información
| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Información perfecta** | Todos los jugadores conocen todos los movimientos anteriores | Ajedrez; damas |
| **Información imperfecta** | Algunos movimientos están ocultos | Póker; competencia empresarial |
| **Información completa** | Todos los jugadores conocen todos los pagos y estrategias | La mayoría de los juegos de libros de texto |
| **Información incompleta** | Se desconocen algunos pagos o tipos | Subastas; negociaciones |
---

## Conceptos de solución
### Equilibrio de Nash
| Aspecto | Descripción |
|--------|-------------|
| **Definición** | Ningún jugador puede mejorar sus ganancias cambiando su estrategia por sí solo |
| **Cómo encontrarlo** | Para cada jugador, encuentre la mejor respuesta a las estrategias de los demás; donde todos se cruzan es el equilibrio de Nash |
| **Existencia** | Todo juego finito tiene al menos un equilibrio de Nash (posiblemente en estrategias mixtas) |
| **Singularidad** | Los juegos pueden tener múltiples equilibrios de Nash; surgen problemas de coordinación |
| **Limitación** | El equilibrio de Nash no indica qué equilibrio se seleccionará; no tiene en cuenta la justicia |
### Equilibrio de estrategia dominante
| Paso | Descripción |
|------|-------------|
| **1. Identificar estrategias** | Lista todas las estrategias disponibles para cada jugador |
| **2. Encuentre estrategias dominantes** | Una estrategia que es mejor independientemente de lo que hagan los demás |
| **3. Si todos los jugadores tienen uno** | La combinación es el equilibrio de la estrategia dominante |
| **4. Si no** | Utilice eliminación iterada de estrategias dominadas o equilibrio de Nash |
### Inducción hacia atrás (juegos secuenciales)
| Paso | Descripción |
|------|-------------|
| **1. Dibuja el árbol del juego** | Nodos = puntos de decisión; ramas = acciones |
| **2. Empezar por el final** | Identificar la elección óptima del último jugador en cada nodo terminal |
| **3. Trabajar al revés** | En cada nodo anterior, elija la acción que conduzca al mejor resultado |
| **4. Resultado** | Equilibrio perfecto en subjuegos: estrategia óptima en cada punto de decisión |
---

## Conceptos avanzados
### Estrategias mixtas
| Concepto | Descripción | Ejemplo |
|---------|-------------|---------|
| **Estrategia mixta** | Aleatorización entre acciones según probabilidades | Piedra, papel y tijera: juega cada uno con 1/3 de probabilidad |
| **¿Por qué aleatorizar?** | Evita que los oponentes predigan tu movimiento | Tiros de penalti en el fútbol; auditorías fiscales |
| **Equilibrio de Nash de estrategia mixta** | Cada jugador es indiferente entre sus estrategias puras | Ningún jugador puede explotar al otro |
### Juegos repetidos y teorema popular
| Concepto | Descripción |
|---------|-------------|
| **Finitamente repetido** | La inducción hacia atrás deshace la cooperación; igual que el juego de una sola vez | La deserción en la última ronda se propaga hacia atrás |
| **Infinitamente repetido** | La cooperación puede mantenerse mediante amenazas de futuros castigos | ojo por ojo; estrategias desencadenantes sombrías |
| **Teorema popular** | Cualquier pago individualmente racional puede ser un equilibrio de Nash en un juego infinitamente repetido | La cooperación es posible si el futuro importa lo suficiente |
| **Factor de descuento** | Cuánto valoran los jugadores los pagos futuros; mayor = más cooperación | Los jugadores pacientes cooperan más |
### Diseño de mecanismos (teoría de juegos inversos)
| Concepto | Descripción |
|---------|-------------|
| **Objetivo** | Diseñar las reglas de un juego para lograr el resultado deseado |
| **Aplicaciones** | Subastas; sistemas de votación; diseño de contratos; diseño de mercado |
| **Principio de revelación** | Cualquier resultado que se pueda lograr mediante cualquier mecanismo puede lograrse mediante un mecanismo directo veraz |
| **Ejemplo** | Subasta de Vickrey (oferta sellada de segundo precio): ofertar su verdadero valor es una estrategia dominante |
---

## Aplicaciones
### Negocio
| Solicitud | Concepto de teoría de juegos | Perspectiva |
|-------------|-------------------|---------|
| **Competencia de precios** | El dilema del prisionero | Las guerras de precios perjudican a ambas empresas; colusión tácita en juegos repetidos |
| **Entrada al mercado** | Juego secuencial; compromiso | La amenaza del actual presidente de luchar contra la entrada sólo es creíble si han invertido en capacidad |
| **Subastas** | Diseño de mecanismos | Las subastas de segundo precio obtienen valores verdaderos; subastas de espectro recaudan miles de millones |
| **Negociación** | Juego de negociación; Equilibrio de Nash | Dividir el excedente; ventaja del primero en moverse en juegos de ultimátum |
| **Señalización** | El modelo educativo de Spence | Las señales caras son creíbles porque los tipos de baja calidad no pueden permitírselo |
### Relaciones Internacionales
| Solicitud | Concepto de teoría de juegos | Perspectiva |
|-------------|-------------------|---------|
| **Carreras armamentistas** | El dilema del prisionero | Sería mejor para ambas partes desarmarse, pero no pueden confiar el uno en el otro |
| **Guerras comerciales** | Juego repetido | Ojo por ojo: cooperar hasta que los demás fallen, luego tomar represalias |
| **Acuerdos climáticos** | Juego de bienes públicos | El parasitismo es racional; mecanismos de aplicación necesarios |
| **Disuasión** | Pollo; compromiso creíble | La destrucción mutua asegurada es un equilibrio de Nash |
---

## Resumen
La teoría de juegos estudia interacciones estratégicas en las que el resultado depende de las acciones de los demás. El equilibrio de Nash (donde ningún jugador se beneficia solo con cambiar de estrategia) es el concepto central de solución. Juegos clásicos como el dilema del prisionero muestran que las decisiones individuales racionales pueden producir malos resultados colectivos. Los juegos secuenciales se resuelven por inducción hacia atrás. Los juegos repetidos pueden sostener la cooperación a través de la amenaza de un castigo futuro. Las estrategias mixtas implican la aleatorización para seguir siendo impredecible. El diseño de mecanismos invierte la cuestión: en lugar de predecir resultados, diseña reglas para lograr los resultados deseados (como en las subastas). Las aplicaciones abarcan negocios (precios, entrada, subastas), política (votación, tratados), biología (estrategias evolutivas estables) y la vida cotidiana. La lección fundamental es que la estrategia no se trata sólo de lo que uno hace: se trata de anticipar lo que harán los demás, sabiendo que ellos están haciendo lo mismo.