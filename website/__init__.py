from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


# __init__.py makes the website folder a package.
# that is, wheneber we import website, this file will run automatically
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'random string :P'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # this is the flask app we are gonna use with this database
    db.init_app(app)

    from .api.views import views
    from .api.auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    from .api.models import User, Note
    create_database(app)
    login_manager = LoginManager()
    # when log in is required:
    login_manager.login_view = 'auth.login'
    # tell login manager which app we are using
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
