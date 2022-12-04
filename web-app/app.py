from flask          import Flask, jsonify, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from pymongo        import MongoClient
from bson.objectid  import ObjectId
import os, sys



################## setup ##################
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://db:27017/project4'
app.secret_key = os.urandom(24)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def get_db():
    client = MongoClient(host='db',
                         port=27017)
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
    db = client.project_four
    print(db.list_collection_names(), sys.stderr)
    return db


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    


################## routes ##################
@app.route('/', methods=['GET', 'POST'])
def homepage():
   return redirect("http://localhost:3002/")


@app.route('/results')
def results():
    db = get_db()
    print(db.list_collection_names())

    id = request.args.get('id')

    img_doc = db.images.find_one(
        {'_id' : ObjectId(id)}
    )

    print(f'id:{id}', file=sys.stderr)
    print(img_doc, file=sys.stderr)
    client.close()

    return render_template('results.html', extracted_text=img_doc['img_text'])


################## run server ##################
if __name__=='__main__':
    app.run(host="0.0.0.0", port=3000)