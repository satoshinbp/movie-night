from fastapi import APIRouter, HTTPException

from actions.account import (
    get_watchlist_with_details,
    add_movie_to_watchlist,
    remove_movie_from_watchlist,
)
from schemas.general import Movie, Status

account_router = APIRouter()


@account_router.get("/accounts/{account_id}/watchlist")
def get_account_watchlist(account_id: int) -> list[Movie]:
    try:
        return get_watchlist_with_details(account_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@account_router.post("/accounts/{account_id}/watchlist/add/{movie_id}")
def add_to_account_watchlist(account_id: int, movie_id: int) -> Status:
    try:
        status = add_movie_to_watchlist(account_id, movie_id)
        if not status["success"]:
            raise RuntimeError(status["message"])
        return status
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@account_router.post("/accounts/{account_id}/watchlist/remove/{movie_id}")
def remove_from_account_watchlist(account_id: int, movie_id: int) -> Status:
    try:
        status = remove_movie_from_watchlist(account_id, movie_id)
        if not status["success"]:
            raise RuntimeError(status["message"])
        return status
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
