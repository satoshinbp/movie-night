import requests
import os
from pydantic import BaseModel


class Region(BaseModel):
    iso_3166_1: str
    english_name: str
    native_name: str


class GetWatchProviderRegionsResponseBody(BaseModel):
    results: list[Region]


def get_watch_provider_regions() -> GetWatchProviderRegionsResponseBody:
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
    return data
