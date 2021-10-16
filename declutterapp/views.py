from declutterapp import app
from flask import config, render_template
    
from sawo import createTemplate, verifyToken
import json

user_entries=[("Why Web3 Matters?","hashnode.com","2021-10-18","2021-10-16",["Tech","Web3"]),
            ("Make the Most Out of Your Next Migration Project","https://blog.tomaszgil.me/make-the-most-out-of-your-next-migration-project","2021-10-18","2021-10-16",["Tech","Migration"])]


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