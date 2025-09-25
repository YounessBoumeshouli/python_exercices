from ..connexion import *
users_table = Table(
    'users',
    metadata,
    Column('id',Integer,autoincrement=True,primary_key=True),
    Column('nom',String),
)
