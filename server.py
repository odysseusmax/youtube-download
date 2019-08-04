from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS

import json as js

from youtube.getResponse import GetDetails

app = Sanic()
CORS(app)

@app.route("/api/getyt", methods=['POST', 'OPTIONS'])
async def getyt(request):
    response = {}
    if(request.method == "POST"):
        body = request.json
        url = body.get('url')
        #url = request.form.get('url')
        response = await GetDetails(url).get()
    return json(response)




if __name__ == "__main__":
    app.run()
