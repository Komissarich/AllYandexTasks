from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('autonom.html', title='Авторизация', form=form)


@app.route('/b')
def b():
    return "fsaedaefawdxcfsfvcbv"


@app.route('/success')
def succes():
    return "Успешно"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')