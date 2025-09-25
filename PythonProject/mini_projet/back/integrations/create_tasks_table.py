from ..connexion import *
from ..enums.task_enum import *
categories_table = Table(
    'todolist',
    metadata,
    Column('id',Integer,autoincrement=True,primary_key=True),
    Column('nom',String),
    Column('status',Enum(Tasks))
)
