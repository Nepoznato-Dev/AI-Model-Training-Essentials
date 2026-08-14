---
# Metadata
title: "Erlang & Elixir — Version History & Evolution"
description: "Comprehensive version history and evolution of Erlang and Elixir from 1986 to modern."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [erlang, elixir, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Erlang & Elixir — Lịch sử phiên bản & Tiến hóa
## Dòng thời gian Erlang
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| Erlang 1 | 1986 | **Erlang đầu tiên** (Joe Armstrong, Ericsson) |
| Erlang 4 | 1991 | Phát hành công khai lần đầu tiên |
| Erlang 5 (R1) | 1998 | **Phát hành mã nguồn mở** |
| R9B | 2002 | Cơ sở dữ liệu Mnesia, cải thiện hiệu suất |
| R12B | 2006 | Dialyzer (kiểm tra loại) |
| R13B | 2008 | Cải tiến hồ sơ, cải tiến`fun`|
| R14B | 2010 | Hiểu nhị phân, GC được cải thiện |
| R15B | 2012 | Bản đồ (thử nghiệm) |
| R16B | 2013 | **Bản đồ** ổn định |
| 17.0 | 2014 | **Chính**: Bản đồ, cải tiến`receive`|
| 18.0 | 2015 | **Chính**: API thời gian, hoạt động `maps`, cải tiến`ssl`|
| 19.0 | 2016 |  Cải tiến`try`/ `catch`, cải tiến`binary`|
| 20.0 | 2017 | **Chính**: Cải tiến `maps`, cải tiến`ssl`|
| 21.0 | 2018 | **Chính**: Cải tiến `ssl`,`logger`(thay thế`error_logger`) |
| 22.0 | 2019 | **Chính**: Cải tiến về phân phối, cải tiến`ssl`|
| 23.0 | 2020 | **Chính**: Cải tiến `maps`, cải tiến`ssl`|
| 24.0 | 2021 | **Chính**: Cải tiến `ssl`, cải tiến`maps`|
| 25.0 | 2022 | **Chính**: Cải tiến `ssl`, cải tiến`maps`|
| 26.0 | 2023 | **Chính**: Cải tiến `ssl`, cải tiến`maps`|
| 27.0 | 2024 | **Chính**: Cải tiến `ssl`, cải tiến`maps`|
## Dòng thời gian thuốc tiên
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| 0,1 | 2011 | Bản phát hành đầu tiên (José Valim) |
| 0,12 | 2013 | Ổn định đầu tiên trước 1.0 |
| 0,13 | 2014 | `defprotocol`,`defimpl`|
| 0,14 | 2014 | Thông báo lỗi được cải thiện |
| 0,15 | 2014 | `Stream`,`Enum`cải tiến |
| 1.0 | 2014 | **Bản phát hành ổn định đầu tiên** |
| 1.1 | 2015 |  Tuyên bố `with`, cải tiến`Logger`|
| 1.2 | 2016 | `Multi-call`GenServer,`MapSet`|
| 1.3 | 2016 |  Các loại `Calendar`, cải tiến`Mix`|
| 1.4 | 2017 | `Registry`,`Supervisor`cải tiến |
| 1,5 | 2017 |  Cải tiến `Calendar`, cải tiến`Logger`|
| 1.6 | 2018 | **`mix format`** (bộ định dạng mã), cải tiến`Registry`|
| 1.7 | 2019 |  Cải tiến `defstruct`, cải tiến`mix`|
| 1.8 | 2019 |  Cải tiến `Calendar`, cải tiến`Logger`|
| 1.9 | 2019 | **`mix release`** (bản phát hành độc lập) |
| 1.10 | 2020 |  Cải tiến `Calendar`, cải tiến`Logger`|
| 1.11 | 2020 |  Cải tiến `defdelegate`, cải tiến`mix`|
| 1.12 | 2021 |  Cải tiến `struct`, cải tiến`mix`|
| 1.13 | 2021 |  Cải tiến `mix`, cải tiến`Logger`|
| 1.14 | 2022 |  Cải tiến `def`, cải tiến`mix`|
| 1.15 | 2023 |  Cải tiến `mix`, cải tiến`Logger`|
| 1.16 | 2024 |  Cải tiến `mix`, cải tiến`Logger`|
| 1.17 | 2024 | Đang phát triển |
## Các cột mốc quan trọng
### Erlang: Ngôn ngữ viễn thông (1986–2000)
- **1986**: Joe Armstrong, Robert Virding, Mike Williams tại Ericsson tạo ra Erlang
- **Mục tiêu**: Xây dựng hệ thống viễn thông đáng tin cậy — triết lý "hãy để nó gặp sự cố"
- **Các tính năng chính**: Mô hình diễn viên, trao đổi mã nóng, điện toán phân tán
- **1998**: Nguồn mở (R1) — Erlang bước vào thế giới rộng lớn hơn
- **Được sử dụng bởi**: Bộ chuyển mạch ATM Ericsson AXD301 (99,9999999% thời gian hoạt động — "nine nines")
### Thời gian đáo hạn Erlang/OTP (2000–2013)
- **OTP** (Nền tảng viễn thông mở) — framework, thư viện, công cụ
- **Mnesia** — cơ sở dữ liệu phân tán
- **Quả lọc máu** — phân tích kiểu tĩnh
- **R16B (2013)**: Maps — cấu trúc dữ liệu khóa-giá trị
### Erlang Thời hiện đại (2014–nay)
- **17.0 (2014)**: Maps — tính năng ngôn ngữ chính
- **18.0 (2015)**: API thời gian mới, hoạt động bản đồ
- **21.0 (2018)**:`logger`mới (thay thế`error_logger`)
- **22.0–27.0**: Liên tục cải tiến SSL, phân phối, hiệu suất
### Elixir: Erlang cho cộng đồng Ruby (2011–nay)
- **2011**: José Valim tạo Elixir — biên dịch thành Erlang BEAM
- **Mục tiêu**: Năng suất của Ruby + độ tin cậy của Erlang
- **Các tính năng chính**: Siêu lập trình, ống `|>`, macro, công cụ xây dựng `mix`
- **1.0 (2014)**: Bản phát hành ổn định đầu tiên
- **1.6 (2018)**:`mix format`— trình định dạng mã tích hợp
- **1.9 (2019)**:`mix release`— các bản phát hành độc lập (không cần Erlang)
## Tiến hóa cú pháp
```erlang
%% Erlang R1: Basic Actor model
-module(hello).
-export([start/0, loop/0]).

start() ->
    Pid = spawn(hello, loop, []),
    Pid ! {hello, self()},
    receive
        Response -> io:format("~p~n", [Response])
    end.

loop() ->
    receive
        {hello, From} ->
            From ! {hello_from, node()},
            loop()
    end.

%% Erlang 17+: Maps
Person = #{name => "Alice", age => 30},
Name = maps:get(name, Person),
Person2 = Person#{email => "alice@example.com"}.

%% Erlang: Pattern matching + recursion
factorial(0) -> 1;
factorial(N) -> N * factorial(N - 1).

%% Erlang: List comprehension
[X * 2 || X <- [1, 2, 3, 4, 5], X rem 2 =:= 0].
```

```elixir
# Elixir: Pipe operator
"hello world"
|> String.split()
|> Enum.map(&String.capitalize/1)
|> Enum.join(" ")

# Elixir: Pattern matching
{:ok, result} = SomeModule.compute()

# Elixir: Macros (metaprogramming)
defmodule MyMacro do
  defmacro say_hello do
    quote do
      IO.puts("Hello!")
    end
  end
end

# Elixir: GenServer (OTP behavior)
defmodule Counter do
  use GenServer

  def start_link(initial), do: GenServer.start_link(__MODULE__, initial)
  def inc(pid), do: GenServer.cast(pid, :inc)
  def get(pid), do: GenServer.call(pid, :get)

  @impl true
  def init(initial), do: {:ok, initial}

  @impl true
  def handle_cast(:inc, count), do: {:noreply, count + 1}

  @impl true
  def handle_call(:get, _from, count), do: {:reply, count, count}
end

# Elixir: Comprehensions
for x <- 1..10, rem(x, 2) == 0, do: x * x

# Elixir: with (error handling)
with {:ok, user} <- find_user(id),
     {:ok, perms} <- check_permissions(user) do
  {:ok, perms}
else
  {:error, reason} -> {:error, reason}
end
```

## Nguyên tắc thiết kế chính
```
Erlang:
1. "Let it crash" — isolate failures, restart processes
2. "Share nothing" — processes communicate via messages only
3. "Hot code swapping" — update code without stopping
4. "Distributed" — built for multi-node systems
5. "Fault-tolerant" — supervisor trees, automatic restart
6. "Nine nines" — 99.9999999% uptime is achievable

Elixir:
7. "Productive" — Ruby-like syntax, pipes, macros
8. "Metaprogramming" — extend the language itself
9. "Tooling" — mix (build), format (style), hex (packages)
10. "Compatible" — runs on Erlang BEAM, uses Erlang libraries
```

## Tăng trưởng hệ sinh thái
```
1986: Erlang created at Ericsson (telecom)
1998: Erlang open-sourced (R1)
2000s: Erlang/OTP matures — Mnesia, Dialyzer
2007: RabbitMQ (message broker) — Erlang-based
2011: Elixir created by José Valim
2014: Elixir 1.0 — stable release
2015: Phoenix framework — web development
2018: Elixir 1.6 — mix format
2019: Elixir 1.9 — mix release
2025: Erlang/Elixir power:
       - WhatsApp (Erlang, 2M+ concurrent connections per server)
       - Discord (Elixir, handles millions of users)
       - RabbitMQ, CouchDB, EMQX (Erlang)
       - Phoenix (Elixir web framework)
       - Used by: WhatsApp, Discord, Bleacher Report, Pinterest
```
