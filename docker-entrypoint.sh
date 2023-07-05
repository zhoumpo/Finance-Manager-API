#/bin/sh

echo "Migrate database"
python manage.py migrate --noinput

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Starting server"
gunicorn finance_manager_api.asgi:application -b :8000 -w 2 --worker-class uvicorn.workers.UvicornWorker