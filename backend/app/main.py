from fastapi import FastAPI

from app.routers import health


def create_app() -> FastAPI:
    """Application factory for the backend API.

    This wires up only minimal routing; business logic is intentionally
    left as TODOs for later tickets.
    """

    application = FastAPI(title="Org Health Survey API", version="0.1.0")

    # Core, non-domain-specific routes
    application.include_router(health.router, prefix="/api")

    return application


app = create_app()
