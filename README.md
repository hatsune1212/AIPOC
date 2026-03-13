## Org Health Survey AI PoC

This repository hosts a proof-of-concept implementation for an AI-driven
"organization health" survey platform. The goal is to structure employee
frustrations and visualize organizational health, while preserving
anonymity and surfacing concrete improvement suggestions.

The current state is a **skeleton only**. All business logic, persistence,
and AI integration are intentionally left as TODOs to be implemented via
future tickets.

### Structure

- [docs/ai-poc](docs/ai-poc): Product brief, scope map, minimal domain model, and user stories.
- [backend](backend): Python FastAPI API skeleton (Cloud Run-ready with further work).
	- [backend/app/main.py](backend/app/main.py): FastAPI app factory and health endpoint wiring.
	- [backend/app/models/domain.py](backend/app/models/domain.py): Minimal domain models derived from the domain model doc.
	- [backend/app/core/config.py](backend/app/core/config.py): Configuration skeleton using Pydantic settings.
- [frontend](frontend): Vue 3 + Vite + TypeScript SPA skeleton.
	- [frontend/src/router/index.ts](frontend/src/router/index.ts): Routes for admin, operator, and employee flows.
	- [frontend/src/pages](frontend/src/pages): Placeholder pages for main MVP scenarios (CSV import, campaigns, results, etc.).

### Getting Started (for local dev)

Backend:

1. `cd backend`
2. Create a virtualenv and install dependencies: `pip install -r requirements.txt`
3. Run the API (example): `uvicorn app.main:app --reload --port 8000`

Frontend:

1. `cd frontend`
2. Install dependencies: `npm install` (or `pnpm install` / `yarn`)
3. Start dev server: `npm run dev`

The frontend dev server (Vite) proxies `/api` requests to `http://localhost:8000` by default.

### Next Steps (Suggested Tickets)

- Define concrete API endpoints per domain (tenants, company users, employees, campaigns, responses, reports).
- Introduce persistence layer (Cloud SQL/SQLAlchemy) and migrations.
- Implement authentication/authorization for company admins, analysts, operators, and survey respondents.
- Wire email delivery (SendGrid) for survey invitations and reminders.
- Implement aggregation and n≥5 anonymity rules in the results backend and UI.
- Integrate external Python analytics module for AI-generated insights.
