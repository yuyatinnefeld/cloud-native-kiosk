from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app import schemas
from app.db.engine import SessionLocal
from app.routes.items import crud, models


router = APIRouter(
    tags=["Items"],
    dependencies=[],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List:
    """returns a list of items.

    Args:
        skip (int, optional): The number of items to skip.
        limit (int, optional): The number of items to limit.
        db (Session, optional): The database session.
    Returns:
        List: A list of items.
    """
    items = crud.get_items(db, skip=skip, limit=limit)
    print("read_items: ", type(items))
    return items


@router.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
) -> models.Item:
    result = crud.create_user_item(db=db, item=item, user_id=user_id)
    return result
