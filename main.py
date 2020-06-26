from peewee import *

db = SqliteDatabase('carstore.db')

class Base(Model):
    class Meta:
        database = db

class Cars(Base):
    id = PrimaryKeyField(null=False)
    brand = CharField()
    model = CharField()
    year = IntegerField()
    engine_power = IntegerField()
    auto_gearbox = BooleanField()
    condition = IntegerField()
    features = TextField()
    price = IntegerField()
    class Meta:
        db_table = "cars"

class Clients(Base):
    id = PrimaryKeyField(null=False)
    name = CharField()
    address = CharField()
    brand = CharField()
    model = CharField()
    year = IntegerField()
    condition = IntegerField()
    price = IntegerField()
    class Meta:
        db_table = "cars"
