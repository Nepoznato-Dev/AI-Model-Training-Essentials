---
# Metadata
title: "Docker and Kubernetes Cheat Sheet"
description: "Docker, Docker Compose, Kubernetes, Helm cheat sheet"
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
tags: [docker, kubernetes, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "15 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Ściągawka Dockera i Kubernetesa
Praktyczny podręcznik dotyczący konteneryzacji aplikacji za pomocą Dockera i organizowania ich za pomocą Kubernetes. Zakłada podstawową znajomość wiersza poleceń.
---

## Podstawy Dockera
| Koncepcja | Opis |
|--------|------------|
| **Obraz** | Szablon tylko do odczytu z kodem aplikacji + zależnościami + bibliotekami systemu operacyjnego |
| **Pojemnik** | Uruchamianie instancji obrazu; izolowany proces |
| **Plik Dockera** | Przepis na budowanie wizerunku |
| **Rejestracja** | Przechowywanie obrazów (Docker Hub, ECR, GCR, GHCR) |
| **Objętość** | Pamięć trwała, która przetrwa ponowne uruchomienie kontenera |
| **Sieć** | Sieć wirtualna łącząca kontenery |
---

## Podstawowe polecenia Dockera
### Obrazy
| Polecenie | Opis |
|--------|------------|
| `docker build -t myapp:1.0 .`| Zbuduj obraz z pliku Dockerfile |
| `docker images`| Lista lokalnych obrazów |
| `docker pull nginx:latest`| Wyciągnij obraz z rejestru |
| `docker push myrepo/myapp:1.0`| Wypchnij obraz do rejestru |
| `docker rmi myapp:1.0`| Usuń obraz lokalny |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| Oznacz obraz do rejestru |
| `docker image prune -a`| Usuń wszystkie nieużywane obrazy |
### Kontenery
| Polecenie | Opis |
|--------|------------|
| `docker run -d -p 8080:80 nginx`| Uruchom kontener w tle, zmapuj port 8080 → 80 |
| `docker run -it ubuntu bash`| Uruchom interaktywnie z powłoką |
| `docker run --name web -e DB_HOST=db nginx`| Ustaw nazwę kontenera i zmienną środowiskową |
| `docker ps`| Lista działających kontenerów |
| `docker ps -a`| Lista wszystkich kontenerów (w tym zatrzymanych) |
| `docker stop web`| Zatrzymaj działający kontener |
| `docker start web`| Uruchom zatrzymany kontener |
| `docker rm web`| Usuń zatrzymany kontener |
| `docker exec -it web bash`| Otwórz powłokę wewnątrz działającego kontenera |
| `docker logs -f web`| Śledź dzienniki kontenerów |
| `docker inspect web`| Szczegółowe metadane kontenera (JSON) |
| `docker stats`| Wykorzystanie zasobów na żywo dla wszystkich kontenerów |
### Posprzątać
| Polecenie | Opis |
|--------|------------|
| `docker system prune -a`| Usuń wszystkie nieużywane kontenery, obrazy, sieci i buduj pamięć podręczną |
| `docker volume prune`| Usuń wszystkie nieużywane woluminy |
| `docker container prune`| Usuń wszystkie zatrzymane kontenery |
---

## Odniesienie do pliku Docker
### Wspólne instrukcje
| Instrukcja | Cel | Przykład |
|------------|---------|--------|
| `FROM`| Obraz podstawowy | `FROM python:3.12-slim`|
| `WORKDIR`| Ustaw katalog roboczy wewnątrz obrazu | `WORKDIR /app`|
| `COPY`| Skopiuj pliki z hosta do obrazu | `COPY requirements.txt .`|
| `ADD`| Podobnie jak COPY, ale także wyodrębnia pliki tar i obsługuje adresy URL | `ADD app.tar.gz /app/`|
| `RUN`| Wykonaj polecenie podczas kompilacji | `RUN pip install -r requirements.txt`|
| `CMD`| Domyślne polecenie podczas uruchamiania kontenera | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| Naprawiono polecenie; CMD staje się argumentami | `ENTRYPOINT ["python"]`|
| `ENV`| Ustaw zmienną środowiskową | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| Dokument, na którym porcie nasłuchuje aplikacja | `EXPOSE 8000`|
| `ARG`| Zmienna czasu kompilacji | `ARG VERSION=1.0`|
| `USER`| Przełącz na użytkownika innego niż root | `USER appuser`|
| `HEALTHCHECK`| Zdefiniuj polecenie sprawdzania stanu | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| Utwórz punkt montowania | `VOLUME /data`|
### Najlepsze praktyki
| Praktyka | Dlaczego |
|---------|-----|
| Użyj cienkich/podstawowych obrazów | Mniejsze obrazy = szybsze pociągnięcia, mniejsza powierzchnia ataku |
| Połącz polecenia RUN z`&&`| Zmniejsza warstwy obrazu |
| Najpierw skopiuj pliki zależności, a następnie kod | Wykorzystuje pamięć podręczną kompilacji Dockera |
| Użyj`.dockerignore`| Wyklucz`node_modules`,`.git`,`__pycache__`|
| Uruchom jako użytkownik inny niż root | Najlepsze praktyki w zakresie bezpieczeństwa |
| Użyj kompilacji wieloetapowych | Oddzielne środowisko kompilacji i środowiska wykonawczego; mniejszy obraz końcowy |
| Przypnij wersje obrazu bazowego | Powtarzalne kompilacje (`python:3.12.1-slim`, nie`python:latest`) |
### Przykład kompilacji wieloetapowej
```dockerfile
# Build stage
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# Production stage
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/main.js"]
```

---

## Tworzenie Dockera
Docker Compose definiuje aplikacje wielokontenerowe w jednym pliku YAML.
### Kluczowe polecenia
| Polecenie | Opis |
|--------|------------|
| `docker compose up -d`| Uruchom wszystkie usługi w tle |
| `docker compose down`| Zatrzymaj i usuń kontenery, sieci |
| `docker compose down -v`| Usuń także woluminy |
| `docker compose logs -f`| Śledź logi ze wszystkich usług |
| `docker compose ps`| Lista uruchomionych usług |
| `docker compose build`| Odbuduj obrazy |
| `docker compose exec web bash`| Uruchom polecenie w działającej usłudze |
| `docker compose pull`| Pobierz najnowsze zdjęcia |
### Przykładowy plik tworzenia
```yaml
services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://user:pass@db:5432/mydb
      - REDIS_URL=redis://cache:6379
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_started
    restart: unless-stopped

  db:
    image: postgres:16-alpine
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 5s
      timeout: 5s
      retries: 5

  cache:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  pgdata:
```

---

## Architektura Kubernetesa
| Składnik | Rola |
|----------|------|
| **Klaster** | Zestaw węzłów (maszyn) uruchamiających aplikacje kontenerowe |
| **Płaszczyzna sterująca** | Serwer API, harmonogram, menedżer kontrolera itp. (stan klastra) |
| **Węzeł** | Maszyna robocza (VM lub fizyczna), na której działają zasobniki |
| **Pod** | Najmniejsza jednostka; jeden lub więcej ściśle połączonych kontenerów |
| **Wdrożenie** | Zarządza replikami kapsuły; obsługuje aktualizacje kroczące |
| **Obsługa** | Stabilny punkt końcowy sieci dla zestawu podów |
| **Wejście** | Routing HTTP spoza klastra do usług |
| **Mapa konfiguracji** | Niejawne dane konfiguracyjne |
| **Sekret** | Wrażliwe dane (kodowane w formacie Base64) |
| **Przestrzeń nazw** | Izolacja logiczna w klastrze |
| **Stała objętość (PV)** | Zasób pamięci na poziomie klastra |
| **Trwałe roszczenie objętościowe (PVC)** | Prośba o przechowywanie przez kapsułę |
---

## Polecenia kubectl
### Informacje o klastrze
| Polecenie | Opis |
|--------|------------|
| `kubectl cluster-info`| Szczegóły punktu końcowego klastra |
| `kubectl get nodes`| Lista wszystkich węzłów |
| `kubectl get namespaces`| Lista przestrzeni nazw |
| `kubectl config current-context`| Pokaż bieżący kontekst klastra |
| `kubectl config use-context prod`| Zmień kontekst |
### Obciążenia
| Polecenie | Opis |
|--------|------------|
| `kubectl get pods`| Lista podów w bieżącej przestrzeni nazw |
| `kubectl get pods -A`| Lista podów we wszystkich przestrzeniach nazw |
| `kubectl get deployments`| Lista wdrożeń |
| `kubectl get services`| Lista usług |
| `kubectl get ingress`| Lista zasobów przychodzących |
| `kubectl describe pod <name>`| Szczegółowe informacje o podach (wydarzenia, status, specyfikacje) |
| `kubectl logs <pod>`| Wyświetl dzienniki podów |
| `kubectl logs -f <pod>`| Śledź dzienniki podów |
| `kubectl logs <pod> -c <container>`| Dzienniki z określonego kontenera w zasobniku wielokontenerowym |
| `kubectl exec -it <pod> -- bash`| Skorupa w kapsułę |
| `kubectl delete pod <name>`| Usuń poda (zostanie on odtworzony przez jego kontroler) |
| `kubectl rollout status deployment/<name>`| Sprawdź postęp wdrożenia |
| `kubectl rollout undo deployment/<name>`| Przywróć poprzednią wersję |
### Stosowanie konfiguracji
| Polecenie | Opis |
|--------|------------|
| `kubectl apply -f deployment.yaml`| Zastosuj manifest YAML |
| `kubectl apply -f ./dir/`| Zastosuj wszystkie pliki YAML w katalogu |
| `kubectl delete -f deployment.yaml`| Usuń zasoby zdefiniowane w pliku YAML |
| `kubectl scale deployment/web --replicas=5`| Skaluj wdrożenie |
| `kubectl set image deployment/web web=myapp:2.0`| Zaktualizuj obraz kontenera |
---

## Typowe manifesty Kubernetesa
### Zastosowanie
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
  labels:
    app: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: myapp:1.0
        ports:
        - containerPort: 8080
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 15
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
```

### Praca
```yaml
apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 8080
  type: ClusterIP    # Internal only
  # type: LoadBalancer  # External (cloud provider)
  # type: NodePort      # External via node IP + port
```

### Wejście
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web
            port:
              number: 80
```

---

## Podstawy steru
Helm jest menedżerem pakietów dla Kubernetes. Pakuje zasoby Kubernetes w wykresy wielokrotnego użytku.
| Polecenie | Opis |
|--------|------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| Dodaj repozytorium wykresów |
| `helm repo update`| Zaktualizuj indeks wykresu lokalnego |
| `helm search repo nginx`| Wyszukaj wykres |
| `helm install my-release bitnami/nginx`| Zainstaluj wykres |
| `helm install my-release bitnami/nginx --set replicaCount=3`| Zainstaluj z wartościami niestandardowymi |
| `helm install my-release bitnami/nginx -f values.yaml`| Zainstaluj z plikiem wartości |
| `helm list`| Lista zainstalowanych wersji |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| Uaktualnij wersję |
| `helm rollback my-release 1`| Przywróć poprzednią wersję |
| `helm uninstall my-release`| Odinstaluj wersję |
| `helm status my-release`| Pokaż status wydania |
---

## Krótki opis rozwiązywania problemów
| Problem | Polecenia do wypróbowania |
|------------|----------------|
| Pod nie uruchamia się | `kubectl describe pod <name>`→ sprawdź Wydarzenia |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ zobacz dlaczego się zawiesił |
| Błąd pobierania obrazu | Sprawdź nazwę obrazu, znacznik i poświadczenia rejestru |
| Usługa nieosiągalna | `kubectl get endpoints <service>`→ czy wybrano kapsuły? |
| OOMZabity | Zwiększ limity pamięci lub zoptymalizuj wykorzystanie pamięci aplikacji |
| Oczekujące strąki | `kubectl describe pod`→ sprawdź zasoby węzła, skażenia, powinowactwo |
| Problemy z DNS | `kubectl exec <pod> -- nslookup kubernetes.default`|