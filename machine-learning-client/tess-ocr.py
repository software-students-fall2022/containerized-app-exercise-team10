from pytesseract import image_to_string
from PIL import Image


def get_text_from_image(img_path):
    image = Image.open(image_path)
    # load image 
    image.load()
    return image_to_string(image)


if __name__ == "__main__":
    # TODO:  # get image uploaded on the web application  
    # for now, we're using a sample image from Google 
    image_path = "handwriting-sample-1.jpeg"
    print(get_text_from_image(image_path))

