from flask import Flask, render_template, url_for, request
from data import db_session
from data.jobs import Jobs
from data.users import User
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    login = StringField('Login/email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat Password', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
    
def main():

    #db_session.global_init("db/blogs.db")

   # add_jobs()
   app.run()
   # x = input("Введите бд")
   # print(x)
  #  db_session.global_init(x)
 #   db_sess = db_session.create_session()
   # for user in db_sess.query(User).all():
    #    print(user)
   




def add_jobs():

    job = Jobs()
    job.team_lader = "1"
    job.job = "deployment of residential modules 1 and 2"
    job.work_size = 15
    job.collaborators = "2, 3"
    job.is_finished = False

    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()

    job = User()
    job.surname = "Egor"
    job.name = "Popov"
    job.age = 17
    job.position = "Loh"
    job.speciality = "engineer"
    job.address = "module_2"
    job.email = "scott_egor @ mars.org"

    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()

    job = User()
    job.surname = "Askar"
    job.name = "Kasimov"
    job.age = 17
    job.position = "Manager"
    job.speciality = "noname"
    job.address = "module_3"
    job.email = "scott_askar @ mars.org"


    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()

    job = User()
    job.surname = "Danil"
    job.name = "Mitroshin"
    job.age = 17
    job.position = "Designer"
    job.speciality = "idk"
    job.address = "module_4"
    job.email = "scott_danil @ mars.org"
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()



@app.route("/register")
def register():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('register.html', form=form)
    



if __name__ == '__main__':
    main()
