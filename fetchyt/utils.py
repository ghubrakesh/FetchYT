import os
from dotenv import load_dotenv

load_dotenv()

API_KEYS = [
    os.getenv('API_KEY_1'),
    os.getenv('API_KEY_2'),
    os.getenv('API_KEY_3')
]
