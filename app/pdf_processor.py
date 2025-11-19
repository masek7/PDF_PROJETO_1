from pathlib import Path
import pymupdf




arquivo = input("Digite aqui o caminho para o PDF:")

caminho_path = Path(arquivo)

if caminho_path.suffix == '.pdf':
    doc = pymupdf.open(caminho_path)
    #print(doc.page_count)



    text_page = doc.get_page_text(0)  # Extrai todo o texto da pagina especifica

    #print(text_page)

    procurado = text_page.find("n.")  # Procura o índice da primeira ocorrencia de Nº
    procurado2 = text_page.rfind("TOTAL R")  # Procura o índice da ultima ocorrencia de Nº
    #print(procurado)

    nf = text_page[procurado: procurado + 13]  # A partir do índice encontrado na variável procurado, ele extrai até o décimo 15 a mais. Ou seja, procurado + 15.
    valor = text_page[procurado2: procurado2 + 15]
    print(nf.replace(" ", ""))
    print(valor.replace(" " "\n", ""))

    doc.close()
else:
    print("Por favor, insira um arquivo pdf")