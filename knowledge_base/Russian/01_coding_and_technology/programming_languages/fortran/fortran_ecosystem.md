---
# Metadata
title: "Fortran — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Fortran ecosystem including compilers, build systems, libraries, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [fortran, ecosystem, tooling, compilers, hpc, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Фортран — Руководство по экосистеме и инструментам
В этом руководстве рассматриваются основные инструменты, библиотеки и инфраструктура экосистемы Fortran.
---

## Стандарты и компиляторы Фортрана
| Компилятор | Платформа | Заметки |
|----------|----------|-------|
| **гфортран** | Кроссплатформенный | GNU Fortran (GCC), наиболее широко используемый |
| **ифкс / ифорт** | Кроссплатформенный | Intel Фортран (oneAPI) |
| **нвфортран** | графический процессор | NVIDIA Фортран (CUDA) |
| **фланец** | Кроссплатформенный | На основе LLVM (новое) |
| **НАГ** | Кроссплатформенный | Коммерческое, строгое соответствие |
| **Крей** | высокопроизводительные вычисления | Суперкомпьютеры Cray |
| **IBM XL** | высокопроизводительные вычисления | системы IBM |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## Системы сборки
| Инструмент | Тип | Лучшее для |
|------|------|----------|
| **CMake** | Кроссплатформенный | Отраслевой стандарт |
| **фут/мин** | Фортран-родной | Современный менеджер пакетов Fortran |
| **Мезон** | Современный | Быстрый и понятный синтаксис |
| **Сделать** | Классический | Простые проекты |
| **SCons** | на основе Python | Комплексные постройки |
```toml
# fpm.toml (Fortran Package Manager)
name = "myapp"
version = "0.1.0"
license = "MIT"
author = "Developer"

[build]
auto-executables = true
auto-tests = true

[dependencies]
stdlib = { git = "https://github.com/fortran-lang/stdlib.git" }

[[test]]
name = "test_main"
source-dir = "test"
main = "test_main.f90"
```

```bash
fpm build                 # build
fpm test                  # run tests
fpm run                   # run executable
fpm new myproject         # new project
```

```cmake
# CMakeLists.txt
cmake_minimum_required(VERSION 3.20)
project(myapp LANGUAGES Fortran)

add_executable(myapp src/main.f90 src/module1.f90)
set_target_properties(myapp PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_BINARY_DIR}/modules)
target_include_directories(myapp PRIVATE ${CMAKE_BINARY_DIR}/modules)
```

---

## Управление пакетами
| Инструмент | Цель |
|------|---------|
| **фут/мин** | Менеджер пакетов Fortran (современный) |
| **Стандартная библиотека Фортрана** | Стандартная библиотека |
| **Конан** | Пакеты C/C++/Fortran |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## Научные библиотеки
| Библиотека | Цель |
|---------|---------|
| **БЛАС/ЛАПАК** | Линейная алгебра |
| **OpenBLAS** | Оптимизированный BLAS |
| **Интел МКЛ** | Библиотека математических ядер Intel |
| **ФФТВ** | Быстрое преобразование Фурье |
| **АРПАК** | Проблемы собственных значений |
| **СКАЛАПАК** | Параллельная линейная алгебра |
| **ПЭТС** | Параллельные научные вычисления |
| **Трилинос** | Масштабная научная |
| **HDF5** | Иерархический формат данных |
| **НетКДФ** | Климатические/научные данные |
| **стдлиб** | Стандартная библиотека Фортрана |
| **фортран-ос** | Интерфейс ОС |
| **для лаборатории** | Научные вычисления |
| **М_массив** | Утилиты массива |
```fortran
! LAPACK example (solve linear system Ax = b)
program solve_linear
    use lapack95
    implicit none
    integer, parameter :: n = 3
    real(8) :: A(n,n), b(n)
    integer :: ipiv(n), info
    
    A = reshape([2.0, 1.0, 1.0, 1.0, 3.0, 2.0, 1.0, 2.0, 4.0], [n,n])
    b = [1.0, 2.0, 3.0]
    
    call gesv(A, b, ipiv, info)
    
    print *, "Solution:", b
end program
```

---

