import streamlit as st
from chats import chat_me, chat_demo
from infos import home_info, chat_info, ticket_info, repos
from tickets import ticket_abrir, ticket_visualizar, ticket_responder


#Configuração básica do site
st.set_page_config(
    page_title="Pytendente",
    page_icon="🎩",
    layout="wide"
)

#Criando os session state pro site não ficar resetando
if "menu" not in st.session_state:
    st.session_state.menu = "Início"

if "sub_menu" not in st.session_state:
    st.session_state.sub_menu = None

if "redirect_to" not in st.session_state:
    st.session_state.redirect_to = None

#Essa função de redirecionamento tem que ser feita bem no topo do projeto, pra respeitar a ordem de execução do streamlit
if st.session_state.redirect_to == "Tickets":
    st.session_state.menu = "Tickets"
    sub = ''
    if sub == '1':
        st.session_state.sub_menu = "Abrir Ticket" 
    elif sub == '2':
        st.session_state.sub_menu = "Visualizar Ticket"     
    st.session_state.redirect_to = None

elif st.session_state.redirect_to == "Projetos":
    st.session_state.menu = "Projetos"
    st.session_state.redirect_to = None


#Side bar: É onde o usuário pode navegar
st.sidebar.title("Menu")

menu = st.sidebar.radio(
    "Navegação",
    ["Início", "Chats", "Tickets", "Projetos"],
    key="menu"
)

#Sub menus
if st.session_state.menu == "Chats":
    st.sidebar.radio(
        "Selecionar Chat",
        ["Portifólio", "Demo"],
        key="sub_menu"
    )

if st.session_state.menu == "Tickets":
    st.sidebar.radio(
        "Funções",
        ["Abrir Ticket", "Visualizar Ticket", "Responder Ticket - Admin Only"],
        key="sub_menu"
    )



#A navegação de fato acontece aqui: depois de escolher uma aba, o session state vai receber aquela aba e ficar nela até o usuário mudar
if st.session_state.get("go_to_tickets"):
    st.session_state.menu = "Tickets"
    st.session_state.go_to_tickets = False

if st.session_state.menu == "Início":
    home_info()

elif st.session_state.menu == "Chats" and st.session_state.sub_menu == None:
    chat_info()

if st.session_state.menu == "Tickets" and st.session_state.sub_menu == None:
    ticket_info()    

elif st.session_state.menu == "Chats":
    if st.session_state.sub_menu == "Portifólio":
        #Eu fiquei muito feliz de dar vida a essa parte do código, porque era algo q eu imaginava mas não sabia se ia ser possível com o streamlit. Não me entenda mal, eu sei que esse não é o método mais elegante de fazer o bot executar uma função, mas eu queria algo simples pra esse MVP
        r = chat_me()
        if r == '0':
            st.session_state.redirect_to = "Projetos"
            st.rerun()
        if r == '1':
            st.session_state.redirect_to = "Tickets"
            sub = '1'
            st.rerun()
        if r == '2':
            st.session_state.redirect_to = "Tickets"
            sub = '2'
            st.rerun()
            
    elif st.session_state.sub_menu == "Demo":
        chat_demo()


elif st.session_state.menu == "Tickets":
    if st.session_state.sub_menu == "Abrir Ticket":
        ticket_abrir()
    elif st.session_state.sub_menu == "Visualizar Ticket":
        ticket_visualizar()
    elif st.session_state.sub_menu == "Responder Ticket - Admin Only":
        ticket_responder()


elif st.session_state.menu == "Projetos":
    repos()
