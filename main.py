
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
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='/css/style.css')}" />
                  </head>
                  <body>
                    <h1>Жди нас, Марс </h1>
                    <img src='{url_for('static', filename='/img/mars.jpg')}' alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-dark" role="alert">
                    <p>Человечество вырастает из детства.</p>
                    </div>
                      <div class="alert alert-success" role="alert">
                    <p>Человечеству мала одна планета.  </p>
                    </div>
                     <div class="alert alert-secondary" role="alert">
                    <p>Мы сделаем обитаемыми безжизненные пока планеты. </p>
                    </div>
                    <div class="alert alert-warning" role="alert">
                    <p>И начнем с Марса!</p>
                    </div>
                     <div class="alert alert-danger" role="alert">
                    <p>Присоединяйся! </p>
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
