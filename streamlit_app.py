import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

import textwrap
st.title("Chat-OpenAI")
def generate_response(input_text, messages):
    model = ChatOpenAI(temperature=0.3, model_name='gpt-4o')
    response = model.invoke(messages)
    answer = textwrap.fill(response.content, width=100)
    return answer

if "messages" not in st.session_state:
    system_prompt = "Отвечай только на русском, как будто ты 50 летний вор в законе. Отвечай мемными фразами и побольше юмора,агрессии и оскорблений."
    st.session_state.messages = [{"role": "system", "content": system_prompt}]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Введите ваш запрос"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = generate_response(prompt,st.session_state.messages)
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
