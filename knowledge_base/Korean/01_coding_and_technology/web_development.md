---
# Metadata
title: "Web Development"
description: "Frontend, backend, DevOps, security"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [web, development, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# 웹 개발
## 프론트엔드 개발
### 핵심 기술
#### HTML(하이퍼텍스트 마크업 언어)
- **의미적 HTML**: 의미 있는 태그 사용(`<header>`,`<nav>`,`<main>`,`<article>`,`<section>`,`<aside>`,`<footer>`)
- **양식**: 입력 유형, 유효성 검사, 접근성 라벨
- **미디어**: 이미지, 동영상, 오디오 임베딩
- **메타 태그**: SEO, 뷰포트, 문자 인코딩
- **HTML5 기능**: 캔버스, SVG, 로컬 저장소, 위치정보, 웹 소켓
#### CSS(캐스케이딩 스타일 시트)
- **박스 모델**: 콘텐츠, 패딩, 테두리, 여백
- **레이아웃 시스템**:
  - **Flexbox**: 1차원 레이아웃, justify-content, align-items
  - **그리드**: 2차원 레이아웃, 그리드-템플릿, 그리드-영역
  - **포지셔닝**: 정적, 상대, 절대, 고정, 고정
- **반응형 디자인**: 미디어 쿼리, 모바일 우선 접근 방식
- **CSS 변수**: 테마 지정을 위한 사용자 정의 속성
- **애니메이션**: 전환, 키프레임, 변형
- **전처리기**: Sass, Less(변수, 믹스인, 중첩)
#### 자바스크립트
- **DOM 조작**: 요소 선택, 생성, 수정
- **이벤트**: 클릭, 제출, 키보드, 맞춤 이벤트, 이벤트 위임
- **ES6+ 기능**: 화살표 기능, 구조 분해, 확산/휴식, 모듈, 비동기/대기
- **API**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: 정적 타이핑, 인터페이스, 제네릭, 데코레이터
### 최신 프런트엔드 프레임워크
#### 반응
- **컴포넌트**: 기능적 컴포넌트, 클래스 컴포넌트
- **후크**: useState, useEffect, useContext, useReducer, 사용자 정의 후크
- **상태 관리**: Context API, Redux, Zustand, Recoil
- **라우팅**: React Router(BrowserRouter, Routes, Route, Link)
- **생태계**: Next.js(SSR, SSG), Remix, Gatsby
- **Virtual DOM**: diffing 알고리즘을 통한 효율적인 렌더링
#### Vue.js
- **옵션 API**: 데이터, 메서드, 계산, 감시
- **컴포지션 API**: setup(), ref, 반응성, 계산됨
- **지시문**: v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia**: 상태 관리
- **Vue 라우터**: 클라이언트 측 라우팅
- **Nuxt.js**: 서버 측 렌더링 프레임워크
#### 각도
- **구성 요소**: 데코레이터, 템플릿, 수명 주기 후크
- **서비스**: 종속성 주입, 싱글톤 패턴
- **RxJS**: 반응형 프로그래밍, 관찰 가능 항목
- **라우팅**: RouterModule, 가드, 리졸버
- **양식**: 템플릿 기반 반응형 양식
- **NgRx**: Redux 스타일 상태 관리
### 빌드 도구 및 번들러
- **Webpack**: 모듈 번들링, 코드 분할, 로더, 플러그인
- **Vite**: 기본 ES 모듈을 사용하는 빠른 빌드 도구
- **Parcel**: 구성이 필요 없는 번들러
- **롤업**: 라이브러리에 최적화됨
- **esbuild**: 매우 빠른 JavaScript 번들러
- **바벨**: 이전 버전과의 호환성을 위한 JavaScript 트랜스파일러
- **PostCSS**: 플러그인을 사용한 CSS 처리
### CSS 프레임워크 및 라이브러리
- **부트스트랩**: 구성 요소 라이브러리, 그리드 시스템, 유틸리티
- **Tailwind CSS**: 유틸리티 우선 CSS 프레임워크
- **머티리얼 UI**: Google의 머티리얼 디자인 구현
- **차크라 UI**: 접근 가능한 구성 요소 라이브러리
- **Ant Design**: 엔터프라이즈급 UI 구성 요소
- **스타일이 지정된 구성요소**: CSS-in-JS 라이브러리
- **Emotion**: 소스 맵이 포함된 CSS-in-JS
## 백엔드 개발
### 서버측 언어
#### Node.js
- **런타임**: 서버의 JavaScript(V8 엔진)
- **Express.js**: 최소 웹 프레임워크, 미들웨어 아키텍처
- **NestJS**: Angular에서 영감을 받은 아키텍처, TypeScript
- **Fastify**: 고성능 프레임워크
- **Koa**: 동일한 제작자의 Modern Express
- **패키지 관리**: npm, Yarn, pnpm
#### 파이썬
- **Django**: 모든 기능을 갖춘 프레임워크, ORM, 관리 패널, 배터리 포함
- **Flask**: 마이크로프레임워크, 확장 생태계
- **FastAPI**: 최신 비동기식 자동 API 문서
- **피라미드**: 유연하고 확장 가능한 프레임워크
#### 기타 백엔드 언어
- **Ruby on Rails**: 컨벤션 오버 구성, ActiveRecord ORM
- **Java Spring**: 엔터프라이즈 프레임워크, 종속성 주입
- **PHP Laravel**: 우아한 구문, Eloquent ORM, 블레이드 템플릿
- **Go Gin**: 고성능, 최소 프레임워크
- **Rust Actix**: 메모리 안전성, 성능
- **C# ASP.NET Core**: 크로스 플랫폼, 엔터프라이즈 기능
### 데이터베이스 통합
#### ORM(객체 관계형 매핑)
- **Sequelize**: SQL 데이터베이스용 Node.js ORM
- **Prisma**: 유형이 안전한 데이터베이스 액세스, 자동 생성 클라이언트
- **SQLAlchemy**: Python SQL 도구 키트 및 ORM
- **ActiveRecord**: Ruby on Rails ORM
- **최대 절전 모드**: Java ORM
- **엔티티 프레임워크**: .NET ORM
#### 데이터베이스 드라이버
- **pg**: Node.js용 PostgreSQL 클라이언트
- **mysql2**: Promise가 포함된 MySQL 클라이언트
- **pymongo**: Python용 MongoDB 드라이버
- **redis**: 다국어용 Redis 클라이언트
### API 개발
#### REST API
- **HTTP 메소드**: GET, POST, PUT, PATCH, DELETE
- **상태 코드**: 200, 201, 400, 401, 403, 404, 500
- **리소스 명명**: 명사, 복수형, 계층형
- **버전 관리**: URL 경로, 헤더, 쿼리 매개변수
- **인증**: JWT, OAuth, API 키
- **문서**: OpenAPI/Swagger, Postman
#### GraphQL
- **스키마 정의**: 유형, 쿼리, 변형, 구독
- **Resolvers**: 필드 수준 데이터 가져오기
- **Apollo 서버**: GraphQL 서버 구현
- **릴레이**: Facebook의 GraphQL 클라이언트
- **장점**: 오버페칭 없음, 단일 엔드포인트, 강력한 타이핑
#### gRPC
- **프로토콜 버퍼**: 인터페이스 정의 언어
- **HTTP/2**: 양방향 스트리밍
- **사용 사례**: 마이크로서비스 통신, 실시간 애플리케이션
### 인증 및 승인
- **세션 기반**: 쿠키, 서버측 세션
- **토큰 기반**: JWT(JSON 웹 토큰), 상태 비저장
- **OAuth 2.0**: 인증 프레임워크, 타사 로그인
- **OpenID Connect**: OAuth 2.0의 ID 레이어
- **SAML**: 엔터프라이즈 싱글 사인온(SSO)
- **비밀번호 해싱**: bcrypt, argon2, scrypt
- **다단계 인증**: TOTP, SMS, 이메일 코드
## DevOps 및 배포
### 버전 관리
- **Git**: 분산 버전 제어
- **GitHub/GitLab/Bitbucket**: 저장소 호스팅
- **분기 전략**: Git Flow, GitHub Flow, 트렁크 기반 개발
- **CI/CD**: 자동화된 테스트 및 배포 파이프라인
### 컨테이너화
- **Docker**: 컨테이너 런타임, Dockerfile, 이미지
- **Docker Compose**: 다중 컨테이너 오케스트레이션
- **컨테이너 레지스트리**: Docker Hub, AWS ECR, Google GCR
- **모범 사례**: 다단계 빌드, 최소 기본 이미지
### 오케스트레이션
- **Kubernetes**: 컨테이너 오케스트레이션, 포드, 서비스, 배포
- **헬름**: Kubernetes 패키지 관리자
- **서비스 메시**: 마이크로서비스 네트워킹을 위한 Istio, Linkerd
### 클라우드 플랫폼
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, Cloud Storage, Cloud Functions, GKE
- **Azure**: 가상 머신, Blob Storage, 함수, AKS
- **Vercel**: 프런트엔드 배포, 서버리스 기능
- **Netlify**: 정적 사이트 호스팅, 서버리스 기능
- **Heroku**: 서비스형 플랫폼(PaaS)
- **DigitalOcean**: 단순화된 클라우드 인프라
### CI/CD 파이프라인
- **GitHub 작업**: 워크플로 자동화
- **GitLab CI**: 지속적인 통합 내장
- **Jenkins**: 확장 가능한 자동화 서버
- **CircleCI**: 클라우드 기반 CI/CD
- **Travis CI**: 지속적인 통합 서비스
- **ArgoCD**: Kubernetes를 위한 GitOps 지속적 전달
### 모니터링 및 로깅
- **애플리케이션 성능**: New Relic, Datadog, AppDynamics
- **오류 추적**: Sentry, Rollbar, Bugsnag
- **로깅**: ELK 스택(Elasticsearch, Logstash, Kibana), Splunk
- **가동시간 모니터링**: Pingdom, UptimeRobot
- **분석**: Google Analytics, Mixpanel, Amplitude
## 웹 성능
### 최적화 기술
- **코드 분할**: 지연 로딩, 동적 가져오기
- **Tree Shaking**: 사용하지 않는 코드 제거
- **축소**: 파일 크기 줄이기
- **압축**: Gzip, Brotli
- **캐싱**: 브라우저 캐시, CDN, 서비스 워커
- **이미지 최적화**: WebP, AVIF, 지연 로딩, 반응형 이미지
- **중요한 CSS**: 스크롤 없이 볼 수 있는 스타일 인라인
- **데이터베이스 최적화**: 인덱싱, 쿼리 최적화, 연결 풀링
### 핵심 웹 바이탈
- **LCP(Largest Contentful Paint)**: 로딩 성능(<2.5s)
- **FID(첫 번째 입력 지연)**: 상호작용성(<100ms)
- **CLS(Cumulative Layout Shift)**: 시각적 안정성(<0.1)
- **INP(다음 페인트에 대한 상호작용)**: 반응성 측정항목
### 콘텐츠 전송 네트워크(CDN)
- **Cloudflare**: 보안, 성능, DNS
- **Akamai**: Enterprise CDN
- **Amazon CloudFront**: AWS CDN
- **Fastly**: 엣지 클라우드 플랫폼
- **StackPath**: 엣지 서비스
## 웹 보안
### 일반적인 취약점(OWASP 상위 10개)
- **인젝션**: SQL 인젝션, 명령어 인젝션
- **깨진 인증**: 세션 하이재킹, 크리덴셜 스터핑
- **민감한 데이터 노출**: 암호화되지 않은 데이터, 약한 암호화
- **XML 외부 엔터티(XXE)**: XML 파서 취약점
- **접근 통제 실패**: 권한 상승, 무단 접속
- **보안 잘못된 구성**: 기본 자격 증명, 자세한 오류
- **교차 사이트 스크립팅(XSS)**: 반영, 저장, DOM 기반
- **안전하지 않은 역직렬화**: 객체 주입 공격
- **알려진 취약점이 있는 구성요소 사용**: 오래된 종속성
- **불충분한 로깅 및 모니터링**: 감지되지 않은 위반
### 보안 모범 사례
- **HTTPS**: TLS/SSL 암호화, HSTS
- **콘텐츠 보안 정책(CSP)**: XSS 공격 방지
- **입력 유효성 검사**: 사용자 입력을 삭제합니다.
- **출력 인코딩**: 주입 공격 방지
- **CSRF 보호**: Anti-CSRF 토큰, SameSite 쿠키
- **속도 제한**: 무차별 대입 공격 방지
- **보안 헤더**: X-Frame-Options, X-Content-Type-Options
- **종속성 검색**: npm audit, Snyk, dependencyabot
## 테스트
### 테스트 유형
- **단위 테스트**: 개별 구성요소/기능
- **통합 테스트**: 구성 요소 상호 작용
- **엔드 투 엔드(E2E)**: 전체 사용자 워크플로우
- **시각적 회귀**: UI 변경 감지
- **성능 테스트**: 부하, 스트레스, 스파이크 테스트
- **접근성 테스트**: WCAG 준수
### 테스트 프레임워크
- **Jest**: JavaScript 테스트 프레임워크
- **모카**: 유연한 테스트 실행기
- **pytest**: Python 테스트 프레임워크
- **RSpec**: Ruby 테스트 프레임워크
- **JUnit**: Java 테스트 프레임워크
### E2E 테스트 도구
- **Selenium**: 브라우저 자동화
- **Cypress**: 최신 E2E 테스트
- **극작가**: 크로스 브라우저 자동화
- **Puppeteer**: 헤드리스 Chrome 컨트롤
## 접근성(a11y)
### WCAG 지침
- **인식 가능**: 텍스트 대체, 캡션, 적응형 콘텐츠
- **작동 가능**: 키보드 탐색, 충분한 시간, 발작 없음
- **이해 가능**: 읽기 가능하고 예측 가능하며 입력 지원
- **강건함**: 보조 기술과 호환 가능
### 구현
- **의미적 HTML**: 적절한 제목 계층 구조, 랜드마크
- **ARIA 속성**: 역할, 상태, 속성
- **포커스 관리**: 시각적 포커스 표시기, 논리적 탭 순서
- **색상 대비**: 텍스트의 최소 4.5:1 비율
- **스크린 리더 테스트**: NVDA, JAWS, VoiceOver
- **키보드 탐색**: 모든 대화형 요소에 액세스 가능
## 프로그레시브 웹 앱(PWA)
### PWA 기능
- **서비스 워커**: 오프라인 기능, 백그라운드 동기화
- **웹 앱 매니페스트**: 설치 프롬프트, 아이콘, 테마 색상
- **앱 셸**: 캐시된 UI 뼈대
- **푸시 알림**: 사용자 참여
- **반응형 디자인**: 모든 기기에서 작동
- **HTTPS 필수**: 보안 컨텍스트
### 도구
- **워크박스**: 서비스 워커 라이브러리
- **Lighthouse**: PWA 감사
- **PWA Builder**: 매니페스트 및 아이콘 생성
## 새로운 기술
### 웹어셈블리(Wasm)
- **목적**: 브라우저에서 컴파일된 코드를 거의 기본 속도로 실행합니다.
- **언어**: C++, Rust, Go 컴파일 대상
- **사용 사례**: 게임, 비디오 편집, 암호화, ML 추론
### 서버리스 아키텍처
- **서비스로서의 기능**: AWS Lambda, Azure Functions, Google Cloud Functions
- **이점**: 서버 관리 불필요, 자동 확장, 종량제 결제
- **고려사항**: 콜드 스타트, 공급업체 종속, 디버깅 복잡성
### 잼스택 아키텍처
- **자바스크립트**: 클라이언트측 상호작용
- **API**: 서버리스 기능, 타사 서비스
- **마크업**: 사전 구축된 정적 파일
- **도구**: Next.js, Gatsby, Hugo, Eleventy
- **이점**: 성능, 보안, 확장성, 개발자 경험
### 실시간 커뮤니케이션
- **WebSockets**: 양방향 통신
- **서버 전송 이벤트**: 서버-클라이언트 스트리밍
- **WebRTC**: P2P 비디오, 오디오, 데이터
- **사용 사례**: 채팅, 협업, 라이브 스트리밍, 게임
### 마이크로 프런트엔드
- **개념**: 마이크로서비스를 프런트엔드로 확장
- **접근 방식**: 빌드 타임, 런타임, 에지 측 통합
- **이점**: 독립적인 배포, 팀 자율성
- **도전과제**: 일관성, 성능, 복잡성