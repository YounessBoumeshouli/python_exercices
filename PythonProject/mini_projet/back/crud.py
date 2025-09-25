from connexion import engine
def execute_query(query):
    with engine as connection:
        connection.execute(query)
def create(name_table , data):

      query =  name_table.insert().values(data)
      execute_query(query)
def update(name_table , id,data):
      query =  name_table.update().values(data).where(name_table.c.id == id)
      execute_query(query)


def delete(name_table , id):
     query =  name_table.delete().where(name_table.c.id == id)
     execute_query(query)
