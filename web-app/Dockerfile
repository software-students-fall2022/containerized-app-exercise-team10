# base image on required python build
FROM python:3.10.8

EXPOSE 5000

# set working dir within image
WORKDIR /web-app

# copy current dir contents into image dir
ADD . /web-app




# pip install reqs
RUN pip install requests
RUN pip install -r requirements.txt

# run web app
CMD flask run -h 0.0.0.0 -p 5000

# CMD ["flask", "run", "--host=localhost", "--port=5000"]
# EXPOSE 5000