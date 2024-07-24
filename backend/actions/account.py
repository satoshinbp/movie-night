from apis.account import get_tmbd_watchlist, add_to_tmbd_watchlist
from apis.movie import get_tmbd_provider, get_tmbd_runtime
from apis.watch import get_tmbd_regions
from schemas.tmdb import Movie, Region
from schemas.general import Status


def get_full_watchlist(account_id: int) -> list[Movie]:
    movies = []
    page = 1
    while True:
        data = get_tmbd_watchlist(account_id, page)
        movies.extend(data["results"])
        if page == data["total_pages"]:
            break
        page += 1
    return movies


def get_netflix_regions(movie_id: int, regions: list[Region]) -> list[str]:
    providers = get_tmbd_provider(movie_id)
    netflix_regions = []
    for region in regions:
        provider_region = providers.get(region["iso_3166_1"])
        if not provider_region:
            continue

        flatrate = provider_region.get("flatrate")
        if not flatrate:
            continue

        if "Netflix" in [provider["provider_name"] for provider in flatrate]:
            netflix_regions.append(region["iso_3166_1"])
    return netflix_regions


def get_watchlist_with_details(account_id: int) -> list[Movie]:
    movies = get_full_watchlist(account_id)
    regions = get_tmbd_regions()
    for movie in movies:
        movie["netflix_regions"] = get_netflix_regions(movie["id"], regions)
        movie["runtime"] = get_tmbd_runtime(movie["id"])
    return movies


def add_to_watchlist(account_id: int, movie_id: int) -> Status:
    data = add_to_tmbd_watchlist(account_id, "movie", movie_id, True)
    return {"success": data["success"], "message": data["status_message"]}


def remove_from_watchlist(account_id: int, movie_id: int) -> Status:
    data = add_to_tmbd_watchlist(account_id, "movie", movie_id, False)
    return {"success": data["success"], "message": data["status_message"]}
