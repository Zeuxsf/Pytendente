import streamlit as st
import requests
import os
from dotenv import load_dotenv
import re

load_dotenv()


def validar_email(email):
    #Pra garantir que o programa funcione na maioria das vezes
    padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if re.fullmatch(padrao, email):
        return True
    return False

def ticket_abrir():
    st.title("Abrir Ticket")
    nome = st.text_input("Nome")
    user_email = st.text_input('E-mail')
    assunto = st.text_input("Assunto")
    mensagem = st.text_area("Descrição")

    if st.button("Enviar"):
        try:
            #Verificação de erros pra não rodar o comando com problemas
            if nome == '' or user_email == '' or assunto == '' or mensagem == '':
                st.error("Verifique se tem algum Campo de texto vazio.")
                st.stop()
            if validar_email(user_email) == False:
                st.error("Verifique se digitou seu E-email corretamente.")
                st.stop()

            #Um loading pra mostrar ao usuário que o email está sendo enviado
            with st.spinner("Enviando..."):
                requests.post(f"{os.getenv('API_URL')}/action/tickets/abrir",
                    json={"nome": nome,"user_email": user_email,"assunto": assunto,"mensagem": mensagem})
            
            st.success(f"Ticket '{assunto}' criado com sucesso.")
        except Exception as e:
            st.error("Não foi possível abrir esse ticket.")
            print(e)


def ticket_visualizar():
    st.title("Visualizar Ticket")
    user_email = st.text_input('E-mail')
    codigo = st.text_input('Código')

    if st.button("Visualizar"):
        try:    
            if user_email == '' or codigo == '':
                st.error("Verifique se tem algum Campo de texto vazio.")
                st.stop()
            if validar_email(user_email) == False:
                st.error("Verifique se digitou seu E-email corretamente.")
                st.stop()

            with st.spinner("Visualizando..."):
                response = requests.get(f"{os.getenv('API_URL')}/action/tickets/visualizar?user_email={user_email}&codigo={codigo}")
                response = response.json()   

            st.text_input("Assunto:",response["subject"])
            st.text_area("Resposta:",response["response"])

        except Exception as e:
            st.error("Não foi possível visualizar esse ticket.")
            print(e) 
            

def ticket_responder():
    st.title("Responder Ticket")
    st.write("Apenas Admins com a senha podem realizar essa função.")

    codigo = st.text_input("Código")
    senha = st.text_input("Senha")
    resposta = st.text_area("Resposta")

    if st.button("Enviar"):
        try:    
            if codigo == '' or senha == '' or resposta == '':
                st.error("Verifique se tem algum Campo de texto vazio.")
                st.stop()

            with st.spinner("Respondendo..."):
                response = requests.patch(f"{os.getenv('API_URL')}/action/tickets/responder",
                    json={"ticket": codigo,"senha": senha,"resposta": resposta})
                response = response.json()
            
            st.write(response["resposta"])

        except Exception as e:
            st.error("Não foi possível responder esse ticket.")
            print(e) 

