from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config    # импортируем объекты класса Config из модуля config

app = Flask(__name__)
app.config.from_object(Config)  # указываем, что для приложения app переменные конфига мы берем в Config
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models