from flask import Blueprint, render_template, request, redirect, url_for,session as flask_session
from models.taskModel import Task

from models import db

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.before_request
def verificar_sesion():
    if flask_session.get("user_id") is None:
        print("Usuario no autenticado. Redirigiendo al login.")
        return redirect(url_for("users.login"))

@tasks_bp.route("/tasks")
def task():
    all_tasks = db.session.query(Task).all()
    return render_template("Home/index.html", tasks=all_tasks)


@tasks_bp.route("/create_task", methods=["GET", "POST"])
def create_task():
    if request.method == "POST":
        title = request.form["title"]
        new_task = Task(title=title)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("tasks.task"))
    return render_template("Home/create.html")


@tasks_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_task(id):
    task = db.session.query(Task).filter(Task.id == id).first()
    if request.method == "POST":
        task.title = request.form["title"]
        db.session.commit()
        return redirect(url_for("tasks.task"))
    return render_template("Home/edit.html", task=task)

@tasks_bp.route("/delete/<int:id>")
def delete_task(id):
    task= db.session.query(Task).filter(Task.id == id).first()
    if task:
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for("tasks.task"))
    return render_template("Home/index.html")