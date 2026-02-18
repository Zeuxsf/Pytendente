import streamlit as st 
import requests


def chat_demo():

    API_URL = "http://127.0.0.1:8000"

    st.title("Meu Assistente")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar histórico
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Input
    if prompt := st.chat_input("Digite sua pergunta..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.write(prompt)

        # Chamada para sua API
        response = requests.post(
            f"{API_URL}/action/conversation/demo",
            json={"question": prompt}
        )

        bot_reply = response.json()

        with st.chat_message("assistant"):
            st.write(bot_reply['resposta'])
        
        st.session_state.messages.append({"role": "assistant", "content": bot_reply['resposta']})

