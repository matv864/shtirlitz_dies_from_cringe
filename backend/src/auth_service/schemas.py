from pydantic import BaseModel, field_validator

from src.security_module import get_hashing_password


class Auth_shema(BaseModel):
    username: str
    password: str

    @field_validator('password')
    @classmethod
    def ensure_foobar(cls, password: str):
        return get_hashing_password(password)


class Its_me(BaseModel):
    username: str


class Access_token(BaseModel):
    access_token: str


class Refresh_token(BaseModel):
    refresh_token: str


class Pair_tokens(BaseModel):
    token_type: str = "bearer"
    access_token: str
    refresh_token: str
