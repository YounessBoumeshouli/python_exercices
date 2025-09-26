from enum import Enum
Tasks = Enum('Tasks', [('TODO',"todo"), ('DOING', "doing"), ('DONE', "done")])
Priority  =  Enum('Priority', [('LOW',"low"), ('MEDIUM', "medium"), ('HIGH', "high")])
class tache_enum(Enum) :
    TODO  = "todo",
    DOING  = "doing",
    DONE  = "done",
