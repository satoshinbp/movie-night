from pydantic import BaseModel


class Movie(BaseModel):
    adult: bool
    backdrop_path: str
    genre_ids: list[int]
    id: int
    original_language: str
    overview: str
    popularity: float
    poster_path: str
    release_date: str
    title: str
    video: bool
    vote_average: float
    vote_count: int
    netflix_regions: list[str]
    runtime: int


class Region(BaseModel):
    iso_3166_1: str
    english_name: str
    native_name: str
