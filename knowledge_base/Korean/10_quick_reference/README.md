# 빠른 참조
프로그래밍 언어, 명령줄 도구, 인프라 및 DevOps에 대한 체계화된 치트 시트 및 빠른 참조 가이드 모음으로 일상 업무 중 빠른 조회를 위해 설계되었습니다.
## 구조
```
10_quick_reference/
├── README.md                          ← You are here
├── programming/                       ← Language and tool syntax
│   ├── python_syntax.md                  Python syntax cheat sheet
│   ├── sql_quick_ref.md                  SQL query reference
│   ├── regular_expressions.md            Regex syntax and common patterns
│   └── git_commands.md                   Git commands and workflows
└── infrastructure/                    ← Systems, DevOps, and cloud
    ├── linux_commands.md                  Linux command line reference
    ├── bash_and_shell_scripting.md        Bash scripting and one-liners
    ├── docker_and_kubernetes.md           Docker, Compose, Kubernetes, Helm
    ├── cloud_services_comparison.md       AWS vs Azure vs GCP comparison
    ├── ansible_quick_ref.md               Ansible playbooks and automation
    ├── terraform_quick_ref.md             Terraform commands and IaC
    ├── cicd_pipeline_config.md            GitHub Actions, GitLab CI, Jenkins
    └── prometheus_and_grafana.md          PromQL, dashboards, alerting
```

## 하위 범주별 파일
### 프로그래밍
| 파일 | 설명 |
|------|-------------|
| [python_syntax.md](programming/python_syntax.md)| Python 구문 치트 시트 |
| [sql_quick_ref.md](programming/sql_quick_ref.md)| SQL 쿼리 참조 |
| [regular_expressions.md](programming/regular_expressions.md)| 정규식 구문, 일반적인 패턴, 언어별 사용법 |
| [git_commands.md](programming/git_commands.md)| Git 명령 및 워크플로 |
### 인프라
| 파일 | 설명 |
|------|-------------|
| [linux_commands.md](infrastructure/linux_commands.md)| Linux 명령줄 참조 |
| [bash_and_shell_scripting.md](infrastructure/bash_and_shell_scripting.md)| Bash 스크립팅, 텍스트 처리, 유용한 한 줄짜리 |
| [docker_and_kubernetes.md](infrastructure/docker_and_kubernetes.md)| Docker, Docker Compose, Kubernetes, Helm 치트 시트 |
| [cloud_services_comparison.md](infrastructure/cloud_services_comparison.md)| AWS와 Azure와 GCP를 나란히 비교 |
| [ansible_quick_ref.md](infrastructure/ansible_quick_ref.md)| Ansible 플레이북, 모듈, 역할, 자동화 |
| [terraform_quick_ref.md](infrastructure/terraform_quick_ref.md)| IaC 개념, Terraform 명령, 상태 관리 |
| [cicd_pipeline_config.md](infrastructure/cicd_pipeline_config.md)| GitHub Actions, GitLab CI, Jenkins, 파이프라인 YAML 패턴 |
| [prometheus_and_grafana.md](infrastructure/prometheus_and_grafana.md)| PromQL, 수출업체, 대시보드, 경고 |
## 권장 읽기 경로
### **DevOps 엔지니어 경로**
1.`infrastructure/linux_commands.md`— 리눅스 기초
2.`infrastructure/bash_and_shell_scripting.md`— 쉘 스크립팅
3.`infrastructure/docker_and_kubernetes.md`— 컨테이너 및 오케스트레이션
4.`infrastructure/cicd_pipeline_config.md`— CI/CD 파이프라인
5.`infrastructure/terraform_quick_ref.md`— 코드형 인프라
6.`infrastructure/prometheus_and_grafana.md`— 모니터링
### **개발자 필수 과정**
1.`programming/python_syntax.md`— Python 참조
2.`programming/sql_quick_ref.md`— 데이터베이스 쿼리
3.`programming/git_commands.md`- 버전 관리
4.`programming/regular_expressions.md`— 패턴 일치