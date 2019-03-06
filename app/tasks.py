from app import celery

@celery.task()
def make_file(fname, content):
    with open(fname, "w") as f:
        f.write(content)
