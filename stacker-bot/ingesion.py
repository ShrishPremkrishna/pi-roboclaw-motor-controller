from urllib import request


import requests
import os

API_KEY = os.environ.get('API_KEY')
with open('image1.jpg', 'r') as file:
    res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/data',
                        data=file,
                        headers={
                            'Content-Type': 'image/jpeg',
                            'x-file-name': 'image1.jpg',
                            'x-label': 'sample',
                            'x-api-key': API_KEY
                        })

    if (res.status_code == 200):
        print('Uploaded file to Edge Impulse', res.status_code, res.content)
    else:
        print('Failed to upload file to Edge Impulse', res.status_code, res.content)