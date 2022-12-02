from flask import Flask, jsonify, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
import pymongo
from pymongo import MongoClient
import os
import glob
import requests

UPLOAD_FOLDER = './'
app = Flask(__name__)
UPLOAD_FOLDER = os.getcwd()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.urandom(24)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                         authSource="admin")
    db = client["animal_db"]
    return db

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        print('test')
        return render_template('index.html')
    #new extracted_text collection in db
    db = get_db()
    extrColl = db['extracted_text']
    # dic = {'test': 1}
    # extrColl.insert_one(dic)
    
    print(db.list_collection_names())

    f = request.files['file']
    f.save(secure_filename(f.filename))
    print(f, 'files saved')

    # from flask docs on file uploading
    # files = request.files['file']
    # files.save(secure_filename(files.filename))
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            print("hi")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("image uploaded")
            send_image("http://localhost:5002/process")
            print("here")
            return  render_template('result.html')# TODO: this is just temporary
    return render_template('result.html')

# @app.route('/send_image')
def send_image(url_link):
    images = glob.glob("*.jpg") + glob.glob("*.png") + glob.glob("*.jpeg")
    payload = {"image": images[0]}
    response = requests.post(url_link, files=payload)

# SAMPLE CODE
@app.route('/animals')
def get_stored_animals():
    db=""
    try:
        db = get_db()
        _animals = db.animal_tb.find()
        animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
        return jsonify({"animals": animals})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

if __name__=='__main__':
    app.run(host="localhost", port=5000)