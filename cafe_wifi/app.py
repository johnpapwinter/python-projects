from flask import Flask
from flask_cors import CORS
from db import db

from api import blp as CafeBlueprint

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'

app.register_blueprint(CafeBlueprint)

db.init_app(app)
cors = CORS(app)


