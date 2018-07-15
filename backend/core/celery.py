from __future__ import absolute_import, unicode_literals

import os

import django
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()
app = Celery(app='core', backend='amqp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

