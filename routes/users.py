from flask import Blueprint, render_template, request, redirect, url_for, session as flask_session

from models.userModel import User
from middlewares.auth import login_required


from models import db

users_bp = Blueprint("users", __name__)


@users_bp.route("/home")
@login_required
def home():
    return render_template("Home/index.html")

@users_bp.route("/logout")
def logout():   
    flask_session.clear()
    return redirect(url_for("users.login"))


@users_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            flask_session["user_id"] = user.id
            return redirect(url_for("tasks.task"))
        else:
            error = "Credenciales inválidas"
            return render_template("Auth/login.html", error=error)
    return render_template("Auth/login.html")


@users_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        new_user = User(username=username, email=email, password=password)
        user = User.query.filter_by(email=email).first()
        if user:
            error = "El email ya está en uso"
            return render_template("Auth/register.html", error=error)
        else:
            with db.session() as session:
                session.add(new_user)
                session.commit()    
                # db.session.close()
            return redirect(url_for("users.home"))
    return render_template("Auth/register.html")
