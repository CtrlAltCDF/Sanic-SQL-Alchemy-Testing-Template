from sanic.response import text


def load_routes(app):
    @app.get("/")
    async def helloWorld(request):
        return text("Awe!")