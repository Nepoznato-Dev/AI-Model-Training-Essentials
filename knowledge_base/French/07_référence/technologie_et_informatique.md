<!-- 
This file was automatically translated from English to French.
Source: technology_and_computing.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Technologie et informatique

## Qu'est-ce qu'un ordinateur ?

Un ordinateur est un appareil électronique qui traite des données selon un ensemble d'instructions appelé programme. Les ordinateurs modernes reposent sur l'architecture de von Neumann, composée d'une unité centrale de traitement (CPU), de mémoire, de stockage et de périphériques d'entrée/sortie. Le CPU exécute les instructions. La RAM (random access memory) stocke temporairement les données pendant le fonctionnement de l'ordinateur. Les dispositifs de stockage comme les SSD et les disques durs conservent les données de manière permanente.

## Langages de programmation

Un langage de programmation est un langage formel utilisé pour écrire des instructions destinées aux ordinateurs. Python est un langage de haut niveau, interprété et polyvalent, apprécié pour sa syntaxe simple et sa lisibilité. Il est largement utilisé en data science, en machine learning, en développement web et en automatisation. JavaScript est le principal langage du développement web et s'exécute dans les navigateurs. Java est un langage compilé et orienté objet, très répandu dans les logiciels d'entreprise et le développement Android. C et C++ sont des langages de plus bas niveau qui offrent un contrôle fin du matériel et sont utilisés en programmation système, en développement de jeux et dans les applications où les performances sont critiques. Rust est un langage moderne de programmation système centré sur la sûreté et les performances.

## Fonctionnement d'Internet

Internet est un réseau mondial d'ordinateurs interconnectés qui communiquent au moyen de protocoles normalisés. Le World Wide Web est un système de sites et de pages web accessibles via Internet à l'aide de navigateurs. HTTP (HyperText Transfer Protocol) et HTTPS (HTTP sécurisé) sont les protocoles utilisés pour transférer les pages web. Une adresse IP est un identifiant numérique unique attribué à chaque appareil d'un réseau. Le DNS (Domain Name System) traduit les noms de domaine lisibles par l'humain (comme google.com) en adresses IP. Un routeur dirige le trafic réseau entre les appareils et les réseaux.

## Réseaux et protocoles

TCP/IP est la suite de protocoles fondamentale d'Internet. IP (Internet Protocol) gère l'adressage et le routage des paquets entre les réseaux, tandis que TCP (Transmission Control Protocol) assure une livraison fiable et ordonnée grâce à la retransmission et au contrôle de flux. UDP est une alternative sans connexion utilisée lorsque la faible latence compte davantage que la garantie de livraison, par exemple pour le streaming, les jeux ou les requêtes DNS. HTTP est un protocole sans état de la couche application pour la communication requête/réponse entre clients et serveurs. HTTPS correspond à HTTP sur TLS et ajoute le chiffrement ainsi que la protection de l'intégrité. REST (Representational State Transfer) est un style d'architecture d'API fondé sur des ressources, des verbes HTTP standard (GET, POST, PUT, PATCH, DELETE) et des interactions sans état. Les WebSockets fournissent des connexions persistantes bidirectionnelles complètes, ce qui permet au client et au serveur d'échanger des messages en temps réel, utile pour le chat, les tableaux de bord en direct et les applications collaboratives.

## Intelligence artificielle

L'intelligence artificielle (IA) est la simulation de l'intelligence humaine par des machines, en particulier des systèmes informatiques. Le machine learning est un sous-ensemble de l'IA dans lequel des systèmes apprennent à partir de données afin de faire des prédictions ou de prendre des décisions sans être explicitement programmés. Le deep learning est un sous-ensemble du machine learning qui utilise des réseaux de neurones comportant de nombreuses couches. Les réseaux de neurones sont des modèles de calcul librement inspirés de la structure des cerveaux biologiques. Les grands modèles de langage (LLMs) sont des modèles d'IA entraînés sur d'énormes volumes de texte afin de générer et de comprendre le langage naturel.

## Algorithmes et structures de données

