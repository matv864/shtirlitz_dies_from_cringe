from typing import AsyncGenerator

from fastapi import FastAPI

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)
from sqlalchemy.ext.declarative import declarative_base

from src.database.settings import get_settings

Base = declarative_base()
engine = create_async_engine(get_settings().postgres_url)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
