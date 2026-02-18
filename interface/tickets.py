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
            if nome or user_email or assunto or mensagem == '':
                st.error("Verifique se tem algum Campo de texto vazio.")
                st.stop()
            if validar_email(user_email) == False:
                st.error("Verifique se digitou seu E-email corretamente.")
                st.stop()

            #Um loading pra mostrar ao usuário que o email está sendo enviado
            with st.spinner("Enviando..."):
                requests.post(f"{os.getenv('API_URL')}/action/tickets/abrir",
                    json={"nome": nome,"user_email": user_email,"assunto": assunto,"mensagem": mensagem}
                )
            
            st.success(f"Ticket '{assunto}' criado com sucesso.")
        except Exception as e:
            st.error("Não foi possível abrir esse ticket.")
            print(e)


def ticket_visualizar():
    st.title("📋 Listar Tickets")

    # Mock simples
    tickets = [
        {"id": 1, "titulo": "Erro no login"},
        {"id": 2, "titulo": "Bug na API"},
        {"id": 3, "titulo": "Atualização pendente"},
    ]

    for ticket in tickets:
        st.write(f"ID: {ticket['id']} | {ticket['titulo']}")


def ticket_responder():
    st.title("❌ Fechar Ticket")
    ticket_id = st.number_input("ID do Ticket", min_value=1, step=1)

    if st.button("Fechar"):
        st.warning(f"Ticket {ticket_id} fechado.")
