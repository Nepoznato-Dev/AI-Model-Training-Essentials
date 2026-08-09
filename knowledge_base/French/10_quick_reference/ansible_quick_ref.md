---
# Métadonnées
titre : "Ansible et gestion de la configuration"
description : "Playbooks Ansible, modules, rôles, inventaire, aide-mémoire d'automatisation"
catégorie : "Référence rapide"
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
review_by : "Équipe de base de connaissances de référence rapide"
next_review : "2027-08-05"
#Classement
balises : [ansible, référence rapide]
niveau de difficulté : "débutant"
prérequis : []
estimate_reading_time : "8 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
# Ansible et gestion des configurations
Ansible est un outil de gestion et d'automatisation de configuration sans agent. Il utilise SSH (ou WinRM pour Windows) pour se connecter aux serveurs et exécuter les tâches définies dans les playbooks YAML. Contrairement aux outils qui nécessitent l'installation d'agents sur chaque machine, Ansible est basé sur le push : vous exécutez des commandes à partir d'un nœud de contrôle. Il est utilisé pour le provisionnement du serveur, le déploiement d'applications, la gestion de la configuration et l'exécution de tâches ad hoc.
---

## Concepts de base
| Concepts | Descriptif |
|---------|-------------|
| **Inventaire** | Liste des hôtes gérés (format INI ou YAML) |
| **Livre de jeu** | Fichier YAML définissant un ensemble de tâches à exécuter |
| **Jouer** | Un mappage entre les hôtes et les tâches au sein d'un playbook |
| **Tâche** | Une seule action à effectuer sur un hôte |
| **Module** | Une unité de travail (par exemple,`apt`,`copy`,`service`,`template`) |
| **Rôle** | Collection réutilisable de tâches, variables, fichiers et gestionnaires |
| **Variable** | Valeurs dynamiques utilisées dans les playbooks |
| **Gestionnaire** | Tâche déclenchée par une notification (par exemple, redémarrage du service) |
| **Fait** | Informations système collectées sur les hôtes (OS, IP, etc.) |
---

## Commandes communes
| Commande | Descriptif |
|---------|-------------|
| `ansible all -m ping`| Tester la connectivité à tous les hôtes |
| `ansible all -m shell -a "uptime"`| Exécuter une commande shell sur tous les hôtes |
| `ansible-playbook site.yml`| Exécuter un playbook |
| `ansible-playbook site.yml --check`| Exécution à sec (mode vérification) |
| `ansible-playbook site.yml --diff`| Montrer ce qui changerait |
| `ansible-playbook site.yml -l web`| Courir contre un groupe spécifique |
| `ansible-playbook site.yml --tags deploy`| Exécutez uniquement les tâches avec des balises spécifiques |
| `ansible-playbook site.yml --skip-tags debug`| Ignorer les tâches avec des balises spécifiques |
| `ansible-vault encrypt secrets.yml`| Chiffrer un fichier |
| `ansible-vault decrypt secrets.yml`| Décrypter un fichier |
| `ansible-vault edit secrets.yml`| Modifier un fichier crypté |
| `ansible-galaxy install geerlingguy.nginx`| Installer un rôle depuis Ansible Galaxy |
| `ansible-inventory --graph`| Afficher l'inventaire sous forme de graphique |
| `ansible-doc apt`| Afficher la documentation d'un module |
---

## Formats d'inventaire
### Format INI
```ini
[web]
web1.example.com
web2.example.com

[db]
db1.example.com ansible_user=deploy

[production:children]
web
db
```

### Format YAML
```yaml
all:
  children:
    web:
      hosts:
        web1:
          ansible_host: 10.0.0.1
        web2:
          ansible_host: 10.0.0.2
    db:
      hosts:
        db1:
          ansible_user: deploy
```

---

## Structure du manuel de jeu
```yaml
---
- name: Deploy web application
  hosts: web
  become: true
  vars:
    app_port: 8080
  
  tasks:
    - name: Install dependencies
      apt:
        name: ['nginx', 'python3', 'git']
        state: present
        update_cache: true

    - name: Copy application config
      template:
        src: templates/app.conf.j2
        dest: /etc/app/config.conf
      notify: Restart application

    - name: Ensure service is running
      service:
        name: myapp
        state: started
        enabled: true

  handlers:
    - name: Restart application
      service:
        name: myapp
        state: restarted
```

