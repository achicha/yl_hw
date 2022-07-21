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
    def create_token(self, email):
        """create new token"""
        exp_time = dt.utcnow() + td(minutes=JWT_EXPIRATION_TIME)
        to_encode = {'email': email, "exp": exp_time}
        token = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
        self.cache.set(key=email, value=token, expire=CACHE_EXPIRE_IN_SECONDS)

    def get_active_token(self, email: str) -> str:
        """check that token is not expired"""
        active_token = self.cache.get(key=f"{email}")
        if not active_token:
            return None
        return active_token

    def remove_active_token(self, email):
        token = self.get_active_token(email)
        self.cache.active_tokens.remove(key=email, value=token)

    @staticmethod
    def verify_token(token: str) -> bool:
        """verify token"""
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            email = payload.get('email')
            if email is None:
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
