# OS-OtakuShelf-
# 🎮 All-in-One Media Tracker & Recommender

Track what you watch, read, and love — all in one place.

A personal CLI-based tracker (Level 1) for:
- 📺 Anime
- 📖 Manga & Manhwa
- 🎬 Movies
- 📺 TV Series
- 📘 Books

> 🚀 This is the first version of a long-term project that will eventually evolve into a full **web-based** and **mobile-friendly** media management and recommendation platform.

---

## 📦 Features (CLI Version)
- ✅ Add a media entry manually
- 📄 View all your tracked content
- 🔍 Search by media type or title
- 🗑️ Delete entries
- 💾 Save & load your list from JSON

---

## 🗂️ Folder Structure

media_tracker/
├── data/ # JSON file for storing entries
│ └── media.json
├── media_types/ # Future expansion by content type
│ ├── anime.py
│ ├── manga.py
│ └── ...
├── tracker/
│ └── manager.py # Core add/view/delete/search logic
├── utils.py # Save/load helpers
└── main.py # CLI interface entry point


---

## 🧪 How to Run

```bash
git clone https://github.com/50022005/OS-OtakuShelf.git
cd OS-OtakuShelf
python main.py

```
🧠 Planned Features
🎯 Level 2 – API Integration
Fetch live anime data from Jikan API

Fetch movie/TV metadata from TMDB API

Pull book info using Google Books API

🌐 Level 3 – Flask Web App
Web dashboard with filters and search

Database support with SQLite/PostgreSQL

User login and saved lists

💡 Level 4 – Recommendation Engine
AI-based recommendations by genre, tags, and ratings

Content-based and collaborative filtering

Show similar titles across types (e.g., manga <=> anime)

📱 Level 5 – React / Mobile App
Responsive web frontend using React

Optional mobile version using React Native or Flutter

🛠 Tech Stack
Area	Tools Used
CLI App	Python
Data Storage	JSON (Level 1), SQLite (Level 3)
Web Framework	Flask (Level 3+)
Frontend	React (Level 4)
APIs	Jikan, TMDB, Google Books
ML (Recs)	pandas, sklearn (Level 4)

💻 Demo (Coming Soon)
A live demo will be deployed in future milestones using:

Backend: Render

Frontend: Vercel

🙌 Contributing
This is a solo learning project.

📚 License
IDK.

👨‍💻 Author
Muhammad Hashim Rahim
FAST NUCES Islamabad | BSCS '27
Built with ❤️ and way too much coffee.
