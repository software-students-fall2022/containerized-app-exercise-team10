from flask import Flask, request,render_template, redirect, flash
from pymongo import MongoClient
import os, glob, requests, sys
from werkzeug.utils import secure_filename
# from PIL import Image
# import pymongo
# import handprint




################## setup ##################
app = Flask(__name__)
UPLOAD_FOLDER = os.getcwd()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.urandom(24)
# app.config['MONGO_URI'] = 'mongodb://db:27017/project4'

def get_db():
    client = MongoClient(host='db', port=27017)
    return client

def allowed_file(filename):
    '''
    check for allowed extensions
    '''
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


################## Handprint functions ##################
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
    return text_file[0]

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

def delete_process_files(filename):
    '''
    function used to clean the directory from the data output 
    of the tool 
    '''
    curr_dir = os.getcwd()
    files = os.listdir(curr_dir)
    for item in files:
        if  item.endswith("-microsoft.txt") or \
            item.endswith("-microsoft.png") or \
            item.endswith("-microsoft.json") or \
            item.endswith(filename):
            os.remove(os.path.join(curr_dir, item))

def process_image():
    images = get_images()

    for image in images:
        #     print(image)

        print("handprint -s microsoft -e " + image, file=sys.stderr)

        # run handprint
        os.system("handprint -s microsoft -e " + image)

        # annotated_images = get_annotated_images()
        # # TODO: save annontated imahes somewhere

        text = get_extracted_text(get_raw_text_data())

        # delete_process_files()
        return text
    



################## routes ##################
@app.route('/', methods=['GET','POST'])
def process():
    if request.method == "GET":
        return render_template('index.html')


    #     print(request, file=os.stderr)
    #     # TODO: get image from request and save it
    #     return "received"
    



    if request.method == "POST":
         # check that file exists
        if 'file' not in request.files:
            redirect('/')
        
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect('/')

        if file and allowed_file(file.filename):
            # save file
            filename = secure_filename(file.filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(filename)

            # get text 
            text = process_image() 
            
            # db connection
            client = get_db()
            db = client['project4']

            # insert text into db
            id = db.images.insert_one({
                'img_text' : text
            }).inserted_id

            print(db.images.find_one({'_id' : id} ), file=sys.stderr)
            print("here", file=sys.stderr)
            print(f'id:{id}', file=sys.stderr)
            print(db.list_collection_names(), file=sys.stderr)

            delete_process_files(filename) # delete uploaded images 

            client.close()
            
            # go to web app for displaying results
            return redirect(f'http://localhost:3000/results?id={id}')


# run server
if __name__ == "__main__":    
    app.run(host="0.0.0.0", port=3002)
