from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
# Connecting our config class and our flask application
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)
