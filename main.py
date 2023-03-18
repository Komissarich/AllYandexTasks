from flask import Flask
from data import db_session
from data.users import User
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


from requests import get

def main():

    db_session.global_init("db/blogs.db")

    add_jobs()

    app.run()
   




def add_jobs():

    job = User()
    job.surname = "Scott"
    job.name = "Ridley"
    job.age = 21
    job.position = "Captain"
    job.speciality = "research engineer"
    job.address = "module_1"
    job.email = "scott_chief @ mars.org"

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






if __name__ == '__main__':
    main()
