FROM python:3.10.8
ADD . /app
WORKDIR /app
RUN pip install requests
RUN pip install -r requirements.txt