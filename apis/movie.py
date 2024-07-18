import requests
import os

from schemas.tmdb import Region


def get_tmbd_provider(movie_id: int) -> list[Region]:
    url = os.getenv("BASE_URL") + f"movie/{movie_id}/watch/providers"
    access_token = os.getenv("TMDB_ACCESS_TOKEN")
    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {access_token}",
        },
    )
    data = response.json()
    return data["results"]


def get_tmbd_runtime(movie_id: int) -> int:
    url = os.getenv("BASE_URL") + f"movie/{movie_id}"
    access_token = os.getenv("TMDB_ACCESS_TOKEN")
    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {access_token}",
        },
    )
    data = response.json()
    return data["runtime"]
