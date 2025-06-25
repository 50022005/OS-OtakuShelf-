from api_wrappers.jikan_api import search_jikan
from api_wrappers.tmdb_api import search_tmdb
from api_wrappers.google_books import search_books
from .media_types import MEDIA_CATEGORIES

def fetch_media_metadata(title, media_type, genre=None, status=None):
    if media_type == "anime":
        data = search_jikan(title, "anime")
    elif media_type == "manga":
        data = search_jikan(title, "manga")
    elif media_type == "movie":
        data = search_tmdb(title, "movie")
    elif media_type == "tv":
        data = search_tmdb(title, "tv")
    elif media_type == "book":
        data = search_books(title)
    else:
        print("❌ Unsupported media type.")
        return None

    return filter_result(data, genre, status)
def filter_result(data, genre=None, status=None):
    if not data:
        return None
    if genre and genre not in str(data).lower():
        return None
    if status and status not in (data.get("status", "") or "").lower():
        return None
    return data
