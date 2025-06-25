import requests
import time

def search_books(query, retries=3, delay=1):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
    
    for attempt in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                items = response.json().get("items", [])
                if items:
                    top = items[0]["volumeInfo"]
                    return {
                        "title": top.get("title"),
                        "authors": top.get("authors", []),
                        "published_date": top.get("publishedDate"),
                        "description": top.get("description"),
                        "page_count": top.get("pageCount"),
                        "thumbnail": top.get("imageLinks", {}).get("thumbnail"),
                        "info_link": top.get("infoLink")
                    }
                else:
                    return None
            else:
                print(f"Google Books error {response.status_code}, retrying...")
        except Exception as e:
            print(f"Error: {e}, retrying...")
        time.sleep(delay)
    return None
