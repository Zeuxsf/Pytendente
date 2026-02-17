import streamlit as st

st.set_page_config(
    page_title="Pytendente",
    page_icon="🎩",
    layout="wide",
    initial_sidebar_state="expanded",
)

def load_css():
    with open("interface/style.css") as f:
        st.markdown(f"""<style>{f.read()}</style>""", unsafe_allow_html=True)

load_css()

# ── Session State ──
if "page" not in st.session_state:
    st.session_state.page = "home"
if "chat_sub" not in st.session_state:
    st.session_state.chat_sub = None
if "ticket_sub" not in st.session_state:
    st.session_state.ticket_sub = None

def go(page, chat_sub=None, ticket_sub=None):
    st.session_state.page = page
    st.session_state.chat_sub = chat_sub
    st.session_state.ticket_sub = ticket_sub

# ── Sidebar ──
with st.sidebar:
    st.markdown('<div class="sidebar-title">Pytendente</div>', unsafe_allow_html=True)

    # Início
    css = "nav-active" if st.session_state.page == "home" else ""
    st.markdown(f'<div class="{css}">', unsafe_allow_html=True)
    if st.button("🏠  Início", key="btn_home"):
        go("home")
    st.markdown('</div>', unsafe_allow_html=True)

    # Chat
    st.markdown('<div class="sidebar-label">Chat</div>', unsafe_allow_html=True)
    css = "nav-active" if st.session_state.page == "chat" else ""
    st.markdown(f'<div class="{css}">', unsafe_allow_html=True)
    if st.button("💬  Chat", key="btn_chat"):
        go("chat")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.page == "chat":
        css = "nav-sub-active" if st.session_state.chat_sub == "demo" else "nav-sub"
        st.markdown(f'<div class="{css}">', unsafe_allow_html=True)
        if st.button("↳ Demo de empresa fictícia", key="btn_demo"):
            go("chat", chat_sub="demo")
        st.markdown('</div>', unsafe_allow_html=True)

        css = "nav-sub-active" if st.session_state.chat_sub == "portfolio" else "nav-sub"
        st.markdown(f'<div class="{css}">', unsafe_allow_html=True)
        if st.button("↳ Sobre mim · Chat portfólio", key="btn_portfolio"):
            go("chat", chat_sub="portfolio")
        st.markdown('</div>', unsafe_allow_html=True)

    # Ticket
    st.markdown('<div class="sidebar-label">Suporte</div>', unsafe_allow_html=True)
    css = "nav-active" if st.session_state.page == "ticket" else ""
    st.markdown(f'<div class="{css}">', unsafe_allow_html=True)
    if st.button("🎫  Ticket", key="btn_ticket"):
        go("ticket")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.page == "ticket":
        for key, label in [("abrir", "↳ Abrir ticket"), ("visualizar", "↳ Visualizar tickets"), ("responder", "↳ Responder ticket")]:
            css = "nav-sub-active" if st.session_state.ticket_sub == key else "nav-sub"
            st.markdown(f'<div class="{css}">', unsafe_allow_html=True)
            if st.button(label, key=f"btn_{key}"):
                go("ticket", ticket_sub=key)
            st.markdown('</div>', unsafe_allow_html=True)

# ── Conteúdo principal ──
page = st.session_state.page

