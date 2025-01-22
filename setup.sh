#!/bin/bash

# Apply database migrations

echo "Applying database migrations..."

python manage.py makemigrations

python manage.py migrate

# Start the Django development server

echo "Starting server..."

exec python manage.py runserver 0.0.0.0:8000
