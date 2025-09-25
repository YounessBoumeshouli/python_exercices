from ..crud import *
class Taches :
 name_table = "taches_table"
 def __init(self,title,description,status,created_at,modified_at):
     self._id = None
     self.title = title
     self.description = description
     self.status = status
     self.created_at = created_at
     self.modified_at = modified_at
 @property
 def id(self):
    return self.id

 def create(self):
    create(self.name_table, {self.title,self.description,self.status})
 def update(self):
    update(self.name_table, self.id() ,{self.title,self.description,self.status})

 def delete(self):
     delete(self.name_table, self.id())
