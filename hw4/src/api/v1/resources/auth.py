from fastapi import APIRouter, Depends, HTTPException, status

from src.api.v1.schemas.auth import UserBase, UserSignup, Token
from src.services.user import UserService, get_user_service

router = APIRouter()


@router.post(
    path="/signup",
    summary="User Registration",
    tags=["auth"],
)
def signup(
    user: UserSignup,
    user_service: UserService = Depends(get_user_service)
) -> dict:
    signed_user = user_service.create(user=user)
    return {'msg': 'User created.', 'user': signed_user}


@router.post(
    path="/login",
    summary="User Login",
    tags=["auth"],
)
def login(
    user: UserBase,
    user_service: UserService = Depends(get_user_service)
) -> Token:
    signed_user = user_service.login(user=user)
    if not signed_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="wrong user credentials")
    return ''