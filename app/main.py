import streamlit as st
import pandas as pd
from service import analyze_pdf as ap




st.set_page_config(
    page_title="Processador de PDF", 
    page_icon=":memo:", 
    layout="wide")

st.title("Processador de PDF")
st.write("Carregue um arquivo PDF para extrair informações como CNPJ, Data e Valor.")

def get_pdf():

    arquivo = st.file_uploader(
    "Adicione um PDF",
     type=["pdf"],
     accept_multiple_files=True)
    
    if arquivo is not None:
        st.write("Arquivo carregado com sucesso! Processando...")

    return arquivo

get_pdf() 