from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def a():
    return "Миссия Колонизация Марса"


@app.route('/index/<letter>')
def index(letter):
    return render_template('base.html', title= letter)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
