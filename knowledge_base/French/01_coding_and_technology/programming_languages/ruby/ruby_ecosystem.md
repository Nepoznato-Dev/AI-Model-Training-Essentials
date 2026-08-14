<!--
---
# Metadata
title: "Ruby — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Ruby ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [ruby, ecosystem, tooling, rails, gems, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Ruby — Guide de l'écosystème et des outils
Ce guide couvre les outils, frameworks et infrastructures essentiels de l'écosystème Ruby.
---

## Implémentations Ruby
| Mise en œuvre | Remarques |
|---------------|-------|
| **CRuby (IRM)** | Par défaut, le plus largement utilisé |
| **JRuby** | Interopérabilité Java basée sur JVM |
| **TruffeRubis** | Basé sur GraalVM, hautes performances |
| **mruby** | Léger, intégrable |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## Gestion des paquets
| Outil | Objectif |
|------|--------------|
| **RubyGems** | Gestionnaire de paquets de gemmes intégré |
| **Regroupeur** | Gestion des dépendances (Gemfile) |
| **rubygems.org** | Dépôt officiel de gemmes |
```ruby
# Gemfile
source "https://rubygems.org"

gem "rails", "~> 7.1"
gem "pg", "~> 1.5"
gem "puma", "~> 6.0"
gem "redis", "~> 5.0"

group :development, :test do
  gem "rspec", "~> 3.12"
  gem "rubocop", "~> 1.50"
  gem "debug"
end
```

```bash
bundle install          # install dependencies
bundle update           # update gems
bundle exec rspec       # run with bundled gems
```

---

## Cadres Web
| Cadre | Tapez | Idéal pour |
|---------------|------|--------------|
| **Rails** | Pile complète | Convention sur la configuration |
| **Sinatra** | Micro | API simples, petites applications |
| **Hanami** | Arc propre. | Applications maintenables et testables |
| **Roda** | Arbre de routage | Haute performance, flexibilité |
| **Raisin** | API REST | Framework axé sur les API |
| **Support** | Interfaces | Interface du serveur Web de bas niveau |
```ruby
# Sinatra example
require "sinatra"

get "/hello" do
  "Hello, #{params[:name] || 'World'}!"
end

get "/users/:id" do
  user = User.find(params[:id])
  json user
end
```

```ruby
# Rails controller example
class UsersController < ApplicationController
  def index
    @users = User.order(:name).page(params[:page])
    render json: @users
  end

  def create
    @user = User.new(user_params)
    if @user.save
      render json: @user, status: :created
    else
      render json: @user.errors, status: :unprocessable_entity
    end
  end
end
```

---

## Base de données et ORM
| Technologie | Tapez |
|------------|------|
| **Enregistrement actif** | Rails ORM (basé sur des conventions) |
| **Suite** | ORM flexible et puissant |
| **ROM (Mappeur d'objets Ruby)** | Fonctionnel, composable |
| **page** | Adaptateur PostgreSQL |
| **mysql2** | Adaptateur MySQL |
| **SQLite3** | Adaptateur SQLite |
| **Mongoide** | MongoDB ODM |
| **Redis** | Magasin clé-valeur |
---

## Tests
| Cadre | Objectif |
|-----------|---------|
| **RSpec** | Tests de style BDD (les plus populaires) |
| **Minitest** | Intégré, léger |
| **Capybara** | Tests d'intégration/navigateur |
| **FactoryBot** | Usines de données de test |
| **Faux** | Génération de fausses données |
| **WebMock** | Stubbing de requête HTTP |
| **SimpleCov** | Couverture du code |
| **Magnétoscope** | Enregistrer/rejouer les interactions HTTP |
| **Timecop** | Manipulation du temps dans les tests |
```ruby
# RSpec example
RSpec.describe UserService do
  subject(:service) { described_class.new(repository) }

  describe "#find" do
    it "returns the user when found" do
      user = build(:user, name: "Alice")
      allow(repository).to receive(:find).with(1).and_return(user)

      result = service.find(1)

      expect(result.name).to eq("Alice")
    end

    it "raises NotFound when missing" do
      allow(repository).to receive(:find).and_raise(NotFound)

      expect { service.find(999) }.to raise_error(NotFound)
    end
  end
end
```

---

## Qualité du code
| Outil | Objectif |
|------|--------------|
| **RuboCop** | Linter et formateur |
| **StandardRB** | Configuration RuboCop avisée |
| **Puant** | Détection d'odeur de code |
| **Breineur** | Scanner de vulnérabilités de sécurité |
| **Audit-Bundler** | Vérificateur de vulnérabilité de gemme |
| **SimpleCov** | Couverture du code |
| **Graphique solaire** | Serveur de langue, documents YARD |
```yaml
# .rubocop.yml
AllCops:
  TargetRubyVersion: 3.3
  NewCops: enable

Style/Documentation:
  Enabled: false

Layout/LineLength:
  Max: 120
```

---

## Exécuteurs de tâches et CLI
| Outil | Objectif |
|------|--------------|
| **Râteau** | Exécuteur de tâches (Make-like) |
| **Thor** | Cadre CLI |
| **Console Rails** | Environnement Rails interactif |
| **Thor** | Créez de puissants outils CLI |
| **Dryrun** | Tester les CLI de gem |
---

## Bibliothèques clés
| Bibliothèque | Objectif |
|---------|---------|
| **Rails** | Framework Web complet |
| **Sidekiq** | Traitement des tâches en arrière-plan |
| **Concevoir** | Authentification |
| ** Expert ** | Autorisation |
| **Puma** | Serveur Web |
| **Support** | Interface du serveur Web |
| **Nokogiri** | Analyse HTML/XML |
| **Faraday** | Client HTTP |
| **httppartie** | Requêtes HTTP simples |
| **Support actif** | Classes utilitaires (Rails) |
| **Sec-rb** | Bibliothèques Ruby fonctionnelles |
| **Hanami::Utils** | Utilitaires légers |
| **Levier** | Console développeur / débogueur |
| **dotenv** | Variables d'environnement |
| **figaro** | Configuration de l'application |
---

## IDE et éditeurs
| EDI | Points forts |
|-----|-----------|
| **RubyMine** | IDE JetBrains Ruby complet |
| **Code VS + Graphique solaire** | Léger, basé sur LSP |
| **Vim/Neovim + ruby-lsp** | Basé sur un terminal |
| **TexteMate** | Éditeur macOS classique |
---

## Déploiement
| Méthode | Remarques |
|--------|-------|
| **Puma** | Serveur Web Rails par défaut |
| **Passager** | Module Apache/Nginx |
| **Capistrano** | Déploiement multi-serveur à distance |
| **Docker** | Déploiement conteneurisé |
| **Héroku** | PaaS (compatible avec Ruby) |
| **Fly.io** | Plateforme d'hébergement d'applications |
| **Chemin de fer** | PaaS moderne |
| **Kamal (camp de base)** | Déploiement basé sur Docker |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## Résumé
L'écosystème de Ruby se concentre sur le bonheur des développeurs et les conventions en matière de configuration. La pile standard est : **Ruby 3.3+** comme environnement d'exécution, **Bundler** pour les dépendances, **Rails** pour le Web full-stack (ou **Sinatra** pour les micro-applications), **RSpec** pour les tests, **RuboCop** pour le peluchage, **Sidekiq** pour les tâches en arrière-plan et **Puma** comme serveur Web. Ruby excelle dans le prototypage rapide, les applications Web, les scripts et les outils CLI. L'écosystème RubyGems compte plus de 170 000 packages. Ruby 3.x apporte Ractors pour la concurrence, RBS pour le typage statique et la correspondance de modèles.