import requests 


def web_ai(urls,query):
    try :
        response=requests.get(f"https://dev-pycodz-blackbox.pantheonsite.io/DEvZ44d/deepseek.php?text=I will send you a set of linksin json format, arrange them using the search feature based on the following topic (query) If you don't find a topic, make your own conclusion the urls {urls} the result shuld be in json format")
        response.raise_for_status()  # Raise an error for bad responses
        # Assuming the response is JSON, return the JSON data
        return response.json()  # This will return the JSON content of the response
    except requests.RequestException as e:
        return {"error": f"Request failed: {str(e)}"} 
