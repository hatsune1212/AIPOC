<template>
  <div class="app-root">
    <header class="app-header">
      <nav class="nav">
        <span class="nav-title">AI Survey POC</span>
        <div class="nav-links">
          <!-- Admin (Company) views -->
          <RouterLink class="nav-link" to="/admin/dashboard">Admin: Dashboard</RouterLink>
          <RouterLink class="nav-link" to="/admin/employees/import">Admin: Employees Import</RouterLink>
          <RouterLink class="nav-link" to="/admin/campaigns">Admin: Campaigns</RouterLink>
          <RouterLink class="nav-link" to="/admin/results">Admin: Results</RouterLink>
          <RouterLink class="nav-link" to="/admin/reports">Admin: Reports</RouterLink>

          <!-- Operator views -->
          <RouterLink class="nav-link" to="/operator/tenants">Operator: Tenants</RouterLink>
          <RouterLink class="nav-link" to="/operator/inbox">Operator: Inbox</RouterLink>

          <!-- Employee survey views -->
          <RouterLink class="nav-link" to="/survey/intro">Survey: Intro</RouterLink>
          <RouterLink class="nav-link" to="/survey/questions">Survey: Questions</RouterLink>
          <RouterLink class="nav-link" to="/survey/completed">Survey: Completed</RouterLink>
        </div>
      </nav>
    </header>

    <main class="app-main">
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts"></script>

<style>
.app-root {
  min-height: 100vh;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background-color: #f5f5f7;
}

.app-header {
  position: sticky;
  top: 0;
  z-index: 10;
  background-color: #111827;
  color: #f9fafb;
  box-shadow: 0 1px 3px rgba(15, 23, 42, 0.3);
}

.nav {
  max-width: 1120px;
  margin: 0 auto;
  padding: 0.75rem 1.5rem;
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.nav-title {
  font-weight: 600;
  letter-spacing: 0.03em;
}

.nav-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  font-size: 0.875rem;
}

.nav-link {
  padding: 0.25rem 0.6rem;
  border-radius: 999px;
  color: #e5e7eb;
  text-decoration: none;
  border: 1px solid transparent;
}

.nav-link.router-link-active {
  background-color: #f9fafb;
  color: #111827;
  border-color: #d1d5db;
}

.nav-link:hover {
  background-color: #1f2937;
}

.app-main {
  max-width: 1120px;
  margin: 0 auto;
}
</style>
