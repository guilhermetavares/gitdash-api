import os
import json

from sanic import Sanic
from sanic.response import json
from sanic.request import RequestParameters

from client import GithubClient

app = Sanic('app')

@app.route("/", methods=["POST", "GET"])
async def hello(request):
    return json({'hello': 'word'})


@app.route("/pulls/<org>/<project>", methods=["POST", "GET"])
async def pr_api(request, org, project):
    return json(GithubClient().pulls(org, project))

app.run(host='0.0.0.0', port=int(os.environ['PORT']))
