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
    ticket = gerar_ticket_randômico()

    enviar_email(nome,user_email,assunto,mensagem,ticket)

if __name__ == '__main__':
    #abrir_ticket('Alexandre','alexandrefranca270324@gmail.com','OTESTE2','Cara, você é foda demais, meu sonho é ser igual você um dia')
    #print(gerar_ticket_randômico())
    ...
