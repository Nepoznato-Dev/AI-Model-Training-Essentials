---
# Metadata
title: "Logic and Critical Thinking"
description: "Formal logic, logical fallacies, argument analysis, and critical thinking frameworks"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Split from mathematics_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [logic, critical-thinking, fallacies, arguments, reasoning, boolean-algebra]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "12 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Logique et pensée critique
La logique est l’étude du raisonnement valable – comment construire des arguments solides et identifier ceux qui sont erronés. La pensée critique est l’habitude disciplinée de remettre en question les hypothèses, d’évaluer les preuves et de raisonner soigneusement. Ces compétences sont essentielles non seulement en mathématiques et en informatique, mais aussi pour la prise de décision quotidienne, la recherche scientifique et la navigation dans un monde riche en informations.
---

## Qu'est-ce qu'un argument ?
En logique, un **argument** est un ensemble d'énoncés (prémisses) destinés à étayer une conclusion.
| Composant | Rôle | Exemple |
|---------------|------|--------------|
| **Prémisse** | Une déclaration présentée comme preuve | "Tous les humains sont mortels" |
| **Conclusion** | La revendication que les locaux soutiennent | "Socrate est mortel" |
| **Inférence** | L'étape logique des prémisses à la conclusion | "Socrate est humain, donc..." |
### Valide vs. Son
| Terme | Signification | Exemple |
|------|---------|---------|
| **Valide** | Si les prémisses sont vraies, la conclusion doit être vraie | La structure est correcte, même si les prémisses sont fausses |
| **Invalide** | La conclusion ne découle pas des prémisses | La structure logique est brisée |
| **Son** | Valide ET toutes les prémisses sont réellement vraies | L'étalon-or de l'argumentation |
| **Malsain** | Soit invalide, soit a de fausses prémisses | Arguments les plus erronés |
---

## Types de raisonnement
| Tapez | Itinéraire | Force | Exemple |
|------|-----------|--------------|---------|
| **Déductif** | Général → spécifique | Certain (si valide) | "Tous les mammifères ont des poumons. Une baleine est un mammifère. Par conséquent, une baleine a des poumons." |
| **Inductif** | Spécifique → général | Probable | "Tous les cygnes que j'ai vus sont blancs. Par conséquent, tous les cygnes sont probablement blancs." |
| **Abductif** | Observation → meilleure explication | Plausible | "L'herbe est mouillée. La meilleure explication est qu'il a plu." |
---

## Logique propositionnelle
La logique propositionnelle traite des propositions simples et de la manière dont elles se combinent :
### Connecteurs logiques
| Connectif | Symbole | Signification | État de vérité |
|---------------|--------|---------|----------------|
| **ET** | ∧ (p ∧q) | Conjonction | Vrai seulement lorsque les deux sont vrais |
| **OU** | ∨ (p ∨q) | Disjonction | Vrai quand au moins un est vrai |
| **PAS** | ¬ (¬p) | Négation | Valeur de vérité opposée |
| **SI... ALORS** | → (p → q) | Implications | Faux uniquement lorsque p est vrai et q est faux |
| **IFF** | ↔ (p ↔q) | Biconditionnel | Vrai lorsque les deux ont la même valeur de vérité |
### Table de vérité pour l'implication (p → q)
| p | q | p → q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |
Remarque : Une fausse prémisse rend l’implication faussement vraie. "Si la lune est du fromage, alors je suis le Pape" est logiquement vrai.
---

## Algèbre booléenne
L'algèbre booléenne est la mathématique des valeurs vraies/fausses et constitue le fondement de la conception et de la programmation de circuits numériques :
| Droit | Expressions | Signification |
|-----|-----------|---------|
| **Commutatif** | UNE ∧ B = B ∧ UNE | L'ordre n'a pas d'importance |
| **Associatif** | (UNE ∧ B) ∧ C = UNE ∧ (B ∧ C) | Le regroupement n'a pas d'importance |
| **Distributif** | UNE ∧ (B ∨ C) = (UNE ∧ B) ∨ (UNE ∧ C) | AND distribue sur OR |
| **De Morgan** | ¬(UNE ∧ B) = ¬UNE ∨ ¬B | La négation retourne ET en OU |
| **De Morgan** | ¬(UNE ∨ B) = ¬UNE ∧ ¬B | La négation retourne OU en ET |
| **Double négation** | ¬(¬A) = UNE | Deux négations annulent |
| **Identité** | UNE ∧ T = UNE ; UNE ∨ F = UNE | Éléments d'identité |
| **Complément** | A ∧ ¬A = F ; UNE ∨ ¬A = T | Contradiction et tautologie |
---

