from flask import Flask
from data import db_session, jobs_api
from data.jobs import Jobs
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
import sqlalchemy_serializer

from requests import get

def main():

    db_session.global_init("db/blogs.db")
    app.register_blueprint(jobs_api.blueprint)
    add_jobs()

    app.run()
    #print(get('http://localhost:5000/api/jobs').json())




def add_jobs():
    job = Jobs()
    job.name = "Программирование"
    job.work_size = 10
    job.collaborators = "Egor"

    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()

    job = Jobs()
    job.name = "Инженерия"
    job.work_size = 50
    job.collaborators = "Danil"

    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()

    job = Jobs()
    job.name = "Вождение"
    job.work_size = 1
    job.collaborators = "Mark"

    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()

    job = Jobs()
    job.name = "Экспериментирование"
    job.work_size = 100
    job.collaborators = "Askar"

    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()

    for user in db_sess.query(Jobs).all():
        print(user.name)





if __name__ == '__main__':
    main()
