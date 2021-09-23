#!/bin/bash

# Install new requirements
echo "INSTALL NEW REQUIREMENTS"
pip install -r requirements.txt

# Create static folder if not exists to avoid error
mkdir -p static
# STATIC_DIR="$(pwd)/static/"
# if [! -d "$STATIC_DIR" ]; then
#   echo "CREATING STATIC FILES DIRETORY"
# fi

# Collect static files
echo "COLLECT STATIC FILES"
python manage.py collectstatic --noinput

# Apply database migrations
echo "MAKING MIGRATIONS"
python manage.py makemigrations

echo "APPLY DATABASE MIGRATIONS"
python manage.py migrate

# if [ ${DEBUG} == True ]
# then
#     # Running Tests
#     echo "RUNING TESTS"
#     pytest
#     #TODO : stop database test after tests
# fi

# Start server
echo "STARTING SERVER"
python manage.py runserver 0.0.0.0:8000