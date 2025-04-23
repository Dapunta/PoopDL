#--> standard module & library
import json

#--> flask
from flask import Flask, Response, request
from flask_cors import CORS
app = Flask(import_name=__name__)
CORS(app=app)

#--> local module
from python.poop import Poop

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
            poop = Poop()
            poop.execute(url)
            list_file : list = poop.result['data']

            #--> Response condition
            if(len(list_file) != 0): result = {'status':'success', 'message':'', 'data':list_file}
            else: result = {'status':'failed', 'message':'file not found', 'data':[]}

    except Exception as e: result = {'status':'failed', 'message':'i dont know why error in poop app : {}'.format(str(e)), 'data':[]}
    return Response(response=json.dumps(obj=result, sort_keys=False), mimetype='application/json')

#--> Initialization
if __name__ == '__main__':
    app.run(debug=True)

# list_url : list[str] = ['https://dood.cm/f/i37879otxpi', 'https://poop.vin/d/LPxbX8Mn4KZ', 'https://poop.pm/f/t8e12zcx7ra', 'https://poop.pm/f/p6mqkgysdr0', 'https://poop.pm/f/be20crhis8g', 'https://poop.pm/f/WTdgWsSnlnv']
# list_id  : list[str] = ['LPxbX8Mn4KZ', 'ggvl28sr6tuu', 'sjg5d1abyi5e', '6yz2q62slsir', 'JJOXFuOZoJL']