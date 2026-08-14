---
# Metadata
title: "Go — Version History & Evolution"
description: "Comprehensive version history and evolution of Go from 1.0 to modern Go."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [go, golang, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Go — История версий и эволюция
## Временная шкала
| Версия | Дата выпуска | Ключевая тема |
|---------|-------------|-----------|
| 1.0 | март 2012 г. | Первый стабильный выпуск |
| 1.1 | май 2013 г. | Производительность, детектор гонок |
| 1,3 | июнь 2014 г. | Сетевой опрос, крипто/TLS |
| 1,4 | декабрь 2014 г. | Bootstrap с Go (самостоятельный хостинг) |
| 1,5 | август 2015 г. | **Параллельный сборщик мусора**, барьеры записи |
| 1,7 | август 2016 г. |  Пакет `context`, подтесты`testing`|
| 1,8 | февраль 2017 г. |  `http.Server.Shutdown`, плагины |
| 1,9 | август 2017 г. | Псевдонимы типов, параллельные`make`|
| 1.10 | февраль 2018 г. |  Пул соединений`database/sql`|
| 1.11 | август 2018 г. | **Модули Go**,`go mod`|
| 1.12 | февраль 2019 г. | TLS 1.3, управление версиями модулей |
| 1.13 | Сентябрь 2019 г. |  `errors.Is/As`, числовые литералы `0b`,`0o`|
| 1.14 | февраль 2020 г. | **Перекрывающийся ввод-вывод в Windows**, вытеснение горутины |
| 1,15 | август 2020 г. |  Сброс `time.Ticker`/`Timer`, прокси модуля |
| 1.16 | февраль 2021 г. |  Пакет `embed`, `io/fs`, по умолчанию с поддержкой модулей |
| 1.17 | август 2021 г. | Преобразование среза в массив,`unsafe.Slice`|
| 1.18 | март 2022 г. | **Обобщенные**, фаззинг, рабочие области |
| 1.19 | август 2022 г. | Комментарии к документации, пересмотр модели памяти |
| 1,20 | февраль 2023 г. | `errors.Join`, оптимизация на основе профиля |
| 1.21 | август 2023 г. | **`slog`**, встроенные функции `min/max`,`maps/slices`|
| 1,22 | февраль 2024 г. | Диапазон целых чисел, улучшенная маршрутизация |
| 1,23 | август 2024 г. | Пакет Iterator (`iter`), изменения таймера |
| 1,24 | февраль 2025 г. |  Пакет `weak`, улучшенные карты |
## Основные вехи
### Начало (2009–2012)
- **2009**: Google анонсирует Go (Роберт Гриземер, Роб Пайк, Кен Томпсон)
- **2012**: **Go 1.0** — «Обещание совместимости с Go 1».
### Производительность и оснастка (2012–2018 гг.)
- **1.1**: повышение производительности более чем на 30 %; детектор гонок
- **1.5**: параллельный сборщик мусора (паузы GC сокращаются с миллисекунд до микросекунд)
- **1.5**: компилятор Go загружен — написан на Go (больше не C)
- **1.7**: пакет`context`становится стандартным.
### Модули и экосистема (2018–2021 гг.)
- **1.11**: **Модули Go** — официальное управление зависимостями.
- **1.13**:`errors.Is/As`— перенос ошибок становится идиоматическим
- **1.16**: пакет`embed`— встраивание файлов во время компиляции.
### Современное го (2022 – настоящее время)
- **1.18**: **Обобщенные** — параметры типа с ограничениями.
- **1.21**:`slog`— структурированное журналирование в stdlib;  Встроенные функции `min/max`
- **1.22**: Диапазон целых чисел (`for i := range 10`)
- **1.23**: Пакет Iterator — ленивая оценка в stdlib
## Путешествие по дженерикам
```
2010: "Go doesn't need generics" (early stance)
2016: Go generics proposal discussions begin
2018: Type parameters design draft published
2020: Go 2 generics proposal (draft designs)
2022: Go 1.18 — generics land! Type parameters, constraints
2023: Generic code patterns emerge (slices, maps packages)
2024: Community adapts — generic data structures, algorithms
```

## Философия обработки ошибок
```
1.0:     Explicit error returns — "errors are values"
1.13:    Error wrapping with %w — "inspect and unwrap"
1.20:    errors.Join — multiple errors
Future:  go2 proposal for try/handle (not yet adopted)
```

## Эволюция параллелизма
```
1.0:  Goroutines + channels — CSP-inspired
1.1:  Race detector
1.4:  Non-blocking syscalls (net poller)
1.5:  Concurrent GC
1.7:  context package for cancellation
1.14: Cooperative goroutine preemption (signals)
1.21: Synchronization improvements
1.23: iter package — iterator pattern
```

## Обещание совместимости Go
```
Go 1.0 (2012): "Go 1 will be available for a long time.
  Compatibility is important. Programs that work at Go 1
  will continue to work at every subsequent Go 1 release."

This means:
- No breaking changes to the language spec
- No breaking changes to the standard library
- Only additive changes
- Forward compatibility guaranteed
```

## Рост экосистемы
```
2012: Go 1.0 — basic stdlib, no package manager
2014: dep (early dependency management experiments)
2018: Go modules — official solution
2019: Go used by Uber, Twitch, Dropbox, Cloudflare
2022: Generics — opens new library design patterns
2023: Go in Kubernetes, Docker, Terraform, Hugo
2025: Top 10 most used language; cloud-native standard
```

## Эволюция производительности
```
Go 1.0:  Baseline
Go 1.1:  ~30% faster (register-based calling prep)
Go 1.5:  Concurrent GC (pause time: ms → μs)
Go 1.7:  SSA backend (15-30% faster)
Go 1.11: PGO experiments
Go 1.13: Faster map operations
Go 1.18: Generics (initial overhead, optimized in 1.19+)
Go 1.20: Profile-guided optimization
Go 1.22: Faster crypto, improved compiler
```
