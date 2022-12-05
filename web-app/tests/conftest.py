from flask          import Flask, jsonify, render_template, request, redirect, flash
import pytest
import os, sys

def setup():
    app = Flask(__name__)
    app.config['MONGO_URI'] = 'mongodb://db:27017/project4'
    app.secret_key = os.urandom(24)
    UPLOAD_FOLDER = './'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return app

@pytest.fixture
def flask_app():
    app = setup()
    return app
    