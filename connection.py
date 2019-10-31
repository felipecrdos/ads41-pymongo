from pymongo import MongoClient
from pprint import pprint

class Connction():
    def __init__(self, database:str, collection:str):
        try:
            # Conectando ao mongodb
            self.client = MongoClient(host="localhost", port=27017)

            # Obtendo a base de dados que esta no mongodb
            self.db = self.client[database]

            # Obtendo a coleção da base de dados faculdade
            self.coll = self.db[collection]
        except Exception as e:
            print(f'Erro ao conectar no banco mongodb: {e}')

    # Salvar documentos
    def save(self, doc):
        try:
            id = self.coll.insert_one(doc).inserted_id
            print(f'id: {id}')
        except Exception as e:
            print(f'Erro ao inserir documento: {e}')
            print(f'Documento: {doc}')

    # Listar documentos
    def read(self, filterr=None, projection=None):
        try:
            for doc in self.coll.find(filterr, projection):
                pprint(doc)
            
        except Exception as e:
            print(f'Erro ao ler docs: {e}')
            print(f'docs: {doc}')
    
    # Atualizar documento(s)
    def update(self, filterr, fields):
        try:
            self.coll.update_many(filterr, fields)
        except Exception as e:
            print(f'Erro ao atualizar doc: {e}')
            print(f'doc: {filterr}')

    # Deletando documento(s)
    def delete(self, filterr):
        try:
            self.coll.delete_many(filterr)
        except Exception as e:
            print(f'Erro ao deletar doc: {e}')
            print(f'doc: {filterr}')