import streamlit as st

def home_info():
    st.title("Início")
    st.write("Bem-vindo ao painel.")
    st.info("Selecione uma opção na barra lateral.")


def chat_info():
    st.title("Início")
    st.write("Bem-vindo aos chats.")
    st.info("Selecione uma opção na barra lateral.")


def ticket_info():
    st.title("Início")
    st.write("Bem-vindo aos tickets.")
    st.info("Selecione uma opção na barra lateral.")

def repos():
    st.title("📋 Listar Tickets")

    # Mock simples
    tickets = [
        {"id": 1, "titulo": "Erro no login", "star": 10},
        {"id": 2, "titulo": "Bug na API", "star": 10},
        {"id": 3, "titulo": "Atualização pendente", "star": 5},
    ]

    for ticket in tickets:
        st.write(f"ID: {ticket['id']} | {ticket['titulo']} | {ticket['star']}")