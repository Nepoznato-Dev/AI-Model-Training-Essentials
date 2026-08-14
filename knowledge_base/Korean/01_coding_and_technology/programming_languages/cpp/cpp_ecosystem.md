<!--
---
# Metadata
title: "C++ — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the C++ ecosystem including compilers, build systems, libraries, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [cpp, ecosystem, tooling, compilers, build-systems, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "18 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# C++ — 생태계 및 도구 가이드
이 가이드에서는 C++ 생태계의 필수 도구, 라이브러리 및 인프라를 다룹니다.
---

## 컴파일러
| 컴파일러 | 플랫폼 | 메모 |
|----------|----------|-------|
| **GCC(g++)** | 리눅스/유닉스 | 널리 사용되는 GNU 컴파일러 컬렉션 |
| **삐걱거리는 소리++** | 크로스 플랫폼 | LLVM 기반의 우수한 진단 |
| **MSVC** | 윈도우 | Microsoft Visual C++ 컴파일러 |
| **인텔 oneAPI(icpx)** | 크로스 플랫폼 | 고성능, HPC 중심 |
| **지그 C++** | 크로스 플랫폼 | 훌륭한 크로스 컴파일 |
```bash
g++ -std=c++23 -O2 -Wall -Wextra -o app main.cpp
clang++ -std=c++23 -stdlib=libc++ -o app main.cpp
```

---

## 시스템 구축
| 도구 | 유형 | 최고의 대상 |
|------|------|----------|
| **CMake** | 크로스 플랫폼 | 업계 표준, 대부분의 프로젝트 |
| **중간** | 현대 | 빠르고 깔끔한 구문, Ninja 백엔드 |
| **바젤** | 규모 | Google 규모의 Monorepos |
| **코난 + CMake** | 패키지 인식 | C++ 패키지 관리 |
| **xmake** | 현대 | Lua 기반 내장 패키지 관리자 |
| **만들기** | 클래식 | 간단한 유닉스 프로젝트 |
| **닌자** | 빠른 | 저수준 빌드 시스템 |
```cmake
# CMakeLists.txt example
cmake_minimum_required(VERSION 3.24)
project(myapp LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(myapp src/main.cpp)
target_compile_features(myapp PRIVATE cxx_std_23)

# Find packages
find_package(fmt REQUIRED)
target_link_libraries(myapp PRIVATE fmt::fmt)
```

---

## 패키지 관리자
| 도구 | 유형 | 메모 |
|------|------|-------|
| **코난** | 탈중앙화 | Python 기반, 가장 인기 있음 |
| **vcpkg** | 마이크로소프트 | CMake/VcpkgManifest 통합 |
| **헌터** | CMake 네이티브 | CMake 기반 종속성 관리자 |
| **xrepo** | Lua 기반 | xmake를 통한 크로스 플랫폼 |
```bash
# Conan 2.x
conan install . --output-folder=build --build=missing
cd build && cmake .. -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake

# vcpkg (manifest mode)
# vcpkg.json in project root
vcpkg install
```

---

## 테스트
| 프레임워크 | 목적 |
|------------|---------|
| **구글 테스트(gtest)** | 가장 인기 있는 Google |
| **Google Mock(gmock)** | 모의 프레임워크 |
| **캐치2** | 단일 헤더, BDD 스타일 |
| **문서 테스트** | 경량 단일 헤더 |
| **부스트.테스트** | 부스트 기반 테스트 |
| **구글 벤치마크** | 마이크로벤치마킹 |
| **나노벤치** | 경량 벤치마킹 |
```cpp
// Catch2 example
#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>

TEST_CASE("vector operations") {
    std::vector<int> v = {1, 2, 3};
    REQUIRE(v.size() == 3);
    REQUIRE(v[0] == 1);
    SECTION("push_back") {
        v.push_back(4);
        REQUIRE(v.size() == 4);
    }
}
```

---

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **깔끔하게 정리** | 린터, 현대화, 버그 발생 가능성 검사 |
| ** 소리 형식 ** | 코드 서식 |
| **cpp체크** | 정적 분석 |
| **PVS-스튜디오** | 상업용 정적 분석 |
| **보장** | 기업 정적 분석 |
| **소나큐브** | 코드 품질 플랫폼 |
| **사용한 내용 포함(IWYU)** | 헤더 종속성 분석 |
| **cppdep** | 종속성 분석 |
```yaml
# .clang-tidy example
Checks: >
  -*,
  bugprone-*,
  modernize-*,
  performance-*,
  readability-*,
  -modernize-use-trailing-return-type
```

