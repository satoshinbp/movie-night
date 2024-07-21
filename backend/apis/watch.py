import requests
import os

from schemas.tmdb import Region


def get_tmbd_regions() -> list[Region]:
    url = os.getenv("BASE_URL") + "watch/providers/regions"
    access_token = os.getenv("TMDB_ACCESS_TOKEN")
    response = requests.get(
        url,
        params={
            "language": "en-US",
        },
        headers={
            "Authorization": f"Bearer {access_token}",
        },
    )
    data = response.json()
    return data["results"]
