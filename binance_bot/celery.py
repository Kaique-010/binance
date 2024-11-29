from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Define o nome do projeto Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'binance_bot.settings')

# Cria a instância do Celery
app = Celery('binance_bot')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Celery está funcionando corretamente!')
