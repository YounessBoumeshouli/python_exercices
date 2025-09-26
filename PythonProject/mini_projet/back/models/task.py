from ..crud import *
from ..connexion import *
class Task:
 def __init__(self,title,description,deadline,start,priority = None,created_at = None,modified_at = None,id = None,status = None):
     self._id = id
     self.title = title
     self.description = description
     self.status = status
     self.start = start
     self.deadline = deadline
     self.priority = priority
     self.created_at = created_at
     self.modified_at = modified_at
 @property
 def id(self):
    return self.id

 def create(self,name_table):
     data = [{'title': self.title, 'description':self.description, 'start': self.start,'deadline': self.deadline}]
     query = create(name_table, data)
     execute(query)
 def update(self,name_table):
     execute(update(name_table, self.id() ,{self.title,self.description,self.status}))

 def delete(self,name_table):
     execute(delete(name_table, self.id()))
