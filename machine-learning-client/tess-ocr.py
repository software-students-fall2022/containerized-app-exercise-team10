from pytesseract import image_to_string
from PIL import Image

image_path = "handwriting-sample-1.jpeg"
image = Image.open(image_path)
image.load()
print(image_to_string(image))
