# base image on required python build
FROM python:3.10.8

# expose port 3000 to outside of container
EXPOSE 3002

# set working dir within image
WORKDIR /ml-client

# copy current dir contents into image dir
ADD . /ml-client

# pip install reqs
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install numpy --upgrade
RUN handprint -a microsoft myazurecredentials.json

# run ML app
CMD flask run -h 0.0.0.0 -p 3002