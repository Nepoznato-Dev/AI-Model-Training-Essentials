<!--
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

-->
# Fortran — 생태계 및 툴링 가이드
이 가이드에서는 Fortran 생태계의 필수 도구, 라이브러리 및 인프라를 다룹니다.
---

## 포트란 표준 및 컴파일러
| 컴파일러 | 플랫폼 | 메모 |
|----------|----------|-------|
| **그포트란** | 크로스 플랫폼 | 가장 널리 사용되는 GNU Fortran(GCC) |
| **ifx / ifort** | 크로스 플랫폼 | 인텔 포트란(oneAPI) |
| **nvfortran** | GPU | 엔비디아 포트란(CUDA) |
| **플랭** | 크로스 플랫폼 | LLVM 기반(신규) |
| **잔소리** | 크로스 플랫폼 | 상업적이고 엄격한 준수 |
| **크레이** | HPC | 크레이 슈퍼컴퓨터 |
| **IBM XL** | HPC | IBM 시스템 |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## 시스템 구축
| 도구 | 유형 | 최고의 대상 |
|------|------|----------|
| **CMake** | 크로스 플랫폼 | 업계 표준 |
| **fpm** | 포트란 네이티브 | 최신 포트란 패키지 관리자 |
| **중간** | 현대 | 빠르고 깔끔한 구문 |
| **만들기** | 클래식 | 간단한 프로젝트 |
| **스콘** | Python 기반 | 복잡한 빌드 |
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

## 패키지 관리
| 도구 | 목적 |
|------|---------|
| **fpm** | 포트란 패키지 관리자(최신) |
| **포트란 표준 라이브러리** | 표준 도서관 노력 |
| **코난** | C/C++/포트란 패키지 |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## 과학 도서관
| 도서관 | 목적 |
|---------|---------|
| **블라/라팩** | 선형대수학 |
| **오픈BLAS** | 최적화된 BLAS |
| **인텔 MKL** | 인텔 수학 커널 라이브러리 |
| **FFTW** | 고속 푸리에 변환 |
| **아팩** | 고유값 문제 |
| **스칼라팩** | 병렬선형대수학 |
| **PETSc** | 병렬 과학 컴퓨팅 |
| **트릴리노스** | 대규모 과학 |
| **HDF5** | 계층적 데이터 형식 |
| **NetCDF** | 기후/과학 데이터 |
| **표준 라이브러리** | 포트란 표준 라이브러리 |
| **포트란-OS** | OS 인터페이스 |
| **실험실** | 과학 컴퓨팅 |
| **M_어레이** | 어레이 유틸리티 |
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

## 테스트
| 프레임워크 | 목적 |
|------------|---------|
| **pFUnit** | 단위 테스트(NASA) |
| **포트란 테스트** | 간단한 테스트 |
| **시운전** | 최신 테스트 |
| **fpm 테스트** | 내장된 테스트 러너 |
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

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **예쁘게 만들기** | 코드 서식 |
| **찾기** | 들여쓰기 및 서식 |
| **포트란-린터** | 린팅 |
| **캠포트** | 리팩토링 |
| **코코넛** | 코드 적용 범위 |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## 병렬 컴퓨팅
| 기술 | 목적 |
|------------|---------|
| **오픈MP** | 공유 메모리 병렬성 |
| **MPI** | 분산 메모리(메시지 전달) |
| **코어레이** | 포트란 기본 병렬성 |
| **쿠다 포트란** | GPU 컴퓨팅 |
| **오픈ACC** | 지시문 기반 GPU |
| **동시 진행** | Fortran 2008 병렬 루프 |
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

## 주요 라이브러리
| 도서관 | 목적 |
|---------|---------|
| **표준 라이브러리** | 표준 라이브러리 |
| **json-포트란** | JSON 구문 분석 |
| **forutils** | 유틸리티 기능 |
| **플랩** | 명령줄 인수 구문 분석 |
| **for_time** | 날짜/시간 처리 |
| **FiNeR** | 파일 처리 |
| **xml용** | XML 구문 분석 |
| **포피** | Python 상호 운용성 |
| **ISO_C_BINDING** | C 상호 운용성 |
---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **VS 코드 + 최신 포트란** | 최고의 포트란 LSP |
| **IntelliJ + 포트란 플러그인** | JetBrains 지원 |
| **네오빔 + 요새** | 터미널 기반 |
| **이클립스 + 포토란** | 이클립스 포트란 |
| **코드::블록** | 경량 IDE |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **정적 바이너리** | `gfortran -static`|
| **공유 라이브러리** | `gfortran -shared`|
| **C 상호 운용성** | `ISO_C_BINDING`를 통해 C/C++에서 호출 |
| **Python 상호 운용성** | f2py, 포피 |
| **도커** | 컨테이너화 |
| **HPC 클러스터** | MPI + 슬럼 |
---

## 요약
Fortran의 생태계는 고성능 과학 컴퓨팅을 위해 특별히 제작되었습니다. 표준 툴체인은 컴파일용 **gfortran** 또는 **ifx**, 패키지 관리용 **fpm**, 빌드용 **CMake**, 선형 대수용 **BLAS/LAPACK**, 병렬 처리용 **OpenMP** 및 **MPI**, 테스트용 **pFUnit**, 서식 지정용 **fprettify**입니다. Fortran은 수치 컴퓨팅, 날씨 시뮬레이션, 전산 유체 역학 및 대규모 과학 시뮬레이션에 탁월합니다. 공동 배열, DO CONCURRENT 및 향상된 OOP를 갖춘 Modern Fortran(2018/2023)은 유능한 현대 언어입니다. 생태계는 HPC, 기후 모델링, 컴퓨터 물리학에 필수적입니다.