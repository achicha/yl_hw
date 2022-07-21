from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel, UniqueConstraint

__all__ = ("User",)


class User(SQLModel, table=True):
    __table_args__ = (UniqueConstraint('email'), UniqueConstraint('username'))
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(nullable=False)
    email: str = Field(nullable=False)
    password: str = Field(nullable=False)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
