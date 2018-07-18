from flask import Blueprint, render_template
from ..models import User

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/<username>')
def index(username):
    users=User.query.filter_by(username=username).all()
    return render_template('user.html', users=users)

