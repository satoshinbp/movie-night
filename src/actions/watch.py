from tmbd.watch import get_tmbd_regions
from schema import Region


def get_regions() -> list[Region]:
    return get_tmbd_regions()
