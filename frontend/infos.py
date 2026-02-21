import streamlit as st
import requests


def home_info():
    st.title("Início")
    st.markdown("**Seja muito bem-vindo(a)!**")
    st.write("Esse projeto é um MVP, sujeito à mudanças. Caso ache algum bug ou queira sugerir uma melhoria: Abra um ticket!")
    st.info("Selecione uma opção na barra lateral.")
    st.warning("O servidor foi hospedado em um plano gratuito, o serviço de tickets pode não funcionar. Caso queira entrar em contato comigo, me envie um e-mail: Alexandrefranca270324@gmail.com.")


def chat_info():
    st.title("Chats")    
    st.markdown("**Selecione o chat na barra lateral.**") 
    
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("Portifólio")
            st.markdown("**O chat 'Portifólio' é o chat principal desse projeto, nele contém informações sobre mim, sobre meus projetos e funções que interagem diretamenta com a interface.**")
            st.write("Sugestôes de mensagens: 'Me conte mais sobre você, 'Experiência', 'Seus principais projetos', 'Meios de contato', 'Sobre o ticket'")
            st.info("Recomendado")

    with col2:
        with st.container(border=True):
            st.subheader("Demo")
            st.markdown("**O chat 'Demo' foi criado mais como um assistente de teste, pra testar como o bot se comporta com um volume maior de informações guardadas, mas ele é bem simples**")
            st.write("Sugestôes de mensagens: 'Quero abrir uma conta', 'Como posso ver meu saldo?', 'Quero investir', 'Quantas contas eu posso ter?'")  

    st.markdown("**obs: Este projeto é um MVP, podem haver erros de compreensão.**")
             


def ticket_info():
    st.title("Tickets")
    st.markdown("**Selecione uma função na barra lateral.**")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("Abrir ticket")
            st.markdown("**Quer falar comigo? Abra um ticket!**")
            st.write("Após abrir um ticket você irá receber um email com um código, é assim que você vai poder visualizar sua resposta.")
            st.caption("Tempo mínimo de resposta: 24h")

    with col2:
        with st.container(border=True):
            st.subheader("Visualizar ticket")
            st.markdown("**Visualize sua reposta!**")
            st.write("Use o código que você recebeu por email para visualizar a resposta do seu ticket.")         

def repos():
    with st.spinner("Carregando os projetos..."):    
        st.title("Meus projetos")
        st.markdown("**Aqui vão alguns projetos que estão Pinados no meu perfil do github.**")
        st.info("Eles são buscados dinâmicamente via API.")

        response = requests.get(f"{st.secrets['API_URL']}/action/conversation/me/repos")
        response = response.json()

        for item in response:
            with st.container(border=True):
                st.subheader(item['name'])
                st.write(item['description'])
                st.write(item['primaryLanguage']['name'])
                st.metric('Estrelas', item['stargazerCount'])
                st.caption(item['url'])
            
