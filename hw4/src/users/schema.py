from pydantic import BaseModel, Field, constr, EmailStr, UUID4

__all__ = (
    "UserBase",
    "UserSignup",
)


class UserBase(BaseModel):
    email: str = Field(min_length=5, max_length=20)
    password: str = Field(min_length=5, max_length=10)


class UserSignup(UserBase):
    username: str = Field(min_length=5, max_length=20)
