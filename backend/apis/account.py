import requests
import os


def get_tmbd_watchlist(account_id: int, page: int) -> dict:
    url = os.getenv("BASE_URL") + f"account/{account_id}/watchlist/movies"
    access_token = os.getenv("TMDB_ACCESS_TOKEN")
    response = requests.get(
        url,
        params={
            "language": "en-US",
            "page": page,
        },
        headers={
            "accept": "application/json",
            "Authorization": f"Bearer {access_token}",
        },
    )
    data = response.json()
    return data


def add_to_tmbd_watchlist(
    account_id: int, media_type: str, media_id: int, add: bool
) -> dict:
    url = os.getenv("BASE_URL") + f"account/{account_id}/watchlist"
    access_token = os.getenv("TMDB_ACCESS_TOKEN")
    payload = {"media_type": media_type, "media_id": media_id, "watchlist": add}
    print(url, payload)
    response = requests.post(
        url,
        headers={
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Bearer {access_token}",
        },
        json=payload,
    )
    data = response.json()
    print(data)
    return data
