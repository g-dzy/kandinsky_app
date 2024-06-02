import json
import time
from PIL import Image, ImageDraw, ImageFont
import base64
from PIL import Image
import requests
class Text2ImageAPI:
    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }
    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']
    def generate(self, prompt, model, images=1, width=1200, height=600):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": f"{prompt}"
            }
        }
        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']
    def check_generation(self, request_id, attempts=100, delay=20):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']
            attempts -= 1
            time.sleep(delay)
if __name__ == '__main__':
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', '36155A52222868A23479A9C80B89309A', '326A9D81EE671D18342CDA126CAE4C22')
    model_id = api.get_model()
    a=input("Введите тезис для создания изображения: ")
    uuid = api.generate('high quality,without text,banner:0.7 for add on theme,('+a+')', model_id)
    images = api.check_generation(uuid)
    image_base64 = images[0]
    image_data = base64.b64decode(image_base64)
    with open("image.jpg", "wb") as file:
        file.write(image_data)
    img = Image.open('image.jpg')
    img.show()




