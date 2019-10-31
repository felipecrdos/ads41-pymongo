from connection import Connction

class Aluno():
    def __init__(self):
        self.connection = Connction("curso","aluno")
    
    def save(self, doc):
        self.connection.save(doc)
    
    def read(self, filterr=None, projection=None):
        self.connection.read(filterr, projection)
    
    def update(self, filterr, fields):
        self.connection.update(filterr, fields)
    
    def delete(self, filterr):
        self.connection.delete(filterr)


