from fastapi import APIRouter

from src.actions.watch import get_regions
from src.schema import Region

watch_router = APIRouter()


@watch_router.get("/watch/regions")
def get_watch_regions() -> list[Region]:
    return get_regions()
