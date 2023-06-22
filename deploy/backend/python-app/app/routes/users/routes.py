from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.db.engine import SessionLocal, engine
from app.routes.users import crud, models


models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    tags=["Users"],
    dependencies=[],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)) -> models.User:
    """
    Creates a new user in the database.
    Args:
        user (schemas.UserCreate): The user to create.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Raises:
        HTTPException: If the email is already registered.

    Returns:
        models.User: The created user.
    """
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return crud.create_user(db=db, user=user)


@router.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List:
    """
    Reads a list of users from the database.

    Args:
        skip (int, optional): Number of users to skip.. Defaults to 0.
        limit (int, optional): Maximum number of users to retrieve.. Defaults to 100.
        db (Session, optional): Database session.. Defaults to Depends(get_db).

    Returns:
        List[models.User]: List of users.
    """
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)) -> models.User:
    """Reads a user from the database.

    Args:
        user_id (int): The ID of the user to read.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Raises:
        HTTPException: If the user is not found.

    Returns:
        models.User: The database user
    """
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
