from sqlalchemy.orm import Session

from app.routes.users import models
from app import schemas


def get_user(db: Session, user_id: int):
    """Get a user from the database by the user id.

    Args:
        db (Session): The database session.
        user_id (int): The id of the user to get.

    Returns:
        ???: The user with id `user_id` or `None` if no user with that id exists.
    """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """Get a user by email.

    Args:
        db (Session): The database session.
        email (str): The email of the user.

    Returns:
        ???: The user with the given email.

    """
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """Get a list of users from the database.

    Args:
        db (Session): The database session.
        skip (int, optional): The number of users to skip. Defaults to 0.
        limit (int, optional): The number of users to limit. Defaults to 100.

    Returns:
        List[models.User]: The list of users.
    """
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    """Create a new user in the database.

    Args:
        db (Session): The database session.
        user (schemas.UserCreate): The user to create.

    Returns:
        ???: The created user.
    """
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
