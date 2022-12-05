from flask          import Flask, jsonify, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from pymongo        import MongoClient
from bson.objectid  import ObjectId
import os, sys
import gridfs
import glob 
import shutil


################## setup ##################
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://db:27017/project4'
app.secret_key = os.urandom(24)
UPLOAD_FOLDER = './'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

client = MongoClient(host='db',
                         port=27017)
                         
def get_db(client):
    try:
        # verify the connection works by pinging the database
        # The ping command is cheap and does not require auth.
        client.admin.command('ping')
        # if we get here, the connection worked!
        print(' *', 'Connected to MongoDB!',file=sys.stderr)
    except Exception as e:
        # the ping command failed, so the connection is not available.
        # render_template('error.html', error=e) # render the edit template
        print(' *', "Failed to connect to MongoDB")
        return
    db = client.project_four
    return db

def download_image_from_db(db, img_doc):
    '''
    download image saved into the MongoDB database 
    using GridFS and return the path of the saved image
    '''
    fs = gridfs.GridFS(db)
    data = db.fs.files.find_one({'filename': img_doc['filename']})
    my_id = data['_id']
    output_data = fs.get(my_id).read()
    output = open(UPLOAD_FOLDER + 'web-app/static/images/' +img_doc['filename'], "wb")
    output.write(output_data)
    output.close()
    print("download_completed", file=sys.stderr)
    images = glob.glob("*.png")

    return UPLOAD_FOLDER + 'web-app/static/images/' +img_doc['filename']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


################## routes ##################
@app.route('/', methods=['GET', 'POST'])
def homepage():
   return redirect("http://localhost:3002/")


@app.route('/results')
def results(testing=False):
    db = get_db(client)

    id = request.args.get('id')

    img_doc = db.images.find_one(
        {'_id' : ObjectId(id)}
    )

    # print(f'id:{id}', file=sys.stderr)
    # print(img_doc, file=sys.stderr)
    if not testing:
        filename = download_image_from_db(db, img_doc)

    return render_template('results.html', extracted_text=img_doc['img_text'], image_filename=img_doc['filename'])


################## run server ##################
if __name__=='__main__':
    app.run(host="0.0.0.0", port=3000)