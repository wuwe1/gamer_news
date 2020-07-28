from fastapi import APIRouter, Depends

from ....crud.count import fetch_news_count
from ....db.mongodb import AsyncIOMotorClient, get_database

router = APIRouter()

@router.get("/count", response_model=int, tags=["news"])
async def get_news_count(db: AsyncIOMotorClient = Depends(get_database)):
    count = await fetch_news_count(db)
    return count