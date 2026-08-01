<!-- 
This file was automatically translated from English to Japanese.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 機械学習の評価とワークフロー

問題設定から本番監視まで、ML ライフサイクル全体を実践的に整理したガイドです。評価指標、検証方法、デバッグの考え方に重点を置いています。

---

## ML ワークフロー（CRISP-ML）

1. **ビジネス理解**: 目的と成功基準を定義する。
2. **データ理解**: 利用可能なデータを調査し、品質上の問題を特定する。
3. **データ準備**: データをクリーニングし、変換し、分割する。
4. **モデリング**: モデルを学習させ、ハイパーパラメータを調整する。
5. **評価**: 指標に基づいて性能を評価する。
6. **デプロイ**: モデルを本番環境で提供する。
7. **監視**: ドリフト、性能、異常を追跡する。

これは反復的なループであり、評価結果に応じて前の工程に戻ることが前提です。

---

## データ分割

### Train / Validation / Test Split
- **Training set**（約 70%）: モデルのパラメータを学習するために使う。
- **Validation set**（約 15%）: ハイパーパラメータの調整やモデル候補の選択に使う。
- **Test set**（約 15%）: 汎化性能を見積もるため、最後に一度だけ使う。

**重要:** テストセットはデータリークを防ぐため、最終評価まで完全に手を触れない状態に保つ必要があります。

### Cross-Validation（k-fold）
データセットが小さい場合は k-fold cross-validation を使います。データを k 個の fold に分け、k-1 個で学習し、残り 1 個で検証する操作を k 回繰り返し、性能を平均します。一般的には k=5 または k=10 がよく使われます。

### Stratified Splitting
分類問題でクラス不均衡がある場合は、各分割でクラス比率が保たれるよう stratified split を使います。

### Time-Based Splitting
時系列データでは、ランダム分割ではなく時系列順に分割します。過去で学習し、未来で評価するのが基本です。

---

## 評価指標

### 分類の評価指標

| 指標 | 測っているもの | 適した用途 |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | クラスが均衡しているデータセット |
| **Precision** | TP / (TP + FP) | 偽陽性のコストが高い場合（例: スパム検知） |
| **Recall** | TP / (TP + FN) | 偽陰性のコストが高い場合（例: がん検診） |
| **F1-score** | Precision と Recall の調和平均 | 不均衡データセット、単一指標で見たい場合 |
| **AUC-ROC** | ROC 曲線下面積。TPR と FPR のトレードオフを見る | しきい値に依存しない分類器の総合性能 |
| **AUC-PR** | Precision-Recall 曲線下面積 | 極端に不均衡なデータセット |

**定義:**
- TP = True Positive
- TN = True Negative
- FP = False Positive（第一種過誤）
- FN = False Negative（第二種過誤）

### 回帰の評価指標

| 指標 | 測っているもの | 外れ値への感度 |
|--------|------------------|--------------------------|
| **MSE**（Mean Squared Error） | 二乗誤差の平均 | 高い |
| **RMSE**（Root Mean Squared Error） | MSE の平方根（目的変数と同じ単位） | 高い |
| **MAE**（Mean Absolute Error） | 絶対誤差の平均 | 低い |
| **R²**（Coefficient of Determination） | 分散のうち説明できた割合 | 直接ではないが、間接的に外れ値の影響を受ける |

### ランキング・検索系の指標
- **Precision@k**: 上位 k 件に含まれる関連アイテムの割合。
- **Recall@k**: すべての関連アイテムのうち、上位 k 件に現れた割合。
- **NDCG**（Normalised Discounted Cumulative Gain）: 順位位置を考慮した関連度指標。
- **Hit Rate**: 上位 k 件に少なくとも 1 件の関連アイテムが含まれるかどうか。

### 生成モデル / LLM の指標
- **Perplexity**: 未知テキストに対してモデルがどれだけ「驚くか」を表す指標。低いほど良い。
- **BLEU**: 参照翻訳との n-gram 一致度を測る指標。Precision 寄り。
- **ROUGE**: 要約でよく使われる Recall 寄りの重なり指標。
- **BERTScore**: 文脈埋め込みを使った意味的類似度。BLEU より頑健なことが多い。
- **METEOR**: 同義語や語幹も考慮して評価する指標。

---

## 評価時の落とし穴

### データリーク
テストセットの情報が意図せず学習に入り込む状態です。
- **防止策:** 特徴量設計、正規化、ハイパーパラメータ調整にテストデータを使わない。
- **兆候:** 不自然に高すぎるスコアが出たらリークを疑う。

