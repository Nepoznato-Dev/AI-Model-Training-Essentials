---
# Metadata
title: "DevOps and CI/CD"
description: "CI/CD pipelines, Docker, Kubernetes, Terraform, GitOps"
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
tags: [devops, cicd, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "11 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# DevOps と CI/CD
DevOps は、チームがソフトウェアをより迅速かつ確実に提供できるようにする文化的な哲学、実践、ツールを組み合わせたものです。これにより、開発者 (変更を出荷したい) と運用者 (安定性を求める) の間の壁が取り払われます。 CI/CD (継続的インテグレーションと継続的デリバリー) は、それを可能にする自動化バックボーンです。
---

## CI/CD パイプライン
### CI/CD の実際の意味
|用語 |何をするのか |
|------|---------------|
| **継続的インテグレーション (CI)** |開発者はコードを頻繁にマージします。各マージは自動化されたビルドとテストをトリガーします。
| **継続的デリバリー (CD)** |コードは常にデプロイ可能な状態にあります。運用環境へのリリースは手動で決定します。
| **継続的な展開** |テストに合格したすべての変更は自動的に本番環境に移行されます。手動ゲートは必要ありません。
### 一般的なパイプライン ステージ
|ステージ |何が起こるのか |ツール |
|----------|---------------|----------|
| **出典** |開発者がコードを Git にプッシュする | GitHub、GitLab、Bitbucket |
| **ビルド** |コードをコンパイルし、依存関係をインストールする | Maven、Gradle、npm、pip |
| **テスト** |ユニット、統合、lint チェックを実行する | Jest、pytest、JUnit |
| **パッケージ** | Docker イメージまたはアーティファクトをビルドする | Docker、ビルドパック |
| **デプロイ (ステージング)** |ステージング環境へのデプロイ | Kubernetes、ECS、VM |
| **テスト (ステージング)** |結合テスト、スモークテスト |セレン、郵便配達員 |
| **デプロイ (本番)** |運用環境へのリリース |青緑色、カナリア、ローリング | 写真 青緑色、カナリア、ローリング
| **モニター** |健全性、エラー、パフォーマンスを観察する |プロメテウス、グラファナ、Datadog |
### CI/CD ツールの比較
|ツール |タイプ |強さ |
|------|------|----------|
| **GitHub アクション** |クラウド CI/CD | GitHub と緊密に統合されています。 YAML ワークフロー |
| **GitLab CI** |内蔵CI/CD |リポジトリ + パイプライン用の単一プラットフォーム |
| **ジェンキンス** |セルフホスト型 CI/CD |高度に構成可能。大規模なプラグイン エコシステム |
| **CircleCI** |クラウド CI/CD |速い;コンテナ化されたワークフローに適しています。
| **アルゴCD** | Kubernetes 向け GitOps |宣言型の Git 主導のデプロイメント |
---

## Docker とコンテナ
### なぜコンテナなのか?
コンテナーが登場する以前の古典的な問題は、「自分のマシンで動作する」というものでした。コンテナーは、アプリケーションとそのすべての依存関係 (ライブラリ、ランタイム、構成) を、どこでも同じように実行できる単一のポータブルなユニットにパッケージ化することで、この問題を解決します。
### Docker の基礎
|コンセプト |説明 |
|----------|---------------|
| **画像** |アプリ + 依存関係を含む読み取り専用テンプレート |
| **コンテナ** |イメージのインスタンスを実行中 |
| **Dockerfile** |イメージを構築するためのレシピ |
| **レジストリ** |イメージ用ストレージ (Docker Hub、ECR、GCR) |
| **ボリューム** |コンテナーの再起動後も存続する永続ストレージ |
| **ネットワーク** |コンテナー用の分離されたネットワーク層 |
### Dockerfile のベスト プラクティス
```dockerfile
# Use specific base image tags, not 'latest'
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (leverage Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run as non-root user
USER appuser

# Expose port and define entrypoint
EXPOSE 8000
CMD ["python", "main.py"]
```

主な実践方法: スリム/アルパインベースイメージの使用、非ルートとして実行、レイヤーキャッシュの活用、`.dockerignore`の使用、イメージの脆弱性のスキャン (`trivy`、`docker scan`)、およびリソース制限の設定。
### Docker Compose
複数のコンテナを一緒に実行する場合 (アプリ + データベース + キャッシュ):
```yaml
services:
  app:
    build: .
    ports: ["8000:8000"]
    depends_on: [db, redis]
    environment:
      DATABASE_URL: postgresql://user:pass@db:5432/mydb
  db:
    image: postgres:16
    volumes: [pgdata:/var/lib/postgresql/data]
  redis:
    image: redis:7-alpine
volumes:
  pgdata:
```

---

## Kubernetes (K8s)
Kubernetes は業界標準のコンテナ オーケストレーターです。コンテナ化されたアプリケーションのデプロイ、スケーリング、および操作を管理します。
### コアアーキテクチャ
|コンポーネント |役割 |
|-----------|------|
| **コントロール プレーン** |クラスターを管理します (API サーバー、スケジューラー、etcd、コントローラーマネージャー) |
| **ノード** |コンテナーを実行するワーカー マシン (VM または物理) |
| **ポッド** |展開可能な最小ユニット。ネットワークを共有する 1 つ以上のコンテナ |
| **サービス** |トラフィックをポッドにルーティングする安定したネットワーク エンドポイント |
| **展開** |必要なポッド状態 (レプリカ、イメージなど) の宣言的定義 |
| **イングレス** |外部トラフィックの HTTP ルーティング ルール |
| **ConfigMap / シークレット** |ポッドに挿入された構成および機密データ |
### 必須の kubectl コマンド
```bash
kubectl get pods                    # List pods
kubectl get services                # List services
kubectl describe pod <name>         # Detailed pod info
kubectl logs <pod-name>             # View pod logs
kubectl exec -it <pod> -- /bin/sh   # Shell into a pod
kubectl apply -f deployment.yaml    # Apply a manifest
kubectl rollout status deploy/myapp # Check rollout progress
kubectl scale deploy/myapp --replicas=5  # Scale to 5 replicas
```

### ヘルム
Helm は Kubernetes のパッケージ マネージャーです。 **チャート**は、事前構成された Kubernetes リソースのバンドルです。 K8 の場合は`apt`または`brew`と考えてください。
```bash
helm install my-release bitnami/postgresql   # Install a chart
helm upgrade my-release bitnami/postgresql   # Upgrade
helm rollback my-release 1                   # Rollback to revision 1
helm list                                    # List releases
```

---

## コードとしてのインフラストラクチャ (IaC)
IaC は、アプリケーション コードを扱うのと同じ方法でインフラストラクチャ構成を扱い、パイプラインを通じてバージョン管理、テスト、デプロイが行われます。
### Terraform と Ansible
|ツール |タイプ |アプローチ |最適な用途 |
|------|------|----------|----------|
| **テラフォーム** |プロビジョニング |宣言的 (HCL);状態ベース |クラウド リソース (VPC、VM、データベース) の作成 |
| **アンシブル** |構成 |宣言型 (YAML);エージェントレス |サーバーの構成、ソフトウェアのインストール |
| **プルミ** |プロビジョニング |命令型 (Python、Go、TS) |本物のプログラミング言語を好むチーム |
| **クラウドフォーメーション** |プロビジョニング |宣言型 (YAML/JSON)。 AWS ネイティブ | AWS のみのインフラストラクチャ |
### テラフォームの例
```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  tags = {
    Name = "web-server"
  }
}
```

ベストプラクティス: 再利用性のためにモジュールを使用し、状態をリモートに保存し (ロックのために S3 + DynamoDB)、シークレットをハードコーディングせず、すべてをバージョン管理します。
---

## 監視と可観測性
### 3 本の柱
|柱 |それがあなたに伝えること |ツール |
|------|------|------|
| **メトリクス** |経時的な数値測定 (CPU、リクエスト率、エラー率) |プロメテウス、CloudWatch、Datadog |
| **ログ** |コンテキストを含む個別のイベント (エラー、リクエスト、状態変化) | ELK スタック、Loki、CloudWatch ログ |
| **痕跡** |サービス間のエンドツーエンドのリクエスト ジャーニー |イェーガー、X レイ、ジップキン |
### プロメテウス + Grafana スタック
標準のオープンソース監視スタック:
|コンポーネント |役割 |
|-----------|------|
| **プロメテウス** |時系列データベース。サービスからメトリクスを取得します |
| **グラファナ** |視覚化とダッシュボード |
| **アラートマネージャー** |アラートを Slack、PagerDuty、電子メールにルーティングします。
| **ノード エクスポーター** |システムレベルのメトリクス (CPU、RAM、ディスク) を公開 |
| **ブラックボックス エクスポーター** |プローブエンドポイント (HTTP、TCP、ICMP) |
### 追跡すべき主要な指標
|カテゴリー |メトリクス |
|----------|----------|
| **インフラストラクチャ** | CPU、RAM、ディスク使用量、ネットワーク I/O |
| **アプリケーション** |リクエスト率、レイテンシー (p50、p95、p99)、エラー率 |
| **データベース** |クエリ数、遅いクエリ、接続プールの使用率 |
| **ビジネス** |サインアップ、コンバージョン、収益 |
---

## 導入戦略
|戦略 |仕組み |リスク |ロールバック |
|----------|---------------|------|----------|
| **ローリングアップデート** |古いインスタンスを徐々に新しいインスタンスに置き換えます。一部のユーザーは古いバージョンを使用し、一部のユーザーは新しいバージョンを使用します。前の画像に戻る |
| **ブルーグリーン** | 2 つの同一の環境を実行します。スイッチトラフィック |移行中のインフラストラクチャ コストが 2 倍になる |瞬時にスイッチバック |
| **カナリア** |トラフィックのごく一部を新しいバージョンにルーティングします。徐々に増加します |複雑なトラフィック管理 |トラフィックを安定した環境にルーティングします。
| **機能フラグ** |コードをデプロイしますが、トグルの後ろに機能を隠します |条件付きロジックによるコードの複雑さ |オフに切り替える |
---

## GitOps
GitOps は、IaC の論理的な結論を導き出します。つまり、Git リポジトリは、インフラストラクチャとアプリケーションの望ましい状態に関する唯一の信頼できる情報源です。
|原則 |説明 |
|----------|---------------|
| **宣言的** |コードとして記述されたすべて (YAML、HCL) |
| **バージョン付き** | Git は真実の情報源です |
| **自動化** |ツールは継続的に望ましい状態と実際の状態を調和させます。
| **監査可能** |すべての変更は Git コミットです |
**ArgoCD** と **Flux** は、Kubernetes 用の主要な GitOps ツールです。変更を Git リポジトリにプッシュすると、ツールによってその変更が自動的にクラスターにデプロイされます。
---

## インシデント対応
午前 3 時に何かが壊れた場合:
1. アラートを **承認**します。
2. **範囲を評価**: どのサービス、ユーザー、データが影響を受けますか?
3. 根本原因を **特定** — ログ、メトリクス、最近のデプロイメントを確認します。
4. 可能であれば **包含** — サーキットブレーカー、機能フラグ、トラフィックシフト。
5. **修正** — ロールバックまたはパッチフォワード。
6. **コミュニケーション** — 関係者とユーザーに最新情報を伝えます (ステータス ページ)。
7. **事後分析** — 24 ～ 48 時間以内に、根本原因とアクション項目を文書化します。
目的は、インシデントを解決するだけでなく、同じインシデントが再発しないようにすることです。