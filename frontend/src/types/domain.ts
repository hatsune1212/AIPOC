// Minimal shared domain types mirroring backend/app/models/domain.py
// NOTE: This is intentionally small; extend per ticket.

export interface Tenant {
  tenant_id: string;
  name: string;
  status: string;
  created_at: string;
}

export interface CompanyUser {
  user_id: string;
  tenant_id: string;
  email: string;
  role: "Admin" | "Analyst" | string;
  status: string;
}

export interface Employee {
  employee_id: string;
  tenant_id: string;
  internal_id: string;
  email: string;
  status: string;
}
