import pytesseract
from PIL import Image, ImageDraw

# 1. Cria uma imagem branca com texto preto (simulando um PDF)
img = Image.new('RGB', (200, 50), color=(255, 255, 255))
d = ImageDraw.Draw(img)
d.text((10, 10), "Teste Zorin OS", fill=(0, 0, 0))

# 2. Tenta ler usando o Tesseract
try:
    texto = pytesseract.image_to_string(img)
    print(f"Sucesso! O Tesseract leu: '{texto.strip()}'")
except Exception as e:
    print(f"Erro: {e}")