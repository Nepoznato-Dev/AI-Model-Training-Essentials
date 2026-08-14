---
# Metadata
title: "Scratch"
description: "Comprehensive reference for the Scratch programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
tags: [scratch, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "29 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Gratter
Scratch est un langage de programmation visuel basé sur des blocs développé par le MIT Media Lab et lancé pour la première fois en 2007. Au lieu d'écrire du code textuel, les utilisateurs assemblent des blocs de couleur pour créer des programmes. Scratch est conçu spécifiquement pour les enfants âgés de 8 à 16 ans (bien que les apprenants de tous âges l'utilisent) pour enseigner les concepts fondamentaux de la programmation (boucles, conditions, variables, événements et fonctions) sans la barrière des erreurs de syntaxe.
Scratch est le langage de programmation d'introduction le plus utilisé au monde, avec plus de 100 millions d'utilisateurs enregistrés et une disponibilité dans plus de 70 langues. Il fonctionne dans un navigateur Web et est gratuit.
---

## Pourquoi les rayures sont importantes
- **Meilleure introduction à la programmation** : supprime entièrement les barrières syntaxiques. Les concepts sont enseignés par manipulation visuelle.
- **Pensée informatique** : enseigne la décomposition, la reconnaissance de formes, l'abstraction et la conception d'algorithmes.
- **Axé sur la créativité** : les enfants créent des jeux, des animations, des histoires et de la musique, apprenant ainsi la programmation en tant que sous-produit de la création de choses qui les intéressent.
- **Portée mondiale** : utilisé dans les écoles du monde entier. Disponible dans plus de 70 langues. Gratuit et basé sur un navigateur.
- **Communauté** : la communauté en ligne Scratch enseigne le partage, le remixage et l'apprentissage collaboratif.
## Les compromis
| Limitation | Détails | Solution de contournement typique |
|-----------|---------|-------------------|
| **Pas un "vrai" langage de programmation** | Impossible de créer des logiciels, des API ou des systèmes de production | Transition vers Python, JavaScript ou les langages textuels |
| **Capacités limitées** | Pas d'E/S de fichiers, de mise en réseau ou de structures de données avancées | Utilisation pour l'apprentissage ; passer aux langages de texte pour de vrais projets |
| **Performances** | Interprété, lent pour les projets complexes | Non conçu pour les travaux critiques en termes de performances |
| **Perception de l'âge** | Souvent considéré comme « réservé aux enfants » | Scratch est un outil d'apprentissage, pas un langage professionnel |
---

## Comment fonctionne Scratch
Les programmes Scratch (appelés « projets ») sont constitués de **sprites** (personnages/objets) qui répondent à des **blocs** assemblés dans des scripts.
### Concepts de base (enseignés via des blocs)
| Concepts | Catégorie de blocs à gratter | Exemple |
|---------|------------|---------|
| **Séquences** | Mouvement, regards | "Déplacez-vous de 10 pas" puis "Dites bonjour" |
| **Boucles** | Contrôle (jaune) | "Répéter 10", "Pour toujours", "Répéter jusqu'à" |
| **Conditions** | Contrôle (jaune) | "Si... alors", "Si... alors... sinon" |
| **Variables** | Variables (orange) | "Mettre le score à 0", "Modifier le score de 1" |
| **Événements** | Événements (jaune) | "Lorsque le drapeau vert est cliqué", "Lorsque la touche est enfoncée" |
| **Fonctions** | Mes blocs (personnalisés) | Définir des séquences de blocs réutilisables |
| **Listes (tableaux)** | Variables (orange) | "Ajouter à la liste", "Élément de la liste" |
| **Diffusion** | Événements | Envoyer des messages entre sprites |
### Exemple : Logique de jeu simple
```
When green flag clicked:
  Set [score] to 0
  Forever:
    If <touching [enemy]?> then:
      Change [score] by -1
      Play sound [ouch]
    If <touching [coin]?> then:
      Change [score] by 1
      Go to random position
```

---

