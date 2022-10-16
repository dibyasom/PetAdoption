#!/bin/bash

if [ "$DEBUG" == "True" ]; then
    sleep 15
fi

# As we are using S3, takes 30-60 to load static. Not needed.
# python3 manage.py collectstatic --no-input
python3 manage.py migrate

if [ "$DEBUG" == "True" ]; then
    python3 manage.py runserver 0.0.0.0:8080
else
    NEW_RELIC_CONFIG_FILE=newrelic_back.ini newrelic-admin run-program mod_wsgi-express start-server vmps_backend/wsgi.py \
  --with-newrelic \
  --port 8080 \
  --threads 30 \
  --user app --group app \
  --limit-request-body 4294967296 \
  --log-level info --log-to-terminal \
  --locale C.UTF-8
fi