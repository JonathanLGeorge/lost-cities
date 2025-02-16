from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config import Config
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
api = Api(app)

# Enable CORS
# if app.env == 'production':
#     CORS(app, origins=["https://DOMAIN.com", "https://www.DOMAIN.com"])
# else:
CORS(app)

db.init_app(app)

from src.models import *
from src.resources.game import Game, GameList

# Examples
api.add_resource(GameList, '/games')
api.add_resource(Game, '/games/<int:pid>')
