from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Me_Info, Enterprise_Info, SessionLocal

session = SessionLocal()

"""
while True:
    p = []
    for c in range(0,4):
        perguntas = str(input('Digite suas perguntas: '))
        p.append(perguntas)
    resposta = str(input('Digite uma resposta para as peguntas: '))
    

    conhecimento = Enterprise_Info(
        question=p,
        response=resposta
        )
"""

dados_me = [
    {

    }
]

for item in dados_me:
    resp = Me_Info(question=item['perguntas'],response=item['resposta'])

    session.add(resp)
    session.commit()

print('Banco de dados atualizado com sucesso')

#Código para deletar conhecimentos
"""
item = session.query(Knowledge).filter(Knowledge.id == 2).first()
session.delete(item)
session.commit()
"""
