
from ..enums.task_enum import *
from ..enums.priority_enum import *
from sqlalchemy import Enum as SqlEnum

# title,description,deadline,start,priority,created_at = None,modified_at = None,id = None,status = None
def create_tasks_table(Column,metadata,Table,Integer,String,TIMESTAMP) :
    tasks_table = Table(
        'tasks',
        metadata,
        Column('id', Integer, autoincrement=True, primary_key=True),
        Column('title', String),
        Column('description', String),
        Column('deadline', TIMESTAMP),
        Column('start', TIMESTAMP),
        Column('priority',SqlEnum(Priority, name = "priority_enum") ,  default = Priority.LOW),
        Column('status', SqlEnum(Tasks , name = "task_enum") , default = Tasks.TODO),

        Column('created_at', TIMESTAMP),
        Column('modified_at', TIMESTAMP),
        extend_existing=True
    )
    return tasks_table
