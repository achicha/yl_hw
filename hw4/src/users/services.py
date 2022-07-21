from typing import Union
from functools import lru_cache
from sqlmodel import Session
from fastapi import Depends
from passlib.context import CryptContext

from src.db import AbstractCache, get_cache, get_session
from src.core.mixins import ServiceMixin
from src.users.models import User


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService(ServiceMixin):
    def register_new_user(self, username: str, email: str, password: str) -> User:
        """add new user to db"""
        new_user = User(
            username=username,
            email=email,
            password=pwd_context.hash(password)
        )
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user

    def get_current_user(self, email: str) -> Union[None, User]:
        """verify that email already exist in our DB"""
        return self.session.query(User).filter(User.email == email).first()

    @staticmethod
    def verify_user_password(password, password_hash):
        return pwd_context.verify(password, password_hash)


@lru_cache()
def get_user_service(
        cache: AbstractCache = Depends(get_cache),
        session: Session = Depends(get_session),
) -> UserService:
    return UserService(cache=cache, session=session)
