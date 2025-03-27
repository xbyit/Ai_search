

<\h1 Ai_search>

Ai_search is a Flask-based backend application that enhances search results for documents and videos using AI processing. It integrates external search services to refine and improve the relevance of search results.


---

📌 Table of Contents

📖 Overview

✨ Features

🛠️ Tech Stack

📥 Installation

⚙️ Configuration

🚀 Usage

📡 API Endpoints

📂 Project Structure

🤝 Contributing

📜 License

📧 Contact['📧 Contact']



---

<h1 📖 Overview>

Ai_search leverages Flask blueprints to provide a modular backend supporting two main search functionalities:

Document Search: Fetches and enhances search results related to documents.

Video Search: Fetches and enhances search results related to videos.


Both endpoints combine search results from DuckDuckGo with AI processing to deliver more accurate and relevant responses.


---

<h1 ✨ Features >

✅ AI-Enhanced Search: Merges traditional search results with AI-driven processing for improved accuracy.
✅ Modular Architecture: Built using Flask blueprints, making it easy to extend.
✅ Dual Search Functionality: Separate API endpoints for document and video searches.
✅ External API Integration: Uses duckduckgo-search to query external data sources.

---

<h1 📥 Installation >

<h3 1. Clone the repository: >

git clone https://github.com/xbyit/Ai_search.git
cd Ai_search


<h3 2. Install dependencies:>

Ensure Python 3 is installed, then run:

pip install -r requirements.txt

Dependencies in requirements.txt:

Flask==3.0.0
requests==2.31.0
duckduckgo-search==4.3




---

<h1 ⚙️ Configuration>

Before running the application, update the configuration settings in config.py:

DEBUG: Set to True for development, False for production.

SEARCH_API_URL: URL of the external search engine.

AI_API_URL: URL of the AI processing service.



---

<h1 🚀 Usage>

To start the application, run:

python app.py

The server will be available at:
http://0.0.0.0:5000


---

<h1 📡 API Endpoints>

<h3 🔍 Document Search>

Endpoint: /api/search/document

Method: POST

Description: Accepts a JSON payload with a query string and returns AI-enhanced document search results.


📤 Request:

{
  "query": "example search term"
}

📥 Response:

{
  "result": "AI processed search result"
}

<h3 🎥 Video Search>

Endpoint: /api/search/video

Method: POST

Description: Accepts a JSON payload with a query string and returns AI-enhanced video search results.


📤 Request:

{
  "query": "example video search term"
}

📥 Response:

{
  "result": "AI processed search result"
}

📌 For more details, refer to routes/api_routes.py.


---

<h2 📂 Project Structure>
'''
Ai_search/
├── app.py                # Main application file initializing Flask and registering blueprints
├── config.py             # Application configuration settings
├── routes/
│   └── api_routes.py     # API endpoint definitions
└── services/
    ├── search_service.py # Integration with external search APIs (DuckDuckGo)
    └── ai_service.py     # AI processing of search results

'''
---

<h1 🤝 Contributing >

Contributions are welcome! If you find an issue or have an enhancement proposal, please open an issue or submit a pull request.


---

<h1 📜 License >

This project is open source. See the LICENSE file for more details.


---

<h1 📧 Contact >

For questions or further information, contact the maintainer:

📩 Telegram: https://t.me/XTOOLPYCHAT


---

