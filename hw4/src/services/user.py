from typing import Union
from functools import lru_cache
from sqlmodel import Session
from fastapi import Depends

from src.db import AbstractCache, get_cache, get_session
from src.services import ServiceMixin
from src.models.user import User
from src.core.verify import get_password_hash, verify_password
from src.api.v1.schemas.auth import UserBase, UserSignup, Token


class UserService(ServiceMixin):
    def create(self, user: UserSignup) -> User:
        new_user = User(
            username=user.username,
            email=user.email,
            password=get_password_hash(user.password)
        )
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user

    def login(self, user: UserBase) -> Union[str, Token]:
        # get user from db
        user_exist = self.session.query(User).filter(User.username == user.username).first()
        if not user_exist or verify_password(user.password, user_exist.password_hash):
            return None

        # create refresh token


        # create access token

        return Token(

        )


@lru_cache()
def get_user_service(
        cache: AbstractCache = Depends(get_cache),
        session: Session = Depends(get_session),
) -> UserService:
    return UserService(cache=cache, session=session)
