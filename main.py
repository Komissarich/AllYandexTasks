
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def a():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/image_mars')
def promotion():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  </head>
                  <body>
                    <h1>Жди нас, Марс </h1>
                    <img src='{url_for('static', filename='/img/mars.jpg')}' alt="здесь должна была быть картинка, но не нашлась">
                    <p>Вот она какая, красная планета</p>
                    
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
