from fastapi import APIRouter


router = APIRouter(tags=["health"])


@router.get("/health", summary="Health check")
async def health_check() -> dict:
    """Simple health endpoint for Cloud Run/load balancer checks."""

    return {"status": "ok"}
