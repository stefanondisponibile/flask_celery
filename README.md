# flask_celery
Run Flask with Celery.

Read [Medium article](https://medium.com/@frassetto.stefano/flask-celery-howto-d106958a15fe) for more.

## Set up.

You'll maybe want to create a new environment, if you're using `conda` you can do the following:

```bash
conda create --name fc --no-default-packages python=3.6.7
conda activate fc
pip install -r requirements.txt
```

## Running the example.

### 1. Set up redis.
First off, make sure to have `redis` running on `0.0.0.0:6379`. If you're using docker you may want to:

```bash
docker run --name some-redis -d redis
```

### 2. Start a celery worker.
You'll need a worker to get things done, run the following command in a separate terminal tab:

```bash
celery worker -A celery_worker.celery --loglevel=info --pool=solo
```

### 3. Start the app.

Open a new terminal tab and start the app:

```bash
python run.py
```

### 4. Try it!
On your browser, go to: `http://localhost:5000/flask_celery_howto.txt/it-works!`
