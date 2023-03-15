from . import users
from sqlalchemy import orm
from . import jobs
news = orm.relationship("News", back_populates='user')