from __future__ import absolute_import

from celery import shared_task
from constance import config


@shared_task
def check_urls():
    if config.CHECK_URLS is False:
        return
    from .models import Url
    for url in Url.objects.all():
        url.check_url()
