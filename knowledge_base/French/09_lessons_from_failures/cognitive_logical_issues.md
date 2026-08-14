---
# Metadata
title: "Cognitive Biases and Logical Fallacies"
description: "Reasoning errors and cognitive biases"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cognitive, logical, issues, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "27 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Biais cognitifs et erreurs logiques
Ce document consolide les biais cognitifs, les erreurs logiques et les erreurs de raisonnement qui affectent à la fois la prise de décision humaine et les résultats du système d'IA.
---

## Biais cognitifs
Les biais cognitifs sont des modèles systématiques d’écart par rapport à la rationalité dans le jugement et la prise de décision. Dans le développement de logiciels et les systèmes d’IA, cela peut conduire à de mauvaises décisions de conception, à des exigences erronées et à un comportement biaisé du modèle.
### Biais de confirmation
**Qu'est-ce que c'est :** La tendance à rechercher, interpréter et rappeler des informations d'une manière qui confirme des croyances préexistantes.
**Mauvais exemple de développement :**```python
# Developer believes their algorithm is O(n log n)
def analyze_complexity(code):
    # Only looks for evidence supporting O(n log n)
    sees_divide_and_conquer = True
    sees_recursion = True
    
    # Ignores contradictory evidence
    nested_loop_present = True  # Actually makes it O(n²)
    redundant_computation = True  # Adds extra factor
    
    return "O(n log n)"  # Wrong conclusion
```

**Dans les révisions de code :**```markdown
Developer A (senior): "This looks good, nice work!"
Developer B (junior): "This has several potential issues..."

Team accepts Developer A's review without scrutiny but questions Developer B's feedback excessively.
```

**Atténuation :**
- Rechercher activement des preuves infirmantes
- Utiliser les revues de code aveugles
- Encourager les opinions dissidentes
- Documenter explicitement les hypothèses
### Biais d'ancrage
**Qu'est-ce que c'est :** Se fier trop à la première information rencontrée.
**Mauvais exemple :**```markdown
Project Manager: "This feature should take about 2 days."
Developer: (Anchored to 2 days, even though realistic estimate is 5 days)
"Okay, I'll try to finish in 2 days."

Result: Rushed work, technical debt, missed deadlines anyway.
```

**Atténuation :**
- Obtenez plusieurs estimations indépendantes
- Utilisez le poker de planification pour l'estimation
- Considérez des plages plutôt que des estimations ponctuelles
- Données historiques de référence
### Erreur de coût irrécupérable
**Qu'est-ce que c'est :** Poursuivre un effort en raison des ressources précédemment investies (temps, argent, efforts), même s'il serait préférable de l'abandonner.
**Mauvais exemple :**```markdown
"We've already spent 6 months building this custom framework. 
We can't switch to the industry standard now, even though 
it would save us time in the long run."
```

**Atténuation :**
- Évaluer les décisions en fonction de la valeur future et non des investissements passés
- Réévaluer régulièrement la viabilité du projet
- Créer une sécurité psychologique pour le pivotement
- Utiliser des critères objectifs pour les décisions de continuer/arrêter
### Heuristique de disponibilité
**Qu'est-ce que c'est :** Surestimer l'importance des informations facilement disponibles ou récentes.
**Mauvais exemple :**```markdown
"I just read about a SQL injection attack, so we should 
prioritize SQL injection prevention over XSS, even though 
our security audit shows XSS is our bigger risk."
```

**Atténuation :**
- Utiliser la prise de décision basée sur les données
- Consulter des modèles de menaces complets
- Consultez les taux de base et les statistiques
- Éviter les biais de récence dans la priorisation
### Effet Dunning-Kruger
**Qu'est-ce que c'est :** Les personnes ayant de faibles capacités dans une tâche surestiment leurs capacités ; les experts peuvent sous-estimer les leurs.
**Mauvais exemple :**```markdown
Junior Developer: "I've completed a Python tutorial. 
I'm ready to architect our entire microservices platform."

Senior Developer: "I've been building distributed systems for 10 years. 
I'm probably missing something important in this design."
```

**Atténuation :**
- Encourager l'apprentissage continu
- Mettre en œuvre des processus d'évaluation par les pairs
- Créer des programmes de mentorat
- Favoriser l'humilité et la curiosité
---

## Erreurs logiques
Les erreurs logiques sont des erreurs de raisonnement qui minent la validité des arguments. Les modèles d’IA peuvent produire des résultats contenant ces erreurs.
### Ad Hominem (Attaque contre la personne)
**Qu'est-ce que c'est :** Attaquer la personne qui avance un argument plutôt que l'argument lui-même.
**Mauvais exemple :**```markdown
"This code review is wrong because the reviewer is a junior developer."
```

