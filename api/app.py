from flask import Flask, render_template, request, url_for, flash, redirect, g
import lights
import asyncio
import utilityfunctions

app = Flask(__name__)
app.config['SECRET_KEY'] = '2decf1d53dd9c26c755be2c6702bbfe568f15bab34097cde'
lightList = lights.getAllLightsTest("192.168.254.255")
#commented out for testing when not on a network with lights.
#lightList = asyncio.run(lights.getAllLights("192.168.254.255"))

@app.before_request
def load_navs():
    navlinks = utilityfunctions.parseAppRoutes("./app.py")
    g.navlinks = navlinks

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/lightpanel', methods=('GET', 'POST'))
def lightpanel():
    global navlinks
    if request.method == 'POST':
        for light in lightList:
            input = request.form[f'{light.listNumber}']
            print(input)
            hexColor = input.lstrip('#')
            rgb = utilityfunctions.hexToRGB(hexColor)
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]
            asyncio.run(lights.setLightColor(light.ip, red, green, blue))
    return render_template("lightpanel.html", lightList=lightList)

@app.route('/refreshLights', methods=('GET','POST'))
def refreshLights():
    if request.method == 'POST':
        global lightList 
        lightList = asyncio.run(lights.getAllLights("192.168.254.255"))
    return render_template("refreshLights.html")

if __name__ == "__main__":
    app.run()
