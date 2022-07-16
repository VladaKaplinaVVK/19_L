from flask import Flask
from flask_restx import Api
from dao.model.user import User

from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.user import user_ns
from views.auth import auth_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    # create_data(app, db)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


def create_data(app , db):
    with app.app_context():
        db.create_all()

        u1 = User(username="olga", password="nvdfkjvh", role="user")
        u2 = User(username="oleg", password="yvol", role="admin")

        with db.session.begin():
            db.session.add_all([u1, u2])


app = create_app(Config())


if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
