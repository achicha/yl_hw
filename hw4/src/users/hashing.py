from datetime import datetime as dt, timedelta as td
from jose import jwt, JWTError
from typing import Union, Any
from passlib.context import CryptContext

from src.core.config import JWT_SECRET_KEY, JWT_ALGORITHM, JWT_EXPIRATION_TIME


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """get password hash"""
    return pwd_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    """verify password"""
    return pwd_context.verify(password, password_hash)


def create_token(subject: dict) -> str:
    """generate encoded token"""
    to_encode = subject
    to_encode.update({
        "exp": dt.utcnow() + td(minutes=JWT_EXPIRATION_TIME),
    })
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


def verify_token(token: str) -> str:
    """Gets jti from token"""
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        email = payload.get('email')
        if email is None:
            raise Exception
    except JWTError:
        raise Exception
