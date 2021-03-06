from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    make_response,
)
from models.user import User
from utils import log


main = Blueprint('user', __name__)


@main.route("/add", methods=['POST'])
def add():
    form = request.form
    u = User.register(form)
    if u is None:
        session['message'] = "Register Failed"
    else:
        session['message'] = "Register Done"
    return redirect(url_for('welcome.welcome'))
