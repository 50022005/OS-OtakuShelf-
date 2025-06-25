import requests
import time

API_KEY = "5abeae167d951cbd25d1942c02a1fd51"
BASE_URL = "https://api.themoviedb.org/3"

def search_tmdb(query, media_type="movie", retries=3, delay=1):
    url = f"{BASE_URL}/search/{media_type}"
    params = {"query": query, "api_key": API_KEY}
    
    for attempt in range(retries):
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json().get("results", [])
                if data:
                    top = data[0]
                    return {
                        "title": top.get("title") or top.get("name"),
                        "type": media_type,
                        "overview": top.get("overview"),
                        "release_date": top.get("release_date") or top.get("first_air_date"),
                        "rating": top.get("vote_average"),
                        "image_url": f"https://image.tmdb.org/t/p/w500{top.get('poster_path')}" if top.get("poster_path") else None
                    }
                else:
                    return None
            else:
                print(f"TMDB error {response.status_code}, retrying...")
        except Exception as e:
            print(f"Error: {e}, retrying...")
        time.sleep(delay)
    return None
