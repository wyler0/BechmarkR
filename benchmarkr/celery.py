import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "benchmarkr.settings")
app = Celery("benchmarkr")
app.config_from_object(settings, namespace="CELERY")
app.autodiscover_tasks()

from celery import shared_task

import logging
logger = logging.getLogger('main_logger')

@shared_task(bind=True)
def test_celery(self, **kwargs):
    logger.debug("Celery is working")