Un algorithme est une procédure étape par étape permettant de résoudre un problème. Les structures de données sont des façons d'organiser les données dans un ordinateur afin d'y accéder efficacement et de les modifier. Parmi les structures de données courantes figurent les tableaux, les listes chaînées, les piles, les files, les arbres, les graphes et les tables de hachage. Les algorithmes de tri ordonnent les éléments selon un ordre donné ; les exemples classiques sont le tri à bulles, le tri fusion et le tri rapide. La recherche binaire est un algorithme efficace pour trouver un élément dans une liste triée en divisant à plusieurs reprises l'intervalle de recherche par deux.

## Bases de données

Une base de données est une collection organisée de données structurées stockées électroniquement. Une base de données relationnelle stocke les données dans des tables composées de lignes et de colonnes. SQL (Structured Query Language) est le langage standard pour gérer et interroger les bases de données relationnelles. Les bases de données NoSQL stockent les données dans des formats autres que les relations tabulaires, par exemple sous forme de documents, de paires clé-valeur ou de graphes. Parmi les systèmes de bases de données courants figurent PostgreSQL, MySQL, SQLite, MongoDB et Redis. Un index dans une base de données accélère la récupération des données au prix d'un espace de stockage supplémentaire.

## Fondamentaux de la conception de systèmes

La conception de systèmes vise à construire des logiciels fiables, évolutifs et maintenables. L'équilibrage de charge répartit le trafic entre plusieurs serveurs afin d'améliorer la disponibilité et de réduire la latence. La montée en charge horizontale ajoute des machines supplémentaires ; la montée en charge verticale ajoute davantage de ressources à une seule machine. La mise en cache conserve les données fréquemment consultées dans un stockage rapide, par exemple Redis, Memcached ou des caches en périphérie de CDN, afin de réduire la charge sur la base de données et le temps de réponse. À grande échelle, les bases de données exigent de la réplication, du partitionnement (sharding), des stratégies de sauvegarde et des arbitrages soigneux en matière de cohérence. Les microservices divisent les grandes applications en services plus petits, déployables indépendamment, tandis que les monolithes regroupent l'essentiel de la logique dans une seule unité déployable ; les deux approches impliquent des compromis en matière de complexité, de vitesse de déploiement, de débogage et d'autonomie des équipes.

## Systèmes d'exploitation

