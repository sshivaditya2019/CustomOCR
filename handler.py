import base64
import io
from PIL import Image
import requests
import pytesseract
import json
import os



def main(evt, ctx):
    request_body = json.loads(evt['body'])
    image = io.BytesIO(base64.b64decode(request_body['image']))
    txt = pytesseract.image_to_string(Image.open(image))
    body = {
        "text": txt
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response