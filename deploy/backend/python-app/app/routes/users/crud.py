from typing import List

from sqlalchemy.orm import Session

from app.routes.users import models
from app import schemas


def get_user(db: Session, user_id: int) -> models.User:
    """Get a user from the database by the user id.

    Args:
        db (Session): The database session.
        user_id (int): The id of the user to get.

    Returns:
        models.User: The user with id `user_id` or `None` if no user with that id exists.
    """
    result = db.query(models.User).filter(models.User.id == user_id).first()
    return result


def get_user_by_email(db: Session, email: str) -> models.User:
    """Get a user by email.

    Args:
        db (Session): The database session.
        email (str): The email of the user.

    Returns:
        models.User: The user with the given email.

    """
    result = db.query(models.User).filter(models.User.email == email).first()
    return result


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List:
    """Get a list of users from the database.

    Args:
        db (Session): The database session.
        skip (int, optional): The number of users to skip. Defaults to 0.
        limit (int, optional): The number of users to limit. Defaults to 100.

    Returns:
        List[models.User]: The list of users.
    """
    result = db.query(models.User).offset(skip).limit(limit).all()
    return result


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    """Create a new user in the database.

    Args:
        db (Session): The database session.
        user (schemas.UserCreate): The user to create.

    Returns:
        models.User: The created user.
    """
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
