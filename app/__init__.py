from flask import Flask
from .database import mongo
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'secret key'
app.config.from_object(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/task4_database"
Bootstrap(app)
from . import views
