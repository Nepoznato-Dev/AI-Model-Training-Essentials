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
# Erlang & Elixir — 생태계 및 툴링 가이드
이 가이드에서는 BEAM VM과 OTP를 공유하는 Erlang 및 Elixir 생태계의 필수 도구, 프레임워크 및 인프라를 다룹니다.
---

## 런타임 및 VM
| 구성요소 | 목적 |
|------------|---------|
| **빔** | 얼랭 가상 머신 |
| **OTP** | 개방형 통신 플랫폼(Erlang) |
| **얼랭/OTP** | Erlang 런타임 + 라이브러리 |
| **엘릭서** | BEAM의 현대 언어 |
```bash
erl -version              # Erlang version
elixir --version          # Elixir version
iex                       # Elixir interactive
erl                       # Erlang interactive
```

---

## 빌드 도구
| 도구 | 언어 | 목적 |
|------|----------|---------|
| **믹스** | 엘릭서 | 빌드 도구, 작업 실행기 |
| **철근3** | 얼랭 | 빌드 도구, 종속성 관리자 |
| **16진수** | 둘 다 | 패키지 관리자 |
| **hex.pm** | 둘 다 | 패키지 저장소 |
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

## 웹 프레임워크
| 프레임워크 | 언어 | 유형 |
|------------|----------|------|
| **피닉스** | 엘릭서 | 풀스택 웹(가장 인기 있음) |
| **피닉스 라이브뷰** | 엘릭서 | 실시간 서버 렌더링 UI |
| **산적** | 엘릭서 | Pure-Elixir HTTP 서버 |
| **카우보이** | 얼랭 | HTTP 서버 |
| **시카고 보스** | 얼랭 | 장고와 유사한 |
| **N2O** | 얼랭 | WebSocket 프레임워크 |
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

## 데이터베이스
| 기술 | 언어 | 유형 |
|------------|----------|------|
| **엑토** | 엘릭서 | 데이터베이스 래퍼 + 쿼리 |
| **포스트그렉스** | 엘릭서 | PostgreSQL 드라이버 |
| **MyXQL** | 엘릭서 | MySQL 드라이버 |
| **epgsql** | 얼랭 | PostgreSQL 드라이버 |
| **기억 상실증** | 얼랭 | 분산 DB 내장 |
| **리악** | 얼랭 | 분산 키-값 |
| **카우치DB** | 얼랭 | 문서 데이터베이스 |
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

## 테스트
| 프레임워크 | 언어 | 목적 |
|------------|----------|---------|
| **엑유닛** | 엘릭서 | 내장된 테스트 프레임워크 |
| **EU단위** | 얼랭 | Erlang 단위 테스트 |
| **공통 테스트** | 얼랭 | OTP 테스트 프레임워크 |
| **PropCheck** | 엘릭서 | 속성 기반(QuickCheck) |
| **스트림데이터** | 엘릭서 | 속성 기반 테스트 |
| **목스** | 엘릭서 | 조롱 |
| **왈라비** | 엘릭서 | 브라우저 테스트 |
| **에스펙** | 엘릭서 | BDD 스타일 |
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

## 코드 품질
| 도구 | 언어 | 목적 |
|------|----------|---------|
| **신조** | 엘릭서 | 린팅 및 스타일 |
| **디알릭시르** | 엘릭서 | 투석기 통합 |
| **아래** | 엘릭서 | 보안 분석 |
| **erlang_ls** | 얼랭 | 언어 서버 |
| **엘비스** | 얼랭 | 스타일 검사기 |
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

## 동시성 및 배포
| 기능 | 목적 |
|---------|---------|
| **프로세스** | 경량, 절연 |
| **메시지 전달** | 프로세스 간 보내기/받기 |
| **젠서버** | 클라이언트-서버 패턴 |
| **감독자** | 내결함성 |
| **신청** | OTP 구성요소 |
| **배포** | 다중 노드 통신 |
| **기억 상실증** | 분산 데이터베이스 |
| **libcluster** | 클러스터 형성 |
| **호드** | 분산 프로세스 레지스트리 |
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

## 주요 라이브러리
| 도서관 | 언어 | 목적 |
|---------|----------|---------|
| **피닉스** | 엘릭서 | 웹 프레임워크 |
| **엑토** | 엘릭서 | 데이터베이스 |
| **압생트** | 엘릭서 | GraphQL |
| **브로드웨이** | 엘릭서 | 데이터 파이프라인 |
| **오반** | 엘릭서 | 백그라운드 작업 |
| **테슬라** | 엘릭서 | HTTP 클라이언트 |
| **핀치** | 엘릭서 | HTTP 클라이언트 |
| **민첩한 옵션** | 엘릭서 | 옵션 검증 |
| **타이멕스** | 엘릭서 | 날짜/시간 |
| **제이슨** | 엘릭서 | JSON |
| **카우보이** | 얼랭 | HTTP 서버 |
| **목장** | 얼랭 | 소켓 수용체 |
| **라거** | 얼랭 | 로깅 |
| **jsx** | 얼랭 | JSON |
---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **VS 코드 + ElixirLS** | 최고의 엘릭서 지원 |
| **IntelliJ + 엘릭서** | JetBrains 지원 |
| **Vim + alchemist.vim** | 빔 엘릭서 |
| **Emacs + 얼랭 모드** | 클래식 얼랭 |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **믹스 릴리스** | 독립형 릴리스 |
| **도커** | 컨테이너화 |
| **기가릭시르** | 엘릭서 PaaS |
| **플라이.io** | 분산 호스팅 |
| **렌더링** | 앱 호스팅 |
| **Erlang 릴리스** | OTP 출시 |
| **핫 코드 업그레이드** | 다운타임 없는 업그레이드 |
---

## 요약
Erlang과 Elixir는 BEAM VM과 OTP를 공유하여 비교할 수 없는 동시성과 내결함성을 제공합니다. 표준 Elixir 스택은 빌드용 **Mix**, 웹용 **Phoenix**, 실시간 UI용 **Phoenix LiveView**, 데이터베이스용 **Ecto**, 테스트용 **ExUnit**, Linting용 **Credo**, 백그라운드 작업용 **Oban**입니다. Erlang은 빌드에 **rebar3**, HTTP에 **Cowboy**, 테스트에 **EUnit** 또는 **Common Test**를 사용합니다. 두 언어 모두 분산 시스템, 실시간 애플리케이션(채팅, 게임, IoT), 통신 및 고가용성 서비스에 탁월합니다. 생태계의 강점은 "Let it crash" 철학, 핫 코드 업그레이드, 경량 프로세스 및 메시지 전달입니다.