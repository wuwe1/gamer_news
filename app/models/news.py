from typing import List

from .dbmodel import DBModelMixin
from .rwmodel import RWModel


class News(RWModel):
    title: str
    excerpt: str
    url: str
    source: str
    time: int


class NewsInDB(DBModelMixin, News):
    pass


class NewsList(RWModel):
    news: List[News] = []