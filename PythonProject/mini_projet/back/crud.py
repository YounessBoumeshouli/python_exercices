from ..back.connexion import *

def create(name_table , data):
     print(data)
     return  name_table.insert().values(data)

def update(name_table , id,data):
      return  name_table.update().values(data).where(name_table.c.id == id)

def delete(name_table , id):
     return  name_table.delete().where(name_table.c.id == id)
def select(name_table):
     print("dd");
     return execute(name_table.select())
