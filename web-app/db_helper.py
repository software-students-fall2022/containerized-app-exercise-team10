import gridfs
UPLOAD_FOLDER = './'
import glob 
import os, sys
def download_image_from_db(db, img_doc, testing=False):
    '''
    download image saved into the MongoDB database 
    using GridFS and return the path of the saved image
    '''
    fs = gridfs.GridFS(db)
    data = db.fs.files.find_one({'filename': img_doc['filename']})
    print(db.fs.files.find({}))
    my_id = data['_id']
    output_data = fs.get(my_id).read()
    output = open(UPLOAD_FOLDER + 'web-app/static/images/' +img_doc['filename'], "wb")
    output.write(output_data)
    output.close()
    print("download_completed", file=sys.stderr)
    images = glob.glob("*.png")

    return UPLOAD_FOLDER + 'web-app/static/images/' +img_doc['filename']