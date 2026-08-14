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

# Ruby — Ecossistema e Guia de Ferramentas
Este guia cobre as ferramentas, estruturas e infraestrutura essenciais do ecossistema Ruby.
---

## Implementações Ruby
| Implementação | Notas |
|---------------|-------|
| **CRuby (ressonância magnética)** | Padrão, mais utilizado |
| **JRuby** | Interoperabilidade Java baseada em JVM |
| **TrufaRuby** | Baseado em GraalVM, alto desempenho |
| **mruby** | Leve, incorporável |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## Gerenciamento de pacotes
| Ferramenta | Finalidade |
|------|---------|
| **RubyGems** | Gerenciador de pacotes gem integrado |
| **Pacote** | Gerenciamento de dependências (Gemfile) |
| **rubygems.org** | Repositório oficial de gemas |
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

## Estruturas Web
| Estrutura | Tipo | Melhor para |
|-----------|------|----------|
| **Trilhos** | Pilha completa | Convenção sobre configuração |
| **Sinatra** | Micro | APIs simples, aplicativos pequenos |
| **Hanami** | Arco limpo. | Aplicativos passíveis de manutenção e testáveis ​​|
| **Roda** | Árvore de roteamento | Alto desempenho, flexível |
| **Uva** | API REST | Estrutura focada em API |
| **Rack** | Interface | Interface de servidor web de baixo nível |
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

## Banco de dados e ORM
| Tecnologia | Tipo |
|------------|------|
| **Registro Ativo** | Rails ORM (baseado em convenção) |
| **Sequela** | ORM flexível e poderoso |
| **ROM (Mapeador de Objetos Ruby)** | Funcional, combinável |
| **pág.** | Adaptador PostgreSQL |
| **mysql2** | Adaptador MySQL |
| **SQLite3** | Adaptador SQLite |
| **Mongóide** | ODM do MongoDB |
| **Redes** | Armazenamento de valor-chave |
---

## Teste
| Estrutura | Finalidade |
|-----------|---------|
| **RSpec** | Teste estilo BDD (mais popular) |
| **Miniteste** | Integrado, leve |
| **Capivara** | Teste de integração/navegador |
| **FactoryBot** | Fábricas de dados de teste |
| **Falsificador** | Geração de dados falsos |
| **WebMock** | stub de solicitação HTTP |
| **SimpleCov** | Cobertura de código |
| **VCR** | Gravar/reproduzir interações HTTP |
| **Timecop** | Manipulação de tempo em testes |
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

## Qualidade do código
| Ferramenta | Finalidade |
|------|---------|
| **RuboCop** | Linter e formatador |
| **PadrãoRB** | Configuração opinativa do RuboCop |
| **Fedorento** | Detecção de cheiro de código |
| **Freio** | Verificador de vulnerabilidade de segurança |
| **Auditoria de pacote** | Verificador de vulnerabilidade de gemas |
| **SimpleCov** | Cobertura de código |
| **Sológrafo** | Servidor de idiomas, documentos YARD |
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

## Executores de tarefas e CLI
| Ferramenta | Finalidade |
|------|---------|
| **Ancinho** | Executor de tarefas (Make-like) |
| **Thor** | Estrutura CLI |
| **Console de trilhos** | Ambiente Rails interativo |
| **Thor** | Crie ferramentas CLI poderosas |
| **Teste** | Testar CLIs de gemas |
---

## Bibliotecas principais
| Biblioteca | Finalidade |
|--------|---------|
| **Trilhos** | Estrutura web full-stack |
| **Sidekiq** | Processamento de trabalho em segundo plano |
| **Desenvolver** | Autenticação |
| **Especialista** | Autorização |
| **Puma** | Servidor web |
| **Rack** | Interface do servidor web |
| **Nokogiri** | Análise HTML/XML |
| **Faraday** | Cliente HTTP |
| **httpfesta** | Solicitações HTTP simples |
| **Suporte Ativo** | Classes utilitárias (trilhos) |
| **Rb seco** | Bibliotecas funcionais Ruby |
| **Hanami::Utilitários** | Utilitários leves |
| **Insistir** | Console do desenvolvedor/depurador |
| **dotenv** | Variáveis ​​de ambiente |
| **fígaro** | Configuração do aplicativo |
---

## IDEs e editores
| IDE | Pontos fortes |
|-----|-----------|
| **RubyMine** | IDE JetBrains Ruby completo |
| **Código VS + Solargraph** | Leve, baseado em LSP |
| **Vim/Neovim + ruby-lsp** | Baseado em terminal |
| **TextMate** | Editor clássico do macOS |
---

## Implantação
| Método | Notas |
|-------|-------|
| **Puma** | Servidor web Rails padrão |
| **Passageiro** | Módulo Apache/Nginx |
| **Capistrano** | Implantação remota de vários servidores |
| **Docker** | Implantação em contêineres |
| **Heroku** | PaaS (compatível com Ruby) |
| **Fly.io** | Plataforma de hospedagem de aplicativos |
| **Ferrovia** | PaaS moderna |
| **Kamal (campo base)** | Implantação baseada em Docker |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## Resumo
O ecossistema do Ruby centra-se na felicidade do desenvolvedor e nas convenções sobre a configuração. A pilha padrão é: **Ruby 3.3+** como tempo de execução, **Bundler** para dependências, **Rails** para web full-stack (ou **Sinatra** para microaplicativos), **RSpec** para testes, **RuboCop** para linting, **Sidekiq** para trabalhos em segundo plano e **Puma** como servidor web. Ruby é excelente em prototipagem rápida, aplicações web, scripts e ferramentas CLI. O ecossistema RubyGems possui mais de 170.000 pacotes. Ruby 3.x traz Ractors para simultaneidade, RBS para digitação estática e correspondência de padrões.