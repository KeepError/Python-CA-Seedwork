import uuid
from typing import Annotated

from api.v1.dependencies.use_cases import get_user_use_case
from domain.user import errors as domain_errors
from domain.user.usecases import UserUseCase
from fastapi import APIRouter, Depends, HTTPException

from . import models as api_models

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.get("/{user_id}", response_model=api_models.User)
def get_user(
        user_use_case: Annotated[UserUseCase, Depends(get_user_use_case)],
        user_id: uuid.UUID,
):
    try:
        user = user_use_case.get(user_id)
    except domain_errors.UserNotFoundError:
        raise HTTPException(status_code=404, detail="User not found")
    return api_models.User(id=user.id, username=user.username, email=user.email)
