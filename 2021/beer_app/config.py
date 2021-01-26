import os

beer_base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY =os.environ.get('SECRET_KEY') or 'something_like_secret_word'
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or 'sqlite://' + os.path.join(beer_base_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False