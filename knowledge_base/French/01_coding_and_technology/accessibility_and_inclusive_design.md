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
# Accessibilité et conception inclusive
L'accessibilité (souvent abrégé en a11y) est la pratique consistant à rendre un logiciel utilisable par tout le monde, y compris les personnes souffrant de handicaps visuels, auditifs, moteurs, cognitifs et neurologiques. Il s'agit d'une exigence légale dans de nombreuses juridictions et d'une pratique d'ingénierie standard. Un logiciel accessible est un meilleur logiciel pour tout le monde, car les décisions de conception qui prennent en charge les utilisateurs handicapés (structure claire, navigation au clavier, contraste suffisant, texte lisible) améliorent l'expérience de tous les utilisateurs.
---

## À qui profite l’accessibilité ?
| Type de handicap | Exemples | Technologie d'assistance |
|----------------|---------|-------------------------|
| **Visuel** | Cécité, basse vision, daltonisme | Lecteurs d'écran (JAWS, NVDA, VoiceOver) ; loupes; modes à contraste élevé |
| **Auditif** | Surdité, malentendant | Légendes ; transcriptions; alertes visuelles |
| **Moteur** | Dextérité limitée, paralysie, tremblements | Navigation au clavier uniquement ; commande vocale ; changer d'appareil ; suivi oculaire |
| **Cognitif** | Dyslexie, TDAH, autisme, troubles de la mémoire | Langage clair ; navigation cohérente ; réduction des distractions |
| **Temporaire** | Bras cassé, soleil éclatant, environnement bruyant | Mêmes aménagements que les invalidités permanentes |
| **Situationnel** | Tenir un bébé, conduire, une main occupée | Interfaces vocales ; grandes cibles tactiles |
**Aperçu clé** : les fonctionnalités d'accessibilité conçues pour les utilisateurs handicapés aident tout le monde. Les coupe-bordures (rampes sur les trottoirs) ont été conçues pour les fauteuils roulants, mais sont utilisées par les parents avec des poussettes, les livreurs avec des chariots et les voyageurs avec des bagages.
---

## Accessibilité du Web (WCAG)
Les directives pour l'accessibilité du contenu Web (WCAG) constituent la norme internationale en matière d'accessibilité du Web.
### Principes WCAG (POUR)
| Principe | Exigence |
|---------------|-------------|
| **Perceptible** | Les informations doivent être présentables de manière à ce que les utilisateurs puissent les percevoir (textes alternatifs, légendes, mise en page adaptable) |
| **Utilisable** | L'interface doit être navigable et utilisable (clavier accessible, suffisamment de temps, pas de contenu provoquant des crises) |
| **Compréhensible** | Les informations et le fonctionnement doivent être compréhensibles (lisibles, prévisibles, aide à la saisie) |
| **Robuste** | Le contenu doit fonctionner avec les technologies d'assistance actuelles et futures |
### Niveaux de conformité WCAG
| Niveau | Exigences | Cible typique |
|-------|-------------|--------------------|
| **A** | Niveau minimum ; 30 critères de réussite | Minimum légal dans certaines juridictions |
| **AA** | Répond aux obstacles les plus courants | Cible standard pour la plupart des organisations |
| **AAA** | Niveau le plus élevé ; tous les contenus ne peuvent pas y parvenir | Contenu spécialisé ; sites éducatifs |
### Critères clés de réussite (niveau AA)
| Critère | Exigence | Comment y parvenir |
|---------------|-------------|--------------|
| **1.1.1 Contenu non textuel** | Toutes les images ont des alternatives de texte |  Attributs `alt` ; `aria-label`pour les icônes |
| **1.3.1 Informations et relations** | Structure transmise par programme | HTML sémantique ; les titres ; listes; monuments |
| **1.4.3 Contraste (minimum)** | Le texte a un rapport de contraste d'au moins 4,5:1 | Testez avec des vérificateurs de contraste ; choisir des palettes de couleurs accessibles |
| **1.4.4 Redimensionner le texte** | Le texte peut être redimensionné à 200 % sans perte | Utilisez des unités relatives (rem, em) ; conception réactive |
| **2.1.1 Clavier** | Toutes les fonctionnalités disponibles via le clavier | Pas de pièges au clavier ; indicateurs de mise au point visibles |
| **2.4.3 Ordre de mise au point** | L'ordre de mise au point préserve le sens et l'opérabilité | Ordre de tabulation logique ; L'ordre DOM correspond à l'ordre visuel |
| **2.4.7 Mise au point visible** | La mise au point du clavier est indiquée visuellement | Styles CSS`:focus-visible` ; jamais`outline: none`sans remplacement |
| **3.3.2 Étiquettes ou instructions** | Les entrées ont des étiquettes |  Éléments `<label>` ; `aria-label`|
| **4.1.2 Nom, rôle, valeur** | Les composants de l'interface utilisateur ont des noms et des rôles accessibles | Attributs ARIA ; HTML sémantique |
---

