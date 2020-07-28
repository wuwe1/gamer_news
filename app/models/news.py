from typing import List, Optional

from .dbmodel import DBModelMixin
from .rwmodel import RWModel


class News(RWModel):
    title: str
    excerpt: Optional[str]
    url: str
    source: str
    image: Optional[str]
    time: int


class NewsInDB(DBModelMixin, News):
    pass


class NewsList(RWModel):
    news: List[News] = []