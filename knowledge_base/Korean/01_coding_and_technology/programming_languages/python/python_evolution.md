---
# Metadata
title: "Python — Version History & Evolution"
description: "Comprehensive version history and evolution of Python from 1.x to modern Python."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [python, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Python — 버전 기록 및 진화
## 타임라인
| 버전 | 출시일 | 주요 테마 |
|---------|-------------|------------|
| 1.0 | 1994년 1월 | 최초 출시 |
| 1.5 | 1997년 12월 | 클래스, 예외, 모듈 |
| 2.0 | 2000년 10월 | 목록 이해, 가비지 수집 |
| 2.2 | 2001년 12월 | 통합 유형(유형/클래스), 생성기 |
| 2.5 | 2006년 9월 | `with`문, 표현식으로`yield`|
| 2.6 | 2008년 10월 | `bytes`,`future`가져오기, 3으로 전환 |
| 2.7 | 2010년 7월 | 사전/집합 이해,`argparse`|
| 3.0 | 2008년 12월 | **중간**:`print()`,`str`/`bytes`, 반복자 |
| 3.3 | 2012년 9월 |  `yield from`, 네임스페이스 패키지 |
| 3.4 | 2014년 3월 | `asyncio`,`pathlib`,`enum`|
| 3.5 | 2015년 9월 | `async/await`, 유형 힌트(PEP 484),`**`압축 풀기 |
| 3.6 | 2016년 12월 | f-문자열,`async`이해, 순서가 지정된 dicts |
| 3.7 | 2018년 6월 | `dataclasses`,`contextvars`, 예약됨`async`|
| 3.8 | 2019년 10월 | 바다코끼리 연산자 `:=`, 위치 전용 매개변수 |
| 3.9 | 2020년 10월 | Dict Union`|`, 일반 유형`list[int]`|
| 3.10 | 2021년 10월 |  `match/case`, 구조적 패턴 일치 |
| 3.11 | 2022년 10월 | 예외 그룹,`Self`유형, 더 빠른 CPython |
| 3.12 | 2023년 10월 | 인터프리터별 GIL 준비, 유형 매개변수 구문 |
| 3.13 | 2024년 10월 | 자유 스레드 모드(실험적), 개선된 REPL |
| 3.14 | 2025년 10월 | No-GIL 안정적이고 지연된 주석 평가 |
## 주요 이정표
### Python 2.x 시대(2000~2020)
- **2.0**: Haskell에서 영감을 받은 목록 이해; 순환 GC
- **2.2**:`object`기본 클래스; `yield`키워드(생성기)
- **2.5**:`with`문;  `yield`는 표현식이 됩니다.
- **2.7**: 최종 2.x 릴리스; 사전 이해; `argparse`
- **수명 종료**: 2020년 1월 1일
### Python 3.x 혁명(2008~현재)
- **3.0**: 깔끔한 중단 — 함수로서의 `print`,`str`대 `bytes`, 모든 반복자는 뷰를 반환합니다.
- **3.5**:`async`/`await`구문;`typing`모듈로 힌트 입력
- **3.6**: f-문자열(가장 많이 요청되는 기능); `asyncio`안정화됨
- **3.8**: 인라인 할당을 위한 Walrus 연산자
- **3.10**: 구조적 패턴 매칭 (`match`/`case`)
- **3.11**: 10-60% 더 빠릅니다. `except*`를 사용한 예외 그룹 
- **3.13**: 실험적인 자유 스레드 모드(GIL 없음)
## 디자인 철학의 진화
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## Python을 형성한 주요 PEP
| 격려 | 연도 | 기능 |
|------|------|---------|
| 20 | 2004년 | 젠 오브 파이썬 |
| 257 | 2001 | Docstring 규칙 |
| 279 | 2002 | `enumerate()`|
| 289 | 2002 | 생성기 표현식 |
| 342 | 2005년 |  표현식으로 `yield`,`send()`|
| 380 | 2009 | `yield from`|
| 484 | 2014 | 힌트 입력 |
| 492 | 2014 | `async`/`await`|
| 498 | 2015 | f-문자열 |
| 572 | 2018 | 바다코끼리 운영자`:=`|
| 622 | 2020 | 구조적 패턴 일치 |
| 654 | 2021 | 예외 그룹 |
| 684 | 2022 | 인터프리터별 GIL |
| 703 | 2023년 | GIL을 선택적으로 만들기 |
## 성능의 진화
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## 커뮤니티 및 생태계 성장
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
