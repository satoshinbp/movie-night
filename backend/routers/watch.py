from fastapi import APIRouter

from actions.watch import get_regions
from schemas.general import Region

watch_router = APIRouter()


@watch_router.get("/watch/regions")
def get_watch_regions() -> list[Region]:
    return get_regions()
