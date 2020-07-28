from fastapi import APIRouter

from .endpoints.news import router as news_router
from .endpoints.count import router as count_router

router = APIRouter()
router.include_router(news_router)
router.include_router(count_router)
