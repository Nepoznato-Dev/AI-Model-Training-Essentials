---
# Métadonnées
titre : "Systèmes embarqués et IoT"
description : "Microcontrôleurs, capteurs, RTOS, protocoles IoT, edge computing"
catégorie : "Codage et technologie"
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
review_by : "Équipe de base de connaissances en matière de codage et de technologie"
next_review : "2027-08-05"
#Classement
tags : [embarqué, systèmes, IoT, codage et technologie]
niveau de difficulté : "intermédiaire"
prérequis : []
estimate_reading_time : "8 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
# Systèmes Embarqués et IoT
Les systèmes embarqués sont des ordinateurs cachés dans d'autres appareils : l'unité de commande du moteur de votre voiture, le contrôleur de votre machine à laver, le microcontrôleur d'un thermostat intelligent. Contrairement aux ordinateurs à usage général, ils sont conçus pour des tâches spécifiques, souvent avec des contraintes strictes en termes de puissance, de mémoire et de vitesse de traitement. L'Internet des objets (IoT) étend les systèmes embarqués en les connectant aux réseaux, permettant ainsi la surveillance, le contrôle et la collecte de données à distance. Ensemble, ils représentent des milliards d’appareils informatiques qui interagissent avec le monde physique.
---

## Fondamentaux des systèmes embarqués
### Qu'est-ce qui rend l'intégration différente
| Aspects | Ordinateur à usage général | Système embarqué |
|--------|------------------------|-----------------|
| **Objectif** | Exécutez n'importe quel logiciel | Effectuer des tâches spécifiques |
| **Ressources** | Processeur, RAM et stockage abondants | Limité (Ko à Mo de RAM ; MHz à faible GHz) |
| **Puissance** | Branché ou grosse batterie | Souvent alimenté par batterie ou récupérant de l'énergie |
| **OS** | Système d'exploitation complet (Windows, Linux, macOS) | RTOS, bare-metal ou Linux embarqué |
| **Interface utilisateur** | Riche (écran, clavier, souris) | Minimal (LED, boutons, capteurs) ou aucun |
| **En temps réel** | Meilleur effort | Des délais souvent serrés en temps réel |
| **À vie** | 3-7 ans | 10-25+ ans |
### Microcontrôleurs vs microprocesseurs
| Fonctionnalité | Microcontrôleur (MCU) | Microprocesseur (MPU) |
|---------|----------------------|-----------|
| **Intégration** | CPU + RAM + Flash + périphériques sur une seule puce | Processeur uniquement ; RAM et stockage externes |
| **Performances** | Faible à modéré (plage MHz) | Élevé (gamme GHz) |
| **Puissance** | Très faible (µA à mA) | Plus élevé (centaines de mA en ampères) |
| **Coût** | 0,10 $ - 10 $ | 5 $ - 100 $+ |
| **Exemples** | STM32, ESP32, Arduino (ATmega), nRF52 | Raspberry Pi (BCM2835), i.MX, Allwinner |
| **Cas d'utilisation** | Capteurs, actionneurs, contrôle simple | Afficheurs, traitements complexes, Linux |
---

## Plateformes embarquées courantes
| Plateforme | MCU/MPU | Caractéristique clé | Idéal pour |
|----------|---------|-------------|----------|
| **Arduino** | ATmega328P (et autres) | Simple; immense communauté | Apprentissage; prototypage |
| **ESP32** | Expressif dual-core | Wi-Fi + Bluetooth ; faible coût | Projets IoT ; appareils connectés |
| **Framboise Pi Pico** | RP2040 (ARM double cœur) | Abordable; Prise en charge de MicroPython | Éducation; projets de loisirs |
| **STM32** | Série ARM Cortex-M | Qualité industrielle ; large gamme | Professionnel intégré ; industriel |
| **nRF52/nRF53** | Semi-conducteur nordique | Spécialiste Bluetooth Low Energy | Appareils portables ; balises |
| **Framboise Pi** | Broadcom BCM (ARM) | Linux complet ; Broches GPIO | Prototypage ; centres de médias ; informatique de pointe légère |
| **BeagleBone** | TI Sitara (BRAS) | Cœurs PRU en temps réel | Industriel; applications en temps réel |
| **ESP32-S3** | Expressif | Accélération de l'IA ; USB | IA de pointe ; applications visuelles |
---

