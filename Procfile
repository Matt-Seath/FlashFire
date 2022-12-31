release: python manage.py migrate
web: gunicorn flashfire.wsgi
worker: celery -A flashfire worker