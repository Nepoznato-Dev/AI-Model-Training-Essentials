---
# Métadonnées
titre : "Ingénierie rapide"
description : "Techniques et stratégies d'invite"
catégorie : "IA et Machine Learning"
version : "1.0.0"
statut : "actif"
# Contribution
auteurs :
  - nom : « Équipe de formation des modèles IA »
    email: ""
    rôle : "original_author"
contributeurs : []
journal des modifications :
  - version : "1.0.0"
    date : "05/08/2026"
    auteur : « Équipe de formation des modèles IA »
    modifications : « Ajout des métadonnées de premier plan YAML pour le suivi des contributeurs »
# Révision
créé : "2026-08-05"
last_modified : "05/08/2026"
date_de_revue : "05/02/2027"
review_by : "Équipe de base de connaissances sur l'IA et l'apprentissage automatique"
next_review : "2027-08-05"
#Classement
balises : [invite, ingénierie, IA et apprentissage automatique]
niveau de difficulté : "intermédiaire"
prérequis : []
estimate_reading_time : "7 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
# Ingénierie rapide
L'ingénierie des invites consiste à concevoir, affiner et optimiser les invites de saisie pour obtenir le meilleur résultat possible à partir d'un modèle de langage. C'est à la fois un art et une science, et c'est la principale interface pour contrôler le comportement du LLM sans réglage fin.
---

## Principes fondamentaux
### Clarté et spécificité
Une invite claire ne laisse aucune place à l’ambiguïté. Spécifiez exactement ce que vous voulez, y compris le format, la longueur et la perspective.
**Vague :**
> "Parlez-moi de Python."
**Spécifique :**
> "Expliquez le Global Interpreter Lock (GIL) de Python. Décrivez son impact sur le multithreading, donnez une solution de contournement et gardez votre réponse en moins de 200 mots."
### Fournir le contexte
Les modèles fonctionnent mieux lorsqu’ils connaissent le rôle, le public et l’objectif.
**Sans contexte :**
> "Écrivez une fonction pour trier une liste."
**Avec contexte :**
> "Vous êtes un développeur Python senior. Écrivez une fonction pour trier une liste de dictionnaires selon une clé donnée. Utilisez des astuces de type et gérez les cas extrêmes. Le public est constitué de développeurs juniors."
### Utilisez des instructions positives
Dites au modèle quoi faire, pas ce qu'il faut éviter. « N'incluez pas de jargon » est plus faible que « Utilisez un langage simple et accessible à un enfant de 10 ans ».
---

## Structures d'invite
### Rôles système / utilisateur / assistant
La plupart des API LLM prennent en charge une structure multi-tours :
- **Message système** : définit le comportement, la personnalité et les contraintes du modèle (persiste pendant toute la session).
- **Message utilisateur** : La requête ou l'instruction en cours.
- **Message de l'assistant** : Les réponses précédentes du modèle (utilisées pour la continuité).
**Exemple (style API OpenAI) :**
Système : Vous êtes un assistant de codage utile. Vous répondez avec des exemples de code concis et de brèves explications. Ne fournissez jamais de code dangereux.
Utilisateur : écrivez une fonction Python pour télécharger un fichier à partir d'une URL.
### Invite de quelques tirs
Fournissez 2 à 3 exemples du format d'entrée-sortie souhaité avant de demander au modèle d'effectuer la tâche. Cela enseigne le modèle.
**Exemple :**
Utilisateur : Convertissez ces phrases à la voix passive :
Entrée : Le chat a poursuivi la souris.
Résultat : La souris a été poursuivie par le chat.
Entrée : Le chef a préparé le repas.
Résultat : Le repas a été cuisiné par le chef.
Entrée : La tempête a détruit la maison.
Résultat : (modèle terminé)
### Chaîne de pensée (CoT)
Encouragez le modèle à montrer son raisonnement étape par étape. Cela améliore la précision des tâches arithmétiques, logiques et en plusieurs étapes.
**Sans CoT :**
> "Qu'est-ce que 24×37 ?"
**Avec CoT :**
> "Calculez 24 × 37. Montrez votre raisonnement étape par étape."
Le modèle produira des étapes intermédiaires, réduisant ainsi les erreurs arithmétiques.
### Résultats structurés
Demandez un format spécifique comme JSON, YAML ou des tableaux de démarques pour rendre l'analyse fiable.
Utilisateur : énumérez trois avantages et trois inconvénients des microservices. Renvoie uniquement un objet JSON valide avec les clés « avantages » et « contre », chacune étant un tableau de chaînes.
---

