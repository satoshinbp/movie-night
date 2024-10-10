import requests
from functools import cache
from schemas.tmdb import ListResponse, Region
from . import BASE_URL, GET_REQ_HEADERS, LANGUAGE


def get_watch_providers_route() -> str:
    return BASE_URL + "watch/providers"


@cache
def get_watch_provider_regions() -> ListResponse[Region]:
    url = get_watch_providers_route() + "/regions"
    response = requests.get(
        url,
        params={"language": LANGUAGE},
        headers=GET_REQ_HEADERS,
    )
    data = response.json()
    return data
