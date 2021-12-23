from peewee import *
from peewee import MySQLDatabase, Model, CharField

database = MySQLDatabase(
    'test_umh',
    user='test',
    password='123',
    host= 'localhost', port= 3306

)

class Heroe(Model):
    alter_ego = CharField(max_length=50)
    real_name = CharField(max_length=50)
    universe = CharField(max_length=50)
    state = CharField(max_length=50)

    def __str__(self):
        return self.alter_ego

    class Meta:
        database = database
        table_name ='heroes'