## ARIA (Applications Internet riches accessibles)
ARIA ajoute des informations d'accessibilité aux éléments HTML qui n'ont pas de sémantique intégrée.
### Rôles ARIA
| Rôle | Objectif | Exemple |
|------|---------|---------|
| `button`| Identifie un élément comme un bouton | Un`<div>`conçu comme un bouton |
| `dialog`| Dialogue modal ou non modal | Composants modaux personnalisés |
| `tablist`/`tab`/`tabpanel`| Interface des onglets | Composants d'onglets personnalisés |
| `alert`| Message important qui apparaît dynamiquement | Notifications d'erreur |
| `progressbar`| Indicateur de progrès | États de chargement |
| `menu`/`menuitem`| Navigation dans les menus | Menus déroulants |
### Attributs ARIA
| Attribut | Objectif | Exemple |
|-----------|---------|---------|
| `aria-label`| Nom accessible lorsqu'aucun texte visible | Bouton avec icône uniquement :`aria-label="Search"`|
| `aria-describedby`| Lie l'élément à sa description | Champ de formulaire avec texte d'aide |
| `aria-expanded`| Indique si une section est développée | Accordéon; liste déroulante |
| `aria-hidden`| Masque l’élément de la technologie d’assistance | Icônes décoratives |
| `aria-live`| Annonce des changements de contenu dynamique | Mises à jour en direct ; notifications |
| `aria-disabled`| Indique que l'élément est désactivé | Boutons grisés |
### La première règle d'ARIA
> **N'utilisez pas ARIA si vous pouvez utiliser du HTML natif à la place.** Un`<button>`est déjà accessible. Un`<div role="button">`vous oblige à ajouter manuellement la gestion du clavier, la gestion de la mise au point et la prise en charge du lecteur d'écran. Utilisez d'abord le HTML sémantique ; ARIA uniquement lorsque les éléments natifs ne peuvent pas faire le travail.
---

## Navigation au clavier
| Clé | Comportement attendu |
|-----|-------------------|
| **Onglet** | Déplacer le focus vers l'élément interactif suivant |
| **Maj + Tabulation** | Déplacer le focus sur l'élément interactif précédent |
| **Entrer / Espace** | Activer l'élément focus (bouton, lien) |
| **Touches fléchées** | Naviguer dans les composants (menus, onglets, groupes radio) |
| **Évasion** | Fermer une boîte de dialogue, un menu ou un popover |
| **Accueil / Fin** | Aller au premier/dernier élément d'une liste |
### Pièges courants du clavier
| Problème | Corriger |
|---------|-----|
| Le focus entre dans un composant mais ne peut pas le quitter | Assurez-vous que Tab déplace le focus ; poignée Évasion |
| Le modal ne piège pas le focus | Le focus doit circuler dans le modal ; revenir au déclencheur à la fermeture |
| Les composants personnalisés ne répondent pas au clavier | Ajouter des gestionnaires de touches pour Entrée, Espace, flèches |
---

