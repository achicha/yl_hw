from typing import Union, Optional
from functools import lru_cache
from sqlmodel import Session
from fastapi import Depends
from jose import jwt, JWTError
from datetime import datetime as dt, timedelta as td

from src.db import AbstractCache, get_cache, get_session
from src.core.mixins import ServiceMixin
from src.core.config import JWT_SECRET_KEY, JWT_ALGORITHM, JWT_EXPIRATION_TIME, CACHE_EXPIRE_IN_SECONDS


class AuthService(ServiceMixin):
    @staticmethod
    def get_current_user_email(token) -> dict:
        """check that token is not expired"""
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload.get('email')

    def create_token(self, email):
        """create new token"""
        exp_time = dt.utcnow() + td(minutes=JWT_EXPIRATION_TIME)
        to_encode = {'email': email, "exp": exp_time}
        token = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
        self.cache.set(key=email, value=token, expire=CACHE_EXPIRE_IN_SECONDS)
        return token

    def get_active_token(self, email) -> str:
        """check that token is not expired"""
        active_token = self.cache.get(key=f"{email}")
        return active_token

    def check_auth(self, token: str) -> bool:
        """verify token"""
        try:
            email = self.get_current_user_email(token)
            if not email:
                return False

            active_token = self.get_active_token(email)
            if not active_token:
                return False

            return True

        except JWTError:
            return False


@lru_cache()
def get_auth_service(
        cache: AbstractCache = Depends(get_cache),
        session: Session = Depends(get_session),
) -> AuthService:
    return AuthService(cache=cache, session=session)
