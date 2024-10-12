
import requests
import os
from dotenv import load_dotenv

load_dotenv()
FLASK_URL = os.getenv('FLASK_URL')

def send_flask_data(data):
    # Making a POST request
    response = requests.post(FLASK_URL, json=data)

    # Checking the response
    if response.status_code == 200:
        return {'status': 0,
                'message': response.text}
    else:
        return {'status': response.status_code,
                'message': response.text}