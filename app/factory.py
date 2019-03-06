from flask import Flask
import os
from .celery_utils import init_celery

PKG_NAME = os.path.dirname(os.path.realpath(__file__)).split("/")[-1]

def create_app(app_name=PKG_NAME, **kwargs):
    app = Flask(app_name)
    if kwargs.get("celery"):
        init_celery(kwargs.get("celery"), app)
    from app.all import bp
    app.register_blueprint(bp)
    return app
