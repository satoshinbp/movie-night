from src.tmbd.watch import get_tmbd_regions
from ..types import Region


def get_regions(access_token) -> list[Region]:
    return get_tmbd_regions(access_token)
