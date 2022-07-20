from pydantic import BaseModel, Field, constr, EmailStr, UUID4

__all__ = (
    "UserBase",
    "UserSignup",
)


class UserBase(BaseModel):
    username: str = Field(min_length=5, max_length=10)
    password: str = Field(min_length=5, max_length=10)


class UserSignup(UserBase):
    email: str = Field(min_length=5, max_length=20)


class Token:
    access_token: str = Field(min_length=5)
    refresh_token: str = Field(min_length=5)
