import os
from replit import db
from base64 import b64encode

import requests, json
api_key = db["imgbb_api_key"]
url = "https://api.imgbb.com/1/upload"



def post_image(img_path):
    data = {
        'key': api_key,
        'image': b64encode(open(img_path, 'rb').read()),

    }
    response = requests.request("POST", url, data=data)
    # print(json.dumps(response.json(), indent=4))
    if response.status_code == 200:
        return response.json()['data']['display_url']
    else:
        print(json.dumps(response.json(), indent=4))
        raise Exception("Error: Could not upload image.")