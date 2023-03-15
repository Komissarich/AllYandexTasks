from flask import Flask
from data import db_session
from data.users import User
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    cap = User()
    cap.surname = "Scott"
    cap.name = "Ridley"
    cap.age = 21
    cap.position = "captain"
    cap.speciality = "research engineer"
    cap.address = "module_1"
    cap.email = "scott_chief@mars.org"
    cap.hashed_password = "cap"
    db_sess = db_session.create_session()
    db_sess.add(cap)
    db_sess.commit()


    cap = User()
    cap.surname = "Andrew"
    cap.name = "Bolkonskii"
    cap.age = 21
    cap.position = "engineer"
    cap.speciality = "idk"
    cap.address = "module_2"
    cap.email = "andrew_chief@earth.org"
    cap.hashed_password = "cop"
    db_sess = db_session.create_session()
    db_sess.add(cap)
    db_sess.commit()


    cap = User()
    cap.surname = "Donald"
    cap.name = "Trump"
    cap.age = 21
    cap.position = "president"
    cap.speciality = "lol"
    cap.address = "module_5"
    cap.email = "USA@mars.org"
    cap.hashed_password = "pr"
    db_sess = db_session.create_session()
    db_sess.add(cap)
    db_sess.commit()


    cap = User()
    cap.surname = "Vladimir"
    cap.name = "Lenin"
    cap.age = 21
    cap.position = "Vojd"
    cap.speciality = "communist"
    cap.address = "module_7"
    cap.email = "USSR@mars.org"
    cap.hashed_password = "vo"
    db_sess = db_session.create_session()
    db_sess.add(cap)
    db_sess.commit()

if __name__ == '__main__':
    main()

