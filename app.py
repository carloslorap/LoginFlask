from flask import Flask
from models import db
from models.userModel import User
from routes.users import users_bp
from routes.task import tasks_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = "123412341234124123"
db.init_app(app)
app.register_blueprint(users_bp)
app.register_blueprint(tasks_bp)

# app.before_request()
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)