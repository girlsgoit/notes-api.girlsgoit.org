#!/usr/bin/env bash
python manage.py migrate
sleep 2m
python manage.py createadmin