---

## 디버깅 및 분석
| 도구 | 목적 |
|------|---------|
| **GDB** | GNU 디버거 |
| **LLDB** | LLVM 디버거 |
| **발그린드** | 메모리 오류 감지 |
| **AddressSanitizer(ASan)** | 빠른 메모리 오류 감지기 |
| **정의되지 않은BehaviorSanitizer(UBSan)** | UB 감지 |
| **ThreadSanitizer(TSan)** | 데이터 경합 감지 |
| **MemorySanitizer(MSan)** | 초기화되지 않은 메모리 |
| **LeakSanitizer(LSan)** | 메모리 누수 감지 |
| **성능** | Linux 성능 프로파일링 |
| **트레이시** | 실시간 프레임 프로파일러 |
| **엔비디아 엔사이트** | GPU 프로파일링 |
```bash
# Compile with sanitizers
g++ -fsanitize=address,undefined -g -o app main.cpp
clang++ -fsanitize=thread -g -o app main.cpp
```

---

## 주요 라이브러리
| 도서관 | 목적 |
|---------|---------|
| **STL** | 표준 라이브러리(컨테이너, 알고리즘) |
| **부스트** | 종합 유틸리티 라이브러리 |
| **fmt** | 최신 형식(std::format의 기초) |
| **nlohmann/json** | JSON 구문 분석 |
| **spdlog** | 빠른 로깅 |
| **아이겐** | 선형대수학 |
| **오픈CV** | 컴퓨터 비전 |
| **Qt** | 크로스 플랫폼 GUI 프레임워크 |
| **SDL2** | 멀티미디어/게임 |
| **OpenGL/Vulkan/DirectX** | 그래픽 API |
| **gRPC** | RPC 프레임워크 |
| **프로토부프** | 직렬화 |
| **libcurl** | HTTP 전송 |
| **오픈SSL** | 암호화, TLS |
| **SQLite** | 내장형 데이터베이스 |
| **포코** | 네트워크 및 유틸리티 라이브러리 |
| **ASIO / Boost.Asio** | 비동기 I/O, 네트워킹 |
| **범위(C++20)** | 지연 평가, 구성 가능한 알고리즘 |
---

## 동시성 및 비동기
| 도서관 | 목적 |
|---------|---------|
| **std::스레드 / std::jthread** | C++11/20 스레딩 |
| **표준::비동기 / 표준::미래** | 작업 기반 병렬성 |
| **표준::실행** | 병렬 알고리즘(C++17) |
| **부스트.아시오** | 비동기 네트워킹 |
| **리부브** | 비동기 I/O |
| **오픈MP** | 지시어 기반 병렬성 |
| **미정** | 인텔 스레딩 빌딩 블록 |
| **표준::stop_token** | 협력 취소(C++20) |
---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **클리온** | 전체 JetBrains C++ IDE, CMake 통합 |
| **VS 코드 + clangd** | 경량, LSP 기반 |
| **비주얼 스튜디오** | 최고의 Windows C++ IDE |
| **Qt 크리에이터** | Qt 개발 |
| **네오빔 + clangd** | LSP를 사용한 터미널 기반 |
| **Eclipse CDT** | 오픈 소스 C/C++ |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **정적 바이너리** | `g++ -static`또는 musl |
| **도커** | 다단계 빌드 |
| **크로스 컴파일** | GCC/Clang 크로스 툴체인 |
| **코난 + CI** | 패키지 및 배포 |
| **vcpkg + CI** | 매니페스트 모드 배포 |
| **내장형** | 베어메탈, RTOS, 크로스 컴파일 |
---

## 요약
C++는 가장 풍부하고 복잡한 생태계를 가지고 있습니다. 표준 툴체인은 컴파일용 **GCC** 또는 **Clang**, 빌드용 **CMake**, 패키지용 **Conan** 또는 **vcpkg**, 테스트용 **Google Test** 또는 **Catch2**, Linting용 **clang-tidy**, 디버깅용 **GDB**, 새니타이저용 **ASan/UBSan**입니다. 주요 라이브러리에는 유틸리티용 **Boost**, 포맷용 **fmt**, JSON용 **nlohmann/json**, 로깅용 **spdlog**, 수학용 **Eigen**, GUI용 **Qt**가 포함됩니다. 개념, 범위, 코루틴 및 모듈을 갖춘 최신 C++(20/23)는 생태계를 변화시키고 있습니다. 항상 `-Wall -Wextra -Werror`로 컴파일하고 CI에서 새니타이저를 사용하세요.