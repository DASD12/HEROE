#dadabase
from fastapi.exceptions import HTTPException
from pydantic.utils import truncate
from database import database as conenection
from database import Heroe
from schemas import heroeModel

from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()



@app.on_event('startup')
def startup():
    if not conenection.is_closed():
        conenection.connect()
    
    # conenection.create_tables([heroes])

@app.on_event('shutdown')
def shutdown():
    if not conenection.is_closed():
        conenection.close()

@app.get("/")    #recibir datos del servidor
def home():
    return  {"Hello": "Worldssss"}

@app.post("/heroe/new") #enviar informacion al servidor
async def create_Heroe(heroe: heroeModel): #si hay (...) significa que el parametro es obligatorio
    heroe = Heroe.create(
        alter_ego = Heroe.alter_ego,
        real_name = Heroe.real_name,
        universe = Heroe.universe,
        state = Heroe.state
    )

@app.get("/heroe/mostrar/{nombre}") #traer informacion
async def create_Heroe(nombre):
    heroe = Heroe.select().where(Heroe.alter_ego == nombre).firs()

    if heroe:
        return Heroe
    else:
        return HTTPException(404, 'ususario no encontrado')

@app.delete("/heroe/editar/{nombre_heroe}")     #put es para actualizar
async def create_eliminar(nombre_heroe):
    user = Heroe.select().where(Heroe.alter_ego == nombre_heroe).first()

    if user:
        user.delete_instance()
        return True
    else:
        return HTTPException(404, 'ususario no encontrado')
