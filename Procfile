web: sh -c "python manage.py migrate --noinput && python manage.py ensure_admin && gunicorn backend_config.wsgi:application --bind 0.0.0.0:$PORT"
