from flask import Flask, render_template, request

from test import getItem, getUser

app = Flask(__name__)

@app.route("/")
def index():
    res = getItem()
    return render_template("index.html", a = res)

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/signin", methods = ["GET","POST"])
def signin():
    if request.method == "POST":
        data = request.form
        if getUser(data["login"],data['psw']):
            return f"Привет, {data['login']}"
        else:
            return "Нет такого пользователя"
    return render_template("signin.html")

@app.route("/register")
def register():
    return render_template("register.html")

app.run (debug=True, host="0.0.0.0",port = "9080")