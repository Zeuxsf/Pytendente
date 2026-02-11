import smtplib
import email.message
from dotenv import load_dotenv
import os
import random
import string
from api.models import Client, Ticket, SessionLocal, Base, database

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
    msg['To'] = user_email
    password = f'{os.getenv('SENHA_APP')}'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')#Debug

def gerar_ticket_randômico():
    #Essa função vai gerar um codigo aleatório e verificar se esse código já existe no banco de dados, se ele existir, vai acontecer um loop while até gerar um código único, a condição será satisfeita e o a função vai retornar o código gerado
    session = SessionLocal()
    
    unico = 0
    while unico != 1:
        caracteres = string.ascii_letters + string.digits
        ticket_gerado = ''.join(random.choices(caracteres, k=8))

        tickets_guardados = session.query(Ticket).filter(Ticket.ticket).all()
        
        if ticket_gerado not in tickets_guardados:
            unico = 1
    
    session.close()
    return ticket_gerado

def abrir_ticket(nome,user_email,assunto,mensagem):
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
    session.close()
    return ticket #Pra api poder retornar o ticket que o usuário deve guardar para obter a resposta

if __name__ == '__main__':
    #abrir_ticket('Alexandre','alexandrefranca270324@gmail.com','ovo','Caro programador, estamos felizes de te contratar, você começa amanhã como CEO') #Tão deixando a gente sonhar kkkkkk
    #print(gerar_ticket_randômico())
    
    '''
    session = SessionLocal()
    item = session.query(Client).filter(Client.id == 12).first() #Código pra excluir usuários defeituosos
    session.delete(item)
    print('excluido')
    session.commit()
    session.close()
    '''
