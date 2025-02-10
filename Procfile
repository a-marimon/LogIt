web: gunicorn api.wsgi --log-file - --worker-tmp-dir /dev/shm --timeout 120
#web: daphne -u /tmp/daphne.sock api.asgi:application
release: python manage.py collectstatic --no-input
release: python manage.py migrate