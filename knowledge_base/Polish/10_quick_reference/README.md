# Szybkie odniesienie
Ustrukturyzowany zbiór ściągawek i skróconych przewodników po językach programowania, narzędziach wiersza poleceń, infrastrukturze i DevOps — zaprojektowany z myślą o szybkim wyszukiwaniu w codziennej pracy.
## Struktura
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

## Pliki według podkategorii
### Programowanie
| Plik | Opis |
|------|------------|
| [python_syntax.md](programming/python_syntax.md)| Ściągawka ze składni Pythona |
| [sql_quick_ref.md](programming/sql_quick_ref.md)| Odniesienie do zapytania SQL |
| [regular_expressions.md](programming/regular_expressions.md)| Składnia wyrażeń regularnych, typowe wzorce, użycie specyficzne dla języka |
| [git_commands.md](programming/git_commands.md)| Polecenia i przepływy pracy Git |
### Infrastruktura
| Plik | Opis |
|------|------------|
| [linux_commands.md](infrastructure/linux_commands.md)| Informacje o wierszu poleceń systemu Linux |
| [bash_and_shell_scripting.md](infrastructure/bash_and_shell_scripting.md)| Skrypty Bash, przetwarzanie tekstu, przydatne jednowierszowe |
| [docker_and_kubernetes.md](infrastructure/docker_and_kubernetes.md)| Docker, Docker Compose, Kubernetes, ściągawka Helm |
| [cloud_services_comparison.md](infrastructure/cloud_services_comparison.md)| Porównanie AWS, Azure i GCP |
| [ansible_quick_ref.md](infrastructure/ansible_quick_ref.md)| Podręczniki Ansible, moduły, role, automatyzacja |
| [terraform_quick_ref.md](infrastructure/terraform_quick_ref.md)| Koncepcje IaC, polecenia Terraform, zarządzanie stanem |
| [cicd_pipeline_config.md](infrastructure/cicd_pipeline_config.md)| GitHub Actions, GitLab CI, Jenkins, wzorce YAML potoku |
| [prometheus_and_grafana.md](infrastructure/prometheus_and_grafana.md)| PromQL, eksporterzy, dashboardy, alerty |
## Sugerowane ścieżki czytania
### **Ścieżka inżyniera DevOps**
1.`infrastructure/linux_commands.md`— Podstawy Linuksa
2.`infrastructure/bash_and_shell_scripting.md`— skrypty powłoki
3.`infrastructure/docker_and_kubernetes.md`— Kontenery i orkiestracja
4.`infrastructure/cicd_pipeline_config.md`— rurociągi CI/CD
5.`infrastructure/terraform_quick_ref.md`— Infrastruktura jako kod
6.`infrastructure/prometheus_and_grafana.md`— Monitorowanie
### **Ścieżka Developer Essentials**
1.`programming/python_syntax.md`— odniesienie do Pythona
2.`programming/sql_quick_ref.md`— Zapytania do bazy danych
3.`programming/git_commands.md`— Kontrola wersji
4.`programming/regular_expressions.md`— Dopasowywanie wzorców