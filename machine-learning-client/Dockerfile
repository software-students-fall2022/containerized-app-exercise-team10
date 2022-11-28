# FROM ubuntu:latest
FROM python:3.10.8

WORKDIR /ml-client
ADD . /ml-client
# RUN apt-get -y update
# RUN apt install 
# RUN apt install tesseract-ocr

RUN apt-get update

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install numpy --upgrade
RUN handprint -a microsoft myazurecredentials.json 