## Systèmes d'exploitation en temps réel (RTOS)
Un RTOS garantit que les tâches critiques se terminent dans un laps de temps défini.
| RTOS | Licence | Idéal pour |
|------|---------|--------------|
| **RTOS gratuit** | MIT | Le plus courant ; large prise en charge des MCU |
| **Zéphyr** | Apache2.0 | Moderne; Fondation Linux ; écosystème en pleine croissance |
| **ThreadX (RTOS Azure)** | MIT | Certifié de sécurité ; IdO |
| **embOS** | Commerciale | Industriel; certifié |
| **RT-Thread** | Apache2.0 | Écosystème chinois ; en croissance à l'échelle mondiale |
### RTOS contre Bare Metal
| Aspects | Métal nu | RTOS |
|--------|-----------|------|
| **Complexité** | Simple pour des tâches simples | Nécessaire pour des tâches complexes et simultanées |
| **Planification** | Manuel (boucle principale + interruptions) | Planification préemptive avec priorités |
| **Évolutivité** | Difficile d'ajouter des fonctionnalités | Facile à ajouter des tâches |
| **Mémoire** | Frais généraux minimes | Petit surcharge (quelques Ko) |
---

## Protocoles de communication
### Protocoles filaires
| Protocole | Vitesse | Distance | Cas d'utilisation |
|----------|-------|----------|----------|
| **UART** | Jusqu'à 1 Mbit/s | Court (à bord) | Console de débogage ; Modules GPS |
| **SPI** | Jusqu'à 100 MHz | Court (à bord) | Périphériques haut débit (écrans, flash) |
| **I²C** | Jusqu'à 3,4 MHz | Court (à bord) | Capteurs ; communication à faible nombre de broches |
| **PEUT** | Jusqu'à 1 Mbit/s | Jusqu'à 1 km | Automobile; industriel |
| **Ethernet** | 10 Mbit/s - 100 Gbit/s | Jusqu'à 100 mètres | Réseautage ; industriel (avec extensions) |
| **USB** | Jusqu'à 40 Gbit/s (USB4) | Jusqu'à 5 mètres | Périphériques ; chargement |
### Protocoles sans fil
| Protocole | Gamme | Puissance | Vitesse | Cas d'utilisation |
|--------------|-------|-------|-------|----------|
| **Wi-Fi** | ~100 m | Élevé | Jusqu'au Wi-Fi 7 (46 Gbit/s théorique) | IoT à large bande passante ; diffusion en continu |
| **Bluetooth Classique** | ~100 m | Moyen | 1-3 Mbit/s | Audio ; transfert de fichiers |
| **BLE** (Bluetooth basse consommation) | ~100 m | Très faible | 1-2 Mbit/s | Appareils portables ; balises; capteurs |
| **Zigbee** | ~100 m (maille) | Faible | 250 kbit/s | Domotique ; capteurs industriels |
| **Z-Wave** | ~100 m (maille) | Faible | 100 kbit/s | Domotique |
| **LoRa/LoRaWAN** | Jusqu'à 15 km | Très faible | 0,3-50 kbit/s | Agriculture; services publics; capteurs à l'échelle de la ville |
| **NB-IoT** | Couverture cellulaire | Faible | 250 kbit/s | Mesure; suivi des actifs |
| **Thème / Matière** | ~100 m (maille) | Faible | Modéré | Maison intelligente (Apple, Google, Amazon) |
| **Cellulaire (4G/5G)** | Mondial | Élevé | Élevé | Véhicules connectés ; surveillance à distance |
---

## Architecture IoT
### La pile IoT
| Couche | Fonction | Exemples |
|-------|----------|---------|
| **Appareils** | Capteurs, actionneurs, microcontrôleurs | ESP32, STM32, Framboise Pi |
| **Connectivité** | Protocoles réseau | MQTT, HTTP, CoAP, LoRaWAN |
| **Informatique de pointe** | Traitement à proximité de l'appareil | AWS Greengrass, Azure IoT Edge |
| **Plateforme cloud** | Ingestion, stockage, traitement de données | AWS IoT, Azure IoT Hub, Google Cloud IoT |
| **Candidature** | Tableaux de bord, analyses, alertes | Grafana, applications web personnalisées |
### Protocoles de communication IoT
| Protocole | Modèle | Idéal pour |
|--------------|---------|--------------|
| **MQTT** | Publier/s'abonner ; léger | La plupart des applications IoT ; faible bande passante |
| **HTTP/REST** | Demande/réponse | Quand la simplicité compte ; intégration web |
| **CoAP** | Demande/réponse ; Basé sur UDP | Appareils contraints ; faible puissance |
| **AMQP** | File d'attente des messages | IoT d'entreprise ; livraison fiable |
| **WebSocket** | Bidirectionnel ; connexion persistante | Tableaux de bord en temps réel ; données en direct |
### MQTT en détail
| Concepts | Descriptif |
|---------|-------------|
| **Courtier** | Serveur central qui achemine les messages (Mosquitto, EMQX, HiveMQ) |
| **Sujet** | Adresse hiérarchique (par exemple,`home/living-room/temperature`) |
| **QoS** | 0 (au plus une fois), 1 (au moins une fois), 2 (exactement une fois) |
| **Message conservé** | Dernier message sur un sujet ; livré aux nouveaux abonnés |
| **Dernière volonté** | Message publié lorsqu'un client se déconnecte de manière inattendue |
---

