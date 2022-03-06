from urllib import request


import request
import os

API_KEY = os.environ.get('API_KEY')
with open('image1.jpeg', 'r') as file:
    res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/data',
                        data=file,
                        headers={
                            'Content-Type': 'application/cbor',
                            'x-file-name': 'idle.01',
                            'x-label': 'idle',
                            'x-api-key': API_KEY
                        })

    if (res.status_code == 200):
        print('Uploaded file to Edge Impulse', res.status_code, res.content)
    else:
        print('Failed to upload file to Edge Impulse', res.status_code, res.content)