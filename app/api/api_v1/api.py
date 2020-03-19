from fastapi import APIRouter

from app.api.api_v1.endpoints import sentence

api_router = APIRouter()

api_router.include_router(sentence.router, prefix="/sentence", tags=["sentence"])
