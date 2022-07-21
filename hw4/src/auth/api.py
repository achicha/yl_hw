from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from src.auth.schema import Login
from src.auth.services import AuthService, get_auth_service
from src.users.services import UserService, get_user_service

router = APIRouter(tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post(
    path="/signup",
    status_code=status.HTTP_201_CREATED,
    summary="User Registration",
)
def signup(
        user: Login,
        user_service: UserService = Depends(get_user_service),
        auth_service: AuthService = Depends(get_auth_service),
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
    token = auth_service.create_token(user.email)
    user_service.cache.set(key='refresh_token', value=token)

    return {"msg": "User created.", "user": new_user}


@router.post(
    path="/login",
    summary="User Login",
)
def login(
        user: Login,
        user_service: UserService = Depends(get_user_service),
        auth_service: AuthService = Depends(get_auth_service),
) -> dict:
    # user exist
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
    # token exist
    token = auth_service.get_active_token(email=user.email)
    if not token:
        token = auth_service.create_token(user.email)

    # save token into local cache
    user_service.cache.set(key='refresh_token', value=token)

    return {
        "access_token": token,
        "refresh_token": token
    }


@router.post(
    path="/refresh",
    summary="User Token Refresh",
)
def refresh(
    user_service: UserService = Depends(get_user_service),
    auth_service: AuthService = Depends(get_auth_service),
) -> dict:
    # find email
    token = user_service.cache.get('refresh_token').decode()
    is_authorized = auth_service.check_auth(token=token)
    if not is_authorized:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"user not authorized"
        )

    email = auth_service.get_current_user_email(token=token)

    # create new token
    new_token = auth_service.create_token(email)
    user_service.cache.set(key='refresh_token', value=new_token)

    return {
        "access_token": new_token,
        "refresh_token": new_token
    }


@router.post(
    path="/logout",
    summary="Logout from current device",
)
def logout(
    auth_service: AuthService = Depends(get_auth_service),
) -> dict:
    auth_service.cache.remove("refresh_token")
    return {"msg": "You have been logged out"}


@router.post(
    path="/logout_all",
    summary="Logout from all device",
)
def logout_all(
    auth_service: AuthService = Depends(get_auth_service),
) -> dict:
    auth_service.cache.remove("refresh_token")
    auth_service.cache.close()
    return {"msg": "You have been logged out from all devices"}
