from apis.watch import get_tmbd_regions
from schemas.tmdb import Region


def get_regions() -> list[Region]:
    return get_tmbd_regions()
