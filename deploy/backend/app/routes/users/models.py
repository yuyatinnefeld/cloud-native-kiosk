from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.engine import Base


class User(Base):
    """
    Takes a user's email and password and returns a User object
    if the user exists and the password is correct.
    If the user does not exist or the password is incorrect, it returns None.

    Args:
        Base (_type_): _description_
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
