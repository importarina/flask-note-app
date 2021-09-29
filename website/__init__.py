from flask import Flask
# __init__.py makes the website folder a package.
# that is, wheneber we import website, this file will run automatically
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'random string :P'

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
