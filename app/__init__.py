from sanic import Sanic
from sanic.response import json


def generate_app():
    app = Sanic("exampleApp")

    @app.route("/")
    async def hello_world(request):
        return json({"hello": "world"})

    @app.before_server_start
    async def setup(app, loop):
        print(f"app mode: {app.state.mode}")
    
    return app