from flask import Flask
# Импортируем файл конфигурации
from config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)