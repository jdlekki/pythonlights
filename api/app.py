from flask import Flask, render_template, request, url_for, flash, redirect
import lights
import asyncio

app = Flask(__name__)
app.config['SECRET_KEY'] = '2decf1d53dd9c26c755be2c6702bbfe568f15bab34097cde'

lightList = asyncio.run(lights.getAllLights("192.168.254.255"))


@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template("home.html", name=name)

@app.route("/allLights", methods=('GET', 'POST'))
def allLights():
    if request.method == 'POST':
        for light in lightList:
            input = request.form[f'{light.listNumber}']
            print(input)
            hexColor = input.lstrip('#')
            rgb = hexToRGB(hexColor)
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]
            asyncio.run(lights.setLightColor(light.ip, red, green, blue))
    return render_template("lightlist.html", lightList=lightList)

@app.route("/color")
def color():
    colorString = request.args.get('color', '')
    return render_template('color.html', colorString=colorString)

def hexToRGB(hex):
    rgb = []
    for i in (0, 2, 4):
        decimal = int(hex[i:i+2], 16)
        rgb.append(decimal)
    return tuple(rgb)