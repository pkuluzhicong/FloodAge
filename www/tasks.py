from floodage import Floodage

from celery import Celery

from flask import Flask

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

floodage = Floodage(10,18)

app = Flask(__name__)

app.config.update(
	CELERY_BROKER_URL='redis://localhost:6379',
	CELERY_RESULT_BACKEND='redis://localhost:6379'
	)
celery = make_celery(app)

@celery.task()
def activate(position,name):
	floodage.activate(position,name)

@celery.task()
def update():
	floodage.update()

@celery.task()
def query_city(position):
	floodage.query_city(position)

