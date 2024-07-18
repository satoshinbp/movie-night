from apis.account import get_tmbd_watchlist
from apis.movie import get_tmbd_provider, get_tmbd_runtime
from apis.watch import get_tmbd_regions
from schemas.tmdb import Movie


def get_watchlist(account_id: int) -> list[Movie]:
    movies = get_tmbd_watchlist(account_id)
    regions = get_tmbd_regions()

    for movie in movies:
        providers = get_tmbd_provider(movie["id"])
        runtime = get_tmbd_runtime(movie["id"])
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

        movie["netflix_regions"] = netflix_regions
        movie["runtime"] = runtime

    return movies
