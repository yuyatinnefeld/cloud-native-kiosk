from fastapi import APIRouter

from app.settings import Settings

settings = Settings()

router = APIRouter(
    tags=["Info"],
    dependencies=[],
)


@router.get("/info")
async def info():
    """Returns a dictionary with the following setting informations

    Returns:
        db_provider: The database provider used by the application.
        postgres_db_url: The PostgreSQL database URL.
        sqlite_db_url: The SQLite database URL.
    """
    return {
        "db_provider": settings.db_provier,
        "postgres_db_url": settings.postgresql_db_url,
        "sqlite_db_url": settings.sqlite_db_url,
    }
