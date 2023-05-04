import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')
# we are setting the environmetal variable(DJANGO_SETTINGS_MODULE) to this settings (storefront.settings)

celery = Celery('storefront')
celery.config_from_object('django.conf:settings', namespace='CELERY')
# new sttings added to connect to redis
celery.autodiscover_tasks()
# tasks in task folder, by calling this will run the tasks