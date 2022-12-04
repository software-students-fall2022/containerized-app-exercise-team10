
import pytest
import io
from app import app
from app import get_images
from app import get_raw_text_data
from app import get_extracted_text
from app import process_image
from app import get_annotated_images


class Tests:

#Valid Function Tests
#-------------------------------------------------------------------
    #Valid get_images test: One file stored in directory
    def test_get_image(self):
        images=get_images()
        assert len(images)==2
        assert images[0]=="testwrite.jpg"
        assert ".jpg" in images[0]
        assert ".png" in images[1]

    #Valid get_raw_text_data test
    def test_get_raw_text_data(self):
        file=get_raw_text_data()
        #Make sure it gets the correct file
        assert "txt" in file
        assert file=='testTxtFile-microsoft.txt'
        assert isinstance(file,str)
    
    #Valid get_annotated_iamges() test
    def test_get_annotated_images(self):
        image=get_annotated_images()
        assert len(image)==1
        assert ".png" in image[0]
        assert "testImage2-microsoft.png" in image
       
    #Valid get_extracted_text test
    def test_get_extracted_text(self):
        insert=get_raw_text_data()
        text=get_extracted_text(insert)
        assert len(text)!=0
        assert text=="Hi there all"
        assert isinstance(text,str)

    #Valid process_image test
    def test_process_image(self):
        text=process_image()
        assert len(text)!=0
        assert isinstance(text,str)
        
#Invalid Extraction Tests
#-------------------------------------------------------------------
    #Invalid get_images test: Check that other file types not extracted
    def test_invalid_get_image(self):
        images=get_images()
        assert (".txt" in images[0])==False

   #Invalid get_raw_text_data test: Checks that only text file is extracted 
    def test_invalid_get_raw_text_data_invalid(self):
        file=get_raw_text_data()
        assert (".jpg" in file)==False
   

#Handle Route Tests
#------------------------------------------------------------------
    #ROUTE: (valid) route handler for GET request to '/'
    def test_get(self):
         url='/'
         client = app.test_client()
         response = client.get(url)
         assert response.status_code==200

    #ROUTE: (invalid) route handler for GET request to '/process' which does not exist
    def test_invalid_route(self):
        url='/process'
        client = app.test_client()
        response = client.get(url)
        assert response.status_code==404


    #ROUTE: (valid) route handler for GET request to '/'
    #Test with file sent and no file sent
    def test_post(self):
        file = "testwrite.jpg"
        data = {
        'image': (open(file, 'rb'), file)
    }
        url='/'
        client = app.test_client()
        response = client.post(url,data=data)
        assert response.status_code == 400
        #No file sent
        response = client.post(url,data=None)
        assert response.status_code == 400

   

   