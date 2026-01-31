from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Knowledge

engine = create_engine("sqlite:///dados.db")
Session = sessionmaker(bind=engine)
session = Session()

#Código para deletar conhecimentos
"""
item = session.query(Knowledge).filter(Knowledge.id == 2).first()
session.delete(item)
session.commit()
"""

pergunta = ""
while pergunta != "exit":
    pergunta = str(input("Pergunta: "))
    if pergunta == "exit":
        break
    resposta = str(input("Resposta: "))

    conhecimento = Knowledge(pergunta, resposta)
    session.add(conhecimento)
session.commit()
