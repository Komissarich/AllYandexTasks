from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def a():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/choice/<planet_name>')
def choice(planet_name):
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
                    <h1>Мое предложение: {planet_name} </h1>
                      <h2>Эта планета близка к Земле; </h2>
                  
                      <div class="alert alert-success" role="alert">
                    <p>На ней много необходимых ресурсов;  </p>
                    </div>
                     <div class="alert alert-secondary" role="alert">
                    <p>На ней есть вода и атмосфера; </p>
                    </div>
                    <div class="alert alert-warning" role="alert">
                    <p>На ней есть небольшое магнитное поле;</p>
                    </div>
                     <div class="alert alert-danger" role="alert">
                    <p>Наконец, она просто красивая! </p>
                    </div>
                  </body>
                </html>"""

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