## Syntaxe et modèles avancés
### Catégories de blocs en détail
Scratch 3.0 organise les blocs en catégories codées par couleur :
| Catégorie | Couleur | Types de blocs |
|--------------|--------|-------------|
| **Mouvement** | Bleu | déplacer, tourner, aller à, glisser, pointer, changer x/y |
| **On dirait** | Violet | dire, réfléchir, changer de costume, changer de taille, afficher/masquer |
| **Son** | Rose | jouer du son, arrêter les sons, changer le volume, changer la hauteur |
| **Événements** | Jaune | lorsque le drapeau est cliqué, lorsque la touche est enfoncée, lorsque le sprite est cliqué, diffusion |
| **Contrôle** | Or | attendre, répéter, pour toujours, si, si-sinon, répéter jusqu'à, arrêter |
| **Détection** | Bleu clair | toucher, touche enfoncée, souris, distance, question/réponse, minuterie |
| **Opérateurs** | Vert | opérations mathématiques, opérations de texte, comparaison et/ou/non, aléatoire |
| **Variables** | Orange | définir/modifier une variable, opérations de liste |
| **Mes blocs** | Rouge foncé | définitions de blocs personnalisés (fonctions) |
### Modèles de blocs avancés
```
// Pattern: Timer-based movement (smooth animation)
When green flag clicked:
  Set [speed] to 5
  Forever:
    Change x by (speed)
    If <(x position) > 200> then
      Set [speed] to ((speed) * -1)
    If <(x position) < -200> then
      Set [speed] to ((speed) * -1)

// Pattern: State machine using variables
When green flag clicked:
  Set [game_state] to [menu]
  Forever:
    If <(game_state) = [menu]> then
      Show
      Go to x: 0 y: 0
    If <(game_state) = [playing]> then
      Hide
    If <(game_state) = [game_over]> then
      Say [Game Over!] for 2 secs

// Pattern: Object-oriented sprite (each sprite manages its own state)
When green flag clicked:
  Set [hp] to 100
  Set [max_hp] to 100
  Set [is_alive] to true
  Forever:
    If <(is_alive) = true> then
      If <touching [enemy]?> then
        Change [hp] by -10
        If <(hp) < 1> then
          Set [is_alive] to false
          Broadcast [player_dead]
```

### Blocs personnalisés (fonctions)
```
// Define a custom block with parameters
Define: Jump (height) times (count)
  Repeat (count):
    Change y by (height)
    Wait 0.2 seconds
    Change y by ((height) * -1)
    Wait 0.2 seconds

// Usage:
When space key pressed:
  Jump height: 50 times: 3

// Custom block with "run without screen refresh" (optimization)
Define: Draw fractal (depth) (size)
  Run without screen refresh: true
  If <(depth) = 0> then
    Move (size) steps
  Else:
    Draw fractal depth: ((depth) - 1) size: ((size) / 2)
    Turn right 60 degrees
    Draw fractal depth: ((depth) - 1) size: ((size) / 2)
    Turn left 120 degrees
    Draw fractal depth: ((depth) - 1) size: ((size) / 2)
    Turn right 60 degrees
```

### Opérations de liste (tableaux)
```
// Creating and using lists
When green flag clicked:
  Delete all of [scores]
  Add [100] to [scores]
  Add [85] to [scores]
  Add [92] to [scores]
  Add [78] to [scores]
  
  // Access items (1-indexed)
  Set [total] to 0
  Set [i] to 1
  Repeat (length of [scores]):
    Change [total] by (item (i) of [scores])
    Change [i] by 1
  
  Set [average] to ((total) / (length of [scores]))
  Say (join [Average: ] (average)) for 2 secs

// Sorting a list (bubble sort)
Define: Sort List
  Set [n] to (length of [scores])
  Repeat (n)
    Set [i] to 1
    Repeat ((n) - 1)
      If <(item (i) of [scores]) > (item ((i) + 1) of [scores])> then
        // Swap
        Set [temp] to (item (i) of [scores])
        Replace item (i) of [scores] with (item ((i) + 1) of [scores])
        Replace item ((i) + 1) of [scores] with (temp)
      Change [i] by 1
```

