
from pydantic import BaseModel
from marshmallow_peewee import ModelSchema, fields
from marshmallow import fields


class HeroSchemaPydantic(BaseModel):
    alter_ego: str
    real_name: str
    universe: str
    state: str

class HeroSchema(ModelSchema):
    alter_ego = fields.Str()
    real_name = fields.Str()
    universe = fields.Str()
    state = fields.Str()

