FROM ubuntu:latest
FROM python:3.10.8

WORKDIR /ml-client
ADD . /ml-client
RUN sudo apt install tesseract-ocr
RUN sudo apt install libtesseract-dev

RUN pip install -r requirements.txt

