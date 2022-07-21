from fastapi import APIRouter, Depends, status

from src.users.schema import UserBase, UserSignup

router = APIRouter(tags=["users"])


@router.get(
    path="/me",
    summary="Show my info",
)
def me_get() -> dict:
    # todo:
    pass


@router.put(
    path="/me",
    summary="Update my info",
)
def me_put() -> dict:
    # todo:
    pass
