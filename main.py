from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import sys
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

class LoginForm(FlaskForm):
    username = StringField('id астронавта', validators=[DataRequired()])
    password = StringField('Пароль астронавта', validators=[DataRequired()])
    captain_name = StringField('id капитана', validators=[DataRequired()])
    password_captain = StringField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')

@app.route('/')
def a():
    return "Миссия Колонизация Марса"


@app.route('/distribution')
def distribution():
    data = list(map(str.strip, sys.stdin))
    return render_template('distribution.html', user_list = data)



@app.route('/table/<sex>/<int:age>')
def page(sex, age):
    path = ""
    if sex == "female":
        color = [str(age * 10), '0',  '0']
    else:
        color = ['0', '0', str(age * 10)]
    if age >= 21:
        path = "/static/img/elder.png"
    else:
        path = "/static/img/small.jpg"
    #"rgb(210, 0, 0)"
    color = ", ".join(color)
    a = f'rgb({color})'
    print(a)
    return render_template("table.html", colored= a, path = path)


@app.route('/success')
def succes():
    return "Успешно"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
