<!--
---
# Metadata
title: "Docker and Kubernetes Cheat Sheet"
description: "Docker, Docker Compose, Kubernetes, Helm cheat sheet"
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

-->
# Docker と Kubernetes のチートシート
Docker を使用してアプリケーションをコンテナ化し、Kubernetes を使用してアプリケーションをオーケストレーションするための実践的なリファレンス。コマンド ラインの基本的な知識があることを前提としています。
---

## Docker の基礎
|コンセプト |説明 |
|----------|---------------|
| **画像** |アプリコード + 依存関係 + OS ライブラリを含む読み取り専用テンプレート |
| **コンテナ** |イメージの実行中のインスタンス。孤立したプロセス |
| **Dockerfile** |イメージを構築するためのレシピ |
| **レジストリ** |イメージ用ストレージ (Docker Hub、ECR、GCR、GHCR) |
| **ボリューム** |コンテナーの再起動後も存続する永続ストレージ |
| **ネットワーク** |コンテナを接続する仮想ネットワーク |
---

## 必須の Docker コマンド
### 画像
|コマンド |説明 |
|----------|---------------|
| `docker build -t myapp:1.0 .`| Dockerfile からイメージを構築する |
| `docker images`|ローカルイメージをリストする |
| `docker pull nginx:latest`|レジストリからイメージをプルする |
| `docker push myrepo/myapp:1.0`|イメージをレジストリにプッシュする |
| `docker rmi myapp:1.0`|ローカルイメージを削除する |
| `docker tag myapp:1.0 myrepo/myapp:1.0`|レジストリのイメージにタグを付ける |
| `docker image prune -a`|未使用のイメージをすべて削除 |
### コンテナ
|コマンド |説明 |
|----------|---------------|
| `docker run -d -p 8080:80 nginx`|バックグラウンドでコンテナを実行し、ポート 8080→80 をマップします。
| `docker run -it ubuntu bash`|シェルを使用して対話的に実行する |
| `docker run --name web -e DB_HOST=db nginx`|コンテナ名と環境変数を設定する |
| `docker ps`|実行中のコンテナをリストする |
| `docker ps -a`|すべてのコンテナをリストします (停止したコンテナも含む)。
| `docker stop web`|実行中のコンテナを停止する |
| `docker start web`|停止したコンテナを起動する |
| `docker rm web`|停止したコンテナを削除する |
| `docker exec -it web bash`|実行中のコンテナ内でシェルを開く |
| `docker logs -f web`|コンテナーのログを追跡する |
| `docker inspect web`|詳細なコンテナメタデータ (JSON) |
| `docker stats`|すべてのコンテナーのライブ リソース使用率 |
＃＃＃ 掃除
|コマンド |説明 |
|----------|---------------|
| `docker system prune -a`|未使用のコンテナー、イメージ、ネットワーク、およびビルド キャッシュをすべて削除します。
| `docker volume prune`|未使用のボリュームをすべて削除する |
| `docker container prune`|停止したコンテナをすべて削除します。
---

