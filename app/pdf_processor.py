from pathlib import Path
import pymupdf as fitz
from PIL import Image
import io
import pytesseract


def process_pdf(pdf_file):

    #funcao que processa o pdf e extrai o texto da primeira pagina
    read_pdf = pdf_file.read()

    try:
        doc = fitz.open(stream= read_pdf, filetype="pdf")
        page = doc.load_page(0)  # Carrega a primeira página (índice 0)
        text_content = page.get_text()  # Extrai todo o texto da pagina especifica


        if len(text_content.strip()) == 0:
            for page in doc:
                zoom = 3.0
                matriz = fitz.Matrix(zoom, zoom)
                pix = page.get_pixmap(matrix=matriz)
                #converte para pillow image
                img_data = pix.tobytes("png")
                image = Image.open(io.BytesIO(img_data))
                ocr_text = pytesseract.image_to_string(image, lang='por')
                text_content += ocr_text + "\n"
            return {
                "status": "success",
                "filename": pdf_file.name,
                "content": text_content
            }
        else:

            return {
                "status": "success",
                "filename": pdf_file.name,
                "content": text_content
            }

    except Exception as e:
        return {
            "status": "error",
            "filename": getattr (pdf_file, 'name', 'desconhecido'),
            "message": str(e)
        }
        
       
    
