from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\desardi131\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

image_path = './Ticket-prueba.jpg'

text = pytesseract.image_to_string(Image.open(image_path))

print('Texto extraido: ')
print(text)