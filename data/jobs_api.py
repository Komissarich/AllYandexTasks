import flask
from requests import get
from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs/<int:job_id>')
def get_news(job_id):
    print(1)
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).get(job_id)
    if not news:
        return flask.jsonify({'error': 'Not found'})
    return flask.jsonify(
        {
            'jobs': news.to_dict(only=(
                'id', 'name', 'work_size', 'collaborators'))
        }
    )

