
# DOCKER COMPOSE

    Build and start the app:

        docker-compose up
        # Or to rebuild
        docker-compose up --build

        # migrate and collectstatic
        docker-compose run app init

        # create admin user
        docker-compose run app manage createsuperuser

    Other helpful commands

        # enter db
        docker-compose run app manage dbshell

        # enter bash shell
        docker-compose run app /bin/bash

        # stop everything
        docker-compose stop

        # stop everything, destroy containers, and volumes
        docker-compose down

    Override the default docker compose variables

        # vim docker-compose.override.yml
        version: '2'
        services:
            web:
              ports:
                - 8000:80
