
import pytest
import os
from app import app
from app import get_images
from app import get_raw_text_data
from app import get_extracted_text
from app import process_image

class Tests:

#Valid Function Tests
#-------------------------------------------------------------------
    #Valid get_images test: Two files stored in directory
    def test_get_image(self):
        images=get_images()
        assert len(images)==1

    #Valid get_raw_text_data test
    def test_get_raw_text_data(self):
        file=get_raw_text_data()
        #Make sure it gets the file
        assert file=='testTxtFile-microsoft.txt'
        assert isinstance(file,str)
    
    #Valid get_extracted_text test
    def test_get_extracted_text(self):
        insert=get_raw_text_data()
        text=get_extracted_text(insert)
        assert text=="Hi there all"
        assert isinstance(text,str)


#NEED TO GET TEXT FROM AN ACTUAL IMAGE
    #Valid process image
    def test_process_image(self):
        text=process_image()
        assert isinstance(text,str)
        
#Invalid Function sTests
#-------------------------------------------------------------------
   
   #Invalid get_raw_text_data test: Checks for incorrect file
    def test_get_raw_text_data_invalid(self):
        file=get_raw_text_data()
        assert (file=='testTxtFile.txt')==False
   #Process image-no image error
   

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
    


