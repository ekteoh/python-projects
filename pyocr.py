import pytesseract
from PIL import Image
Image.open("helloworld.png")
text=pytesseract.image_to_string(Image.open("test.jpg"))

print(text)