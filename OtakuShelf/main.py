from tracker import *

def show_menu():
    print("\n===============🎮 OtakuShelf================")
    print("1. Add Media (Auto-Fetch Metadata)")
    print("2. Add Media (Manual Entry)")
    print("3. View All")
    print("4. Search by Type")
    print("5. Search by Genre")
    print("6. Update Entry")
    print("7. Delete Entry")
    print("8. Exit")

def get_manual_entry():
    title = input("Title: ")
    media_type = input("Type (anime/manga/movie/tv/book): ").lower()
    status = input("Status (Watching/Reading/Completed/Plan-to): ").capitalize()
    rating = float(input("Rating (0-10): "))
    if rating < 0 or rating > 10:
        print("❌ Invalid rating. Please enter a value between 0 and 10.")
        return get_manual_entry()
    genres = input("Genres (comma separated): ").split(",")
    if status == "Completed":
        progress = "Finished"
    elif status == "Plan-to":
        progress = "0"
    else:
        progress = input("Progress (e.g. 12 / 24): ")
    return {
        "title": title,
        "type": media_type,
        "My status": status,
        "My rating": rating,
        "genres": [g.strip() for g in genres],
        "progress": progress
    }

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("\n➡️ Add using online metadata")
            media_type = input("Type (anime/manga/movie/tv/book): ").strip().lower()
            title = input("Enter title: ").strip()
            genre = input("Optional genre filter (press Enter to skip): ").strip().lower()
            status = input("Optional status filter (press Enter to skip): ").strip().lower()
            add_media(media_type, title, genre, status)

        elif choice == "2":
            print("\n➡️ Add manually")
            entry = get_manual_entry()
            data = load_data()
            data.append(entry)
            save_data(data)
            print("✅ Manually added.")

        elif choice == "3":
            view_library()

        elif choice == "4":
            media_type = input("Enter media type to search: ").strip().lower()
            search_by_type(media_type)

        elif choice == "5":
            genre = input("Enter genre to search: ").strip().lower()
            search_by_genre(genre)

        elif choice == "6":
            update_media()

        elif choice == "7":
            delete_media()

        elif choice == "8":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option. Please select from 1–8.")

if __name__ == "__main__":
    main()