### Diffusion (Communication Inter-Sprite)
```
// Sprite 1 (Player):
When space key pressed:
  Broadcast [fire_bullet]

// Sprite 2 (Bullet):
When I receive [fire_bullet]:
  Go to [Player]
  Show
  Repeat 50:
    Change y by 10
  Hide

// Sprite 3 (Enemy):
When I receive [fire_bullet]:
  If <touching [Bullet]?> then
    Change [hp] by -25
    If <(hp) < 1> then
      Broadcast [enemy_destroyed]
      Hide
```

---

## Architecture et conception de systèmes
### Conception basée sur les événements
Scratch utilise une architecture basée sur les événements. Chaque script commence par un bloc d'événement (bloc chapeau) et s'exécute en réponse à cet événement.
```
Event Types:
+-------------------------------------------+
| when [green flag] clicked    (startup)     |
| when [space] key pressed     (keyboard)    |
| when this sprite clicked     (mouse)       |
| when [backdrop] switches to  (stage event) |
| when [loudness] > [10]       (sound)       |
| when I receive [message]     (broadcast)   |
| when video motion > [10]     (camera)      |
+-------------------------------------------+
```

### Structure du projet
```
scratch-project/
├── project.sb3              * Saved project file (ZIP format)
├── sprites/
│   ├── Player/              * Player sprite
│   │   ├── costumes/        * Costume images
│   │   └── sounds/          * Sound files
│   ├── Enemy/
│   │   ├── costumes/
│   │   └── sounds/
│   └── Bullet/
├── stage/
│   ├── backdrops/           * Background images
│   └── sounds/              * Stage sounds
└── README.md
```

### Système de clonage (création d'objets)
```
// Creating clones (like creating object instances)
When green flag clicked:
  Forever:
    Wait 1 seconds
    Create clone of [Enemy]

When I start as a clone:
  Go to random position
  Show
  Set [hp] to 3
  Forever:
    Change y by -3
    If <(y position) < -170> then
      Delete this clone
    If <touching [Bullet]?> then
      Change [hp] by -1
      If <(hp) < 1> then
        Change [score] by 10
        Delete this clone
```

---

## Configuration du projet et système de construction
### Extensions à gratter
Scratch prend en charge les extensions officielles et communautaires qui ajoutent des fonctionnalités :
| Rallonge | Objectif |
|-----------|---------|
| **Stylo** | Dessinez des lignes et des formes sur scène |
| **Détection vidéo** | Utiliser la webcam pour la détection de mouvement |
| **Texte en parole** | Convertir du texte en audio parlé |
| **Traduire** | Traduire du texte entre les langues |
| **Makey Makey** | Connecter des objets physiques en entrée |
| **micro:bit** | Connectez le matériel BBC micro:bit |
| **Tempêtes d'esprit LEGO** | Contrôler les robots LEGO |
| **Musique** | Jouer des notes et des instruments de musique |
### Format de fichier de travail
```
Scratch 3.0 projects (.sb3) are ZIP archives containing:
├── project.json             * All scripts, sprites, and metadata
├── [md5hash].svg           * Costume images (SVG or PNG)
├── [md5hash].png           * Additional costumes
└── [md5hash].wav           * Sound files

The project.json contains:
{
  "targets": [
    {
      "isStage": true,
      "name": "Stage",
      "costumes": [...],
      "sounds": [...],
      "blocks": {...}
    },
    {
      "isStage": false,
      "name": "Sprite1",
      "position": {"x": 0, "y": 0},
      "blocks": {...}
    }
  ],
  "monitors": [...],
  "meta": {"semver": "3.0.0"}
}
```

### Éditeur hors ligne
```
Scratch Desktop (offline editor) available for:
- Windows 10+ (Microsoft Store or direct download)
- macOS 10.13+
- ChromeOS

Installation:
1. Download from https://scratch.mit.edu/download
2. Install and run — no internet required
3. Projects save as .sb3 files locally
```

