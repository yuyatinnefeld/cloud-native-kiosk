from pydantic import BaseSettings


class Settings(BaseSettings):
    """Stores the settings for the backend application.

    Attributes:
        db_provider (str): The database provider to use.
        postgresql_db_url (str): The URL for the PostgreSQL database.
        sqlite_db_url (str): The URL for the SQLite database.

    Args:
        BaseSettings (_type_): _description_
    """

    db_provier: str = "postgresql"
    postgresql_db_url: str = "postgresql://user:password@postgresserver/db"
    sqlite_db_url: str = "sqlite:///./sql_app.db"
