import streamlit as st
import pandas as pd
from datetime import date

dados = pd.read_csv("clientes.csv")

st.title ("Cliente cadastrados: ")
st.divider()

st.dataframe (dados)