from pydantic import BaseModel
from typing import Optional


class Message(BaseModel):
    title: str = "CNK ERROR"
    text: str = "this is a placeholder text from FastAPI alerting backend"
    link: Optional[str] = "https://example.com"
    color: Optional[str] = "#5F9EA0"
