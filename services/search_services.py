
from duckduckgo_search import DDGS

def search_duckduckgo(query):
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=10)
            urls = [res['href'] for res in results]
        return urls
    except Exception as e:
        return {"error": str(e)}
