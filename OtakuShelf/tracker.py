import json
import os
from utility.api_handler import fetch_media_metadata
from utils import load_data, save_data

def view_library():
    print("\n\U0001F4DA Your Media Library")
    all_data = load_data()
    if not all_data:
        print("No entries found.")
        return
    for i, item in enumerate(all_data, start=1):
        print(f"{i}. {item['type'].capitalize()}: {item['title']}\n   My Status: {item.get('My_status', 'N/A')}\n   My Rating: {item.get('My_rating', 'N/A')}\n   Genres: {', '.join(item.get('genres', [])) if item.get('genres') else 'N/A'}\n   Official Status: {item.get('status', 'N/A')}\n   Rating: {item.get('rating')or item.get('score')or 'N/A'}\n  ")

def filter_result(data, genre=None, status=None):
    if not data:
        return None
    if genre and genre not in str(data).lower():
        return None
    if status and status not in (data.get("status", "") or "").lower():
        return None
    return data

def add_media(media_type, title, genre=None, status=None):
    data = fetch_media_metadata(title, media_type, genre, status)
    if not data:
        print("\u274C No results found.")
        return

    print(f"\n\U0001F389 Found {media_type.upper()}: {data['title']}")
    synopsis = data.get("synopsis") or data.get("overview") or data.get("description") or ""
    print("\U0001F4C4 Synopsis:", synopsis[:200], "...")
    print("Release Date:", data.get("release_date") or data.get("first_air_date") or "N/A")
    print("Rating:", data.get("rating") or data.get("score") or "N/A")
   #print("Genres:", ", ".join(data.get("genres", [])))
    confirm = input("Add to your tracker? (y/n): ").lower()
    if confirm == "y":
        status = input("Status (Watching/Reading/Completed/Plan-to): ").capitalize()
        rating = get_rating()
        data["My_status"] = status
        data["My_rating"] = rating
        all_data = load_data()
        all_data.append(data)
        save_data(all_data)
        print("\u2705 Saved successfully.")
    else:
        print("\u274C Canceled.")

def update_media():
    all_data = load_data()
    if not all_data:
        print("No entries to update.")
        return

    view_library()
    choice = input("Enter number to update: ")
    if not choice.isdigit() or int(choice) > len(all_data):
        print("\u274C Invalid choice.")
        return

    index = int(choice) - 1
    item = all_data[index]
    print(f"Editing {item['title']} ({item['type']})")

    new_title = input("New title (Enter to keep current): ").strip()
    if new_title:
        item["title"] = new_title

    new_status = input("New status (Enter to keep current): ").strip()
    if new_status:
        item["My_status"] = new_status
    new_rating = get_rating()
    item["My_rating"] = new_rating
    all_data[index] = item
    save_data(all_data)
    print("\u2705 Updated.")

def delete_media():
    all_data = load_data()
    if not all_data:
        print("No entries to delete.")
        return

    view_library()
    choice = input("Enter number to delete: ")
    if not choice.isdigit() or int(choice) > len(all_data):
        print("\u274C Invalid choice.")
        return

    index = int(choice) - 1
    deleted = all_data.pop(index)
    save_data(all_data)
    print(f"\U0001F5D1️ Deleted: {deleted['title']}")

def search_by_genre(genre):
    data = load_data()
    results = [item for item in data if genre.lower() in (g.lower() for g in item['genres'])]
    if not results:
        print("❌ No entries found for this genre.")
        return
    for item in results:
        print(f"\n- {item['title']} ({item['type']}) - {item['status']} - ⭐ {item['rating']}")
def search_by_type(media_type):
    data = load_data()
    results = [item for item in data if item['type'].lower() == media_type.lower()]
    for item in results:
        print(f"\n- {item['title']} ({item['status']})")
def get_rating():
    while True:
        try:
            rating = float(input("Rating (0-10): "))
            if 0 <= rating <= 10:
                return rating
            else:
                print("❌ Invalid rating. Please enter a value between 0 and 10.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")