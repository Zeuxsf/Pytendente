import streamlit as st
from chat_me import chat_me
from chat_demo import chat_demo
from infos import home_info, chat_info, ticket_info

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(
    page_title="Pytendente",
    page_icon="🕹",
    layout="wide"
)

if "menu" not in st.session_state:
    st.session_state.menu = "Início"

if "sub_menu" not in st.session_state:
    st.session_state.sub_menu = None


# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("Menu")

if "redirect_to" not in st.session_state:
    st.session_state.redirect_to = None


# 🔥 PROCESSA REDIRECIONAMENTO AQUI
if st.session_state.redirect_to == "Tickets":
    st.session_state.menu = "Tickets"
    st.session_state.sub_menu = "Criar Ticket"  # se quiser já abrir algo específico
    st.session_state.redirect_to = None


menu = st.sidebar.radio(
    "Navegação",
    ["Início", "Chats", "Tickets"],
    key="menu"
)

# Submenus dinâmicos
if st.session_state.menu == "Chats":
    st.sidebar.radio(
        "Selecionar Chat",
        ["Portifólio", "Demo - Empresa Fictícia"],
        key="sub_menu"
    )

if st.session_state.menu == "Tickets":
    st.sidebar.radio(
        "Funções",
        ["Criar Ticket", "Listar Tickets", "Fechar Ticket"],
        key="sub_menu"
    )

# -----------------------------
# PÁGINAS
# -----------------------------


def ticket_create():
    st.title("🎫 Criar Ticket")
    titulo = st.text_input("Título")
    descricao = st.text_area("Descrição")

    if st.button("Criar"):
        st.success(f"Ticket '{titulo}' criado com sucesso.")


def ticket_list():
    st.title("📋 Listar Tickets")

    # Mock simples
    tickets = [
        {"id": 1, "titulo": "Erro no login"},
        {"id": 2, "titulo": "Bug na API"},
        {"id": 3, "titulo": "Atualização pendente"},
    ]

    for ticket in tickets:
        st.write(f"ID: {ticket['id']} | {ticket['titulo']}")


def ticket_close():
    st.title("❌ Fechar Ticket")
    ticket_id = st.number_input("ID do Ticket", min_value=1, step=1)

    if st.button("Fechar"):
        st.warning(f"Ticket {ticket_id} fechado.")


# -----------------------------
# ROTEAMENTO
# -----------------------------

if st.session_state.get("go_to_tickets"):
    st.session_state.menu = "Tickets"
    st.session_state.go_to_tickets = False

if st.session_state.menu == "Início":
    home_info()

if st.session_state.menu == "Chats":
    chat_info()

if st.session_state.menu == "Tickets":
    ticket_info()    

elif st.session_state.menu == "Chats":
    if st.session_state.sub_menu == "Portifólio":
        r = chat_me()
        if r == '1':
            st.session_state.redirect_to = "Tickets"
            st.rerun()
    elif st.session_state.sub_menu == "Demo - Empresa Fictícia":
        chat_demo()

elif st.session_state.menu == "Tickets":
    if st.session_state.sub_menu == "Criar Ticket":
        ticket_create()
    elif st.session_state.sub_menu == "Listar Tickets":
        ticket_list()
    elif st.session_state.sub_menu == "Fechar Ticket":
        ticket_close()