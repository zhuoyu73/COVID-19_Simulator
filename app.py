from flask import Flask, render_template, request
from helpers import todo

app: Flask = Flask(__name__)
todo_list: list[todo] = []
todo_count: int = 0

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/create-game')
def create_game():
    return render_template("create-game.html")

@app.route('/find-your-keys')
def find_your_keys():
    return render_template("find-your-keys.html")

@app.route('/view-todo-list')
def view_todo_list():
    return render_template('view-list.html', todo_list=todo_list)


if __name__ == '__main__':
    app.run(debug=True)