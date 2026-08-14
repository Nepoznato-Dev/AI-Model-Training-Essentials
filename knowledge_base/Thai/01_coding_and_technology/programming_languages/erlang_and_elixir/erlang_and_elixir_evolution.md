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

# Erlang & Elixir - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์เออร์แลง
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| เออร์ลัง 1 | 1986 | **เฟิร์ส เออร์แลง** (โจ อาร์มสตรอง, อีริคสัน) |
| เออร์ลัง 4 | 1991 | เผยแพร่สู่สาธารณะครั้งแรก |
| เออร์แลง 5 (R1) | 1998 | **โอเพ่นซอร์ส** ปล่อย |
| R9B | 2545 | ฐานข้อมูล Mnesia ปรับปรุงประสิทธิภาพ |
| R12B | 2549 | Dialyzer (ตัวตรวจสอบประเภท) |
| R13B | 2551 | การปรับปรุงบันทึก, การปรับปรุง`fun`|
| R14B | 2010 | ความเข้าใจแบบไบนารี ปรับปรุง GC |
| R15B | 2555 | แผนที่ (ทดลอง) |
| R16B | 2013 | **แผนที่** เสถียร |
| 17.0 | 2014 | **สำคัญ**: แผนที่ การปรับปรุง`receive`|
| 18.0 | 2558 | **สำคัญ**: Time API, การดำเนินการ `maps`, การปรับปรุง`ssl`|
| 19.0 | 2559 |  การปรับปรุง`try`/`catch`การปรับปรุง`binary`|
| 20.0 | 2017 | **สำคัญ**: การปรับปรุง `maps`, การปรับปรุง`ssl`|
| 21.0 | 2018 | **สำคัญ**: การปรับปรุง `ssl`,`logger`(แทนที่`error_logger`) |
| 22.0 | 2019 | **หลัก**: การปรับปรุงการจัดจำหน่าย การปรับปรุง`ssl`|
| 23.0 | 2020 | **สำคัญ**: การปรับปรุง `maps`, การปรับปรุง`ssl`|
| 24.0 | 2021 | **สำคัญ**: การปรับปรุง `ssl`, การปรับปรุง`maps`|
| 25.0 | 2022 | **สำคัญ**: การปรับปรุง `ssl`, การปรับปรุง`maps`|
| 26.0 | 2023 | **สำคัญ**: การปรับปรุง `ssl`, การปรับปรุง`maps`|
| 27.0 | 2024 | **สำคัญ**: การปรับปรุง `ssl`, การปรับปรุง`maps`|
## ไทม์ไลน์ของน้ำอมฤต
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| 0.1 | 2554 | การเปิดตัวครั้งแรก (José Valim) |
| 0.12 | 2013 | เสถียรครั้งแรกก่อน 1.0 |
| 0.13 | 2014 | `defprotocol`,`defimpl`|
| 0.14 | 2014 | ปรับปรุงข้อความแสดงข้อผิดพลาด |
| 0.15 | 2014 | `Stream`, การปรับปรุง`Enum`|
| 1.0 | 2014 | **การเปิดตัวที่เสถียรครั้งแรก** |
| 1.1 | 2558 |  คำสั่ง `with`, การปรับปรุง`Logger`|
| 1.2 | 2559 | `Multi-call`เจนเซิร์ฟเวอร์,`MapSet`|
| 1.3 | 2559 |  ประเภท`Calendar`การปรับปรุง`Mix`|
| 1.4 | 2017 | `Registry`, การปรับปรุง`Supervisor`|
| 1.5 | 2017 |  การปรับปรุง `Calendar`, การปรับปรุง`Logger`|
| 1.6 | 2018 | **`mix format`** (ตัวจัดรูปแบบโค้ด), การปรับปรุง`Registry`|
| 1.7 | 2019 |  การปรับปรุง `defstruct`, การปรับปรุง`mix`|
| 1.8 | 2019 |  การปรับปรุง `Calendar`, การปรับปรุง`Logger`|
| 1.9 | 2019 | **`mix release`** (วางจำหน่ายในตัวเอง) |
| 1.10 | 2020 |  การปรับปรุง `Calendar`, การปรับปรุง`Logger`|
| 1.11 | 2020 |  การปรับปรุง `defdelegate`, การปรับปรุง`mix`|
| 1.12 | 2021 |  การปรับปรุง `struct`, การปรับปรุง`mix`|
| 1.13 | 2021 |  การปรับปรุง `mix`, การปรับปรุง`Logger`|
| 1.14 | 2022 |  การปรับปรุง `def`, การปรับปรุง`mix`|
| 1.15 | 2023 |  การปรับปรุง `mix`, การปรับปรุง`Logger`|
| 1.16 | 2024 |  การปรับปรุง `mix`, การปรับปรุง`Logger`|
| 1.17 | 2024 | การพัฒนาอย่างต่อเนื่อง |
## เหตุการณ์สำคัญที่สำคัญ
### Erlang: ภาษาโทรคมนาคม (1986–2000)
- **1986**: Joe Armstrong, Robert Virding, Mike Williams จาก Ericsson สร้าง Erlang
- **เป้าหมาย**: สร้างระบบโทรคมนาคมที่เชื่อถือได้ — ปรัชญา "ปล่อยให้มันพัง"
- **คุณสมบัติหลัก**: โมเดลนักแสดง, การสลับโค้ดร้อน, การคำนวณแบบกระจาย
- **1998**: โอเพ่นซอร์ส (R1) — Erlang เข้าสู่โลกกว้าง
- **ใช้โดย**: Ericsson AXD301 ATM switch (เวลาทำงาน 99.9999999% — "nine nines")
### Erlang/OTP ครบกำหนด (2000–2013)
- **OTP** (แพลตฟอร์มโทรคมนาคมแบบเปิด) — เฟรมเวิร์ก ไลบรารี เครื่องมือ
- **Mnesia** — ฐานข้อมูลแบบกระจาย
- **ตัวฟอก** — การวิเคราะห์แบบคงที่
- **R16B (2013)**: แผนที่ — โครงสร้างข้อมูลคีย์-ค่า
### ยุคสมัยใหม่เออร์ลัง (พ.ศ. 2557–ปัจจุบัน)
- **17.0 (2014)**: แผนที่ — คุณลักษณะภาษาหลัก
- **18.0 (2015)**: API เวลาใหม่ การดำเนินการของแผนที่
- **21.0 (2018)**:`logger`ใหม่ (แทนที่`error_logger`)
- **22.0–27.0**: การปรับปรุง SSL, การกระจาย และประสิทธิภาพอย่างต่อเนื่อง
### Elixir: Erlang สำหรับชุมชน Ruby (2011–ปัจจุบัน)
- **2011**: José Valim สร้าง Elixir — คอมไพล์เป็น Erlang BEAM
- **เป้าหมาย**: ประสิทธิภาพการทำงานของ Ruby + ความน่าเชื่อถือของ Erlang
- **คุณสมบัติหลัก**: การเขียนโปรแกรมเมตา, ไปป์ `|>`, มาโคร, เครื่องมือสร้าง `mix`
- **1.0 (2014)**: การเปิดตัวที่เสถียรครั้งแรก
- **1.6 (2018)**:`mix format`— ตัวจัดรูปแบบโค้ดในตัว
- **1.9 (2019)**:`mix release`— รุ่นที่มีในตัวเอง (ไม่จำเป็นต้องใช้ Erlang)
## วิวัฒนาการไวยากรณ์
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

## หลักการออกแบบที่สำคัญ
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

## การเติบโตของระบบนิเวศ
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
