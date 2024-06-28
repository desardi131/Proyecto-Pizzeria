from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\desardi131\AppData\Local\Programs\Tesseract-OCR\tesseract.exe' # Colocar siempre para usar tesseract

image_path = './captura.jpg'

text = pytesseract.image_to_string(Image.open(image_path),lang='spa')

print('Texto extraido: ')
print(text)