import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'something_very_secrets'