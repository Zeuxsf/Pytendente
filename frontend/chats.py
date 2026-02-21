import streamlit as st 
import requests

def chat_me():

    st.title("Portifólio - Informações sobre mim")

    if "messages_me" not in st.session_state:
        st.session_state.messages_me = []

    #Vai carregar todas as mensagens enviadas, porque toda vez que o site executa uma função, ele executa todo o código de novo, então é importante recarregar tudo pro usuário não perceber
    for msg in st.session_state.messages_me:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    #Aqui é onde o usuário vai digitar a mensagem dele pro bot analisar
    if prompt := st.chat_input("Digite sua pergunta..."):
        st.session_state.messages_me.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.write(prompt)

        #Vai fazer a chamada na API do bot
        response = requests.post(
            f"{st.secrets['API_URL']}/action/conversation/me",
            json={"question": prompt}
        )

        bot_reply = response.json()

        with st.chat_message("assistant"):
            st.write(bot_reply['resposta'])
        
        st.session_state.messages_me.append({"role": "assistant", "content": bot_reply['resposta']})

        #Aqui são os comandos pré configurados no bot. Como eu disse no arquivo app.py: não é o método mais elegante de redirecionamento, mas funciona muito bem!
        if '[0]' in bot_reply['resposta'] and 'principais projetos' in bot_reply['resposta']:
            return '0'
        elif '[1]' in bot_reply['resposta'] and 'abrindo' in bot_reply['resposta']:
            return '1'
        elif '[2]' in bot_reply['resposta'] and 'criação' in bot_reply['resposta']:
            return '2'        


def chat_demo(): #Deixei o chat Demo sem comentários porque é basicamente o chat_me com menos coisas

    st.title("Demo - Informações sobre uma empresa fictícia")

    if "messages_demo" not in st.session_state:
        st.session_state.messages_demo = []

    for msg in st.session_state.messages_demo:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if prompt := st.chat_input("Digite sua pergunta..."):
        st.session_state.messages_demo.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.write(prompt)

        response = requests.post(
            f"{st.secrets['API_URL']}/action/conversation/demo",
            json={"question": prompt}
        )

        bot_reply = response.json()

        with st.chat_message("assistant"):
            st.write(bot_reply['resposta'])
        
        st.session_state.messages_demo.append({"role": "assistant", "content": bot_reply['resposta']})