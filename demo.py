from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 
from bot.models import Me_Info, Enterprise_Info, Log, SessionLocal, Base, database
import pickle

#Essa função vai carregar o modelo pré treinado, para que não seja preciso carregar o banco de dados toda vez que usar o bot
def carregar_modelo():
    with open('bot/trained_model.pkl', 'rb') as file:
        model = pickle.load(file)

    vectorizer = model['vectorizer']
    questions = model['questions']
    responses = model['responses']
    vectors = model['vectors']
    print("Modelo Carregado com Sucesso!")
    return vectorizer,questions,responses,vectors

vectorizer,questions,responses,vectors = carregar_modelo()

#Função em que o bot vai comparar a pergunta do usuário e as salvas no banco de conhecimento, a com o melhor score será usada
def responder(pergunta):
    vetor_user = vectorizer.transform([pergunta])
    similaridades = cosine_similarity(vetor_user, vectors)

    idx = similaridades.argmax()
    score = similaridades[0][idx]

    if score < 0.1:
        return 'Desculpe, não entendi. Pode repetir?'
    return responses[idx]


#Essa função vai atualizar o banco de log durante a execução do programa, para que não seja reiniciar para que o sistema tenha acesso ás novas informações
def atualizar_log():
    session = SessionLocal()
    dados_do_log = session.query(Log).all()
    log = []
    for item in dados_do_log:
        log.append(item.question)  
    session.close()     
    return log    

#Essa função vai adicionar perguntas que o bot não conseguiu entender ao banco de Log, o admin poderá revisar essas mensagens e decidir se vai alocar elas ou descartá-las (lembrando que essa parte de revisar logs vai depender se você vai criar um script pra automatizar isso ou se vai fazer hardcoded)
def adicionar_log(pergunta):
    session = SessionLocal()
    log = Log(pergunta,'Demo')
    session.add(log)
    session.commit()
    session.close()


log = atualizar_log() #Já deixa o log ativado, pronto pra ser usado no teste abaixo

#Teste do modelo Empresa Fictícia
if __name__ == '__main__':
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
