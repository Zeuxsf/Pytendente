from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Me_Info, Enterprise_Info, SessionLocal, Base, database
import os

def clear():
    os.system('clear')

session = SessionLocal()


#Método de adicionar perguntas uma a uma
"""
while True:
    p = []
    for c in range(0,5):
        perguntas = str(input('Digite suas perguntas: '))
        p.append(perguntas)
    resposta = str(input('Digite uma resposta para as peguntas: '))
    

    conhecimento = Me_Info(
        question=p,
        response=resposta
        )
    session.add(conhecimento)
    session.commit()
    session.close()
    clear()    
"""

#Método automático, só colar um JSON dentro da lista com perguntas e respostas e depois rodar o script
""" 
dados_me = [
    {

    }
]

for item in dados_me:
    resp = Me_Info(question=item['perguntas'],response=item['resposta'])

    session.add(resp)
    session.commit()
    session.close() 

print('Banco de dados atualizado com sucesso')
"""

#Código para deletar conhecimentos
"""
item = session.query(Knowledge).filter(Knowledge.id == 2).first()
session.delete(item)
session.commit()
"""

#Código para treinar modelos de bot com conhecimentos do banco de dados
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle

  

session = SessionLocal()
Base.metadata.create_all(bind=database)
dados = session.query(Me_Info).all()


perguntas = []
respostas = []


for item in dados:

    for p in item.question:

        perguntas.append(p) 
        respostas.append(item.response)

  
vectorizer = TfidfVectorizer()
vetores = vectorizer.fit_transform(perguntas)
  

model_data = {

'vectorizer': vectorizer,
'questions': perguntas,
'responses': respostas,
'vectors': vetores

}

  

with open('bot/trained_model_2.pkl','wb') as file:
    pickle.dump(model_data,file)

print('salvo')
