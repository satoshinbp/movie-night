import requests
from functools import cache
from pydantic import BaseModel

from . import BASE_URL, GET_REQ_HEADERS


class GetMovieWatchProviderResponseBody(BaseModel):
    id: int
    results: dict


def get_movie_watch_provider(movie_id: int) -> GetMovieWatchProviderResponseBody:
    url = BASE_URL + f"movie/{movie_id}/watch/providers"
    response = requests.get(
        url,
        headers=GET_REQ_HEADERS,
    )
    data = response.json()
    return data


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


class GetMovieDetailsResponseBody(BaseModel):
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


@cache
def get_movie_details(movie_id: int) -> GetMovieDetailsResponseBody:
    url = BASE_URL + f"movie/{movie_id}"
    response = requests.get(
        url,
        headers=GET_REQ_HEADERS,
    )
    data = response.json()
    return data
