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
from routes import (
    login_required,
    current_user,
)
from utils import log


main = Blueprint('welcome', __name__)


@main.route("/", methods=['GET'])
def welcome():
    u = current_user()
    if u is None:
        username = "Stranger"
    else:
        return redirect(url_for(".index"))
    template = render_template(
        "welcome.html", username=username, message=session.get('message', ''))
    r = make_response(template)
    r.set_cookie('cookie_name', 'RUA')
    return r


@main.route("/login", methods=['POST'])
def login():
    u = User.validate_login(request.form)
    if u is None:
        return render_template("welcome.html", username="Stranger", message="User Not Exist")
    else:
        session["uid"] = u.id
        return redirect(url_for(".index"))


@main.route("/index")
@login_required
def index():
    u = current_user()
    return render_template("index.html", username=u.username)


@main.route("/logout", methods=['POST'])
def logout():
    session.pop("uid")
    return redirect(url_for(".welcome"))
