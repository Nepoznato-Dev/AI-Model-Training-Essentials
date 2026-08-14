<!--
---
# Metadata
title: "Erlang & Elixir — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Erlang and Elixir ecosystem including tools, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [erlang, elixir, ecosystem, tooling, otp, beam, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Erlang & Elixir – Ecossistema e Guia de Ferramentas
Este guia cobre as ferramentas, estruturas e infraestrutura essenciais no ecossistema Erlang e Elixir, compartilhando o BEAM VM e OTP.
---

## Tempo de execução e VM
| Componente | Finalidade |
|-----------|---------|
| **FEIXE** | Máquina virtual Erlang |
| **OTP** | Plataforma Aberta de Telecomunicações (Erlang) |
| **Erlang/OTP** | Tempo de execução Erlang + bibliotecas |
| **Elixir** | Linguagem moderna no BEAM |
```bash
erl -version              # Erlang version
elixir --version          # Elixir version
iex                       # Elixir interactive
erl                       # Erlang interactive
```

---

## Ferramentas de construção
| Ferramenta | Idioma | Finalidade |
|------|----------|--------|
| **Misturar** | Elixir | Ferramenta de construção, executor de tarefas |
| **vergalhão3** | Erlang | Ferramenta de construção, gerenciador de dependências |
| **hexágono** | Ambos | Gerenciador de pacotes |
| **hex.pm** | Ambos | Repositório de pacotes |
```bash
# Elixir / Mix
mix new myapp               # create project
mix deps.get                # install dependencies
mix compile                 # compile
mix test                    # run tests
mix run                     # run application
mix phx.new myapp           # Phoenix project
mix release                 # create release

# Erlang / rebar3
rebar3 new app myapp        # create project
rebar3 get-deps             # install dependencies
rebar3 compile              # compile
rebar3 eunit                # run tests
rebar3 release              # create release
```

```elixir
# mix.exs
defmodule Myapp.MixProject do
  use Mix.Project

  def project do
    [
      app: :myapp,
      version: "0.1.0",
      elixir: "~> 1.16",
      start_permanent: Mix.env() == :prod,
      deps: deps()
    ]
  end

  defp deps do
    [
      {:phoenix, "~> 1.7"},
      {:ecto_sql, "~> 3.11"},
      {:jason, "~> 1.4"},
      {:plug_cowboy, "~> 2.7"}
    ]
  end
end
```

---

## Estruturas Web
| Estrutura | Idioma | Tipo |
|-----------|----------|------|
| **Fênix** | Elixir | Web full-stack (mais popular) |
| **Phoenix LiveView** | Elixir | UI renderizada pelo servidor em tempo real |
| **Bandido** | Elixir | Servidor HTTP Pure-Elixir |
| **Cowboy** | Erlang | Servidor HTTP |
| **Chefe de Chicago** | Erlang | Tipo Django |
| **N2O** | Erlang | Estrutura WebSocket |
```elixir
# Phoenix controller
defmodule MyAppWeb.UserController do
  use MyAppWeb, :controller

  def index(conn, _params) do
    users = Accounts.list_users()
    render(conn, :index, users: users)
  end

  def show(conn, %{"id" => id}) do
    user = Accounts.get_user!(id)
    render(conn, :show, user: user)
  end

  def create(conn, %{"user" => user_params}) do
    case Accounts.create_user(user_params) do
      {:ok, user} ->
        conn |> put_status(:created) |> render(:show, user: user)
      {:error, changeset} ->
        conn |> put_status(:unprocessable_entity) |> render(:error, changeset: changeset)
    end
  end
end
```

---

## Banco de dados
| Tecnologia | Idioma | Tipo |
|------------|----------|------|
| **Ecto** | Elixir | Wrapper de banco de dados + consulta |
| **Pós-grex** | Elixir | Driver PostgreSQL |
| **MeuXQL** | Elixir | Driver MySQL |
| **epgsql** | Erlang | Driver PostgreSQL |
| **Mnésia** | Erlang | Banco de dados distribuído integrado |
| **Riak** | Erlang | Valor-chave distribuído |
| **CouchDB** | Erlang | Banco de dados de documentos |
```elixir
# Ecto schema and query
defmodule MyApp.Accounts.User do
  use Ecto.Schema
  import Ecto.Changeset

  schema "users" do
    field :name, :string
    field :email, :string
    field :age, :integer
    timestamps()
  end

  def changeset(user, attrs) do
    user
    |> cast(attrs, [:name, :email, :age])
    |> validate_required([:name, :email])
    |> validate_format(:email, ~r/@/)
    |> unique_constraint(:email)
  end
end

# Query
import Ecto.Query

users = from(u in User,
  where: u.age > ^min_age,
  order_by: [asc: u.name],
  select: u
)
|> Repo.all()
```

---

