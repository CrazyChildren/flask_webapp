import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from main.apps.login import login_bp
from main.config import config

db = SQLAlchemy()
FLASK_ENV = os.getenv("FLASK_ENV")

def creat_app(env_name):
    app = Flask(__name__)

    app.config.from_object(config[env_name]())

    app.register_blueprint(login_bp)

    db.init_app(app)

    return app

app = creat_app(FLASK_ENV)