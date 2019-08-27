

from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


app.config['SECRET_KEY'] = '5bcc0f9e34c15efa9fefb136c16730ec'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from flaskblog import routes