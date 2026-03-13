import type { RouteRecordRaw } from "vue-router";

import AdminDashboardPage from "../pages/admin/AdminDashboardPage.vue";
import EmployeesImportPage from "../pages/admin/EmployeesImportPage.vue";
import CampaignsPage from "../pages/admin/CampaignsPage.vue";
import ResultsPage from "../pages/admin/ResultsPage.vue";
import ReportsPage from "../pages/admin/ReportsPage.vue";
import TenantManagementPage from "../pages/operator/TenantManagementPage.vue";
import OperatorInboxPage from "../pages/operator/OperatorInboxPage.vue";
import SurveyIntroPage from "../pages/employee/SurveyIntroPage.vue";
import SurveyQuestionsPage from "../pages/employee/SurveyQuestionsPage.vue";
import SurveyCompletedPage from "../pages/employee/SurveyCompletedPage.vue";

export const routes: RouteRecordRaw[] = [
  {
    path: "/admin",
    children: [
      { path: "dashboard", component: AdminDashboardPage },
      { path: "employees/import", component: EmployeesImportPage },
      { path: "campaigns", component: CampaignsPage },
      { path: "results", component: ResultsPage },
      { path: "reports", component: ReportsPage }
    ]
  },
  {
    path: "/operator",
    children: [
      { path: "tenants", component: TenantManagementPage },
      { path: "inbox", component: OperatorInboxPage }
    ]
  },
  {
    path: "/survey",
    children: [
      { path: "intro", component: SurveyIntroPage },
      { path: "questions", component: SurveyQuestionsPage },
      { path: "completed", component: SurveyCompletedPage }
    ]
  },
  {
    path: "/:pathMatch(.*)*",
    redirect: "/admin/dashboard"
  }
];
