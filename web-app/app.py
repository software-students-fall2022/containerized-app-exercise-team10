from flask import Flask, jsonify, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo
import os, glob, requests, sys
from bson.objectid import ObjectId



# setup
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://db:27017/project4'
app.secret_key = os.urandom(24)

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
    db = client.project_four
    print(db.list_collection_names(), sys.stderr)
    return db


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    


# routes
@app.route('/', methods=['GET', 'POST'])
def homepage():
    # GET
    # if request.method == 'GET':
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


    # POST
    # if request.method == 'POST':
        # check that file exists
        # if 'file' not in request.files:
        #     redirect('/')

        # # connect to db
        # images_db = get_db()['images']

        # print('posted from homepage', file=sys.stderr)

        # image = request.files['file']
        # oid = images_db.insert_one(
        #     {
        #         'img_original'       : image.read(),
        #         'img_original_name'  : secure_filename(image.filename),
        #         'img_annotated'      : 'init',
        #         'img_annotated_name' : 'init',
        #         'img_text'           : 'init'
        #     }
        # ).inserted_id

        # # send to ml client for processing    
        # requests.get('http://ml-client:3000/process', params={'oid' : oid})

        # # get images again after processing is done
        # updated_img = images_db.find_one({'_id' : oid})


        # img = Image.open(io.BytesIO(updated_img['img_original']))


        # return render_template(
        #     'results.html') 
            # img_text=updated_img['img_text'], 
            # img_original_name=updated_img['img_original_name'],
            # image=img)

    # if request.method == 'GET':
    #     print('test')
    #     return render_template('index.html')
    # # #new extracted_text collection in db
    # # db = get_db()
    # # extrColl = db['extracted_text']
    # # # dic = {'test': 1}
    # # # extrColl.insert_one(dic)
    
    # # print(db.list_collection_names())

    # # f = request.files['file']
    # # f.save(secure_filename(f.filename))
    # # print(f, 'files saved')

    # # # from flask docs on file uploading
    # # files = request.files['file']
    # # files.save(secure_filename(files.filename))
    # if request.method == 'POST':
    #     # check if the post request has the file part
    #     if 'file' not in request.files:
    #         flash('No file part')
    #         return redirect(request.url)
    #     file = request.files['file']
    #     # if user does not select file, browser also
    #     # submit an empty part without filename
    #     if file.filename == '':
    #         flash('No selected file')
    #         print("hi")
    #         return redirect(request.url)
    #     if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #         flash("image uploaded")
    #         # send_image("http://ml-client:3000/process")
    #         # print("here")
    #         return render_template('results.html')# TODO: this is just temporary
    # return render_template('result.html')







# # @app.route('/send_image')
# def send_image(url_link):
#     images = glob.glob("*.jpg") + glob.glob("*.png") + glob.glob("*.jpeg")
#     payload = {"image": images[0]}
#     response = requests.post(url_link, files=payload)





# # SAMPLE CODE
# @app.route('/animals')
# def get_stored_animals():
#     db=""
#     try:
#         db = get_db()
#         _animals = db.animal_tb.find()
#         animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
#         return jsonify({"animals": animals})
#     except:
#         pass
#     finally:
#         if type(db)==MongoClient:
#             db.close()





# run server
if __name__=='__main__':
    app.run(host="0.0.0.0", port=3000)