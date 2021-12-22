
from peewee import Model

class heroeModel(Model):
    alter_ego: str
    real_name: str
    universe: str
    state: str
