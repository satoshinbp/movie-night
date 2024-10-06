import requests
from pydantic import BaseModel

from . import BASE_URL, GET_REQ_HEADERS, POST_REQ_HEADERS


class WatchlistMovie(BaseModel):
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


class GetWatchlistMoviesResponseBody(BaseModel):
    page: int
    results: list[WatchlistMovie]
    total_pages: int
    total_results: int


def get_watchlist_movies(account_id: int, page: int) -> GetWatchlistMoviesResponseBody:
    url = BASE_URL + f"account/{account_id}/watchlist/movies"
    response = requests.get(
        url,
        params={
            "language": "en-US",
            "page": page,
        },
        headers=GET_REQ_HEADERS,
    )
    data = response.json()
    return data


class AddToWatchlistResponseBody(BaseModel):
    status_code: int
    status_message: str


def add_to_watchlist(
    account_id: int, media_type: str, media_id: int, add: bool
) -> AddToWatchlistResponseBody:
    url = BASE_URL + f"account/{account_id}/watchlist"
    payload = {"media_type": media_type, "media_id": media_id, "watchlist": add}
    response = requests.post(
        url,
        headers=POST_REQ_HEADERS,
        json=payload,
    )
    data = response.json()
    return data
