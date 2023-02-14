from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app import schemas
from app.db.engine import SessionLocal, engine
from app.routes.items import crud, models

models.Base.metadata.create_all(bind=engine)


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
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """returns a list of items.

    Args:
        skip (int, optional): The number of items to skip. Defaults to 0.
        limit (int, optional): The number of items to limit. Defaults to 100.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List: A list of items.
    """
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@router.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)
