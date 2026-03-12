<!-- Source: https://linear.app/simpleasy/document/2-domain-model-minimalv0-bfcb774e95ed -->

# Domain Model (Minimal)（v0）

* 更新日：2026-03-05
* 更新者：AI
* 変更サマリ：
  * v0 初版（SSOTの概念・データ境界を固定）
  * 匿名性・n>=5・運用者閲覧制限をモデルに反映

## 用語（Glossary）

* テナント：企業（契約組織）単位の分離単位
* 企業管理者：企業側で設定・配信・閲覧を行うユーザー
* 従業員：アンケートに回答する対象者
* 運用者：サービス提供会社側の管理ユーザー
* 属性ラベル：部署/職種/雇用形態など、集計に用いる分類
* セグメント：属性ラベルの組み合わせで切った集計単位
* n閾値：匿名性のため、集計表示を許可する最小回答者数（n>=5）

## エンティティ一覧（最小）

| Entity | 主キー | 主な属性（抜粋） | 関連 | 備考 |
| -- | -- | -- | -- | -- |
| Tenant | tenant_id | name, status, created_at | 1..\* CompanyUser / Employee / Campaign | テナント分離（行レベル） |
| CompanyUser | user_id | tenant_id, email, password_hash, role, status | belongs Tenant | role: Admin/Analyst |
| OperatorUser | operator_id | email, password_hash, role, status | * 

 | role: Admin/Support |
| Employee | employee_id | tenant_id, internal_id, email, status | belongs Tenant | CSVで上書き、退職者は無効化 |
| Label | label_id | tenant_id, name, type | belongs Tenant | 企業が作成 |
| EmployeeLabel | (employee_id,label_id) | value | Employee-Label | セグメント切り口 |
| SurveyCampaign | campaign_id | tenant_id, status, send_at, due_at | Tenant | 月次等の配信単位 |
| SurveyQuestion | question_id | version, text, type, order | Campaign? | 項目固定（version管理） |
| Response | response_id | campaign_id, employee_id, submitted_at, answers | Campaign/Employee | 企業管理者に個票非公開 |
| Insight | insight_id | campaign_id, content, created_at | Campaign | 外部ロジック生成（組込み） |
| SegmentMetric | metric_id | campaign_id, segment_key, n, values | Campaign | n>=5のみ表示 |
| Report | report_id | campaign_id, pdf_path, generated_at | Campaign | PDF出力 |
| AuditLog | audit_id | actor_type, actor_id, tenant_id?, action, meta, created_at | * 

 | 重要操作の監査 |

## 匿名性・表示ルール（必須）

* 企業管理者UI/エクスポートでは個人回答（Response）を表示しない（個票非公開）
* 集計表示はセグメント回答者数 n>=5 の場合のみ（n<5は「データ不足」扱い）
* 従業員は内部的に一意IDで管理し、未回答者判定/リマインドに使用する（ただし企業管理者には個人特定情報を出さない）
* 運用者は原則として個人回答本文・個人特定情報を閲覧不可。例外時は限定権限＋監査ログ必須
* 退職者/無効メールは配信対象外（CSV再インポートで無効化反映）

## キー・一意制約（最小）

* (tenant_id, CompanyUser.email) は一意
* (tenant_id, Employee.internal_id) は一意（CSV上書きキー）
* (campaign_id, employee_id) は一意（再回答不可の根拠）