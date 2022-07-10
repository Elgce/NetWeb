from sre_constants import SUCCESS
from types import NoneType
from flask import Flask, request, abort, send_file, g, session
from time import time
import os

flux = 0

app = Flask(__name__, static_folder="./dist/", static_url_path="/")
# app.config['SECRET_KEY'] = os.urandom(24)

@app.route("/")
def index():
    return send_file("./dist/index.html")

@app.route("/api/")
def api_hello():
    return "hello api"

@app.route("/api/flux")
def add_flux():
    global flux
    flux = flux + 0.25
    return {"flux": flux}

if __name__=="__main__":
    app.run(debug=True, port=5000)