# base image on required python build
FROM python:3.10.8

# set working dir within image
WORKDIR /app

# copy current dir contents into image dir
ADD . /app

# pip install reqs
RUN pip install requests
RUN pip install -r requirements.txt

# run web app
CMD ['python', 'app.py']