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
# Erlang ve İksir — Ekosistem ve Araç İşleme Kılavuzu
Bu kılavuz, BEAM VM ve OTP'yi paylaşan Erlang ve Elixir ekosistemindeki temel araçları, çerçeveleri ve altyapıyı kapsar.
---

## Çalışma Zamanı ve VM
| Bileşen | Amaç |
|-----------|------------|
| **KİRİŞ** | Erlang sanal makinesi |
| **OTP** | Açık Telekom Platformu (Erlang) |
| **Erlang/OTP** | Erlang çalışma zamanı + kitaplıklar |
| **İksir** | BEAM'de modern dil |
```bash
erl -version              # Erlang version
elixir --version          # Elixir version
iex                       # Elixir interactive
erl                       # Erlang interactive
```

---

## Oluşturma Araçları
| Araç | Dil | Amaç |
|------|----------|-----------|
| **Karıştır** | İksir | Derleme aracı, görev çalıştırıcısı |
| **inşaat demiri3** | Erlang | Derleme aracı, bağımlılık yöneticisi |
| **altıgen** | Her ikisi de | Paket yöneticisi |
| **hex.pm** | Her ikisi de | Paket deposu |
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

## Web Çerçeveleri
| Çerçeve | Dil | Tür |
|-----------|----------|------|
| **Anka Kuşu** | İksir | Tam yığın web (en popüler) |
| **Phoenix LiveView** | İksir | Gerçek zamanlı sunucu tarafından oluşturulan kullanıcı arayüzü |
| **Haydut** | İksir | Pure-İksir HTTP sunucusu |
| **Kovboy** | Erlang | HTTP sunucusu |
| **Chicago Patronu** | Erlang | Django benzeri |
| **N2O** | Erlang | WebSocket çerçevesi |
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

## Veritabanı
| Teknoloji | Dil | Tür |
|---------------|----------|------|
| **Ekto** | İksir | Veritabanı sarmalayıcı + sorgu |
| **Postgrex** | İksir | PostgreSQL sürücüsü |
| **MyXQL** | İksir | MySQL sürücüsü |
| **epgsql** | Erlang | PostgreSQL sürücüsü |
| **Mnesia** | Erlang | Yerleşik dağıtılmış veritabanı |
| **Riak** | Erlang | Dağıtılmış anahtar/değer çifti |
| **KanepeDB** | Erlang | Belge veritabanı |
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

## Test etme
| Çerçeve | Dil | Amaç |
|-----------|----------|-----------|
| **ExUnit** | İksir | Yerleşik test çerçevesi |
| **ABbirimi** | Erlang | Erlang birim testi |
| **Ortak Test** | Erlang | OTP test çerçevesi |
| **PropCheck** | İksir | Özellik tabanlı (HızlıKontrol) |
| **Veri Akışı** | İksir | Mülkiyet bazlı testler |
| **Mox** | İksir | Alaycı |
| **Vallaby** | İksir | Tarayıcı testi |
| **ESpec** | İksir | BDD tarzı |
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

## Kod Kalitesi
| Araç | Dil | Amaç |
|------|----------|-----------|
| **İnanç** | İksir | Linting ve stil |
| **dialiksir** | İksir | Diyalizör entegrasyonu |
| **Aşağıda** | İksir | Güvenlik analizi |
| **erlang_ls** | Erlang | Dil sunucusu |
| **elvis** | Erlang | Stil denetleyicisi |
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

## Eşzamanlılık ve Dağıtım
| Özellik | Amaç |
|-----------|-----------|
| **Süreçler** | Hafif, yalıtılmış |
| **Mesaj aktarımı** | İşlemler arasında gönder/al |
| **GenServer** | İstemci-sunucu modeli |
| **Danışman** | Hata toleransı |
| **Uygulama** | OTP bileşeni |
| **Dağıtım** | Çok düğümlü iletişim |
| **Mnesia** | Dağıtılmış veritabanı |
| **libcluster** | Küme oluşumu |
| **Sürü** | Dağıtılmış işlem kaydı |
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

## Anahtar Kitaplıklar
| Kütüphane | Dil | Amaç |
|-----------|----------|-----------|
| **Anka Kuşu** | İksir | Web çerçevesi |
| **Ekto** | İksir | Veritabanı |
| **Absinthe** | İksir | GraphQL |
| **Broadway** | İksir | Veri hatları |
| **Oban** | İksir | Arka plan işleri |
| **Tesla** | İksir | HTTP istemcisi |
| **İspinoz** | İksir | HTTP istemcisi |
| **NimbleOptions** | İksir | Seçenek doğrulama |
| **Timex** | İksir | Tarih/saat |
| **Jason** | İksir | JSON |
| **kovboy** | Erlang | HTTP sunucusu |
| **çiftlik** | Erlang | Soket alıcısı |
| **bira** | Erlang | Günlük |
| **jsx** | Erlang | JSON |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **VS Kodu + ElixirLS** | En İyi İksir desteği |
| **IntelliJ + Elixir** | JetBrains desteği |
| **Vim + alchemist.vim** | Vim İksiri |
| **Emacs + erlang modu** | Klasik Erlang |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Karışık sürüm** | Bağımsız sürüm |
| **Docker** | Konteynerde |
| **Gigalixir** | İksir PaaS |
| **Fly.io** | Dağıtılmış barındırma |
| **Oluşturma** | Uygulama barındırma |
| **Erlang sürümü** | OTP sürümü |
| **Sıcak kod yükseltmesi** | Sıfır kesinti süreli yükseltmeler |
---

## Özet
Erlang ve Elixir, benzersiz eşzamanlılık ve hata toleransı sunan BEAM VM ve OTP'yi paylaşıyor. Standart Elixir yığını şu şekildedir: Derlemeler için **Mix**, web için **Phoenix**, gerçek zamanlı kullanıcı arayüzü için **Phoenix LiveView**, veritabanları için **Ecto**, test için **ExUnit**, linting için **Credo** ve arka plan işleri için **Oban**. Erlang, derlemeler için **rebar3**, HTTP için **Cowboy** ve test için **EUnit** veya **Common Test** kullanıyor. Her iki dil de dağıtılmış sistemlerde, gerçek zamanlı uygulamalarda (sohbet, oyun, IoT), telekom ve yüksek kullanılabilirlik hizmetlerinde mükemmeldir. Ekosistemin güçlü yönleri "bırakın çöksün" felsefesi, sıcak kod yükseltmeleri, hafif süreçler ve mesaj aktarımıdır.