---

## Modules communs
| Module | Objectif | Exemple |
|--------|---------|---------|
| **apt / miam / dnf** | Gestion des paquets | `apt: name=nginx state=present`|
| **copie** | Copier les fichiers sur les hôtes | `copy: src=file.txt dest=/tmp/`|
| **modèle** | Copier des fichiers avec des variables Jinja2 | `template: src=conf.j2 dest=/etc/app.conf`|
| **fichier** | Gérer les fichiers et répertoires | `file: path=/tmp/dir state=directory`|
| **service** | Gérer les services | `service: name=nginx state=restarted`|
| **utilisateur/groupe** | Gérer les utilisateurs et les groupes | `user: name=deploy shell=/bin/bash`|
| **cron** | Gérer les tâches cron | `cron: name="backup" job="/usr/bin/backup.sh"`|
| **shell / commande** | Exécuter des commandes | `shell: echo "hello" > /tmp/test`|
| **git** | Cloner des référentiels | `git: repo=https://... dest=/opt/app`|
| **systèmed** | Gérer les unités systemd | `systemd: name=myapp enabled=true`|
| **pare-feu / ufw** | Gérer les règles de pare-feu | `ufw: rule=allow port=80 proto=tcp`|
| **fichier de ligne** | Gérer les lignes dans les fichiers | `lineinfile: path=/etc/hosts line="..."`|
| **fichier bloqué** | Gérer les blocs de texte dans les fichiers | Insérer/mettre à jour des blocs de configuration |
| **récupérer** | Copier des fichiers depuis des hôtes | `fetch: src=/var/log/app.log dest=/local/`|
| **uri** | Interagissez avec les services Web | `uri: url=https://api.example.com method=GET`|
| **débogage** | Imprimer les messages | `debug: msg="Deployed {{ app_version }}"`|
---

## Structure des rôles
```
role_name/
├── tasks/
│   └── main.yml       # Main task list
├── handlers/
│   └── main.yml       # Handlers
├── templates/
│   └── *.j2           # Jinja2 templates
├── files/
│   └── *              # Static files
├── vars/
│   └── main.yml       # Role variables (high priority)
├── defaults/
│   └── main.yml       # Default variables (low priority)
├── meta/
│   └── main.yml       # Role metadata and dependencies
└── README.md
```

---

## Conseils et dépannage
| Astuce | Descriptif |
|-----|-------------|
| **Utiliser le mode vérification** | Toujours`--check --diff`avant d'appliquer les modifications |
| **Utiliser des balises** | Marquer les tâches pour une exécution sélective |
| **Utiliser le coffre-fort pour les secrets** | Ne stockez jamais les mots de passe en texte brut |
| **Idempotence** | Les tâches doivent pouvoir être exécutées plusieurs fois en toute sécurité |
| **Utiliser devenir** | Utiliser`become: true`pour l'élévation de privilèges |
| **Limiter le parallélisme** | Utilisez`--forks`pour contrôler les connexions simultanées |
| **Tester avec Vagrant / Docker** | Testez les playbooks localement avant de les exécuter en production |
| **Utilisez`--step`** | Mode interactif : confirmer chaque tâche avant exécution |
---

## Résumé
Ansible automatise la configuration du serveur et le déploiement d'applications via des playbooks YAML exécutés via SSH. Le flux de travail est le suivant : définir l'inventaire → écrire des playbooks → exécuter`ansible-playbook`. Les concepts clés incluent les modules (unités de travail), les rôles (collections réutilisables), les gestionnaires (tâches déclenchées) et les variables (valeurs dynamiques). Les modules communs couvrent la gestion des packages, les opérations sur les fichiers, le contrôle des services et la gestion des utilisateurs. Utilisez toujours le mode vérification avant de postuler ; stocker les secrets dans Ansible Vault ; s'assurer que les tâches sont idempotentes ; et tester localement avant de l'exécuter en production.