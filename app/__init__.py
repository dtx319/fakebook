from flask import Flask
from config import Config

app = Flask(__name__)

# Connecting our config class and our flask application
app.config.from_object(Config)

from app import routes