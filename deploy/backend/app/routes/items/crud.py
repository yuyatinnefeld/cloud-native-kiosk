from sqlalchemy.orm import Session

from app.routes.items import models
from app import schemas


def get_items(db: Session, skip: int = 0, limit: int = 100):
    """Get items from the database.

    Args:
        db (Session): The database session.
        skip (int, optional): The number of items to skip. Defaults to 0.
        limit (int, optional): The number of items to limit to. Defaults to 100.

    Returns:
        List: The list of items from the database.
    """
    result = db.query(models.Item).offset(skip).limit(limit).all()
    return result


def create_user_item(
    db: Session, item: schemas.ItemCreate, user_id: int
) -> models.Item:
    """Create a new item for a user.

    Args:
        db (Session): The database session.
        item (schemas.ItemCreate): The item to create.
        user_id (int): The user to create the item for.

    Returns:
        models.Item: The created item.
    """
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
