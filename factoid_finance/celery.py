import os
from celery import Celery
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'factoid_finance.settings')

app = Celery('factoid_finance')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'screen_stocks': {
        'task': 'analysis.tasks.screen_stocks',
        'schedule': datetime.timedelta(days=1),
    },
}
