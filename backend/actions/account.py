from apis.account import get_watchlist_movies, add_to_watchlist
from apis.movie import get_movie_watch_provider, get_movie_details
from apis.watch import get_watch_provider_regions
from schemas.tmdb import Movie, Region
from schemas.general import Status


def get_full_watchlist(account_id: int) -> list[Movie]:
    movies = []
    page = 1
    while True:
        data = get_watchlist_movies(account_id, page)
        movies.extend(data["results"])
        if page == data["total_pages"]:
            break
        page += 1
    return movies


def get_provider_regions(
    provider_name: str, movie_id: int, regions: list[Region]
) -> list[str]:
    providers = get_movie_watch_provider(movie_id)["results"]
    provider_regions = []
    for region in regions:
        provider_region = providers.get(region["iso_3166_1"])
        if not provider_region:
            continue
        flatrate = provider_region.get("flatrate")
        if not flatrate:
            continue
        if provider_name in [provider["provider_name"] for provider in flatrate]:
            provider_regions.append(region["iso_3166_1"])
    return provider_regions


def get_watchlist_with_details(account_id: int) -> list[Movie]:
    movies = get_full_watchlist(account_id)
    regions = get_watch_provider_regions()["results"]
    for movie in movies:
        movie["netflix_regions"] = get_provider_regions("Netflix", movie["id"], regions)
        movie["runtime"] = get_movie_details(movie["id"])["runtime"]
    return movies


def add_movie_to_watchlist(account_id: int, movie_id: int) -> Status:
    data = add_to_watchlist(account_id, "movie", movie_id, True)
    return {"success": data["success"], "message": data["status_message"]}


def remove_movie_from_watchlist(account_id: int, movie_id: int) -> Status:
    data = add_to_watchlist(account_id, "movie", movie_id, False)
    return {"success": data["success"], "message": data["status_message"]}