Un système d'exploitation (OS) est un logiciel qui gère le matériel informatique et fournit des services aux programmes. Les systèmes d'exploitation les plus courants sont Windows, macOS et Linux. Linux est un noyau d'OS open source utilisé dans les serveurs, les systèmes embarqués et Android. L'OS gère les processus (programmes en cours d'exécution), la mémoire, les systèmes de fichiers et les périphériques d'entrée/sortie. Un processus est une instance en cours d'exécution d'un programme. Un thread est la plus petite unité d'exécution au sein d'un processus.

## Contrôle de version

Les systèmes de contrôle de version suivent les modifications du code au fil du temps, ce qui permet aux développeurs de collaborer et de revenir à des états antérieurs. Git est le système de contrôle de version le plus utilisé. Un dépôt (repo) est un ensemble de fichiers et de leur historique. Un commit est un instantané enregistré des modifications. Une branche est une ligne de développement indépendante. Une pull request est une proposition de fusionner des changements d'une branche dans une autre.

## Pratiques de développement logiciel

La programmation orientée objet (OOP) organise le code en objets qui combinent données et comportements. Parmi les principes clés de l'OOP figurent l'encapsulation, l'héritage, le polymorphisme et l'abstraction. Le développement piloté par les tests (TDD) consiste à écrire des tests avant d'écrire le code. Agile désigne un ensemble de méthodologies de développement logiciel mettant l'accent sur le développement itératif, la collaboration et l'adaptabilité. DevOps réunit le développement logiciel et les opérations IT afin de raccourcir le cycle de développement. Les API (Application Programming Interfaces) permettent à différents systèmes logiciels de communiquer entre eux.

## Bases du cloud et de DevOps

Le cloud computing fournit à la demande une infrastructure et des services managés via Internet. Les trois grands fournisseurs de cloud public sont AWS (Amazon Web Services), Microsoft Azure et Google Cloud Platform (GCP). Les modèles de service courants sont IaaS (infrastructure), PaaS (plateforme) et SaaS (logiciel). Les principaux composants du cloud comprennent les instances de calcul, les conteneurs, le stockage objet, les bases de données managées, le réseau et l'IAM (Identity and Access Management). Le CI/CD (Continuous Integration et Continuous Delivery/Deployment) automatise les pipelines de build, de test et de publication afin que le code puisse passer en toute sécurité du commit à la production. Docker regroupe les applications et leurs dépendances dans des conteneurs portables ; en production, ces conteneurs sont généralement déployés via des orchestrateurs comme Kubernetes, des plateformes serverless ou des services de conteneurs managés.

## Formats de données et outils

JSON (JavaScript Object Notation) est un format texte léger construit à partir d'objets (paires clé/valeur), de tableaux, de chaînes, de nombres, de booléens et de `null` ; il est très utilisé dans les API. YAML est un format de configuration convivial qui prend en charge les structures imbriquées et les commentaires, couramment utilisé dans le CI/CD et les définitions d'infrastructure. CSV (Comma-Separated Values) stocke des données tabulaires sous forme de lignes de texte délimitées et est fréquent dans les flux d'import/export de données. XML (eXtensible Markup Language) est un format structuré à base de balises utilisé dans les systèmes hérités, la configuration et les flux documentaires. Les développeurs valident et transforment souvent ces formats avec des linters, des validateurs de schéma (comme JSON Schema), des outils de requête (`jq`, XPath) et des bibliothèques d'analyse dans leur langage de programmation.

## Expressions régulières (Regex)

Une expression régulière est un langage de motifs utilisé pour rechercher, faire correspondre, extraire et transformer du texte. Les concepts de base des regex incluent les littéraux (`cat`), les classes de caractères (`[a-z]`, `\d`), les quantificateurs (`*`, `+`, `?`, `{n,m}`), les ancres (`^`, `$`), les groupes (`(...)`), l'alternance (`a|b`) et l'échappement des caractères spéciaux. Les regex sont largement utilisées pour la validation des entrées, l'analyse de journaux, l'extraction de texte et l'automatisation du rechercher/remplacer. Les différents moteurs (PCRE, JavaScript, Python `re`, RE2) proposent des fonctionnalités variées ; le comportement peut donc changer selon les outils. Les regex sont puissantes mais peuvent vite devenir difficiles à lire ; les motifs complexes doivent être testés et documentés afin d'éviter les erreurs.

## Cybersécurité

La cybersécurité est l'ensemble des pratiques visant à protéger les systèmes informatiques, les réseaux et les données contre les attaques numériques. Les menaces courantes incluent les malwares (logiciels malveillants), le phishing (communication frauduleuse conçue pour voler des informations), les ransomwares (malwares qui chiffrent les données et exigent un paiement) et les attaques par déni de service. Le chiffrement transforme les données en une forme illisible qui ne peut être décodée qu'à l'aide d'une clé. HTTPS utilise TLS (Transport Layer Security) pour chiffrer le trafic web. Des mots de passe forts et uniques ainsi que l'authentification à deux facteurs constituent des pratiques de sécurité fondamentales.

## Concepts de sécurité pour les développeurs

OAuth 2.0 est un cadre d'autorisation qui permet aux utilisateurs d'accorder à une application un accès limité sans partager directement leurs identifiants. OpenID Connect (OIDC) est une couche d'identité construite sur OAuth 2.0 pour l'authentification. JWT (JSON Web Token) est un format de jeton compact contenant des revendications, souvent utilisé pour une authentification sans état, mais il doit être signé correctement et validé strictement (signature, expiration, émetteur, audience). TLS sécurise les données en transit en fournissant chiffrement, intégrité et authentification du serveur par certificats. L'OWASP Top 10 est une liste largement utilisée des risques de sécurité les plus courants pour les applications web, notamment le contrôle d'accès défaillant, les défaillances cryptographiques, l'injection, la conception non sécurisée, les mauvaises configurations de sécurité, les composants vulnérables et l'insuffisance de journalisation et de surveillance. Un développement sécurisé exige une défense en profondeur : validation des entrées, encodage des sorties, principe du moindre privilège, gestion des secrets, correction des dépendances et tests de sécurité réguliers.
