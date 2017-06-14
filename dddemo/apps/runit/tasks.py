from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task(name='dddemo.add')
def add(x, y):
    return x + y
