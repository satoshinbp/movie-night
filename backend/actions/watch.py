from apis.watch import get_watch_provider_regions
from schemas.tmdb import Region


def get_regions() -> list[Region]:
    return get_watch_provider_regions()["results"]
