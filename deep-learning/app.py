import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

a = Image.open('테스트.jpg')
txt = pytesseract.image_to_string(a, lang='kor')

print(txt)