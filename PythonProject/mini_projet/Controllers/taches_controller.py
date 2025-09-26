from ..back.models.task import *
from ..back.models.todolist import *
from ..back.connexion import *


def selectTasks() :
    return select(tasks_table)


class taskController :
    def addTask(data):
        task = Task(data["title"],data["description"],data["start"],data["deadline"])
        task.create(tasks_table)