## Dockerfile リファレンス
### 共通の手順
|指示 |目的 |例 |
|-----------|-----------|----------|
| `FROM`|ベースイメージ | `FROM python:3.12-slim`|
| `WORKDIR`|イメージ内に作業ディレクトリを設定します | `WORKDIR /app`|
| `COPY`|ホストからイメージにファイルをコピー | `COPY requirements.txt .`|
| `ADD`| COPY と似ていますが、tar を抽出し、URL もサポートします。 `ADD app.tar.gz /app/`|
| `RUN`|ビルド中にコマンドを実行する | `RUN pip install -r requirements.txt`|
| `CMD`|コンテナ起動時のデフォルトコマンド | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`|修正されたコマンド。 CMD が引数になる | `ENTRYPOINT ["python"]`|
| `ENV`|環境変数を設定する | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`|アプリがリッスンするポートを文書化します。 `EXPOSE 8000`|
| `ARG`|ビルド時変数 | `ARG VERSION=1.0`|
| `USER`|非 root ユーザーに切り替える | `USER appuser`|
| `HEALTHCHECK`|ヘルスチェックコマンドを定義する | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`|マウントポイントを作成する | `VOLUME /data`|
### ベストプラクティス
|練習 |なぜ |
|----------|-----|
|スリム/ベース イメージを使用する |イメージが小さい = プルが速く、攻撃対象領域が小さい |
| RUN コマンドと`&&`を組み合わせる |画像レイヤーを減らす |
|最初に依存関係ファイルをコピーしてからコードを記述します。 Docker のビルド キャッシュを活用 |
|`.dockerignore`を使用する |`node_modules`、`.git`、`__pycache__`を除外する |
|非 root ユーザーとして実行 |セキュリティのベストプラクティス |
|マルチステージ ビルドを使用する |ビルドとランタイムを分離する。小さい最終イメージ |
|ベースイメージのバージョンを固定する |再現可能なビルド (`python:latest`ではなく`python:3.12.1-slim`) |
### マルチステージビルドの例
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

## Docker Compose
Docker Compose は、単一の YAML ファイルでマルチコンテナー アプリケーションを定義します。
### 主要なコマンド
|コマンド |説明 |
|----------|---------------|
| `docker compose up -d`|すべてのサービスをバックグラウンドで開始する |
| `docker compose down`|コンテナー、ネットワークの停止と削除 |
| `docker compose down -v`|ボリュームも削除します |
| `docker compose logs -f`|すべてのサービスのログを追跡する |
| `docker compose ps`|実行中のサービスをリストする |
| `docker compose build`|イメージを再構築する |
| `docker compose exec web bash`|実行中のサービスでコマンドを実行する |
| `docker compose pull`|最新のイメージをプルする |
### Compose ファイルの例
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

## Kubernetes アーキテクチャ
|コンポーネント |役割 |
|-----------|------|
| **クラスター** |コンテナ化されたアプリケーションを実行するノード (マシン) のセット |
| **コントロール プレーン** | API サーバー、スケジューラー、コントローラー マネージャー、etcd (クラスター状態) |
| **ノード** |ポッドを実行するワーカー マシン (VM または物理) |
| **ポッド** |最小単位。 1 つ以上の密結合コンテナ |
| **展開** |ポッドのレプリカを管理します。ローリングアップデートを処理します。
| **サービス** |ポッドのセットの安定したネットワーク エンドポイント |
| **イングレス** |クラスターの外部からサービスへの HTTP ルーティング |
| **構成マップ** |非機密構成データ |
| **秘密** |機密データ (base64 エンコード) |
| **名前空間** |クラスター内の論理分離 |
| **永続ボリューム (PV)** |クラスターレベルのストレージリソース |
| **PersistentVolumeClaim (PVC)** |ポッドによるストレージのリクエスト |
---

## kubectl コマンド
### クラスター情報
|コマンド |説明 |
|----------|---------------|
| `kubectl cluster-info`|クラスターエンドポイントの詳細 |
| `kubectl get nodes`|すべてのノードをリストする |
| `kubectl get namespaces`|名前空間のリスト |
| `kubectl config current-context`|現在のクラスターコンテキストを表示 |
| `kubectl config use-context prod`|コンテキストを切り替える |
### ワークロード
|コマンド |説明 |
|----------|---------------|
| `kubectl get pods`|現在の名前空間内のポッドを一覧表示する |
| `kubectl get pods -A`|すべての名前空間にわたるポッドをリストする |
| `kubectl get deployments`|デプロイメントのリストを表示 |
| `kubectl get services`|サービスの一覧 |
| `kubectl get ingress`|入力リソースをリストする |
| `kubectl describe pod <name>`|ポッドの詳細情報 (イベント、ステータス、仕様) |
| `kubectl logs <pod>`|ポッドのログを表示する |
| `kubectl logs -f <pod>`|ポッドのログをフォローする |
| `kubectl logs <pod> -c <container>`|マルチコンテナ ポッド内の特定のコンテナからのログ |
| `kubectl exec -it <pod> -- bash`|ポッドにシェルを入れる |
| `kubectl delete pod <name>`|ポッドを削除します (コントローラーによって再作成されます)。
| `kubectl rollout status deployment/<name>`|ロールアウトの進行状況を確認する |
| `kubectl rollout undo deployment/<name>`|以前のバージョンにロールバックする |
### 構成の適用
|コマンド |説明 |
|----------|---------------|
| `kubectl apply -f deployment.yaml`| YAML マニフェストを適用する |
| `kubectl apply -f ./dir/`|ディレクトリ内のすべての YAML ファイルを適用します。
| `kubectl delete -f deployment.yaml`| YAML ファイルで定義されたリソースを削除する |
| `kubectl scale deployment/web --replicas=5`|展開をスケールする |
| `kubectl set image deployment/web web=myapp:2.0`|コンテナイメージの更新 |
---

## 共通の Kubernetes マニフェスト
### 導入
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

＃＃＃ サービス
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

### イングレス
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

## ヘルムの基本
Helm は Kubernetes のパッケージ マネージャーです。 Kubernetes リソースを再利用可能なチャートにパッケージ化します。
|コマンド |説明 |
|----------|---------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`|チャートリポジトリを追加する |
| `helm repo update`|ローカル チャート インデックスを更新 |
| `helm search repo nginx`|チャートを検索 |
| `helm install my-release bitnami/nginx`|チャートをインストールする |
| `helm install my-release bitnami/nginx --set replicaCount=3`|カスタム値を使用してインストールする |
| `helm install my-release bitnami/nginx -f values.yaml`|値ファイルを使用してインストールする |
| `helm list`|インストールされているリリースをリストする |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`|リリースをアップグレードする |
| `helm rollback my-release 1`|以前のリビジョンにロールバックする |
| `helm uninstall my-release`|リリースをアンインストールする |
| `helm status my-release`|リリースステータスを表示 |
---

## トラブルシューティングのクイック リファレンス
|問題 |試してみるコマンド |
|----------|----------------|
|ポッドが起動しない | `kubectl describe pod <name>`→ イベントをチェック |
|クラッシュループバックオフ | `kubectl logs <pod> --previous`→ クラッシュした理由を確認 |
|画像プルエラー |イメージ名、タグ、およびレジストリ資格情報を確認する |
|サービスにアクセスできません | `kubectl get endpoints <service>`→ ポッドが選択されていますか? |
| OOMキル |メモリ制限を増やすか、アプリのメモリ使用量を最適化する |
|保留中のポッド | `kubectl describe pod`→ ノードのリソース、テイント、アフィニティをチェック |
| DNS の問題 | `kubectl exec <pod> -- nslookup kubernetes.default`|