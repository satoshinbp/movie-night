import requests
from schemas.tmdb import StatusResponse, Movie, PaginatedListResponse
from . import BASE_URL, GET_REQ_HEADERS, POST_REQ_HEADERS, LANGUAGE


def get_account_route(account_id: int) -> str:
    return BASE_URL + f"account/{account_id}"


def get_watchlist_movies(account_id: int, page: int) -> PaginatedListResponse[Movie]:
    url = get_account_route(account_id) + "/watchlist/movies"
    response = requests.get(
        url,
        params={"language": LANGUAGE, "page": page},
        headers=GET_REQ_HEADERS,
    )
    data = response.json()
    return data


def add_to_watchlist(
    account_id: int, media_type: str, media_id: int, add: bool
) -> StatusResponse:
    url = get_account_route(account_id) + "/watchlist"
    payload = {"media_type": media_type, "media_id": media_id, "watchlist": add}
    response = requests.post(
        url,
        headers=POST_REQ_HEADERS,
        json=payload,
    )
    data = response.json()
    return data
