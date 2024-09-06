#!/bin/bash

# Wait for PostgreSQL to be available.
check_postgres() {
  PGPASSWORD=$PGPASSWORD psql -h "$PGHOST" -U "$PGUSER" -d "$PGDATABASE" -c '\q' >/dev/null 2>&1
}
until check_postgres; do
  >&2 echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done
>&2 echo "PostgreSQL is up - continuing..."

#python manage.py collectstatic --no-input
python manage.py migrate --no-input
python -m gunicorn asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
