from duckduckgo_search import DDGS
def search_duckduckgo_web(query):
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=10)
            urls = [res['href'] for res in results]
        return urls
    except Exception as e:
        return {"error": str(e)}
def search_duckduckgo_video(query):
    try:
        with DDGS() as ddgs:
            results = ddgs.videos(query, max_results=5) 
            urls = [res['content'] for res in results if 'content' in res]
        return urls
    except Exception as e:
        return {"error": str(e)}

