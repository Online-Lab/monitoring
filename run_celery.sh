#!/bin/sh

sleep 10
cd src
# run Celery worker for our project myproject with Celery configuration stored in Celeryconf
celery worker -A main -Q default -n default@%h
