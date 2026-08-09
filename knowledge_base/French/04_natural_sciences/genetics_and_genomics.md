---
# Métadonnées
titre : "Génétique et génomique"
description : "ADN, expression génique, CRISPR, GWAS, technologies de séquençage"
catégorie : "Sciences naturelles"
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
review_by : "Équipe de base de connaissances en sciences naturelles"
next_review : "2027-08-05"
#Classement
tags : [génétique, génomique, sciences naturelles]
niveau de difficulté : "débutant"
prérequis : []
estimate_reading_time : "6 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
# Génétique et Génomique
La génétique est l'étude de l'hérédité – comment les traits sont transmis des parents à la progéniture via l'ADN. La génomique est l'étude de génomes entiers : tous les gènes, les régions non codantes, la manière dont ils interagissent et varient selon les individus et les populations. La transition de la génétique à la génomique a été motivée par la technologie de séquençage : nous sommes passés de l’étude d’un gène à la fois à la lecture de génomes entiers en quelques heures, générant ainsi des données qui transforment la médecine, l’agriculture, la médecine légale et notre compréhension de l’évolution.
---

## Fondamentaux de l'ADN
### Structure de l'ADN
| Composant | Descriptif |
|---------------|-------------|
| **Nucléotide** | Élément constitutif de l'ADN ; se compose d'un sucre (désoxyribose), d'un groupe phosphate et d'une base azotée |
| **Bases** | Adénine (A), Thymine (T), Guanine (G), Cytosine (C) |
| **Appairage de bases** | A s'apparie avec T (2 liaisons hydrogène) ; G s'apparie avec C (3 liaisons hydrogène) |
| **Double hélice** | Deux brins antiparallèles (5' à 3' et 3' à 5') ; tordu en hélice |
| **Chromosomes** | Une seule et longue molécule d’ADN enroulée autour de protéines histones ; les humains en ont 46 (23 paires) |
| **Génome** | L'ensemble complet de l'ADN dans un organisme ; génome humain représente environ 3,2 milliards de paires de bases |
### Dogme central de la biologie moléculaire
| Étape | Processus | Localisation | Produit |
|------|---------|----------|---------|
| **Réplication** | ADN → ADN | Noyau | Deux molécules d'ADN identiques |
| **Transcription** | ADN → ARNm | Noyau | ARN messager |
| **Traduction** | ARNm → protéine | Ribosome (cytoplasme) | Chaîne polypeptidique (protéine) |
---

## Expression génétique
### Comment les gènes sont régulés
| Niveau | Mécanisme | Exemple |
|-------|-----------|---------|
| **Épigénétique** | méthylation de l'ADN ; modification des histones ; remodelage de la chromatine | Inactivation d'un chromosome X chez les femmes |
| **Transcriptionnel** | Les facteurs de transcription lient les promoteurs/amplificateurs ; activer ou réprimer | Opéron Lac dans les bactéries ; gènes sensibles aux hormones |
| **Post-transcriptionnel** | Épissage alternatif ; stabilité de l'ARNm ; microARN | Un gène → plusieurs variantes protéiques |
| **Traductionnel** | Disponibilité des ribosomes ; régulation du facteur d'initiation | Régulation du fer via l'ARNm de la ferritine |
| **Post-traductionnel** | Modification des protéines (phosphorylation, ubiquitination) ; dégradation | Contrôle du cycle cellulaire |
---

## Modèles d'héritage
### Génétique mendélienne
| Modèle | Descriptif | Exemple |
|---------|-------------|---------|
| **Autosomique dominant** | Une copie de l'allèle suffit | la maladie de Huntington ; achondroplasie |
| **Autosomique récessif** | Deux exemplaires requis | Fibrose kystique; drépanocytose |
| **Dominante liée à l'X** | Gène sur le chromosome X ; un exemplaire suffit | Syndrome de Rett |
| **Récessif lié à l'X** | Gène sur le chromosome X ; les hommes sont plus touchés | Hémophilie; daltonisme |
| **Codominance** | Les deux allèles sont exprimés de manière égale | Groupes sanguins ABO (A et B) |
| **Dominance incomplète** | L'hétérozygote est intermédiaire | Fleurs roses de parents rouges et blancs |
| **Polygénique** | Plusieurs gènes contribuent à un seul trait | Hauteur; couleur de peau; renseignements |
| **Pléiotropie** | Un gène affecte plusieurs traits | Syndrome de Marfan (tissu conjonctif, yeux, cœur) |
---

