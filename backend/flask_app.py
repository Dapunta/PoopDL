#--> standard module & library
import json, requests

#--> flask
from flask import Flask, Response, request
from flask_cors import CORS
app = Flask(import_name=__name__)
CORS(app=app)

#--> local module
from python.poop_download import PoopDownload

#--> main
@app.route(rule='/')
def stream() -> Response:
    response: dict[str,str] = {
        'status'  : 'success',
        'service' : [
            {
                'method'   : 'POST',
                'endpoint' : 'get_file',
                'url'      : '{}get_file'.format(request.url_root),
                'params'   : 'url',
                'response' : 'status, message, data',
            },
        ],
        'message' : 'hayo mau ngapain?'}
    return Response(response=json.dumps(obj=response, sort_keys=False), mimetype='application/json')

#--> get file
@app.route(rule='/get_file', methods=['POST'])
def getFile() -> Response:

    #--> Set default response
    result : dict[str,str] = {'status':'failed', 'message':'invalid params', 'file':[]}

    try:

        #--> Get params
        data : dict = request.get_json()
        url  : str  = data.get('url')

        if url:

            #--> Get file
            poop = PoopDownload()
            poop.execute(url)
            list_file : list = poop.result['data']

            #--> Response condition
            if(len(list_file) != 0): result = {'status':'success', 'message':'', 'data':list_file}
            else: result = {'status':'failed', 'message':'file not found', 'data':[]}

    except Exception as e: result = {'status':'failed', 'message':'i dont know why error in poop app : {}'.format(str(e)), 'data':[]}
    return Response(response=json.dumps(obj=result, sort_keys=False), mimetype='application/json')

#--> proxy
@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    range_header = request.headers.get('Range', None)

    headers : dict[str,str] = {
        'Referer': 'https://poophd.video-src.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    }

    if range_header:
        headers['Range'] = range_header

    r = requests.get(url, headers=headers, stream=True)

    def generate():
        for chunk in r.iter_content(chunk_size=8192):
            yield chunk

    response_headers = {
        'Content-Type': r.headers.get('Content-Type', 'video/mp4'),
        'Content-Length': r.headers.get('Content-Length'),
        'Accept-Ranges': r.headers.get('Accept-Ranges', 'bytes'),
    }

    if r.status_code == 206:
        response_headers['Content-Range'] = r.headers.get('Content-Range')

    return Response(generate(), status=r.status_code, headers=response_headers)

#--> Initialization
if __name__ == '__main__':
    app.run(debug=True)

# list_url : list[str] = ['https://dood.cm/f/i37879otxpi', 'https://poop.vin/d/LPxbX8Mn4KZ', 'https://poop.pm/f/t8e12zcx7ra', 'https://poop.pm/f/p6mqkgysdr0', 'https://poop.pm/f/be20crhis8g', 'https://poop.pm/f/WTdgWsSnlnv']
# list_id  : list[str] = ['LPxbX8Mn4KZ', 'ggvl28sr6tuu', 'sjg5d1abyi5e', '6yz2q62slsir', 'JJOXFuOZoJL']