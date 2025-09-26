from ..enums.task_enum import *

def create_users_table(Column,metadata,Table,Integer,String) :
    users = Table(
        'users',
        metadata,
        Column('id', Integer, autoincrement=True, primary_key=True),
        Column('name', String),
    )
    return users

