<!--
---
# Metadata
title: "CI/CD Pipeline Configuration"
description: "GitHub Actions, GitLab CI, Jenkins, pipeline YAML patterns"
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
tags: [cicd, pipeline, config, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# CI/CD パイプライン構成
継続的インテグレーション (CI) および継続的デプロイメント (CD) パイプラインは、ソフトウェアの構築、テスト、デプロイのプロセスを自動化します。このリファレンスでは、最も一般的な CI/CD プラットフォーム (GitHub Actions、GitLab CI、および一般的なパイプライン設計原則) の構成パターンについて説明します。
---

## GitHub アクション
### ワークフロー構造
```yaml
name: CI Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up language
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
      - name: Build
        run: python setup.py build
```

### 一般的なトリガー
|トリガー |説明 |
|----------|---------------|
| `on: push`|プッシュするたびに |
| `on: pull_request`| PR オープン、更新、再開 |
| `on: schedule`| Cron ベースのスケジュール |
| `on: workflow_dispatch`|手動トリガー |
| `on: release`|リリースの作成について |
| `on: workflow_call`|別のワークフローによって呼び出される (再利用可能) |
### 主な機能
|特集 |説明 |
|----------|---------------|
| **マトリックス戦略** |異なる構成で同じジョブを実行する |
| **秘密** |暗号化された環境変数 (`${{ secrets.MY_SECRET }}`) |
| **環境** |保護ルールを備えた展開ターゲット |
| **キャッシング** |実行間の依存関係をキャッシュする |
| **アーティファクト** |ジョブからファイルをアップロード (テスト レポート、ビルド) |
| **再利用可能なワークフロー** |リポジトリ間でワークフロー ロジックを共有する |
| **複合アクション** |複数のステップを 1 つのアクションに結合する |
### マトリックス戦略
```yaml
jobs:
  test:
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']
        os: [ubuntu-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
```

---

## GitLab CI
### パイプライン構造
```yaml
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - docker build -t myapp:$CI_COMMIT_SHA .
    - docker push myapp:$CI_COMMIT_SHA

test:
  stage: test
  script:
    - docker run myapp:$CI_COMMIT_SHA pytest

deploy:
  stage: deploy
  script:
    - deploy.sh $CI_COMMIT_SHA
  only:
    - main
  when: manual
```

### 重要なキーワード
|キーワード |説明 |
|----------|---------------|
| `stages`|パイプライン ステージとその順序を定義する |
| `stage`|ジョブをステージに割り当てる |
| `script`|実行するコマンド |
| `before_script`|コマンドはメイン スクリプトの前に実行されます。
| `after_script`|コマンドはメイン スクリプトの後に実行されます (失敗した場合でも)。
| `only / except`|ジョブの実行時期の制御 (ブランチ、タグ) |
| `rules`| Only/Except のより柔軟なバージョン |
| `variables`| CI/CD 変数を定義する |
| `cache`|パイプラインの実行間にファイルをキャッシュする |
| `artifacts`|ジョブ間で受け渡すファイル |
| `environment`|導入環境 |
| `when`|ジョブ実行の制御 (成功時、失敗時、手動、常時) |
| `needs`|ジョブの依存関係を指定する (DAG モード) |
| `extends`|別のジョブから設定を継承する |
| `include`|外部 YAML ファイルをインポートする |
### 事前定義された変数
|変数 |説明 |
|----------|---------------|
| `$CI_COMMIT_SHA`|現在のコミットハッシュ |
| `$CI_COMMIT_REF_NAME`|ブランチまたはタグ名 |
| `$CI_PIPELINE_ID`|パイプライン ID |
| `$CI_JOB_ID`|ジョブID |
| `$CI_PROJECT_DIR`|プロジェクトへのフルパス |
| `$CI_REGISTRY`|コンテナ レジストリの URL |
| `$CI_DEFAULT_BRANCH`|デフォルトのブランチ名 |
---

## パイプライン設計パターン
### 一般的なパターン
|パターン |説明 |
|----------|---------------|
| **一度構築すれば、何度でも導入可能** |アーティファクトを一度構築します。同じアーティファクトを各環境にデプロイする |
| **ゲートチェック** |運用展開前の手動承認 |
| **機能フラグ** |運用環境にデプロイしますが、機能フラグの背後に隠れます |
| **カナリア展開** |少数の割合に展開します。モニター;ロールアウト |
| **ブルーグリーン展開** | 2 つの同一の環境。スイッチトラフィック |
| **並行テスト** |テスト スイートを並列実行してパイプライン時間を短縮する |
| **最初にリント** |高価なテストの前にリンターを実行します。失敗が早い |
| **キャッシュの依存関係** |ビルドを高速化するために、node_modules、pip、Maven をキャッシュする |
### パイプライン ステージ (標準)
|ステージ |目的 |
|------|-----------|
| **糸くず** |コードスタイルと静的解析 |
| **ビルド** |コンパイル;バンドル;アーティファクトを作成する |
| **単体テスト** |迅速なテスト。外部依存関係はありません |
| **結合テスト** |データベースを使用したテスト。 API;外部サービス |
| **セキュリティ スキャン** |依存関係の脆弱性。秘密のスキャン。 SAST |
| **パッケージ** | Docker イメージを作成します。ビルド リリース アーティファクト |
| **ステージングのデプロイ** |ステージング環境へのデプロイ |
| **E2E テスト** |ステージングに対する完全なシステム テスト |
| **本番環境の展開** |実稼働環境への展開 (手動または自動) |
| **煙テスト** |展開が正常であることを確認する |
---

## キャッシュ戦略
|言語 / ツール |キャッシュパス |例 |
|-----|----------|----------|
| **Python (pip)** | `~/.cache/pip`| `requirements.txt`ハッシュからのキーを含む`actions/cache`|
| **Node.js (npm)** | `~/.npm`|  キャッシュを内蔵した`actions/setup-node`|
| **Java (Maven)** | `~/.m2/repository`|`pom.xml`ハッシュからのキーを使用したキャッシュ |
| **Java (Gradle)** | `~/.gradle/caches`|`build.gradle`ハッシュからのキーを使用したキャッシュ |
| **行く** | `~/go/pkg/mod`|`go.sum`ハッシュからのキーを使用したキャッシュ |
| **錆 (貨物)** | `~/.cargo/registry`|`Cargo.lock`ハッシュからのキーを使用したキャッシュ |
| **ドッカー** | Docker 層のキャッシュ | `docker/build-push-action`キャッシュフロム付き |
---

## トラブルシューティング
|問題 |ソリューション |
|----------|----------|
| **パイプラインが遅い** |依存関係をキャッシュします。ジョブを並列化します。より小さい基本イメージを使用する |
| **秘密は利用できません** |シークレット名を確認してください。環境の範囲を確認します。フォークの PR 制限を確認する |
| **アーティファクトが大きすぎます** |不要なファイルを除外します。圧縮する。より短い保持期間を使用する |
| **マトリックスが大きすぎます** |組み合わせを減らします。`include`/`exclude`を使用する |
| **不安定なテスト** |不安定なテストを隔離します。根本原因を修正します。`retry:`で再試行 |
| **許可が拒否されました** |トークンのスコープを確認します。ランナーの権限を確認する |
---

＃＃ まとめ
CI/CD パイプラインは、ソフトウェアの構築、テスト、デプロイを自動化します。 GitHub Actions は、リポジトリ イベントによってトリガーされる YAML ワークフローを使用します。 GitLab CI は、柔軟なルールを持つステージとジョブを使用します。主なパターンは次のとおりです。一度構築したら何度もデプロイします。生産前のゲートチェック。迅速なフィードバックのために最初に lint を実行します。依存関係をキャッシュしてビルドを高速化します。そしてテストを並列化します。パイプラインのステージは通常、lint → ビルド → テスト → セキュリティ → パッケージ → デプロイ → スモーク テストと進みます。キャッシュ戦略は言語によって異なりますが、ロック ファイル ハッシュをキーとした依存関係ディレクトリをキャッシュするという同じ原則に従います。目標は、すべての変更に対する迅速で信頼性の高いフィードバックと、本番環境への安全で再現可能なデプロイメントです。