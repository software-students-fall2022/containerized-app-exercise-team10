# import handprint
from PIL import Image
from flask import Flask, request
import requests 
import os 
import glob

app = Flask(__name__)

def get_images():
    '''function that fetches all images in the current 
    directory 
    TODO: this function will need to be rewritten to fetch
    images from the web application. for now, it is getting the images
    used for testing from the current directory.
    '''
    images = glob.glob("*.jpg") + glob.glob("*.png") + glob.glob("*.jpeg")
    return images

def get_annotated_images():
    '''
    this function retrieves the annontated images returned by
    handprint.
    '''
    images = glob.glob("*-microsoft.png")
    return images

def get_raw_text_data():
    '''
    function returns the text read by handprint
    '''
    text_files =  glob.glob("*-microsoft.txt")
    return text_files 

def print_extracted_text(texts):
    '''
    function prints the text read from handwritten content 
    read by handprint 
    '''
    for text in texts:
        with open(text) as file:
            print(" ".join(file.readlines()))
        file.close()

def delete_process_files():
    '''
    function used to clean the directory from the data output 
    of the tool 
    '''
    curr_dir = os.getcwd()
    files = os.listdir(curr_dir)
    for item in files:
        if item.endswith("-microsoft.txt") or item.endswith("-microsoft.png") or item.endswith("-microsoft.json"):
            os.remove(os.path.join(curr_dir, item))


@app.route('/process', methods=["GET"])
def process():
    if request.method == "GET":
        print(request)
        # TODO: get image from request and save it
        return "received"

    
        # if request.files.get("image"):
        #     # read the image in PIL format
        #     image = request.files["image"].read()
        #     image = Image.open(io.BytesIO(image))
        #     img_str = str(image)

if __name__ == "__main__":    
    # # TODO:  # get image uploaded on the web application  
    # # for now, we're using a sample image from Google 
    # images = get_images() # fetch images in the local directory 
    # # call the tool on the images in the directory 
    # for image in images:
    #     print(image)
    #     os.system("handprint -s microsoft -e " + image)
    # annotated_images = get_annotated_images()
    # # TODO: save annontated imahes somewhere
    # print_extracted_text(get_raw_text_data())
    # delete_process_files()

    app.run(host="0.0.0.0", port=3000)
