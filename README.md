

# Ai_search
```markdown
Ai_search is a Flask-based backend application designed to enhance search results for documents and videos using AI processing. It integrates external search services to refine and improve the relevance of search results.
```
---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [update](#update.md)
---

## 📖 Overview

Ai_search leverages Flask blueprints to provide a modular backend supporting two main search functionalities:

- **Document Search:** Fetches and enhances search results related to documents.
- **Video Search:** Fetches and enhances search results related to videos.

Both endpoints combine search results from DuckDuckGo with AI processing to deliver more accurate and relevant responses.

---

## ✨ Features

- **AI-Enhanced Search:** Merges traditional search results with AI-driven processing for improved accuracy.
- **Modular Architecture:** Built using Flask blueprints, making it easy to extend.
- **Dual Search Functionality:** Separate API endpoints for document and video searches.
- **External API Integration:** Uses duckduckgo-search to query external data sources.

---

## 📥 Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/xbyit/Ai_search.git
    cd Ai_search
    ```

2. **Install dependencies:**

    Ensure Python 3 is installed, then run:
    ```sh
    pip install -r requirements.txt
    ```

    Dependencies in `requirements.txt`:
    ```sh
    Flask==3.0.0
    requests==2.31.0
    duckduckgo-search==4.3
    ```

---

## ⚙️ Configuration

Before running the application, update the configuration settings in `config.py`:
```python
DEBUG: Set to True for development, False for production.
SEARCH_API_URL: URL of the external search engine.
AI_API_URL: URL of the AI processing service.
```

---

## 🚀 Usage

To start the application, run:
```sh
python app.py
```

The server will be available at:
[http://0.0.0.0:5000](http://0.0.0.0:5000)

---

## 📡 API Endpoints

### 🔍 Document Search

- **Endpoint:** `/api/search/document`
- **Method:** `POST`
- **Description:** Accepts a JSON payload with a query string and returns AI-enhanced document search results.

**Request:**
```json
{
  "query": "example search term"
}
```

**Response:**
```json
{
  "result": "AI processed search result"
}
```

### 🎥 Video Search

- **Endpoint:** `/api/search/video`
- **Method:** `POST`
- **Description:** Accepts a JSON payload with a query string and returns AI-enhanced video search results.

**Request:**
```json
{
  "query": "example video search term"
}
```

**Response:**
```json
{
  "result": "AI processed search result"
}
```

For more details, refer to `routes/api_routes.py`.

---

## 📂 Project Structure

```
Ai_search/
├── app.py                # Main application file initializing Flask and registering blueprints
├── config.py             # Application configuration settings
├── routes/
│   └── api_routes.py     # API endpoint definitions
└── services/
    ├── search_service.py # Integration with external search APIs (DuckDuckGo)
    └── ai_service.py     # AI processing of search results
```

---

## 🤝 Contributing

Contributions are welcome! If you find an issue or have an enhancement proposal, please open an issue or submit a pull request.

---

## 📜 License

This project is open source. See the LICENSE file for more details.

---

## 📧 Contact

For questions or further information, contact the maintainer:

- **Telegram:** [https://t.me/XTOOLPYCHAT](https://t.me/XTOOLPYCHAT)

