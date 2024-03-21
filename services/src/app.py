from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from src.api.v1.router import v1_router

app = FastAPI(
    title="services",
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(v1_router)
