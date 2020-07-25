from typing import List

from ..db.mongodb import AsyncIOMotorClient
from ..models.news import NewsInDB
from ..core.config import database_name, news_collection_name


async def fetch_all_news(conn: AsyncIOMotorClient) -> List[NewsInDB]:
    news = []
    rows = conn[database_name][news_collection_name].find()
    async for row in rows:
        news.append(NewsInDB(**row))

    return news

async def fetch_news_with_pagination(conn: AsyncIOMotorClient, pageNum: int, pageSize: int) -> List[NewsInDB]:
    news = []
    offset = pageSize * (pageNum - 1)
    rows = conn[database_name][news_collection_name].find().sort('time', -1).skip(offset).limit(pageSize)
    async for row in rows:
        news.append(NewsInDB(**row))

    return news