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

@app.route('/i-or-p-less-than-0')
def i_or_p_less_than_0():
    return render_template("i-or-p-less-than-0.html")

@app.route('/s-less-than-0')
def s_less_than_0():
    return render_template("s-less-than-0.html")

@app.route('/s-more-than-0')
def s_more_than_0():
    return render_template("s-more-than-0.html")

@app.route('/i-or-p-more-than-100')
def i_or_p_more_than_100():
    return render_template("i-or-p-more-than-100.html")

@app.route('/w-less-than-0')
def w_less_than_0():
    return render_template("w-less-than-0.html")

@app.route('/w-more-than-100')
def w_more_than_100():
    return render_template("w-more-than-100.html")

@app.route('/nothing')
def nothing():
    return render_template("nothing.html")

if __name__ == '__main__':
    app.run(debug=True)