## Génomique
### Types de génomique
| Tapez | Mise au point | Demande |
|------|-------|-------------|
| **Génomique structurale** | Structure 3D de toutes les protéines d'un génome | Conception de médicaments ; ingénierie des protéines |
| **Génomique fonctionnelle** | Que font les gènes ? interactions génétiques ; modèles d'expression | Comprendre les mécanismes de la maladie |
| **Génomique comparative** | Comparaison des génomes d'une espèce à l'autre | Relations évolutives ; identifier les régions conservées |
| **Métagénomique** | ADN provenant d'échantillons environnementaux (non cultivés) | Études du microbiome ; découvrir de nouveaux organismes |
| **Pharmacogénomique** | Comment les gènes affectent la réponse aux médicaments | Médecine personnalisée ; dosage de médicaments |
| **Épigenomique** | Modifications épigénétiques à l'échelle du génome | Diagnostic du cancer ; biologie du développement |
### Technologies de séquençage de l'ADN
| Génération | Technologie | Lire la longueur | Débit | Caractéristique clé |
|-----------|-----------|-------------|------------|-------------|
| **Première génération** | Séquençage de Sanger | ~1 000 pb | Faible | Précision de référence ; utilisé pour la validation |
| **Deuxième génération** | Illumina (Solexa) | 50 à 300 points de base | Très élevé | Lectures courtes ; plateforme dominante ; faible coût par base |
| **Deuxième génération** | Torrent ionique | 200-400 pb | Élevé | À base de semi-conducteurs ; pas d'optique |
| **Troisième génération** | PacBio (SMRT) | 10 000 à 100 000 points de base | Modéré | Lectures longues ; résout les régions répétitives |
| **Troisième génération** | Oxford Nanopore | Jusqu'à des millions de pb | Modéré à élevé | Lectures ultra-longues ; portable (MinION); en temps réel |
---

## Variation génétique
### Types de variations
| Tapez | Descriptif | Fréquence |
|------|-------------|---------------|
| **SNP** (polymorphisme nucléotidique unique) | Changement de base unique | Le plus courant ; ~1 base sur 1 000 |
| **Insertion / Suppression (indel)** | Ajout ou suppression de bases | Peut provoquer des mutations de décalage de cadre de lecture |
| **CNV** (Variation du numéro de copie) | Segments dupliqués ou supprimés (1 Ko – plusieurs Mo) | Contribue à la maladie et à l'évolution |
| **Variation structurelle** | Inversions ; les translocations; grands réaménagements | Moins courant ; peut être pathogène |
| **Microsatellite (STR)** | Répétitions courtes en tandem (2 à 6 pb répétées) | Forensique ; tests de paternité |
### GWAS (Études d'association à l'échelle du génome)
| Étape | Descriptif |
|------|-------------|
| **1. Recueillir des échantillons** | Cas (avec maladie) et contrôles (sans) |
| **2. Génotype** | Utilisez des matrices SNP pour génotyper des centaines de milliers de variantes |
| **3. Test statistique** | Testez chaque SNP pour son association avec le trait |
| **4. Terrain de Manhattan** | Visualisez les résultats sur tous les chromosomes |
| **5. Réplication** | Confirmer les résultats d'échantillons indépendants |
---

## Édition génétique
### CRISPR-Cas9
| Composant | Fonction |
|-----------|----------|
| **ARN guide (ARNg)** | ~20 nucléotides ; correspond à la séquence d'ADN cible |
| **Protéine Cas9** | Ciseaux moléculaires; coupe l'ADN au site cible |
| **Séquence PAM** | Motif court (NGG) à côté de la cible ; requis pour la liaison Cas9 |
| **HDR** (réparation dirigée par homologie) | Édition précise à l'aide d'un modèle de donateur |
| **NHEJ** (Assemblage d'extrémités non homologues) | Réparation sujette aux erreurs ; crée des insertions/suppressions (knockout) |
### Applications d'édition de gènes
| Demande | Descriptif |
|-------------|-------------|
| **Thérapeutique** | Corriger les mutations pathogènes (drépanocytose ; bêta-thalassémie) |
| **Agriculture** | Cultures résistantes aux maladies ; élevage amélioré |
| **Recherche** | Créer des modèles à élimination directe ; étudier la fonction des gènes |
| **Forçage génétique** | Propagation d'une modification génétique dans une population (par exemple, moustiques résistants au paludisme) |
---

## Considérations éthiques
| Problème | Préoccupation |
|-------|--------------|
| **Confidentialité génétique** | À qui appartiennent vos données génomiques ? Les employeurs ou les assureurs peuvent-ils l'utiliser ? |
| **Modification génétique chez les embryons** | Changements héréditaires ; bébés de créateurs; effets non intentionnels hors cible |
| **Discrimination génétique** | GINA (États-Unis) protège contre certaines discriminations mais présente des lacunes |
| **Consentement éclairé** | Les données génomiques révèlent des informations sur des proches qui n'ont pas consenti |
| **Stockage de données** | Les génomes sont volumineux (~ 200 Go bruts) ; défis de stockage et de sécurité à long terme |
| **Actions** | La médecine génomique risque d’élargir les disparités en matière de santé si elle n’est accessible qu’aux populations riches |
---

## Résumé
La génétique étudie le fonctionnement et la transmission des gènes individuels. La génomique étudie des génomes entiers – tous les gènes, leurs interactions et leurs variations. L'ADN est transcrit en ARN, qui est ensuite traduit en protéines. L'expression des gènes est régulée à plusieurs niveaux : épigénétique, transcriptionnel, post-transcriptionnel, traductionnel et post-traductionnel. L'héritage suit des modèles (dominants, récessifs, polygéniques) qui déterminent la manière dont les traits se transmettent entre les générations. Les technologies de séquençage modernes (Illumina, PacBio, Nanopore) permettent de lire des génomes entiers rapidement et à moindre coût. CRISPR-Cas9 permet une édition génétique précise avec un potentiel transformateur en médecine et en agriculture. Les plus grands défis sont d’ordre éthique : qui contrôle les données génomiques, comment réglementer l’édition génétique des embryons et comment garantir que la médecine génomique profite à tous, et pas seulement aux privilégiés.