## Techniques avancées
### Auto-cohérence
Générez plusieurs réponses pour la même invite (avec une température > 0) et votez à la majorité sur la réponse finale. Ceci est particulièrement efficace pour les tâches de raisonnement.
### Arbre des pensées
Explorez plusieurs chemins de raisonnement en parallèle, évaluez chacun d'entre eux et choisissez le meilleur. Il s'agit d'une technique de niveau recherche mais qui peut être approchée en demandant au modèle « d'explorer des solutions alternatives ».
### ReAct (Raisonnement + Agir)
Laissez le modèle entrelacer le raisonnement avec les appels d'outils. Il peut réfléchir, puis agir (par exemple, effectuer une recherche sur le Web, exécuter du code), puis réfléchir à nouveau en fonction du résultat.
**Structure de l'invite :**
Vous avez accès à une calculatrice et à un moteur de recherche. Pour chaque étape, obtenez :
Pensée : (votre raisonnement)
Action : (nom de l'outil, entrée)
Observation : (sortie de l'outil)
... continuez jusqu'à ce que vous ayez la réponse finale.
### Affectation de personnalité
Attribuez un personnage spécifique pour encadrer la réponse.
**Exemples :**
- "Vous êtes un développeur de noyau Linux expliquant la gestion de la mémoire à un nouveau diplômé."
- "Vous êtes un nutritionniste sympathique qui donne des conseils généraux à un client."
- "Vous êtes un critique technologique cynique qui examine un nouveau gadget."
---

## Réglage des paramètres
- **Température** (0,0 – 1,0+) : contrôle le caractère aléatoire. Inférieur = plus déterministe, supérieur = plus créatif. Utilisez 0,0 à 0,3 pour les réponses factuelles ; 0,7 à 1,0 pour l’écriture créative.
- **Top-p** (échantillonnage de noyau) : coupe la masse de probabilité à un certain seuil cumulatif. 0,9 signifie que le modèle échantillonne les 90 % des jetons les plus probables. Ajustez généralement la température ou le top-p, pas les deux.
- **Max tokens** : définit la longueur maximale de sortie. N'oubliez pas de réserver un espace pour la réponse dans la fenêtre contextuelle.
- **Pénalité de fréquence** : Réduit la répétition des mêmes jetons.
- **pénalité de présence** : encourage le modèle à introduire de nouveaux sujets.
---

## Pièges et solutions courants
| Problème | Cause probable | Corriger |
|---------|--------------|-----|
| Le modèle ignore certaines parties de l'invite | Invite trop longue ou surchargée | Raccourcir; mettre l'instruction la plus importante à la fin |
| La sortie est trop verbeuse | Aucune contrainte de longueur | Ajoutez "Limiter à 3 phrases" ou définissez max_tokens |
| La sortie est trop laconique | Trop restrictif | Ajoutez « Expliquez en détail » ou baissez la température |
| Hallucinations factuelles | Contexte insuffisant ou question ambiguë | Ajoutez « Si vous n'êtes pas sûr, dites « Je ne sais pas » » et fournissez un contexte RAG |
| Formatage incohérent | Aucune instruction de format explicite | Demandez du JSON, un tableau de démarques ou une liste à puces |
| Modèle de réponses dans une mauvaise langue | Pas d'enseignement linguistique | Indiquez explicitement « Répondre en anglais » (ou dans votre langue cible) |
---

## Modèles d'invite pour les tâches courantes
### Résumé
Résumez le texte suivant en 3 puces. Concentrez-vous sur les principaux arguments et évitez les détails.
Texte : [insérer le texte]

### Génération de code
Écrivez une fonction [langage] qui [fait X].
Exigences:
Utilisez des astuces de type.
Incluez une docstring.
Gérer les cas extrêmes : [liste].
N'utilisez pas de bibliothèques externes, sauf indication contraire.

### Explication
Expliquez [le concept] à un [non-expert / étudiant universitaire / enfant]. Utilisez une analogie le cas échéant.
### Réflexion
Générez 10 idées pour [sujet]. Pour chaque idée, donnez une description en une phrase et un défi potentiel.
texte
###Classement
Classez les commentaires clients suivants comme [positifs, neutres, négatifs].
Fournissez un score de confiance (0-100) et une brève raison.
Commentaires : [insérer le texte]
### Traduction avec style
Traduisez le texte anglais suivant en espagnol. Utilisez un ton informel adapté à une publication sur les réseaux sociaux.
Texte : [insérer le texte]
---

## Évaluation des invites
Traitez les invites comme du code : versionnez-les, testez-les et itérez.
- **Test A/B** différentes variantes d'invite sur un ensemble de requêtes retenu.
- **Mesurez le succès** via une évaluation humaine ou des mesures automatisées (par exemple, correspondance exacte, BLEU, notation personnalisée).
- **Conservez un registre d'invites** (un simple fichier texte ou une feuille de calcul) avec l'invite, la version et les performances observées.
---