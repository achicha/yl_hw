from fastapi import APIRouter, Depends, HTTPException, status

from src.auth.services import AuthService, get_auth_service
from src.users.services import UserService, get_user_service

router = APIRouter(tags=["users"])


@router.get(
    path="/me",
    summary="Show my info",
)
def me_get(
        user_service: UserService = Depends(get_user_service),
        auth_service: AuthService = Depends(get_auth_service)
) -> dict:
    token = user_service.cache.get('refresh_token').decode()
    is_authorized = auth_service.check_auth(token=token)
    if not is_authorized:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"user not authorized"
        )
    email = auth_service.get_current_user_email(token)
    return {"user": user_service.get_current_user(email)}


@router.put(
    path="/me",
    summary="Update my info",
)
def me_put(
        user_data: dict,
        user_service: UserService = Depends(get_user_service),
        auth_service: AuthService = Depends(get_auth_service)
) -> dict:
    token = user_service.cache.get('refresh_token')
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"user not authorized"
        )

    token = token.decode()
    is_authorized = auth_service.check_auth(token=token)
    if not is_authorized:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"user not authorized"
        )
    email = auth_service.get_current_user_email(token)
    updated_user = user_service.update_info(email, user_data)

    return {
        "msg:": "Update is successful",
        "user": updated_user
    }
