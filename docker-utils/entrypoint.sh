#!/bin/bash

set -eoux pipefail

if [ "$1" == 'init' ]; then
    echo "Run Migrations"
    ${SITE_DIR}/env/bin/python ${SITE_DIR}/proj/manage.py migrate
    ${SITE_DIR}/env/bin/python ${SITE_DIR}/proj/manage.py collectstatic
elif [ "$1" == 'manage' ]; then
    shift
    echo "Manage.py $@"
    ${SITE_DIR}/env/bin/python ${SITE_DIR}/proj/manage.py $@
else
    exec "$@"
fi
