<!-- 
This file was automatically translated from English to French.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Ingénierie des prompts

L'ingénierie des prompts est la pratique qui consiste à concevoir, affiner et optimiser des prompts d'entrée afin d'obtenir la meilleure sortie possible d'un modèle de langage. C'est à la fois un art et une science, et c'est le principal moyen de contrôler le comportement d'un LLM sans recourir au fine-tuning.

---

## Principes fondamentaux

### Clarté et précision
Un prompt clair ne laisse aucune place à l'ambiguïté. Indiquez exactement ce que vous voulez, y compris le format, la longueur et la perspective.

**Vague :**
> "Tell me about Python."

**Spécifique :**
> "Explain Python's Global Interpreter Lock (GIL). Describe its impact on multithreading, give one workaround, and keep your answer under 200 words."

### Fournir du contexte
Les modèles obtiennent de meilleurs résultats lorsqu'ils connaissent le rôle, le public visé et l'objectif.

**Sans contexte :**
> "Write a function to sort a list."

**Avec contexte :**
> "You are a senior Python developer. Write a function to sort a list of dictionaries by a given key. Use type hints and handle edge cases. The audience is junior developers."

### Utiliser des consignes positives
Dites au modèle ce qu'il doit faire, plutôt que ce qu'il doit éviter. « N'utilise pas de jargon » est moins efficace que « Utilise un langage simple, accessible à un enfant de 10 ans ».

---

## Structures de prompts

### Rôles System / User / Assistant
La plupart des API de LLM prennent en charge une structure multi-tour :

- **System message** : définit le comportement, la persona et les contraintes du modèle (et reste valable pendant toute la session).
- **User message** : la requête ou l'instruction en cours.
- **Assistant message** : les réponses précédentes du modèle (utilisées pour la continuité).

**Exemple (style API OpenAI) :**
System: You are a helpful coding assistant. You reply with concise code examples and brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.

### Few-shot prompting
Fournissez 2 à 3 exemples du format d'entrée-sortie attendu avant de demander au modèle d'effectuer la tâche. Cela lui enseigne le motif à reproduire.

**Exemple :**
User: Convert these sentences to passive voice:
Input: the cat chased the mouse.
Output: the mouse was chased by the cat.
Input: the chef cooked the meal.
Output: the meal was cooked by the chef.
Input: the storm destroyed the house.
Output: (model completes)

### Chain-of-Thought (CoT)
Encouragez le modèle à exposer son raisonnement étape par étape. Cela améliore la précision sur l'arithmétique, la logique et les tâches en plusieurs étapes.

**Sans CoT :**
> "What is 24 × 37?"

**Avec CoT :**
> "Calculate 24 × 37. Show your reasoning step by step."

Le modèle produira des étapes intermédiaires, ce qui réduit les erreurs de calcul.

### Sorties structurées
Demandez un format précis comme JSON, YAML ou des tableaux markdown afin de rendre le traitement plus fiable.
User: List three pros and three cons of microservices. Return only a valid JSON object with keys "pros" and "cons", each an array of strings.

---

## Techniques avancées

### Self-Consistency
Générez plusieurs réponses pour un même prompt (avec une température > 0), puis prenez la réponse finale majoritaire. Cette approche est particulièrement efficace pour les tâches de raisonnement.

### Tree-of-Thoughts
Explorez plusieurs chemins de raisonnement en parallèle, évaluez-les, puis choisissez le meilleur. C'est une technique de niveau recherche, mais on peut l'approcher en demandant au modèle d'« explorer des solutions alternatives ».

### ReAct (Reasoning + Acting)
Permettez au modèle d'alterner raisonnement et appels d'outils. Il peut réfléchir, puis agir (par exemple chercher sur le Web, exécuter du code), puis réfléchir à nouveau à partir du résultat.

**Structure de prompt :**
You have access to a calculator and a search engine. For each step, output:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have the final answer.

### Attribution d'une persona
Attribuez une persona précise pour cadrer la réponse.

**Exemples :**
- "You are a Linux kernel developer explaining memory management to a new graduate."
- "You are a friendly nutritionist giving general advice to a client."
- "You are a cynical tech critic reviewing a new gadget."

---

## Réglage des paramètres

- **Temperature** (0.0 – 1.0+) : contrôle l'aléa. Plus elle est basse, plus la réponse est déterministe ; plus elle est élevée, plus elle est créative. Utilisez 0.0–0.3 pour des réponses factuelles ; 0.7–1.0 pour de l'écriture créative.
- **Top-p** (nucleus sampling) : coupe la masse de probabilité à un certain seuil cumulé. 0.9 signifie que le modèle échantillonne parmi les 90 % de tokens les plus probables. En général, on ajuste soit la température, soit le top-p, pas les deux.
- **Max tokens** : fixe la longueur maximale de sortie. Pensez à réserver de la place pour la réponse dans la fenêtre de contexte.
- **Frequency penalty** : réduit la répétition des mêmes tokens.
- **Presence penalty** : encourage le modèle à introduire de nouveaux sujets.

---

## Pièges courants et solutions

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Le modèle ignore certaines parties du prompt | Prompt trop long ou trop chargé | Raccourcissez ; placez l'instruction la plus importante à la fin |
| La sortie est trop verbeuse | Aucune contrainte de longueur | Ajoutez « Limit to 3 sentences » ou définissez `max_tokens` |
| La sortie est trop concise | Contraintes trop strictes | Ajoutez « Explain in detail » ou baissez la température |
| Hallucinations factuelles | Contexte insuffisant ou question ambiguë | Ajoutez « If you are unsure, say 'I don't know' » et fournissez un contexte RAG |
| Format incohérent | Aucune consigne de format explicite | Demandez du JSON, un tableau markdown ou une liste à puces |
| Le modèle répond dans la mauvaise langue | Aucune consigne de langue | Indiquez explicitement « Respond in English » (ou dans la langue cible) |

---

## Modèles de prompts pour des tâches courantes

### Résumé
Résumez le texte suivant en 3 puces. Concentrez-vous sur les arguments principaux et évitez les détails.

Text: [insert text]

### Génération de code
Écrivez une fonction [language] qui [does X].
Requirements:

Use type hints.

Include a docstring.

Handle edge cases: [list].

Do not use external libraries unless specified.

### Explication
Expliquez [concept] à [un non-spécialiste / un étudiant universitaire / un enfant]. Utilisez une analogie lorsque c'est pertinent.

### Brainstorming
Générez 10 idées pour [topic]. Pour chaque idée, donnez une description en une phrase et un défi potentiel.

text

### Classification
Classifiez le retour client suivant comme [positive, neutral, negative].
Fournissez un score de confiance (0-100) et une brève justification.

Feedback: [insert text]

### Traduction avec style
Traduisez le texte anglais suivant en espagnol. Utilisez un ton informel adapté à une publication sur les réseaux sociaux.
Text: [insert text]

---

## Évaluation des prompts

Traitez les prompts comme du code : versionnez-les, testez-les et itérez.

- **A/B testez** différentes variantes de prompt sur un ensemble de requêtes mis de côté.
- **Mesurez le succès** via une évaluation humaine ou des métriques automatisées (par exemple exact match, BLEU, scoring personnalisé).
- **Tenez un registre des prompts** (un simple fichier texte ou un tableur) avec le prompt, sa version et les performances observées.

---
