from duckduckgo_search import DDGS
query = 'python'
urls = DDGS().videos(query)
print(urls)  # طباعة النتائج للتحقق منها

