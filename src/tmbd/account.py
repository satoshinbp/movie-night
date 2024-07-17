import requests
import os

from src.schema import Movie


def get_tmbd_watchlist(account_id: int) -> list[Movie]:
    url = os.getenv("BASE_URL") + f"account/{account_id}/watchlist/movies"
    access_token = os.getenv("TMDB_ACCESS_TOKEN")
    movies = []
    page = 1
    while True:
        response = requests.get(
            url,
            params={
                "language": "en-US",
                "page": page,
            },
            headers={
                "Authorization": f"Bearer {access_token}",
            },
        )
        data = response.json()
        movies.extend(data["results"])
        if page == data["total_pages"]:
            break
        page += 1
    return movies
