"""Minimal domain model skeleton based on docs/domain-model-minimal-v0.

NOTE:
- These are Pydantic models used for API I/O and internal wiring.
- Persistence models, migrations, and actual business logic are out of
  scope for this skeleton and should be implemented in later tickets.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class Tenant(BaseModel):
    tenant_id: str
    name: str
    status: str
    created_at: datetime


class CompanyUser(BaseModel):
    user_id: str
    tenant_id: str
    email: EmailStr
    role: str  # Admin / Analyst
    status: str


class OperatorUser(BaseModel):
    operator_id: str
    email: EmailStr
    role: str  # Admin / Support
    status: str


class Employee(BaseModel):
    employee_id: str
    tenant_id: str
    internal_id: str
    email: EmailStr
    status: str


class SurveyCampaign(BaseModel):
    campaign_id: str
    tenant_id: str
    status: str
    send_at: Optional[datetime]
    due_at: Optional[datetime]


class SegmentMetric(BaseModel):
    metric_id: str
    campaign_id: str
    segment_key: str
    n: int
    # values structure (scores, distributions, etc.) will be defined later


class Report(BaseModel):
    report_id: str
    campaign_id: str
    pdf_path: str
    generated_at: datetime


class AuditLog(BaseModel):
    audit_id: str
    actor_type: str
    actor_id: str
    tenant_id: Optional[str] = None
    action: str
    created_at: datetime
