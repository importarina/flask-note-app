from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


# __init__.py makes the website folder a package.
# that is, wheneber we import website, this file will run automatically
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'random string :P'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)  # this is the flask app we are gonna use with this database
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    from .models import User, Note
    return app

def create_database(app):
    if not path('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Databae!')
