from app import app
from flask import render_template


@app.route("/")
def hello_world():
    return render_template("main/index.html")


@app.route("/calc/<int:x>/<int:y>/+")
def calc_plus(x, y):
    return render_template("main/calc.html", x=x, y=y, sum=x+y)

@app.route("/calc/<int:x>/<int:y>/-")
def calc_minus(x, y):
    return render_template("main/calc.html", x=x, y=y, sum=x-y)