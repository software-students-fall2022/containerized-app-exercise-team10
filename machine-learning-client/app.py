from flask import Flask, request,render_template, redirect, flash
# from PIL import Image
from flask_pymongo import PyMongo
import os, glob, requests
# import handprint
from werkzeug.utils import secure_filename

# setup
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://db:27017/project4'
app.secret_key = os.urandom(24)
client = PyMongo(app)


UPLOAD_FOLDER = os.getcwd()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    '''
    check for allowed extensions
    '''
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



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
    text_file =  glob.glob("*-microsoft.txt")
    return text_file 

def get_extracted_text(text):
    '''
    function prints the text read from handwritten content 
    read by handprint 
    '''
    complete_text = ""
    with open(text) as file:
        complete_text += " ".join(file.readlines())
    file.close()
    return complete_text

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





def process_image():
    images = get_images()

    for image in images:
        #     print(image)
        os.system("handprint -s microsoft -e " + image)
        # annotated_images = get_annotated_images()
        # # TODO: save annontated imahes somewhere
        text = get_extracted_text(get_raw_text_data())
        # delete_process_files()
        return text
    
# routes
@app.route('/', methods=['GET','POST'])
def process():
    if request.method == "GET":
    #     print(request, file=os.stderr)
    #     # TODO: get image from request and save it
    #     return "received"
        return render_template('index.html')
    
    if request.method == "POST":
         # check that file exists
        if 'file' not in request.files:
            redirect('/')    
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print("hi")
            return redirect('/')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(secure_filename(file.filename))
            text = process_image() # get text 
            delete_process_files() # delete uploaded images 
            return  render_template('results.html', extracted_text=text) # TODO: display result in web app instead of here  


# run server
if __name__ == "__main__":    
    app.run(host="0.0.0.0", port=3002)
