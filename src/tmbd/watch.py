import requests
from url import BASE_URL
from ..types import Region


def get_tmbd_regions(access_token) -> list[Region]:
    url = BASE_URL + "watch/providers/regions"
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
