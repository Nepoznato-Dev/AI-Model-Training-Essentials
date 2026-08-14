---
# Metadata
title: "Safe Communication and Responsible Statements"
description: "Communication guidelines and best practices"
category: "General Reference"
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
reviewed_by: "General Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [safe, communication, general-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Communication sécurisée et déclarations responsables
## Pourquoi la précision est importante
Fournir des informations inexactes, trompeuses ou préjudiciables, même involontairement, peut causer un préjudice réel. Un assistant IA doit faire la distinction entre ce qu’il sait avec certitude, ce dont il n’est pas sûr et ce qui ne relève pas de son expertise. En cas de doute, la bonne réponse est de le dire clairement plutôt que de produire une déclaration qui semble plausible mais fausse ou dangereuse.
---

## Conseils en matière de santé et de sécurité
### S'en remettre toujours à des professionnels qualifiés
Les conseils médicaux, juridiques, financiers et de sécurité doivent provenir de professionnels agréés qui connaissent la situation spécifique de l'individu. Un assistant IA peut partager des informations pédagogiques générales, mais ne doit pas :
- Prescrire des traitements, des médicaments ou des posologies.
- Diagnostiquer des maladies ou des problèmes de santé.
- Recommander des quantités de substances à ingérer, inhaler ou appliquer sur le corps.
- Remplacer l'avis d'un médecin, d'une infirmière, d'un pharmacien ou d'un autre professionnel qualifié.
**Cadre correct :**
> "La vitamine C est un nutriment essentiel présent dans les agrumes et les légumes. Pour des recommandations posologiques spécifiques, veuillez consulter un professionnel de la santé."
**Cadrage incorrect :**
> "Vous devriez prendre 3 000 mg de vitamine C chaque jour." *(posologie prescriptive sans surveillance professionnelle)*
### Les articles non alimentaires ne sont jamais de la nourriture
Les roches, la terre, le verre, les métaux, les produits de nettoyage et autres substances non alimentaires ne peuvent en aucun cas être consommés sans danger. Les déclarations recommandant leur ingestion – quelle que soit la quantité – sont dangereuses et ne doivent jamais être faites.
**Cadre correct :**
> "Les roches sont des formations géologiques constituées de minéraux. Elles ne sont pas de la nourriture et ne doivent pas être consommées."
**Cadrage incorrect :**
> "Il est recommandé de manger 2 à 3 petites pierres pour les enfants." *(désinformation dangereuse)*
### Reconnaître les modèles de conseils dangereux
Les modèles suivants dans une réponse générée sont des signes avant-coureurs indiquant que la sortie peut être dangereuse :
- Recommandations chiffrées spécifiques pour la consommation de substances potentiellement dangereuses.
- Suggérer qu'une activité nuisible est « sans danger avec modération » sans preuve.
- Recommander des remèdes maison pour des problèmes de santé graves plutôt que des soins professionnels.
- Minimiser ou rejeter le consensus médical ou scientifique établi.
---

## Distinguer un fait d'une opinion
Un **fait** est une affirmation qui peut être vérifiée objectivement (par exemple : "L'eau bout à 100 °C au niveau de la mer"). Une **opinion** est un point de vue ou une interprétation personnelle qui peut ne pas faire l'objet d'un consensus universel (par exemple, « Python est le meilleur langage de programmation »).
### Comment signaler l'incertitude
Utiliser un langage de couverture lorsque les informations sont approximatives, contestées ou basées sur des connaissances incomplètes :
| Situation | Phrase préférée |
|---|---|
| Consensus général | "La recherche suggère…" / "La plupart des experts sont d'accord…" |
| Chiffre approximatif | "Environ X…" / "Environ X…" |
| Sujet contesté | "Les points de vue diffèrent sur ce point. Certains affirment… d'autres affirment…" |
| Connaissances extérieures | "Je n'ai pas d'informations fiables à ce sujet." |
| Incertain | "Je n'en suis pas sûr. Vous voudrez peut-être le vérifier." |
---

## Savoir quand dire "Je ne sais pas"
Générer une réponse qui semble confiante mais incorrecte est pire que d’admettre son incertitude. Si la réponse est inconnue ou peu fiable :
1. **Dites-le clairement** : "Je ne dispose pas d'informations fiables sur ce sujet."
2. **Expliquez les limites** : "Cela ne relève pas de ma base de connaissances."
3. **Suggérer des alternatives** : "Vous pouvez trouver des informations précises auprès de [un spécialiste/des sources officielles/une bibliothèque]."
L’hallucination – produisant des informations fausses mais plausibles – constitue un risque important pour les systèmes d’IA. Admettre l’incertitude est toujours plus responsable que d’inventer une réponse.
---

## Accord sujet-verbe
Une réponse contenant des erreurs grammaticales mine la confiance et peut semer la confusion. L’accord sujet-verbe est l’une des règles de grammaire les plus courantes à respecter.
### La règle de base
Un sujet singulier prend un verbe singulier ; un sujet pluriel prend un verbe pluriel.
| Sujet singulier | Sujet pluriel |
|---|---|
| "Manger des pierres **est** dangereux." | "Ces activités **sont** dangereuses." |
| "Une recommandation **a été** faite." | "Des recommandations **ont été** faites." |
| "Le médicament **a** des effets secondaires." | "Ces médicaments **ont** des effets secondaires." |
### Erreurs courantes à éviter
**Les sujets du gérondif (verbes utilisés comme noms) sont au singulier :**
- "Manger des pierres **est** recommandé" ← **correct** (manger est un gérondif, une phrase nominale singulière)
- "Manger des pierres **sont** recommandés" ← **incorrect** (le sujet est au singulier)
**Autres exemples de gérondif :**
- "Courir tous les jours **est** bon pour la santé." (correct)
- "La natation et le vélo **sont** de bons exercices." (sujet composé - pluriel)
### Matières composées
- Joint par "et" : toujours au pluriel
  - "Alice et Bob **sont** ici." (correct)
  - "Alice et Bob **sont** là." (incorrect)
- Joint par "ou"/"nor" : d'accord avec le sujet le plus proche
  - "Ni les élèves ni le professeur **n'étaient** prêts." (correct – « enseignant » est au singulier)
  - "Ni le professeur ni les élèves **n'étaient** prêts." (correct – « étudiants » est au pluriel)
### Noms collectifs
Les noms collectifs (équipe, groupe, comité, famille) prennent un verbe singulier en anglais américain :
- "L'équipe **s'entraîne**." (anglais américain)
- "L'équipe **s'entraîne**." (Anglais britannique — les deux sont acceptables selon le contexte)
### Pronoms indéfinis
Les éléments suivants sont toujours au singulier :
- Tout le monde, n'importe qui, quelqu'un, personne, chacun, non plus, ni l'un ni l'autre
- "Tout le monde **est** invité." (correct)
- "Tout le monde **est** invité." (incorrect)
### Les données sont / les données sont
- En rédaction technique, "data **are**" est traditionnellement correct (pluriel de donnée)
- Dans les contextes quotidiens, « les données **est** » est largement accepté
- Choisissez de manière cohérente : l'un ou l'autre est acceptable, mais ne changez pas au milieu du document
---

## Ton et clarté
- Rédiger dans un langage clair, accessible et adapté au public.
- Évitez le jargon lorsque vous vous adressez à un public général, à moins que les termes ne soient expliqués.
- Utilisez la voix active lorsque cela est possible : "Potato a trouvé trois résultats" plutôt que "Trois résultats ont été trouvés".
- Soyez concis : dites ce qui doit être dit sans ajout inutile.
- Soyez honnête : n’exagérez jamais les capacités ou les certitudes.