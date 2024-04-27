import requests

def setLightsOff(url):
    data = {
        "toggle":"off"
        }
    post_response = requests.post(url, json=data)
    post_response_json = post_response.json()
    print(post_response_json)

def setLightsOn(url):
    data = {
        "toggle":"on"
        }
    post_response = requests.post(url, json=data)
    post_response_json = post_response.json()
    print(post_response_json)

