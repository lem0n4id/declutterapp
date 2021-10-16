from flask import render_template

from flask import Flask, request
app = Flask(__name__)
    
from sawo import createTemplate, verifyToken
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


user_entries=[("Why Web3 Matters?","hashnode.com","2021-10-18","2021-10-16",["Tech","Web3"]),
            ("Make the Most Out of Your Next Migration Project","https://blog.tomaszgil.me/make-the-most-out-of-your-next-migration-project","2021-10-18","2021-10-16",["Tech","Migration"])]

createTemplate("templates/partials", flask=True)

load = ''
loaded = 0


def setPayload(payload):
    global load
    load = payload


def setLoaded(reset=False):
    global loaded
    if reset:
        loaded = 0
    else:
        loaded += 1


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/greet')
def hello():
    return render_template("greetings.html")

@app.route('/details')
def fill_details():
    return render_template("details.html")

@app.route('/home')
def home():
    return render_template("home.jinja2", entries=user_entries)

@app.route('/entry')
def entry():
    return render_template("add_entry.html")

@app.route('/settings')
def settings():
    return render_template("settings.html")

@app.route("/login_page")
def login_page():
    setLoaded()
    setPayload(load if loaded < 2 else '')
    sawo = {
        "auth_key": API_KEY,
        "to": "login",
        "identifier": "email"
    }
    return render_template("login.html", sawo=sawo, load=load)


@app.route("/login", methods=["POST", "GET"])
def login():
    payload = json.loads(request.data)["payload"]
    setLoaded(True)
    setPayload(payload)
    status = 200 if(verifyToken(payload)) else 404
    return {"status": status}

if __name__ == '__main__':
    app.run()