import os

BASE_URL = os.getenv("BASE_URL")

TMDB_ACCESS_TOKEN = os.getenv("TMDB_ACCESS_TOKEN")

GET_REQ_HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {TMDB_ACCESS_TOKEN}",
}

POST_REQ_HEADERS = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": f"Bearer {TMDB_ACCESS_TOKEN}",
}

LANGUAGE = "en-US"
