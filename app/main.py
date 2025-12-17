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

    arquivos = st.file_uploader(
    "Adicione um PDF",
     type=["pdf"],
     accept_multiple_files=True)
    

    arquivos_processados = []
    if arquivos :
        st.write(f'Arquivos carregados com sucesso! Total de {len(arquivos)} arquivo(s).')

        for file in arquivos:
            resultado = ap(file)

            if resultado["status"] == "success":
                arquivos_processados.append({
                    "ARQUIVO": resultado["filename"],
                    **resultado["dados"]
            })
            else:
                st.error(f"Erro ao processar {resultado['filename']}: {resultado['message']}")

        if arquivos_processados:
            df = pd.DataFrame(arquivos_processados)
            st.dataframe(df)
    return arquivos

get_pdf() 