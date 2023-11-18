from dataclasses import dataclass
from typing import List, Generic, TypeVar, Optional

T = TypeVar('T')


@dataclass
class Quote:
    _id: str
    dialog: str
    movie: str
    character: str
    id: str


@dataclass
class Character:
    _id: str
    height: str
    race: str
    gender: str
    birth: str
    spouse: str
    death: str
    realm: str
    hair: str
    name: str
    wikiUrl: str


@dataclass
class PaginatedResponse(Generic[T]):
    docs: List[T]
    total: int
    limit: int
    offset: int
    page: int
    pages: int


@dataclass
class Movie:
    _id: str
    name: str


@dataclass
class SearchFilters:
    race: Optional[str] = None
    gender: Optional[str] = None
    realm: Optional[str] = None
    name: Optional[str] = None


@dataclass
class Page:
    page: int = 1
    limit: int = 5
