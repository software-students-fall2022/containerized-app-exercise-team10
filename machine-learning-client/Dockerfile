# base image on required python build
# FROM ubuntu:latest
FROM python:3.10.8

# set working dir within image
WORKDIR /ml-client

# copy current dir contents into image dir
ADD . /ml-client

# ubuntu + tesseract setup
# RUN apt-get -y update
# RUN apt install 
# RUN apt install tesseract-ocr
# RUN apt-get update

# pip install reqs
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN pip install numpy --upgrade

# configure cloud service credentials 
RUN handprint -a microsoft myazurecredentials.json

# run ML app
CMD ["flask", "run", "--host", "localhost"]
EXPOSE 5002