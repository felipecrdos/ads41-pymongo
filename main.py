from documents import Aluno
from connection import Connction

aluno = Aluno()

#INSERT-----------------------------------------------------------------
aluno.save({"nome":"Felipe Cardoso", "email":"felipecrdos@gmail.com", "matricula":1807017})
aluno.save({"nome":"Fulano", "email":"fulano@gmail.com", "matricula":181510})
aluno.save({"nome":"Ciclano", "email":"ciclano@gmail.com", "matricula":181120, "idade": 20})
aluno.save({"nome":"Carolina", "email":"carolina@gmail.com", "matricula":161325, "idade": 17})

# READ-------------------------------------------------------------------
# listar dodos documentos com todos os campos
aluno.read()

# listar o aluno com matrícula igual a 1816017
aluno.read({"matricula":1807017})

# listar apenas alunos que tenham a idade maio que 18
aluno.read({"idade":{"$gt":18}})

# listar todos os alunos que tenham email, mas não mostrar o campo _id
aluno.read({"email":{"$exists": True}}, {"_id":0})
# UPDATE------------------------------------------------------------------
# atualizar o nome e add idade para o aluno com matrícula 18116017
aluno.update({"matricula":1807017}, {"$set":{"nome":"Felipe Cardozo", "idade":33}})

# DELETE------------------------------------------------------------------
# deletar o aluno com matrícula 181120
aluno.delete({"matricula":181120})

# remover todos os alunos que não possuem email ou tem idade menor que 18 anos
aluno.delete({"$or":[{"email":{"$exists": False}}, {"idade":{"$lt":18}}]})


