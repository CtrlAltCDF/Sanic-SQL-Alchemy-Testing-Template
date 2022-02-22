from sanic import Sanic, json

def zoom(testing=False):
    app = Sanic("GoFast")

    @app.before_server_start
    def before_we_lift_off(app, loop):
        if testing:
            print("watchout we are in testing mode")


    @app.get("/health_check")
    async def health_check(request):
        return json({"health": "ok"})

    return app