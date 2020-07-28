from ..db.mongodb import AsyncIOMotorClient
from ..core.config import database_name, news_collection_name


async def fetch_news_count(conn: AsyncIOMotorClient) -> int:
    count = await conn[database_name][news_collection_name].count_documents({})
    return count
