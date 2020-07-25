from fastapi import APIRouter, Depends

from ....crud.news import fetch_news_with_pagination
from ....db.mongodb import AsyncIOMotorClient, get_database
from ....models.news import NewsList, News

router = APIRouter()


# @router.get("/news", response_model=NewsList, tags=["news"])
# async def get_all_news(db: AsyncIOMotorClient = Depends(get_database)):
#     news = await fetch_all_news(db, )
#     return NewsList(news=[News(**n.dict()) for n in news])


@router.get("/news", response_model=NewsList, tags=["news"])
async def get_news_by_page(pageNum: int, pageSize: int, db: AsyncIOMotorClient = Depends(get_database)):
    news = await fetch_news_with_pagination(db, pageNum, pageSize)
    return NewsList(news=[News(**n.dict()) for n in news])