**Pourquoi c'est mauvais :** La validité des commentaires dépend de leur contenu et non de l'ancienneté de l'évaluateur.
### Appel à l'autorité
**Qu'est-ce que c'est :** Affirmer que quelque chose est vrai parce qu'une figure d'autorité le dit, sans preuve.
**Mauvais exemple :**```markdown
"This architecture must be correct because Google uses it."
```

**Pourquoi c'est mauvais :** Ce qui fonctionne pour Google à son échelle peut ne pas fonctionner pour votre cas d'utilisation.
### Fausse dichotomie (pensée en noir et blanc)
**Qu'est-ce que c'est :** Présenter seulement deux options lorsqu'il en existe d'autres.
**Mauvais exemple :**```markdown
"We either rewrite everything in Rust or accept that our 
codebase will always be slow and buggy."
```

**Réalité :** De nombreuses options existent entre ces extrêmes (optimiser les hot paths, utiliser Rust pour des composants spécifiques, améliorer le code Python, etc.)
### Pente glissante
**Qu'est-ce que c'est :** Faire valoir qu'un événement entraînera inévitablement une chaîne de conséquences négatives.
**Mauvais exemple :**```markdown
"If we allow this small technical debt, soon our entire 
codebase will be unmaintainable and the company will fail."
```

**Pourquoi c'est mauvais :** Suppose une progression inévitable sans preuve ; ignore les facteurs atténuants.
### Raisonnement circulaire
**Qu'est-ce que c'est :** Utiliser la conclusion comme prémisse.
**Mauvais exemple :**```markdown
"Our code is high quality because we write good code."
```

### Post Hoc Ergo Propter Hoc (Fausse Cause)
**Qu'est-ce que c'est :** En supposant que parce que B a suivi A, A a causé B.
**Mauvais exemple :**```markdown
"We deployed the new feature and then saw increased latency. 
The new feature must be causing the latency."
```

**Réalité :** La corrélation n'implique pas la causalité. D'autres facteurs pourraient être responsables.
### L'homme de paille
**Qu'est-ce que c'est :** Déformer l'argument de quelqu'un pour faciliter son attaque.
**Mauvais exemple :**```markdown
Developer A: "We should add more tests for edge cases."
Developer B: "So you want us to spend all our time writing tests 
and never ship features?"
```

### Erreur de train en marche
**Qu'est-ce que c'est :** Argumenter sur quelque chose est correct parce que beaucoup de gens le croient.
**Mauvais exemple :**```markdown
"Everyone is using Kubernetes, so we should too."
```

**Pourquoi c'est mauvais :** La popularité ne garantit pas l'adéquation à vos besoins spécifiques.
---

## Échecs du raisonnement dans l'IA
### Erreurs logiques en plusieurs étapes
**Mauvais exemple :**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Yes, Alice must be a programmer.
```

**Pourquoi c'est mauvais :**
- Commet l'erreur d'affirmer le conséquent
- Alice pouvait écrire du code sans être programmeuse
- Structure logique : (P→Q, Q) ⊬ P
**Raisonnement correct :**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Not necessarily. While all programmers write code, not everyone
who writes code is a programmer. Alice could be a student, hobbyist, or
work in another field that involves coding.
```

### Échecs du raisonnement mathématique
**Mauvais exemple :**```
User: A bat and ball cost $1.10 together. The bat costs $1 more than the ball.
How much does the ball cost?
Assistant: The ball costs $0.10.
```

**Réalité :** Si la balle coûte 0,10 $ et que la batte coûte 1 $ de plus (1,10 $), le total serait de 1,20 $. La bonne réponse est 0,05 $ pour la balle et 1,05 $ pour la batte.
### Erreurs de raisonnement causal
**Mauvais exemple :**```
User: Ice cream sales and drowning rates both increase in summer. Does ice cream cause drowning?
Assistant: Yes, there appears to be a causal relationship.
```

**Réalité :** Les deux sont causés par un troisième facteur (le temps chaud), et non l'un par l'autre.
---

