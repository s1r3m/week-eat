import os

APP_HOST = os.environ.get('APP_HOST', 'localhost:8000')
APP_URL = os.environ.get(f'http://{APP_HOST}')
