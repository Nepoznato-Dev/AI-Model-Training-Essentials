---
# Metadata
title: "Ruby — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Ruby ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Ruby: guía de ecosistemas y herramientas
Esta guía cubre las herramientas, los marcos y la infraestructura esenciales en el ecosistema Ruby.
---

## Implementaciones de Ruby
| Implementación | Notas |
|---------------|-------|
| **CRubí (MRI)** | Predeterminado, el más utilizado |
| **JRubí** | Interoperabilidad Java basada en JVM |
| **TrufaRubí** | Basado en GraalVM, alto rendimiento |
| **mrubí** | Ligero, integrable |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## Gestión de paquetes
| Herramienta | Propósito |
|------|---------|
| **RubíGemas** | Administrador de paquetes de gemas incorporado |
| **Paquete** | Gestión de dependencias (Gemfile) |
| **rubygems.org** | Repositorio oficial de gemas |
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

## Marcos web
| Marco | Tipo | Mejor para |
|-----------|------|----------|
| **Rieles** | Pila completa | Convención sobre configuración |
| **Sinatra** | micro | API simples, aplicaciones pequeñas |
| **Hanami** | Arco limpio. | Aplicaciones mantenibles y comprobables |
| **Roda** | Árbol de enrutamiento | Alto rendimiento, flexible |
| **Uva** | API REST | Marco centrado en API |
| **Estante** | Interfaz | Interfaz de servidor web de bajo nivel |
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

## Base de datos y ORM
| Tecnología | Tipo |
|------------|------|
| **Registro activo** | Rails ORM (basado en convenciones) |
| **Secuela** | ORM flexible y potente |
| **ROM (Mapeador de objetos Ruby)** | Funcional, componible |
| **página** | Adaptador PostgreSQL |
| **mysql2** | Adaptador MySQL |
| **SQLite3** | Adaptador SQLite |
| **Mongoide** | MongoDB ODM |
| **Redis** | Tienda de valores clave |
---

## Pruebas
| Marco | Propósito |
|-----------|------------------|
| **REspecificación** | Pruebas estilo BDD (más populares) |
| **Miniprueba** | Incorporado, ligero |
| **Carpincho** | Integración/pruebas del navegador |
| **Bot de fábrica** | Fábricas de datos de prueba |
| **Falso** | Generación de datos falsos |
| **WebMock** | Trozo de solicitud HTTP |
| **SimpleCov** | Cobertura de código |
| **VCR** | Grabar/reproducir interacciones HTTP |
| **Policía del tiempo** | Manipulación del tiempo en las pruebas |
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

## Calidad del código
| Herramienta | Propósito |
|------|---------|
| **RuboCop** | Linter y formateador |
| **EstándarRB** | Configuración obstinada de RuboCop |
| **Apesta** | Detección de olores de código |
| **Reparador** | Escáner de vulnerabilidades de seguridad |
| **Auditoría de paquetes** | Comprobador de vulnerabilidad de gemas |
| **SimpleCov** | Cobertura de código |
| **Solarógrafo** | Servidor de idiomas, documentos YARD |
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

## Ejecutores de tareas y CLI
| Herramienta | Propósito |
|------|---------|
| **Rastrillo** | Ejecutor de tareas (Make-like) |
| **Thor** | Marco CLI |
| **Consola de rieles** | Entorno de rieles interactivos |
| **Thor** | Cree potentes herramientas CLI |
| **Ejecución en seco** | Pruebe las CLI de gemas |
---

## Bibliotecas clave
| Biblioteca | Propósito |
|---------|---------|
| **Rieles** | Marco web de pila completa |
| **Compañero** | Procesamiento de trabajos en segundo plano |
| **Diseñar** | Autenticación |
| **Experto** | Autorización |
| **Puma** | Servidor web |
| **Estante** | Interfaz del servidor web |
| **Nokogiri** | Análisis HTML/XML |
| **Faraday** | Cliente HTTP |
| **httppartido** | Solicitudes HTTP simples |
| **Soporte activo** | Clases de servicios públicos (rieles) |
| **rb seco** | Bibliotecas funcionales de Ruby |
| **Hanami::Utilidades** | Utilidades ligeras |
| **Hacer palanca** | Consola de desarrollador/depurador |
| **dotenv** | Variables de entorno |
| **fígaro** | Configuración de la aplicación |
---

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **RubíMina** | IDE completo de JetBrains Ruby |
| **Código VS + Solargraph** | Ligero, basado en LSP |
| **Vim/Neovim + rubí-lsp** | Basado en terminal |
| **TextMate** | Editor clásico de macOS |
---

## Implementación
| Método | Notas |
|--------|-------|
| **Puma** | Servidor web Rails predeterminado |
| **Pasajero** | Módulo Apache/Nginx |
| **Capistrano** | Implementación remota de múltiples servidores |
| **Acoplador** | Implementación en contenedores |
| **Heroku** | PaaS (compatible con Ruby) |
| **Fly.io** | Plataforma de alojamiento de aplicaciones |
| **Ferrocarril** | PaaS moderna |
| **Kamal (campamento base)** | Implementación basada en Docker |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## Resumen
El ecosistema de Ruby se centra en la felicidad de los desarrolladores y en las convenciones sobre la configuración. La pila estándar es: **Ruby 3.3+** como tiempo de ejecución, **Bundler** para dependencias, **Rails** para web de pila completa (o **Sinatra** para microaplicaciones), **RSpec** para pruebas, **RuboCop** para linting, **Sidekiq** para trabajos en segundo plano y **Puma** como servidor web. Ruby se destaca en la creación rápida de prototipos, aplicaciones web, secuencias de comandos y herramientas CLI. El ecosistema RubyGems tiene más de 170.000 paquetes. Ruby 3.x ofrece Ractors para concurrencia, RBS para escritura estática y coincidencia de patrones.