#!/bin/sh

# NOTE: This shell script is intended to be used inside a docker container.
# Running this script outside a docker container may lead to problems since
# it is not activating any virtualenv. It uses the default Python from the system.

pip install -r requirements.txt --require-hashes
python manage.py collectstatic --noinput