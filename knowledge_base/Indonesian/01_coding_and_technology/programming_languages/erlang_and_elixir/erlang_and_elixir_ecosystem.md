---
# Metadata
title: "Erlang & Elixir — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Erlang and Elixir ecosystem including tools, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Erlang & Elixir — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, kerangka kerja, dan infrastruktur penting dalam ekosistem Erlang dan Elixir, serta berbagi BEAM VM dan OTP.
---

## Waktu Proses & VM
| Komponen | Tujuan |
|-----------|---------|
| **BALOK** | Mesin virtual Erlang |
| **OTP** | Buka Platform Telekomunikasi (Erlang) |
| **Erlang/OTP** | Runtime Erlang + perpustakaan |
| **Ramuan** | Bahasa modern di BEAM |
```bash
erl -version              # Erlang version
elixir --version          # Elixir version
iex                       # Elixir interactive
erl                       # Erlang interactive
```

---

## Alat Bangun
| Alat | Bahasa | Tujuan |
|------|----------|---------|
| **Campur** | Ramuan | Alat bangun, pelari tugas |
| **rebar3** | Erlang | Alat bangun, manajer ketergantungan |
| **hex** | Keduanya | Manajer paket |
| **hex.pm** | Keduanya | Repositori paket |
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

## Kerangka Web
| Kerangka | Bahasa | Ketik |
|-----------|----------|------|
| **Phoenix** | Ramuan | Web tumpukan penuh (paling populer) |
| **Tampilan Langsung Phoenix** | Ramuan | UI yang dirender server secara real-time |
| **Bandit** | Ramuan | Server HTTP Ramuan Murni |
| **Koboi** | Erlang | Server HTTP |
| **Bos Chicago** | Erlang | Seperti Django |
| **N2O** | Erlang | Kerangka kerja WebSocket |
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

## Basis Data
| Teknologi | Bahasa | Ketik |
|------------|----------|------|
| **Ekto** | Ramuan | Pembungkus basis data + kueri |
| **Postgrex** | Ramuan | Pengandar PostgreSQL |
| **MyXQL** | Ramuan | Pengandar MySQL |
| **epgsql** | Erlang | Pengandar PostgreSQL |
| **Mnesia** | Erlang | DB terdistribusi bawaan |
| **Riak** | Erlang | Nilai kunci terdistribusi |
| **CouchDB** | Erlang | Basis data dokumen |
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

## Pengujian
| Kerangka | Bahasa | Tujuan |
|-----------|----------|---------|
| **ExUnit** | Ramuan | Kerangka pengujian bawaan |
| **Unit** | Erlang | Pengujian unit Erlang |
| **Tes Umum** | Erlang | Kerangka pengujian OTP |
| **Pemeriksaan Prop** | Ramuan | Berbasis properti (QuickCheck) |
| **Data Aliran** | Ramuan | Pengujian berbasis properti |
| **Moks** | Ramuan | Mengejek |
| **Wallaby** | Ramuan | Pengujian peramban |
| **ESpesifikasi** | Ramuan | Gaya BDD |
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

## Kualitas Kode
| Alat | Bahasa | Tujuan |
|------|----------|---------|
| **Kredo** | Ramuan | Linting dan gaya |
| **dialiksir** | Ramuan | Integrasi dialyzer |
| **Jadi di bawah** | Ramuan | Analisis keamanan |
| **erlang_ls** | Erlang | Server bahasa |
| **elvis** | Erlang | Pemeriksa gaya |
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

## Konkurensi & Distribusi
| Fitur | Tujuan |
|---------|---------|
| **Proses** | Ringan, terisolasi |
| **Pesan lewat** | Kirim/terima antar proses |
| **GenServer** | Pola klien-server |
| **Pengawas** | Toleransi kesalahan |
| **Aplikasi** | Komponen OTP |
| **Distribusi** | Komunikasi multi-node |
| **Mnesia** | Basis data terdistribusi |
| **libcluster** | Pembentukan klaster |
| **Gerombolan** | Registri proses terdistribusi |
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

## Perpustakaan Utama
| Perpustakaan | Bahasa | Tujuan |
|---------|----------|---------|
| **Phoenix** | Ramuan | Kerangka web |
| **Ekto** | Ramuan | Basis Data |
| **Absinth** | Ramuan | GrafikQL |
| **Broadway** | Ramuan | Saluran data |
| **Oban** | Ramuan | Pekerjaan latar belakang |
| **Tesla** | Ramuan | Klien HTTP |
| **Burung Kutilang** | Ramuan | Klien HTTP |
| **Opsi Cekatan** | Ramuan | Validasi opsi |
| **Waktu** | Ramuan | Tanggal/waktu |
| **Jason** | Ramuan | JSON |
| **koboi** | Erlang | Server HTTP |
| **peternakan** | Erlang | Akseptor soket |
| **bir** | Erlang | Pencatatan |
| **jsx** | Erlang | JSON |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **Kode VS + RamuanLS** | Dukungan Elixir terbaik |
| **IntelliJ + Ramuan** | Dukungan JetBrain |
| **Vim + alkemis.vim** | Obat mujarab vim |
| **Emacs + mode erlang** | Erlang Klasik |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Rilis campuran** | Rilis mandiri |
| **Buruh pelabuhan** | dalam kontainer |
| **Gigalixir** | Ramuan PaaS |
| **Terbang.io** | Hosting terdistribusi |
| **Render** | Hosting aplikasi |
| **Rilis Erlang** | Rilis OTP |
| **Peningkatan kode terbaru** | Peningkatan tanpa waktu henti |
---

## Ringkasan
Erlang dan Elixir berbagi BEAM VM dan OTP, menawarkan konkurensi dan toleransi kesalahan yang tak tertandingi. Tumpukan Elixir standar adalah: **Mix** untuk build, **Phoenix** untuk web, **Phoenix LiveView** untuk UI real-time, **Ecto** untuk database, **ExUnit** untuk pengujian, **Credo** untuk linting, dan **Oban** untuk pekerjaan latar belakang. Erlang menggunakan **rebar3** untuk build, **Cowboy** untuk HTTP, dan **EUnit** atau **Common Test** untuk pengujian. Kedua bahasa tersebut unggul dalam sistem terdistribusi, aplikasi real-time (obrolan, game, IoT), telekomunikasi, dan layanan ketersediaan tinggi. Kekuatan ekosistem ini adalah filosofi "biarkan crash", peningkatan kode terbaru, proses yang ringan, dan penyampaian pesan.