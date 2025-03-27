
---

Ai_search

Ai_search is a Flask-based Python application that provides AI-enhanced search functionality. It integrates external search APIs with an AI processing layer to deliver enriched document and video search results.

Table of Contents

Features

Getting Started

Prerequisites

Installation

Configuration

Running the Application


API Endpoints

Document Search

Video Search


Project Structure

Contributing


Contact


Features

Document Search Endpoint: Processes search queries for documents.

Video Search Endpoint: Processes search queries for videos.

AI-Enhanced Responses: Integrates external search results with AI processing to deliver refined results.

Modular Design: Built using Flask blueprints and service layers for ease of maintenance and extensibility.


Getting Started

Prerequisites

Python 3.x

pip (Python package installer)

Internet connection for API calls


Installation

1. Clone the repository:

git clone https://github.com/xbyit/Ai_search.git
cd Ai_search


2. Install required dependencies:

If a requirements.txt file is available, run:

pip install -r requirements.txt

Otherwise, ensure that at minimum Flask is installed:

pip install Flask



Configuration

The application settings are managed in the config.py file. Update the configuration values as needed:

DEBUG: Set to True for development or False for production.

SEARCH_API_URL: URL endpoint for the external search API.

AI_API_URL: URL endpoint for the AI processing service.


Refer to config.py for the current configuration.

Running the Application

Run the application using the following command:

python app.py

The server will start on http://0.0.0.0:5000.

API Endpoints

Document Search

Endpoint: /api/search/Document

Method: POST

Description: Submits a search query to fetch document-related results. The query is processed via the external search API and refined using an AI service.

Request Payload Example:

{
  "query": "your search term"
}

Response Example:

{
  "resulte": "AI processed response based on search results"
}


Video Search

Endpoint: /api/search/video

Method: POST

Description: Submits a search query to fetch video-related results. Similar to document search, results are enhanced using the AI service.

Request Payload Example:

{
  "query": "your video search term"
}

Response Example:

{
  "resulte": "AI processed response based on video search results"
}


Refer to api_routes.py for detailed endpoint implementation.

Project Structure

Ai_search/
├── app.py                # Main application file that initializes Flask and registers blueprints
├── config.py             # Configuration settings for API endpoints and debugging options
├── routes/
│   └── api_routes.py     # API route definitions for document and video search
└── services/
    ├── search_service.py # Service functions to interface with external search APIs
    └── ai_service.py     # Service functions to handle AI processing of search results

Contributing

Contributions are welcome! If you have suggestions for improvements or encounter issues, please open an issue or submit a pull request.

License

This project is open-source. Please refer to the LICENSE file for more details.

Contact

For additional information or inquiries, please contact the project maintainer at [https://t.me/XTOOLPYCHAT].

