---
# Metadata
title: "Terraform and Infrastructure as Code"
description: "IaC concepts, Terraform commands, state management, modules"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
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
# Terraforma i infrastruktura jako kod
Terraform to najszerzej stosowane narzędzie Infrastructure as Code (IaC) — umożliwia definiowanie infrastruktury chmury (serwery, bazy danych, sieci, uprawnienia) w deklaratywnych plikach konfiguracyjnych, które można wersjonować, przeglądać, testować i automatyzować. Zamiast klikać w konsoli w chmurze, piszesz kod opisujący pożądany stan infrastruktury, a Terraform ustala, jakie zmiany należy wprowadzić.
---

## Podstawowe pojęcia
| Koncepcja | Opis |
|--------|------------|
| **Dostawca** | Wtyczka zarządzająca konkretną platformą chmurową (AWS, Azure, GCP itp.) |
| **Zasób** | Obiekt infrastruktury (serwer, baza danych, sieć) |
| **Stan** | Rejestr Terraform dotyczący istniejącej infrastruktury; przechowywane w pliku stanu |
| **Planuj** | Podgląd zmian jakie wprowadzi Terraform |
| **Zastosuj** | Wykonaj plan; tworzyć/aktualizować/niszczyć infrastrukturę |
| **Moduł** | Zbiór zasobów wielokrotnego użytku |
| **Zmienna** | Parametr wejściowy dla konfiguracji |
| **Wyjście** | Wartość wyeksportowana z modułu lub konfiguracji |
| **Źródło danych** | Odczyt informacji z istniejącej infrastruktury |
---

## Podstawowy przepływ pracy
| Krok | Polecenie | Opis |
|------|---------|------------|
| **1. Zapisz konfigurację** | Utwórz pliki`.tf`| Zdefiniuj dostawców, zasoby, zmienne |
| **2. Zainicjuj** | `terraform init`| Dostawcy pobierania; skonfiguruj backend |
| **3. Formatuj** | `terraform fmt`| Standaryzuj formatowanie |
| **4. Zatwierdź** | `terraform validate`| Sprawdź składnię i konfigurację |
| **5. Zaplanuj** | `terraform plan`| Podgląd zmian (praca próbna) |
| **6. Zastosuj** | `terraform apply`| Utwórz lub zaktualizuj infrastrukturę |
| **7. Zniszcz** | `terraform destroy`| Zburz całą zarządzaną infrastrukturę |
---

## Typowe polecenia
| Polecenie | Opis |
|--------|------------|
| `terraform init`| Zainicjuj katalog roboczy; pobierz dostawców i moduły |
| `terraform plan`| Pokaż jakie zmiany zostaną wprowadzone |
| `terraform apply`| Zastosuj zmiany; dodaj `-auto-approve`, aby pominąć potwierdzenie |
| `terraform destroy`| Zniszcz wszystkie zarządzane zasoby |
| `terraform fmt`| Sformatuj pliki konfiguracyjne do standardowego stylu |
| `terraform validate`| Sprawdź składnię konfiguracji |
| `terraform output`| Pokaż wartości wyjściowe |
| `terraform state list`| Lista wszystkich zasobów w stanie |
| `terraform state show <resource>`| Pokaż szczegóły konkretnego zasobu |
| `terraform import <resource> <id>`| Importuj istniejącą infrastrukturę do stanu |
| `terraform taint <resource>`| Oznacz zasób rekreacyjny przy następnym zastosowaniu |
| `terraform refresh`| Zaktualizuj stan, aby dopasować go do rzeczywistej infrastruktury |
| `terraform graph`| Wygeneruj wizualny wykres zależności (format DOT) |
| `terraform console`| Interaktywna konsola do testowania wyrażeń |
---

## Zarządzanie stanem
| Najlepsza praktyka | Opis |
|-------------|------------|
| **Stan zdalny** | Przechowuj stan w S3, GCS, Azure Blob lub Terraform Cloud — nigdy lokalnie |
| **Blokowanie stanu** | Użyj DynamoDB (backend S3) lub blokady natywnej, aby zapobiec jednoczesnym modyfikacjom |
| **Szyfrowanie stanu** | Włącz szyfrowanie w stanie spoczynku dla plików stanu (zawierają wrażliwe dane) |
| **Separacja państwa** | Użyj oddzielnych plików stanu dla różnych środowisk lub zespołów |
| **Kopia zapasowa stanu** | Zdalne backendy automatycznie określają stan wersji; pozostaw tę opcję włączoną |
| **Nigdy nie edytuj stanu ręcznie** | Zamiast tego użyj`terraform state mv`,`rm`,`import`|
---

## Struktura modułu
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

## Typy zmiennych
| Wpisz | Przykład | Przypadek użycia |
|------|---------|--------------|
| **ciąg** | `variable "region" { type = string }`| Pojedyncza wartość tekstowa |
| **numer** | `variable "count" { type = number }`| Wartość liczbowa |
| **buł** | `variable "enable" { type = bool }`| Flaga prawda/fałsz |
| **lista** | `variable "zones" { type = list(string) }`| Zamówiona kolekcja |
| **mapa** | `variable "tags" { type = map(string) }`| Pary klucz-wartość |
| **obiekt** | `variable "config" { type = object({...}) }`| Konfiguracja strukturalna |
---

## Typowe wzorce
| Wzór | Opis |
|--------|------------|
| **Policz** | `count = 3`tworzy wiele instancji zasobu |
| **Dla każdego** | `for_each = var.items`iteruje po mapie lub zestawie |
| **Bloki dynamiczne** | Generuj powtarzające się zagnieżdżone bloki (np. reguły ingresu) |
| **Wartości lokalne** | `locals { ... }`dla wartości obliczonych i ograniczania powtórzeń |
| **Źródła danych** | Przeczytaj istniejącą infrastrukturę (np. znajdź istniejącą VPC) |
| **Dostawcy** | Uruchamiaj skrypty na zasobach po utworzeniu (używaj oszczędnie) |
| **Przestrzenie robocze** | Oddzielny stan dla różnych środowisk w ramach tej samej konfiguracji |
---

## Rozwiązywanie problemów
| Problem | Rozwiązanie |
|--------|----------|
| **Dryf stanu** | Uruchom `terraform plan`, aby zobaczyć różnice; `terraform apply`do uzgodnienia |
| **Stan zablokowany** | Sprawdź, kto ma zamek; użyj `terraform force-unlock`, jeśli jest bezpieczny |
| **Błędy dostawcy** | Sprawdź referencje; zaktualizuj wersję dostawcy; sprawdź limity API |
| **Konflikty importu** | Zasób już w stanie; użyj najpierw`terraform state rm`|
| **Zależności cykliczne** | Restrukturyzacja zasobów; używaj ostrożnie`depends_on`|
| **Duży stan** | Podzielony na moduły; użyj`-target`dla operacji częściowych |
---

## Streszczenie
Terraform zarządza infrastrukturą poprzez deklaratywne pliki konfiguracyjne. Przepływ pracy jest następujący: zapisz konfigurację → init → plan → zastosuj. Stan śledzi to, co istnieje i musi być przechowywany zdalnie z blokadą. Moduły umożliwiają ponowne wykorzystanie. Zmienne parametryzują konfiguracje. Kluczowe zasady to: traktuj infrastrukturę jak kod (kontrola wersji, przegląd, test); nigdy nie edytuj stanu ręcznie; zaplanuj przed złożeniem wniosku; użyj stanu zdalnego z blokowaniem; i konfiguracje struktur z modułami ułatwiającymi konserwację.