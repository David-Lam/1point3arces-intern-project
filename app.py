from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_pyfile("config.py")


@app.route("/")
def index():
    return ("Avaible api: /posts; /messages; /login/{username}/{password}; /logout; /register/{username}/{password}/{email}")


api = Api(app)
database = SQLAlchemy(app)
ma = Marshmallow(app)
loginManger = LoginManager(app)
mail = Mail(app)


