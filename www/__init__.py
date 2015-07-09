from flask import Flask
#from config import config
import os

# Creates our Flask application.
app = Flask(__name__)
#config_name = os.getenv('FLASK_CONFIG') or 'default'
#app.config.from_object(config[config_name])
#config[config_name].init_app(app)

from celery import Celery

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


from www import views, errors




