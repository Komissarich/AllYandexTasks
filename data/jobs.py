import datetime
import sqlalchemy
from sqlalchemy import orm
import sqlalchemy_serializer
from .db_session import SqlAlchemyBase
import flask_login
class Jobs(SqlAlchemyBase,flask_login.UserMixin, sqlalchemy_serializer.SerializerMixin):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.id"))
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)

