---
# Metadata
title: "Rust — Version History & Evolution"
description: "Comprehensive version history and evolution of Rust from early development to modern Rust."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [rust, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Rust — История версий и эволюция
## Временная шкала
| Версия | Дата выпуска | Ключевая тема |
|---------|-------------|-----------|
| 0,1 | январь 2012 г. | Первый компилятор (rustc), параллелизм на основе задач |
| 0,5 | 2012 | Система типов, основанная на признаках, обретает форму |
| 0,6 | 2012 | Удаление управляемых ящиков`@`|
| 0,7 | 2013 | `@`удален,`~`для принадлежащих ящиков |
| 0,8 | 2013 | Пожизненные аннотации,`&mut`|
| 0,9 | январь 2014 г. | Финальная очистка до версии 1.0 |
| 0,10 | февраль 2014 г. | Последняя версия до 1.0 |
| 0,11 | апрель 2014 г. | `Box<T>`заменяет`~T`|
| 0,12 | май 2014 г. |  Начинается перезапись модуля`io`|
| 1.0 | 15 мая 2015 г. | **Стабильная версия** — «Rust 1.0» |
| 1.10 | август 2016 г. |  Распространение ошибки`?`(как`try!`→ `?`) |
| 1,15 | февраль 2017 г. | Первая стабильная версия Rust с подготовкой`impl Trait`|
| 1.18 | июнь 2017 г. |  `pub(crate)`, инкрементная компиляция |
| 1,20 | Октябрь 2017 г. | Связанные константы |
| 1,26 | май 2018 г. | `impl Trait`в позиции аргумента/возврата |
| 1,28 | Сентябрь 2018 г. | Глобальные распределители |
| 1.31 | декабрь 2018 г. | **Rust 2018 Edition** — модули,`dyn Trait`|
| 1,34 | апрель 2019 г. | Альтернативные реестры |
| 1,39 | ноябрь 2019 г. | `async/await`в стабильной версии |
| 1,44 | июль 2020 г. | Улучшения диагностики |
| 1,51 | апрель 2021 г. |  Дженерики`const`(MVP) |
| 1,56 | октябрь 2021 г. | **Rust 2021 Edition** — замыкания, IntoIterator |
| 1,59 | февраль 2022 г. | Линейная сборка |
| 1,62 | июнь 2022 г. | `#[default]`для перечислений |
| 1,65 | декабрь 2022 г. | `let else`|
| 1,68 | март 2023 г. | `#[ffi_pure]`, оптимизация на основе профиля |
| 1,70 | июнь 2023 г. | Изолированные зависимости`crates.io`|
| 1,74 | ноябрь 2023 г. | Грузовой автономный режим |
| 1,76 | февраль 2024 г. | **Rust 2024 Edition** — блоки `gen`,`unsafe extern`|
| 1,79 | июнь 2024 г. | `LazyCell`,`LazyLock`|
| 1,82 | октябрь 2024 г. |  Требуется`unsafe`в блоках`extern`|
| 1,85 | февраль 2025 г. | Версия Rust 2024 стабилизирована |
## Основные вехи
### До 1.0 (2010–2015 гг.)
- **2010**: побочный проект Грейдона Хоара в Mozilla набирает обороты.
- **2012**: Первый общедоступный компилятор; система типов претерпевает серьезные изменения
- **2013**: выкристаллизовывается модель собственности;  Ящики`@`удалены.
- **2014**: процесс Rust RFC формализован; сообщество растет
- **2015**: **1.0** — гарантия стабильности; «абстракции с нулевой стоимостью»
### Годы роста (2015–2019)
- **2015**: Cargo становится стандартным менеджером пакетов.
- **2018**: **Rust 2018 Edition** — капитальный ремонт системы модулей,`dyn Trait`,`impl Trait`
- **2019**:`async/await`выходит в стабильную версию — начинается асинхронная экосистема.
### Зрелость (2020 – настоящее время)
- **2021**: **Rust 2021 Edition** — устранение неоднозначности полей в замыканиях,`IntoIterator`для массивов.
- **2024**: **Rust 2024 Edition** — блоки `gen`, требования `unsafe extern`
- **2025**: ржавчина в ядре Linux, Android, Windows и инфраструктуре AWS.
## Система Изданий
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## Эволюция собственности
```
2010: GC-based, like Erlang
2011: Region-based lifetimes proposed
2012: Ownership model emerges (unique, shared, owned)
2013: Simplified to &T / &mut T / Box<T>
2014: Box<T> replaces ~T; Rc<T> for shared ownership
2015: 1.0 — ownership model finalized
2018: Non-Lexical Lifetimes (NLL) in Rust 2018
2021: IntoIterator for arrays (was blocked by edition concerns)
2024: Further NLL improvements
```

## Асинхронная эволюция
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## Рост экосистемы
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## Ключевые RFC
| РФЦ | Год | Особенность |
|------|------|---------|
| 25 | 2013 | Сопоставление с образцом |
| 153 | 2014 |  Тип`Result`|
| 217 | 2014 |  Оператор`?`(попробовать) |
| 460 | 2016 | `?`заменяет`try!`|
| 1210 | 2015 | `impl Trait`|
| 1414 | 2016 | Версия Руста 2018 |
| 2394 | 2018 | `async/await`|
| 2515 | 2018 |  Дженерики`const`|
| 3013 | 2020 | Проверка условной компиляции |
| 3517 | 2023 | `gen`блоки |