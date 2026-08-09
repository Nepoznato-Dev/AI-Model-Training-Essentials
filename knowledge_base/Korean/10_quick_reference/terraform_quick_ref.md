---
# Metadata
title: "Terraform and Infrastructure as Code"
description: "IaC concepts, Terraform commands, state management, modules"
category: "Quick Reference"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [terraform, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Terraform 및 코드형 인프라
Terraform은 가장 널리 사용되는 IaC(Infrastructure as Code) 도구입니다. 이를 사용하면 버전 관리, 검토, 테스트 및 자동화가 가능한 선언적 구성 파일에서 클라우드 인프라(서버, 데이터베이스, 네트워크, 권한)를 정의할 수 있습니다. 클라우드 콘솔을 클릭하는 대신 원하는 인프라 상태를 설명하는 코드를 작성하면 Terraform이 어떤 변경 사항을 적용할지 파악합니다.
---

## 핵심 개념
| 개념 | 설명 |
|---------|-------------|
| **공급자** | 특정 클라우드 플랫폼(AWS, Azure, GCP 등)을 관리하는 플러그인 |
| **리소스** | 인프라 객체(서버, 데이터베이스, 네트워크) |
| **상태** | 어떤 인프라가 존재하는지에 대한 Terraform의 기록입니다. 상태 파일에 저장됨 |
| **계획** | Terraform이 어떤 변화를 가져올지 미리보기 |
| **신청** | 계획을 실행합니다. 인프라 생성/업데이트/파괴 |
| **모듈** | 재사용 가능한 리소스 컬렉션 |
| **변수** | 구성을 위한 입력 매개변수 |
| **출력** | 모듈 또는 구성에서 내보낸 값 |
| **데이터 소스** | 기존 인프라에서 정보 읽기 |
---

## 기본 작업 흐름
| 단계 | 명령 | 설명 |
|------|---------|-------------|
| **1. 구성 쓰기** |`.tf`파일 만들기 | 공급자, 리소스, 변수 정의 |
| **2. 초기화** | `terraform init`| 다운로드 공급자; 백엔드 설정 |
| **3. 형식** | `terraform fmt`| 서식 표준화 |
| **4. 유효성 검사** | `terraform validate`| 구문 및 구성 확인 |
| **5. 계획** | `terraform plan`| 변경사항 미리보기(시험 실행) |
| **6. 신청** | `terraform apply`| 인프라 생성 또는 업데이트 |
| **7. 파괴** | `terraform destroy`| 모든 관리형 인프라 해체 |
---

## 일반적인 명령
| 명령 | 설명 |
|---------|-------------|
| `terraform init`| 작업 디렉토리를 초기화합니다. 공급자 및 모듈 다운로드 |
| `terraform plan`| 어떤 변경사항이 적용될지 표시 |
| `terraform apply`| 변경 사항을 적용합니다. 확인을 건너뛰려면 `-auto-approve`를 추가하세요 |
| `terraform destroy`| 모든 관리 리소스 삭제 |
| `terraform fmt`| 구성 파일을 표준 스타일로 포맷 |
| `terraform validate`| 구성 구문 유효성 검사 |
| `terraform output`| 출력 값 표시 |
| `terraform state list`| 상태의 모든 리소스 나열 |
| `terraform state show <resource>`| 특정 리소스의 세부정보 표시 |
| `terraform import <resource> <id>`| 기존 인프라를 상태로 가져오기 |
| `terraform taint <resource>`| 다음 신청 시 레크리에이션을 위한 리소스 표시 |
| `terraform refresh`| 실제 인프라와 일치하도록 상태 업데이트 |
| `terraform graph`| 시각적 종속성 그래프 생성(DOT 형식) |
| `terraform console`| 표현식 테스트를 위한 대화형 콘솔 |
---

## 상태 관리
| 모범 사례 | 설명 |
|---------------|-------------|
| **원격 상태** | S3, GCS, Azure Blob 또는 Terraform Cloud에 상태를 저장하며 로컬로는 저장하지 않음 |
| **상태 잠금** | DynamoDB(S3 백엔드) 또는 기본 잠금을 사용하여 동시 수정 방지 |
| **상태 암호화** | 상태 파일에 대한 저장 암호화 활성화(민감한 데이터 포함) |
| **국가 분리** | 다양한 환경이나 팀에 대해 별도의 상태 파일 사용 |
| **상태 백업** | 원격 백엔드는 자동으로 버전 상태를 유지합니다. 이것을 활성화된 상태로 유지 |
| **상태를 수동으로 편집하지 마세요** | 대신`terraform state mv`,`rm`,`import`를 사용하세요 |
---

## 모듈 구조
```
module/
├── main.tf          # Primary resources
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider and Terraform version constraints
├── README.md        # Documentation
└── examples/        # Example usage
    └── basic/
        └── main.tf
```

---

## 변수 유형
| 유형 | 예 | 사용 사례 |
|------|---------|----------|
| **문자열** | `variable "region" { type = string }`| 단일 텍스트 값 |
| **번호** | `variable "count" { type = number }`| 숫자 값 |
| **부끄러운** | `variable "enable" { type = bool }`| 참/거짓 플래그 |
| **목록** | `variable "zones" { type = list(string) }`| 주문 컬렉션 |
| **지도** | `variable "tags" { type = map(string) }`| 키-값 쌍 |
| **객체** | `variable "config" { type = object({...}) }`| 구조화된 구성 |
---

## 일반적인 패턴
| 패턴 | 설명 |
|---------|-------------|
| **카운트** |  `count = 3`는 리소스의 여러 인스턴스를 작성합니다. |
| **각각** |  `for_each = var.items`는 지도 또는 세트를 반복합니다 |
| **동적 블록** | 반복적으로 중첩된 블록 생성(예: 수신 규칙) |
| **로컬 값** |  계산된 값과 반복 감소를 위한`locals { ... }`|
| **데이터 소스** | 기존 인프라 읽기(예: 기존 VPC 찾기) |
| **제공자** | 생성 후 리소스에 대해 스크립트 실행(아껴서 사용) |
| **작업공간** | 동일한 구성 내에서 서로 다른 환경에 대한 별도의 상태 |
---

## 문제 해결
| 문제 | 솔루션 |
|---------|----------|
| **상태 드리프트** | `terraform plan`를 실행하여 차이점을 확인하세요. `terraform apply`화해하다 |
| **잠긴 상태** | 자물쇠를 갖고 있는 사람이 누구인지 확인하세요. 안전하다면 `terraform force-unlock`를 사용하세요 |
| **공급자 오류** | 자격 증명을 확인하십시오. 업데이트 공급자 버전; API 제한 확인 |
| **가져오기 충돌** | 리소스가 이미 상태입니다. 먼저 `terraform state rm`를 사용하세요 |
| **순환 종속성** | 자원 재구성 `depends_on`를 신중하게 사용하세요 |
| **큰 주** | 모듈로 분할합니다. 부분 작업에`-target`사용 |
---

## 요약
Terraform은 선언적 구성 파일을 통해 인프라를 관리합니다. 작업 흐름은 구성 쓰기 → 초기화 → 계획 → 적용입니다. 상태는 존재하는 것을 추적하며 잠금을 사용하여 원격으로 저장해야 합니다. 모듈을 사용하면 재사용이 가능합니다. 변수는 구성을 매개변수화합니다. 핵심 원칙은 다음과 같습니다: 인프라를 코드로 처리(버전 제어, 검토, 테스트); 상태를 수동으로 편집하지 마십시오. 적용하기 전에 계획을 세우십시오. 잠금 기능이 있는 원격 상태를 사용합니다. 유지 관리를 위한 모듈을 갖춘 구조 구성.