from sqlalchemy.orm import Session
from sanic import Sanic, json
from myapi.models.Person import Person

app = Sanic.get_app()

# @app.get("/people")
# async def show_all_people(request):
#     pass

@app.post("/people")
async def add_person(request):
    session: Session = request.ctx.session
    async with session.begin():
        person = Person(name="Test User")
        session.add_all([person])
    return json(person.to_dict())

