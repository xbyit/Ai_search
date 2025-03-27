import requests
from config import Config

def web_ai(urls):
    try:
        json_payload = {'urls': urls}
        ai_response = requests.post(Config.AI_API_URL, json=json_payload, timeout=10)
        ai_response.raise_for_status()
        if "application/json" in ai_response.headers.get("Content-Type", ""):
            return ai_response.json(), None
        return None, "AI response is not in JSON format."
    except requests.RequestException as e:
        return None, f"AI request failed: {str(e)}"
