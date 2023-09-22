from flask import Flask, render_template, request, jsonify
from database import load_games_from_db, getresult

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    if request.method == "POST":
        data = request.form
        users = getresult(data["search"])
    else:
        users = []

    return render_template("nextpage.html", usr=users)


@app.route("/api/games")
def list_games():
    games = load_games_from_db()
    return jsonify(games)


@app.route("/login")
def login():
    return render_template("signin.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run('localhost', debug=True)
