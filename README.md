# Agirvieverte.com
These sources contain all the code necessary to build and start the web app.

## Architecture
-  **app/**: Backend code (Django)
-  **config/** App config files
-  **frontend/**: Frontend code (React, buit with webpack)
-  **requirements/**: Python requirements
-  **docker**: Docker configuration files

## Installation
### Production (server)
For usage in production, you should follow these 2 steps in the `docker/production/` folder to deploy the app:
- First, load the docker images into the local docker context, by executing the `load_local_docker_images.sh` script, for example in Debian: `/bin/sh load_local_docker_images.sh`. If the docker images are not available in the `.tar` files, and you have an Internet access you can build them by running:
    - `docker build -f app/Dockerfile -t agirvieverte-app:latest ../../` for the app
    - `docker build -f reverse-proxy/Dockerfile -t agirvieverte-reverse-proxy:latest ../../` for the reverse proxy server
    - `docker pull postgres:15-alpine` for the database cluster
    - `docker pull redis:7-alpine` for the message broker
    - then, run the `save_local_docker_images.sh`
- Then, run `docker compose up -d`
- You can also uncomment the `build:` block in the `compose.yaml` files and run `docker compose up --build -d` (equivalent of the 2 previous steps)

You can then access the app at `http://<your_server_ip_or_domain_name>`

### Development (local)
To launch a local development version of Agirvieverte.com, go to the `docker/development/` folder and execute the following command:
```
docker compose up --build
```

You'll need a user account to use the app. To create a default superuser account, you can either:
- In the app container (you can get into the app container bash with the folowing command: `docker compose exec app bash`), type in the `python manage.py createsuperuser`
- Use the following command: `docker compose exec app python manage.py createsuperuser`

You can access the app at `0.0.0.0:8000`
