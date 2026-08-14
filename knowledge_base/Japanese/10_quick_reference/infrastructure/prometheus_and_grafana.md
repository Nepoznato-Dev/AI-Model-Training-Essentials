---
# Metadata
title: "Prometheus and Grafana"
description: "PromQL, exporters, dashboards, alerting, monitoring stack"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [prometheus, grafana, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

#プロメテウスとグラファナ
Prometheus は、信頼性と拡張性を考慮して設計されたオープンソースの監視および警告ツールキットです。 Grafana は、時系列データを視覚化するための主要なオープンソース プラットフォームです。これらは一緒になって、最新のインフラストラクチャとアプリケーション用の最も一般的な監視スタックを形成します。 Prometheus はメトリクスを収集して保存します。 Grafana はそれらをダッシュ​​ボードに表示します。
---

## プロメテウスのアーキテクチャ
|コンポーネント |説明 |
|----------|---------------|
| **プロメテウス サーバー** |ターゲットからメトリクスを取得します。時系列データを保存します。アラート ルールを評価する |
| **輸出業者** |システム (Node Exporter、cAdvisor など) からのメトリクスを公開します。
| **プッシュゲートウェイ** |有効期間の短いジョブ (バッチ ジョブ、CI) からメトリクスを受信します。
| **アラートマネージャー** |アラートの処理: グループ化、サイレンシング、ルーティング、抑制 |
| **サービスの検出** |ターゲットを自動的に検出 (Kubernetes、Consul、EC2 など) |
---

## 主要な概念
|コンセプト |説明 |
|----------|---------------|
| **メトリック** |オプションのラベルと値 | を含む名前付き測定値。
| **時系列** |特定のメトリックとラベルの組み合わせのデータ ポイントのストリーム |
| **仕事** |同じ目的を持つターゲットのコレクション |
| **インスタンス** |スクレイピングする単一のターゲット (通常はプロセス) |
| **スクレープ** | Prometheus がターゲットから一定の間隔でメトリクスを取得する |
| **ラベル** |メトリクスのディメンションを設定するキーと値のペア (例:`method="GET"`) |
| **サンプル** |ある時点の値: (タイムスタンプ, 値) |
---

## メトリクスのタイプ
|タイプ |説明 |使用例 |
|------|---------------|----------|
| **カウンター** |単調増加値（上がるだけ） |リクエスト数。エラー。完了したタスク |
| **ゲージ** |上がることも下がることもある値 |温度;メモリ使用量。キューの長さ |
| **ヒストグラム** |値ごとにバケット化された観測値 |リクエストのレイテンシ。応答サイズ |
| **概要** |ヒストグラムに似ています。クライアント側で分位数を計算します。レイテンシのパーセンタイル |
---

## PromQL (クエリ言語)
### 基本的なクエリ
|クエリ |説明 |
|------|-----------|
| `http_requests_total`|生の時系列 |
| `http_requests_total{method="GET"}`|ラベルでフィルター |
| `http_requests_total{method="GET", status="200"}`|複数のラベルフィルター |
| `rate(http_requests_total[5m])`| 5 分間の 1 秒あたりのレート |
| `increase(http_requests_total[1h])`| 1 時間の合計増加率 |
| `sum(rate(http_requests_total[5m])) by (status)`|ステータスごとの合計レート |
| `histogram_quantile(0.95, rate(http_duration_bucket[5m]))`| 95 パーセンタイルのレイテンシ |
| `avg(node_cpu_seconds_total{mode="idle"})`|平均 CPU アイドル状態 |
| `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))`| CPU 使用率 |
### 共通機能
|機能 |説明 |例 |
|----------|---------------|----------|
| `rate()`| 1 秒あたりの平均増加率 | `rate(requests_total[5m])`|
| `irate()`|最後の 2 つのデータ ポイントに基づく 1 秒あたりのレート | `irate(requests_total[1m])`|
| `increase()`|時間範囲にわたる合計増加率 | `increase(errors_total[1h])`|
| `sum()`|系列全体の合計 | `sum(rate(requests_total[5m])) by (service)`|
| `avg()`|シリーズ全体の平均 | `avg(node_memory_usage)`|
| `histogram_quantile()`|ヒストグラムから分位点を計算する | `histogram_quantile(0.99, rate(duration_bucket[5m]))`|
| `topk()`|値による上位 K シリーズ | `topk(5, rate(requests_total[5m]))`|
| `predict_linear()`|線形予測 | `predict_linear(disk_usage[1h], 4*3600)`|
| `absent()`|メトリックが欠落しているかどうかを確認する | `absent(up{job="myapp"})`|
---

## 一般的なエクスポーター
|輸出業者 |監視対象 |
|----------|------|
| **ノード エクスポーター** | Linux/Unix ホスト メトリック (CPU、メモリ、ディスク、ネットワーク) |
| **cアドバイザー** |コンテナーのメトリック (CPU、メモリ、ネットワーク、ファイルシステム) |
| **MySQL エクスポーター** | MySQL データベースのメトリクス |
| **PostgreSQL エクスポーター** | PostgreSQL データベースのメトリクス |
| **Redis エクスポーター** | Redis メトリクス |
| **ブラックボックス エクスポーター** | HTTP、HTTPS、DNS、TCP、ICMP 経由でエンドポイントを調査する |
| **SNMP エクスポーター** | SNMP 経由のネットワーク デバイス メトリクス |
| **JSON エクスポーター** | JSON API からのカスタム メトリクス |
---

## グラファナ
### 主要な概念
|コンセプト |説明 |
|----------|---------------|
| **データソース** | Prometheus (または他のバックエンド) への接続 |
| **ダッシュボード** |レイアウトに配置されたパネルのコレクション |
| **パネル** |単一のビジュアライゼーション (グラフ、ゲージ、テーブル、ヒートマップ) |
| **変数** |ダッシュボードの動的フィルター (インスタンスの選択など) |
| **注釈** |グラフ上のイベントにマークを付ける (展開、インシデント) |
| **アラート ルール** | Grafana 内のしきい値ベースのアラート |
| **テンプレート** |変数を使用した再利用可能なダッシュボード パターン |
### 便利なダッシュボード パターン
|パターン |説明 |
|----------|---------------|
| **概要行** |主要な指標の概要: エラー率、レイテンシ、スループット |
| **ドリルダウン** |変数を使用して概要から詳細ビューへクリック |
| **RED メソッド** |レート、エラー、継続時間 — 3 つの主要なサービス指標 |
| **使用方法** |使用率、飽和、エラー — インフラストラクチャ向け |
| **ゴールデンシグナル** |レイテンシ、トラフィック、エラー、飽和 (Google の SRE 本) |
---

## アラート中
### アラート ルールの構造
```yaml
groups:
  - name: example
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate on {{ $labels.instance }}"
          description: "Error rate is {{ $value | humanizePercentage }}"
```

### アラートマネージャーのルーティング
|コンセプト |説明 |
|----------|---------------|
| **グループ** |同様のアラートを 1 つの通知に結合する |
| **ルート** |アラートの送信先を決定するマッチャーのツリー |
| **受信機** |アラートを送信する場所 (電子メール、Slack、PagerDuty、Webhook) |
| **禁止** |別のアラートが発生しているときにアラートを抑制する |
| **沈黙** |ラベルマッチャーによるアラートを一時的にミュートする |
---

## トラブルシューティング
|問題 |ソリューション |
|----------|----------|
| **ターゲットダウン** |エクスポーターが実行されているかどうかを確認します。ネットワーク/ファイアウォールを確認してください。スクレイピング構成を確認する |
| **データなし** |メトリクス名のスペルを確認してください。ラベルフィルターを確認してください。時間範囲を確認する |
| **高いカーディナリティ** |ラベルの組み合わせが多すぎます。ラベル値を減らす。記録ルールを使用する |
| **クエリが遅い** |複雑なクエリには記録ルールを使用します。スクレイピング間隔を増やす |
| **警戒疲労** |しきい値を調整します。`for`の期間を追加します。グループ関連のアラート |
| **再起動後にメトリクスが失われる** | Prometheus はデータをローカルに保存します。保持設定を確認する |
---

＃＃ まとめ
Prometheus は、エクスポータから定期的にメトリクスを取得することでシステムを監視します。メトリックには、カウンター (上昇のみ)、ゲージ (上昇および下降)、ヒストグラム (バケット化された観測値)、および要約 (分位数) の 4 つのタイプがあります。 PromQL はクエリ言語であり、`rate()`、`increase()`、`histogram_quantile()`、および集計関数 (`sum`、`avg`) が最も一般的な操作です。 Grafana は、パネル、変数、注釈を備えたダッシュボードで Prometheus データを視覚化します。アラートでは、アラートのグループ化、ルーティング、サイレント、および抑制に Alertmanager を使用します。主な監視パターンは、Google のゴールデン シグナル (遅延、トラフィック、エラー、飽和) とサービスの RED メソッド (レート、エラー、期間)、およびインフラストラクチャの USE メソッド (使用率、飽和、エラー) です。