from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename
import pymongo
from pymongo import MongoClient

UPLOAD_FOLDER = './'
app = Flask(__name__)
app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                         authSource="admin")
    db = client["animal_db"]
    return db

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


    return render_template('result.html')


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
    app.run(host="0.0.0.0", port=5000)