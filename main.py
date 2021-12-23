import json
from fastapi.applications import FastAPI
from database import Heroe
from database import database as conenection
from schemas import HeroSchema, HeroSchemaPydantic

app = FastAPI()


@app.on_event('startup')
def startup():
    if not conenection.is_closed():
        conenection.connect()


@app.on_event('shutdown')
def shutdown():
    if not conenection.is_closed():
        conenection.close()


@app.get("/hero")
async def get():
    heroes = Heroe.select()
    schema = HeroSchema()
    return json.loads(schema.dumps(heroes,many=True).encode('utf-8'))


@app.get("/hero/{pk}")
async def get_object(pk: int):
    hero = Heroe.select().where(Heroe.id == pk).first()
    schema = HeroSchema()
    return json.loads(schema.dumps(hero).encode('utf-8'))


@app.post("/hero")
async def post(heroe: HeroSchemaPydantic):
    hero = Heroe.create(
        alter_ego = heroe.alter_ego,
        real_name = heroe.real_name,
        universe = heroe.universe,
        state = heroe.state
    )
    schema = HeroSchema()
    return json.loads(schema.dumps(hero).encode('utf-8'))
