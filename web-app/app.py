from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

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
        return render_template('index.html')
    
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