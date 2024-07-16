import requests
from url import BASE_URL
from ..types import Region


def get_tmbd_provider(access_token: str, movie_id: int) -> list[Region]:
    url = BASE_URL + f"movie/{movie_id}/watch/providers"
    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {access_token}",
        },
    )
    data = response.json()
    return data["results"]


def get_tmbd_runtime(access_token: str, movie_id: int) -> int:
    url = BASE_URL + f"movie/{movie_id}"
    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {access_token}",
        },
    )
    data = response.json()
    return data["runtime"]
