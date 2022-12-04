
import pytest
from app import app
from app import get_images
from app import get_raw_text_data
from app import get_extracted_text
from app import process_image

class Tests:

#Valid Function Tests
#-------------------------------------------------------------------
    def test_get_images(self):
        images=get_images()
        assert  len(images)==0

    #get_annotated_images
    def test_get_extracted_text(self):
        text=get_extracted_text(textTxt.txt)
        assert isinstance(text,str)
   


#Invalid Function sTests
#-------------------------------------------------------------------

    def test_get_extracted_text(self):
        insert=get_raw_text_data()
        text=get_extracted_text(insert)
        assert text==None

   #Process image-no image error
    def test_process_image(self):
        text= process_image()
        assert text==None

#Handle Route Tests
#------------------------------------------------------------------
    #ROUTE: (valid) route handler for GET request to '/process'
    def test_process_get(self):
         url='/'
         client = app.test_client()
         response = client.get(url)
         assert response.status_code==200

    #ROUTE: (invalid) route handler for GET request to '/'
    def test_invalid_route(self):
        url='/process'
        client = app.test_client()
        response = client.get(url)
        assert response.status_code==404
        
#----------------------------------------------------------------
    


