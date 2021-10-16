from declutterapp import app
from flask import render_template

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
    return render_template("home.html")

@app.route('/entry')
def entry():
    return render_template("add_entry.html")

@app.route('/settings')
def settings():
    return render_template("settings.html")