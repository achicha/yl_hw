from fastapi import APIRouter, Depends, HTTPException, status

from src.users import hashing
from src.users.schema import UserBase, UserSignup
from src.users.services import UserService, get_user_service
from src.db.redis_cache import active_refresh_tokens, blocked_access_tokens

router = APIRouter()


@router.post(
    path="/signup",
    status_code=status.HTTP_201_CREATED,
    summary="User Registration",
    tags=["auth"]
)
def signup(user: UserSignup, user_service: UserService = Depends(get_user_service)) -> dict:
    if user_service.verify_email_exist(user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"user with email {user.email} already exist"
        )
    return {"msg": "User created.", "user": user_service.register_new_user(user=user)}


@router.post(
    path="/login",
    summary="User Login",
    tags=["auth"]
)
def login(user: UserBase, user_service: UserService = Depends(get_user_service)) -> dict:
    usr = user_service.get_current_user(user.email)
    if not usr:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credentials"
        )
    if not hashing.verify_password(user.password, usr.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credentials"
        )

    refresh_token = hashing.create_token({"email": usr.email, "type": "refresh"})
    active_refresh_tokens.set(key=usr.email, value=refresh_token)

    return {
        "access_token": hashing.create_token({"email": usr.email, "type": "access"}),
        "refresh_token": hashing.create_token({"email": usr.email, "type": "refresh"})
    }


@router.post(
    path="/refresh",
    summary="User Token Refresh",
    tags=["auth"]
)
def refresh() -> dict:
    # todo:
    pass


@router.post(
    path="/logout",
    summary="Logout from current device",
    tags=["auth"]
)
def logout() -> dict:
    # todo:
    pass


@router.post(
    path="/logout_all",
    summary="Logout from all device",
    tags=["auth"]
)
def logout_all() -> dict:
    # todo:
    pass


@router.get(
    path="/users/me",
    summary="Show my info",
    tags=["users"]
)
def me_get() -> dict:
    # todo:
    pass


@router.put(
    path="/users/me",
    summary="Update my info",
    tags=["users"]
)
def me_put() -> dict:
    # todo:
    pass