## Stratégies d'amélioration
### Pour la prise de décision humaine
1. **Formation de sensibilisation** : Apprenez à reconnaître les préjugés courants
2. **Utilisation des listes de contrôle** : utilisez des listes de contrôle de décision pour contrecarrer les préjugés
3. **Équipes diversifiées** : incluez des personnes ayant des perspectives différentes
4. **Pré-mortems** : imaginez l'échec et travaillez à rebours pour identifier les causes
5. **Documentation** : Enregistrez le raisonnement pour un examen ultérieur
### Pour les systèmes d'IA
1. **Invite de chaîne de pensée** : demandez au modèle d'afficher les étapes de raisonnement
2. **Auto-correction** : demandez au modèle d'examiner et de critiquer ses réponses
3. **Vérification formelle** : utilisez des outils de raisonnement symbolique pour la logique critique
4. **Décomposition** : divisez des problèmes complexes en étapes plus petites
5. **Outils externes** : utilisez des calculatrices et des solveurs pour des tâches mathématiques
6. **Échantillons multiples** : générez plusieurs réponses et comparez
---

## Sujets connexes
- **Échecs AI/LLM** : voir`ai_llm_failures.md`pour les hallucinations et les problèmes de raisonnement
- **Sources contradictoires** : voir la documentation sur l'évaluation des informations contradictoires
- **Pensée critique** : appliquez ces concepts pour évaluer les arguments et les preuves
- **Ingénierie rapide** : voir`../02_artificial_intelligence/prompt_engineering.md`pour les techniques permettant de réduire les erreurs de raisonnement
---

## Biais cognitifs supplémentaires dans le développement de logiciels
### Biais du statu quo
**Qu'est-ce que c'est :** Préférence pour le maintien de l'état actuel ; tout changement est perçu comme une perte.
**Mauvais exemple :**```markdown
Team Lead: "Should we upgrade to Python 3.12? It has performance improvements 
and security fixes."

Developer: "Python 3.8 works fine. Why risk breaking things?"

Reality: Staying on an older version increases technical debt, security risks,
and makes future upgrades harder.
```

**Atténuation :**
- Quantifier les coûts liés au fait de ne pas changer
- Définir des calendriers de mise à niveau réguliers
- Créer des environnements d'expérimentation sécurisés
- Considérez les changements comme des opportunités et non comme des menaces
### Biais d'optimisme
**Qu'est-ce que c'est :** Sous-estimer le temps, les coûts et les risques tout en surestimant les avantages.
**Mauvais exemple :**```markdown
Project Plan:
- Development: 2 weeks (realistic: 4 weeks)
- Testing: 3 days (realistic: 1 week)
- Bug fixes: 2 days (realistic: 1-2 weeks)
- Contingency: None

Result: Project takes 3x longer than planned.
```

**Atténuation :**
- Utiliser les prévisions de classe de référence (comparer à des projets antérieurs similaires)
- Ajouter des tampons pour imprévus (20-50%)
- Réaliser des pré-mortems
- Suivre la précision de l'estimation au fil du temps
### Biais de survie
**Qu'est-ce que c'est :** Se concentrer sur les exemples réussis tout en ignorant les échecs.
**Mauvais exemple :**```markdown
"Look at all these successful startups that didn't do market research!
We don't need market research either."

Reality: Many more startups failed without market research, but they're 
not visible because they didn't survive.
```

**Atténuation :**
- Étudier à la fois les réussites ET les échecs
- Rechercher des taux de base et des statistiques
- Considérez les données invisibles
- Évitez de sélectionner des exemples triés sur le volet
### Erreur d'attribution fondamentale
**Qu'est-ce que c'est :** Attribuer le comportement des autres au caractère plutôt qu'aux circonstances.
**Mauvais exemple :**```markdown
"That developer made a bug because they're careless."

Reality: The bug might be due to unclear requirements, time pressure,
lack of testing infrastructure, or fatigue.
```

**Atténuation :**
- Tenir compte des facteurs situationnels
- Pratiquer l'empathie
- Concentrez-vous sur les systèmes et non sur les individus
- Utiliser des autopsies irréprochables
### Biais rétrospectif
**Qu'est-ce que c'est :** Après qu'un événement se soit produit, croire qu'il était prévisible depuis le début.
**Mauvais exemple :**```markdown
After production outage:
"I knew that deployment was risky. This was totally predictable."

Reality: The outcome wasn't obvious beforehand; hindsight makes it seem clear.
```

**Atténuation :**
- Documenter les prédictions avant les résultats
- Examiner le contexte de la décision, pas seulement les résultats
- Évitez la culture du "je vous l'avais bien dit"
- Se concentrer sur l'amélioration des processus, sans blâmer
---

