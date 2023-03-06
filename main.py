
from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def a():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    try:
        f = request.files['file']
        path = "C:/Users/User/Downloads/AllYandexTasks-image_mars/AllYandexTasks-image_mars/static/img/image.jpg"
        f.save(path)
        htm = f"""<!doctype html>
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
                        <h1>Загрузка фотографии</h1>
                          <h2>для участия в миссии </h2>
                        <div class= "form-control">

                          <form class="login_form" method="post" enctype="multipart/form-data">
                          <p>Приложите фотографию</p>
                            
                          <input type="file" class="form-control-file" id="photo" name="file">
                          <br>
                          <img src = "{url_for('static', filename='img/image.jpg')}" alt="awdad" width="150" height="200">
                          <br>
                          <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </form>
                        </div>
                        
                      </body>
                    </html>
    """

    except Exception:
        print("FUCK")
        htm = f"""<!doctype html>
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
                        <h1>Загрузка фотографии</h1>
                          <h2>для участия в миссии </h2>
                        <div class= "form-control">

                          <form class="login_form" method="post" enctype="multipart/form-data">
                          <p>Приложите фотографию</p>
                            
                          <input type="file" class="form-control-file" id="photo" name="file">
                          <img alt="awdad">
                          <br>
                          <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </form>
                        </div>
                        
                      </body>
                    </html>
"""

    return htm


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

