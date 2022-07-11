from types import NoneType
from flask import Flask, jsonify, request, abort, send_file, g, session
from time import time
import os

user_info = {
    "lizy14":{
        "login": False,
        "passwd": "123456",
        "flux": 0,
    },
    "bqw20":{
        "login": False,
        "passwd": "123456",
        "flux": 0,
    }
}

app = Flask(__name__, static_folder="./dist/", static_url_path="/")
# app.config['SECRET_KEY'] = os.urandom(24)
app.secret_key = "bqw123"
@app.route("/")
def index():
    return send_file("./dist/index.html")

@app.route("/api/get_flux")
def get_flux():
    name = session['name']
    flux = user_info[name]['flux']
    return {"flux": flux}

@app.route("/api/")
def api_hello():
    return "hello api"

@app.route("/api/flux")
def add_flux():
    name = session["name"]
    flux = user_info[name]['flux'] + 0.25
    user_info[name]['flux'] += 0.25
    return {"flux": flux}

def get_profile(name):
    return {
        "user_name": name,
        "login": user_info[name]['login'],
        "flux": user_info[name]['flux'],
    }

@app.route("/api/name")
def name():
    name = session.get("name", None)
    return {"user_name": name}

@app.route("/api/login",methods=['GET','POST'])
def log_in():
    name = session.get("name", None)
    if name:
        return get_profile(name)
    else:
        session.clear()
        print("200")
        dat = request.get_data()
        print(dat)
        
        
        print("100")
        name = dat.get("uname")
        print(name)
        passwd = dat["passwd"]
        if name in user_info.keys() and user_info[name]["passwd"] == passwd:
            session['name'] = name
            user_info[name]['login'] = True
            return get_profile(name)
        else:
            abort(403)
if __name__=="__main__":
    app.run(debug=True, port=5000)