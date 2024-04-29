from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from typing import Annotated

from src.auth_service.service import Auth_service
from src.auth_service.schemas import (
    Auth_shema,
    Access_token,
    Refresh_token,
    Pair_tokens
)

auth_router = APIRouter(tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


@auth_router.post("/registration", status_code=status.HTTP_201_CREATED)
async def registration_user(payload: Auth_shema):
    return await Auth_service().create_user(payload)


@auth_router.post("/login", response_model=Pair_tokens)
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    # print(form_data.username, form_data.password)
    return await Auth_service().login_user(form_data)


@auth_router.post("/refresh", response_model=Access_token)
async def refresh(payload: Refresh_token):
    return await Auth_service().update_token(payload)


# ----
async def who_is_it(token: Annotated[str, Depends(oauth2_scheme)]):
    return await Auth_service().who_is_it(token)


@auth_router.post("/who_am_i")
async def who_am_i(current_user: str = Depends(who_is_it)):
    return current_user
