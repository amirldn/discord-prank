from base64 import b64encode
import requests, json
from replit import db

client_id = db['client_id']
url = "https://api.imgur.com/3/image"

def post_image(img_path):
    headers = {
  'Authorization': 'Client-ID '+client_id
}
    files = []
    payload={'image': b64encode(open(img_path, 'rb').read()),
             'type': 'base64'
            }
  
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
  
    if response.status_code == 200:
        return response.json()['data']['link']
    else:
        print(json.dumps(response.json(), indent=4))
        raise Exception("Error: Could not upload image.")