## Plus d'erreurs logiques
### Appel à la nouveauté
**Qu'est-ce que c'est :** Supposer que quelque chose est meilleur parce qu'il est plus récent.
**Mauvais exemple :**```markdown
"We should rewrite our entire backend in the latest framework. 
It's the newest, so it must be better."

Reality: Newer doesn't mean better for your specific use case.
Mature technologies often have better support and stability.
```

### Appel à la tradition
**Qu'est-ce que c'est :** Argumenter sur quelque chose est correct parce que cela a toujours été fait de cette façon.
**Mauvais exemple :**```markdown
"We've always deployed on Fridays at 5 PM. We shouldn't change that."

Reality: Just because something is traditional doesn't make it optimal.
(Actually, deploying on Friday at 5 PM is generally considered bad practice!)
```

### Tu Quoque (Appel à l'hypocrisie)
**Qu'est-ce que c'est :** Rejeter les critiques en soulignant leur incohérence.
**Mauvais exemple :**```markdown
Senior Dev: "You should write tests for this code."
Junior Dev: "But you don't write tests for your code either!"

Reality: The validity of the advice is independent of who gives it.
```

### Question chargée
**Qu'est-ce que c'est :** Poser une question qui contient une hypothèse.
**Mauvais exemple :**```markdown
"Why did you write such terrible code for this module?"

Reality: The question assumes the code is terrible, putting the respondent
on the defensive regardless of actual code quality.
```

### Pas de vrai Écossais
**Qu'est-ce que c'est :** Faire une exception à une affirmation universelle en cas de contestation.
**Mauvais exemple :**```markdown
Person A: "No professional developer writes code without tests."
Person B: "But John is a professional developer and doesn't write tests."
Person A: "Well, no TRUE professional developer writes code without tests."

Reality: This redefines the category to exclude counterexamples rather 
than revising the claim.
```

### Erreur génétique
**Qu'est-ce que c'est :** Juger quelque chose en fonction de son origine plutôt que de son mérite actuel.
**Mauvais exemple :**```markdown
"That library came from a small startup, so it can't be enterprise-grade."

Reality: The origin doesn't determine current quality. Evaluate based on
actual characteristics, not source.
```

### Erreur du juste milieu
**Qu'est-ce que c'est :** En supposant que la vérité se situe toujours entre deux extrêmes.
**Mauvais exemple :**```markdown
Developer A: "We should add comprehensive error handling."
Developer B: "Error handling isn't important, skip it."
Compromise: "Let's add some error handling, but not too much."

Reality: One position might be clearly correct. Compromise isn't always wise.
```

---

## Biais cognitifs dans les systèmes d'IA
### Biais des données de formation
Les modèles d'IA héritent des biais présents dans leurs données d'entraînement.
**Exemple:**```markdown
Training data contains: "The doctor said..." (mostly male pronouns)
                       "The nurse said..." (mostly female pronouns)

Model learns: Doctors are typically male, nurses are typically female.

Result: Model exhibits gender bias in profession associations.
```

**Atténuation :**
- Auditer les données de formation pour déceler les biais
- Utiliser des techniques de débiaisation
- Test des sorties biaisées
- Collecte de données diversifiées
### Biais d'automatisation
**Qu'est-ce que c'est :** S'appuyer trop sur des systèmes automatisés, même lorsqu'ils se trompent.
**Exemple:**```markdown
AI suggests code with a subtle bug.
Developer accepts it without review because "the AI is usually right."

Result: Bug makes it to production.
```

**Atténuation :**
- Maintenir une surveillance humaine
- Encourager l'évaluation critique des résultats de l'IA
- Ne considérez pas l'IA comme infaillible
- Mettre en œuvre des processus de révision
### Illusion de compréhension
**Qu'est-ce que c'est :** Croire que vous comprenez comment fonctionne une IA alors que vous ne le comprenez pas.
**Exemple:**```markdown
User: "The AI understands what I mean, it's like talking to a person."

Reality: LLMs predict tokens based on patterns, they don't truly 
"understand" in the human sense. This illusion leads to over-trust.
```

**Atténuation :**
- Éduquer les utilisateurs sur les limites de l'IA
- Soyez transparent sur le fonctionnement des systèmes
- Évitez d'anthropomorphiser l'IA
- Définir des attentes appropriées
---

