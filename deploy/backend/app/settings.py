from pydantic import BaseSettings


class Settings(BaseSettings):
    db_provier: str = "postgresql"
    postgresql_db_url: str = "postgresql://user:password@postgresserver/db"
    sqlite_db_url: str = "sqlite:///./sql_app.db"
