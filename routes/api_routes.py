from flask import Blueprint, request, jsonify
from services.search_service import search_duckduckgo_web
from services.search_service import search_duckduckgo_video
from services.ai_service import web_ai

api = Blueprint('api', __name__)
@api.route('/api/search/document',methods=['POST'])
def api_search_Document():
    data = request.json
    query = data.get('query')
    urls = search_duckduckgo_web(query)
    if isinstance(urls, dict) and 'error' in urls:
        return jsonify(urls), 500
    if not urls:
        return jsonify({'error': 'No URLs found.'}), 404
#    return jsonify({'url':urls}), 200
    if not query:
        return jsonify({'error': 'Query parameter is required.'}), 400
    ai_res = web_ai(urls,query)
    return jsonify({'resulte' : ai_res['response']}), 200
@api.route('/api/search/video',methods=['POST'])
def api_search_video():
    data = request.json
    query = data.get('query')
    urls = search_duckduckgo_video(query)
#    print(urls)
    if isinstance(urls, dict) and 'error' in urls:
        return jsonify(urls), 500
    if not urls:
        return jsonify({'error': 'No URLs found.'}), 404
#    return jsonify({'url':urls}), 200
    if not query:
        return jsonify({'error': 'Query parameter is required.'}), 400
    ai_res = web_ai(urls,query)
    return jsonify({'resulte' : ai_res['response']}), 200
