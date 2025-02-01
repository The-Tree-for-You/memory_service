from fastapi import FastAPI
from .routers import memory

memory_app = FastAPI()
memory_app.include_router(memory.router, prefix="/memory", tags=["memory"])