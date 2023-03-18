import flask
from requests import get
from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_news():
    print(1)
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()

    return flask.jsonify(
        {
            'jobs':
                [item.to_dict(only=('id', 'name', 'work_size', 'collaborators'))
                 for item in news]
        }
    )

