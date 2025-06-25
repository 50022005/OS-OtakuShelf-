import requests
import time

BASE_URL = "https://api.jikan.moe/v4"

def search_jikan(query, media_type="anime", retries=3, delay=1):
    """
    Search for anime or manga using Jikan API (MAL wrapper).
    
    Args:
        query (str): The search query (e.g., "Naruto")
        media_type (str): "anime" or "manga"
        retries (int): Number of retry attempts on failure
        delay (int): Seconds to wait between retries

    Returns:
        dict or None: Parsed top result or None if not found
    """
    url = f"{BASE_URL}/{media_type}?q={query}"

    for attempt in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                results = response.json().get("data", [])
                if results:
                    top = results[0]
                    return {
                        "title": top.get("title"),
                        "type": media_type,
                        "chapters_or_episodes": top.get("episodes") if media_type == "anime" else top.get("chapters"),
                        "status": top.get("status"),
                        "score": top.get("score"),
                        "synopsis": top.get("synopsis"),
                        "image_url": top.get("images", {}).get("jpg", {}).get("image_url"),
                        "mal_url": top.get("url")
                    }
                else:
                    print(f"No {media_type} found for '{query}'")
                    return None
            else:
                print(f"Jikan API error {response.status_code}, retrying...")
        except Exception as e:
            print(f"Error: {e}, retrying...")
        time.sleep(delay)

    return None
