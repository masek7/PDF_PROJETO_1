import re

def extract_cnpj(doc):
    #func que extrai o cnpj do pdf

    try:
        

        cnpj = re.compile(r'\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}')
        cnpj_encontrado = cnpj.findall(doc)

        
        return cnpj_encontrado[0]
        
    except IndexError as e:
        return f"Erro ao extrair CNPJ: {e}" 
    



def extract_value(doc):

    try:

        #func que extrai o valor contido na nota

        
    
        value = doc.rfind("TOTAL R")
        valor = doc[value + 8: value + 15]
        valor_format = valor.replace(" " "\n", "")
        
        
        return float(valor_format)


    except Exception as e:
        return f"Erro ao extrair valor: {e}"
    


def extract_date(doc):
    
    try:

        #func que extrai a data contida na nota
       

        data = re.compile(r'\d{2}\/\d{2}\/\d{4}')
        data_nota = data.findall(doc)
        dn_format = data_nota[0]

        
        return dn_format
    
    except Exception as e:
        return f"Erro ao extrair data: {e}"
    

