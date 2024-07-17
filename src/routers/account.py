from fastapi import APIRouter

from src.actions.account import get_watchlist
from src.schema import Movie

account_router = APIRouter()


@account_router.get("/accounts/{account_id}/watchlist")
def get_account_watchlist(account_id: int) -> list[Movie]:
    return get_watchlist(account_id)