## Informatique de périphérie
Traiter les données à proximité de la source au lieu de tout envoyer dans le cloud.
| Avantage | Descriptif |
|---------|-------------|
| **Latence réduite** | Pas d’aller-retour vers le cloud ; décisions immédiates |
| **Économies de bande passante** | Envoyer uniquement des résumés ou des anomalies |
| **Confidentialité** | Les données sensibles restent sur site |
| **Fiabilité** | Fonctionne quand Internet est en panne |
| Plateforme | Descriptif |
|--------------|-------------|
| **AWS Greengrass** | Exécuter des fonctions Lambda sur les appareils Edge |
| **Azure IoT Edge** | Exécuter des conteneurs sur des appareils Edge |
| **NVIDIA Jetson** | IA de pointe accélérée par GPU (Orin, Nano) |
| **Framboise Pi** | Informatique de pointe légère |
---

## Mise à jour du micrologiciel (OTA)
Les mises à jour en direct vous permettent de corriger des bugs et d'ajouter des fonctionnalités aux appareils déployés.
| Préoccupation | Solutions |
|---------|----------|
| **Fiabilité** | Flash à double banque ; restauration en cas d'échec |
| **Sécurité** | Images signées ; transferts cryptés |
| **Taille** | Mises à jour Delta (uniquement les parties modifiées) |
| **Connectivité** | Mises à jour en file d'attente lorsque l'appareil est mis en ligne |
---

## Systèmes embarqués critiques pour la sécurité
| Domaine | Normes | Exemples |
|--------|-----------|---------|
| **Automobile** | ISO 26262 (ASIL AD) | Contrôle moteur, freinage, airbags |
| **Médical** | CEI 62304 | Stimulateurs cardiaques, pompes à perfusion |
| **Aérospatiale** | DO-178C (DAL AE) | Contrôle de vol, navigation |
| **Industriel** | CEI 61508 (SIL 1-4) | Automates, contrôleurs de sécurité |
| **Chemin de fer** | EN 50128 (SIL 1-4) | Signalisation, contrôle des trains |
---

## Outils et développement
| Outil | Objectif |
|------|--------------|
| **PlateformeIO** | Développement embarqué multiplateforme (Arduino, ESP32, STM32) |
| **STM32CubeIDE** | L'EDI officiel de ST pour STM32 |
| **IDE Arduino** | Développement simple pour Arduino et cartes compatibles |
| **ESP-IDF** | SDK officiel d'Espressif pour ESP32 |
| **SDK Zephyr** | Système de construction West pour Zephyr RTOS |
| **OpenOCD** | Débogage sur puce |
| **Analyseur logique** | Déboguer les protocoles SPI, I²C, UART |
| ** Wireshark ** | Analyse du protocole réseau |
---

## Résumé
Les systèmes embarqués et l'IoT représentent l'intersection du logiciel et du monde physique. Des microcontrôleurs contrôlant les moteurs aux réseaux de capteurs connectés au cloud, ils nécessitent un état d'esprit différent de celui du développement Web ou d'applications : ressources limitées, exigences en temps réel, longues durées de vie et conséquences des bugs sur le monde physique. L'écosystème a énormément mûri : des frameworks comme ESP-IDF et Zephyr rendent le développement professionnel accessible, tandis que des plateformes comme AWS IoT et Azure IoT Hub gèrent le côté cloud. Les compétences clés sont la compréhension des interfaces matérielles, des protocoles de communication, de la gestion de l'énergie et la discipline nécessaire pour écrire des logiciels qui doivent fonctionner de manière fiable pendant des années sans intervention.