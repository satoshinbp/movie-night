from fastapi import APIRouter
import os

from src.types import Movie
from src.actions.account import get_watchlist

account_router = APIRouter()


@account_router.get("/accounts/{account_id}/watchlist")
def get_account_watchlist(account_id: int) -> list[Movie]:
    access_token = os.getenv("TMDB_ACCESS_TOKEN")
    if access_token is None:
        raise ValueError("TMDB_ACCESS_TOKEN environment variable is not set")
    return get_watchlist(account_id, access_token)
