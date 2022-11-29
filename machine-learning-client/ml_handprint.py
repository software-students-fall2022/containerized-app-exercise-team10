import handprint
from PIL import Image
import os 
import glob

def get_images():
    # get all the images in the working directory
    images = glob.glob("*.jpg") + glob.glob("*.png") + glob.glob("*.jpeg")
    return images

def get_annotated_images():
    images = glob.glob("*-microsoft.png")
    return images

def get_raw_text_data():
    text_files =  glob.glob("*-microsoft.txt")
    return text_files 


def delete_process_files():
    curr_dir = os.getcwd()
    files = os.listdir(curr_dir)
    for item in files:
        if item.endswith("-microsoft.txt") or item.endswith("-microsoft.png") or item.endswith("-microsoft.json"):
            os.remove(os.path.join(curr_dir, item))

if __name__ == "__main__":    
    # TODO:  # get image uploaded on the web application  
    # for now, we're using a sample image from Google 
    images = get_images()
    for image in images:
        os.system("handprint -s microsoft -e " + image)

    annotated_images = get_annotated_images()
    texts = get_raw_text_data()
    delete_process_files()
