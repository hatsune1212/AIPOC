<!-- Source: https://linear.app/simpleasy/document/3-user-stories-and-acceptance-criteriav0-d65da20ee08a -->

# User Stories & Acceptance Criteria（v0）

* 更新日：2026-03-05
* 更新者：AI
* 変更サマリ：
  * v0 初版（代表シナリオをStory化）
  * 匿名性/n>=5/再回答不可/運用者閲覧制限をACに反映

---

## 企業管理者（Company Admin / Analyst）

### US-ADM-01 ログインしたい

* So that：管理画面を利用できる
* AC:
  * Given 有効なアカウント, When メール+パスワードでログイン, Then 管理画面に遷移する
  * Given 無効な認証情報, When ログイン, Then エラーを表示しログインできない

### US-ADM-02 従業員CSVをインポートしたい

* So that：配信対象者リストを整備できる
* AC:
  * Given 正しいCSV, When アップロード, Then 取込成功件数/失敗件数/失敗理由が表示される
  * Given CSVに不備行がある, When 取込, Then 行単位でエラー提示し正常行のみ反映される
  * Given 既存従業員(internal_id一致), When 再インポート, Then 従業員情報が上書き更新される
  * Given 退職者/無効化対象が含まれる, When 再インポート, Then 当該従業員は無効化され配信対象外となる

### US-ADM-03 属性ラベルを作成したい

* So that：結果を任意の切り口で集計できる
* AC:
  * When ラベルを作成, Then 従業員に対してラベル値を紐付けられる
  * When ラベルを編集/削除, Then 集計表示に反映される（影響範囲を明示）

### US-ADM-04 アンケートを配信したい（項目固定）

* So that：従業員から不満足度データを収集できる
* AC:
  * Given 配信対象者が存在, When 配信実行, Then 対象従業員にメールが送信される
  * Then 配信結果（成功/失敗/未達）が確認できる
  * Then 配信期限（due_at）が設定できる（未確定なら要確認ラベル）

### US-ADM-05 リマインドを送りたい

* So that：回答率を上げられる
* AC:
  * Given 未回答者が存在, When リマインド実行, Then 未回答者へメールが送信される
  * Then 未回答者判定は内部IDに基づき行われる

### US-ADM-06 回答状況（運用集計）を確認したい

* So that：配信運用を管理できる
* AC:
  * Then 回答数/未回答数/回答率が表示される
  * Then セグメント件数とn閾値適用結果が確認できる

### US-ADM-07 結果（分析結果）を確認したい（匿名性担保）

* So that：組織の健康状態と解決策を把握できる
* AC:
  * Then 個人回答（Response）は表示されない
  * Then 集計は n>=5 のセグメントのみ表示される（n<5はデータ不足表示）
  * Then 分析結果（Insight）が表示される（外部ロジック組込みの出力）

### US-ADM-08 PDFレポートを出力したい

* So that：社内共有・意思決定に使える
* AC:
  * When レポート出力, Then PDFが生成されダウンロードできる
  * Then PDFの内容は集計結果・分析結果に基づく（詳細構成は未確定）

### US-ADM-09 企業管理者アカウントを管理したい

* So that：社内で利用者を増減できる
* AC:
  * When Adminがアカウント作成/編集/削除, Then 反映される
  * Then Analystはアカウント管理ができない

### US-ADM-10 問い合わせしたい

* So that：運用者に支援を求められる
* AC:
  * When 問い合わせ送信, Then 運用者が参照できる

---

## 従業員（Employee Respondent）

### US-EMP-01 メールリンクからアンケートに回答したい

* So that：匿名性のある形で不満を伝えられる
* AC:
  * Given 有効なリンク, When アクセス, Then 回答画面が表示される
  * Given 期限切れ, When アクセス, Then 期限切れが表示され回答できない
  * When 回答送信, Then 送信完了が表示される
  * Then 期間内再回答は不可（同一campaign_id×employee_idで1回のみ）

### US-EMP-02 自分の属性を回答/確認したい

* So that：適切な集計に寄与できる
* AC:
  * When 属性入力, Then 回答と紐づいて保存される（実装詳細は設計で確定）

---

## 運用者（Operator Admin / Support）

### US-OPS-01 企業アカウント（テナント）を管理したい

* So that：サービス運用を行える
* AC:
  * When テナント作成/編集/削除, Then 反映される
  * Then 企業管理者は自身のテナント外へアクセスできない（テナント分離）

### US-OPS-02 問い合わせに返信したい

* So that：サポート対応ができる
* AC:
  * When 返信送信, Then 企業管理者へ通知される

### US-OPS-03 例外的に調査のためログを参照したい（監査付き）

* So that：障害調査を行える
* AC:
  * Then 原則として個人回答本文・個人特定情報は閲覧不可
  * Given 例外調査が必要, When 限定権限で参照, Then 監査ログが記録される