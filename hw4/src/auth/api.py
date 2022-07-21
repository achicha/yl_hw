from fastapi import APIRouter, Depends, HTTPException, status

from src.auth.schema import Login
from src.auth.services import AuthService, get_auth_service
from src.users.services import UserService, get_user_service

router = APIRouter(tags=["auth"])


@router.post(
    path="/signup",
    status_code=status.HTTP_201_CREATED,
    summary="User Registration",
)
def signup(
        user: Login,
        user_service: UserService = Depends(get_user_service),
        auth_service: AuthService = Depends(get_auth_service)
) -> dict:
    # add user
    if user_service.get_current_user(user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"user with email {user.email} already exist"
        )
    new_user = user_service.register_new_user(
                username=user.username,
                email=user.email,
                password=user.password
            )
    if not new_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"error in registration"
        )

    # create token
    auth_service.create_token(user.email)

    return {"msg": "User created.", "user": new_user}


@router.post(
    path="/login",
    summary="User Login",
)
def login(
        user: Login,
        user_service: UserService = Depends(get_user_service),
        auth_service: AuthService = Depends(get_auth_service)
) -> dict:
    usr = user_service.get_current_user(user.email)
    if not usr:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credentials. Email not found"
        )
    if not user_service.verify_user_password(user.password, usr.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credentials. Wrong Password"
        )
    refresh_token = auth_service.get_active_token(email=user.email)
    if not refresh_token:
        auth_service.create_token(user.email)
        refresh_token = auth_service.get_active_token(email=user.email)

    return {
        "access_token": refresh_token,
        "refresh_token": refresh_token
    }


@router.post(
    path="/refresh",
    summary="User Token Refresh",
)
def refresh(
) -> dict:
    pass


@router.post(
    path="/logout",
    summary="Logout from current device",
)
def logout(
) -> dict:
    pass


@router.post(
    path="/logout_all",
    summary="Logout from all device",
)
def logout_all() -> dict:
    # todo:
    pass
