from fastcrud import FastCRUD

from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from src.security_module import (
    create_pair_tokens,
    create_access_jwt_token,
    verify_jwt_token
)

from src.database.core import async_session_maker

from src.database.models.auth_models import Auth
from src.auth_service.schemas import (
    Auth_shema,
    Access_token,
    Refresh_token,
    Pair_tokens
)


auth_crud = FastCRUD(Auth)


class Auth_service:

    async def create_user(self, payload: Auth_shema):
        async with async_session_maker() as db:
            if await auth_crud.exists(db, username=payload.username):
                raise HTTPException(status_code=403, detail="user exists")

            return await auth_crud.create(db, payload)

    async def login_user(self, payload: OAuth2PasswordRequestForm):
        payload = Auth_shema(
            username=payload.username,
            password=payload.password
        )

        async with async_session_maker() as db:
            if not await auth_crud.exists(db, username=payload.username):
                raise HTTPException(status_code=404, detail="user not exists")
            if not await auth_crud.exists(
                db,
                username=payload.username,
                password=payload.password
            ):
                raise HTTPException(status_code=403, detail="forbidden")

        pair_tokens: Pair_tokens = await create_pair_tokens(payload.username)
        return Pair_tokens(**pair_tokens)

    async def update_token(self, payload: Refresh_token):
        data_from_refresh = await verify_jwt_token(payload.refresh_token)
        if data_from_refresh is None:
            raise HTTPException(status_code=403, detail="bad token")
        access_token = Access_token(
            access_token=await create_access_jwt_token(
                data_from_refresh
            )
        )
        return access_token

    async def who_is_it(self, token: str) -> str | None:
        return await verify_jwt_token(token)
