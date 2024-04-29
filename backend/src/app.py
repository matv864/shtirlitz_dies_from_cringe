from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.database.core import lifespan

from src.auth_service.api import auth_router
# from src.pets_service.api.router import pets_service_router


app = FastAPI(
    title="services",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
# app.include_router(pets_service_router)
