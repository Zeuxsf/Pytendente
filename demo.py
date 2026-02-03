from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 
from bot.models import Me_Info, Enterprise_Info, Log, SessionLocal, Base, database
import pickle

def atualizar_log():
    session = SessionLocal()
    dados_do_log = session.query(Log).all()
    log = []
    for item in dados_do_log:
        log.append(item.question)  
    session.close()     
    return log    

log = atualizar_log()

with open('bot/trained_model.pkl', 'rb') as file:
    model = pickle.load(file)

vectorizer = model['vectorizer']
questions = model['questions']
responses = model['responses']
vectors = model['vectors']
print("Modelo Carregado com Sucesso!")

def responder(pergunta):
    vetor_user = vectorizer.transform([pergunta])
    similaridades = cosine_similarity(vetor_user, vectors)

    idx = similaridades.argmax()
    score = similaridades[0][idx]

    if score < 0.3:
        return 'Desculpe, não entendi. Pode repetir?'
    return responses[idx]

def adicionar_log(pergunta):
    log = Log(pergunta,'Demo')
    session.add(log)
    session.commit()

while True: 
    p = str(input('Pergunte: '))
    print(responder(p))
    if p not in log:
        if responder(p) == 'Desculpe, não entendi. Pode repetir?':
            print('Deseja adicionar sua pergunta ao Log para podermos melhorar nossas respostas?')
            sn = str(input('[1]SIM [Qualquer tecla]NÃO: '))
            if sn == '1':
                adicionar_log(p)
                print(f'"{p}" Adicionado ao log de perguntas sem resposta.')
                log = atualizar_log()
    else:
        print('Sua pergunta existe no Log, e logo mais eu poderei respondê-la. Por favor, faça outra pergunta!')            
