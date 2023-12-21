import os
from flask import Flask, request, redirect, render_template
from lib.database_connection import get_flask_database_connection
from lib.chant_repository import ChantRepository
from lib.user_repository import UserRepository
from lib.user import User
from flask_wtf.csrf import CSRFProtect


# Create a new Flask app
app = Flask(__name__)
app.config.update(SECRET_KEY="secret_key")
csrf = CSRFProtect()
csrf.init_app(app)


@app.route("/chants/all", methods=["GET"])
def show_all():
    connection = get_flask_database_connection(app)
    chant_user_repository = ChantRepository(connection)
    chants = chant_user_repository.all()
    return render_template("chants.html", chants=chants)


@app.route("/users/get_new_user", methods=["GET"])
def collect_user_info():
    return render_template("add_user.html")


@app.route("/users/add_user", methods=["POST"])
def add_user_to_db():
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)

    email = request.form["email"]
    password = request.form["password"]
    name = request.form["name"]
    username = request.form["username"]

    user = User(None, email, password, name, username)

    user = user_repository.add(user)
    return redirect(f"/users/user_info/{user.id}")


@app.route("/users/user_info/<id>")
def show_user_info(id):
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    user = user_repository.get_user(id)
    return render_template("user_info.html", user=user)


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))
