import streamlit as st
from langchain_ollama import ChatOllama


# conectando com o deepseek
llm = ChatOllama(model='deepseek-r1:8b', base_url='http://localhost:11434')

## PÁGINA DO APP
# config
st.set_page_config(page_title='Deepseek R1-8B localmente', layout='centered')
st.title('Converse com o deepseek hospedado localmente')

# criando a memória
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
    
messages = st.session_state['messages']

for m_type, content in messages:
    chat = st.chat_message(m_type)
    chat.markdown(content)

# prompt
prompt = st.chat_input("Fale com o deepseek...")

if prompt:
    messages.append(('human',prompt))
    chat = st.chat_message('human')
    chat.markdown(prompt)

    # interagindo com o modelo
    bot = llm.invoke(messages)
    messages.append(('ai',bot.content))

    chat = st.chat_message('ai')
    chat.markdown(bot.content)