## Couleur et design visuel
| Ligne directrice | Exigence |
|---------------|-------------|
| **Rapport de contraste** | 4,5:1 pour un texte normal ; 3:1 pour les textes volumineux (18 pt+ ou 14 pt+ gras) |
| **Ne comptez pas uniquement sur la couleur** | Utilisez des icônes, du texte ou des motifs en plus de la couleur |
| **Indicateurs de concentration** | Toujours visible ; contraste élevé; jamais retiré sans remplacement |
| **Redimensionnement du texte** | La mise en page doit fonctionner avec un zoom de 200 % |
| **Réactif** | Le contenu doit être redistribué à une largeur de 320 px (mobile) |
### Considérations sur le daltonisme
| Tapez | Couleurs concernées | Conseil de conception |
|------|-------|------------|
| **Deutéranopie** | Rouge-vert (le plus courant) | N'utilisez pas le rouge/vert pour transmettre un statut ; utiliser des icônes + couleur |
| **Protanopie** | Rouge-vert | Comme ci-dessus |
| **Tritanopie** | Bleu-jaune | N'utilisez pas le bleu/jaune comme seul différenciateur |
---

## Test d'accessibilité
| Méthode | Outil | Ce qu'il attrape |
|--------|------|----------------|
| **Numérisation automatisée** | hache, phare, WAVE | Texte alternatif manquant ; problèmes de contraste ; Erreurs ARIA |
| **Test du clavier** | Manuel : débranchez la souris, utilisez uniquement le clavier | Ordre de mise au point ; pièges à clavier; gestionnaires manquants |
| **Test du lecteur d'écran** | NVDA (gratuit), VoiceOver (macOS), JAWS | Étiquettes manquantes ; mauvaise structure; changements inopinés |
| **Test de zoom** | Zoom du navigateur à 200 %, 400 % | Rupture de mise en page ; texte tronqué ; problèmes de débordement |
| **Contraste de couleur** | Vérificateur de contraste WebAIM, plugin Stark | Rapports de contraste insuffisants |
| **Tests utilisateur** | Test avec des utilisateurs handicapés | Obstacles du monde réel qui échappent aux outils automatisés |
---

## Exigences légales
| Droit | Région | Exigences |
|-----|--------|-------------|
| **ADA** (Loi sur les Américains handicapés) | États-Unis | Les sites Internet des hébergements publics doivent être accessibles |
| **Article 508** | États-Unis (fédéral) | Les TIC des agences fédérales doivent être accessibles |
| **EAA** (Loi européenne sur l'accessibilité) | UE (2025+) | Les produits et services doivent répondre aux exigences d'accessibilité |
| **EN 301 549** | UE | Norme technique pour l'accessibilité des TIC |
| **ACA** (Loi sur l'accessibilité Canada) | Canada | Industries gouvernementales et réglementées |
| **Loi sur l'égalité 2010** | Royaume-Uni | Les fournisseurs de services doivent procéder à des ajustements raisonnables |
---

## Accessibilité mobile
| Plateforme | Lignes directrices | Outils clés |
|----------|-----------|---------------|
| **iOS** | Directives relatives à l'interface humaine Apple (section Accessibilité) | Voix off ; Type dynamique ; Contrôle des commutateurs |
| **Android** | Directives d'accessibilité Android | Parler ; Accès au commutateur ; Sélectionner pour parler |
| Préoccupation mobile | Solutions |
|---------------|--------------|
| **Cibles tactiles** | Minimum 44×44 points (iOS) / 48×48 dp (Android) |
| **Prise en charge du lecteur d'écran** | Descriptions de contenu ; étiquettes d'accessibilité |
| **Sensibilité au mouvement** | Respectez`prefers-reduced-motion`; éviter les animations à lecture automatique |
| **Dimensionnement dynamique du texte** | Prise en charge des tailles de police du système ; utiliser des unités de texte évolutives |
---

## Résumé
L'accessibilité est un principe de conception qui doit éclairer chaque décision dès le début, et non une fonctionnalité ajoutée à la fin. Utilisez du HTML sémantique. Assurez-vous que la navigation au clavier fonctionne. Maintenez un contraste de couleurs suffisant. Proposez des alternatives textuelles au contenu non textuel. Testez avec des lecteurs d'écran et des utilisateurs handicapés. Le résultat est un logiciel qui fonctionne mieux pour tout le monde, y compris pour ceux qui souffrent de déficiences temporaires, de limitations situationnelles, d'appareils plus anciens, de connexions lentes et des nombreuses différences entre l'utilisation réelle et un environnement de développement contrôlé.