## Études de cas
### Étude de cas 1 : Biais de confirmation dans la sélection d'architecture
**Incident :** Une équipe a choisi une architecture de microservices pour une petite application.
**Cause fondamentale :** Le chef d'équipe a lu plusieurs articles faisant l'éloge des microservices et 
n'a recherché que des informations confirmant ce choix, ignorant les avertissements sur la complexité.
**Impact :**
- Frais généraux massifs pour une équipe de 3 développeurs
- La complexité du déploiement a été multipliée par 10
- Performances dégradées en raison des appels réseau
- Projet retardé de 6 mois
**Leçon :** Évaluez les architectures en fonction de votre contexte spécifique, et pas seulement 
des témoignages positifs. Envisagez explicitement les compromis.
### Étude de cas 2 : Coûts irrécupérables dans un système existant
**Incident :** L'entreprise a continué à maintenir un CRM personnalisé pendant 5 ans 
malgré de meilleures alternatives.
**Cause fondamentale :** "Nous avons déjà investi 2 millions de dollars, nous ne pouvons pas l'abandonner maintenant."
**Impact :**
- Coût de maintenance annuel : 500 000 $
- Coût d'opportunité : impossible d'utiliser les fonctionnalités modernes
- Problèmes de rétention des talents (les développeurs voulaient travailler avec des technologies modernes)
- Coût total sur 5 ans : 4,5 M$ contre 1,5 M$ pour l'alternative SaaS
**Leçon :** Les investissements passés sont irrécupérables. Prenez des décisions basées sur la valeur future.
### Étude de cas 3 : Heuristique de disponibilité en sécurité
**Incident :** L'équipe a donné la priorité à la défense contre une attaque récemment médiatisée. 
vecteur tout en ignorant les menaces les plus probables.
**Cause première :** Une couverture médiatique récente a rendu un type de menace hautement disponible 
en mémoire, faussant l’évaluation des risques.
**Impact :**
- 100 000 $ dépensés pour atténuer les menaces à faible probabilité
- La violation réelle s'est produite via un vecteur négligé
- Coût de récupération : 500 000 $+
**Leçon :** Utilisez une modélisation des menaces basée sur les données, et non une priorisation basée sur la récence.
---

## Exercices pratiques
### Exercice de détection des biais
Passez en revue les décisions récentes et demandez :
1. Quelles hypothèses avons-nous faites ?
2. Quelles preuves contrediraient notre conclusion ?
3. Avons-nous envisagé plusieurs options ou nous sommes-nous appuyés sur la première idée ?
4. Continuons-nous en raison de la valeur future ou des investissements passés ?
5. Que recommanderions-nous si quelqu’un d’autre nous le demandait ?
### Détection des erreurs logiques
Entraînez-vous à identifier les erreurs dans les discussions quotidiennes :
```markdown
Statement: "If we don't adopt AI now, we'll be left behind forever."

Analysis: This is a slippery slope fallacy. It assumes inevitable 
progression to being "left behind" without evidence. Also presents 
a false dichotomy (adopt AI or be left behind).
```

### Technique pré-mortem
Avant de démarrer un projet :
1. Imaginez que c'est 6 mois dans le futur
2. Le projet a échoué de façon spectaculaire
3. Écrivez l'histoire des raisons pour lesquelles cela a échoué
4. Travaillez à rebours pour éviter ces modes de défaillance
Cela contrecarre le biais d’optimisme et l’heuristique de disponibilité.
---

## Outils et cadres
### Modèle de journal de décision
```markdown
Date: [When]
Decision: [What we decided]
Context: [Situation and constraints]
Options Considered: [Alternatives evaluated]
Expected Outcome: [What we think will happen]
Confidence Level: [How sure we are]
Review Date: [When to revisit]

[Later] Actual Outcome: [What actually happened]
Lessons Learned: [What we'd do differently]
```

### Liste de contrôle des préjugés
Avant de prendre des décisions importantes :
- [ ] Avons-nous recherché des preuves infirmantes ?
- [ ] Sommes-nous ancrés sur les informations initiales ?
- [ ] Les coûts irrécupérables nous influencent-ils ?
- [ ] Sommes-nous trop confiants dans nos estimations ?
- [ ] Avons-nous envisagé des tarifs de base ?
- [ ] Sommes-nous en train de tomber dans le piège de la disponibilité/récence ?
- [ ] Ferions-nous le même choix si nous repartions à zéro ?
### Exercice de l'équipe rouge
Désignez quelqu’un pour contester la décision proposée :
- Leur rôle est de trouver les défauts
- Ils doivent présenter des points de vue alternatifs
- Pratiques d'équipe répondant aux critiques de manière constructive
- Documenter les préoccupations soulevées et résolues
Cela contrecarre le biais de confirmation et la pensée de groupe.