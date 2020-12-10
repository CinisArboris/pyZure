import os
import sys
import requests
from io import BytesIO
from time import sleep


endpoint = "default"
subscription_key = "default"

analyze_url = endpoint + "vision/v2.0/ocr?language=unk&detectOrientation=true"

image_data = {"url":"https://support.discord.com/system/photos/3602/4079/7511/dan.png"}

headers = {'Ocp-Apim-Subscription-Key': subscription_key,'Content-Type': 'application/json'}
params = {'visualFeatures': 'Categories,Description,Color'}

response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
sleep(3)
response.raise_for_status()

analysis = response.json()
print(analysis)
