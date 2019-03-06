from celery import Celery

def make_celery(app_name=__name__):
    backend = "redis://localhost:6379/0"
    broker = backend.replace("0", "1")
    return Celery(app_name, backend=backend, broker=broker)

celery = make_celery()
