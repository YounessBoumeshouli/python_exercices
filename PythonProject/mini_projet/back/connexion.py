from sqlalchemy import Table, MetaData, Integer,Column ,String, ForeignKey,create_engine , Enum , TIMESTAMP
engine = create_engine('postgresql://postgres:12345@localhost:9999/todolist',client_encoding="UTF-8")
from .migrations.create_tasks_table import *
from .migrations.create_user_table import *
metadata = MetaData()


users_table =     create_users_table(Column,metadata,Table,Integer,String)
tasks_table =    create_tasks_table(Column,metadata,Table,Integer,String,TIMESTAMP)
metadata.create_all(engine,checkfirst=True)

def execute(query):
    with engine.begin() as connection:
        results =  connection.execute(query).mappings().fetchall()
        for row in results :
            print(row)
        return results