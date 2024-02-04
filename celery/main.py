from config import *

import os
from logging import info

from celery import Celery
from requests import post


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


@celery.task(name="send_data")
def send_data(name, phone):
    text = f'Новый пользователь\n{name}: {phone}'
    apiURL = f'https://api.telegram.org/bot{API_KEY}/sendMessage'
    for user in USERS:
        try:
            response = post(apiURL, json={'chat_id': user, 'text': text})
        except Exception as e:
            print(e)
    return True