## Erreurs logiques courantes
Reconnaître les erreurs est essentiel pour la pensée critique :
### Erreurs formelles (erreurs structurelles)
| Erreur | Structure | Exemple |
|---------|-----------|---------|
| **Affirmer le conséquent** | Si P alors Q. Q. Donc P. | "S'il pleut, le sol est mouillé. Le sol est mouillé. Donc il a plu." (Peut être un arroseur.) |
| **Nier l'antécédent** | Si P alors Q. Pas P. Donc pas Q. | "S'il pleut, le sol est mouillé. Il n'a pas plu. Donc le sol n'est pas mouillé." |
### Erreurs informelles (erreurs de contenu)
| Erreur | Descriptif | Exemple |
|---------|-------------|---------|
| **Ad Hominem** | Attaquer la personne, pas l'argumentation | "Vous ne pouvez pas faire confiance à son plan économique – elle n'est même pas économiste." |
| **Homme de paille** | Déformer un argument pour faciliter son attaque | "Vous voulez réduire les dépenses militaires ? Alors vous voulez laisser le pays sans défense !" |
| **Appel à l'autorité** | Citer une autorité qui n'est pas experte dans le domaine concerné | "Cette célébrité dit que ce régime fonctionne, donc il doit être efficace." |
| **Faux dilemme** | Présenter seulement deux options alors qu'il en existe d'autres | "Soit vous êtes avec nous, soit vous êtes contre nous." |
| **Pente glissante** | Affirmer qu'un événement mènera inévitablement à un résultat extrême | "Si nous permettons cela, ce sera le chaos total." |
| **Raisonnement circulaire** | La conclusion est supposée dans les prémisses | "Le livre est vrai parce qu'il dit que c'est vrai." |
| **Généralisation hâtive** | Tirer une conclusion générale à partir de preuves insuffisantes | "J'ai rencontré deux personnes impolis de cette ville. Tout le monde là-bas doit être impoli." |
| **Post Hoc Ergo Propter Hoc** | En supposant une causalité à partir d'une séquence temporelle | "J'ai pris ce supplément et je me sentais mieux, donc ça doit marcher." |
| **Hareng rouge** | Introduire un sujet non pertinent pour distraire | "Vous posez des questions sur ma politique en matière d'éducation, mais ce qui compte vraiment, c'est l'économie." |
| **Le train en marche** | Quelque chose est vrai parce que beaucoup de gens le croient | "Tout le monde achète ce produit, donc ce doit être le meilleur." |
---

## Évaluation des arguments : une liste de contrôle
| Étape | Question |
|------|----------|
| 1. **Identifier la conclusion** | Qu’est-ce que l’argument tente de prouver ? |
| 2. **Identifier les lieux** | Quelles preuves sont proposées ? |
| 3. **Vérifier la validité** | La conclusion découle-t-elle des prémisses ? |
| 4. **Vérifier la solidité** | Les prémisses sont-elles réellement vraies ? |
| 5. **Recherchez les erreurs** | Y a-t-il des erreurs de structure ou de contenu ? |
| 6. **Considérez les contre-arguments** | Quelles objections pourrait-il y avoir ? |
| 7. **Évaluer la qualité des preuves** | Les preuves sont-elles fiables, suffisantes et pertinentes ? |
---

## Pourquoi c'est important
La logique et la pensée critique constituent le fondement des mathématiques, de l’informatique, du droit et de la recherche scientifique. Dans un monde plein de désinformation, de publicité et de rhétorique persuasive, la capacité d’évaluer rigoureusement des arguments n’est pas seulement une compétence académique : c’est une compétence de survie. Que vous déboguiez du code, conceviez des algorithmes ou preniez des décisions de vie, un raisonnement clair sépare les bons jugements des mauvais.