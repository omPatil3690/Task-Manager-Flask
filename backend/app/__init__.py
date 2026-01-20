from flask import Flask
from .extensions import db

def create_app():

    app=Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    from .tasks.routes import tasks_bp

    app.register_blueprint(tasks_bp, url_prefix="/api/tasks")

    with app.app_context():
        db.create_all()

    return app