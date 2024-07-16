from fastapi import APIRouter
import os

from src.types import Region
from src.actions.watch import get_regions

watch_router = APIRouter()


@watch_router.get("/watch/regions")
def get_watch_regions() -> list[Region]:
    access_token = os.getenv("TMDB_ACCESS_TOKEN")
    if access_token is None:
        raise ValueError("TMDB_ACCESS_TOKEN environment variable is not set")
    return get_regions(access_token)
