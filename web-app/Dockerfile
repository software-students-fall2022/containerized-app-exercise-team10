# base image on required python build
FROM python:3.10.8

# set working dir within image
WORKDIR /web-app

# copy current dir contents into image dir
ADD . /web-app




# pip install reqs
RUN pip install requests
RUN pip install -r requirements.txt

# run web app
CMD ["flask", "run", "--host", "localhost"]

EXPOSE 5000