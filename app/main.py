import streamlit as st
import pandas as pd
from service import analyze_pdf as ap




st.set_page_config(
    page_title="Processador de notas fiscais em PDF", 
    page_icon=":memo:", 
    layout="wide")

st.markdown("""
    <style>
        
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        
        html, body, [class*="css"], div, span, p, label, button, input, textarea, select {
            font-family: 'Poppins', sans-serif !important;
        }

        
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Poppins', sans-serif !important;
            font-weight: 600 !important;
        }

        
        [data-testid="stDataFrame"], [data-testid="stTable"], .stDataFrame div {
            font-family: 'Poppins', sans-serif !important;
        }

        
        input::placeholder, textarea::placeholder {
            font-family: 'Poppins', sans-serif !important;
            color: #888 !important; /* Opcional: muda a cor do placeholder */
        }
        
        
        [data-testid="stMetricValue"] {
            font-family: 'Poppins', sans-serif !important;
        }
        
        
        div[role="grid"] {
            font-family: 'Poppins', sans-serif !important;
        }
    </style>
    """, unsafe_allow_html=True)

st.title("Processador de notas fiscais em PDF")
st.write("Carregue um arquivo PDF para extrair informações como CNPJ, Data e Valor.")

def get_pdf():

    arquivos = st.file_uploader(
    "Adicione um PDF",
     type=["pdf"],
     accept_multiple_files=True)
    

    
    if arquivos :
        arquivos_processados = []
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
            df_editado = st.data_editor(df)
            csv = df_editado.to_csv(index=False).encode('utf-8')
            
            total_valor = df_editado["VALOR"].sum()

            st.divider()            
            col_acao, col_espaco, col_total = st.columns([2,6,3])
            

            with col_total:
                
                st.metric("VALOR TOTAL:", f"R$ {total_valor:,.2f}")
            with col_acao:
                st.download_button(
                label="BAIXAR PLANILHA (CSV)",
                data=csv,
                file_name="dados_processados.csv",
                mime="text/csv",
                use_container_width=True
               
            )
            

get_pdf() 