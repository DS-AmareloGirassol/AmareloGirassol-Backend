#!/bin/bash

cat scripts/seed_user.py | ./manage.py shell
cat scripts/seed_subject.py | ./manage.py shell
