import smtplib
import email.message
from dotenv import load_dotenv
import os
import random
import string
from models import Client, Ticket, SessionLocal, Base, database

load_dotenv()

def enviar_email(nome,user_email,assunto,mensagem,ticket):  #Quem diria, aprendi um pouco de HTML nesse projeto, sem querer kkkkkkkkk
    corpo_email = f"""
    <strong>Ticket aberto pelo usuário: {nome}</strong>
    <p> </p>
    <strong>Email para resposta: {user_email}</strong>
    <p> </p>
    <strong>Código gerado: {ticket}</strong>
    
    <hr style="border: none; border-top: 1px solid #ddd;">
    
    <p style="white-space: pre-line;">
     {mensagem}
    </p>
    """

    msg = email.message.Message()
    msg['Subject'] = assunto
    msg['From'] = f'{os.getenv('EMAIL_BOT')}' 
    msg['To'] = 'alexandrefranca270324@gmail.com' #Meu email próprio para contato
    password = f'{os.getenv('SENHA_APP')}'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com', 465, timeout=20)
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado para o Admin')#Debug

def enviar_email_usuario(nome,user_email,assunto,ticket):  #Essa função vai mandar um email pro próprio usuário, falando pra ele qual é o ticket dele, pra mostrar que o sistema funciona de fato 
    corpo_email = f"""
    <strong>Olá {nome}, aqui está o seu ticket que você abriu sobre "{assunto}"</strong>
    <p> </p>
    <strong>Para visualizar seu ticket, use o comando "visualizar ticket" no Pytendente, insira o seu email e o ticket gerado.
    <strong>[Aguarde no mínimo 24h para ser respondido(a)]</strong>
    
    <hr style="border: none; border-top: 1px solid #ddd;">
    
    <p style="white-space: pre-line;">
     Seu ticket: {ticket}
    </p>
    """

    msg = email.message.Message()
    msg['Subject'] = f'Ticket do Pytendente: "{assunto}"'
    msg['From'] = f'{os.getenv('EMAIL_BOT')}' 
    msg['To'] = user_email
    password = f'{os.getenv('SENHA_APP')}'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com', 465, timeout=20)
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado para o Usuário')#Debug

def gerar_ticket_randômico():
    try:
        #Essa função vai gerar um codigo aleatório e verificar se esse código já existe no banco de dados, se ele existir, vai acontecer um loop while até gerar um código único, a condição será satisfeita e o a função vai retornar o código gerado
        session = SessionLocal()
        
        unico = 0
        while unico != 1:
            caracteres = string.ascii_letters + string.digits
            ticket_gerado = ''.join(random.choices(caracteres, k=8))

            tickets_guardados = session.query(Ticket).filter(Ticket.ticket).all()
            
            if ticket_gerado not in tickets_guardados:
                unico = 1

        return ticket_gerado
    except Exception as e:
        print(e)
    finally:
        session.close()        

def abrir_ticket(nome,user_email,assunto,mensagem):
    try:
        nome = nome.lower()
        user_email = user_email.lower()

        session = SessionLocal()
        #Esse script vai verificar ser o usuário já existe no sistema, se ele não existir, vai adicionar no banco de dados automaticamente. Pretendo colocar uma verificação de username na função de [visualizar ticket], pra caso exista usuários de nomes diferentes porém com o mesmo email
        user = session.query(Client).filter(Client.name == nome, Client.email == user_email).first()
        if not user:
            new_user = Client(nome,user_email)
            session.add(new_user)
            session.commit()
            user = session.query(Client).filter(Client.name == nome, Client.email == user_email).first()            
        if user:
            print('usuário já existe') #debug    

        ticket = gerar_ticket_randômico()
        
        adicionar_ticket = Ticket(user.id,ticket,assunto)
        session.add(adicionar_ticket)
        session.commit()

        enviar_email(nome,user_email,assunto,mensagem,ticket)
        enviar_email_usuario(nome,user_email,assunto,ticket)
        
        return "Ticket aberto com sucesso! Confira seu email."
    except Exception as e:
        return f"ERRO ao abrir o ticket {e}"    
    finally:
        session.close()

def visualizar_ticket(user_email, ticket):
    try:
        #Essa função serve pro usuário visualizar os tickets que ele possui
        #Eu pensei em fazer um intermediário pra tipo, o usuário visualizar os tickets que ele possui e depois escolher qual ele quer visualizar... mas, eu quis manter a responsabilidade do usuário de guardar o próprio ticket hehe (Além de que me tira a responsabilidade de ter que criar usuários com senha)(É um MVP, espere coisas desse tipo 🫣)
        session = SessionLocal()
        user_id = session.query(Client).filter(Client.email == user_email.lower()).first()
        resposta = session.query(Ticket).filter(Ticket.client_id == user_id.id, Ticket.ticket == ticket).first()

        return {
            "ticket": resposta.ticket,
            "subject": resposta.subject,
            "response": resposta.response
        }
    except Exception as e:
        return f"ERRO ao visualizar o ticket {e}"
    finally:
        session.close()       

def responder_ticket(ticket_user, senha, resposta): #Essa é a função que o ADM (vulgo eu) vai usar para responder os tickets, vai facilitar muito na hora de responder, e é bom que já fica tudo em um sistema só. A senha de ADM fica no .env porque eu estou evitando criar sistema de usuários, pois eu acho desnecessário pra esse projeto, só farei esse sistema se o projeto crescer
    try:
        session = SessionLocal()
        ticket_para_resposta = session.query(Ticket).filter(Ticket.ticket == ticket_user).first()
        
        if ticket_para_resposta and senha == f'{os.getenv('SENHA_ADMIN')}':
            ticket_para_resposta.response = resposta
            session.commit()
            return {"resposta": "Resposta enviada com sucesso!"}
        else:
            return {"resposta": "Não foi possível responder o ticket, confira se ele está correto ou se você tem autorização para isso."}

    except Exception as e:
        return {"resposta": "Não foi possível responder o ticket"}
    finally:
        session.close()

if __name__ == '__main__':
    #abrir_ticket('Alexandre','-----@gmail.com','ovo','Caro programador, estamos felizes de te contratar, você começa amanhã como CEO') #Tão deixando a gente sonhar kkkkkk
    #print(gerar_ticket_randômico())
    #print(visualizar_ticket('Alexandre', 'alexandrefranca270324@gmail.com','uS3sF9tz'))
    '''
    session = SessionLocal()
    item = session.query(Client).filter(Client.id == 12).first() #Código pra excluir usuários defeituosos
    session.delete(item)
    print('excluido')
    session.commit()
    session.close()
    '''
