import requests
from functools import cache
from pydantic import BaseModel

from . import BASE_URL, GET_REQ_HEADERS


class Region(BaseModel):
    iso_3166_1: str
    english_name: str
    native_name: str


class GetWatchProviderRegionsResponseBody(BaseModel):
    results: list[Region]


@cache
def get_watch_provider_regions() -> GetWatchProviderRegionsResponseBody:
    url = BASE_URL + "watch/providers/regions"
    response = requests.get(
        url,
        params={
            "language": "en-US",
        },
        headers=GET_REQ_HEADERS,
    )
    data = response.json()
    return data
