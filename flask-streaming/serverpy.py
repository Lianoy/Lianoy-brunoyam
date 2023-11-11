from flask import Flask, render_template, request

import dbclasses

app = Flask(__name__)

@app.route("/genre", methods = ["GET", "POST"])
def genre_p():
    message_true = ''
    message_fail = ''
    if request.method == "POST":
        data = request.form
        # action = data['action'].split()
        if dbclasses.addGenre(data['name']):
            message_true = f"Жанр {data['name']} успешно добавлен."
        else:
            message_fail = f'''Жанр {data['name']} уже существует.'''
        # elif data['edit'] != None:
        #     dbclasses.editGenre(data['edit'])
        # elif data['delete'] != None:
        #     dbclasses.deleteGenre(data['delete'])
        # return render_template("genre.html", genres = dbclasses.GenreList(), messages=message)
    return render_template("genre.html", genres = dbclasses.GenreList(), message_add=message_true, message_fail = message_fail)

# @app.route("/")
# def index():
#     res = getItem()
#     return render_template("index.html", a = res)

# @app.route("/main")
# def main():
#     return render_template("main.html")

# @app.route("/signin", methods = ["GET","POST"])
# def signin():
#     if request.method == "POST":
#         data = request.form
#         if getUser(data["login"],data['psw']):
#             return f"Привет, {data['login']}"
#         else:
#             return "Нет такого пользователя"
#     return render_template("signin.html")

# @app.route("/register")
# def register():
#     return render_template("register.html")

app.run (debug=True, host="0.0.0.0",port = "9080")