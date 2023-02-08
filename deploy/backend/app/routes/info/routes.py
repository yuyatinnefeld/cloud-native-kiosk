from fastapi import APIRouter

from app.settings import Settings

settings = Settings()

router = APIRouter(
    tags=["Info"],
    dependencies=[],
)


@router.get("/info")
async def info():
    return {
        "db_provider": settings.db_provier,
        "postgres_db_url": settings.postgresql_db_url,
        "sqlite_db_url": settings.sqlite_db_url,
    }
