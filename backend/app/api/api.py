from fastapi import APIRouter
from .endpoints import count

api_router = APIRouter()
api_router.include_router(count.router)
