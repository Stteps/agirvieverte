FROM python:3.10-slim

# ENVIRONMENT VARIABLES
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# CREATING GROUP AND USER FOR SETTING APPROPRIATE PERMISSIONS OVER THE APP
# Note: Some programs require home dir write access, so we create a home dir for the user
RUN addgroup --system --gid 1001 app  \
    && adduser --system --ingroup app --uid 1001 --home=/home/app app

# INSTALLING OS-LEVEL DEPENDENCIES
# Note: We install dependencies then clean the install to reduce image size
# Note: build-essential is used for building python packages
# Note: libpq-dev includes Postgre's client (psycopg2) dependencies
# Note: procps is used for celery autoreload management command
# Note: git is used for git-hooks
# Note: psycopg2 is Postgre's python client
RUN apt-get update && apt-get install -y -q --no-install-recommends \
  build-essential \
  libpq-dev \
  procps \
  git \
  gettext \
  && pip install --no-cache-dir psycopg2 \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# SOURCE CODE DIRECTORY AND BASE PATH
WORKDIR /code/
USER root
# WE CREATE A MEDIA FOLDER FOR MEDIA FILES (STATIC FILES ARE SERVED SEPARATLY IN DEV)
RUN mkdir -p /var/www/media/ && chown -R app:app /var/www/media/

# INSTALLING PYTHON DEPENDENCIES
COPY --chown=app:app requirements/ requirements/
RUN pip install --no-cache-dir -r requirements/local.txt

# CONTAINER ENTRYPOINT: WAITS FOR THE DATABASE TO BE READY
# Note: Entrypoint commands are run before every commands run in the container
COPY --chown=app:app docker/development/app/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
# PYTHON DEV SERVER COMMAND SCRIPT
COPY --chown=app:app docker/development/app/start-dev-server.sh /usr/local/bin/start-dev-server.sh
RUN chmod +x /usr/local/bin/start-dev-server.sh
# CELERY WORKER COMMAND SCRIPT
COPY --chown=app:app docker/development/app/start-celery-worker.sh /usr/local/bin/start-celery-worker.sh
RUN chmod +x /usr/local/bin/start-celery-worker.sh

RUN chown -R app:app /code/

# WE LAUNCH THE APP AS USER 'app'
USER app
ENTRYPOINT ["entrypoint.sh"]
CMD ["start-dev-server.sh"]
