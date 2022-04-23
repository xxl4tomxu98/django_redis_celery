    Django creates a task (Python function) and tells Celery to add it to the queue. Celery puts that task into Redis (freeing Django to continue working on other things). On a separate server, Celery runs workers that can pick up tasks. Those workers listen to Redis. When the new task arrives, one worker picks it up and processes it, logging the result back to Celery

    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install wheel
    pip install django
    pip install celery
    pip install redis

    django-admin startproject proj .
    python manage.py migrate
    python manage.py runserver

    add this line to add redis as celery broker:
    `CELERY_BROKER_URL = 'redis://localhost:6379'`

    python manage.py shell
    >>> from proj.celery import debug_task
    We use .delay() to tell Celery to add the task to the queue.

    We got back a successful AsyncResult — that task is now waiting in Redis for a worker to pick it up!
    >>> debug_task.delay() (should see `<AsyncResult: c6ef74b9-4c03-402a-b1db-9e2adbf52f75>`)

    `celery -A proj.celery worker --loglevel=info`

    `celery -A proj worker -l info`  (Test that the Celery worker is ready to receive tasks:)
    `celery -A proj beat -l info`    (Kill the process with CTRL-C. Now, test that the Celery task scheduler is ready for action:)