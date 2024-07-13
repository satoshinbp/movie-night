from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv


BASE_URL = "https://api.themoviedb.org/3/"
app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Movie(BaseModel):
    adult: bool
    backdrop_path: str
    genre_ids: list[int]
    id: int
    original_language: str
    overview: str
    popularity: float
    poster_path: str
    release_date: str
    title: str
    video: bool
    vote_average: float
    vote_count: int
    netflix_regions: list[str]
    runtime: int


class Region(BaseModel):
    iso_3166_1: str
    english_name: str
    native_name: str


def get_watchlist(access_token, account_id):
    url = BASE_URL + f"account/{account_id}/watchlist/movies"
    movies = []
    page = 1
    while True:
        response = requests.get(
            url,
            params={
                "language": "en-US",
                "page": page,
            },
            headers={
                "Authorization": f"Bearer {access_token}",
            },
        )
        data = response.json()
        movies.extend(data["results"])
        if page == data["total_pages"]:
            break
        page += 1
    return movies


def get_provider(access_token, movie_id):
    url = BASE_URL + f"movie/{movie_id}/watch/providers"
    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {access_token}",
        },
    )
    data = response.json()
    return data["results"]


def get_runtime(access_token, movie_id):
    url = BASE_URL + f"movie/{movie_id}"
    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {access_token}",
        },
    )
    data = response.json()
    return data["runtime"]


def get_regions(access_token):
    url = BASE_URL + "watch/providers/regions"
    response = requests.get(
        url,
        params={
            "language": "en-US",
        },
        headers={
            "Authorization": f"Bearer {access_token}",
        },
    )
    data = response.json()
    return data["results"]


@app.get("/{account_id}/watchlist")
def watchlist(account_id: int) -> list[Movie]:
    access_token = os.getenv("TMDB_ACCESS_TOKEN")
    if access_token is None:
        raise ValueError("TMDB_ACCESS_TOKEN environment variable is not set")

    movies = get_watchlist(access_token, account_id)
    regions = get_regions(access_token)

    for movie in movies:
        providers = get_provider(access_token, movie["id"])
        runtime = get_runtime(access_token, movie["id"])
        netflix_regions = []
        for region in regions:
            provider_region = providers.get(region["iso_3166_1"])
            if not provider_region:
                continue

            flatrate = provider_region.get("flatrate")
            if not flatrate:
                continue

            if "Netflix" in [provider["provider_name"] for provider in flatrate]:
                netflix_regions.append(region["iso_3166_1"])

        movie["netflix_regions"] = netflix_regions
        movie["runtime"] = runtime

    return movies


@app.get("/regions")
def regions() -> list[Region]:
    access_token = os.getenv("TMDB_ACCESS_TOKEN")
    if access_token is None:
        raise ValueError("TMDB_ACCESS_TOKEN environment variable is not set")
    regions = get_regions(access_token)
    return regions


if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
