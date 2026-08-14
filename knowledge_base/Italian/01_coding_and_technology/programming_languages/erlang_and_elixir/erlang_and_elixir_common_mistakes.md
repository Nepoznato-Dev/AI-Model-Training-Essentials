---
# Metadata
title: "Erlang & Elixir — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Erlang and Elixir with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [erlang, elixir, common-mistakes, anti-patterns, pitfalls, otp, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Erlang ed Elixir: errori comuni e anti-schemi
Questo documento cataloga gli errori, le trappole e gli anti-modelli più comuni in Erlang ed Elixir con le relative correzioni.
---

## 1. Compito singolo (Erlang)
```erlang
% ❌ WRONG — expecting reassignment
X = 1.
X = 2.  % exception! X is already bound to 1

% ✅ CORRECT — use different variables or shadow
X1 = 1,
X2 = X1 + 1,

% Or in a new scope (function clause)
f(X) ->
    X = compute(),  % new X in this scope
    use(X).
```

---

## 2. Non collegare/monitorare i processi (Erlang)
```erlang
% ❌ WRONG — fire-and-forget process
spawn(fun() -> risky_operation() end).
% If it crashes, nobody knows

% ✅ CORRECT — link or monitor
Pid = spawn_link(fun() -> risky_operation() end),
% If it crashes, this process gets an exit signal

% ✅ CORRECT — monitor for non-linked observation
Ref = monitor(process, Pid),
receive
    {'DOWN', Ref, process, Pid, Reason} ->
        handle_crash(Reason)
end
```

---

## 3. Chiamata GenServer senza timeout (elisir)
```elixir
# ❌ WRONG — default 5s timeout
GenServer.call(server, :slow_operation)
# crashes with :timeout if operation takes > 5s

# ✅ CORRECT — explicit timeout
GenServer.call(server, :slow_operation, :infinity)
# or appropriate timeout
GenServer.call(server, :operation, 30_000)
```

---

## 4. Pattern Match in`receive`senza timeout (Erlang)
```erlang
% ❌ WRONG — blocks forever
receive
    {ok, Data} -> process(Data)
end.

% ✅ CORRECT — always use timeout
receive
    {ok, Data} -> process(Data)
after 5000 ->
    handle_timeout()
end.
```

---

## 5. Non utilizzare`with`per la corrispondenza di modelli nidificati (Elixir)
```elixir
# ❌ WRONG — deeply nested case
case authenticate(user) do
  {:ok, token} ->
    case authorize(token) do
      {:ok, perms} ->
        case fetch_data(perms) do
          {:ok, data} -> {:ok, data}
          {:error, e} -> {:error, e}
        end
      {:error, e} -> {:error, e}
    end
  {:error, e} -> {:error, e}
end

# ✅ CORRECT — use with
with {:ok, token} <- authenticate(user),
     {:ok, perms} <- authorize(token),
     {:ok, data} <- fetch_data(perms) do
  {:ok, data}
end
```

---

## 6. Anti-Pattern: callback GenServer di lunga durata
```elixir
# ❌ WRONG — blocking GenServer
def handle_call(:slow_op, _from, state) do
  result = :timer.sleep(10_000)  # blocks the server!
  {:reply, result, state}
end

# ✅ CORRECT — async work
def handle_call(:slow_op, from, state) do
  Task.start(fn ->
    result = compute()
    GenServer.reply(from, result)
  end)
  {:noreply, state}
end
```

---

## Riepilogo
Trappole Erlang/Elixir: le variabili sono ad assegnazione singola, i processi necessitano di collegamenti/monitor, le chiamate GenServer necessitano di timeout espliciti,`receive`si blocca per sempre senza timeout e i callback GenServer non dovrebbero bloccarsi. Il modo BEAM è: lasciarlo andare in crash (con supervisione), utilizzare`with`per una corrispondenza di pattern pulita, mantenere veloci i callback GenServer e gestire sempre gli errori di processo.