---

## Tests et débogage
### Outils de débogage intégrés
Scratch fournit plusieurs outils intégrés pour le débogage des projets :
| Outil | Comment utiliser |
|------|-----------|
| **Mode tortue** | Cliquez avec le bouton droit sur un sprite et sélectionnez "afficher le débogage" pour voir les coordonnées |
| **Moniteurs variables** | Cliquez avec le bouton droit sur une variable et sélectionnez « Afficher » pour voir sa valeur en temps réel |
| **Liste des moniteurs** | Afficher le contenu de la liste en affichage normal, en ligne ou en colonne |
| **Mode turbo** | Maintenez Shift tout en cliquant sur le drapeau vert pour une exécution plus rapide |
| **Mode en une seule étape** | Cliquez avec le bouton droit sur le drapeau vert pour "une seule étape" (ralentit l'exécution) |
### Modèles de débogage
```
// Debug: Display variable values on sprite
When green flag clicked:
  Forever:
    Say (join [Score: ] (score))

// Debug: Visual boundary checking
When green flag clicked:
  Forever:
    If <(x position) > 240> then
      Say [TOO FAR RIGHT!] for 0.5 secs
      Set x to 240
    If <(x position) < -240> then
      Say [TOO FAR LEFT!] for 0.5 secs
      Set x to -240

// Debug: Frame counter
When green flag clicked:
  Set [frames] to 0
  Forever:
    Change [frames] by 1
    If <(frames) mod 30 = 0> then
      Say (join [FPS: ] ((frames) / (timer))) for 0.1 secs
```

### Problèmes courants
| Problème | Parce que | Solutions |
|---------|-------|----------|
| Sprite ne répond pas | Aucun bloc de chapeau d'événement | Ajouter "Lorsque le drapeau vert est cliqué" ou un autre événement |
| Le clone ne fonctionne pas | Clone créé mais non affiché | Ajouter le bloc "Afficher" après "Quand je démarre en tant que clone" |
| Variable partagée entre les sprites | Confusion des variables globales et locales | Utilisez l'option "Pour ce sprite uniquement" |
| Diffusion non reçue | Nom du message incorrect | Vérifiez que les noms de diffusion et de réception correspondent exactement |
| Gel de boucle infinie | "Pour toujours" sans attente | Ajoutez de petits blocs « Attendez » dans des boucles serrées |
---

## Interopérabilité
### Extensions matérielles
Scratch peut se connecter au matériel physique via des extensions :
```
Supported Hardware:
├── micro:bit
│   ├── Accelerometer/gyroscope input
│   ├── LED matrix display output
│   ├── Button input
│   └── Radio communication
├── LEGO Education
│   ├── SPIKE Prime / Essential
│   ├── EV3 (older)
│   └── Motors and sensors
├── Makey Makey
│   ├── Capacitive touch input
│   ├── Any conductive object as button
│   └── USB connection (no drivers needed)
├── Arduino (via extensions)
│   ├── GPIO pin control
│   ├── Sensor readings
│   └── Motor control
└── Camera / Webcam
    ├── Video sensing (motion detection)
    └── Face detection (via extensions)
```

### API des extensions Scratch (extensions personnalisées)
```javascript
// Custom Scratch extension (JavaScript)
class MyExtension {
  getInfo() {
    return {
      id: 'myExtension',
      name: 'My Extension',
      blocks: [
        {
          opcode: 'greet',
          blockType: Scratch.BlockType.REPORTER,
          text: 'greet [NAME]',
          arguments: {
            NAME: { type: Scratch.ArgumentType.STRING, defaultValue: 'World' }
          }
        },
        {
          opcode: 'addNumbers',
          blockType: Scratch.BlockType.REPORTER,
          text: '[A] + [B]',
          arguments: {
            A: { type: Scratch.ArgumentType.NUMBER, defaultValue: 1 },
            B: { type: Scratch.ArgumentType.NUMBER, defaultValue: 2 }
          }
        }
      ]
    };
  }
  greet(args) { return 'Hello, ' + args.NAME + '!'; }
  addNumbers(args) { return Number(args.A) + Number(args.B); }
}
Scratch.extensions.register(new MyExtension());
```
---

## Modèles de conception
### Modèle 1 : Mouvement de plateforme
```
When green flag clicked:
  Set [gravity] to -1
  Set [velocity_y] to 0
  Set [speed] to 5
  Set [is_jumping] to false
  Forever:
    // Horizontal movement
    If <key [right arrow] pressed?> then
      Change x by (speed)
    If <key [left arrow] pressed?> then
      Change x by ((speed) * -1)
    // Jumping
    If <key [space] pressed?> then
      If <(is_jumping) = false> then
        Set [velocity_y] to 12
        Set [is_jumping] to true
    // Gravity
    Change [velocity_y] by (gravity)
    Change y by (velocity_y)
    // Ground collision
    If <(y position) < -100> then
      Set y to -100
      Set [velocity_y] to 0
      Set [is_jumping] to false
```

### Modèle 2 : arrière-plan défilant
```
// Background sprite scrolls left to create side-scrolling effect
When green flag clicked:
  Forever:
    Change x by -5
    If <(x position) < -240> then
      Set x to 240

// Or use two copies for seamless scrolling
When I start as a clone:
  Forever:
    Change x by -5
    If <(x position) < -480> then
      Change x by 960
```

### Modèle 3 : Suivi des sprites (Chase AI)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### Modèle 4 : Système d'inventaire avec listes
```
When green flag clicked:
  Delete all of [inventory]
  Add [Sword] to [inventory]
  Add [Shield] to [inventory]
  Add [Potion] to [inventory]

When key [i] pressed:
  // Display inventory
  Set [display] to []
  Set [idx] to 1
  Repeat (length of [inventory]):
    Set [display] to (join (display) (join (item (idx) of [inventory]) [
]))
    Change [idx] by 1
  Say (display) for 3 secs

When key [1] pressed:
  // Use first item
  If <(length of [inventory]) > 0> then
    Set [used_item] to (item 1 of [inventory])
    Delete 1 of [inventory]
    Say (join [Used: ] (used_item)) for 1 secs
```

### Modèle 5 : Système de particules avec clones
```
// Create particles on click
When this sprite clicked:
  Repeat 10:
    Create clone of [Particle]

// Each particle moves randomly and fades
When I start as a clone:
  Go to [mouse-pointer]
  Point in direction (pick random 0 to 360)
  Set [size] to (pick random 20 to 50)
  Set [ghost] to 0
  Show
  Repeat 20:
    Move 5 steps
    Change [ghost] by 5
  Hide
  Delete this clone
```

---

## Performances et optimisation
### Optimisation des sprites
| Techniques | Impact | Descriptif |
|---------------|--------|-------------|
| **Réduire les clones** | Élevé | Chaque clone consomme de la mémoire ; supprimer une fois terminé |
| **Réduire les costumes** | Moyen | Moins de changements de costumes signifie moins de frais de rendu |
| **Utilisez "Exécuter sans actualisation de l'écran"** | Élevé | Les blocs personnalisés sans actualisation de l'écran s'exécutent plus rapidement |
| **Limiter les blocs « dire »** | Moyen | Les bulles provoquent une surcharge de rendu |
| **Évitez "pour toujours" dans chaque sprite** | Moyen | Utilisez des diffusions et des événements au lieu de sondages constants |
### Gestion des clones
```
// BAD: Creating clones without cleanup
When green flag clicked:
  Forever:
    Create clone of [Enemy]
    Wait 0.1 secs
    // Clones pile up and slow everything down

// GOOD: Limit active clones
When green flag clicked:
  Set [max_enemies] to 10
  Forever:
    If <(enemy_count) < (max_enemies)> then
      Create clone of [Enemy]
      Change [enemy_count] by 1
    Wait 1 secs

When I start as a clone:
  // ... enemy behaviour ...
  // When done:
  Change [enemy_count] by -1
  Delete this clone
```

### Liste de contrôle d'optimisation
| Techniques | Impact | Descriptif |
|---------------|--------|-------------|
| **Exécuter sans actualisation de l'écran** | Très élevé | Les blocs personnalisés ignorent le rendu pour plus de vitesse |
| **Réduire les clones actifs** | Élevé | Supprimez les clones dès qu'ils ne sont plus nécessaires |
| **Utilisez les diffusions avec parcimonie** | Moyen | Trop de diffusions par image provoquent un décalage |
| **Simplifier les costumes** | Moyen | Les images plus petites s'affichent plus rapidement |
| **Réduire les opérations de liste** | Moyen | Évitez de numériser de grandes listes à chaque image |
| **Utilisez les blocs "attendre"** | Faible | Empêcher la monopolisation du processeur dans des boucles éternelles |
---

## Déploiement et utilisation dans le monde réel
### Partage de projets
```
Deployment Options:
├── Scratch Community (online)
│   ├── Upload to scratch.mit.edu
│   ├── Share with community
│   └── Allow remixing by others
├── Local sharing
│   ├── Save as .sb3 file
│   ├── Share via email/USB/cloud
│   └── Open in Scratch Desktop or web editor
├── Embedding
│   ├── Embed on websites via iframe
│   └── <iframe src="https://scratch.mit.edu/projects/embed/PROJECT_ID">
└── Standalone apps (via third-party tools)
    ├── TurboWarp (desktop packaging)
    ├── Electron-based wrappers
    └── HTML5 export tools
```

### Utilisation éducative dans le monde réel
| Contexte | Comment Scratch est utilisé | Échelle |
|---------|---------|-------|
| **Écoles K-12** | Introduction à la programmation dans les cours CS | Utilisé dans plus de 190 pays |
| **Clubs de codage** | Ateliers Scratch Club / CoderDojo | Plus de 3000 clubs dans le monde |
| **Bibliothèques** | Programmes de programmation parascolaire | Systèmes de bibliothèques publiques |
| **Enseignement à la maison** | Formation à la programmation à votre rythme | Des millions d'apprenants à domicile |
| **Université CS0** | Cours d'introduction à l'informatique non majeurs | Programmes de transition universitaires |
| **Accessibilité** | Enseigner la programmation aux malvoyants | Prise en charge du lecteur d'écran |
| **Thérapie** | Développement cognitif et moteur | Ergothérapie |
### Scratch dans la recherche en éducation
Des recherches ont montré que Scratch enseigne efficacement :
- **Pensée séquentielle** : diviser les problèmes en étapes ordonnées
- **Compétences en débogage** : recherche et correction des erreurs de logique
- **Expression créative** : combiner art, musique et programmation
- **Collaboration** : Remixer et développer les projets des autres
- **Persistance** : Itérer sur les projets pour les améliorer
---

## Transition à partir de zéro
Après avoir appris Scratch, les prochaines étapes typiques incluent :
| Langue suivante | Pourquoi |
|--------------|----------|
| **Python** | Transition la plus naturelle — syntaxe lisible, concepts logiques similaires |
| **JavaScript** | Si vous êtes intéressé par le Web/les jeux — retour visuel immédiat |
| **Lua (via Roblox/Love2D)** | Si vous êtes intéressé par le développement de jeux |
| **Inventeur d'applications** | Blocs visuels pour les applications Android (même lignée MIT) |
| **En bloc** | Bibliothèque de programmation visuelle de Google (concepts similaires) |
### Cartographie conceptuelle : Scratch vers Python
| Concept de rayures | Équivalent Python |
|----------------|-------------------|
| `set [x] to 0`| `x = 0`|
| `change [x] by 1`| `x += 1`|
| `repeat 10`| `for i in range(10):`|
| `forever`| `while True:`|
| `if ... then`| `if ...:`|
| `broadcast [msg]`| Système d'appel de fonction ou d'événement |
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`| `list[0]`(indexé 0 !) |
| `length of [list]`| `len(list)`|
---

## Quand utiliser Scratch
| Scénario | Pourquoi gratter | Meilleure alternative |
|----------|-----------|-------------------|
| Apprendre aux enfants (8-16 ans) à coder | Conçu spécifiquement pour cela | — |
| Présentation de la pensée informatique | Visuel, aucune erreur de syntaxe | — |
| Ateliers scolaires / clubs de codage | Gratuit, basé sur un navigateur, aucune configuration | — |
| Prototypage visuel d'idées de jeux | Itération rapide | — |
| Développement professionnel | Pas conçu pour ça | Python, JavaScript, n'importe quel langage de texte |
| Formation CS de niveau universitaire | Trop simple | Python, Java, C |
---

## Questions et réponses synthétiques
**Q1 : Scratch est-il vraiment un langage de programmation ?**
R1 : Oui, Scratch est un véritable langage de programmation, mais il est visuel plutôt que textuel. Il prend en charge tous les concepts fondamentaux de programmation : variables, boucles, conditions, fonctions (blocs personnalisés), listes et programmation événementielle. La différence est que vous faites glisser et déposez des blocs au lieu de taper du code. Cela élimine les erreurs de syntaxe et rend la programmation accessible aux jeunes apprenants.
**Q2 : Comment créer des fonctions personnalisées (blocs personnalisés) dans Scratch ?**
A2 : Allez dans la catégorie « Mes blocs » et cliquez sur « Créer un bloc ». Donnez-lui un nom, ajoutez des paramètres si nécessaire, puis définissez son comportement en ajoutant des blocs en dessous. Les blocs personnalisés peuvent accepter des entrées (nombres, chaînes, booléens) et appeler d'autres blocs personnalisés. Cela permet une programmation modulaire et une réutilisation du code.
**Q3 : Quelle est la meilleure façon de gérer une logique de jeu complexe dans Scratch ?**
A3 : utilisez des blocs personnalisés pour organiser la logique, diffusez des messages pour la coordination des événements entre les sprites et utilisez des listes pour stocker l'état du jeu (scores, niveaux, inventaire). Pour l’IA complexe, utilisez des machines à états finis avec des variables suivant l’état actuel. Clonez des sprites pour plusieurs ennemis et utilisez "quand je démarre en tant que clone" pour donner à chaque comportement indépendant.
**Q4 : Comment puis-je partager des données entre sprites dans Scratch ?**
A4 : Utilisez des variables globales (créées sans "pour ce sprite uniquement") pour les données partagées comme le score ou l'état du jeu. Utilisez des messages diffusés pour déclencher des événements sur les sprites. Pour une communication plus complexe, utilisez des listes comme structures de données partagées. Chaque sprite peut lire et modifier des variables globales et des listes, permettant la coordination.
**Q5 : Quelles sont les techniques avancées de Scratch ?**
A5 : Utilisez des blocs de stylos pour dessiner et créer des effets visuels. Implémentez le raycasting pour les graphiques de type 3D. Utilisez des variables cloud pour les jeux multijoueurs (nécessite le statut Scratcher). Créez une génération procédurale avec des nombres et des listes aléatoires. Utilisez des blocs personnalisés avec des paramètres pour des algorithmes réutilisables. Expérimentez la détection vidéo et la manipulation du son pour des projets interactifs.
---

## Chaîne de pensée
### Problème 1 : Créer un jeu de plateforme
**Étape 1 : Comprendre le problème**
Nous devons créer un jeu de plateforme dans lequel un personnage peut se déplacer de gauche à droite, sauter, éviter les obstacles et collecter des objets.
**Étape 2 : Identifiez l'approche**
- Utiliser la simulation gravitationnelle avec une variable "en baisse"
- Détecter le sol/collision en utilisant la couleur ou le toucher des sprites
- Stocker les données de niveau dans des listes
- Utilisez des blocs personnalisés pour la logique de saut et de mouvement
**Étape 3 : Mettre en œuvre la solution**```scratch
// Gravity and movement
when green flag clicked
forever
  change y by (y velocity)
  if touching color [brown] then
    set [y velocity v] to [0]
    set [is jumping v] to [0]
  else
    change [y velocity v] by (-1)
  end
  
  if key [right arrow v] pressed then
    change x by (5)
  end
  if key [left arrow v] pressed then
    change x by (-5)
  end
  if key [space v] pressed and not <is jumping = [1]> then
    set [y velocity v] to [10]
    set [is jumping v] to [1]
  end
end
```

**Étape 4 : Vérifier et optimiser**
Testez le saut sur différentes plateformes. Ajustez la gravité et la hauteur de saut pour une bonne sensation de jeu. Ajoutez des animations pour courir et sauter. Implémentez des points de contrôle à l’aide de messages diffusés.
---

### Problème 2 : Créer un jeu de quiz avec suivi des scores
**Étape 1 : Comprendre le problème**
Créez un jeu de quiz qui pose des questions, vérifie les réponses et suit le score du joueur.
**Étape 2 : Identifiez l'approche**
- Stocker les questions et réponses dans des listes parallèles
- Utilisez un compteur de questions pour suivre les progrès
- Utilisez des blocs "demander et attendre" pour la saisie
- Comparez les réponses et mettez à jour le score
**Étape 3 : Mettre en œuvre la solution**```scratch
when green flag clicked
set [score v] to [0]
set [question number v] to [1]

repeat (length of [questions v])
  ask (item (question number) of [questions v]) and wait
  if <(answer) = (item (question number) of [answers v])> then
    change [score v] by (1)
    say [Correct!] for (2) secs
  else
    say [Wrong!] for (2) secs
  end
  change [question number v] by (1)
end

say (join [Final score: ] join (score) [/5]) for (4) secs
```

**Étape 4 : Vérifier et optimiser**
Testez avec diverses réponses, y compris des cas extrêmes. Ajoutez des commentaires pour les mauvaises réponses. Implémentez une option de nouvelle tentative. Ajoutez des effets sonores et un retour visuel pour les réponses correctes/mauvaises.
---

### Problème 3 : Dessiner des arbres fractaux avec le stylo
**Étape 1 : Comprendre le problème**
Créez un arbre fractal récursif à l'aide de l'extension du stylet.
**Étape 2 : Identifiez l'approche**
- Utiliser la récursivité pour dessiner des branches
- Chaque branche se divise en deux branches plus petites
- Utilisez des angles aléatoires pour une variation naturelle
- Suivre la longueur des branches et diminuer à chaque niveau de récursion
**Étape 3 : Mettre en œuvre la solution**```scratch
define draw branch (length)
pen down
glide (1) secs to (x:(x position) + (length * cos of direction)) (y:(y position) + (length * sin of direction))
pen up

if <(length) > [5]> then
  turn right (pick random (10) to (45))
  draw branch (length * 0.7)
  turn left (pick random (20) to (90))
  draw branch (length * 0.7)
end

when green flag clicked
erase all
goto x:(0) y:(-150)
point in direction (90)
draw branch (100)
```

**Étape 4 : Vérifier et optimiser**
Ajustez le seuil de longueur des branches et les plages d’angle pour les arbres esthétiques. Ajoutez des feuilles aux extrémités des branches en utilisant des changements de couleur. Implémentez différents styles d’arborescence. Enregistrez les dessins sous forme d'images.
---

## Résumé
Scratch n'est pas un langage de programmation au sens traditionnel du terme : c'est un environnement d'apprentissage. Son génie est d'éliminer toute barrière entre un enfant et la joie de créer quelque chose d'interactif. En se concentrant sur les concepts plutôt que sur la syntaxe, Scratch enseigne les principes fondamentaux de la programmation transférables dans n'importe quel langage. Pour initier la programmation aux jeunes apprenants, Scratch est la référence.