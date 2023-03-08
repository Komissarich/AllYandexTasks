from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def a():
    return "Миссия Колонизация Марса"


@app.route('/index/<letter>')
def index(letter):
    return render_template('base.html', title= letter)


@app.route('/training/<specialization>')
def prof(specialization):
    if 'инженер' in specialization:
        return render_template('prof.html', title=specialization, prof='Инженерный симулятор', path="/static/img/eng.jpg")
    elif 'строитель' in specialization:
        return render_template('prof.html', title=specialization, prof="Строительный симулятор", path="/static/img/builder.jpg")
    else:
        return render_template('prof.html', title=specialization, prof="Научный симулятор", path="/static/img/science.jpg")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
