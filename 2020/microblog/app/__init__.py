from flask import Flask
from config import Config    # импортируем объекты класса Config из модуля config

app = Flask(__name__)
app.config.from_object(Config)  # указываем, что для приложения app переменные конфига мы берем в Config

from app import routes