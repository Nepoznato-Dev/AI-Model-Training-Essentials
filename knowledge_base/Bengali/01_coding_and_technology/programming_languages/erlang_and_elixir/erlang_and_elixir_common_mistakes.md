<!--
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

-->
# Erlang & Elixir — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্নস
এই নথিটি সংশোধন সহ Erlang এবং Elixir-এর সবচেয়ে সাধারণ ভুল, ফাঁদ, এবং অ্যান্টি-প্যাটার্নগুলি ক্যাটালগ করে।
---

## 1. একক অ্যাসাইনমেন্ট (Erlang)
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

## 2. লিঙ্কিং/মনিটরিং প্রসেস নয় (Erlang)
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

## 3. সময়সীমা ছাড়াই জেনসার্ভার কল (এলিক্সির)
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

## 4. সময়সীমা ছাড়াই `receive`-এ প্যাটার্ন ম্যাচ (এরলাং)
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

## 5. নেস্টেড প্যাটার্ন ম্যাচিং (Elixir) এর জন্য`with`ব্যবহার করছেন না
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

## 6. অ্যান্টি-প্যাটার্ন: দীর্ঘ-চলমান GenServer কলব্যাক
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

## সারাংশ
Erlang/Elixir ট্র্যাপ: ভেরিয়েবলগুলি একক-অ্যাসাইনমেন্ট, প্রসেসগুলির লিঙ্ক/মনিটরগুলির প্রয়োজন, GenServer কলগুলির সুস্পষ্ট টাইমআউটের প্রয়োজন,`receive`টাইমআউট ছাড়াই চিরতরে ব্লক করা, এবং GenServer কলব্যাকগুলি ব্লক করা উচিত নয়৷ BEAM উপায় হল: এটিকে ক্র্যাশ করতে দিন (তত্ত্বাবধানে), পরিষ্কার প্যাটার্ন ম্যাচিংয়ের জন্য`with`ব্যবহার করুন, GenServer কলব্যাকগুলি দ্রুত রাখুন এবং সর্বদা প্রক্রিয়া ব্যর্থতাগুলি পরিচালনা করুন৷