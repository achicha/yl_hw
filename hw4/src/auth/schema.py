from typing import Optional
from pydantic import BaseModel, Field


__all__ = (
    "Login",
)


class Login(BaseModel):
    username: Optional[str]
    email: str = Field(min_length=5, max_length=20)
    password: str = Field(min_length=5, max_length=10)
