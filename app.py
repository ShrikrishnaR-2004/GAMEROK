from flask import Flask,render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'gamelist'

mysql = MySQL(app)

@app.route("/")
def home():
  return render_template("index.html")
def getusers(search):
  conn = mysql.connect('MYSQL_DB')
  cursor = conn.cursor()
  cursor.execute(
    "SELECT * FROM games WHERE games.Game_Name LIKE ? ",("%"+search+"%")
  )
  results = cursor.fetchall()
  conn.close()
  return results


@app.route("/", methods=["GET", "POST"])
def index():
  # (C1) SEARCH FOR USERS
  if request.method == "POST":
    data = dict(request.form)
    users = getusers(data["search"])
  else:
    users = []

  # (C2) RENDER HTML PAGE
  return render_template("nextpage.html", usr=users)


# (D) START
if __name__ == "__main__":
  app.run('localhost', 3306)