## Teste
| Estrutura | Idioma | Finalidade |
|----------|----------|--------|
| **ExUnit** | Elixir | Estrutura de teste integrada |
| **EUunidade** | Erlang | Teste de unidade Erlang |
| **Teste Comum** | Erlang | Estrutura de teste OTP |
| **PropCheck** | Elixir | Baseado em propriedade (QuickCheck) |
| **StreamData** | Elixir | Testes baseados em propriedades |
| **Mox** | Elixir | Zombando |
| **Wallaby** | Elixir | Teste de navegador |
| **ESpec** | Elixir | Estilo BDD |
```elixir
# ExUnit
defmodule MyApp.UserServiceTest do
  use ExUnit.Case, async: true

  describe "find/1" do
    test "returns user when found" do
      user = UserService.find(1)
      assert user.name == "Alice"
    end

    test "raises when not found" do
      assert_raise NotFoundError, fn ->
        UserService.find(999)
      end
    end
  end
end
```

```bash
mix test                    # run tests
mix test --trace            # verbose
mix test test/user_test.exs # specific file
```

---

## Qualidade do código
| Ferramenta | Idioma | Finalidade |
|------|----------|--------|
| **Credo** | Elixir | Linting e estilo |
| **dialixir** | Elixir | Integração do dialisador |
| **Abaixo** | Elixir | Análise de segurança |
| **erlang_ls** | Erlang | Servidor de idiomas |
| **Elvis** | Erlang | Verificador de estilo |
```elixir
# .credo.exs
%{
  configs: [
    %{
      name: "default",
      strict: true,
      checks: [
        {Credo.Check.Readability.MaxLineLength, max_length: 120},
        {Credo.Check.Design.TagTODO, false}
      ]
    }
  ]
}
```

```bash
mix credo                   # lint
mix dialyzer                # type checking
mix sobelow -r .            # security scan
```

---

## Simultaneidade e distribuição
| Recurso | Finalidade |
|--------|---------|
| **Processos** | Leve, isolado |
| **Transmissão de mensagens** | Enviar/receber entre processos |
| **GenServer** | Padrão cliente-servidor |
| **Supervisor** | Tolerância a falhas |
| **Inscrição** | Componente OTP |
| **Distribuição** | Comunicação multinó |
| **Mnésia** | Banco de dados distribuído |
| **libcluster** | Formação de clusters |
| **Horda** | Registro de processos distribuídos |
```elixir
# GenServer example
defmodule UserService do
  use GenServer

  def start_link(_) do
    GenServer.start_link(__MODULE__, %{}, name: __MODULE__)
  end

  def find(id) do
    GenServer.call(__MODULE__, {:find, id})
  end

  @impl true
  def init(state), do: {:ok, state}

  @impl true
  def handle_call({:find, id}, _from, state) do
    case Map.get(state, id) do
      nil -> {:reply, {:error, :not_found}, state}
      user -> {:reply, {:ok, user}, state}
    end
  end
end
```

---

## Bibliotecas principais
| Biblioteca | Idioma | Finalidade |
|--------|----------|---------|
| **Fênix** | Elixir | Estrutura web |
| **Ecto** | Elixir | Banco de dados |
| **Absinto** | Elixir | GráficoQL |
| **Broadway** | Elixir | Pipelines de dados |
| **Oban** | Elixir | Trabalhos em segundo plano |
| **Tesla** | Elixir | Cliente HTTP |
| **Tentilhão** | Elixir | Cliente HTTP |
| **Opções Ágeis** | Elixir | Validação de opções |
| **Tempo** | Elixir | Data/hora |
| **Jasão** | Elixir | JSON |
| **vaqueiro** | Erlang | Servidor HTTP |
| **fazenda** | Erlang | Aceitador de soquete |
| **cerveja** | Erlang | Registro |
| **jsx** | Erlang | JSON |
---

## IDEs e editores
| IDE | Pontos fortes |
|-----|-----------|
| **Código VS + ElixirLS** | Melhor suporte Elixir |
| **IntelliJ + Elixir** | Suporte JetBrains |
| **Vim + alquimista.vim** | Elixir Vim |
| **Emacs + modo erlang** | Erlang Clássico |
---

## Implantação
| Método | Notas |
|-------|-------|
| **Lançamento da mistura** | Liberação independente |
| **Docker** | Contentorizado |
| **Gigalixir** | Elixir PaaS |
| **Fly.io** | Hospedagem distribuída |
| **Renderizar** | Hospedagem de aplicativos |
| **Lançamento Erlang** | Lançamento OTP |
| **Atualização de código quente** | Atualizações sem tempo de inatividade |
---

## Resumo
Erlang e Elixir compartilham BEAM VM e OTP, oferecendo simultaneidade e tolerância a falhas incomparáveis. A pilha Elixir padrão é: **Mix** para compilações, **Phoenix** para web, **Phoenix LiveView** para UI em tempo real, **Ecto** para bancos de dados, **ExUnit** para testes, **Credo** para linting e **Oban** para trabalhos em segundo plano. Erlang usa **rebar3** para compilações, **Cowboy** para HTTP e **EUnit** ou **Common Test** para testes. Ambas as linguagens são excelentes em sistemas distribuídos, aplicações em tempo real (chat, jogos, IoT), telecomunicações e serviços de alta disponibilidade. Os pontos fortes do ecossistema são a filosofia “deixe travar”, atualizações de código a quente, processos leves e passagem de mensagens.