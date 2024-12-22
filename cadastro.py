import streamlit as st
import pandas as pd
from datetime import date

@st.cache_data
def gravar_dados (nome, dt_nascimento, tipo):
    if nome and dt_nascimento <= date.today(): #date.today = hoje / Se o nome não for vazio e a data de nascimento for de hoje pra baixo
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome}, {dt_nascimento.strftime(format="%d/%m/%Y")}, {tipo}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False

st.set_page_config(
    page_title="Cadastro de clientes",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title ("Cadastro de Clientes")
st.divider() #Adiciona uma linha

nome = st.text_input ("Digite o nome do cliente", 
                      key="nome_input")
dt_nascimento = st.date_input ("Digite sua data de nascimento",
                      key="data_input",
                      format="DD/MM/YYYY")
tipo = st.selectbox ("Tipo do cliente:",
                     ["Pessoa física", "Pessoa jurídica"])
btn_cadastrar = st.button ("Cadastrar", 
                           on_click= gravar_dados,
                           args=[nome, dt_nascimento, tipo])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!",
                   icon="🆗")
    else:
        st.error("Houve um problema no cadastro do cliente.",
                 icon="❌")