## Тестирование
| Рамочная | Цель |
|-----------|---------|
| **pFUnit** | Модульное тестирование (НАСА) |
| **Фортран-тест** | Простое тестирование |
| **тест-драйв** | Современное тестирование |
| **тест fpm** | Встроенный тестировщик |
```fortran
! test-drive example
module test_math
    use testdrive, only : new_unittest, unittest_type, error_type, check
    implicit none
contains
    subroutine collect_tests(testsuite)
        type(unittest_type), allocatable, intent(out) :: testsuite(:)
        testsuite = [ &
            new_unittest("addition", test_addition), &
            new_unittest("multiplication", test_multiplication) &
        ]
    end subroutine
    
    subroutine test_addition(error)
        type(error_type), allocatable, intent(out) :: error
        call check(2 + 3 == 5, error)
    end subroutine
end module
```

---

## Качество кода
| Инструмент | Цель |
|------|---------|
| **украсить** | Форматирование кода |
| **найден** | Отступы и форматирование |
| **фортран-линтер** | Линтинг |
| **камфорт** | Рефакторинг |
| **КоКоНуТ** | Покрытие кода |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## Параллельные вычисления
| Технология | Цель |
|------------|---------|
| **ОпенМП** | Параллелизм с общей памятью |
| **ИМП** | Распределенная память (передача сообщений) |
| **Коаррейсы** | Собственный параллелизм Фортрана |
| **CUDA Фортран** | Вычисления на графическом процессоре |
| **OpenACC** | Графический процессор на основе директив |
| **СДЕЛАТЬ СОВРЕМЕННО** | Параллельные циклы Fortran 2008 |
```fortran
! OpenMP example
program parallel_sum
    implicit none
    integer, parameter :: n = 1000000
    real(8) :: a(n), b(n), c(n)
    integer :: i
    
    !$omp parallel do
    do i = 1, n
        c(i) = a(i) + b(i)
    end do
    !$omp end parallel do
end program
```

```fortran
! Coarray example
program coarray_example
    implicit none
    integer :: i
    real, codimension[:] :: shared_value
    
    shared_value[this_image()] = real(this_image())
    sync all
    
    if (this_image() == 1) then
        do i = 1, num_images()
            print *, "Image", i, "has value", shared_value[i]
        end do
    end if
end program
```

---

## Ключевые библиотеки
| Библиотека | Цель |
|---------|---------|
| **стдлиб** | Стандартная библиотека |
| **json-фортран** | Разбор JSON |
| **для утилит** | Служебные функции |
| **КЛАПАН** | Анализ аргументов командной строки |
| **на_время** | Обработка даты/времени |
| **ФиНер** | Обработка файлов |
| **форммл** | синтаксический анализ XML |
| **форпи** | Взаимодействие с Python |
| **ISO_C_BINDING** | совместимость C |
---

## IDE и редакторы
| IDE | Сильные стороны |
|-----|-----------|
| **VS Code + современный Фортран** | Лучший Фортран ЛСП |
| **IntelliJ + плагин fortran** | Поддержка JetBrains |
| **Неовим + фортлы** | На базе терминала |
| **Затмение + Фотран** | Затмение Фортран |
| **Код::Блоки** | Легкая IDE |
---

## Развертывание
| Метод | Заметки |
|--------|-------|
| **Статический двоичный файл** | `gfortran -static`|
| **Общая библиотека** | `gfortran -shared`|
| **Взаимодействие с C** | Вызов из C/C++ через`ISO_C_BINDING`|
| **Взаимодействие с Python** | f2py, форпи |
| **Докер** | Контейнерный |
| **Кластеры высокопроизводительных вычислений** | MPI + СЛУРМ |
---

## Краткое содержание
Экосистема Fortran специально создана для высокопроизводительных научных вычислений. Стандартная цепочка инструментов: **gfortran** или **ifx** для компиляции, **fpm** для управления пакетами, **CMake** для сборок, **BLAS/LAPACK** для линейной алгебры, **OpenMP** и **MPI** для параллелизма, **pFUnit** для тестирования и **fprettify** для форматирования. Фортран превосходно справляется с численными вычислениями, моделированием погоды, вычислительной гидродинамикой и крупномасштабным научным моделированием. Современный Фортран (2018/2023) с coarrays, DO CONCURRENT и улучшенным ООП — это современный язык, способный работать. Экосистема важна для высокопроизводительных вычислений, моделирования климата и вычислительной физики.