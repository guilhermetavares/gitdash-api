import os
import requests
import json

from sanic import Sanic
from sanic.response import json

app = Sanic('app')

@app.route("/", methods=["POST", "GET"])
async def test(request):
    return json({'hello': 'word'})

app.run(host='0.0.0.0', port=int(os.environ['PORT']))
