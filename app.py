import os
from flask import Flask, request, redirect, render_template
from lib.database_connection import get_flask_database_connection
from lib.peep_repository import PeepRepository
from lib.user_repository import UserRepository
from lib.user import User

# Create a new Flask app
app = Flask(__name__)


@app.route("/peeps/all", methods=["GET"])
def show_all():
    connection = get_flask_database_connection(app)
    peep_user_repository = PeepRepository(connection)
    peeps = peep_user_repository.all()
    return render_template("peeps.html", peeps=peeps)


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

    user_repository.add(user)
    return redirect("peeps/all")


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))