### 過学習（Overfitting）
学習データでは高性能だが、検証・テストデータで性能が落ちる状態です。
- **対策:** 正則化、early stopping、モデルの簡素化、データ追加などを行う。

### 学習不足（Underfitting）
学習データでも検証データでも性能が低い状態です。
- **対策:** より複雑なモデルを使う、特徴量を増やす、正則化を弱める。

### 不均衡データ
- **対策:** クラス重み、oversampling（SMOTE）、undersampling、または Accuracy ではなく F1 や AUC-PR のような適切な指標を使う。

### 時間的ドリフト（Concept Drift）
特徴量と目的変数の関係が時間とともに変化する現象です。
- **対策:** 定期的な再学習、性能監視、ドリフト検知アルゴリズムの活用。

---

## ハイパーパラメータ調整

- **Grid Search**: あらかじめ決めた候補の全組み合わせを総当たりで試す。単純だが計算コストは高い。
- **Random Search**: 分布からランダムに組み合わせをサンプリングする。高次元空間では Grid Search より効率的なことが多い。
- **Bayesian Optimisation**: 目的関数の確率モデルを構築し、賢くハイパーパラメータを選ぶ。代表的なライブラリは Optuna、Hyperopt、scikit-optimise。
- **Automated Tuning**: Optuna、Ray Tune、Weights & Biases Sweeps などを使って分散チューニングする。

**よくあるハイパーパラメータの探索範囲例:**

| パラメータ | 推奨範囲（対数スケール） |
|-----------|-----------------------------|
| Learning rate | 1e-5 〜 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number of layers（NN） | 2 〜 6 |
| Number of neurons（NN） | 32 〜 1024 |
| Regularisation（L2） | 1e-6 〜 1e-2 |
| Tree depth（XGBoost） | 3 〜 12 |

---

## モデル選択と検証

1. **ベースラインモデル**: 単純なヒューリスティックや単純モデル（例: logistic regression、平均予測器）から始め、最低基準を作る。
2. **候補モデル**: Random Forest、XGBoost、Neural Network など複数のモデル群を学習させる。
3. **Cross-validation** によって各候補を検証する。
4. **指標を比較** し、可能なら信頼区間も見ながら最良候補を選ぶ。
5. **最終評価** を保持しておいたテストセットで行う。
6. **誤り分析**: モデルが間違えた例を見て、希少クラスや曖昧な入力などの傾向を特定し、データ準備や特徴量設計に反映する。

---

## デプロイと監視

### 推論提供のパターン
- **Batch inference**: 大量データをオフラインでまとめて処理する（例: 夜間レコメンド）。
- **Online inference**: API 経由でリアルタイム予測を返す（例: 与信判定、不正検知）。
- **Streaming inference**: イベント駆動で低遅延に処理する（例: IoT センサー通知）。

### モデル監視
- **性能監視**: 正解ラベルが得られる場合、ライブデータ上で Accuracy や F1 の推移を追う。
- **データドリフト**: 入力特徴量分布の変化を監視する（例: PSI – Population Stability Index）。
- **Concept drift**: 入力と出力の関係の変化を監視する。
- **Prediction drift**: 予測出力の分布変化を追跡する。
- **Latency と Throughput**: SLA（Service Level Agreements）を満たしているか確認する。

### ログとアラート
- 予測リクエストとレスポンスを、匿名化したうえで記録する。
- 次のような条件でアラートを設定する:
  - 性能が大きく低下したとき。
  - 欠損入力や不正入力の割合が高いとき。
  - モデル出力が想定範囲を外れたとき。

### モデルのバージョン管理とレジストリ
- モデルレジストリ（例: MLflow、Weights & Biases、Sagemaker Model Registry）を使って、モデル、メタデータ、評価結果を保存・管理する。
- 学習コードとデータのバージョン（DVC や Git LFS など）もモデルと合わせて管理する。

---

## 実務向けワークフローチェックリスト

- [ ] 問題設定と成功指標の定義が完了している。
- [ ] データ探索（欠損値、外れ値、分布）を実施した。
- [ ] Train/validation/test split を作成した（必要なら stratified split）。
- [ ] ベースラインモデルを用意した。
- [ ] 候補モデルを学習・検証した。
- [ ] ハイパーパラメータを調整した。
- [ ] Cross-validation に基づいて最良モデルを選定した。
- [ ] テストセットで最終評価を行った。
- [ ] 誤り分析を実施した。
- [ ] デプロイ計画（推論基盤）の準備ができている。
- [ ] 監視ダッシュボードを用意した。
- [ ] Documentation（data card、model card）の整備が完了している。
