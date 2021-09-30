from flask import Blueprint, render_template
from flask_login import login_required, current_user
# views is a Blueprint of our app, meaning it has a roots/urls defined inside it
# so we don't have all of our views in one file, and we can split them up into multiple
# files in an organized way.
views = Blueprint('views', __name__)


@views.route('/')
@login_required  # cannot get to the homepage unless logged in
def home():
    return render_template("home.html")