# HOME
if page == "home":
    st.markdown('<div class="page-title">Bem-vindo 👋</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Navegue pelo menu lateral para explorar.</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class="card">
            <div class="card-title">💬 Chat</div>
            <div class="card-body">Demo de empresa fictícia ou chat de portfólio pessoal.</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="card">
            <div class="card-title">🎫 Tickets</div>
            <div class="card-body">Abra, visualize e responda tickets de suporte.</div>
        </div>""", unsafe_allow_html=True)

# CHAT
elif page == "chat":
    sub = st.session_state.chat_sub
    if sub is None:
        st.markdown('<div class="page-title">💬 Chat</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Selecione uma opção no menu lateral.</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""<div class="card">
                <div class="card-title">Demo de empresa fictícia</div>
                <div class="card-body">Assistente simulando atendimento corporativo.</div>
            </div>""", unsafe_allow_html=True)
        with col2:
            st.markdown("""<div class="card">
                <div class="card-title">Sobre mim · Chat portfólio</div>
                <div class="card-body">Converse sobre minha trajetória e projetos.</div>
            </div>""", unsafe_allow_html=True)

    elif sub == "demo":
        st.markdown('<div class="page-title">Demo — Empresa Fictícia</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Assistente da Nexora Co.</div>', unsafe_allow_html=True)
        with st.chat_message("assistant"):
            st.write("Olá! Bem-vindo à **Nexora Co.** Como posso te ajudar?")
        msg = st.chat_input("Digite sua mensagem...")
        if msg:
            with st.chat_message("user"):
                st.write(msg)
            with st.chat_message("assistant"):
                st.write("_(Integração com IA em breve)_")

    elif sub == "portfolio":
        st.markdown('<div class="page-title">Chat Portfólio</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Pergunte sobre projetos, skills e experiências.</div>', unsafe_allow_html=True)
        with st.chat_message("assistant"):
            st.write("Oi! Me pergunte sobre projetos, tecnologias ou experiências profissionais.")
        msg = st.chat_input("Digite sua mensagem...")
        if msg:
            with st.chat_message("user"):
                st.write(msg)
            with st.chat_message("assistant"):
                st.write("_(Integração com IA em breve)_")

# TICKET
elif page == "ticket":
    sub = st.session_state.ticket_sub
    if sub is None:
        st.markdown('<div class="page-title">🎫 Tickets</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Gerencie suas solicitações de suporte.</div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""<div class="card"><div class="card-title">Abrir Ticket</div>
            <div class="card-body">Registre uma nova solicitação.</div></div>""", unsafe_allow_html=True)
        with col2:
            st.markdown("""<div class="card"><div class="card-title">Visualizar Tickets</div>
            <div class="card-body">Acompanhe o status das solicitações.</div></div>""", unsafe_allow_html=True)
        with col3:
            st.markdown("""<div class="card"><div class="card-title">Responder Ticket</div>
            <div class="card-body">Adicione informações a um ticket existente.</div></div>""", unsafe_allow_html=True)

    elif sub == "abrir":
        st.markdown('<div class="page-title">Abrir Ticket</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Preencha os campos abaixo.</div>', unsafe_allow_html=True)
        with st.form("form_abrir"):
            st.text_input("Assunto")
            st.selectbox("Categoria", ["Dúvida", "Problema técnico", "Sugestão", "Outro"])
            st.selectbox("Prioridade", ["Baixa", "Média", "Alta", "Crítica"])
            st.text_area("Descrição", height=150)
            if st.form_submit_button("Abrir Ticket"):
                st.success("✅ Ticket aberto com sucesso!")

    elif sub == "visualizar":
        st.markdown('<div class="page-title">Meus Tickets</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Acompanhe o status das solicitações.</div>', unsafe_allow_html=True)
        tickets = [
            {"id": "#0042", "assunto": "Erro ao carregar dashboard", "status": "🟢 Aberto"},
            {"id": "#0038", "assunto": "Dúvida sobre integração de API", "status": "⚫ Encerrado"},
            {"id": "#0031", "assunto": "Sugestão de nova funcionalidade", "status": "🟢 Aberto"},
        ]
        for t in tickets:
            col1, col2, col3 = st.columns([1, 4, 2])
            col1.write(t["id"])
            col2.write(t["assunto"])
            col3.write(t["status"])
            st.divider()

    elif sub == "responder":
        st.markdown('<div class="page-title">Responder Ticket</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Selecione e responda um ticket.</div>', unsafe_allow_html=True)
        with st.form("form_responder"):
            st.selectbox("Ticket", ["#0042 — Erro ao carregar dashboard", "#0031 — Sugestão de nova funcionalidade"])
            st.text_area("Resposta", height=150)
            if st.form_submit_button("Enviar Resposta"):
                st.success("✅ Resposta enviada!")