import jwt
from datetime import datetime, timedelta

from fastapi import HTTPException

SECRET_KEY = "my_secret_key"
ALGORITHM = "HS256"
EXPIRATION_TIME_ACCESS = timedelta(minutes=30)
EXPIRATION_TIME_REFRESH = timedelta(days=3)


async def create_jwt_token(username: str, expiration_time):
    data = {
        "username": username
    }
    # expiration = datetime.utcnow() + EXPIRATION_TIME
    expiration = datetime.now() + expiration_time
    data.update({"exp": expiration})
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token


async def create_access_jwt_token(username: str):
    return await create_jwt_token(username, EXPIRATION_TIME_ACCESS)


async def create_refresh_jwt_token(username: str):
    return await create_jwt_token(username, EXPIRATION_TIME_REFRESH)


async def create_pair_tokens(username: str):
    pair = {
        "access_token": await create_access_jwt_token(username),
        "refresh_token": await create_refresh_jwt_token(username)
    }
    return pair


async def verify_jwt_token(token: str):
    try:
        decoded_data = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return decoded_data["username"]
    except jwt.PyJWTError:
        raise HTTPException(status_code=403, detail="bad token")
