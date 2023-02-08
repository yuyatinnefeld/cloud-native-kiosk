from fastapi import APIRouter
from typing import Union


router = APIRouter(
    tags=["Info"],
    dependencies=[],
)


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
