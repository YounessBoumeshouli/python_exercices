from ..crud import *

class Todolist :
 name_table = "todolist"

 def __init__(self, title, status, created_at, modified_at):
     self._id = None
     self.title = title
     self.status = status
     self.created_at = created_at
     self.modified_at = modified_at

 @property
 def id(self):
     return self._id

 def create(self):
     create(self.name_table, {self.title, self.status})

 def update(self):
     update(self.name_table, self.id(), {self.title, self.status})

 def delete(self):
     delete(self.name_table, self.id())