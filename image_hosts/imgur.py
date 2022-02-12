import os
from base64 import b64encode

import requests, json
client_id = os.environ['client_id']
client_secret = os.environ['client_secret']

url = "https://api.imgur.com/3/image"
headers = {
'Authorization': 'Client-ID '+ client_id
}



def post_image(img_path):
    files = []
    data = {
        'key': client_secret,
        'image': b64encode(open(img_path, 'rb').read()),
        'type': 'base64',
        'name': '1.jpg',
        'title': 'Picture no. 1'
    }
    response = requests.request("POST", url, headers=headers, data=data, files=files)
    # print(json.dumps(response.json(), indent=4))
    if response.status_code == 200:
        return response.json()['data']['link']
    else:
        print(json.dumps(response.json(), indent=4))
        raise Exception("Error: Could not upload image.")