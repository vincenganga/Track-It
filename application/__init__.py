from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Configure application
app = Flask(__name__)

# Configure the Database for security purposes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SECRET_KEY'] = 'qsdfgbnmbvcxz12378945bgy789WESVCX'


# Configure Database
db = SQLAlchemy(app)

from application import routes