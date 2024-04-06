from flask import Flask
from flask import render_template
from flask import request
import lights
import asyncio

app = Flask(__name__)

@app.route("/")
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template("home.html", name=name)

@app.route("/getLights")
def getLights():
    lightList = asyncio.run(lights.getAllLights("192.168.254.255")) 
    return render_template("lightlist.html", lightList=lightList)

@app.route("/color")
def color():
    colorString = request.args.get('color', '')
    return render_template('color.html', colorString=colorString)