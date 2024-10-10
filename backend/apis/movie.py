import requests
from functools import cache
from schemas.tmdb import MovieDetails, MovieWatchProvider
from . import BASE_URL, GET_REQ_HEADERS


def get_movie_route(movie_id: int) -> str:
    return BASE_URL + f"movie/{movie_id}"


def get_movie_watch_provider(movie_id: int) -> MovieWatchProvider:
    url = get_movie_route(movie_id) + f"/watch/providers"
    response = requests.get(url, headers=GET_REQ_HEADERS)
    data = response.json()
    return data


@cache
def get_movie_details(movie_id: int) -> MovieDetails:
    url = get_movie_route(movie_id)
    response = requests.get(url, headers=GET_REQ_HEADERS)
    data = response.json()
    return data
