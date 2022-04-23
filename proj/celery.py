from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
# tells Celery to automatically discover a file called tasks.py in all of our Django apps.
app.autodiscover_tasks()
# celery will look for task.py files in apps but here is testers
# This simple task just prints all the metadata about the request when the task is received
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))