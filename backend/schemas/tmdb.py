from pydantic import BaseModel
from typing import Generic, TypeVar, List

T = TypeVar("T")


class StatusResponse(BaseModel):
    status_code: int
    status_message: str


class ListResponse(BaseModel, Generic[T]):
    results: List[T]


class IdentifiableListResponse(ListResponse):
    id: int


class PaginatedListResponse(ListResponse):
    page: int
    total_pages: int
    total_results: int


class Genre(BaseModel):
    id: int
    name: str


class ProductionCompany(BaseModel):
    id: int
    logo_path: str | None
    name: str
    origin_country: str


class ProductionCountry(BaseModel):
    iso_3166_1: str
    name: str


class SpokenLanguage(BaseModel):
    english_name: str
    iso_639_1: str
    name: str


class Movie(BaseModel):
    adult: bool
    backdrop_path: str | None
    genre_ids: list[int]
    id: int
    original_language: str
    original_title: str
    overview: str
    popularity: float
    poster_path: str | None
    release_date: str
    title: str
    video: bool
    vote_average: float
    vote_count: int


class MovieDetails(BaseModel):
    adult: bool
    backdrop_path: str | None
    belongs_to_collection: str | None
    budget: int
    genres: list[Genre]
    homepage: str | None
    id: int
    imdb_id: str | None
    original_language: str
    original_title: str
    overview: str | None
    popularity: float
    poster_path: str | None
    production_companies: list[ProductionCompany]
    production_countries: list[ProductionCountry]
    release_date: str | None
    revenue: int
    runtime: int | None
    spoken_languages: list[SpokenLanguage]
    status: str | None
    tagline: str | None
    title: str
    video: bool
    vote_average: float
    vote_count: int


class MovieWatchProvider(BaseModel):
    id: int
    results: dict


class Region(BaseModel):
    iso_3166_1: str
    english_name: str
    native_name: str
